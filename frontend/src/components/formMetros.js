import React from "react";
import { useForm } from "react-hook-form";
import {
    Badge,
    Button,
    ButtonGroup,
    Row,
    Col,
  } from "react-bootstrap";

function formMetros(props) {
  const { register, handleSubmit, errors } = useForm();
  const onSubmit = data => console.log(data);
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
        <Row>
            <Col md="4">
                <label>Metros lineales</label>
                <input className = "form-control" onChange={(event) => props.setMetros({...props.Metros, lineales: event.target.value})} type = "number" name="metros_lineales" id ="metros_lineales" defaultValue="0" ref={register} />
            </Col>
            <Col md="4">
                <label>Metros cuadrados</label>
                <input className = "form-control" onChange={(event) => props.setMetros({...props.Metros, cuadrados: event.target.value})} type = "number" name="metros_cuadrados" id ="metros_cuadrados" defaultValue="0" ref={register} />
            </Col>
            <Col md="4">
                <label>Metros de frente</label>
                <input className = "form-control" type = "number" onChange={(event) => props.setMetros({...props.Metros, frente: event.target.value})} name="metros_frente" id ="metros_frente" defaultValue="0" ref={register} />
            </Col>
      </Row>
      <hr/>
    </form>
    
  );
}

export default formMetros;
