var total_configuracion=Math.floor(document.getElementById("total").value);
var dic = {"edAire":130,"edRueda":45,"edAndroid":220,"edCamara":291,"edTecho":1393,"edSonido":540}

function sumar(id) {
    for(var clave in dic) {
        if(id == clave){
            total_configuracion += dic[clave];
        }
    }
    document.getElementById("total").value=total_configuracion;
}

function restar(id) {
        for(var clave in dic) {
        if(id == clave){
            total_configuracion -= dic[clave];
        }
    }
    document.getElementById("total").value=total_configuracion;
}
