// import './App.css'
import React from 'react';
import { Form } from 'react-bootstrap';


function Input(props) {

    return (
        <Form.Group>
            <Form.Label>{props.label}</Form.Label>
            <Form.Control 
                type={props.type} 
                placeholder={props.placeholder} 
                value={props.value} 
                onChange={(e) => props.onChange(e)}
                name={props.name}  />
        </Form.Group>
    )
}

export default Input;
