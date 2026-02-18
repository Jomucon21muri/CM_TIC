// Funcionalidades JavaScript personalizadas para el curso TICD
document.addEventListener('DOMContentLoaded', function() {
    // Inicialización de funciones
    initProgressTracking();
    initChecklistPersistence();
    initStatistics();
});

// Guardar progreso de checklists en localStorage
function initChecklistPersistence() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
    checkboxes.forEach((checkbox, index) => {
        // Cargar estado guardado
        const savedState = localStorage.getItem(`checkbox_${index}`);
        if (savedState === 'true') {
            checkbox.checked = true;
        }
        
        // Guardar cambios
        checkbox.addEventListener('change', function() {
            localStorage.setItem(`checkbox_${index}`, this.checked);
            updateProgress();
        });
    });
}

// Seguimiento de progreso general
function initProgressTracking() {
    const progressKey = 'ticd_course_progress';
    
    // Cargar progreso
    let progress = JSON.parse(localStorage.getItem(progressKey) || '{}');
    
    // Mostrar progreso si existe un contenedor
    const progressContainer = document.getElementById('course-progress');
    if (progressContainer &&Object.keys(progress).length > 0) {
        displayProgress(progressContainer, progress);
    }
}

function updateProgress() {
    const totalChecks = document.querySelectorAll('input[type="checkbox"]').length;
    const checkedBoxes = document.querySelectorAll('input[type="checkbox"]:checked').length;
    
    if (totalChecks > 0) {
        const percentage = Math.round((checkedBoxes / totalChecks) * 100);
        localStorage.setItem('ticd_progress_percentage', percentage);
        
        // Actualizar indicador visual si existe
        const indicator = document.getElementById('progress-indicator');
        if (indicator) {
            indicator.textContent = `${percentage}% completado`;
            indicator.style.width = percentage + '%';
        }
    }
}

function displayProgress(container, progress) {
    const html = `
        <div class="progress-summary">
            <h3>Tu Progreso</h3>
            <div class="progress-bar">
                <div class="progress-fill" id="progress-indicator"></div>
            </div>
        </div>
    `;
    container.innerHTML = html;
    updateProgress();
}

// Estadísticas de cuestionarios
function initStatistics() {
    const statsKey = 'ticd_quiz_statistics';
    let stats = JSON.parse(localStorage.getItem(statsKey) || '{}');
    
    // Función para guardar resultado de cuestionario
    window.saveQuizResult = function(module, questions, correct, time) {
        if (!stats[module]) {
            stats[module] = {
                attempts: 0,
                totalQuestions: 0,
                totalCorrect: 0,
                totalTime: 0,
                bestScore: 0
            };
        }
        
        const score = Math.round((correct / questions) * 100);
        
        stats[module].attempts++;
        stats[module].totalQuestions += questions;
        stats[module].totalCorrect += correct;
        stats[module].totalTime += time;
        stats[module].bestScore = Math.max(stats[module].bestScore, score);
        
        localStorage.setItem(statsKey, JSON.stringify(stats));
        return stats[module];
    };
    
    // Función para obtener estadísticas
    window.getQuizStatistics = function(module) {
        return stats[module] || null;
    };
    
    // Función para resetear estadísticas
    window.resetQuizStatistics = function() {
        if (confirm('¿Estás seguro de que quieres borrar todas las estadísticas?')) {
            localStorage.removeItem(statsKey);
            stats = {};
            alert('Estadísticas borradas correctamente');
        }
    };
}

// Función para exportar progreso
window.exportProgress = function() {
    const progress = {
        checkboxes: [],
        quizStats: localStorage.getItem('ticd_quiz_statistics'),
        percentage: localStorage.getItem('ticd_progress_percentage'),
        date: new Date().toISOString()
    };
    
    // Guardar estados de checkboxes
    document.querySelectorAll('input[type="checkbox"]').forEach((cb, i) => {
        progress.checkboxes.push({
            index: i,
            checked: cb.checked
        });
    });
    
    // Crear blob y descargar
    const blob = new Blob([JSON.stringify(progress, null, 2)], {
        type: 'application/json'
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `ticd-progreso-${new Date().toISOString().split('T')[0]}.json`;
    a.click();
    URL.revokeObjectURL(url);
};

// Función para importar progreso
window.importProgress = function(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const progress = JSON.parse(e.target.result);
            
            // Restaurar checkboxes
            if (progress.checkboxes) {
                progress.checkboxes.forEach(item => {
                    localStorage.setItem(`checkbox_${item.index}`, item.checked);
                });
            }
            
            // Restaurar estadísticas
            if (progress.quizStats) {
                localStorage.setItem('ticd_quiz_statistics', progress.quizStats);
            }
            
            // Restaurar porcentaje
            if (progress.percentage) {
                localStorage.setItem('ticd_progress_percentage', progress.percentage);
            }
            
            alert('Progreso importado correctamente. Recarga la página para ver los cambios.');
            location.reload();
        } catch (error) {
            alert('Error al importar el archivo. Asegúrate de que es un archivo válido.');
            console.error(error);
        }
    };
    reader.readAsText(file);
};

// Smooth scroll para enlaces internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Copiar código al portapapeles con feedback
document.querySelectorAll('pre code').forEach((block) => {
    const button = document.createElement('button');
    button.className = 'copy-code-button';
    button.textContent = '📋 Copiar';
    button.title = 'Copiar código';
    
    button.addEventListener('click', async () => {
        const code = block.textContent;
        try {
            await navigator.clipboard.writeText(code);
            button.textContent = '✅ Copiado!';
            setTimeout(() => {
                button.textContent = '📋 Copiar';
            }, 2000);
        } catch(err) {
            button.textContent = '❌ Error';
            setTimeout(() => {
                button.textContent = '📋 Copiar';
            }, 2000);
        }
    });
    
    block.parentElement.style.position = 'relative';
    block.parentElement.appendChild(button);
});

// Print-friendly: añadir fecha al imprimir
window.addEventListener('beforeprint', () => {
    const printDate = document.createElement('div');
    printDate.className = 'print-date';
    printDate.innerHTML = `Impreso el: ${new Date().toLocaleDateString('es-ES')}`;
    document.body.prepend(printDate);
});

window.addEventListener('afterprint', () => {
    const printDate = document.querySelector('.print-date');
    if (printDate) printDate.remove();
});

console.log('🎓 Curso TICD - Sistema cargado correctamente');
console.log('📊 Funciones disponibles: exportProgress(), importProgress(file), resetQuizStatistics()');
