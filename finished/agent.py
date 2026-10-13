"""Video 2: the agent from video 1, now with the web. Two additions, both free, no extra installs:
a tool of our own that searches Wikipedia, and Google's built-in tool that reads a web page.

Run it from this folder:   python agent.py
The key is read from a .env file in this folder:   GEMINI_API_KEY=...   (never in the code)
"""
import json
import urllib.parse
import urllib.request
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.8-flash"
NOTES = Path(__file__).parent / "notes"


def list_files():
    names = sorted(p.name for p in NOTES.glob("*.txt"))
    return "\n".join(names) or "No .txt files found in the notes folder."


def read_file(name):
    path = NOTES / Path(name).name
    return path.read_text(encoding="utf-8") if path.exists() else f"No file named {name}."


# ---- new in video 2: a search tool of our own. Wikipedia answers for free, with no key.
def search_wikipedia(query):
    address = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "opensearch", "search": query, "limit": 3, "format": "json"})
    request = urllib.request.Request(address, headers={"User-Agent": "first-agent-tutorial/1.0"})
    reply = json.loads(urllib.request.urlopen(request, timeout=30).read())
    titles, links = reply[1], reply[3]
    return "\n".join(f"{t}: {u}" for t, u in zip(titles, links)) or "No results."


TOOLS = [
    {"type": "function", "name": "list_files",
     "description": "List the text files in the notes folder.",
     "parameters": {"type": "object", "properties": {}}},
    {"type": "function", "name": "read_file",
     "description": "Read one text file from the notes folder and return its contents.",
     "parameters": {"type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"]}},
    {"type": "function", "name": "search_wikipedia",
     "description": "Search Wikipedia. Returns up to three page titles with their web addresses.",
     "parameters": {"type": "object",
                    "properties": {"query": {"type": "string"}},
                    "required": ["query"]}},
    {"type": "url_context"},          # new in video 2: Google's built-in tool that reads a web page
]
OURS = {"list_files": list_files, "read_file": read_file, "search_wikipedia": search_wikipedia}


def run_tool(name, args):
    print(f"   tool call -> {name}({args})", flush=True)
    return OURS[name](**args)


def agent(goal, max_turns=8):
    interaction = client.interactions.create(model=MODEL, input=goal, tools=TOOLS)
    for turn in range(max_turns):
        for s in interaction.steps:               # the built-in tool runs at Google: we only log it
            if s.type == "url_context_call":
                print(f"   web page  -> {s.arguments}", flush=True)
        calls = [s for s in interaction.steps if s.type == "function_call"]
        if not calls:
            return interaction.output_text
        results = []
        for c in calls:
            text = json.dumps(run_tool(c.name, c.arguments))
            results.append({"type": "function_result", "name": c.name, "call_id": c.id,
                            "result": [{"type": "text", "text": text}]})
        interaction = client.interactions.create(
            model=MODEL, tools=TOOLS, input=results,
            previous_interaction_id=interaction.id)
    return "Stopped: reached the turn limit."


if __name__ == "__main__":
    # Step 4's goal, the vague one. Step 5 replaces it with the goal below, which names the source.
    # print(agent("What is the newest stable version of Python? Search Wikipedia, read the page "
    #             "you find, and answer in two sentences with the address of the page you read."))
    print(agent("What is the newest version of Python? Read https://www.python.org/downloads/ "
                "and answer in one sentence, with the address you read."))
