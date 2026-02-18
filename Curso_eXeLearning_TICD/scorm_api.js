/**
 * SCORM 1.2 API Wrapper
 * Proporciona comunicación básica con el LMS
 */

var scormAPI = null;
var scormInitialized = false;

/**
 * Busca el objeto API del SCORM en las ventanas padre
 */
function findAPI(win) {
    var attempts = 0;
    var maxAttempts = 500;
    
    while ((win.API == null) && (win.parent != null) && (win.parent != win)) {
        attempts++;
        if (attempts > maxAttempts) {
            return null;
        }
        win = win.parent;
    }
    return win.API;
}

/**
 * Obtiene el objeto API del SCORM
 */
function getAPI() {
    if (scormAPI == null) {
        scormAPI = findAPI(window);
    }
    return scormAPI;
}

/**
 * Inicializa la comunicación SCORM
 */
function initSCORM() {
    var api = getAPI();
    if (api == null) {
        console.log("SCORM API no encontrada - Modo standalone");
        return false;
    }
    
    var result = api.LMSInitialize("");
    if (result == "true") {
        scormInitialized = true;
        console.log("SCORM inicializado correctamente");
        return true;
    } else {
        console.log("Error al inicializar SCORM");
        return false;
    }
}

/**
 * Finaliza la comunicación SCORM
 */
function finishSCORM() {
    if (!scormInitialized) return;
    
    var api = getAPI();
    if (api != null) {
        api.LMSFinish("");
        scormInitialized = false;
        console.log("SCORM finalizado");
    }
}

/**
 * Establece el estado de completado
 */
function setCompleted() {
    if (!scormInitialized) return;
    
    var api = getAPI();
    if (api != null) {
        api.LMSSetValue("cmi.core.lesson_status", "completed");
        api.LMSCommit("");
        console.log("Estado establecido: completado");
    }
}

/**
 * Establece el estado de incompleto
 */
function setIncomplete() {
    if (!scormInitialized) return;
    
    var api = getAPI();
    if (api != null) {
        api.LMSSetValue("cmi.core.lesson_status", "incomplete");
        api.LMSCommit("");
        console.log("Estado establecido: incompleto");
    }
}

/**
 * Establece la puntuación
 */
function setScore(score, min, max) {
    if (!scormInitialized) return;
    
    var api = getAPI();
    if (api != null) {
        api.LMSSetValue("cmi.core.score.raw", score.toString());
        api.LMSSetValue("cmi.core.score.min", min.toString());
        api.LMSSetValue("cmi.core.score.max", max.toString());
        api.LMSCommit("");
        console.log("Puntuación establecida: " + score);
    }
}

/**
 * Obtiene el estado de la lección
 */
function getLessonStatus() {
    if (!scormInitialized) return "not attempted";
    
    var api = getAPI();
    if (api != null) {
        return api.LMSGetValue("cmi.core.lesson_status");
    }
    return "not attempted";
}

/**
 * Guarda la ubicación actual
 */
function setLocation(location) {
    if (!scormInitialized) return;
    
    var api = getAPI();
    if (api != null) {
        api.LMSSetValue("cmi.core.lesson_location", location);
        api.LMSCommit("");
    }
}

/**
 * Obtiene la ubicación guardada
 */
function getLocation() {
    if (!scormInitialized) return "";
    
    var api = getAPI();
    if (api != null) {
        return api.LMSGetValue("cmi.core.lesson_location");
    }
    return "";
}

// Inicializar SCORM cuando se carga la página
window.addEventListener('load', function() {
    initSCORM();
    
    // Marcar como incompleto al inicio
    if (scormInitialized) {
        var status = getLessonStatus();
        if (status == "not attempted") {
            setIncomplete();
        }
    }
});

// Finalizar SCORM cuando se cierra la página
window.addEventListener('beforeunload', function() {
    finishSCORM();
});

// Finalizar SCORM cuando se abandona la página
window.addEventListener('unload', function() {
    finishSCORM();
});
