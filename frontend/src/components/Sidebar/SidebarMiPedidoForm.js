import React,{useState, useEffect, Component} from 'react'; 
import { useForm, getValues } from "react-hook-form";
import MultiSelect from "react-multi-select-component"
import * as API from "Api/Api"

function SidebarMiPedidoForm (props) {


  const { register, handleSubmit, errors, getValues } = useForm()

 
  const onSubmit = data => {
    props.SetDataCarrito(props.DataCarrito.concat(props.DataMostrar))
   
  };


  return ( 

    <form onSubmit={handleSubmit(onSubmit)}>  

    
<hr/>
     
<label>P.V.P</label>
      <input className = "form-control" type="number"  id = "pvp" name = "pvp" step = "0.01" />
  
      <hr/>
      <input type="submit"  name = "submit" className=" btn btn-gradient rounded transform-0" />
     
    </form>           
  ); 
} 
  
  export default SidebarMiPedidoForm; 