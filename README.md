# Give your AI agent the internet, in 5 simple steps

The code for the AdiTejus video (day 2 of learning AI). In its setup the video clones a small
starting agent, runs it once, and then adds about twenty lines: a search tool of our own
(Wikipedia, free, no sign-up) and Google's built-in tool that reads a web page (free on the free
tier). No card is needed anywhere.

## Start here

New computer, or starting today? The seven setup steps the video shows (Python, VS Code, Git, clone
the starting agent, the two packages, a free key, run it once) are written out, with their checks
and errors, in [START-HERE.md](START-HERE.md). Already set up? Go straight to step 2 below.

The address the video clones is the starting agent's own repository:

```
https://github.com/aditejus/L03-first-ai-agent.git
```

This repository has the same starting files at its top level, so cloning this one works just as
well, and it adds the finished code in `finished/`.

## What is in this repository

| File | What it is |
| --- | --- |
| `agent.py` | **Where you start:** a small working agent, about forty lines, that reads three notes. The video's five steps change this file. |
| `notes/` | Three sample notes the agent is allowed to read. |
| `requirements.txt` | The two packages to install. |
| `.env.example` | Shows what your own `.env` file must contain. |
| `START-HERE.md` | The setup, step by step. |
| `finished/` | **Where you end:** the finished `agent.py`, `test_search.py` and `read_page_fallback.py`, for comparing with what you typed. |
| `docs/step-card.pdf` | The five steps on one page. |

You need a `.env` file in this folder, next to `agent.py`, with one line in it:

```
GEMINI_API_KEY=paste-your-key-here
```

**Mac users:** wherever these steps say `python`, type `python3`.

## The steps

1. **What "the web" means for an agent.** Two abilities: find a page, then read it.
2. **A search tool of our own.** In `agent.py`: two `import urllib...` lines at the top, the
   `search_wikipedia` function, its entry in `TOOLS`, the `OURS` table, and the new last line of
   `run_tool`. Then make a file called `test_search.py` with the two lines the video shows, and run
   it:

   ```
   python test_search.py
   ```

   You should see a page title and its address within a second or two.
3. **The reading tool.** One line in `TOOLS`: `{"type": "url_context"},` and three lines in `agent`
   that print each page the model opens. There is nothing to run in this step: you see it work in
   step 4.
4. **A goal that needs the web.** The goal used in the video at this step:

   ```
   What is the newest stable version of Python? Search Wikipedia, read the page you find, and
   answer in two sentences with the address of the page you read.
   ```

   ```
   python agent.py
   ```

   You should see a `tool call -> search_wikipedia` line, a `web page ->` line, then the answer.

   In `finished/agent.py` that goal is the two lines near the bottom that start with `#`. To run it
   there, remove the `# ` from those two lines and put `# ` in front of the two lines below them.
5. **Trust, but check.** Open the address the agent gave, and open python.org/downloads. If they
   disagree, the agent was wrong. Then use the goal that is in `finished/agent.py`: it names the
   source.

To run the finished version without typing anything: `python finished/agent.py`.

## The errors you are most likely to see

| What you see | What to do |
| --- | --- |
| `NameError: name 'urllib' is not defined` | The two import lines at the top are missing or misspelled. |
| `URLError` or `getaddrinfo failed` | Your internet connection dropped. Check it and run again. |
| `SyntaxError` or `IndentationError` | A typing slip on the line Python names. Compare it with `finished/agent.py`. |
| `NameError: name 'OURS' is not defined` | The `OURS = {...}` line under the `TOOLS` list is missing. |
| `NameError: name 'search_wikipedia' is not defined` | The function is missing, or its name is spelled differently. |
| `TypeError: read_file() got an unexpected keyword argument 'query'` | The last line of `run_tool` was not changed to `return OURS[name](**args)`. |
| `KeyError` with a tool's name | That name is missing from the `OURS` line, or spelled differently there. |
| `No API key was provided` | The `.env` file must be in this folder, next to `agent.py`, named exactly `.env`. |
| `Program 'pip.exe' failed to run: An Application Control policy has blocked this file` | Windows 11 with Smart App Control on refuses `pip.exe`. Use the form the video types: `python -m pip install google-genai python-dotenv`. |
| `429` ... `Rate limit exceeded` | Read the message: it names the limit. "per minute": wait a minute and run again. "per day": come back tomorrow (it says in how many hours). |
| Nothing for more than five minutes | Press Ctrl+C. Usually the daily limit: the program sometimes waits in silence instead of showing the message. |
| `402` ... `prepayment credits are depleted` | Billing was switched on for the project. Use a new project with billing off. |

## The free limits

On my account the free tier allows 5 requests a minute and 20 a day for this model. One run of the
step 4 goal used about 5 requests. The step 5 goal used 1. `test_search.py` uses none. Your own
limits are in Google AI Studio, under Rate Limit.

**Do not click "Set up billing" to get past a limit, unless you mean to pay.**

Google's own Search tool is not on the free tier, which is why this video does not use it.

## Three honest notes

- The reading tool opens public pages only. It cannot read pages behind a login or a paywall.
- An answer with a link on it can still be wrong. Open the link. Name the source in the goal.
- On the free tier Google may use what you send to improve its products. Practise with public pages
  and sample notes, not private documents.

## If the built-in reader stops working

Google marks the combination of its built-in tools with your own as a Preview feature, so it may
change. `finished/read_page_fallback.py` is a page reader of our own. Test it alone first (free):

```
python finished/read_page_fallback.py
```

To use it in `agent.py`:

1. Copy its three `import` lines and its `read_page` function into `agent.py`.
2. In `TOOLS`, replace the line `{"type": "url_context"},` with an entry shaped like the one for
   `search_wikipedia`: the name `read_page`, the description "Read one public web page and return
   its text.", and one input called `address`.
3. Add `"read_page": read_page` to the `OURS` line.

It is cruder than the built-in reader: it keeps the first 3,000 characters of the page's text. I
tested the function on its own. I have not needed it with the agent yet.

## Make it yours

Change the question. Name the page you trust in the goal. Ask the agent to compare one of your notes
with a web page.

The presenter in the video is an AI avatar with an AI voice; the code and every run shown are real.
