# Prerequisites

Ensure you have Python installed along with Flask and Hyperon                           

 # app.py File

- Defines the Flask web server.
- Handles GET and POST requests for gene queries.
- Calls query_gene_data(gene_id) to fetch data from MeTTa.
- Converts results to a JSON-compatible format before returning them.

# gene_data.py File

- Contains the function query_gene_data(gene_id) that executes MeTTa queries to retrieve gene data.
- metta_to_json_compatible(atom)
- Ensures MeTTa query results are converted into JSON-compatible formats.
- Recursively processes MeTTa atoms to ensure proper serialization.
