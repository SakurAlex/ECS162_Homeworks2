<script>
  import Header from "./Header.svelte";
  import Content from "./Content.svelte";
  import Footer from "./Footer.svelte";
</script>

<main>
  <Header />
  <Content />
  <Footer />
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  #vline {
    width: 1px;
    height: 1.2rem;
    background-color: rgb(175, 165, 165);
    margin: 1rem;
  }
</style>
