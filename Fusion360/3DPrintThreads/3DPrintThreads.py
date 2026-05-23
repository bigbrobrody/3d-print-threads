import os
import shutil
import traceback
from pathlib import Path
from typing import List

import adsk.core

APP = adsk.core.Application.get()
UI = APP.userInterface if APP else None

CMD_ID = 'bigbrobrody_3dPrintThreads_install'
CMD_NAME = 'Install 3D Print Threads'
CMD_DESCRIPTION = 'Install metric 3D print thread definitions (0.0mm to 1.0mm tolerance classes).'
WORKSPACE_ID = 'FusionSolidEnvironment'
PANEL_ID = 'SolidCreatePanel'

_handlers = []


def _thread_data_targets() -> List[Path]:
    home = Path.home()
    targets = []

    appdata = os.getenv('APPDATA')
    if appdata:
        targets.append(Path(appdata) / 'Autodesk' / 'Autodesk Fusion 360' / 'API' / 'ThreadData')
    localappdata = os.getenv('LOCALAPPDATA')
    if localappdata:
        production_root = Path(localappdata) / 'Autodesk' / 'webdeploy' / 'production'
        try:
            if production_root.is_dir():
                for deployment in sorted(production_root.iterdir()):
                    if deployment.is_dir():
                        targets.append(
                            deployment / 'Fusion' / 'Server' / 'Fusion' / 'Configuration' / 'ThreadData'
                        )
        except OSError:
            pass

    targets.append(home / 'Library' / 'Application Support' / 'Autodesk' / 'Autodesk Fusion 360' / 'API' / 'ThreadData')
    return targets


def _install_profiles() -> Path:
    source = Path(__file__).resolve().parent / 'resources' / 'thread_profiles' / '3DPrintMetric.xml'
    if not source.exists():
        raise FileNotFoundError(f'Missing thread profile file: {source}')

    targets = _thread_data_targets()
    last_written = None

    for target in targets:
        try:
            target.mkdir(parents=True, exist_ok=True)
            destination = target / source.name
            shutil.copy2(source, destination)
            last_written = destination
        except OSError:
            continue

    if not last_written:
        raise OSError('No writable Fusion 360 ThreadData folder was found.')

    return last_written


class _ExecuteHandler(adsk.core.CommandEventHandler):
    def notify(self, args: adsk.core.CommandEventArgs):
        try:
            destination = _install_profiles()
            if UI:
                UI.messageBox(
                    f'3D print thread profiles were installed to:\n{destination}\n\n'
                    'Restart Fusion 360 to refresh thread libraries.'
                )
        except Exception:
            if UI:
                UI.messageBox('Failed to install thread profiles:\n' + traceback.format_exc())


class _CreatedHandler(adsk.core.CommandCreatedEventHandler):
    def notify(self, args: adsk.core.CommandCreatedEventArgs):
        handler = _ExecuteHandler()
        args.command.execute.add(handler)
        _handlers.append(handler)


def run(context):
    try:
        if not UI:
            return

        cmd_def = UI.commandDefinitions.itemById(CMD_ID)
        if not cmd_def:
            cmd_def = UI.commandDefinitions.addButtonDefinition(CMD_ID, CMD_NAME, CMD_DESCRIPTION)

        created = _CreatedHandler()
        cmd_def.commandCreated.add(created)
        _handlers.append(created)

        workspace = UI.workspaces.itemById(WORKSPACE_ID)
        panel = workspace.toolbarPanels.itemById(PANEL_ID) if workspace else None
        if panel and not panel.controls.itemById(CMD_ID):
            panel.controls.addCommand(cmd_def)
    except Exception:
        if UI:
            UI.messageBox('Failed to start add-in:\n' + traceback.format_exc())


def stop(context):
    try:
        if not UI:
            return

        workspace = UI.workspaces.itemById(WORKSPACE_ID)
        panel = workspace.toolbarPanels.itemById(PANEL_ID) if workspace else None
        control = panel.controls.itemById(CMD_ID) if panel else None
        if control:
            control.deleteMe()

        cmd_def = UI.commandDefinitions.itemById(CMD_ID)
        if cmd_def:
            cmd_def.deleteMe()
    except Exception:
        if UI:
            UI.messageBox('Failed to stop add-in:\n' + traceback.format_exc())
