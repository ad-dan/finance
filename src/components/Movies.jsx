import React from 'react';

const Movies = () => (
  <div class="section has-background-primary">
    <div class="tile is-ancestor">
      <div class="tile is-parent has-text-centered ">
        <div class="tile is-child is-2" />
        <div class="tile is-child is-3">
          <div class="box has-background-light">
            <div class="image-is-3by4">
              <img src="./wolf.jpeg" alt="Wolf of Wall Street poster" />
            </div>
            <div class="is-size-4 has-text-grey-dark">
              The Wolf of Wall Street
            </div>
            <div class="level">
              <div class="level-item">
                <div class="buttons has-addons">
                  <span class="button is-primary is-rounded">
                    <a
                      href="https://youtu.be/iszwuX1AK6A"
                      class="has-text-white">
                      Trailer
                    </a>
                  </span>
                  <span class="button is-primary is-rounded is-outlined">
                    <a
                      href="https://www.imdb.com/title/tt0993846/"
                      class="has-text-primary">
                      IMDb
                    </a>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="tile is-child is-2" />
        <div class="tile is-child is-3">
          <div class="box has-background-light">
            <div class="image-is-3by4">
              <img src="./short.jpg" alt="The Big Short" />
            </div>
            <div class="is-size-4 has-text-grey-darker">The Big Short</div>
            <div class="level">
              <div class="level-item">
                <div class="buttons has-addons">
                  <span class="button is-primary is-rounded">
                    <a
                      href="https://youtu.be/vgqG3ITMv1Q"
                      class="has-text-white">
                      Trailer
                    </a>
                  </span>
                  <span class="button is-primary is-rounded is-outlined ">
                    <a
                      href="https://www.imdb.com/title/tt1596363/"
                      class="has-text-primary">
                      IMDb
                    </a>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="tile is-child is-2" />
      </div>
    </div>
  </div>
);

export default Movies;
