import React, { } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import NavBarComp from "./components/NavBarComp/NavBarComp";
import 'bootstrap/dist/css/bootstrap.min.css';
// import AboutComp from "./components/AboutComp/AboutComp";
import HomeComp from "./components/HomeComp/HomeComp";
import Users from "./components/Users/Users";
import AlertComp from "./components/Alert/AlertComp";
import "./App.css"

function App() {

  return (
    <div className="App">
      <BrowserRouter basename="">
        <NavBarComp />
        <Routes>
          <Route exact path="/" element={<HomeComp />} />
          <Route exact path="/users" element={<Users />} />
          <Route exact path="/alert" element={<AlertComp />} />
          <Route path="/*" element={<HomeComp />} />

        </Routes>
      </BrowserRouter>

    </div>
  );
}

export default App;



