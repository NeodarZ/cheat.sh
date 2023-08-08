"""
Adapter for local cheatsheets based on https://github.com/cheat/cheat

Cheatsheets are located in `local`
Each cheat sheet is a separate file without extension
"""

# pylint: disable=relative-import,abstract-method

from config import CONFIG
from .file_adapter import FileRepositoryAdapter

class Local(FileRepositoryAdapter):
    """
    File at file  system
    """

    _adapter_name = "local"
    _output_format = "code"
    _cache_needed = True
    _repository_url = CONFIG['adaptaters.config']['local']['repository_url']
    _local_repository_location="local"
    _cheatsheet_files_prefix = ""
    _cheatsheet_files_extension = ".adoc"
