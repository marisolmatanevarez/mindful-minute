import { Store } from 'react-notifications-component';
import 'react-notifications-component/dist/theme.css';
import Input from './Input';

function Signup() {
    function confirmation() {
        Store.addNotification({
            title: "Thank You!",
            message: "You have successfully signed up for Mindful Moments!",
            type: "success",
            insert: "top",
            container: "center",
            animationIn: ["animate__animated", "animate__fadeIn"],
            animationOut: ["animate__animated", "animate__fadeOut"],
            dismiss: {
                duration: 5000,
                onScreen: true,
                pauseOnHover: true
            }
        });
    }

    return (
        <div className = "chat">
            <h1 color="black" align="center">Sign Up</h1>
            <Input />
            <div className = "actions">
                <br />
                <button className="btn" align="left" onClick={confirmation}>Submit</button>
                <br />
            </div>
        </div>
    );
}

export default Signup;