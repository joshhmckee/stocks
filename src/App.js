import axios, { Axios } from "axios";
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Home from "./components/home";


function App() {

  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/test" element={<h1>HELLO!!!</h1>} />
        </Routes>
      </div>
    </Router>
  );

  // const [profileData, setProfileData] = useState(null)

  // async function getData() {
  //   // Get data from the flask backend
  //   try {
  //     const res = await axios.get('/profile');
  //     const data = res.data;
  //     console.log(data);
  //     setProfileData(({
  //       profile_name: data.name,
  //       about_me: data.about
  //     }));
  //   } catch (e) {
  //     console.log(e);
  //   }
  // }

  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>

  //       {/* new line start*/}
  //       <p>To get your profile details: </p><button onClick={getData}>Click me</button>
  //       {profileData && <div>
  //             <p>Profile name: {profileData.profile_name}</p>
  //             <p>About me: {profileData.about_me}</p>
  //           </div>
  //       }
  //        {/* end of new line */}
  //     </header>
  //   </div>
  // );

  // return (
  //   <div style={{
  //     display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh',
  //     backgroundColor: '#D9AFD9', backgroundImage: 'linear-gradient(0deg, #D9AFD9 0%, #97D9E1 100%)'
  //   }}>
  //     <Form>
  //       <Form.Group className="mb-3">
  //         <Form.Control type="text" placeholder="enter ticker..." />
  //       </Form.Group>
  //     </Form>
  //   </div>
  // );
}

export default App;