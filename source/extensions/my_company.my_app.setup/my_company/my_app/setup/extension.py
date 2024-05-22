import asyncio
import omni.ext
import omni.kit.app

from pxr import Usd, Sdf
from .menu_setup import MenuSetup

class CreateSetupExtension(omni.ext.IExt):
    """Create Final Configuration"""
    def on_startup(self, ext_id):
        """setup the window layout, menu, final configuration of the extensions etc"""
        print("[my_company.my_app.setup] MyExtension startup")
        import omni.usd
        import omni.ui
        import omni.timeline
        import carb
        import carb.settings

        self._settings = carb.settings.get_settings()

        # this is a work around as some Extensions don't properly setup their default setting in time
        # self._set_defaults()

        # adjust couple of viewport settings
        # self._settings.set("/app/viewport/grid/enabled", False)
        # self._settings.set("/app/viewport/outline/enabled", False)
        # self._settings.set("/app/viewport/boundingBoxes/enabled", False)
        # self._settings.set("/persistent/app/viewport/displayOptions", 1)

        self._menu_setup = MenuSetup()

        manager = omni.kit.app.get_app().get_extension_manager()
        usd_file_path = manager.get_extension_path_by_module("my_company.my_app.setup")+"/data/DefaultStage.usda"

        async def _open_usd(usd_file_path):
            await omni.usd.get_context().open_stage_async(usd_file_path)
            carb.log_warn(f"Stage opened from {usd_file_path}")
            timeline = omni.timeline.get_timeline_interface()

            timeline.play()

        asyncio.ensure_future(_open_usd(usd_file_path))

        windows = omni.ui.Workspace.get_windows()
        for window in windows:
            if str(window) =="Viewport":
                omni.ui.Workspace.show_window(str(window), True)
            else:
                omni.ui.Workspace.show_window(str(window), False)

    def on_shutdown(self):
        print("[my_company.my_app.setup] MyExtension shutdown")