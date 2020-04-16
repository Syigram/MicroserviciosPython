import axios from 'axios';
import React from 'react';
import Input from './Input'
import Button from 'react-bootstrap/Button';

import { API_BASE_URL, REGISTER_URL, QUERY_START } from '../config/config.js'

const emptyFormValues = {
    name: '',
    email: '',
    region: '',
};

class Form extends React.Component {
    constructor() {
        super();
        this.state =  Object.assign({}, emptyFormValues, {});
      }
    
    
    emptyState = () => {
        this.setState(
            Object.assign({}, emptyFormValues, {})
        );
    }

    handleChange = (event) => {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit = (event) => {
        event.preventDefault();
        let params = new URLSearchParams();
        params.append('name', this.state.name);
        params.append('email', this.state.email);
        params.append('region', this.state.region);
        let requestUrl = API_BASE_URL + REGISTER_URL + QUERY_START + params;
        console.log(requestUrl);
        axios.get(requestUrl).then(response => console.log(response));
        this.emptyState();
    }
    
    render() {
        return (
            <form>
                <Input 
                    placeholder="Ingrese su nombre"
                    name="name"
                    label="Nombre" 
                    value={this.state.name}
                    onChange={this.handleChange}
                    />
                <Input 
                    placeholder="Ingrese su correo electrónico" 
                    name="email" 
                    label="Correo electrónico"
                    value={this.state.email}
                    // onChange={this.handleChange}
                    onChange={(e) => this.handleChange(e)}
                    />
                <Input 
                    placeholder="Región" 
                    name="region" 
                    label="Ingrese su región" 
                    value={this.state.region}
                    onChange={this.handleChange}
                    />
                <Button 
                    variant="outline-primary" 
                    onClick={(e) => this.handleSubmit(e)} 
                    type="submit">Submit</Button>
            </form>
        )
    }
}


export default Form;
