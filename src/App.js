import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import LandingHero from './components/LandingHero';
import Modal from './components/Modal';
import SearchPage from './components/SearchPage';

const stocks = {
  GE: ['General Electric', '$12.46'],
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
  RIO: ['Rio Tinto ADR', '51.15']
};

class App extends Component {
  getStock = name => {
    const stock = stocks[name];
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
  isValidStock = sym => !!stocks[sym];
  render() {
    return (
      <Router>
        <div>
          <Navbar />
          <Route exact path="/" component={LandingHero} />
          <Route path="/login" component={Modal} />

          <Route
            path="/search"
            component={() => (
              <SearchPage
                validCheck={this.isValidStock}
                getStock={this.getStock}
              />
            )}
          />
        </div>
      </Router>
    );
  }
}

export default App;
