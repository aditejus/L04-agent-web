# Starting today? Set up here (about five minutes, all free)

This folder, `first-agent`, is a small working agent that reads three notes. The video "Give Your
AI Agent the Internet in 5 Simple Steps" starts from it. Do these five things once, then follow the
video from step 2.

**Mac users:** wherever these steps say `python`, type `python3`. Wherever they say `pip`, type `pip3`.

1. **Python** (3.10 or newer). Install it from python.org. On Windows, tick "Add to PATH" during the
   install.
2. **VS Code**, the free editor. Install it from code.visualstudio.com. Open it once.
   **Git**, the free tool VS Code uses to fetch code, from git-scm.com: run the installer with every
   default. Then, in VS Code, press Ctrl+Shift+P (Mac: Cmd+Shift+P), type `Git: Clone`, paste
   `https://github.com/aditejus/L03-first-ai-agent.git`, choose a folder, and click Open when it asks.
   (If you unzipped this download instead, open this `first-agent` folder with File, Open Folder.)
3. **The terminal**, the place where we type commands. In VS Code open the Terminal menu and choose
   New Terminal. A panel opens at the bottom, already inside this folder. Check Python is there:

   ```
   python --version
   ```

   You should see `Python 3.` and a number, 10 or higher. If you see `'python' is not recognized` or
   `Python was not found`: install Python again with "Add to PATH" ticked, then close VS Code and
   open it again.
4. **Two packages**, one line:

   ```
   pip install google-genai python-dotenv
   ```

   It ends with `Successfully installed ...`.
   - If Windows says `Program 'pip.exe' failed to run: An Application Control policy has blocked
     this file` (Windows 11 with Smart App Control on), type this instead, and use it every time
     these steps say `pip`: `python -m pip install google-genai python-dotenv`.
   - If Python later says `No module named 'google'`, run the same line:
     `python -m pip install google-genai python-dotenv`.
5. **A free key**, which is like a password: it tells Google the requests come from you. In your
   browser open aistudio.google.com and sign in with a Google account. Click "Get API key", then
   "Create API key", and copy the key. No card is asked for. Do not click "Set up billing" unless
   you mean to pay.

   In VS Code, in the file list on the left, click New File and name it `.env`. That is a dot, then
   `env`: nothing before the dot and nothing after. Put one line in it and save:

   ```
   GEMINI_API_KEY=paste-your-key-here
   ```

   No spaces, no quotes. Never put the key in the code, and never share the `.env` file.

## Check it works

```
python agent.py
```

It prints each tool call as it happens, then an answer about Tuesday's note: invoice 2231, 4,850
rupees. Your wording will differ. If nothing appears for a while, wait: a call can take from a few
seconds to a couple of minutes. If nothing appears for more than five minutes, press Ctrl + C: the
day's free requests are probably used up, and it will work again tomorrow.

That is the whole setup. Now go to step 2 of the video.

The finished code from today's video is in the other folder, `first-agent-web`, for comparing with
what you typed.
