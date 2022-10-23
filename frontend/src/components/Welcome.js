import { Store } from 'react-notifications-component';
import 'react-notifications-component/dist/theme.css';

function Welcome() {
    return(
        Store.addNotification({
            title: "New Message",
            message: "Are you signed up for Mindful Moments?",
            type: "default",
            insert: "top",
            container: "center",
            animationIn: ["animate__animated", "animate__fadeIn"],
            animationOut: ["animate__animated", "animate__fadeOut"],
            dismiss: {
                duration: 5000,
                onScreen: true,
                pauseOnHover: true
            }
        })
    )
}
export default Welcome;