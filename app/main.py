from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(title="Swiss Gourmet", description="Site Institucional")

# --- CONFIGURAÇÃO DE DIRETÓRIOS ---
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

# Suporte flexível aos arquivos estáticos tanto em app/static quanto public/static
STATIC_DIR = BASE_DIR / "static"
if not STATIC_DIR.exists():
    STATIC_DIR = ROOT_DIR / "public" / "static"

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Configura os templates HTML
TEMPLATES_DIR = BASE_DIR / "templates" / "html"
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# --- DADOS INSTITUCIONAIS ---
DADOS = {
    "historia": [
        {"ano": "2007", "titulo": "O Início", "texto": "Nasce o Swiss Gourmet com a missão de trazer a autêntica comida de rua suíça para o Brasil."},
        {"ano": "2022", "titulo": "Expansão Asa Sul", "texto": "Levamos nossa experiência de queijos e sabores alpinos para a Asa Sul, conquistando novos paladares."},
        {"ano": "2024", "titulo": "Chegada na Asa Norte", "texto": "Inauguração da unidade Asa Norte, consolidando a marca como referência em Raclette em Brasília."},
        {"ano": "2025", "titulo": "O Novo Quituart", "texto": "Renovação e fortalecimento da nossa base histórica no Quituart, onde tudo começou."}
    ],
    "fundadora": {
        "nome": "Marília Rodrigues",
        "cargo": "Chef & Fundadora",
        "bio": "A alma por trás do Swiss Gourmet. Com paixão pela gastronomia de rua e pelas tradições suíças, Marília transformou o ato de comer queijo em uma experiência cultural em Brasília.",
        "foto": "marilia_rodrigues.png"
    },
    "influencers": [
        {"nome": "@InfluencerGourmet", "quote": "O melhor queijo que já comi em Brasília!", "foto": "inf1.png"},
        {"nome": "Guia Gastronômico", "quote": "Uma experiência imersiva. O cheiro é inebriante.", "foto": "inf2.png"}
    ],
    "midia_noticias": [
        {"texto": "Destaque no Metrópoles: nossa unidade na Funarte especializada em raclette.", "img": "metropoles_funarte.png"},
        {"texto": "Reconhecidos pelo Metrópoles como referência em raclette em Brasília.", "img": "metropoles_raclette.png"},
        {"texto": "Inovação em destaque na GPS Lifetime: o incrível Pizza Burger com raclette.", "img": "gps_pizzaburger.png"},
        {"texto": "Valorizando produtores: participação em evento com o queijo Brun de MS.", "img": "evento_queijo.png"}
    ],
    "festivais": [
        {"nome": "Burger Fest", "desc": "O maior roteiro gastronômico de hambúrgueres do Brasil.", "img": "burger_fest.png", "link": "https://www.instagram.com/burgerfestoficial/"},
        {"nome": "Festival CoMA", "desc": "Consciência, Música e Arte no coração de Brasília.", "img": ""},
        {"nome": "Villa Gourmet", "desc": "Edição especial no Pontão do Lago Sul inspirada em Campos do Jordão.", "img": ""},
        {"nome": "Nipo Festival", "desc": "Fusão de culturas no tradicional evento asiático.", "img": ""},
        {"nome": "Catarinafest", "desc": "Tradições do Sul do Brasil na capital federal.", "img": ""},
        {"nome": "Made in Japan", "desc": "O maior evento de cultura japonesa do Centro-Oeste.", "img": ""}
    ],
    "premios": ["Melhor Comida de Rua (Veja BSB)", "Destaque Gastronômico Quituart", "Referência em Raclette"]
}

# --- DESTAQUES DA HOME (Os 5 pedidos) ---
DESTAQUES = [
    {"nome": "Swiss Berna", "desc": "Queijo raclette, Burger 180g, molho Zurique e pastrami.", "img": "swiss-berna.jpg"},
    {"nome": "Swiss Salsichão", "desc": "Salsicha cervela, molho da rainha e bacon.", "img": "baguete-salsichao.jpg"},
    {"nome": "Lobster Roll", "desc": "Lascas de lagosta com manteiga de limão siciliano.", "img": "lobster-roll.jpg"},
    {"nome": "Batata Crosstrax", "desc": "Crocante com queijo parmesão.", "img": "crosstrax.jpg"},
    {"nome": "Raclette Chocolate", "desc": "Bolo de chocolate com raspa de raclette de chocolate.", "img": "sobremesa-raclette.jpg"}
]

# --- ROTAS DO SITE ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "title": "Swiss Gourmet - Início",
        "destaques": DESTAQUES
    })

