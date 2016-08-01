import subprocess

import wx
from robotide.controller.filecontrollers import TestCaseFileController, ResourceFileController, \
    TestDataDirectoryController
from robotide.pluginapi import Plugin, ActionInfo, SeparatorInfo
from robotide.widgets import PopupMenuItem


class TortoiseSVNPlugin(Plugin):
    """
    Plugin adds a menu to call dialogs from TortoiseSVN
    """
    MENU_NAME = 'TortoiseSVN'
    SVN_INSTALLATION_URL = 'http://tortoisesvn.net/downloads.html'
    VERSION = '0.1.0'
    # plugin metadata
    metadata = {'Version': VERSION,
                'Author': 'ukostas',
                'URL': 'https://github.com/ukostas/robotframework-ride-tortoisesvn'}

    # http://tortoisesvn.net/docs/release/TortoiseSVN_en/tsvn-automation.html
    menu = [
        {"name": "Check Project for modifications", "action": 'TortoiseProc.exe /command:repostatus /path:"{path}"'},
        {"name": "Show Project Commit Log", "action": 'TortoiseProc.exe /command:log /path:"{path}"'},
        {"name": "Project Update", "action": 'TortoiseProc.exe /command:update /path:"{path}"'},
        {"name": "Project Commit...", "action": 'TortoiseProc.exe /command:commit /path:"{path}"'},
        {"name": "Project Revert...", "action": 'TortoiseProc.exe /command:revert /path:"{path}"'},
        {"name": None},
        {"name": "Item Revert...", "action": 'TortoiseProc.exe /command:revert /path:"{path}"'},
        {"name": "Item Commit Log", "action": 'TortoiseProc.exe /command:log /path:"{path}"', 'context_menu': True},
        {"name": "Item Blame", "action": 'TortoiseProc.exe /command:blame /path:"{path}"', 'context_menu': True},
        {"name": "Item Diff", "action": 'TortoiseProc.exe /command:diff /path:"{path}"', 'context_menu': True},
        {"name": None},
        {"name": "About TortoiseSVN", "action": 'TortoiseProc.exe /command:about'},
        {"name": "TortoiseSVN Installation", "action": SVN_INSTALLATION_URL}]

    def __init__(self, application=None):
        self.context_menu = [PopupMenuItem('---')]
        self.context_menu += [
            PopupMenuItem(item['name'], callable=self.create_callable(item['name'], item['action'])) for
            item in filter(lambda x: x.get('context_menu', False), self.menu)]
        Plugin.__init__(self, application, metadata=self.metadata)

    def enable(self):
        self.add_main_menu()
        self.add_tree_context_menu()

    def disable(self):
        self.remove_main_menu()
        self.remove_tree_context_menu()

    def remove_tree_context_menu(self):
        self.tree.unregister_context_menu_hook(self._context_menu_handler)

    def remove_main_menu(self):
        self.unregister_actions()

    def add_main_menu(self):
        self.unregister_actions()
        for menuItem in self.menu:
            if menuItem['name'] is None:
                self.register_action(SeparatorInfo(self.MENU_NAME))
            else:
                action_info = ActionInfo(self.MENU_NAME, name=menuItem['name'],
                                         action=self.create_callable(menuItem['name'], menuItem['action']))
                self.register_action(action_info)

    def create_callable(self, name, action):
        def callable(event):
            # check if this is for whole project or file/directory
            if 'item' in name.lower():  # for one single item - file/directory
                if not self.datafile:
                    return
                full_cmd = action.format(path=self.datafile.source)
            else:  # for whole project - root file/directory
                full_cmd = action.format(path=self.model.suite.source)
            # RideLogMessage(name + " clicked: " + fullCmd).publish()
            if full_cmd.lower().startswith('http'):
                wx.LaunchDefaultBrowser(full_cmd)
            else:
                subprocess.Popen(full_cmd)

        return callable

    def add_tree_context_menu(self):
        self.tree.register_context_menu_hook(self._context_menu_handler)

    def _context_menu_handler(self, item):
        if isinstance(item, (
                TestCaseFileController, ResourceFileController,
                TestDataDirectoryController)):
            return self.context_menu
        return []
