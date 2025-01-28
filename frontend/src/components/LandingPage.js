import React from "react";
import { Link } from "react-router-dom";
import "./LandingPage.css"; // Link to a CSS file for styling

const LandingPage = () => (
  <div className="landing-container">
    <h1>RedTeam Arena</h1>
    <div className="button-container">
      <button><Link to="/badwords">Play Bad Words</Link></button>
      <button><Link to="/norefund">Play No Refund</Link></button>
    </div>
  </div>
);

export default LandingPage;