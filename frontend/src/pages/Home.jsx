import { Link } from 'react-router-dom';
import '../styles/App.css';

function Home() {
  return (
    <div className="home-container">
      <div className="hero-section">
        <h1 className="hero-title">DevConnect</h1>
        <p className="hero-subtitle">
          Building seamless connections for modern developers. A clean, modern, and production-ready platform.
        </p>
        <Link to="/contact" className="btn-primary">
          Contact Us
        </Link>
      </div>
    </div>
  );
}

export default Home;
