from flask import Flask, request, jsonify
from hyperon import MeTTa, S, V, E

metta = MeTTa()

metta.run('''
(gene ENSG00000290825)
(gene_type (gene ENSG00000290825) lncRNA)
(chr (gene ENSG00000290825) chr1)
(start (gene ENSG00000290825) 11869)
(end (gene ENSG00000290825) 14409)
(gene_name (gene ENSG00000290825) DDX11L2)
''')

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_gene():
    try:
        data = request.get_json()
        gene_id = data.get('gene_id', '').strip()

        if not gene_id:
            return jsonify({"error": "Gene ID is required"}), 400

        query = f'!(match &self ($relationship (gene {gene_id}) $value) (Pair $relationship $value))'
        result = metta.run(query)

        return jsonify({"gene_id": gene_id, "results": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
