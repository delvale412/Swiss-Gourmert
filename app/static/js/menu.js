/* SWISS GOURMET - Lógica do Menu Interativo */

function openModal(element) {
    // 1. Pega os dados do cartão clicado
    const name = element.getAttribute('data-name');
    const desc = element.getAttribute('data-desc');
    const price = element.getAttribute('data-price');
    const img = element.getAttribute('data-img');
    const isDestaque = element.getAttribute('data-destaque');
    const serves = element.getAttribute('data-serves'); // Pega a informação de porção (Individual ou Dividir)
    
    // 2. Preenche os textos da janela modal
    document.getElementById('modalTitle').innerText = name;
    document.getElementById('modalDesc').innerText = desc;
    document.getElementById('modalPrice').innerText = price;
    document.getElementById('modalImg').src = img;
    
    // 3. Atualiza a etiqueta de "Serve X Pessoas"
    document.getElementById('modalServes').innerText = serves;

    // 4. Controla a exibição do selo "Destaque"
    const modalBadge = document.getElementById('modalBadge');
    if (isDestaque === 'true') {
        modalBadge.style.display = 'inline-flex';
    } else {
        modalBadge.style.display = 'none';
    }

    // 5. Mostra a janela com animação
    const modal = document.getElementById('productModal');
    modal.style.display = 'flex';
    setTimeout(() => {
        modal.classList.add('modal-open');
    }, 10);
}

function closeModal(event) {
    if (event.target.id === 'productModal') {
        closeModalDirect();
    }
}

function closeModalDirect() {
    const modal = document.getElementById('productModal');
    modal.classList.remove('modal-open');
    setTimeout(() => {
        modal.style.display = 'none';
    }, 300);
}

document.addEventListener('keydown', function(event) {
    if (event.key === "Escape") {
        closeModalDirect();
    }
});