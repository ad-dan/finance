import React from 'react';
import Eli5 from './Eli5';
import Movies from './Movies';

const LandingHero = () => (
  <div>
    <div class="hero is-dec is-large">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="title has-text-white">Welcome to Mercury Finance</div>
          <div class="subtitle has-text-white">
            The best brokerage firm on Web
          </div>
        </div>
      </div>
    </div>
    <Eli5 />
    <Movies />
  </div>
);

export default LandingHero;
