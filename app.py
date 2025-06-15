from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/eventos')
def eventos():
    # Aqui você poderia buscar eventos de um banco de dados
    # Por enquanto, vamos usar dados estáticos
    eventos_lista = [
        {
            'titulo': 'Torneio de Pesca',
            'data': '28/06/2025',
            'descricao': 'Grande torneio de pesca com premiação para o maior peixe.'
        },
        {
            'titulo': 'Dia da Família',
            'data': '15/07/2025',
            'descricao': 'Traga sua família para um dia especial com descontos e atividades para crianças.'
        }
    ]
    return render_template('eventos.html', eventos=eventos_lista)


@app.route('/cardapio')
def cardapio():
    # Aqui você poderia buscar itens do cardápio de um banco de dados
    # Por enquanto, vamos usar dados estáticos
    porcoes = [
        {'nome': 'Porção de Tilápia', 'preco': 'R$ 75,00', 'descricao': 'Tilápia frita com limão e molho especial'},
        {'nome': 'Porção de Pintado', 'preco': 'R$ 85,00', 'descricao': 'Pintado grelhado com ervas'},
        {'nome': 'Isca de Peixe', 'preco': 'R$ 60,00', 'descricao': 'Iscas de peixe empanadas'},
        {'nome': 'Porção de Batata Frita', 'preco': 'R$ 35,00', 'descricao': 'Batata frita crocante'},
        {'nome': 'Porção de Mandioca', 'preco': 'R$ 30,00', 'descricao': 'Mandioca frita'}
    ]
    
    bebidas = [
        {'nome': 'Refrigerante', 'preco': 'R$ 12,00'},
        {'nome': 'Cerveja', 'preco': 'R$ 15,00'},
        {'nome': 'Água', 'preco': 'R$ 6,00'},
        {'nome': 'Suco Natural', 'preco': 'R$ 14,00'}
    ]
    
    return render_template('cardapio.html', porcoes=porcoes, bebidas=bebidas)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


# Esta parte é importante para o Vercel
if __name__ == '__main__':
    app.run(debug=True)
else:
    # Isso é necessário para o Vercel
    app = app