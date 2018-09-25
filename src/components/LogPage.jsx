import React from 'react';
import { Link } from 'react-router-dom';

class LogPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      logName: '',
      logPass: ''
    };
  }
  changeName = e => {
    this.setState({
      logName: e.target.value
    });
  };
  changePass = e => {
    this.setState({
      logPass: e.target.value
    });
  };
  regUser = () => {
    const name = this.state.logName;
    const pass = this.state.logPass;

    const userExists = this.props.validCheck({ name, pass });

    if (userExists) this.props.register({ name, pass });
  };
  render() {
    return (
      <div class="modal is-active">
        <div class="modal-background" />
        <div class="modal-content">
          <div class="log box">
            <div class="columns">
              <div class="column is-10 is-offset-1">
                <div>
                  <div class="field form-item">
                    <label class="label">Username:</label>
                    <input
                      type="text"
                      class="input"
                      value={this.state.logName}
                      onChange={this.changeName}
                    />
                  </div>
                </div>
                <div>
                  <div class="field form-item">
                    <label class="label">Password:</label>
                    <input
                      type="password"
                      class="input"
                      value={this.state.logPass}
                      onChange={this.changePass}
                    />
                  </div>
                </div>
                <div class="field form-item">
                  <div
                    class="button is-success is-fullwidth"
                    onClick={this.regUser}
                    disabled={
                      !this.state.logName.length || !this.state.logPass.length
                    }>
                    Login
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <Link to={`${process.env.PUBLIC_URL}/`}>
          <button className="modal-close" />
        </Link>
      </div>
    );
  }
}

export default LogPage;
