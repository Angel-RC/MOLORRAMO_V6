import React, {useState} from "react";
import { useForm } from "react-hook-form";

// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Form,
  Navbar,
  Nav,
  Container,
  Col,
} from "react-bootstrap";

function LoginPage() {

  const { register, handleSubmit } = useForm();

  const onSubmit = (data) => console.log(data);

  



  const [User, setUser] = React.useState();
  const [cardClasses, setCardClasses] = React.useState("card-hidden");
  React.useEffect(() => {
    setTimeout(function () {
      setCardClasses("");
    }, 1000);
  });
  return (
    <>



  
  

      <div

      
        className="full-page section-image"
        data-color="black"
        data-image={require("assets/img/full-screen-image-2.jpg").default}
      >
        <div className="content d-flex align-items-center p-0">
          <Container>
            <Col className="mx-auto" lg="4" md="8">
              <Form action="" className="form" method="">
                <Card className={"card-login " + cardClasses}>
                  <Card.Header>
                    <h3 className="header text-center">Acceder</h3>
                  </Card.Header>
                  <Card.Body>
                  

                  <form onSubmit={handleSubmit(onSubmit)}>
    

    <input name="firstName" ref={register} placeholder="First name" />

    <input name="lastName" ref={register} placeholder="Last name" />

    <select name="category" ref={register}>
      <option value="">Select...</option>
      <option value="A">Category A</option>
      <option value="B">Category B</option>
    </select>

    <input type="submit" />
  </form>
                  </Card.Body>
                  <Card.Footer className="ml-auto mr-auto">
                    <Button className="btn-wd" type="submit" variant="warning">
                      Login
                    </Button>
                  </Card.Footer>
                </Card>
              </Form>
            </Col>
          </Container>
        </div>
        <div
          className="full-page-background"
          style={{
            backgroundImage:
              "url(" +
              require("assets/img/full-screen-image-2.jpg").default +
              ")",
          }}
        ></div>
      </div>
    </>
  );
}

export default LoginPage;
