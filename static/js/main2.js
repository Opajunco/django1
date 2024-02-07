
// esta funcion es para conectarse a urls con un parametro str que devuelva un json.

//ejemplo getjson("a","../../obras/get-partidas-json/")
const getjson = async (texto, url) => {
    const response = await fetch(`${url}${texto}`);
    const data = response.json();
    // console.log(data);
    return data
}

//importante que el input de la búsqueda tenga id = "txtSearch"

// en general si para ejecutar una funcion dentro existe una función con latencia, si quiero que se pare el codigo hasta obtener el resultado de esa funcion con latencia, tengo que hacer la función asincrona con async y luego usar el await donde quiera que se espere.
function busqueda(url, funcion) {
    timeout = null;
    txtSearch.addEventListener("keyup", (event) => {

        clearTimeout(timeout);

        timeout = setTimeout( async function () {
            console.log("esto está antes del callback")
            const data = await getjson(event.target.value, url);
            funcion(data);                      
            console.log("esto está despues del callback")         
        }, 600);

    });
}


// esto ya iría en los js de cada pagina
// la funcion que usa la funcion busqueda tiene debe tener un solo argumento que es el json

function prueba(jsonvalue) {
    console.log("ya estamos en la funcion de callback")
    console.log(jsonvalue);
}


busqueda("../../obras/get-partidas-json/",prueba);