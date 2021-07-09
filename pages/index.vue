<template>
  <div class="container">
    <div>
      <Logo />
      <h1 class="title">
        sutras
      </h1>
      <div class="links">
        <NuxtLink to="/sutras/diamond/" class="button--green">
          Diamond Sutra
        </NuxtLink>
        <NuxtLink to="/sutras/gateless-gate-mumonkan/" class="button--green">
          Gateless Gate
        </NuxtLink>
        <NuxtLink to="/sutras/seneca-on-the-shortness-of-life/" class="button--green">
          Shortness of Life
        </NuxtLink>
        <a
          href="https://github.com/life-itself/sutras"
          target="_blank"
          rel="noopener noreferrer"
          class="button--grey"
        >
          GitHub
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style>
/* Sample `apply` at-rules with Tailwind CSS
.container {
@apply min-h-screen flex justify-center items-center text-center mx-auto;
}
*/
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
