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
            path: "/pedidos",
            layout: "/admin",
            name: "Mis Pedidos"
        },
        {
            path: "/grupo",
            layout: "/admin",
            name: "Mi grupo"
        },
        {
            path: "/pvp",
            layout: "/admin",
            name: "Mi PVP"
        }
     
    ],
  },
];
export default routes;
