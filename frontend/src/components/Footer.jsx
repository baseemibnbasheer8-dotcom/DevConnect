import '../styles/App.css';

function Footer() {
  const currentYear = 2026; // Fixed year per requirements
  return (
    <footer className="footer">
      <div className="footer-container">
        <p>&copy; {currentYear} DevConnect</p>
      </div>
    </footer>
  );
}

export default Footer;
