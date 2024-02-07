// function busqueda(url, vars = "") {
//   // recogemos las variables de la pagina (idObra, idUsuario, etc..)
//   // y la unimos con la del texto de busqueda q  y lo mandamos todo a load a la url correspondiente

//   var textInput = document.getElementById("txtSearch");
//   var timeout = null;
//   textInput.onkeyup = function (e) {
//     clearTimeout(timeout);
//     // Make a new timeout set to go off in 800ms
//     timeout = setTimeout(function () {
//       // var json1 = vars;
//       // var json2 = { q: textInput.value };
//       // var json3 = $.extend(false, {}, json1, json2);

//       // load(url, json3);

//       // console.log('Input Value:', textInput.value);
//     }, 200);
//   };
// } //end busqueda

// const listarPaises = async () => {
//   try {
//     const response = await fetch("./paises");
//     const data = await response.json();
//     console.log(data);

//     if (data.message == "Success") {
//       let opciones = ``;
//       data.paises.forEach((pais) => {
//         opciones += `<option value='${pais.id}'>${pais.nombre}</option>`;
//       });
//       cboPais.innerHTML = opciones;
//       listarCiudades(data.paises[0].id);
//     } else {
//       alert("Paises no encontrados ...")
//     }

//   } catch (error) {
//     console.log(error)
//   }


// }

// const cargaInicial = async () => {
//   await busqueda();
// };

function busqueda(url,funcion){

  timeout = null;
txtSearch.addEventListener("keyup",(event)=>{
  clearTimeout(timeout);
  timeout = setTimeout(function () {
    // var json1 = vars;
    // var json2 = { q: textInput.value };
    // var json3 = $.extend(false, {}, json1, json2);

    // load(url, json3);

    // console.log('Input Value:', textInput.value);
    // listarCiudades(event.target.value);
  // console.log(event)
  // console.log(event.target)


  // console.log(event.target.value);
  getjson(event.target.value, url);
  //  console.log(getjson(event.target.value, url));



  // funcion(data);

  }, 600);

});



}

function prueba(jsonvalue) {
  console.log(jsonvalue);
}

window.addEventListener("load", async () => {
  await busqueda('../../obras/get-partidas-json/', prueba);
});




const getjson = async (texto,url) => {
  // try {
      const response = await fetch(`${url}${texto}`);
      const data = await response.json();
      console.log(data)

  //     if(data.message =="Success"){
  //         let opciones=``;
  //         data.paises.forEach((pais) => {
  //             opciones +=`<option value='${pais.id}'>${pais.nombre}</option>`;
  //         });
  //         cboPais.innerHTML = opciones;
  //         listarCiudades(data.paises[0].id);
  //     }else{
  //         alert("Paises no encontrados ...")
  //     }
      
  // } catch (error) {
  //     console.log(error)
  // }


}



