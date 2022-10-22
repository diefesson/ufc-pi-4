import React, { useState } from "react";
import AboutUs from "./pages/AboutUs";
import Classifier from "./pages/Classifier";

function App() {
  const [linkHomePage, setLinkHomePage] = useState(true);
  return (
    <div className="App">
      {linkHomePage ? <Classifier onClick={setLinkHomePage} /> : <AboutUs />}{" "}
    </div>
  );
}

export default App;
