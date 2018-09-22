import React from 'react';

const SearchPage = () => (
  <div>
    <div class="section">
      <div class="level">
        <div class="level-item">
          <span class="is-size-1 has-text-weight-light">Mr.Broker</span>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="level">
        <div class="level-item">
          <div class="field">
            <div class="control has-icons-right">
              <input
                type="text"
                class="input is-primary is-medium is-rounded"
              />
              <span class="icon is-medium is-right">🔍</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="level">
        <div class="level-item has-text-centered">
          <div>
            <p class="heading">Name</p>
            <p class="title">AAPL</p>
          </div>
        </div>
        <div class="level-item has-text-centered">
          <div>
            <p class="heading">Company</p>
            <p class="title">Apple Inc.</p>
          </div>
        </div>
        <div class="level-item has-text-centered">
          <div>
            <p class="heading">Price</p>
            <p class="title">218.24</p>
          </div>
        </div>
        <div class="level-item has-text-centered">
          <div>
            <p class="heading">Status</p>
            <p class="title">+0.83%</p>
          </div>
        </div>
      </div>
    </div>
  </div>
);

export default SearchPage;
