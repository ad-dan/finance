import React from 'react';
import { Link } from 'react-router-dom';

const Modal = () => (
  <div class="modal is-active">
    <div class="modal-background" />
    <div class="modal-content">
      <div class="log box">
        <div class="columns">
          <div class="column is-10 is-offset-1">
            <div>
              <div class="field form-item">
                <label for="" class="label">
                  Username:
                </label>
                <input type="text" class="input" />
              </div>
            </div>
            <div>
              <div class="field form-item">
                <label for="" class="label">
                  Password:
                </label>
                <input type="password" class="input" />
              </div>
            </div>
            <div class="field form-item">
              <div class="button is-success is-fullwidth">Login</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Link to="/">
      <button className="modal-close" />
    </Link>
  </div>
);

export default Modal;
