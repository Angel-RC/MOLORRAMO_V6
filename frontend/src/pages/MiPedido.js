import React, {useState, useEffect, useLayoutEffect} from "react";
import { Switch, Route } from "react-router-dom";
// react-bootstrap components
import {
  Badge,
  Button,
  ButtonGroup,
  Card,
  Form,
  InputGroup,
  Navbar,
  Nav,
  Pagination,
  Container,
  Row,
  Col,
} from "react-bootstrap";


import DataTable from 'react-data-table-component';
// core components
import FormMetros from "components/formMetros"
import Sidebar from "components/Sidebar/Sidebar.js";
import AdminNavbar from "components/Navbars/AdminNavbar.js";
import SidebarProductForm from "components/Sidebar/SidebarProductForm"
import SidebarRoutes from "components/Sidebar/SidebarRoutes"
// Utils
import * as API from "Api/Api"
import * as constant from "constant/index"
import InvoiceInfo from "components/InvoiceInfo"
import SidebarMiPedidoForm from "components/Sidebar/SidebarMiPedidoForm";


function SelectProduct(props) {


  const [Options, setOptions] = useState({
    material : [], 
    color : [], 
    medida : [],
    acabado : [],
    grosor : [], 
    concepto: []
  })
  const [Filtros, setFiltros] = useState({
    material : [], 
    color : [], 
    medida : [],
    acabado : [],
    grosor : [], 
    concepto: [],
    cantidad : []
  });
  

  const [Info, SetInfo] = useState({})
  
  return (
    
    <div className="wrapper">

      <Sidebar
        page       = "Mi Pedido"
        routes     = {SidebarRoutes}
        content   = {<SidebarMiPedidoForm/>}
      />
      <div className="main-panel">
         
        <AdminNavbar />
         
        <div className="content">
          
          <Container fluid>
            <Row>
              <Col md="12">
                <Card >
                  <Card.Body>
                  <Card.Title><h2>Pedido y previsión de material</h2></Card.Title>
                      
                   <InvoiceInfo Info = {Info} SetInfo = {SetInfo}/>
                  { props.DataCarrito.encimeras.length > 0 ?
                  <>
                    <DataTable
                    title   = {"Encimeras"}
                    columns = {constant.columns.encimeras}
                    data    = {props.DataCarrito.encimeras}
                  />
                  <hr/>
                  </>
                   : null}
                   { props.DataCarrito.inventario.length > 0 ?
                   <>
                    <DataTable
                    title   = {"Inventario"}
                    columns = {constant.columns.inventario}
                    data    = {props.DataCarrito.inventario}
                  />                  
                  <hr/>
                  </>
                   : null}
                    { props.DataCarrito.fregaderos.length > 0 ?
                   <>
                    <DataTable
                    title   = {"Fregaderos"}
                    columns = {constant.columns.fregaderos}
                    data    = {props.DataCarrito.fregaderos}
                  />                  
                  <hr/>
                  </>
                   : null}
                    { props.DataCarrito.suplementos.length > 0 ?
                   <>
                    <DataTable
                    title   = {"Suplementos"}
                    columns = {constant.columns.suplementos}
                    data    = {props.DataCarrito.suplementos}
                  />                  
                  <hr/>
                  </>
                   : null}
                   
                  </Card.Body>
                </Card>
              </Col>
            </Row>
          </Container>
        </div>
      </div>
    </div>
    
  );
}

export default SelectProduct;
