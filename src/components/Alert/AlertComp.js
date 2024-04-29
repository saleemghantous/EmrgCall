import React, { Fragment, useState, useEffect } from 'react'
import Form from 'react-bootstrap/Form';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import { useSelector, useDispatch } from 'react-redux'
import { notify } from '../Notification/Notification'
import axios from 'axios'

const AlertComp = () => {

  const [alertTarget, setAlertTarget] = useState("")
  const [alertType, setAlertType] = useState("")
  const ConfigSlice = useSelector((state) => state.config)


  useEffect(() => {
    setAlertType("")
  }, [alertTarget])


  const sendAlert = async () => {
    await axios.post(`${ConfigSlice.baseUrl}/api/send_alert`, { "alertTarget": alertTarget, "alertType": alertType })
      .then(res => {
        console.log(res.data)
        notify(res.data.result, res.data.comment)
        if (res.data.result == "success") {
        }
      })
  }

  return (
    <div>
      <br />
      <br />
      <Container>
        <Form.Label> <b>אנא בחר קהל היעד</b></Form.Label>
        <Form.Select aria-label="Default select example" onChange={(e) => (setAlertTarget(e.target.value))}>
          {alertTarget ? null : <option selected value="" disabled>אנא בחר סוג קריאה</option>}
          <option value="limited">קריאת בעלי תפקידים - צוות מצומצם</option>
          <option value="extended">קריאת בעלי תפקידים - צוות מורחב</option>
          {
            // <option value="staff">קריאת סגל</option>
          }
        </Form.Select>

        {
          alertTarget === "limited" || alertTarget === "extended" ? (
            <Fragment>
              <Form.Label className='mt-4'> <b>אנא בחר סוג קריאה</b></Form.Label>
              <br />
              <Button variant={alertType === "exercise" ? "primary" : "secondary"} value={"exercise"} onClick={(e) => setAlertType(e.target.value)}>תרגיל</Button>{' '}
              {
                // <Button variant={alertType === "raise" ? "primary" : "secondary"} value={"raise"} onClick={(e) => setAlertType(e.target.value)}>העלאת כוננות</Button>{' '}
              }
              <Button variant={alertType === "real" ? "primary" : "secondary"} value={"real"} onClick={(e) => setAlertType(e.target.value)}>אירוע אמת</Button>{' '}
            </Fragment>
          ) : null
        }

        {
          alertTarget === "staff" ? (
            <Fragment>
              <Form.Label className='mt-4'> <b>אנא בחר סוג קריאה</b></Form.Label>
              <br />
              <Button variant={alertType === "exercise" ? "primary" : "secondary"} value={"exercise"} onClick={(e) => setAlertType(e.target.value)}>תרגיל</Button>{' '}
              <Button variant={alertType === "real" ? "primary" : "secondary"} value={"real"} onClick={(e) => setAlertType(e.target.value)}>אירוע אמת</Button>{' '}
            </Fragment>
          ) : null
        }

        {
          alertTarget !== "" && alertType !== "" ? (
            <Fragment>
              <br />
              <br />
              <br />
              <Button variant="success" onClick={(e) => sendAlert()}>שגר קריאה</Button>
            </Fragment>
          ) : null
        }

      </Container>


    </div>
  )
}

export default AlertComp
