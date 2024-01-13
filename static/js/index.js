let ciudades =[]


const listarCiudades = async (idPais) => {
    try {
        const response=await fetch(`./ciudades/${idPais}`);
        const data=await response.json();
        console.log(data);

        if(data.message =="Success"){
            ciudades = data.ciudades;
            let opciones=``;
            ciudades.forEach((ciudad) => {
                opciones +=`<option value='${ciudad.id}'>${ciudad.nombre}</option>`;
            });
            cboCiudad.innerHTML = opciones;
            mostrarAlcalde(ciudades[0].id);
        }else{
            alert("Paises no encontrados ...")
        }
        
    } catch (error) {
        console.log(error)
    }


}





const listarPaises = async () => {
    try {
        const response=await fetch("./paises");
        const data=await response.json();
        console.log(data);

        if(data.message =="Success"){
            let opciones=``;
            data.paises.forEach((pais) => {
                opciones +=`<option value='${pais.id}'>${pais.nombre}</option>`;
            });
            cboPais.innerHTML = opciones;
            listarCiudades(data.paises[0].id);
        }else{
            alert("Paises no encontrados ...")
        }
        
    } catch (error) {
        console.log(error)
    }


}


const mostrarAlcalde=(idCiudad)=>{
    let ciudadEncontrada=ciudades.filter((ciudad)=>ciudad.id==idCiudad);
    console.log(ciudadEncontrada)
    let alcalde = ciudadEncontrada[0].alcalde;
    txtAlcalde.innerHTML = `Alcalde: ${alcalde}`
}


const cargaInicial = async () => {
    await listarPaises();
};

window.addEventListener("load", async () => {
    await cargaInicial();
});

cboPais.addEventListener("change",(event)=>{
    console.log(event)
    console.log(event.target)
    console.log(event.target.value)
    listarCiudades(event.target.value);
});

cboCiudad.addEventListener("change",(event)=>{
    mostrarAlcalde(event.target.value);
})