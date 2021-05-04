<template>
  <article class="prose lg:prose-xl max-w-2xl mx-auto pt-36">
    <h1>{{ article.title }}</h1>
    <p class="text-sm">
      Source: <a :href="article.source"> {{article.source}}</a>
      <br /><br />
      Alternative sources: <a :href="article.alt"> {{article.alt}}</a>
    </p>
    <nuxt-content :document="article" />
  </article>
</template>

<script>
  export default {
    async asyncData({ $content, params }) {
      const article = await $content('sutras', params.slug).fetch()
      return { article }
    }
  }
</script>

<style>
body {
  font-family: 'Libre Baskerville',  serif;
}
</style>
