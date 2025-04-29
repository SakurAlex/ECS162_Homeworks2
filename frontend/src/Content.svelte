<script lang="ts">
  const BASE_URL = 'http://127.0.0.1:8000';
  import { onMount } from 'svelte';
  onMount(() => {
    fetch(`${BASE_URL}/api/ucdavis-news`)
      .then(statusCheck)
      .then(resp => resp.json())
      .then(processData)
      .catch(handleError); 
  });

  /**
   * This function processes the data.
   * 
   * @param {any} data - The data from the fetch request.
   */
  function processData(data: any) {
    console.log(data);
  }
  /**
  * This function checks if the response is ok.
  * 
  * @param {Response} res - The response from the fetch request.
  * @returns {Promise<Response>} The response from the fetch request.
  */
  async function statusCheck(res: Response) {
    if (!res.ok) {
      throw new Error(await res.text());
    }
    return res;
  }
  /**
   * This function handles the error.
   * 
   * @param {Error} err - The error from the fetch request.
   */
  function handleError(err: Error) {
    alert("Error:" + err.message);
  }

</script>

<main id="content">
  <!-- Three-column layout -->
  <!-- Left column: featured articles -->
  <section class="articles">
    <article>
      <div>
        <a href="https://www.nytimes.com/">
          <h2 class="title">
            <!-- Headline -->
            Lorem ipsum dolor sit amet consectetur adipiscing elit.
          </h2>
        </a>
        <p class="abstract">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <!-- Full summary -->
        <p class="readtime">7 MIN READ</p>
        <!-- Read time -->
      </div>

      <div class="hline"></div>
      <!-- Separator -->

      <div>
        <a href="https://www.nytimes.com/">
          <h2 class="title">Dolor sit amet consectetur adipiscing elit quisque faucibus.</h2>
        </a>
        <p class="abstract">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <!-- Full summary -->
        <p class="readtime">5 MIN READ</p>
      </div>

      <figure class="images">
        <img
          src="https://static01.nyt.com/images/2025/03/02/us/16met-prison-death1/16met-prison-death1-threeByTwoMediumAt2X.jpg?format=pjpg&quality=75&auto=webp&disable=upscale"
          alt="building"
        />
        <!-- Image -->
      </figure>

      <div class="hline"></div>
      <!-- Separator -->

      <div>
        <a href="https://www.nytimes.com/">
          <h2>Dolor sit amet consectetur adipiscing elit quisque faucibus.</h2>
        </a>
        <p class="abstract">
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
          dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
          proident, sunt in culpa qui officia deserunt mollit anim id est
          laborum.
        </p>
        <!-- Full summary -->
        <p class="readtime">4 MIN READ</p>
      </div>

      <figure class="images">
        <img
          src="https://static01.nyt.com/images/2025/04/16/multimedia/16int-canada-spa-zmwq/16int-canada-spa-zmwq-threeByTwoMediumAt2X.jpg?format=pjpg&quality=75&auto=webp&disable=upscale"
          alt="ocean"
        />
        <!-- Image -->
      </figure>
    </article>
  </section>

  <!-- The line that separates the left and middle columns -->
  <div class="pline" id="lineleft"></div>

  <!-- Middle column: contain both images and text -->
  <section class="images" id="middle">
    <figure>
      <img
        src="https://static01.nyt.com/images/2025/04/15/multimedia/15nat-harvard-why-01-pcvk/15nat-harvard-why-01-pcvk-threeByTwoMediumAt2X.jpg?format=pjpg&quality=75&auto=webp&disable=upscale"
        alt="trees"
      />
      <!-- Image -->
    </figure>

    <section class="articles">
      <article>
        <div>
          <a href="https://www.nytimes.com/">
            <h2 class="title">
              Conubia nostra inceptos himenaeos orci varius natoque penatibus.
            </h2>
          </a>
          <p class="abstract">
            Urna tempor pulvinar vivamus fringilla lacus nec metus. Iaculis
            massa nisl malesuada lacinia integer nunc posuere. Semper vel class
            aptent taciti sociosqu ad litora.
          </p>
          <!-- Full summary -->
          <p class="readtime">7 MIN READ</p>
        </div>
      </article>
    </section>

    <figure>
      <img
        src="https://static01.nyt.com/images/2025/05/15/multimedia/15dc-iran-nukes-zcqh/15dc-iran-nukes-zcqh-threeByTwoMediumAt2X.jpg?format=pjpg&quality=75&auto=webp&disable=upscale"
        alt="trees"
      />
      <!-- Image -->
    </figure>

    <section class="articles">
      <article>
        <div>
          <h2 class="title">Placerat in id cursus mi pretium tellus duis.</h2>
          <p class="abstract">
            Ex sapien vitae pellentesque sem placerat in id. Placerat in id
            cursus mi pretium tellus duis.
          </p>
          <!-- Full summary -->
          <p class="readtime">4 MIN READ</p>
        </div>
        <div class="hline"></div>
        <!-- Separator -->
        <div>
          <h2 class="title">Urna tempor pulvinar vivamus fringilla lacus nec metus.</h2>
          <p class="abstract">
            Nulla molestie mattis scelerisque maximus eget fermentum odio. Purus
            est efficitur laoreet mauris pharetra vestibulum fusce.
          </p>
          <!-- Full summary -->
          <p class="readtime">3 MIN READ</p>
        </div>
      </article>
    </section>
  </section>

  <div class="pline" id="lineright"></div>
  <!-- Divider -->

  <!-- Right column: mosaic + opinion -->
  <aside>
    <figure>
      <!-- Grid of four images -->
      <img
        class="picture"
        src="https://static01.nyt.com/images/2025/04/15/mosaic-traffwnba-2025final-47-838/mosaic-traffwnba-2025final-47-838-square640.jpg?quality=75&auto=webp"
        alt="woman"
      />
      <img
        class="picture"
        src="https://static01.nyt.com/images/2025/04/15/mosaic-traffwnba-2025final-11-412/mosaic-traffwnba-2025final-11-412-square640-v2.jpg?quality=75&auto=webp"
        alt="woman"
      />
      <img
        class="picture"
        src="https://static01.nyt.com/images/2025/04/15/mosaic-traffwnba-2025final-21-675/mosaic-traffwnba-2025final-21-675-square640.jpg?quality=75&auto=webp"
        alt="woman"
      />
      <img
        class="picture"
        src="https://static01.nyt.com/images/2025/04/15/mosaic-traffwnba-2025final-55-582/mosaic-traffwnba-2025final-55-582-square640.jpg?quality=75&auto=webp"
        alt="woman"
      />
    </figure>

    <div class="articles">
      <article>
        <div class="hline"></div>
        <!-- Separator -->
        <div>
          <h2 class="title">Dis parturient montes nascetur ridiculus</h2>
          <p class="abstract">
            Primis vulputate ornare sagittis vehicula praesent dui felis.
            Senectus netus suscipit auctor curabitur facilisi cubilia curae.
            Quisque faucibus ex sapien vitae pellentesque sem placerat.
          </p>
          <!-- Full summary -->
          <p class="readtime">7 MIN READ</p>
        </div>
      </article>
    </div>

    <figure>
      <img
        class="picture"
        src="https://static01.nyt.com/images/2025/04/16/opinion/15stephens/15stephens-smallSquare252-v2.jpg?format=pjpg&quality=75&auto=webp"
        alt="nuclear energy"
      />
      <img
        class="picture"
        src="https://static01.nyt.com/images/2025/04/16/opinion/15stephens/15stephens-smallSquare252-v2.jpg?format=pjpg&quality=75&auto=webp"
        alt="nuclear energy"
      />
    </figure>

    <div class="articles">
      <article>
        <div class="hline"></div>
        <!-- Separator -->
        <div>
          <h2 class="title">
            Blandit quis suspendisse aliquet nisi sodales consequat magna.
            Ligula congue sollicitudin erat viverra ac tincidunt nam.
          </h2>
          <p class="abstract">
            Primis vulputate ornare sagittis vehicula praesent dui felis.
            Senectus netus suscipit auctor curabitur facilisi cubilia curae.
            Quisque faucibus ex sapien vitae pellentesque sem placerat.
          </p>
          <p class="readtime">4 MIN READ</p>
        </div>
        <div class="hline"></div>
        <!-- Separator -->
        <div>
          <h2 class="title">Bridiculus mus donec rhoncus eros lobortis nulla molestie.</h2>
          <p class="abstract">
            Primis vulputate ornare sagittis vehicula praesent dui felis.
            Senectus netus suscipit auctor curabitur facilisi cubilia curae.
            Quisque faucibus ex sapien vitae pellentesque sem placerat.
          </p>
          <p class="readtime">8 MIN READ</p>
        </div>
      </article>
    </div>
  </aside>
