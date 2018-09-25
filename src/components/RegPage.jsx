import React from 'react';
import { Link } from 'react-router-dom';

class RegPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      regName: '',
      regPass: '',
      userExists: false,
      regDone: false
    };
  }
  changeText = e => {
    const regName = e.target.value;
    let userExists = false;
    if (!!regName) {
      userExists = this.props.validCheck(regName);
    }
    this.setState({
      regName,
      userExists
    });
  };
  changePass = e => {
    const regPass = e.target.value;
    this.setState({
      regPass
    });
  };
  register = () => {
    console.log('1');
    if (this.props.validCheck(this.state.regName)) {
      console.log('3');
      this.setState({
        userExists: true
      });
      return;
    }
    console.log('2');
    this.props.regUser({
      name: this.state.regName,
      pass: this.state.regPass
    });
  };
  closeNotification = () => {
    const userExists = false;
    this.setState({
      userExists
    });
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
                      value={this.state.regName}
                      onChange={this.changeText}
                      type="text"
                      class="input"
                    />
                  </div>
                </div>
                <div>
                  <div class="field form-item">
                    <label class="label">Password:</label>
                    <input
                      value={this.state.regPass}
                      onChange={this.changePass}
                      type="password"
                      class="input"
                    />
                  </div>
                </div>
                <div class="field form-item">
                  <div
                    class="button is-success is-fullwidth"
                    onClick={this.register}
                    disabled={
                      this.state.userExists ||
                      (this.state.regName === '' || this.state.regPass === '')
                    }>
                    Register
                  </div>
                </div>
              </div>
            </div>
          </div>
          {this.state.userExists && (
            <div className="notification is-danger has-text-centered">
              <button className="delete" onClick={this.closeNotification} />
              <span className="is-size-4">User already exists</span>
            </div>
          )}
        </div>
        <Link to={`${process.env.PUBLIC_URL}/`}>
          <button className="modal-close" />
        </Link>
      </div>
    );
  }
}

export default RegPage;
