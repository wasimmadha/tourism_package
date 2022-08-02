import pickle
import sys

from packagePrediction.exception import PackageException


def load_object(file_path:str):
    """
    file_path: str
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise PackageException(e,sys) from e