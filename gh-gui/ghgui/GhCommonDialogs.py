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

import os


class GhCommonDialogs:

    @staticmethod
    def fileSelection(initialFolder=os.getcwd(),
                      title="Select file",
                      filetypes=None):
        """
        Select a file from current folder
        :param initialFolder:
        :param title:
        :param filetypes:
        :return:
        """
        if filetypes is None:
            filetypes = [("Text Files", "*.txt")]
# TODO : Qt implementation
#        return filedialog.askopenfilename(initialdir=initialFolder, title=title, filetypes=filetypes)
