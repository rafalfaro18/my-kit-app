# Omniverse Kit App Template

[Omniverse Kit App Template](https://github.com/NVIDIA-Omniverse/kit-app-template) - is the place to start learning about developing Omniverse Apps.
This project contains everything necessary to develop and package an Omniverse App.

## Links

* Recommended: [Tutorial](https://docs.omniverse.nvidia.com/kit/docs/kit-app-template) for
getting started with application development.
* [Developer Guide](https://docs.omniverse.nvidia.com/dev-guide/latest/index.html).

## Build

1. Clone [this repo](https://github.com/NVIDIA-Omniverse/kit-app-template) to your local machine.
2. Open a command prompt and navigate to the root of your cloned repo.
3. Run `build.bat` to bootstrap your dev environment and build an example app.
4. Run `_build\windows-x86_64\release\my_name.my_app.bat` (or other apps) to open an example kit application.

You should have now launched your simple kit-based application!

## Contributing
The source code for this repository is provided as-is and we are not accepting outside contributions.

## Test template
Defines a new Test template but it tries to load it from ``C:\Users\NAME\Documents\Kit\apps\my_company.my_app\scripts\new_stage\__init__.py`` so currently you have to manually create that file and add this content:
```python
class TestStage():

	def __init__(self):
		omni.kit.stage_templates.register_template("test", self.new_stage, 1)

	def __del__(self):
		omni.kit.stage_templates.unregister_template("test")

	import omni.kit.commands
	from pxr import Usd, Sdf


	def new_stage(self, rootname):
		#############
		# Full Usage
		#############
		from pxr import UsdGeom
		import omni.usd

		# Create new USD stage for this sample in OV
		context: omni.usd.UsdContext = omni.usd.get_context()
		success: bool = context.open_stage("C:/Users/Pc/Documents/Omniverse/DefaultStage.usd")


TestStage()
```
