import glob
import shutil
import pathlib


def hoge():
    return print('hoge')


class File:
    def __init__(self, path=None):
        self.path = path

    def is_file(self, path=None):
        path = self.path if self.is_none(path) else path
        if isinstance(path, str):
            path = pathlib.Path(path)
        return path.suffix

    def is_dir(self, path=None):
        path = self.path if self.is_none(path) else path
        if isinstance(path, str):
            path = pathlib.Path(path)
        return path.exists()

    def mkdir(self, path=None):
        path = self.path if self.is_none(path) else path
        if isinstance(path, str):
            path = pathlib.Path(path)
        return path.mkdir()

    def is_none(self, path):
        return path is None


class JoinFile(File):
    def __init__(self, path=None):
        super(JoinFile, self).__init__(path)
        self.path = path

    def join_filename(self):
        print(pathlib.Path.cwd())
        list = glob.glob('**/*', recursive=True)
        for i in list:
            split_list = i.split('/')
            print('_'.join(split_list))

    def join_and_cp(self, output_dir_path=None):
        output_dir_path = output_dir_path if output_dir_path else 'archive/cp'
        True if self.is_dir(output_dir_path) else self.mkdir(path=output_dir_path)
        # if not self.is_dir(output_dir_path):
        #     self.mkdir(path=output_dir_path)
        list = glob.glob('**/*', recursive=True)
        for i in list:
            if self.is_file(i):
                split_list = i.split('/')
                rename_filename = '_'.join(split_list)
                shutil.copy(i, pathlib.Path(output_dir_path, rename_filename))
