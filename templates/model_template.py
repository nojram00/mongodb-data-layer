PYTHON_TEMPLATE = """#A MongoDB model for the {collection_name} collection
from mongodb_data_layer.base import BaseMongoModel

class {model_name}(BaseMongoModel):
    
    collection_name = '{collection_name}' # Create a collection with this name in the database

"""