from flask import Blueprint, request, jsonify
from app import db
from app.models.review_model import Review

review_bp = Blueprint('review_bp', __name__)

# 1. ROTA PARA CRIAR (INCLUIR) UM NOVO REVIEW
@review_bp.route('/reviews', methods=['POST'])
def create_review():
    """
    Cria um novo review de estudo bíblico.
    ---
    tags:
      - Reviews
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ReviewInput'
    responses:
      201:
        description: Review criado com sucesso.
        schema:
          $ref: '#/definitions/ReviewOutput'
      400:
        description: Erro na requisição. Dados faltando.
    """
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Título e conteúdo são obrigatórios.'}), 400

    new_review = Review(title=data['title'], content=data['content'])
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_json()), 201

# 2. ROTA PARA LISTAR TODOS OS REVIEWS
@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    """
    Retorna uma lista de todos os reviews.
    ---
    tags:
      - Reviews
    responses:
      200:
        description: Uma lista de todos os reviews.
        schema:
          type: array
          items:
            $ref: '#/definitions/ReviewOutput'
    """
    reviews = Review.query.order_by(Review.date_posted.desc()).all()
    return jsonify([review.to_json() for review in reviews]), 200

# 3. ROTA PARA BUSCAR UM REVIEW ESPECÍFICO POR ID
@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """
    Retorna um review específico pelo seu ID.
    ---
    tags:
      - Reviews
    parameters:
      - name: review_id
        in: path
        type: integer
        required: true
        description: O ID do review a ser buscado.
    responses:
      200:
        description: Os detalhes do review.
        schema:
          $ref: '#/definitions/ReviewOutput'
      404:
        description: Review não encontrado.
    """
    review = Review.query.get_or_404(review_id)
    return jsonify(review.to_json()), 200

# 4. ROTA PARA ATUALIZAR UM REVIEW EXISTENTE
@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """
    Atualiza um review existente pelo seu ID.
    ---
    tags:
      - Reviews
    parameters:
      - name: review_id
        in: path
        type: integer
        required: true
        description: O ID do review a ser atualizado.
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ReviewInput'
    responses:
      200:
        description: Review atualizado com sucesso.
        schema:
          $ref: '#/definitions/ReviewOutput'
      400:
        description: Erro na requisição. Dados faltando.
      404:
        description: Review não encontrado.
    """
    review = Review.query.get_or_404(review_id)
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Título e conteúdo são obrigatórios.'}), 400

    review.title = data['title']
    review.content = data['content']
    db.session.commit()
    return jsonify(review.to_json()), 200

# 5. ROTA PARA DELETAR UM REVIEW
@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Deleta um review pelo seu ID.
    ---
    tags:
      - Reviews
    parameters:
      - name: review_id
        in: path
        type: integer
        required: true
        description: O ID do review a ser deletado.
    responses:
      200:
        description: Review deletado com sucesso.
      404:
        description: Review não encontrado.
    """
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deletado com sucesso.'}), 200

# 6. ROTA PARA BUSCAR REVIEWS POR TERMO
@review_bp.route('/reviews/search', methods=['GET'])
def search_reviews():
    """
    Busca por reviews que contenham um termo no título ou no conteúdo.
    ---
    tags:
      - Reviews
    parameters:
      - name: term
        in: query
        type: string
        required: true
        description: O termo a ser buscado no título ou conteúdo dos reviews.
    responses:
      200:
        description: Uma lista de reviews que correspondem ao termo de busca.
        schema:
          type: array
          items:
            $ref: '#/definitions/ReviewOutput'
    """
    search_term = request.args.get('term')
    if not search_term:
        return jsonify({'error': 'O parâmetro "term" é obrigatório.'}), 400
    
    query = Review.query.filter(
        db.or_(
            Review.title.ilike(f'%{search_term}%'),
            Review.content.ilike(f'%{search_term}%')
        )
    ).order_by(Review.date_posted.desc()).all()
    
    return jsonify([review.to_json() for review in query]), 200