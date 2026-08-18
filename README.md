# Custom Discord Rich Presence (Windows)

A simple Python script that sets a custom Rich Presence status ("Listening to...") on Discord. It supports custom text, artwork, a progress bar, and a clickable button.

![Type](https://img.shields.io/badge/type-Rich%20Presence-5865F2?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Windows-0078D6?style=flat-square)

## What This Does

This script connects to your **local Discord desktop app** and sets a custom activity status, similar to how Spotify shows "Listening to..." with a progress bar. You can customize:

- The top and bottom text lines
- A large image (via an uploaded Art Asset)
- A progress bar with a custom duration
- Up to two clickable buttons (visible to others viewing your profile)

## Requirements

- Python 3.9+ (install from [python.org](https://www.python.org/downloads/) if you don't have it, and make sure to check **"Add python.exe to PATH"** during install)
- The [`pypresence`](https://pypi.org/project/pypresence/) library
- Discord **desktop app**. The browser version will not work.
- A free Discord Application (for the Client ID)

Install the dependency by opening **Command Prompt** or **PowerShell** and running:

```powershell
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

> **Note:** Only static images (PNG/JPG) are supported. Animated GIFs will only show a single frame.

### 3. Run the script

Make sure Discord is open and you're logged in, then run:

```powershell
python self.py
```

If everything is set up correctly, your Discord status should update within a few seconds.

## Important Notes

- **Buttons never show on your own profile.** This is a Discord limitation, not a bug. Ask a friend or check from a second account to confirm they're working.
- **App name changes can take a minute or two** to propagate to your live status after editing them in the Developer Portal.
- The elapsed/progress timer is fully controlled by Discord's client. It always displays in `mm:ss`, `h:mm:ss`, or `d:hh:mm:ss` format depending on duration. There's no way to force custom formatting in that specific field. Use the `details`/`state` text fields instead if you want fully custom text.

## Good News for Windows Users

Unlike Linux (particularly Flatpak installs of Discord), Windows generally doesn't need any extra setup for the script to find Discord. As long as the Discord desktop app is open and you're logged in, `pypresence` should connect automatically with no symlinks or workarounds needed.

## Troubleshooting: `DiscordNotFound` Error

If you get:

```
pypresence.exceptions.DiscordNotFound: Could not find Discord installed and running on this machine.
```

Try these in order:

1. **Make sure Discord is actually open and fully loaded**, not just installed. Check your system tray.
2. **Make sure you're logged in.** A Discord window sitting on the login screen won't expose the IPC connection.
3. **Restart Discord**, then run the script again.
4. **Check you're not running the Microsoft Store version of Discord alongside a separate installer version.** Having both installed can sometimes cause the wrong one to be detected. Uninstall one and stick to a single install.
5. **Run Command Prompt/PowerShell as Administrator** and try again. In rare cases, permission issues can block the local named pipe Discord uses for IPC on Windows.
6. **Check your antivirus or firewall isn't blocking local IPC.** Some overly aggressive security software blocks local named pipes. Temporarily disabling it to test can confirm whether this is the cause.

## Disclaimer

This uses only your public Discord **Application ID**, not your account token, so it's safe to share/publish this code. Rich Presence is a supported, official Discord feature. It is not a self-bot or automation of your account.
