import React from 'react';
import Eli5 from './Eli5';

const LandingHero = () => (
  <div>
    <div class="hero is-dec is-large">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="title">Capitalism is awesome!</div>
          <div class="subtitle">Invest money into the economy</div>
        </div>
      </div>
    </div>
    <Eli5 />
  </div>
);

export default LandingHero;