@app.get("/menu", response_class=HTMLResponse)
async def menu(request: Request):
    # DADOS DO CARDÁPIO (Com 'destaque': True nos itens pedidos)
    cardapio = {
        "Hambúrgueres": [
            {"nome": "Swiss Burger", "desc": "Queijo raclette, Burger 180g, cebola caramelizada, bacon.", "preco": "R$ 42,00", "img": "swiss-burger.jpg"},
            {"nome": "Swiss Brie", "desc": "Queijo brie, geleia de pimenta, Burger 180g.", "preco": "R$ 42,00", "img": "swiss-brie.jpg"},
            {"nome": "Swiss 3 Queijos", "desc": "Burger 180g, bacon, queijo cheddar, queijo prato, queijo mussarela.", "preco": "R$ 38,00", "img": "swiss-3queijos.jpg"},
            # DESTAQUE
            {"nome": "Swiss Berna", "desc": "Queijo raclette, Burger 180g, molho Zurique, barbecue de rapadura, pastrami.", "preco": "R$ 42,00", "img": "swiss-berna.jpg", "destaque": True},
            {"nome": "Swiss Salad", "desc": "Queijo raclette, Burger 180g, alface, tomate cereja, molho Zurique.", "preco": "R$ 42,00", "img": "swiss-salad.jpg"},
            {"nome": "Swiss Burger Vegetariano", "desc": "Queijo raclette, Burger vegetariano, tomate cereja, alface, molho Zurique.", "preco": "R$ 42,00", "img": "swiss-veg.jpg"},
            {"nome": "Swiss Ancho", "desc": "Ancho, batata bolinha, tomate cereja com chimichurri e queijo raclette.", "preco": "R$ 79,00", "img": "swiss-ancho.jpg"},
            {"nome": "Swiss Tradicional", "desc": "Salsicha cervela, batata bolinha com ervas, cubos de bacon, picles, queijo raclette.", "preco": "R$ 49,00", "img": "swiss-tradicional.jpg"},
        ],
        "Baguetes": [
            # DESTAQUE
            {"nome": "Swiss Salsichão", "desc": "Queijo raclette, Salsicha cervela, molho da rainha, bacon, chimichurri.", "preco": "R$ 42,00", "img": "baguete-salsichao.jpg", "destaque": True},
            # DESTAQUE
            {"nome": "Lobster Roll (Sazonal)", "desc": "Lascas de lagosta, manteiga de limão siciliano, maionese da casa, vinagrete.", "preco": "R$ 65,00", "img": "lobster-roll.jpg", "destaque": True},
            {"nome": "Swiss Veggie", "desc": "Queijo cheddar vegano, salsicha vegetariana, maionese veganese, tomate cereja.", "preco": "R$ 42,00", "img": "baguete-veg.jpg"},
            {"nome": "Swiss Salsichão Vegetariano", "desc": "Queijo raclette, salsichão vegetariano, chimichurri, tomate cereja.", "preco": "R$ 45,00", "img": "baguete-salsichao-veg.jpg"},
            {"nome": "Swiss Picanha", "desc": "Queijo raclette, picanha fatiada, chimichurri, cubos de bacon.", "preco": "R$ 59,00", "img": "baguete-picanha.jpg"},
        ],
        "Pratos & Especialidades": [
            {
                "nome": "Parmegiana", 
                "desc": "O clássico gratinado com mussarela e molho de tomate caseiro. Acompanha arroz e batata frita. Escolha sua opção: Frango (R$ 45,00) ou Filet Mignon (R$ 59,00).", 
                "preco": "A partir de R$ 45,00", 
                "img": "parmegiana-filet.jpg"
            },
            {"nome": "São Galo", "desc": "Frango empanado no panko, creme de milho, arroz e legumes assados.", "preco": "R$ 45,00", "img": "sao-galo.jpg"},
            {"nome": "PF da Chefe", "desc": "Espetinho (carne ou frango), arroz, farofa, fritas, vinagrete, feijão de caldo.", "preco": "R$ 30,00", "img": "pf-chefe.jpg"},
            {"nome": "Zurcher Geshnetzeltes", "desc": "Filet mignon em tiras, molho bechamel e vinho branco, cogumelos frescos e Rösti.", "preco": "R$ 79,00", "img": "zurcher.jpg"},
        ],
        "Para Compartilhar": [
            {"nome": "Pão de Alho Poró", "desc": "Pão com pasta de alho poró e queijo ralado.", "preco": "R$ 18,00", "img": "pao-alho.jpg"},
            {"nome": "Batata Frita c/ Cheddar", "desc": "Porção de batata frita, cheddar e cubos de bacon.", "preco": "R$ 35,00", "img": "frita-cheddar.jpg"},
            {"nome": "Mini Pastel (6 un)", "desc": "Carne, queijo ou frango. Acompanha geleia de pimenta da casa.", "preco": "R$ 38,00", "img": "mini-pastel.jpg"},
            {"nome": "Batata Frita Parmesão", "desc": "Porção de batata frita com queijo parmesão ralado.", "preco": "R$ 35,00", "img": "frita-parmesao.jpg"},
            # DESTAQUE
            {"nome": "Batata Crosstrax", "desc": "Batata frita crosstrax crocante com parmesão.", "preco": "R$ 35,00", "img": "crosstrax.jpg", "destaque": True},
            {"nome": "Montreal", "desc": "Porção de Filet mignon fatiado, molho de gorgonzola e torradas.", "preco": "R$ 60,00", "img": "montreal.jpg"},
            {
                "nome": "Raclette de Mesa", 
                "desc": "Queijos (300g), Carnes (400g), Picles, Antepastos, Molhos, Pães, Bacon, Sobremesa.", 
                "preco": "R$ 250,00", 
                "img": "raclettes.jpg"
            },
            {"nome": "Fondue de Queijo", "desc": "Fondue (400ml), Pães, Torradas, Molhos, Carnes (300g), Batatas, Goiabada, Sobremesa.", "preco": "R$ 250,00", "img": "fondue.jpg"},
            {"nome": "Burrata Figueira", "desc": "Burrata, figos, pistache, barbecue de balsâmico, mix de folhas.", "preco": "R$ 89,00", "img": "burrata-figo.jpg"},
            {"nome": "Burrata com Ragu", "desc": "Burrata, ragu de linguiça toscana, pesto de manjericão.", "preco": "R$ 89,00", "img": "burrata-ragu.jpg"},
        ],
        "Combos": [
            {"nome": "Combo Miniaturas", "desc": "Batata pq, 1 mini burger, 1 mini brie, 1 mini salad, 1 mini berna.", "preco": "R$ 69,90", "img": "combo-miniaturas.jpg"},
            {"nome": "Combo Kids", "desc": "1 burger c/ mussarela, 1 refri lata ou suco, 1 batata.", "preco": "R$ 55,00", "img": "combo-kids.jpg"},
            {"nome": "Combo Clássico", "desc": "1 burger ou salsichão, 1 refri lata, 1 batata frita.", "preco": "R$ 70,00", "img": "combo-classico.jpg"},
            {"nome": "Combo Mini Burger", "desc": "6 mini hambúrgueres (pão, carne e cheddar).", "preco": "R$ 59,00", "img": "combo-mini-burger.jpg"},
            {"nome": "Combo Inverno", "desc": "1 burger raclette, 1 refri lata, 1 fondue de chocolate frutas.", "preco": "R$ 40,00", "img": "combo-inverno.jpg"},
        ],
        "Sobremesas": [
            # DESTAQUE
            {"nome": "Raclette de Chocolate", "desc": "Bolo de chocolate com raspa de raclette de chocolate.", "preco": "R$ 45,00", "img": "sobremesa-raclette.jpg", "destaque": True},
            {"nome": "S'mores", "desc": "8 marshmallows, creme de chocolate, 16 biscoitos.", "preco": "R$ 49,00", "img": "smores.jpg"},
        ]
    }
    
    return templates.TemplateResponse("menu.html", {"request": request, "title": "Cardápio | Swiss Gourmet", "cardapio": cardapio})

@app.get("/historia", response_class=HTMLResponse)
async def historia(request: Request):
    return templates.TemplateResponse("historia.html", {
        "request": request,
        "historia": DADOS["historia"],
        "premios": DADOS["premios"],
        "fundadora": DADOS["fundadora"],
        "title": "Nossa História - Swiss Gourmet"
    })

@app.get("/midia", response_class=HTMLResponse)
async def midia(request: Request):
    return templates.TemplateResponse("midia.html", {
        "request": request,
        "influencers": DADOS["influencers"],
        "noticias": DADOS["midia_noticias"],
        "festivais": DADOS["festivais"],
        "title": "Na Mídia e Eventos - Swiss Gourmet"
    })

@app.get("/localizacao", response_class=HTMLResponse)
async def localizacao(request: Request):
    return templates.TemplateResponse("localizacao.html", {"request": request, "title": "Localização - Swiss Gourmet"})