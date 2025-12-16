document.addEventListener('DOMContentLoaded', function(){

    const produtos = document.querySelectorAll('.produto');
    
    const formatarBRL = (valor) => {
        return valor.toLocaleString('pt-BR', { 
          minimumFractionDigits: 2, 
          maximumFractionDigits: 2, 
          style: 'currency',
          currency : 'BRL',
     });
    };

    produtos.forEach((produto)=> {

          const valor_element = produto.querySelector('.valor_total');
          const quantidade_element = produto.querySelector('.quantidade_p');
            
          const quantidade_real = quantidade_element.getAttribute('data-quantidade');
          const valor_real = valor_element.getAttribute('data-valor');

          const valor_formatado = parseFloat(valor_real) || 0; 
          const quantidade_formatada = parseInt(quantidade_real) || 0;

          const valor_final = valor_formatado * quantidade_formatada;

          if (!isNaN(valor_final)) {
                
           const valor_formatado_br = formatarBRL(valor_final);
                
           valor_element.textContent = valor_formatado_br;
               }
    });
    
    setTimeout(()=>{
        const msg = document.querySelector('.alert');
        if (msg){
            msg.style.display ='none';
        }
    },4000 );
});