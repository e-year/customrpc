# Custom Discord Rich Presence

A simple Python script that sets a custom Rich Presence status ("Listening to...") on Discord, complete with custom text, artwork, a progress bar, and a clickable button.

![Type](https://img.shields.io/badge/type-Rich%20Presence-5865F2?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)

## What This Does

This script connects to your **local Discord desktop app** and sets a custom activity status, similar to how Spotify shows "Listening to..." with a progress bar. You can customize:

- The top and bottom text lines
- A large image (via an uploaded Art Asset)
- A progress bar with a custom duration
- Up to two clickable buttons (visible to others viewing your profile)

## Requirements

- Python 3.9+
- The [`pypresence`](https://pypi.org/project/pypresence/) library
- Discord **desktop app** — not the browser version (this won't work in-browser)
- A free Discord Application (for the Client ID)

Install the dependency:

```bash
pip install pypresence
```

## Setup

### 1. Create a Discord Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**, give it a name (this name appears next to "Listening to" / "Playing" in your status)
3. Copy the **Application ID** from the General Information page
4. Paste it into the `CLIENT_ID` variable in `self.py`

### 2. (Optional) Upload a custom image

1. In your application, go to **Rich Presence → Art Assets**
2. Upload an image and give it a key name (e.g. `los`)
3. Use that same key name in the `large_image` field in the script

> **Note:** Only static images (PNG/JPG) are supported — animated GIFs will only show a single frame.

### 3. Run the script

```bash
python self.py
```

If everything is set up correctly, your Discord status should update within a few seconds.

## Important Notes

- **Buttons never show on your own profile.** This is a Discord limitation, not a bug — ask a friend or check from a second account to confirm they're working.
- **App name changes can take a minute or two** to propagate to your live status after editing them in the Developer Portal.
- The elapsed/progress timer is fully controlled by Discord's client — it always displays in `mm:ss`, `h:mm:ss`, or `d:hh:mm:ss` format depending on duration. There's no way to force custom formatting in that specific field; use the `details`/`state` text fields instead if you want fully custom text.

## Troubleshooting: `DiscordNotFound` Error

If you get:

```
pypresence.exceptions.DiscordNotFound: Could not find Discord installed and running on this machine.
```

Discord is running, but the script can't find its IPC socket. This is common on **Flatpak** installs of Discord on Linux.

**Fix:**

```bash
ln -s /run/user/1000/app/com.discordapp.Discord/discord-ipc-0 /run/user/1000/discord-ipc-0
```

> Replace `1000` with your actual user ID if different (`id -u` to check).

This symlink resets every time Discord restarts, so you'll need to re-run this command after restarting Discord or rebooting.

If you're running the script from **VS Code's built-in terminal** and it's a Flatpak install, use this version instead (bridges through the host filesystem):

```bash
ln -s /run/host/root/run/user/1000/app/com.discordapp.Discord/discord-ipc-0 /run/user/1000/discord-ipc-0
```

Or simpler: just run the script from your regular system terminal instead of VS Code's integrated terminal.

## Disclaimer

This uses only your public Discord **Application ID**, not your account token, so it's safe to share/publish this code. Rich Presence is a supported, official Discord feature — this is not a self-bot or automation of your account.
