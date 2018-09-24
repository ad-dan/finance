import React from 'react';

const Assets = ({ user }) => {
  if (!user.portfolio.length) {
    return (
      <div className="section">
        <div className="container">
          <div className="title">
            You don't have any stocks. Head over to search to buy some
          </div>
        </div>
      </div>
    );
  }
  const data = user.portfolio.map(stock => {
    const change = 0.001 * Math.floor(Math.random() * 100);
    const isBull = Math.random() >= 0.5;
    const net = isBull
      ? stock.value + stock.value * change
      : stock.value - stock.value * change;
    return (
      <tr>
        <td>{stock.sym}</td>
        <td>{stock.name}</td>
        <td>{stock.amount}</td>
        <td className={isBull ? 'has-text-success' : 'has-text-danger'}>{`${
          isBull ? '+' : '-'
        }${change}%`}</td>
        <td className={isBull ? 'has-text-success' : 'has-text-danger'}>
          {net}
        </td>
        <td>
          <div
            className={`button is-small ${
              isBull ? 'is-success' : 'is-danger'
            }`}>
            Sell
          </div>
        </td>
      </tr>
    );
  });
  return (
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
          <tbody>{data}</tbody>
        </table>
      </div>
    </div>
  );
};

export default Assets;
