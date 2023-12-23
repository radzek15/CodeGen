import React from "react";
import {MDBFooter, MDBContainer, MDBRow, MDBCol, MDBIcon} from 'mdb-react-ui-kit';

const Footer = () => {
  return (
    <MDBFooter className="bg-light text-center">
      <section className='d-flex justify-content-center justify-content-lg-between p-4 border-bottom'>
        <div className='me-5 d-none d-lg-block'>
          <span>Skontaktuj sie z nami:</span>
        </div>
        <div>
          <a href='https://www.facebook.com/radomir.piatkowski/'
             className='me-4 text-reset'>
            <MDBIcon fab icon="facebook-f"/>
          </a>
          <a
            href="mailto:radzek15@gmail.com"
            className='me-4 text-reset'>
            <MDBIcon fab icon="google"/>
          </a>
          <a href='https://www.linkedin.com/in/radomir-pi%C4%85tkowski-9166a5241/' className='me-4 text-reset'>
            <MDBIcon fab icon="linkedin"/>
          </a>
          <a href='https://github.com/radzek15' className='me-4 text-reset'>
            <MDBIcon fab icon="github"/>
          </a>
        </div>
      </section>

      <section>
        <MDBContainer className='text-center text-md-start mt-5'>
          <MDBRow className={ 'mt-3' }>
            <MDBCol md="4" lg="4" xl="4" className='mx-auto mb-4'>
              <h6 className='text-uppercase fw-bold mb-4'>
                <MDBIcon fas icon="code" className="me-3"/>
                CodeGen
              </h6>
              <p>CodeGen will help you to automate creation of configuration and deployment files</p>
            </MDBCol>

            <MDBCol md="4" lg="3" xl="3" className='mx-auto mb-4'>
              <h6 className='text-uppercase fw-bold mb-4'>Useful links</h6>
              <p><a href='/pricing' className='text-reset'>Pricing</a></p>
            </MDBCol>

          </MDBRow>
        </MDBContainer>
      </section>

      <div className={ 'text-center p-3 bg-dark' }>
        <p className={ 'text-light mt-3' }>Copyright: &copy; 2023 radzek15. All rights reserved.</p>
      </div>
    </MDBFooter>
  );
}

export default Footer
