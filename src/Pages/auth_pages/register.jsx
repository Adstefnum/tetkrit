import React from "react";
import logo from './logo.svg';
//get your own logo

export class Register extends React.Component {

    // eslint-disable-next-line no-useless-constructor
    constructor(props){
        super(props);
    }

    render() {
        return <div className = "container">
            <div className = "header">Login</div>
            <div className = "content">
                <div className = "image">
                    <img src ={logo} alt="logo" />
                </div>
                <div className="form">
                    <div className = "form-group">
                        <label htmlFor="username">Username</label>
                        <input type="text" name="username" placeholder = "username"/>
                    </div>
                    <div className = "form-group">
                    <label htmlFor="email">Email</label>
                        <input type="email" name="email" placeholder = "email"/>
                    </div>
                    <div className = "form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" placeholder = "password"/>
                    </div>
                    <div className = "footer">
                        <button type = "button" className = "btn">Register</button>
                    </div>
                </div>
            </div>
        </div>
    }
}