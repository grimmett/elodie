from __future__ import print_function


import os
import sys
import time

import zerorpc

import elodie_cli
from elodie.config import load_config
from elodie.filesystem import FileSystem

class ElodieApi(object):
    @zerorpc.stream
    def import_files(self, destination, source):
        """about any text"""
        # def _import(destination, source, file, album_from_folder, trash, allow_duplicates, debug, paths):
        return elodie_cli._import(
            destination,
            source, 
            False,
            False,
            False,
            True,
            True,
            []
        )

    def preview_file_name(self, fmt, metadata=None):
        filesystem = FileSystem()
        filesystem.default_folder_path_definition['full_path'] = '%date/%state'
        metadata = {'date_taken': time.localtime(), 'directory_path': '/Users/jaisen/dev/tmp/source', 'album': None, 'camera_make': u'Google', 'extension': 'jpg', 'title': None, 'base_name': 'IMG_20180830_110056', 'original_name': None, 'longitude': None, 'camera_model': u'Pixel', 'latitude': None, 'mime_type': 'image/jpeg'}
        return filesystem.get_folder_path(metadata)


def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)

def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(ElodieApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()
