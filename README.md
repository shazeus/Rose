# Aurelia

<p align="center">
  <img width="160" height="160" alt="Aurelia logo" src="assets/icon.png">
</p>

<p align="center">
  <b>Windows-first League of Legends skin workflow, rebuilt around the Aurelia fork.</b>
</p>

<p align="center">
  <a href="https://github.com/shazeus/Aurelia/releases/latest"><img alt="Windows installer" src="https://img.shields.io/badge/Installer-Windows-f5b000?style=flat-square"></a>
  <a href="https://github.com/shazeus/Aurelia/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/shazeus/Aurelia?style=flat-square&label=release"></a>
  <a href="https://github.com/shazeus/Aurelia/releases/latest"><img alt="Downloads" src="https://img.shields.io/github/downloads/shazeus/Aurelia/total?style=flat-square&label=downloads"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-6f38d6?style=flat-square"></a>
</p>

---

Aurelia is a fork of Rose focused on a cleaner Windows install, a fork-owned update source, and a more polished client-facing identity. It keeps the core local skin workflow intact while updating the public packaging, updater target, installer metadata, and visual branding for this repository.

The app runs from the Windows tray, talks to the League Client through the local LCU API, installs Pengu Loader plugins, and applies local visual assets during the normal champion-select and loading flow.

## Download

Get the latest Windows build from:

```txt
https://github.com/shazeus/Aurelia/releases/latest
```

Release assets follow the same style as Rose:

```txt
Aurelia_Setup_1.3.1.exe
update_package_1.3.1.zip
```

Use the setup executable for a normal install. The update package is used by Aurelia's built-in updater.

## What Changed In This Fork

- New Aurelia logo across the README, app icon, tray icons, installer icon, and in-client Jade logo asset.
- Windows-only release workflow that builds the PyInstaller app, creates the Inno Setup installer, and publishes updater ZIPs.
- Updater defaults to `shazeus/Aurelia` releases instead of upstream release feeds.
- Installer metadata now points to this fork and uses versioned setup filenames.
- README rewritten around the current fork, Windows setup, update assets, and safety boundaries.
- Existing runtime behavior remains aligned with the Rose/Aurelia codebase; packaging and identity are the main fork-level changes.

## Features

- System tray app for local League Client workflows.
- LCU integration for champion select, phase changes, and skin selection state.
- Pengu Loader plugin bundle for client UI features.
- Random skin, chroma wheel, forms wheel, historic mode, party mode, and settings panel plugins.
- Local update flow through GitHub Releases.
- Windows installer with Start Menu entry, optional desktop shortcut, uninstall support, and admin launch.

## Requirements

- Windows 10 or Windows 11.
- League of Legends installed.
- Administrator permission when launching the installed app.
- A user-provided `cslol-dll.dll` if the local injection workflow requires it.

## DLL Notice

Aurelia does not distribute `cslol-dll.dll`. If your workflow needs that file, you must provide your own authorized copy and place it when the app asks for it. This repository does not bypass private access controls or ship restricted third-party binaries.

## Install

1. Open the latest release.
2. Download `Aurelia_Setup_VERSION.exe`.
3. Run the installer as administrator.
4. Launch Aurelia from the Start Menu or desktop shortcut.
5. Keep League closed while installing or uninstalling.

## Auto Update

Aurelia checks this repository by default:

```txt
https://api.github.com/repos/shazeus/Aurelia/releases/latest
```

For custom testing, override the updater target:

```powershell
$env:AURELIA_RELEASE_REPO = "owner/Aurelia"
```

Or provide a full API URL:

```powershell
$env:AURELIA_RELEASE_API = "https://api.github.com/repos/owner/Aurelia/releases/latest"
```

## Build From Source

Install Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Build the Windows app:

```powershell
python build_pyinstaller.py
```

Create the installer:

```powershell
python create_installer.py
```

Or run the full Windows build:

```powershell
python build_all.py
```

Create release assets after a successful build:

```powershell
python scripts/package_release.py 1.3.1
```

## Release

Create a version tag:

```bash
git tag 1.3.1
git push origin 1.3.1
```

GitHub Actions publishes:

```txt
release/Aurelia_Setup_1.3.1.exe
release/update_package_1.3.1.zip
```

## Project Layout

```txt
main.py                         App entry point
config.py                       App version and global constants
Aurelia.spec                    PyInstaller build definition
installer.iss                   Inno Setup installer definition
build_all.py                    Windows executable + installer build
launcher/update/                GitHub release updater
Pengu Loader/plugins/           League Client plugin bundle
assets/                         App icons and UI assets
```

## Credits

Aurelia is based on the Rose project by Alban1911:

```txt
https://github.com/Alban1911/Rose
```

This fork is maintained at:

```txt
https://github.com/shazeus/Aurelia
```

## Legal

This project is not endorsed by Riot Games and is not affiliated with Riot Games. Riot Games and League of Legends are trademarks or registered trademarks of Riot Games, Inc.

Use local skin tools responsibly and only where you understand the risk. You are responsible for your own client setup and files.

## License

[MIT](LICENSE)
