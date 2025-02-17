PYTHON_TEMPLATE = """#A MongoDB authenticatable model
from mdb_models.authenticatable import AuthenticatableModel

class {model_name}(AuthenticatableModel):
    
    collection_name = 'users' # You can change this to the name of the collection in the database

"""
