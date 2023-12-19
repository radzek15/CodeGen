import React, { useState } from "react";
import './NavBar.css';
import {MDBNavbar, MDBContainer, MDBNavbarToggler, MDBIcon, MDBCollapse, MDBNavbarNav, MDBNavbarItem, MDBNavbarLink} from 'mdb-react-ui-kit';

const NavBar = () => {
		const [showNavCentred, setShowNavCentred] = useState(false);
		return (
			<MDBNavbar expand='lg' className={ 'navbar navbar-expand-md navbar-light bg-light p-4' }>
				<MDBContainer fluid>
					<MDBNavbarToggler type='button' data-target='#navbarNav' aria-controls='navbarCenteredExample' aria-expanded='false' aria-label='Toggle navigation' onClick={() => setShowNavCentred(!showNavCentred)}>
						<MDBIcon icon='bars' fas />
					</MDBNavbarToggler>
					<MDBCollapse navbar show={showNavCentred} center id={ 'navbarNav' }>
						<MDBNavbarNav fullWidth={ false } className={ 'navbar-nav nav-fill w-100' }>
							<MDBNavbarItem>
								<MDBNavbarLink active aria-current='page' href='/' className={ 'nav-link text-success' }>Home Page</MDBNavbarLink>
							</MDBNavbarItem>
							<MDBNavbarItem>
								<MDBNavbarLink active aria-current='page' href='/nginx' className={ 'nav-link text-success' }>Nginx Generator</MDBNavbarLink>
							</MDBNavbarItem>
							<MDBNavbarItem>
								<MDBNavbarLink active aria-current='page' href='/docker' className={ 'nav-link text-success' }>Docker Generator</MDBNavbarLink>
							</MDBNavbarItem>
						</MDBNavbarNav>
					</MDBCollapse>
				</MDBContainer>
			</MDBNavbar>
		);
}

export default NavBar
