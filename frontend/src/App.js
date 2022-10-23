import './App.css';
import Signup from './components/Signup';

function App() {
  return (
      <div className="backdrop" style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: '100vh'
      }}>
        <Signup />
      </div>
  );
}

export default App;
