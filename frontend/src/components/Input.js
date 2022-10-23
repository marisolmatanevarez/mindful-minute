function Input() {
    return (
        <div align="center">
            <p align="center">
                Fill out the information below to sign up for Mindful Moments!
            </p>
            <label align="center">
                Name:  
                <input type="text" name="name" />
            </label>
            <br />
            <br />
            <label align="center">
                Phone Number: 
                <input type="text" name="number" />
            </label>
        </div>
    ); 
}

export default Input;