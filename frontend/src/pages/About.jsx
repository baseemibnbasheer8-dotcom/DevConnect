import { useEffect, useState } from 'react';
import api from '../api/api';
import '../styles/App.css';

function About() {
  const [aboutInfo, setAboutInfo] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAbout = async () => {
      try {
        const response = await api.get('/about');
        setAboutInfo(response.data);
      } catch (err) {
        setError('Failed to load about information.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchAbout();
  }, []);

  return (
    <div className="page-container">
      <div className="card">
        <h2>About DevConnect</h2>
        
        {loading && <p>Loading information...</p>}
        {error && <p className="error-message">{error}</p>}
        
        {aboutInfo && (
          <div className="about-details">
            <p><strong>Application:</strong> {aboutInfo.application}</p>
            <p><strong>Version:</strong> {aboutInfo.version}</p>
            <p><strong>Frontend:</strong> {aboutInfo.frontend}</p>
            <p><strong>Backend:</strong> {aboutInfo.backend}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default About;
