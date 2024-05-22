import omni.kit.menu.utils
from omni.kit.mainwindow import get_main_window


REMOVE_EDITOR_MENUS = {
    "Window/Layout/Save Layout...",
    "Window/Layout/Load Layout...",
    "Window/Layout/Quick Save",
    "Window/Layout/Quick Load",
    "Window/Viewport",
    "Window/Tools/Navigation",
    "Window/Activity Monitor",
    "Window/Property",
    "Window/Animation/Sequencer",
    "Window/Physics/Debug",
    "Window/Physics/Demo Scenes",
    "Window/Physics/Test Runner",
    "Window/Physics/Character Controller",
    "Window/Physics/Physics Settings",
    "Window/Physics/Settings",
    "Window/Utilities/Attribute Connection",
    "Window/Visual Scripting/Node Description Editor",
    "Window/ToolBar",
    "Window/Flow/Presets",
    "Window/Flow/Monitor",
    "Window/Particles/Editor",
    "Window/Particles/Templates",
    "Window/Particles/Samples",
    "Window/Particles/Tools",
    "Window/Extensions",
    "Window/New Viewport Window",
    "Rendering/Render Settings",
    "Help/Physics Scripting Manual",
    "Window/Warp/Scenes/Cloth",
    "Window/Warp/Scenes/Deform",
    "Window/Warp/Scenes/Particles",
    "Window/Warp/Scenes/Wave",
    "Window/Warp/Scenes/Browse",
    "Window/Warp/Help/Getting Started",
    "Window/Warp/Help/Documentation",
}


class MenuSetup:
    def __init__(self):
        # Use menu hook to hide most menu items in "Edit", "Create", "File"
        omni.kit.menu.utils.add_hook(self._menu_hook)

        # Remove editor menus
        self._remove_editor_menus()

        # Hide menubar
        main_menu_bar = get_main_window().get_main_menu_bar()
        main_menu_bar.visible = False


    def destroy(self):
        omni.kit.menu.utils.remove_hook(self._menu_hook)

    def _menu_hook(self, menu: dict):
        for key in menu:
            for item in menu[key]:
                item.show_fn = lambda: False

    def _remove_editor_menus(self):
        editor_menu = omni.kit.ui.get_editor_menu()
        for item in REMOVE_EDITOR_MENUS:
            editor_menu.remove_item(item)
