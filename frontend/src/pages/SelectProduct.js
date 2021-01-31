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



function SelectProduct(props) {

  // Data
  const [DataInicial, setDataInicial] = useState([])
  const [DataMostrar, setDataMostrar] = useState([])

  const [Options, setOptions] = useState({
    material : [], 
    color : [], 
    medida : [],
    acabado : [],
    grosor : [], 
    concepto: []
  })
  const [Metros, setMetros] = useState({
    lineales : 0, 
    cuadrados : 0, 
    frente : 0
  });
  const [Filtros, setFiltros] = useState({
    material : [], 
    color : [], 
    medida : [],
    acabado : [],
    grosor : [], 
    concepto: [],
    cantidad : []
  });
  
  
  console.log(props.DataCarrito)
  useEffect(() => {
    API.CreateDataInicial(props.page, Metros, setDataInicial, setOptions)

    setFiltros({
      material : [], 
      color : [], 
      medida : [],
      acabado : [],
      grosor : [], 
      concepto: [],
      cantidad : []
    });

  }, [props.page]) 

  
  useEffect(() => {
    API.CreateDataInicial(props.page, Metros, setDataInicial, setOptions)

  
    
  }, [Metros]) 

  useEffect(() => {
    if (DataInicial.length > 0){
      API.filterData(props.page, DataInicial, Filtros, setDataMostrar, Options, setOptions)
    }

  }, [DataInicial, Filtros]) 


  return (
    
    <div className="wrapper">

      <Sidebar
        page       = {props.page}
        routes     = {SidebarRoutes}
        content    = {<SidebarProductForm 
                        page           = {props.page}
                        Filtros        = {Filtros}
                        setFiltros     = {setFiltros}
                        Options        = {Options}
                        DataMostrar    = {DataMostrar}
                        DataCarrito    = {props.DataCarrito}
                        SetDataCarrito = {props.SetDataCarrito}/>
                      }
      />
      <div className="main-panel">
         
        <AdminNavbar />
         
        <div className="content">
          
          <Container fluid>
            <Row>
              <Col md="12">
                <Card>
                  <Card.Body>
                  { "encimeras" === props.page ? <FormMetros setMetros = {setMetros} Metros = {Metros}/>: null}
                    <DataTable
                      columns = {constant.columns.[props.page]}
                      data    = {DataMostrar}
                      pagination = {true}
                      fixedHeader = {true}
                      progressPending = {DataInicial.length === 0}
                    />
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
