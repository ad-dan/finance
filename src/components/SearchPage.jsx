import React, { Component } from 'react';

class SearchPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      sym: '',
      stock: {},
      stockFound: false,
      count: 0
    };
  }
  incrCount = () => {
    const count = this.state.count + 1;
    this.setState({
      count
    });
  };
  decrCount = () => {
    const count = this.state.count - 1;
    this.setState({
      count
    });
  };
  check = sym => this.props.validCheck(sym);
  broker = sym => this.props.getStock(sym);
  changeVal = e => {
    const symbol = e.target.value.toUpperCase();
    console.log(symbol);
    if (this.check(symbol)) {
      const stock = this.broker(symbol);
      if (stock) {
        this.setState({
          sym: symbol,
          stock,
          stockFound: true
        });
      }
    } else {
      this.setState({
        sym: symbol,
        stock: {},
        stockFound: false
      });
    }
  };
  render() {
    const cost = this.state.stock.price * this.state.count;
    return (
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
                    value={this.state.sym}
                    type="text"
                    class="input is-primary is-medium is-rounded"
                    onChange={this.changeVal}
                  />
                  <span
                    class="icon is-medium is-right clickable"
                    onClick={() => {
                      console.log('click');
                    }}>
                    🔍
                  </span>
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
                <p class="title">{this.state.stock.sym || ''}</p>
              </div>
            </div>
            <div class="level-item has-text-centered">
              <div>
                <p class="heading">Company</p>
                <p class="title">{this.state.stock.company || ''}</p>
              </div>
            </div>
            <div class="level-item has-text-centered">
              <div>
                <p class="heading">Price (USD)</p>
                <p class="title">
                  {this.state.stock.price ? `$${this.state.stock.price}` : ''}
                </p>
              </div>
            </div>
            <div class="level-item has-text-centered">
              <div>
                <p class="heading">Status</p>
                <p class="title">
                  {this.state.stock.change
                    ? `0.${this.state.stock.change}%`
                    : ''}
                </p>
              </div>
            </div>
          </div>
        </div>
        {this.state.stockFound && this.props.logged ? (
          <div className="section">
            <div className="level">
              <div className="level-item">
                <button
                  className="button is-small"
                  onClick={this.decrCount}
                  disabled={this.state.count == 0}>
                  {' '}
                  -{' '}
                </button>
                <span> {this.state.count} </span>
                <button className=" button is-small" onClick={this.incrCount}>
                  {' '}
                  +{' '}
                </button>
              </div>
            </div>
            <div className="level">
              <div className="level-item">
                <span
                  className={`tag is-large ${
                    cost > this.props.balance ? 'is-danger' : 'is-info'
                  }`}>
                  Cost: {cost.toFixed(2)}
                </span>
              </div>
            </div>
            <div className="level">
              <div className="level-item">
                <button
                  className="button is-medium is-info"
                  disabled={this.state.count == 0 || cost > this.props.balance}
                  onClick={() => {
                    this.props.buy({
                      price: cost,
                      amount: this.state.count,
                      sym: this.state.sym
                    });
                  }}>
                  Buy
                </button>
              </div>
            </div>
          </div>
        ) : null}
      </div>
    );
  }
}

export default SearchPage;
