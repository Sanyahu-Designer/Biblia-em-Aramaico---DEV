// Debug utilities
const debugLogger = {
    init() {
        console.log('Debug initialized');
        this.checkFontLoading();
        this.checkAPIEndpoints();
    },

    checkFontLoading() {
        document.fonts.ready.then(() => {
            const fontLoaded = document.fonts.check('1em "Estrangelo Edessa"');
            console.log('Estrangelo Edessa font loaded:', fontLoaded);
        });
    },

    checkAPIEndpoints() {
        const bookSelect = document.getElementById('book-select');
        if (bookSelect) {
            console.log('Book select found:', bookSelect.value);
            bookSelect.addEventListener('change', (e) => {
                console.log('Book selection changed:', e.target.value);
                console.log('Attempting to fetch chapters from:', `/get-chapters/?book_id=${e.target.value}`);
            });
        } else {
            console.error('Book select element not found');
        }
    }
};

// Initialize debug logging
document.addEventListener('DOMContentLoaded', () => {
    debugLogger.init();
});