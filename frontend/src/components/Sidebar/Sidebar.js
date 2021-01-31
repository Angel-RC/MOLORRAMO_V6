import React from "react";
import { Link, useLocation } from "react-router-dom";
import PropTypes from "prop-types";
import image from "assets/img/full-screen-image-4.jpg";
// react-bootstrap components
import {
  Badge,
  Button,
  ButtonGroup,
  Card,
  Collapse,
  Form,
  InputGroup,
  Navbar,
  Nav,
  Pagination,
  Container,
  Row,
  Col,
} from "react-bootstrap";

function Sidebar({ page, routes, content }) {

  const background = "black"
  // to check for active links and opened collapses
  let location = useLocation();
  // this is for the user collapse
  const [userCollapseState, setUserCollapseState] = React.useState(false);
  // this is for the rest of the collapses
  const [state, setState] = React.useState({});
  React.useEffect(() => {
    setState(getCollapseStates(routes));
  }, []);
  // this creates the intial state of this component based on the collapse routes
  // that it gets through routes prop
  const getCollapseStates = (routes) => {
    let initialState = {};
    routes.map((prop, key) => {
      if (prop.collapse) {
        initialState = {
          [prop.state]: getCollapseInitialState(prop.views),
          ...getCollapseStates(prop.views),
          ...initialState,
        };
      }
      return null;
    });
    return initialState;
  };
  // this verifies if any of the collapses should be default opened on a rerender of this component
  // for example, on the refresh of the page,
  // while on the src/views/forms/RegularForms.jsx - route /admin/regular-forms
  const getCollapseInitialState = (routes) => {
    for (let i = 0; i < routes.length; i++) {
      if (routes[i].collapse && getCollapseInitialState(routes[i].views)) {
        return true;
      } else if (location.pathname ===routes[i].path) {
        return true;
      }
    }
    return false;
  };
  // this function creates the links and collapses that appear in the sidebar (left menu)
  const createLinks = (routes) => {
    return routes.map((prop, key) => {
      if (prop.redirect) {
        return null;
      }
      if (prop.collapse) {
        var st = {};
        st[prop["state"]] = !state[prop.state];
        return (
          <Nav.Item
            className={getCollapseInitialState(prop.views) ? "active" : ""}
            as="li"
            key={key}
          >
            <Nav.Link
              className={state[prop.state] ? "collapsed" : ""}
              data-toggle="collapse"
              onClick={(e) => {
                e.preventDefault();
                setState({ ...state, ...st });
              }}
              aria-expanded={state[prop.state]}
            >
              <i className={prop.icon}></i>
              <p>
                {prop.name} <b className="caret"></b>
              </p>
            </Nav.Link>
            <Collapse in={state[prop.state]}>
              <div>
                <Nav as="ul">{createLinks(prop.views)}</Nav>
                
              </div>
            </Collapse>
            

          </Nav.Item>
          
        );
      }
      return (
        <Nav.Item
          className={activeRoute(prop.path)}
          key={key}
          as="li"
        >
          <Nav.Link to={prop.path} as={Link}>
            {prop.icon ? (
              <>
                <i className={prop.icon} />
                <p>{prop.name}</p>
              </>
            ) : (
              <>
                <span className="sidebar-mini">{prop.mini}</span>
                <span className="sidebar-normal">{prop.name}</span>
              </>
            )}
          </Nav.Link>
        </Nav.Item>
      );
    });
  };
  // verifies if routeName is the one active (in browser input)
  const activeRoute = (routeName) => {
    return location.pathname === routeName ? "active" : "";
  };
  return (
    <>
      <div className="sidebar" data-color={background} data-image={image}>
        <div className="sidebar-wrapper">
          <div className="logo">
            <a className="simple-text logo-mini" >
            </a>
            <a className="simple-text logo-normal">
              {page.toUpperCase()}
            </a>
          </div>

          <Nav as="ul">{createLinks(routes)}</Nav>
          
         {content}
       
        </div>
        <div
          className="sidebar-background"
          style={{
            backgroundImage: "url('" + image + "')",
          }}
        ></div>
      </div>
    </>
  );
}


export default Sidebar;
