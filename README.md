# Cave

A short pixel-art visual novel inspired by the Nickajack Cave rescue, created with Ren’Py for a Creative Coding university project.

**Creator:** Ziqi Yin  
**Language:** English  
**Estimated playtime:** Around 10 minutes

# About

Follow Buddy and Dennis as they help coordinate the search for a missing diver. Through conversations, choices and flashbacks, players gradually discover what happened inside the cave.

This game is a creative adaptation. Dialogue, characters and events may differ from historical accounts.

#Download and Play

[Download Cave](https://github.com/ziqiyin-code/cave/releases/tag/v1.0)

#Windows

1. Open the release page above.
2. Under **Assets**, download the desktop game ZIP uploaded with the release.
3. Extract the entire ZIP.
4. Open the game application (`.exe`) inside the extracted folder.
5. Keep all included files and folders together.

You do not need to install Ren’Py to play the desktop build.

**Note:** GitHub’s automatic “Source code” downloads contain the repository files. Choose the uploaded desktop game ZIP to play.

# Controls

- **Left click / Space:** Advance dialogue.
- **Click an option:** Make a choice.
- **Esc:** Open the game menu.
- Use the game menu to save, load and adjust sound settings.


# Repository Files

- `script.rpy` — Main story script, including dialogue, choices, variables and character display logic. Click this file on GitHub to read the code.
- `game.zip` — An additional archive included in this repository.
- `README.md` — Project information and instructions.
- **Releases** — Downloadable game builds.

# Code Features

- `menu` presents player choices.
- Variables record earlier decisions, and `if` statements select later dialogue.
- Character callbacks update `current_speaker`.
- `ConditionSwitch` uses this value to keep the speaking character bright and darken other displayed characters.
- Image transitions and audio help establish atmosphere.


# Credits

- **Development and adaptation:** Ziqi Yin
- **Engine:** Ren’Py
- **Artwork:** Original artwork and art direction by Ziqi Yin, with ChatGPT-assisted image generation and editing.
- **Audio:** Sound assets sourced from Pixabay, alongside a self-recorded voice effect.
- **Code reference:** The speaker-highlighting feature was adapted from a community-shared example.https://www.bilibili.com/video/BV1sc411m7Cf
