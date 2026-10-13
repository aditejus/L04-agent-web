# Starting today? Set up here (about ten minutes, all free)

These are the seven setup steps the video shows, in the same order. Do them once. If you already
have a thing, skip that step.

**Mac users:** wherever these steps say `python`, type `python3`.

1. **Python** (3.10 or newer). Install it from python.org. On Windows, tick "Add python.exe to PATH"
   before you click Install Now.
2. **VS Code**, the free editor. Install it from code.visualstudio.com, and open it once.
3. **Git**, the free tool VS Code uses to fetch code. Install it from git-scm.com: run the installer
   and keep every default.
4. **The code.** In VS Code press Ctrl+Shift+P (Mac: Cmd+Shift+P), type `Git: Clone`, and paste:

   ```
   https://github.com/aditejus/L03-first-ai-agent.git
   ```

   That is the address the video shows. (This repository's own address has the same starting files
   and also the finished code.) Choose a folder, and click Open when it asks. Then open the Terminal menu and choose New Terminal:
   a panel opens at the bottom, already inside the folder. That is where every command is typed.
   Check Python is there:

   ```
   python --version
   ```

   You should see `Python 3.` and a number, 10 or higher. If you see `'python' is not recognized` or
   `Python was not found`: close VS Code and open it again (it was open while Python installed), or
   install Python again with "Add python.exe to PATH" ticked.

   No Git? Use the green Code button on the repository's page, Download ZIP, unzip it, and open the
   folder with File, Open Folder.
5. **Two packages**, one line:

   ```
   python -m pip install google-genai python-dotenv
   ```

   It ends with `Successfully installed ...`. This is the form the video types. The shorter
   `pip install ...` does the same, but Windows 11 with Smart App Control on may refuse it with
   `Program 'pip.exe' failed to run: An Application Control policy has blocked this file`; the
   `python -m pip` form above is the fix.
6. **A free key**, which is like a password: it tells Google the requests come from you. In your
   browser open aistudio.google.com and sign in with a Google account. Click "Get API key", then
   "Create API key", and copy the key. No card is asked for. Do not click "Set up billing" unless
   you mean to pay.

   In VS Code, in the file list on the left, click New File and name it `.env`. That is a dot, then
   `env`: nothing before the dot and nothing after. Put one line in it and save:

   ```
   GEMINI_API_KEY=paste-your-key-here
   ```

   No spaces, no quotes. Never put the key in the code, and never share the `.env` file.
7. **Run it once.**

   ```
   python agent.py
   ```

   It prints each tool call as it happens, then an answer about Tuesday's note: invoice 2231, 4,850
   rupees. Your wording will differ. If nothing appears for a while, wait: a call can take from a few
   seconds to a couple of minutes. If nothing appears for more than five minutes, press Ctrl + C: the
   day's free requests are probably used up, and it will work again tomorrow.

That is the whole setup. Now follow the video from step 2: you will change `agent.py`. The finished
version is in the `finished/` folder, for comparing with what you typed.
