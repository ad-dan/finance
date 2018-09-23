import React from 'react';
import { Link } from 'react-router-dom';

const UserNav = ({ out }) => (
  <div class="navbar navy">
    <div class="navbar-brand">
      <div class="level">
        <div class="level-item">
          <Link to="/">
            <div className="level">
              <div className="level-item">
                <svg
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 512 512">
                  <g />
                  <path
                    d="M409.241 34.038h-306.442c-37.98 0-68.741 30.771-68.741 68.721v306.462c0 37.959 30.761 68.741 68.741 68.741h306.442c37.929 0 68.7-30.781 68.7-68.741v-306.462c0-37.95-30.771-68.721-68.7-68.721zM270.101 370.903v38.676h-30.781v-36.423c-23.685-0.717-47.35-7.516-60.846-16.517l10.148-35.277c14.613 8.622 35.645 16.517 58.563 16.517 23.685 0 39.803-11.684 39.803-29.696 0-16.855-13.118-27.76-40.919-37.929-39.434-14.254-64.973-32.276-64.973-67.185 0-32.327 22.507-57.088 60.447-63.846v-36.834h30.812v34.939c23.654 0.758 39.824 6.4 51.845 12.391l-10.168 34.54c-9.022-4.117-25.529-12.718-51.077-12.718-26.245 0-35.666 13.486-35.666 26.245 0 15.381 13.517 24.034 45.476 36.803 42.046 15.79 60.815 36.055 60.815 69.468-0.010 31.928-22.19 60.078-63.478 66.846z"
                    fill="#ffffff"
                  />
                </svg>
                <span class="is-size-4 has-text-white">tocks</span>
              </div>
            </div>
          </Link>
        </div>
      </div>
    </div>
    <div class="navbar-menu ">
      <div class="navbar-end">
        <div class="navbar-item field is-grouped">
          <p class="control">
            <div class=" button is-primary is-inverted is-rounded">
              <Link to="search">Search </Link>
            </div>
          </p>
          <p class="control">
            <div class=" button is-success is-inverted is-rounded">
              <Link to="/dashboard">Dashboard</Link>
            </div>
          </p>
          <p class="control">
            <div
              onClick={out}
              class=" button is-primary is-inverted is-rounded">
              Register
            </div>
          </p>
        </div>
      </div>
    </div>
  </div>
);

export default UserNav;
