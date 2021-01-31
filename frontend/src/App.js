/*!

=========================================================
* Light Bootstrap Dashboard PRO React - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-pro-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React, {useState} from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";

import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "assets/scss/light-bootstrap-dashboard-pro-react.scss?v=2.0.0";
import "assets/css/demo.css";
import PrivateRoute from './PrivateRoute';
import {AuthContext}  from "./context/Auth";
import AuthLayout from "layouts/Auth.js";
import AdminLayout from "layouts/Admin.js";
import SelectProduct from "pages/SelectProduct"
import MiPedido from "pages/MiPedido"
import LoginPage from "pages/LoginPage"


function App()  {


  const [Carrito, SetCarrito] = useState({
    encimeras  : [], 
    fregaderos : [], 
    inventario : [],
    suplementos: []
  })

  const [UserLogin, SetUserLogin] = useState(true)
  
console.log(Carrito)
  return (
    <div className = "App">
      <AuthContext.Provider value = {UserLogin}>
      <BrowserRouter>
        <Switch>
          <PrivateRoute path = "/encimeras"   component = {SelectProduct} page = "encimeras"   DataCarrito = {Carrito.encimeras}   SetDataCarrito = {(data) =>{SetCarrito({...Carrito, encimeras: data})}}/>
          <PrivateRoute path = "/inventario"  component = {SelectProduct} page = "inventario"  DataCarrito = {Carrito.inventario}  SetDataCarrito = {(data) =>{SetCarrito({...Carrito, inventario: data})}}/>
          <PrivateRoute path = "/fregaderos"  component = {SelectProduct} page = "fregaderos"  DataCarrito = {Carrito.fregaderos}  SetDataCarrito = {(data) =>{SetCarrito({...Carrito, fregaderos: data})}}/>
          <PrivateRoute path = "/suplementos" component = {SelectProduct} page = "suplementos" DataCarrito = {Carrito.suplementos} SetDataCarrito = {(data) =>{SetCarrito({...Carrito, suplementos: data})}}/>
          <PrivateRoute path = "/mipedido"    component = {MiPedido}      DataCarrito = {Carrito}/>
         
          <Route        path = '/signin'      component = {LoginPage}  UserLogin = {UserLogin} SetUserLogin = {SetUserLogin}/>
         <Redirect to="/encimeras" />
        </Switch>
      </BrowserRouter>
      </AuthContext.Provider>
  
    </div>
  );
}

export default App;
