import * as constant from "constant/index"

export async function filterData(page, DataInicial, Filtros, setDataMostrar, Options, setOptions){
    console.log("llamada a api filter")
    var body = {"page": page, "Filtros": Filtros, "data": DataInicial}
   

    const response = await fetch(constant.URL_FILTER_DATA,{
        method : "POST",
        body : JSON.stringify(body)})
    
    const response1 = await response.json();
    
    const data = await setDataMostrar(response1.data);
    const options = await setOptions(response1.options);
                
}

export async function CreateDataInicial(page, Metros,  setDataInicial, setOptions){
    console.log("llamada a api create")
    var body = {"page": page, "Metros": Metros}

    const response = await fetch(constant.URL_CREATE_DATA_INICIAL,{
        method : "POST",
        body : JSON.stringify(body)})

    const response1 = await response.json();

    const data = await setDataInicial(response1.data);
    const options = await setOptions(response1.options);

   
        
      
}
