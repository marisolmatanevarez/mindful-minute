function Input() {
    return (
        <div>
            <p>
                Fill out the information below to sign up for MindfulMinute!
            </p>
            <label>
                Name:  
                <input type="text" name="name" />
            </label>
            <br />
            <br />
            <label>
                Phone Number: 
                <input type="text" name="number" />
            </label>
        </div>
    ); 
}

export default Input;