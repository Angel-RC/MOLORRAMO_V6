import React from "react";
import { useForm } from "react-hook-form";
import {
    Badge,
    Button,
    ButtonGroup,
    Row,
    Col,
  } from "react-bootstrap";

function InvoiceInfo(props) {
  const { register, handleSubmit, errors } = useForm();
  const onSubmit = data => console.log(data);

  const handleChange = data => {
  props.SetInfo({...props.Info, [data.target.name]: data.target.value});
 
}
  
  return (
    <form   onSubmit={handleSubmit(onSubmit)}>
        <h4>Emisor:</h4>
        <Row>
              
            <Col md="3">
                <label>Nombre: </label>
                <input className = "form-control"  type = "text" name="name_emisor" id ="name_emisor"  ref={register} onChange = {handleChange} />
                </Col>
                <Col md="3"> 
                <label>Email</label>
                <input className = "form-control"  type = "email" name="email_emisor" id ="email_emisor"  ref={register} onChange = {handleChange} />
                </Col>
                <Col md="2">
                <label>Telefono</label>
                <input className = "form-control"  type = "text" name="telefono_emisor" id ="telefono_emisor"  ref={register} onChange = {handleChange} />
                </Col>
                <Col md="4">
                <label>Dirección</label>
                <input className = "form-control"  type = "text" name="adress_emisor" id ="adress_emisor"  ref={register} onChange = {handleChange} />
            </Col>
            </Row>
            <hr/>
            <h4>Receptor:</h4>
        <Row>
              
            <Col md="3">
                <label>Nombre: </label>
                <input className = "form-control"  type = "text" name="name_receptor" id ="name_receptor"  ref={register}  onChange = {handleChange}/>
                </Col>
                <Col md="3"> 
                <label>Email</label>
                <input className = "form-control"  type = "email" name="email_receptor" id ="email_receptor"  ref={register} onChange = {handleChange} />
                </Col>
                <Col md="2">
                <label>Telefono</label>
                <input className = "form-control"  type = "text" name="telefono_receptor" id ="telefono_receptor"  ref={register} onChange = {handleChange} />
                </Col>
                <Col md="4">
                <label>Dirección</label>
                <input className = "form-control"  type = "text" name="adress_receptor" id ="adress_receptor"  ref={register} onChange = {handleChange} />
            </Col>
            </Row>
            <hr/>

            <Row>
            <Col md="4">
                <label>Fecha Pedido</label>
                <input className = "form-control" Defaultvalue="2018-07-22" type = "date" name="fecha_pedido" id ="fecha_pedido"  ref={register} onChange = {handleChange} />
            </Col>
            <Col md="4">
                <label>Fecha Medicion</label>
                <input className = "form-control" disabled type = "date" name="fecha_medicion" id ="fecha_medicion"  ref={register} onChange = {handleChange} />
            </Col>
            <Col md="4">
                <label>Fecha Entrega</label>
                <input className = "form-control"  type = "date" name="fecha_entrega" id ="fecha_entrega"  ref={register} onChange = {handleChange} />
            </Col>
           
      </Row>
      <hr/>
    </form>
    
  );
}

export default InvoiceInfo;
