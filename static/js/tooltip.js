// Inicialização dos tooltips
document.addEventListener('DOMContentLoaded', function() {
    // Procura por todas as palavras com tooltip no texto
    const tooltipWords = document.querySelectorAll('.tooltip-word');
    
    // Adiciona listeners para eventos de toque em dispositivos móveis
    tooltipWords.forEach(word => {
        word.addEventListener('touchstart', function(e) {
            e.preventDefault();
            const tooltip = this.getAttribute('data-tooltip');
            
            // Remove qualquer tooltip ativo anterior
            const activeTooltip = document.querySelector('.mobile-tooltip');
            if (activeTooltip) {
                activeTooltip.remove();
            }
            
            // Cria e posiciona o tooltip
            const mobileTooltip = document.createElement('div');
            mobileTooltip.className = 'mobile-tooltip';
            mobileTooltip.textContent = tooltip;
            
            // Posiciona o tooltip acima da palavra
            const rect = this.getBoundingClientRect();
            mobileTooltip.style.position = 'fixed';
            mobileTooltip.style.top = (rect.top - 40) + 'px';
            mobileTooltip.style.left = (rect.left + (rect.width / 2)) + 'px';
            
            document.body.appendChild(mobileTooltip);
            
            // Remove o tooltip após 2 segundos
            setTimeout(() => {
                mobileTooltip.remove();
            }, 2000);
        });
    });
    
    // Fecha tooltip ao tocar fora
    document.addEventListener('touchstart', function(e) {
        if (!e.target.classList.contains('tooltip-word')) {
            const activeTooltip = document.querySelector('.mobile-tooltip');
            if (activeTooltip) {
                activeTooltip.remove();
            }
        }
    });
});