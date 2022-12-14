# Copyright 2022 joetjo https://github.com/joetjo/MarkdownHelper
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# TODO Move from tkinter to QT

class GhIcons:
    ICON_PACK = "-16.png"
    THEME = JopSETUP.get(JopSETUP.APP_THEME)

    def __init__(self, platforms):
        self.VOID = PhotoImage(file="icons/{}/void{}".format(GhIcons.THEME, GhIcons.ICON_PACK))

        self.ABOUT = PhotoImage(file="icons/{}/about{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.CANCEL_EDIT = PhotoImage(file="icons/{}/remove-edit{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.CLOSE = PhotoImage(file="icons/{}/close{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.DOCUMENT = PhotoImage(file="icons/{}/document{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.EDIT = PhotoImage(file="icons/{}/edit{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.ESCAPE = PhotoImage(file="icons/{}/esc{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.FILE_SELECTION = PhotoImage(file="icons/{}/file-explorer{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.MENU = PhotoImage(file="icons/{}/menu{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.NA = PhotoImage(file="icons/{}/not-applicable{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.PLAY = PhotoImage(file="icons/{}/play{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.PLAY_OFF = PhotoImage(file="icons/{}/closed-sign{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.PLUS = PhotoImage(file="icons/{}/plus-math{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.REFRESH = PhotoImage(file="icons/{}/refresh{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.REMOVE = PhotoImage(file="icons/{}/remove{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.SEARCH = PhotoImage(file="icons/{}/search{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.SEARCH_RESET = PhotoImage(file="icons/{}/clear-search{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.SHOP = PhotoImage(file="icons/{}/shop{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.SWITCH = PhotoImage(file="icons/{}/switch{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.TIPS = PhotoImage(file="icons/{}/website{}".format(GhIcons.THEME, GhIcons.ICON_PACK))

        # IMAGES
        self.DISCORD = self.loadImage("icons/platforms/discord.png")

        self.NO_PLATFORM = PhotoImage(file="icons/{}/none{}".format(GhIcons.THEME, GhIcons.ICON_PACK))
        self.PLATFORMS = dict()
        for p in platforms:
            acronym = platforms[p]
            self.PLATFORMS[acronym] = self.loadImage("icons/platforms/{}.png".format(acronym))

    @staticmethod
    def loadImage(file):
        if GhFileUtil.fileExist(file):
            return PhotoImage(file=file)
        else:
            Log.info("Missing icon resources: {}".format(file))
            return None
