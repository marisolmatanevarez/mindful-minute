import './App.css';
import Signup from './components/Signup';
import Description from './components/Description';
import Image from './components/Image';

function App() {
  return (
      <div>
        <div class="chat">
          <div class="yours messages">
            <div class="message">
              Are you signed up for Mindful Moments?
            </div>
            <div class="message last">
              <Description />
            </div>
          </div>
          <div class="mine messages">
            <div class="message last">
              How do I sign up?
            </div> 
          </div>
          <div class="yours messages">
            <div class="message last">
              See below!
            </div>
          </div>
      </div>
      <Signup />
      <Image />
    </div>
  );
}

export default App;
