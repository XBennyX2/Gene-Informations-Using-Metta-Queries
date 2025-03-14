from flask import Flask, jsonify, request, render_template_string
from hyperon import MeTTa
from gene_data import query_gene_data

# Initialize MeTTa
metta = MeTTa()

# Create Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template_string('''
            <form id="geneForm">
                <label for="gene_id">Gene ID:</label>
                <input type="text" id="gene_id" name="gene_id" required>
                <input type="submit" value="Submit">
            </form>
            <pre id="result"></pre>
            <script>
                document.getElementById('geneForm').onsubmit = async function(event) {
                    event.preventDefault(); // Prevent the form from submitting normally
                    const geneId = document.getElementById('gene_id').value;
                    const response = await fetch('/', {
                        method: 'POST',
                        headers: {
                                                                  'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ gene_id: geneId })
                    });
                    const result = await response.json();
                    document.getElementById('result').textContent = JSON.stringify(result, null, 2);
                };
            </script>
        ''')

    if request.method == 'POST':
        try:
            data = request.get_json()
            gene_id = data.get('gene_id', '').strip()

            if not gene_id:
                return jsonify({"error": "Gene ID is required"}), 400

            # Query the gene data
            result = query_gene_data(gene_id)
        

            if not result or not result[0]:
                return jsonify({"error": "Gene ID not found"}), 404
            


            return jsonify({"gene_id": gene_id,"result": result})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)