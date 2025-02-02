# MongoDB Data Layer

A data modeling **MongoDB** library for **Python**

<hr />

### Installation
1. Install the python package via pip:

```bash
pip install mongodb_data_layer
```
**Note**: It is better to create a python virtual environment...

2. Setup an environment variables:
   
   - To create an environment variables, simply create a file named **".env"**.
    - Then, add these following variables to a created file:

    ```bash
    MONGO_DB_URL="mongodb://localhost:27020" # The default mongodb localhost but you can also put a connection string from atlas server.
    MONGO_DB_NAME="my_database" # Your created database
    ```

3. To create a model you can simply enter this command on a command promt:

```bash
generate-model /models/test_model.py  # where '/models/test_model.py' is your file path and file name
```

4. It will generate a file like this:

```python
#A MongoDB model for the tests collection
from mongodb_data_layer.base import BaseMongoModel

class Test(BaseMongoModel):
    
    collection_name = 'tests' # Create a collection with this name in the database
```

<hr />

### Notes

<p>This library is very useful to lessen the configuration for mongodb database. </p>

<p>This package is build on top of MongoDB official package/drivers.</p>

<p>This is also works well in fastapi.</p>

<p>This library is currently in development. Feel free to contribute.</p>

<hr />

Official repository: <a href="https://github.com/nojram00/mongodb-data-layer">https://github.com/nojram00/mongodb-data-layer</a>