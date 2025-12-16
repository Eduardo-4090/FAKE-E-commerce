
    document.addEventListener('DOMContentLoaded', function() {
        const imagemPrincipal = document.querySelector('.img-principal img');
        const miniaturas = document.querySelectorAll('.mini-img img');
        
   
        function setActive(element) {
            document.querySelectorAll('.mini-img').forEach(div => {
                div.classList.remove('ativo');
            });
            element.parentNode.classList.add('ativo');
        }


        miniaturas.forEach(miniatura => {
            miniatura.addEventListener('click', function() {
                
                imagemPrincipal.src = this.src;
                
                setActive(this);
            });
        });

        const primeiraMinia = document.querySelector('.mini-img');
        if (primeiraMinia) {
            primeiraMinia.classList.add('ativo');
        }
        const add_carrinho = document.querySelector('.btn-carrinho')
        const form = document.getElementById('add-carrinho-form')

        add_carrinho.addEventListener('click', function(){
            form.submit();
        });

        const formatarBRL =(valor) => {
          return valor.toLocaleString('pt-BR', { 
          minimumFractionDigits: 2, 
          maximumFractionDigits: 2, 
          style: 'currency',
          currency : 'BRL',
            } )};

        const preco = document.querySelector('.preco');
        let valor_string = preco.getAttribute('data-valor');

        let valor = parseFloat(valor_string)
        
        const valor_formatado = formatarBRL(valor);

        preco.textContent = valor_formatado

        setTimeout(()=>{
            const msg = document.getElementById('messages');
            if (msg){
                 msg.style.display ='none'
            }
        },4000 );
    })