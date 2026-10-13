"""Your first AI agent, in about 40 lines of Python, on the Gemini API free tier.

Steps 4 to 7 of the video live in this one file. Step 3 (one call, no tools) is step3_chat.py.
Run it from this folder:   python agent.py
The key is read from a .env file in this folder:   GEMINI_API_KEY=...   (never in the code)
"""
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()                             # step 2: the key comes from .env, not from the code
client = genai.Client()                   # the SDK reads GEMINI_API_KEY on its own
MODEL = "gemini-3.8-flash"                # free of charge on the free tier
NOTES = Path(__file__).parent / "notes"   # the small folder the agent may look at


# ---- step 4: the tools. The model never runs code. It asks us to, and we send back the result.
def list_files():
    names = sorted(p.name for p in NOTES.glob("*.txt"))
    return "\n".join(names) or "No .txt files found in the notes folder."


def read_file(name):
    path = NOTES / Path(name).name        # .name keeps it inside notes/
    return path.read_text(encoding="utf-8") if path.exists() else f"No file named {name}."


TOOLS = [
    {"type": "function", "name": "list_files",
     "description": "List the text files in the notes folder.",
     "parameters": {"type": "object", "properties": {}}},
    {"type": "function", "name": "read_file",
     "description": "Read one text file from the notes folder and return its contents.",
     "parameters": {"type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"]}},
]


def run_tool(name, args):
    print(f"   tool call -> {name}({args})", flush=True)   # step 7: the log
    return list_files() if name == "list_files" else read_file(**args)


# ---- step 5: the loop. This loop is the agent.
def agent(goal, max_turns=8):             # step 7: a hard stop, so it can never run forever
    interaction = client.interactions.create(model=MODEL, input=goal, tools=TOOLS)
    for turn in range(max_turns):
        calls = [s for s in interaction.steps if s.type == "function_call"]
        if not calls:                     # no more tool calls: the model has its answer
            return interaction.output_text
        results = []
        for c in calls:
            text = json.dumps(run_tool(c.name, c.arguments))
            results.append({"type": "function_result", "name": c.name, "call_id": c.id,
                            "result": [{"type": "text", "text": text}]})
        interaction = client.interactions.create(
            model=MODEL, tools=TOOLS, input=results,
            previous_interaction_id=interaction.id)        # how the model remembers
    return "Stopped: reached the turn limit."


# ---- step 6: give it a goal and watch it work.
if __name__ == "__main__":
    print(agent("Which of my notes mentions an invoice, and what is the amount? Check the files."))
