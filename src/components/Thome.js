import React,{ useState} from "react";
import Data from "../Data";
import BootstrapSwitchButton from 'bootstrap-switch-button-react';
import axios from "axios";
import Dropdown from 'react-bootstrap/Dropdown';

const apiUrl = "http://localhost:8080/api/tasks/start";
const apiUrl1 = "http://localhost:8080/api/tasks/stop";


const Thome = ({email, handleLogout}) => {
  const [language,setLanguage] = useState({});
  const [start, setStart] = useState(false);
  
  function startPipeline(task) {
    console.log("clicked: Start");
    setStart(!start)
    return axios.post(apiUrl, task);
  }
  function stopPipeline(task) {
    console.log("clicked: Stop");
    setStart(!start)
    return axios.post(apiUrl1, task);
  }
  // console.log(language);
  return (
      <>
    <section className="hero">
      <nav>
      {language.isMarathi ? (
        <h2>स्वागत {email?(email):("")}</h2>
      ):(
        <h2>Welcome {email?(email):("")}</h2>
        )}
      {start ? (
            <>
              <button onClick={()=>stopPipeline({text: "Stop the pipeline"})}>
                <span>Stop</span>
              </button>
            </>
          ) : (
            <>
              <button onClick={()=>startPipeline({text: "Run the pipeline"})}>
                <span>Start</span>
              </button>
            </>
          )}
          <Dropdown >
        {language.isMarathi?
        (<Dropdown.Toggle variant="secondary" >
          मराठी
        </Dropdown.Toggle>):(<Dropdown.Toggle variant="secondary" >
          English
        </Dropdown.Toggle>) }
        <Dropdown.Menu>
          <Dropdown.Item href="#" onClick={(checked: boolean) => {
                setLanguage({})
            }} >
            English
          </Dropdown.Item>
          <Dropdown.Item href="#" onClick={(checked: boolean) => {
                setLanguage({ isMarathi: checked })
            }} >
            मराठी
          </Dropdown.Item>
          
        </Dropdown.Menu>
      </Dropdown>
        {/* <BootstrapSwitchButton
            width={100} height={40}
            checked={false}
            onlabel='Marathi'
            offlabel='English'
            onChange={(checked: boolean) => {
                setLanguage({ isMarathi: checked })
            }}
        /> */}
        
        {language.isMarathi ? (
        <button onClick={handleLogout}>लॉग आउट</button>
        ):(
        <button onClick={handleLogout}>Logout</button>
        )}
      </nav>
    </section>
    <Data language={language}/>
      </>
  );
};

export default Thome;
