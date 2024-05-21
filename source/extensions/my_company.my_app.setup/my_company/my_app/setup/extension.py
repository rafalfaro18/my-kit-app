import asyncio
import omni.ext
import carb.settings
import omni.kit.app
import omni.kit.stage_templates as stage_templates
from omni.kit.viewport.menubar.core import get_instance as get_mb_inst, DEFAULT_MENUBAR_NAME
from omni.kit.viewport.menubar.core.viewport_menu_model import ViewportMenuModel
from omni.kit.viewport.utility import get_active_viewport, get_active_viewport_window, disable_selection

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

        self._set_viewport_fill_on()

        self._set_viewport_menubar_visibility(False)

        disable_selection(get_active_viewport())

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

    def _set_viewport_menubar_visibility(self, show: bool) -> None:
        mb_inst = get_mb_inst()
        if mb_inst and hasattr(mb_inst, "get_menubar"):
            main_menubar = mb_inst.get_menubar(DEFAULT_MENUBAR_NAME)
            if main_menubar.visible_model.as_bool != show:
                main_menubar.visible_model.set_value(show)
        ViewportMenuModel()._item_changed(None)  # type: ignore

    def _set_viewport_fill_on(self) -> None:
        vp_window = get_active_viewport_window()
        vp_widget = vp_window.viewport_widget if vp_window else None
        if vp_widget:
            vp_widget.expand_viewport = True