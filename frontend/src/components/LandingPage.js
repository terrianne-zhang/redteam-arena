import React from "react";
import { Link } from "react-router-dom";

const LandingPage = () => (
  <div>
    <h1>Welcome to RedTeam Arenas</h1>
    <button><Link to="/badwords">Badwords</Link></button>
    <button><Link to="/norefund">NoRefund</Link></button>
  </div>
);

export default LandingPage;