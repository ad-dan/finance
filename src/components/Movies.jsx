import React from 'react';

const Movies = () => (
  <div class="section has-background-info mov">
    <div className="container">
      <div className="section">
        <div className="container has-text-centered">
          <div className="level">
            <div className="level-item title has-text-white">
              Our Recommended Watchs
            </div>
          </div>
        </div>
      </div>
      <div className="section">
        <div class="tile is-ancestor">
          <div class="tile is-parent has-text-centered ">
            <div class="tile is-child is-2" />
            <div class="tile is-child is-3">
              <div class="box b">
                <div class="image-is-3by4">
                  <img src="./wolf.jpeg" alt="Wolf of Wall Street poster" />
                </div>
                <div className="is-size-4 has-text-white is-hidden-desktop">
                  The Wolf of Wall Street
                </div>
                <div class="is-size-4 has-text-grey-dark is-hidden-touch">
                  The Wolf of Wall Street
                </div>
                <div class="level">
                  <div class="level-item">
                    <div class="buttons has-addons">
                      <span class="button is-info is-rounded is-hidden-touch">
                        <a
                          href="https://youtu.be/iszwuX1AK6A"
                          class="has-text-white">
                          Trailer
                        </a>
                      </span>
                      <span class="button is-info is-rounded is-hidden-desktop">
                        <a
                          href="https://youtu.be/iszwuX1AK6A"
                          class="has-text-white">
                          Trailer
                        </a>
                      </span>
                      <span class="button is-info is-inverted is-rounded is-hidden-desktop">
                        <a
                          href="https://www.imdb.com/title/tt0993846/"
                          class="has-text-info">
                          IMDb
                        </a>
                      </span>
                      <span class="button is-info is-rounded is-outlined is-hidden-touch">
                        <a
                          href="https://www.imdb.com/title/tt0993846/"
                          class="has-text-info">
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
              <div class="box b">
                <div class="image-is-3by4">
                  <img src="./short.jpg" alt="The Big Short" />
                </div>
                <div className="is-size-4 has-text-white is-hidden-desktop">
                  The Big Short
                </div>
                <div class="is-size-4 has-text-grey-darker is-hidden-touch">
                  The Big Short
                </div>
                <div class="level">
                  <div class="level-item">
                    <div class="buttons has-addons">
                      <span class="button is-info is-rounded is-hidden-touch">
                        <a
                          href="https://youtu.be/vgqG3ITMv1Q"
                          class="has-text-white">
                          Trailer
                        </a>
                      </span>
                      <span class="button is-info is-rounded is-hidden-desktop">
                        <a
                          href="https://youtu.be/vgqG3ITMv1Q"
                          class="has-text-white">
                          Trailer
                        </a>
                      </span>
                      <span class="button is-info  is-rounded is-inverted is-hidden-desktop">
                        <a
                          href="https://www.imdb.com/title/tt1596363/"
                          class="has-text-info">
                          IMDb
                        </a>
                      </span>
                      <span class="button is-info is-rounded is-outlined is-hidden-touch">
                        <a
                          href="https://www.imdb.com/title/tt1596363/"
                          class="has-text-info">
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
    </div>
  </div>
);

export default Movies;
