import React from "react";
import { useForm } from "react-hook-form";
import {
    Badge,
    Button,
    ButtonGroup,
    Row,
    Col,
  } from "react-bootstrap";

function InvoiceDates(props) {
  const { register, handleSubmit, errors } = useForm();
  const onSubmit = data => console.log(data);
  
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
        <Row>
            <Col md="4">
                <label>Fecha Pedido</label>
                <input className = "form-control" Defaultvalue="2018-07-22" type = "date" name="fecha_pedido" id ="fecha_pedido"  ref={register} />
            </Col>
            <Col md="4">
                <label>Fecha Medicion</label>
                <input className = "form-control" disabled type = "date" name="fecha_medicion" id ="fecha_medicion"  ref={register} />
            </Col>
            <Col md="4">
                <label>Fecha Entrega</label>
                <input className = "form-control"  type = "date" name="fecha_entrega" id ="fecha_entrega"  ref={register} />
            </Col>
           
      </Row>
      <hr/>
    </form>
    
  );
}

export default InvoiceDates;
