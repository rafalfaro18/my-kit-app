import asyncio
import omni.ext
import carb.settings
import omni.kit.app
import omni.kit.commands

from pxr import Usd, Sdf

class CreateSetupExtension(omni.ext.IExt):
    """Create Final Configuration"""
    def on_startup(self, ext_id):
        """setup the window layout, menu, final configuration of the extensions etc"""
        print("[my_company.my_app.setup] MyExtension startup")
        import omni.usd
        import carb

        manager = omni.kit.app.get_app().get_extension_manager()
        usd_file_path = manager.get_extension_path_by_module("my_company.my_app.setup")+"/data/DefaultStage.usd"

        async def _open_usd(usd_file_path):
            await omni.usd.get_context().open_stage_async(usd_file_path)
            carb.log_warn(f"Stage opened from {usd_file_path}")

        asyncio.ensure_future(_open_usd(usd_file_path))

    def on_shutdown(self):
        print("[my_company.my_app.setup] MyExtension shutdown")