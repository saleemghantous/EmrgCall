import React, { useState, useEffect } from "react";
import { Container } from "react-bootstrap";
import { useNavigate } from 'react-router-dom';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { Form, Row, Col, Button } from 'react-bootstrap';
import axios from "axios";
import { useSelector, useDispatch } from 'react-redux'
import { notify } from './../Notification/Notification';
import { setUserProp } from "../redux_slice/UserSlice";

const HomeComp = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const ConfigSlice = useSelector((state) => state.config)
    const dispatch = useDispatch()

    const handleLogin = async () => {
        if (username === "" || password === "") {
            notify("error", "יש למלא את כל השדות")
        }
        else {
            await axios.post(`${ConfigSlice.baseUrl}/api/login`, { username: username, password: password }, {
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*', // Add this if needed for CORS
                    // Add any other required headers here
                },
            })
                .then(res => {
                    if (res.data.loginStatus) {
                        console.log(res.data)
                        dispatch(setUserProp({ prop: "username", value: username }))
                        dispatch(setUserProp({ prop: "password", value: password }))
                        dispatch(setUserProp({ prop: "admin", value: res.data.admin }))
                        dispatch(setUserProp({ prop: "loginStatus", value: res.data.loginStatus }))
                        navigate('/users')
                    }
                    else {
                        notify("error", "שם המשתמש או הסיסמה לא נכונים")
                    }
                }
                )
        }
    }

    

    return (
        <Container style={{ maxWidth: "500px" }}>
            <div className="mb-3 text-center" style={{ marginTop: "100px" }}>
                <Form>
                    <Row className="mb-3">
                        <Col>
                            <Form.Label htmlFor="username" className="float-end">
                                <b> שם משתמש</b>
                            </Form.Label>
                            <Form.Control
                                type="text"
                                id="username"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                        </Col>
                    </Row>
                    <Row className="mb-3">
                        <Col>
                            <Form.Label htmlFor="password" className="float-end">
                                <b> סיסמה</b>
                            </Form.Label>
                            <Form.Control
                                type="password"
                                id="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </Col>
                    </Row>
                    <Row className="justify-content-center mx-1 mt-5">
                        <Button onClick={handleLogin} variant="primary">כניסה</Button>
                    </Row>
                </Form>
            </div>


        
        </Container>
    );
}

export default HomeComp;
