document.addEventListener('DOMContentLoaded', function() {

    const campoBusca = document.getElementById('campo-busca');
 
    const linksProduto = document.querySelectorAll('.link-produto');

    campoBusca.addEventListener('keyup', function() {
        const termoBusca = campoBusca.value.toLowerCase();

        linksProduto.forEach(link => {

            const cardProduto = link.querySelector('.card-produto');
            
            const nomeProduto = cardProduto.getAttribute('data-nome-produto');

            if (nomeProduto.includes(termoBusca)) {
                link.style.display = ''; 
            } else {
                link.style.display = 'none';
            }
        });
    });
    const formatarBRL =(valor) => {
          return valor.toLocaleString('pt-BR', { 
          minimumFractionDigits: 2, 
          maximumFractionDigits: 2, 
          style: 'currency',
          currency : 'BRL',
            } )};
    
    const class_link = document.querySelectorAll('.link-produto');
    class_link.forEach((link) => {
        const preco = link.querySelector('.preco');
        let valor_string = preco.getAttribute('data-valor');

        let valor = parseFloat(valor_string)
        
        const valor_formatado = formatarBRL(valor);

        preco.textContent = valor_formatado
    });


    setTimeout(()=>{
            const msg = document.getElementById('messages');
            if (msg){
                 msg.style.display ='none'
            }
        },4000 );
});