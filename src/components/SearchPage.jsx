import React, { Component } from 'react';

class SearchPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      sym: '',
      stock: {}
    };
  }
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
          stock
        });
      }
    } else {
      this.setState({
        sym: symbol,
        stock: {}
      });
    }
  };
  render() {
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
      </div>
    );
  }
}

export default SearchPage;
