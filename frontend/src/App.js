import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import BadWordsPage from "./components/BadWordsPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/badwords" element={<BadWordsPage />} />
      </Routes>
    </Router>
  );
}

export default App;