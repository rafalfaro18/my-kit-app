import asyncio
import omni.ext
import carb.settings
import omni.kit.app
import omni.kit.stage_templates as stage_templates

class TestStage():

    def __init__(self):
        omni.kit.stage_templates.register_template("test", self.new_stage, 0)

    def __del__(self):
        omni.kit.stage_templates.unregister_template("test")

    from pxr import Usd, Sdf


    def new_stage(self, rootname):
        import omni.kit.commands

        manager = omni.kit.app.get_app().get_extension_manager()

        omni.kit.commands.execute(
            "CreatePrim",
            prim_path="/World",
            prim_type="Xform",
            select_new_prim=False,
        )
        refSphere = omni.usd.get_context().get_stage().OverridePrim("/World/newRef")
        refSphere.GetReferences().AddReference(manager.get_extension_path_by_module("my_company.my_app.setup")+"/data/DefaultStage.usd")

class CreateSetupExtension(omni.ext.IExt):
    """Create Final Configuration"""
    def on_startup(self, ext_id):
        """setup the window layout, menu, final configuration of the extensions etc"""
        print("[my_company.my_app.setup] MyExtension startup")
        TestStage()
        self._settings = carb.settings.get_settings()

        # Setting to hack few things in test run. Ideally we shouldn't need it.
        test_mode = self._settings.get("/app/testMode")

        if not test_mode and not self._settings.get("/app/content/emptyStageOnStart"):
            self.__await_new_scene = asyncio.ensure_future(self.__new_stage())


    async def __new_stage(self):

            # 10 frame delay to allow Layout
            for i in range(10):
                await omni.kit.app.get_app().next_update_async()

            if omni.usd.get_context().can_open_stage():
                stage_templates.new_stage(template="test")

    def on_shutdown(self):
        print("[my_company.my_app.setup] MyExtension shutdown")