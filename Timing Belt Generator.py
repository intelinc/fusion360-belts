import adsk.core
import traceback

import os

try:
    from . import config
    from .apper import apper

    # ************Samples**************
    # Basic Fusion 360 Command Base samples
    from .commands.SampleCommand1 import SampleCommand1
    from .commands.SampleCommand2 import SampleCommand2

    # Palette Command Base samples
    from .commands.SamplePaletteCommand import SamplePaletteSendCommand, SamplePaletteShowCommand

    # Various Application event samples
    from .commands.SampleCustomEvent import SampleCustomEvent
    from .commands.SampleDocumentEvents import SampleDocumentEvent1, SampleDocumentEvent2
    from .commands.SampleWorkspaceEvents import SampleWorkspaceEvent
    from .commands.SampleWebRequestEvent import SampleWebRequestOpened
    from .commands.SampleCommandEvents import SampleCommandEvent
    from .commands.SampleActiveSelectionEvents import SampleActiveSelectionEvent

    # Create our addin definition object
    my_addin = apper.FusionApp(config.app_name, config.company_name, False)
    my_addin.root_path = config.app_path

    # Creates a basic Hello World message box on execute
    my_addin.add_command(
        'Sample Command 1',
        SampleCommand1,
        {
            'cmd_description': 'Hello World!',
            'cmd_id': 'sample_cmd_1',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Commands',
            'cmd_resources': 'command_icons',
            'command_visible': True,
            'command_promoted': True,
        }
    )

    # General command showing inputs and user interaction
    my_addin.add_command(
        'Sample Command 2',
        SampleCommand2,
        {
            'cmd_description': 'A simple example of a Fusion 360 Command with various inputs',
            'cmd_id': 'sample_cmd_2',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Commands',
            'cmd_resources': 'command_icons',
            'command_visible': True,
            'command_promoted': False,
        }
    )

    # Create an html palette to as an alternative UI
    my_addin.add_command(
        'Sample Palette Command - Show',
        SamplePaletteShowCommand,
        {
            'cmd_description': 'Shows the Fusion 360 Demo Palette',
            'cmd_id': 'sample_palette_show',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Palette',
            'cmd_resources': 'palette_icons',
            'command_visible': True,
            'command_promoted': True,
            'palette_id': 'sample_palette',
            'palette_name': 'Sample Fusion 360 HTML Palette',
            'palette_html_file_url': os.path.join('commands', 'palette_html', 'Timing Belt Generator.html'),
            'palette_use_new_browser': True,
            'palette_is_visible': True,
            'palette_show_close_button': True,
            'palette_is_resizable': True,
            'palette_width': 500,
            'palette_height': 600,
        }
    )

    # Send data from Fusion 360 to the palette
    my_addin.add_command(
        'Send Info to Palette',
        SamplePaletteSendCommand,
        {
            'cmd_description': 'Send data from a regular Fusion 360 command to a palette',
            'cmd_id': 'sample_palette_send',
            'workspace': 'FusionSolidEnvironment',
            'toolbar_panel_id': 'Palette',
            'cmd_resources': 'palette_icons',
            'command_visible': True,
            'command_promoted': False,
            'palette_id': 'sample_palette',
        }
    )

    app = adsk.core.Application.cast(adsk.core.Application.get())
    ui = app.userInterface

    # Uncomment as necessary.  Running all at once can be overwhelming :)
    # my_addin.add_custom_event("Timing Belt Generator_message_system", SampleCustomEvent)
    # my_addin.add_document_event("Timing Belt Generator_open_event", app.documentActivated, SampleDocumentEvent1)
    # my_addin.add_document_event("Timing Belt Generator_close_event", app.documentClosed, SampleDocumentEvent2)
    # my_addin.add_workspace_event("Timing Belt Generator_workspace_event", ui.workspaceActivated, SampleWorkspaceEvent)
    # my_addin.add_web_request_event("Timing Belt Generator_web_request_event", app.openedFromURL, SampleWebRequestOpened)
    # my_addin.add_command_event("Timing Belt Generator_command_event", app.userInterface.commandStarting, SampleCommandEvent)
    # my_addin.add_command_event("Timing Belt Generator_active_selection_event", ui.activeSelectionChanged, SampleActiveSelectionEvent)

except:
    app = adsk.core.Application.get()
    ui = app.userInterface
    if ui:
        ui.messageBox('Initialization Failed: {}'.format(traceback.format_exc()))

# Set to True to display various useful messages when debugging your app
debug = False


def run(context):
    my_addin.run_app()


def stop(context):
    my_addin.stop_app()

