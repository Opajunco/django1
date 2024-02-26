let ciudades = []

var checks

var response 
const listarPartidas = async () => {

    // alert(idObra);
    try {
        // indice = 0;
        // indice_ended = 0;
        // indicebloque = 0;
        // cuidado repsonse estaba con const
        response = await fetch(`../../getpartis/${idObra}/`);
        const data = await response.text();
        // console.log(data);
        partis.innerHTML = data;
        // checks = document.querySelectorAll("input[data-checkid]");


        // if (data.message == "Success") {
        //     obras = data.obras;
        //     let html = ``;

        //     // obras.forEach((obra) => {
        //     //     html +=`<p>${obra.id} ${obra.titulo} ${obra.ended} ----------- ${obra.concepto} ${obra.comentarios} ${obra.porcGg} ${obra.porcBi} ${obra.gastosFijos}</p>`;
        //     // });

        //     obras.forEach((obra) => {

        //         if (obra.ended == false) { indice_ended = 1 } else { indice: indice_ended = 2 }
        //         if (indice_ended != indicebloque) {
        //             html += `
        //             <div class="rowfran bloque">
        //             <div class="checkdivfran">
        //               <input class="checkfran" name='${indice_ended}' type="checkbox" data-checkparent=${indice_ended}>
        //             </div>
        //             <div class="" style="width:600px;margin-top:20px;margin-left:20px"><label class="" for="parentid2"><strong>Bloque ${indice_ended}</strong></label></div>
        //           </div>

        //             `

        //         }

        //         html += `<div class="rowfran"><div class="checkdivfran">
        //         <input class="checkfran form-check-input" type="checkbox" id="${obra.id}"
        //            data-checkid="${indice}" data-checkchild = ${indice_ended}
        //            name="${obra.id}" value="${obra.id}">
        //         </div>
        //         <div class=""style="width:600px;margin-top:20px;margin-left:20px">
        //         <a class="form-group form-check-label pl-5 unselectable not-selectable" href= "./partidas/${obra.id}/ ">${obra.titulo}</a>
        //         </div>
        //         </div>`
        //         indice += 1;
        //         indicebloque = indice_ended;
        //     });



        //     divobras.innerHTML = html;
        //     // mostrarAlcalde(ciudades[0].id);
        //     // cargadivs();
        // } else {
        //     alert("Obras no encontradas ...")
        // }



    } catch (error) {
        console.log(error)
    }
}

const editfieldspartis = async () => {
    comments = document.querySelectorAll("div[data-commentid]");
    for (let i = 0; i < comments.length; i++) {

        // const div = document.querySelector("div")
        // const observer = new MutationObserver((mutationRecords) => {
        //     console.log(mutationRecords.target.data)
        // })
        // observer.observe(this, {
        //     characterData: true,
        //     subtree: true,
        // })


//edita comentarios!!!!
// podemos ponerlo cuando focusout o cuando input. El input lógicamente hace más llamadas a la base de datos
        comments[i].addEventListener("focusout", function () {

            console.log(`comentario ${this.getAttribute("data-commentid")} ha cambiado`)
            console.log(encodeURI(this.innerText))
            fetch(`../../editfieldspartis/update-comment/${this.getAttribute("data-commentid")}/${encodeURI(this.innerText)}/`)
        })
    }


    medis = document.querySelectorAll("input[data-medid]");
    for (let i = 0; i < medis.length; i++) {
        actualizaPrecioGen(medis[i])
        medis[i].addEventListener("change", async function () {

            console.log(`comentario ${this.getAttribute("data-medid")} ha cambiado`)            
            const response = await fetch(`../../editfieldspartis/update-med/${this.getAttribute("data-medid")}/${this.value}/`)
            const data = await response.json()
            var cantidad = data.cantidad
            this.value = cantidad

            actualizaPrecioGen(this)

            // this.value = cantidad
            // var precioUnit = this.parentElement.parentElement.getElementsByClassName('precioUnit')[0].innerText
            // precio = precioUnit * cantidad   
            // this.parentElement.parentElement.getElementsByClassName('precio')[0].innerText = precio                     

        })
    }

    titles = document.querySelectorAll("input[data-titleid]");
    for (let i = 0; i < titles.length; i++) {
        
        titles[i].addEventListener("change", async function () {

            console.log(`title ${this.getAttribute("data-titleid")} ha cambiado`)            
            fetch(`../../editfieldspartis/update-title/${this.getAttribute("data-titleid")}/${this.value}/`)                  

        })
    }



}


function actualizaPrecioGen(medElement){

    cantidad = medElement.value
    var precioUnit = Number(medElement.parentElement.parentElement.getElementsByClassName('precioUnit')[0].innerText)
    console.log(`cantidad: ${cantidad}`)
    console.log(precioUnit)
    precio = precioUnit * cantidad 
    medElement.parentElement.parentElement.getElementsByClassName('precio')[0].innerText = precio.toLocaleString('es', { style: 'currency', currency: 'EUR' });
    medElement.parentElement.parentElement.getElementsByClassName('precio')[0].setAttribute('value', precio)
    totalPem();

}


// mejorar
function totalPem(){
    precios = document.getElementsByClassName('precio');
    var pemTotal = 0;
    for (let i = 0; i < precios.length; i++) {
        // pemTotal = Number(precios[i].getAttribute('value')) + pemTotal
        pemTotal = Number(precios[i].getAttribute('value')) + pemTotal
        console.log (pemTotal)  
        pem.innerText = pemTotal.toLocaleString('es', { style: 'currency', currency: 'EUR' })         
    }

}



const cargaInicial = async () => {
    await listarPartidas();
};





function prueba(jsonvalue) {
    console.log("ya estamos en la funcion de callback")
    console.log(jsonvalue);
}




window.addEventListener("load", async () => {
    await cargaInicial();
    await cargadivs();
    await editfieldspartis();
    busqueda("../../obras/get-partidas-json/",prueba);
});
