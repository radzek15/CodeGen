import React from "react";
import NavBar from "../components/NavBar/NavBar";
import Footer from "../components/Footer/Footer";

export default function HomePage() {
  return (
    <div style={{display: "flex", flexDirection: "column", minHeight: "100vh"}}>
      <NavBar />
      <div style={{flex: "1"}}>
        <h1
          className={"fw-bold text-center mt-3 text-primary"}
          style={{ fontFamily: "'Dancing Script', cursive", fontSize: "5rem" }}
        >
          CodeGen
        </h1>
      </div>
      <Footer style={{flexShrink: "0"}} />
    </div>
  );
}
