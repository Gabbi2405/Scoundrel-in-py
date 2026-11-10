# Info
The Scoundrel rules are made by Zach Gage and Kurt Bieg I just wrote some code to play it on devices
# Todo
fare funzione select in Room 

#ideal folder struct
my_python_game/
│
├── assets/                     # All visual and audio game elements
│   ├── images/                 # Sprites, backgrounds, UI textures
│   ├── audio/                  # Background music (.mp3/ .ogg), SFX (.wav)
│   ├── fonts/                  # TrueType fonts (.ttf)
│   └── maps/                   # Tiled maps, levels (.json, .tmx)
│
├── src/                        # Main source code package
│   └── game_name/              # Using underscores for package naming
│       ├── __init__.py         # Makes the folder an importable package
│       ├── core/               # Foundational engine code
│       │   ├── __init__.py
│       │   ├── engine.py       # Main loop, delta time, state management
│       │   ├── settings.py     # Screen size, FPS, global constants
│       │   └── input.py        # Keyboard/mouse event routing
│       │
│       ├── entities/           # Domain-driven game objects
│       │   ├── __init__.py
│       │   ├── player.py
│       │   ├── enemy.py
│       │   └── bullet.py
│       │
│       ├── states/             # Game states (Menus, Levels, Game Over)
│       │   ├── __init__.py
│       │   ├── menu_state.py
│       │   └── play_state.py
│       │
│       └── utils.py            # Helpful math, raycasting, or color helpers
│
├── tests/                      # Unit testing modules (lives outside src)
├── .gitignore                  # Tells Git to ignore .venv/ and __pycache__/
├── main.py                     # Entry point (Keep this file as simple as possible)
├── README.md                   # Instructions, controls, and installation notes
└── pyproject.toml              # Modern configuration file / project metadata
