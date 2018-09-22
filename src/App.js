import React, { Component } from 'react';
import './App.css';
import {BrowserRouter as Router, Link, Route}from 'react-router-dom';
import Box from './Box';
import Cat from './Cat';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
        <div>
          Click the links below!
        </div>
        <div>
          <div>
            <Link to="/test">
              Test link
            </Link>
          </div>
          <div>
            <Link to="/kek">
              Lol
            </Link>
          </div>
        </div>
        <div>
          <Route path="/test" component={Box} />
          <Route path="/kek" component={Cat}/>
        </div>
        </div>
        
      </Router>
    );
  }
}

export default App;
