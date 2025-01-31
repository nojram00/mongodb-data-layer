from .db import create_connection

class BaseMongoModel:
    """
    A base model for mongodb models.

    Attributes:
        collection_name (str): The name of the collection. Must be specified by subclasses.
    """

    collection_name = None
    """
    Can be overriden by subclasses to specify the collection name.
    """

    def __init__(self):
        if self.collection_name is None:
            raise ValueError('collection_name is not specified.')

        # Initialize the collection
        self.collection = create_connection()[self.collection_name] 