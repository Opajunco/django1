let ciudades =[]


const listarObras = async () => {
    try {
        const response=await fetch(`./get-obras/`);
        const data=await response.json();
        console.log(data);
        indice=0;
        indice_ended=0;
        indicebloque=0;
        if(data.message =="Success"){
            obras = data.obras;
            let html=``;

            // obras.forEach((obra) => {
            //     html +=`<p>${obra.id} ${obra.titulo} ${obra.ended} ----------- ${obra.concepto} ${obra.comentarios} ${obra.porcGg} ${obra.porcBi} ${obra.gastosFijos}</p>`;
            // });

            obras.forEach((obra) => {

                if (obra.ended == false) {indice_ended = 1} else{indice:indice_ended =2}
                if (indice_ended != indicebloque) { 
                    html += `
                    <div class="rowfran bloque">
                    <div class="checkdivfran">
                      <input class="checkfran" name='${indice_ended}' type="checkbox" data-checkparent=${indice_ended}>
                    </div>
                    <div class="" style="width:600px;margin-top:20px;margin-left:20px"><label class="" for="parentid2"><strong>Bloque ${indice_ended}</strong></label></div>
                  </div>
                    
                    `
                
                }

                html +=`<div class="rowfran"><div class="checkdivfran">
                <input class="checkfran form-check-input" type="checkbox" id="${obra.id}"
                   data-checkid="${indice}" data-checkchild = ${indice_ended}
                   name="${obra.id}" value="${obra.id}">
                </div>
                <div class=""style="width:600px;margin-top:20px;margin-left:20px">
                <label class="form-group form-check-label pl-5 unselectable not-selectable" for="checkid{{i}}">${obra.titulo}</label>
                </div>
                </div>`   
                indice +=1;
                indicebloque = indice_ended;
            });

                

            divobras.innerHTML = html;
            // mostrarAlcalde(ciudades[0].id);
            // cargadivs();
        }else{
            alert("Obras no encontradas ...")
        }
        
    } catch (error) {
        console.log(error)
    }
}



const cargaInicial = async () => {
    await listarObras();
    await cargadivs();
};

window.addEventListener("load", async () => {
    await cargaInicial();
    await cargadivs();

});

