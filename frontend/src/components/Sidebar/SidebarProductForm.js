import React,{useState, useEffect, Component} from 'react'; 
import { useForm, getValues } from "react-hook-form";
import MultiSelect from "react-multi-select-component"
import * as API from "Api/Api"

function ProductSidebarForm (props) {


  const { register, handleSubmit, errors, getValues } = useForm()

 
  


  





  const onSubmit = data => {
    props.SetDataCarrito(props.DataCarrito.concat(props.DataMostrar))
   
  };


  return ( 


    <form onSubmit={handleSubmit(onSubmit)}>  

      { ["encimeras", "inventario", "fregaderos"].includes(props.page) ? 
        <div>
        <hr/>
        Material
        <MultiSelect 
          hasSelectAll = {false}
          options      = {props.Options.material}
          value        = {props.Filtros.material}
          onChange     = {(event) => props.setFiltros({...props.Filtros, material: event})}
          labelledBy   = {"Selecciona el material"}
        />      
        </div>
        : null
      }

      { ["encimeras", "inventario", "fregaderos"].includes(props.page) ? 
        <div>
        <hr/>
        Color
        <MultiSelect 
          options={props.Options.color}
          value={props.Filtros.color}
          onChange     = {(event) => props.setFiltros({...props.Filtros, color: event})}
          labelledBy={"Selecciona el color"}
        />
        </div>
        : null
      }

      { ["encimeras", "inventario"].includes(props.page) ? 
        <div>
        <hr/>
        Acabado
        <MultiSelect 
          options={props.Options.acabado}
          value={props.Filtros.acabado}
          onChange     = {(event) => props.setFiltros({...props.Filtros, acabado: event})}
          labelledBy={"Selecciona el acabado"}
        />
        </div>
        : null
      }

      { ["encimeras", "inventario"].includes(props.page) ? 
        <div>
        <hr/>
        Grosor
        <MultiSelect 
          options={props.Options.grosor}
          value={props.Filtros.grosor}
          onChange     = {(event) => props.setFiltros({...props.Filtros, grosor: event})}
          labelledBy={"Selecciona el grosor"}
        />
        </div>
        : null
      }


      { ["inventario", "inventario", "fregaderos"].includes(props.page) ? 
        <div>
        <hr/>
        Medida
        <MultiSelect 
          options={props.Options.medida}
          value={props.Filtros.medida}
          onChange     = {(event) => props.setFiltros({...props.Filtros, medida: event})}
          labelledBy={"Selecciona la medida"}
        />
        </div>
        : null
      }
     
    
      { ["suplementos"].includes(props.page) ? 
        <div>
        <hr/>
        Concepto
        <MultiSelect 
          options={props.Options.concepto}
          value={props.Filtros.concepto}
          onChange     = {(event) => props.setFiltros({...props.Filtros, concepto: event})}
          labelledBy={"Selecciona el concepto"}
        />
        </div>
        : null
      }
      { ["suplementos"].includes(props.page) ? 
        <div>
        <hr/>
        Cantidad
        <input name = "cantidad" defaultValue="0" id = "cantidad" type="number" step="0.01" className = "form-control" onSubmit = {(event) => event.preventDefault()} onChange={(event) => props.setFiltros({...props.Filtros, cantidad: event.target.value})}/>
        </div>
        : null
      }

      <hr/>
      <input type="submit"  name = "submit" className=" btn btn-gradient rounded transform-0" />
     
    </form>           
  ); 
} 
  
  export default ProductSidebarForm; 