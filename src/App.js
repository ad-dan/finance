import React, { Component } from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Link,
  Route,
  Redirect
} from 'react-router-dom';
import Navbar from './components/Navbar';
import LandingHero from './components/LandingHero';
import LogPage from './components/LogPage';
import SearchPage from './components/SearchPage';
import RegPage from './components/RegPage';
import Assets from './components/Assets';
import UserNav from './components/UserNav';
/*
  TODO:
    https://www.marketwatch.com/tools/industry/stocklist.asp?bcind_ind=9535&bcind_period=3mo
    https://www.barchart.com/stocks/top-100-stocks
*/
class App extends Component {
  constructor() {
    super();
    const stocks = JSON.parse(localStorage.getItem('stocks')) || {
      GE: ['General Electric', '12.46'],
      BAC: ['Bank of America', '31.19'],
      F: ['Ford Motor', '9.81'],
      NIO: ['NIO ADR', '8.78'],
      ELAN: ['Elanco Animal Health', '36.00'],
      CHK: ['Chesapeake Energy', '4.41'],
      SNAP: ['Snap', '9.21'],
      ORCL: ['Oracle', '50.43'],
      T: ['AT&T', '33.44'],
      C: ['Citigroup', '74.79'],
      SWN: ['Southwestern Energy', '5.64'],
      KEY: ['KeyCorp', '20.75'],
      BABA: ['Alibaba Group Holding ADR', '165.88'],
      FCX: ['Freeport-McMoRan', '14.39'],
      ABEV: ['Ambev ADR', '4.62'],
      RIG: ['Transocean', '12.63'],
      WFC: ['Wells Fargo', '55.55'],
      CGC: ['Canopy Growth', '52.40'],
      VALE: ['Vale ADR', '14.52'],
      PFE: ['Pfizer', '43.75'],
      FTV: ['Fortive', '87.37'],
      JPM: ['JPMorgan Chase', '118.63'],
      TWTR: ['Twitter', '29.85'],
      ABX: ['Barrick Gold', '10.62'],
      NOK: ['Nokia ADR', '5.52'],
      VZ: ['Verizon Communications', '53.95'],
      PBR: ['Petroleo Brasileiro ADR', '11.36'],
      VIPS: ['Vipshop Holdings ADR', '6.55'],
      KKR: ['KKR Cl A', '28.02'],
      NLY: ['Annaly Capital Management', '10.31'],
      WFT: ['Weatherford International', '2.57'],
      KMI: ['Kinder Morgan', '18.04'],
      EGO: ['Eldorado Gold', '0.89'],
      ITUB: ['Itau Unibanco Holding ADR', '10.64'],
      HST: ['Host Hotels&Resorts', '21.22'],
      UAA: ['Under Armour Cl A', '20.00'],
      MS: ['Morgan Stanley', '49.88'],
      CLF: ['Cleveland-Cliffs', '12.22'],
      GM: ['General Motors', '36.08'],
      ESV: ['ENSCO', '7.70'],
      EB: ['Eventbrite', '36.50'],
      CTL: ['CenturyLink', '22.57'],
      VER: ['VEREIT', '7.46'],
      WMB: ['Williams', '28.25'],
      FBP: ['First BanCorp (Puerto Rico)', '9.04'],
      ATUS: ['Altice USA Cl A', '19.21'],
      XOM: ['Exxon Mobil', '84.82'],
      RRC: ['Range Resources', '17.82'],
      RHT: ['Red Hat', '133.81'],
      SO: ['Southern', '43.29'],
      HPQ: ['HP', '25.69'],
      SAN: ['Banco Santander ADR', '5.41'],
      JCP: ['J.C. Penney', '2.00'],
      AUY: ['Yamana Gold', '2.54'],
      INFY: ['Infosys ADR', '10.07'],
      AKS: ['AK Steel Holding', '4.85'],
      KO: ['Coca-Cola', '46.64'],
      ADT: ['ADT', '8.92'],
      PG: ['Procter&Gamble', '85.36'],
      SQ: ['Square Cl A', '86.51'],
      BP: ['BP ADR', '44.57'],
      TEVA: ['Teva Pharmaceutical Industries ADR', '24.83'],
      NWL: ['Newell Brands', '22.00'],
      KR: ['Kroger', '29.18'],
      RF: ['Regions Financial', '19.49'],
      HPE: ['Hewlett Packard Enterprise', '16.87'],
      SBGL: ['Sibanye-Stillwater ADR', '2.51'],
      X: ['United States Steel', '29.85'],
      STM: ['STMicroelectronics', '19.06'],
      DNR: ['Denbury Resources', '5.54'],
      DWDP: ['DowDuPont', '70.03'],
      GGB: ['Gerdau ADR', '4.15'],
      KGC: ['Kinross Gold', '3.01'],
      MRO: ['Marathon Oil', '21.55'],
      PHM: ['PulteGroup', '26.39'],
      HAL: ['Halliburton', '40.39'],
      AVP: ['Avon Products', '2.40'],
      GLW: ['Corning', '36.13'],
      SPN: ['Superior Energy Services', '9.61'],
      RDC: ['Rowan Cos.', '17.48'],
      COTY: ['Coty Cl A', '13.01'],
      DIS: ['Walt Disney', '111.62'],
      V: ['VISA Cl A', '149.24'],
      NE: ['Noble', '6.51'],
      SLB: ['Schlumberger', '61.57'],
      BHC: ['Bausch Health', '25.01'],
      COG: ['Cabot Oil&Gas', '22.90'],
      HL: ['Hecla Mining', '3.04'],
      THO: ['Thor Industries', '91.95'],
      GG: ['Goldcorp', '10.77'],
      CAT: ['Caterpillar', '156.00'],
      CVS: ['CVS Health', '79.39'],
      BEN: ['Franklin Resources', '32.92'],
      ECA: ['Encana', '12.64'],
      SKX: ['Skechers USA Cl A', '26.58'],
      M: ["Macy's", '35.18'],
      UNP: ['Union Pacific', '164.01'],
      MPC: ['Marathon Petroleum', '81.93'],
      NKE: ['Nike Cl B', '85.37'],
      RIO: ['Rio Tinto ADR', '51.15'],
      HDB: ['HDFC Bank Limited', '93.61'],
      TYO: ['Tokyo Stock Exchange', '24.77'],
      NZE: ['New Zealand Exchange', '0.66'],
      MSFT: ['Microsoft Corporation', '115.61'],
      TL0: ['Tesla Inc', '310.345'],
      KBT: ['K3 Business Technology Group','242.50'], //new
      K3C: ['K3 Capital Group','291.00'],
      KNOS: ['Kainos Group','425.00'],
      KAPE: ['Kape Technologies','126.50'],
      KDR: ['Karelian Diamond Resource','4.55'],
      KAT: ['Katoro Gold Mining','1.20'],
      KAV: ['Kavango Resources Ord 0.1p','2.55'],
      KAZ: ['Kaz Minerals','537.40'],
      KZG: ['Kazera Global Ord 1p','2.25'],
      KCOM: ['KCOM Group','94.25'],
      KCR: ['KCR Residential Reit','74.50'],
      BME: ['B&M European Value Retail','74.50']
      
    };
    const users = JSON.parse(localStorage.getItem('users')) || {};
    const database = JSON.parse(localStorage.getItem('database')) || {};
    this.state = {
      stocks,
      users,
      database,
      current: {},
      logged: false
    };
  }
  getStock = name => {
    const stock = this.state.stocks[name];
    const change = Math.floor(Math.random() * 100);
    if (stock) {
      return {
        sym: name,
        company: stock[0],
        price: stock[1],
        change
      };
    }
  };
  regUser = user => {
    const { users } = this.state;
    console.log(users);
    users[user.name] = user.pass;
    const entry = this.generateUser(user);
    const { database } = this.state;
    database[user.name] = entry;
    this.setState({
      users,
      database
    });
  };
  userLog = ({ name, pass }) => {
    return this.state.users[name] && this.state.users[name] === pass;
  };
  generateUser = ({ name, pass }) => {
    const newUser = {
      name,
      pass,
      balance: 1000,
      portfolio: []
    };
    return newUser;
  };
  buyStock = ({ price, amount, sym }) => {
    const { current, database } = this.state;
    current.balance -= price;
    const stock = {
      sym,
      name: this.state.stocks[sym][0],
      amount,
      value: price
    };
    current.portfolio.push(stock);
    database[current.name] = current;
    this.setState({
      current,
      database
    });
  };
  sellStock = ({ price, sym }) => {
    const { current, database } = this.state;
    current.balance += price;
    const index = current.portfolio.findIndex(stock => stock.sym === sym);
    current.portfolio.splice(index, 1);
    database[current.name] = current;
    this.setState({
      current,
      database
    });
  };
  loginUser = ({ name, pass }) => {
    const current = this.state.database[name];
    console.table(current);
    this.setState({
      current,
      logged: true
    });
  };
  logoutUser = () => {
    if (this.state.logged) {
      this.setState({
        current: {},
        logged: false
      });
    }
  };
  userExists = name => !!this.state.users[name];
  isValidStock = sym => !!this.state.stocks[sym];
  componentDidUpdate() {
    localStorage.setItem('database', JSON.stringify(this.state.database));
    localStorage.setItem('users', JSON.stringify(this.state.users));
  }
  render() {
    return (
      <Router>
        <div className="is-dec">
          {this.state.logged ? (
            <UserNav out={this.logoutUser} money={this.state.current.balance} />
          ) : (
            <Navbar />
          )}
          <Route
            path={`${process.env.PUBLIC_URL}/dashboard`}
            component={() =>
              this.state.logged ? (
                <Assets user={this.state.current} sell={this.sellStock} />
              ) : (
                <LandingHero />
              )
            }
          />
          <Route
            exact
            path={`${process.env.PUBLIC_URL}/`}
            component={LandingHero}
          />
          <Route
            path={`${process.env.PUBLIC_URL}/login`}
            render={() =>
              this.state.logged ? (
                <Redirect
                  to={`${process.env.PUBLIC_URL}/dashboard`}
                  user={this.state.current}
                />
              ) : (
                <div>
                  <LandingHero />
                  <LogPage
                    validCheck={this.userLog}
                    register={this.loginUser}
                  />
                </div>
              )
            }
          />
          <Route
            path={`${process.env.PUBLIC_URL}/register`}
            component={() => (
              <div>
                <LandingHero />
                <RegPage validCheck={this.userExists} regUser={this.regUser} />
              </div>
            )}
          />
          <Route
            path={`${process.env.PUBLIC_URL}/search`}
            component={() => (
              <SearchPage
                buy={this.buyStock}
                validCheck={this.isValidStock}
                getStock={this.getStock}
                logged={this.state.logged}
                balance={this.state.current.balance}
                stocks={this.state.stocks}
              />
            )}
          />
        </div>
      </Router>
    );
  }
}

export default App;
