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

var routes = [
  
  {
    collapse: true,
    path: "/seccion",
    name: "Sección",
    state: "openComponents",
    icon: "nc-icon nc-app",
    views: [
        {
            path: "/encimeras",
            layout: "/admin",
            name: "Encimeras"
        },
        {
            path: "/inventario",
            layout: "/admin",
            name: "Inventario"
        },
        {
            path: "/fregaderos",
            layout: "/admin",
            name: "Fregaderos"
        },
        {
            path: "/suplementos",
            layout: "/admin",
            name: "Suplementos"
        },
        {
            path: "/mipedido",
            layout: "/admin",
            name: "Mi pedido",
        },
     
    ],
  },
];
export default routes;
