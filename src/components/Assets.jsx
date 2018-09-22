import React from 'react';

const Assets = () => (
  <div class="section">
    <div class="container">
      <div class="title">Your stocks</div>
      <table class="table is-striped is-fullwidth">
        <thead>
          <th>Symbol</th>
          <th>Company Name</th>
          <th>Stocks</th>
          <th>Price</th>
          <th>Revenue</th>
          <th>Decision</th>
        </thead>
        <tbody>
          <tr>
            <td>AAPL</td>
            <td>Apple Inc.</td>
            <td>100</td>
            <td>281.88</td>
            <td>+0.9</td>
            <td>
              <div class="button is-success is-small">Sell</div>
            </td>
          </tr>
          <tr>
            <td>AAPL</td>
            <td>Apple Inc.</td>
            <td>100</td>
            <td>281.88</td>
            <td>+0.9</td>
            <td>
              <div class="button is-success is-small">Sell</div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
);

export default Assets;
