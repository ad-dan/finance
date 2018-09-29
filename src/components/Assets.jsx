import React from 'react';

class Assets extends React.Component {
  constructor(props) {
    super(props);
  }
  componentDidUpdate() {}
  render() {
    const { user, sell } = this.props;

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
    setTimeout(() => {
      const { Chartist } = window;
      new Chartist.Pie('.ct-chart-pie', {
        labels: user.portfolio.map(stock => stock.sym),
        series: user.portfolio.map(stock => stock.value.toFixed(0))
      });
    }, 0);
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
          }${change.toFixed(3)}%`}</td>
          <td className={isBull ? 'has-text-success' : 'has-text-danger'}>
            {net.toFixed(2)}
          </td>
          <td>
            <div
              className={`button is-small ${
                isBull ? 'is-success' : 'is-danger'
              }`}
              onClick={() =>
                sell({
                  price: net,
                  sym: stock.sym
                })
              }>
              Sell
            </div>
          </td>
        </tr>
      );
    });
    return (
      <div class="section has-background-white">
        <div class="container">
          <div className="columns">
            <div className="column is-three-quarters-desktop">
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
            <div className="column">
              <div className="ct-chart-pie" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Assets;
