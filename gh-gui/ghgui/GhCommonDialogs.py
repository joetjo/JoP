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
