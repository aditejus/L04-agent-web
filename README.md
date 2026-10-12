# Give your AI agent the internet, in 5 simple steps

The code from the video. It is the agent from video 1 with about twenty new lines: a search tool of
our own (Wikipedia, free, no sign-up) and Google's built-in tool that reads a web page (free on the
free tier). No card is needed anywhere.

## Start here

New computer, or starting today? The seven setup steps the video shows (Python, VS Code, Git, clone
the starting agent, the two packages, a free key, run it once) are written step by step, with their
checks and errors, in [START-HERE.md](START-HERE.md). Already set up? Go straight to step 2 below.

The starting agent (what the video clones in setup 4): https://github.com/aditejus/L03-first-ai-agent
This repository is the finished code of the video, for comparing with what you typed.

## What is in this folder

| File | What it is |
| --- | --- |
| `agent.py` | The finished agent: video 1's file plus the new lines from steps 2, 3 and 5. |
| `test_search.py` | Step 2: tests the search tool alone. Free: it never calls the model. |
| `notes/` | The three sample notes from video 1. |
| `read_page_fallback.py` | Only for the day Google's built-in reader stops working. See the end. |
| `requirements.txt` | The two packages from video 1. Nothing new to install. |
| `.env.example` | Shows what your own `.env` file must contain. |

## Before you start

This video builds on the small agent in the `first-agent` folder of this download. You need its
setup: Python 3.10 or newer, VS Code, the two packages, a free Gemini key, and a `.env` file with one
line in it:

```
GEMINI_API_KEY=paste-your-key-here
```

Start in the other folder of this download, `first-agent`: its `START-HERE.md` lists the five setup
steps (about five minutes, all free). If you already have a `first-agent` folder from before, keep
working in it. This folder, `first-agent-web`, is the
finished code, for comparing with what you typed.

**Mac users:** wherever these steps say `python`, type `python3`.

## The steps

1. **What "the web" means for an agent.** Two abilities: find a page, then read it.
2. **A search tool of our own.** In `agent.py`: two `import urllib...` lines at the top, the
   `search_wikipedia` function, its entry in `TOOLS`, the `OURS` table, and the new last line of
   `run_tool`. Then test it alone:

   ```
   python test_search.py
   ```

   You should see a page title and its address within a second or two.
3. **The reading tool.** One line in `TOOLS`: `{"type": "url_context"},` and three lines in `agent`
   that print each page the model opens.
4. **A goal that needs the web.** The goal used in the video at this step:

   ```
   What is the newest stable version of Python? Search Wikipedia, read the page you find, and
   answer in two sentences with the address of the page you read.
   ```

   ```
   python agent.py
   ```

   You should see a `tool call -> search_wikipedia` line, a `web page ->` line, then the answer.

   In this download that goal is the two lines near the bottom of `agent.py` that start with `#`.
   To run it, remove the `# ` from those two lines and put `# ` in front of the two lines below them.
5. **Trust, but check.** Open the address the agent gave, and open python.org/downloads. If they
   disagree, the agent was wrong. Then use the goal that is in this download's `agent.py`: it names
   the source.

## The errors you are most likely to see

| What you see | What to do |
| --- | --- |
| `NameError: name 'urllib' is not defined` | The two import lines at the top are missing or misspelled. |
| `URLError` or `getaddrinfo failed` | Your internet connection dropped. Check it and run again. |
| `SyntaxError` or `IndentationError` | A typing slip on the line Python names. Compare it with this download. |
| `NameError: name 'OURS' is not defined` | The `OURS = {...}` line under the `TOOLS` list is missing. |
| `NameError: name 'search_wikipedia' is not defined` | The function is missing, or its name is spelled differently. |
| `TypeError: read_file() got an unexpected keyword argument 'query'` | The last line of `run_tool` was not changed to `return OURS[name](**args)`. |
| `KeyError` with a tool's name | That name is missing from the `OURS` line, or spelled differently there. |
| `No API key was provided` | The `.env` file must be in this folder, next to `agent.py`, named exactly `.env`. |
| `Program 'pip.exe' failed to run: An Application Control policy has blocked this file` | Windows 11 with Smart App Control on refuses `pip.exe`. Type `python -m pip install google-genai python-dotenv` instead, and use `python -m pip` wherever these steps say `pip`. |
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
change. `read_page_fallback.py` is a page reader of our own. Test it alone first (free):

```
python read_page_fallback.py
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
