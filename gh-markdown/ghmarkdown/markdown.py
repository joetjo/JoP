# Copyright 2021 joetjo https://github.com/joetjo/MarkdownHelper
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

from pathlib import Path

from ghbase.GhSetup import GhSetup
from ghmarkdown.markdownfile import MhMarkdownFile
from ghmarkdown.report import MhReport


#
# Setup from $home/.markdownHelper
#    ( Sample provided in example.markdownHelper.json )
#
class MarkdownHelper:
    def __init__(self):
        self.SETUP = GhSetup('markdownHelper')
        self.VAULT = self.SETUP.getBloc("global")["base_folder"]
        self.IGNORE = self.SETUP.getBloc("global")["ignore"]
        self.REPORTS = self.SETUP.getBloc("global")["reports"]
        self.SUB_CONTENT = self.SETUP.getBloc("global")["shared_contents"]
        self.FILES = dict()
        self.SORTED_FILES = dict()
        self.TAGS = dict()

    # folder: Path
    # shift: String ( String length provide the indentation level )
    def processFolder(self, folder, shift):
        print("{}{}".format(folder, shift))
        entryCount = 0

        # Loop on file in current folder
        for entry in folder.iterdir():
            if entry.is_file() and entry.name.endswith(".md") and entry.name not in self.IGNORE:
                key = entry.name[0:len(entry.name) - 3]
                entryCount = entryCount + 1
                mdFile = MhMarkdownFile(key, entry)
                self.FILES[key] = mdFile
                print("{}>{} {}".format(shift, key, mdFile.tags))
                if len(mdFile.tagsComment) > 0:
                    print("{}>>>> comments {}".format(shift, mdFile.tagsComment))
                for tag in mdFile.tags:
                    self.TAGS[tag] = tag

        # Loop on sub folder
        for entry in folder.iterdir():
            if not entry.is_file() and entry.name not in self.IGNORE:
                entryCount = entryCount + self.processFolder(entry, "{}{}".format(shift, " "))

        return entryCount

    def markdown(self):
        print("   | Markdown vault: {}\n====".format(self.VAULT))
        count = self.processFolder(Path(self.VAULT), "")

        print("\n=================")
        print("> {} md files detected".format(count))
        print("> {} tags detected".format(len(self.TAGS)))

        for key in sorted(self.FILES):
            self.SORTED_FILES[key] = self.FILES[key]

        try:
            for report in self.REPORTS:
                print("\n=================\nProcessing report \"{}\"\n=================\n".format(report["title"]))
                MhReport(report, self.VAULT, self.SORTED_FILES, self.TAGS, self.SUB_CONTENT).generate()
        except Exception:
            raise
