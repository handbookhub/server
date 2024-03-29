"""
    Provides config class and methods which may be useful for it
"""
from urllib import request
from collections import namedtuple
from file_system import get_yaml_file

RoutesTuple = namedtuple("routes", ["image"])

class Config:
    """
        Contains all the config data from config.yml

        data_folder: str - path to folder that contains all the data
        icon_name: str - standard name for icons
        file_names: namedtuple - file names for [["description", "content"]
    """

    data_folder: str = ""
    icon_name: str = ""
    file_names: namedtuple = namedtuple("file_names", ["description", "content"])
    ip: str = ""
    port: str = ""
    routes: namedtuple = RoutesTuple("image")

    def __init__(self, config_dict):
        assert isinstance(config_dict["data_folder"], str) and len(config_dict["data_folder"]) > 0, "There is should be not empty data folder"
        self.data_folder = config_dict["data_folder"]

        assert isinstance(config_dict["icon_name"], str) and config_dict["icon_name"].endswith(".png"), "There is should be icon in png format"
        self.icon_name = config_dict["icon_name"]

        for name, file_name in config_dict["file_names"].items():
            assert hasattr(self.file_names, name), f"there is no file name: {name}"
            assert isinstance(file_name, str) and file_name.endswith(".md"), "File names should have .md extension"

            setattr(self.file_names, name, file_name)

        self.ip = request.urlopen("https://checkip.amazonaws.com").read().decode("utf8").strip("\n")
        self.port = config_dict["port"]


config = Config(get_yaml_file("config.yml"))