</main>

<style>
  #content {
    margin-top: 1rem;
    gap: 1rem;
    display: flex;
    flex-direction: row;
  }
  .articles {
    display: flex;
    display: column;
    flex: 1;
    font-family: "Newsreader", serif;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
    gap: 1rem;
  }

  .articles article h2 {
    font-size: 1.2rem;
    cursor: pointer;
  }
  .articles p {
    margin: 0.8rem 0 0.2rem 0;
    font-size: 1rem;
    color: rgb(114, 110, 110);
  }

  .hline {
    height: 0.5px;
    background-color: rgb(175, 165, 165);
    margin: 1rem 0;
  }

  .articles .readtime {
    font-family: "Lato", sans-serif;
    margin: 0.5rem 0 0.2rem 0;
    font-weight: 350;
    font-size: 0.7rem;
    font-style: normal;
  }

  .images {
    flex: 1.2;
    margin: 0rem 0.5rem;
  }
  .images img {
    max-width: 100%;
    height: auto;
    margin: 1rem 0rem;
  }
  .pline {
    width: 0.5px;
    background-color: rgb(196, 190, 190);
  }
  #content aside {
    flex: 0.5;
  }
  #content aside img {
    max-width: 100%;
  }
  aside figure {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
  }
  .picture {
    width: 100%;
    height: auto;
  }
</style>
