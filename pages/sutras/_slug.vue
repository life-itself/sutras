<template>
<section class="md:grid md:grid-cols-4 md:gap-4 pt-24 px-4">
  <header class="prose lg:prose-xl md:col-start-2 md:col-span-2">
    <h1 class="text-center leading-6">{{ article.title }}</h1>
    <p class="text-sm truncate">
      Source: <a :href="article.source">{{article.source}}</a>
    </p>
  </header>
  <aside ref="toc" class="pt-6 md:pt-0 md:col-start-1 md:col-span-1 md:flex md:flex-col">
    <div class="sticky top-16">
      <h2
        class="uppercase text-black font-h2 text-lg lg:mt-16 tracking-wider"
      >
        Table of contents
      </h2>
      <nav class="mt-4">
        <ul>
          <li
            @click="tableOfContentsHeadingClick(link)"
            :class="{
              'pl-4': link.depth === 3,
            }"
            class="toc-list"
            v-for="link of article.toc"
            :key="link.id"
          >
            <a
            :class="{
                'text-red-500 hover:text-red-600': link.id === currentlyActiveToc,
                'text-black hover:gray-900': link.id !== currentlyActiveToc,
              }"
              role="button"
              class="transition-colors duration-75 text-base mb-2 block"
              :href="`#${link.id}`"
              >{{ link.text }}</a
            >
          </li>
        </ul>
      </nav>
    </div>
  </aside>
  <article class="prose lg:prose-xl md:col-span-2">
    <nuxt-content :document="article" />
  </article>
</section>
</template>

<script>
export default {
  data() {
    return {
      currentlyActiveToc: "",
      observer: null,
      observerOptions: {
        root: this.$refs.nuxtContent,
        threshold: 0,
      },
    };
  },
  mounted() {
    this.observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          const id = entry.target.getAttribute('id');
          if (entry.isIntersecting) {
            this.currentlyActiveToc = id;
          }
      });
    }, this.observerOptions);

    // Track all sections that have an `id` applied
    document.querySelectorAll('.nuxt-content h2[id], .nuxt-content h3[id]').forEach((section) => {
        this.observer.observe(section);
    });
  },
  beforeDestroy() {
    this.observer.disconnect();
  },
  async asyncData({ $content, params }) {
    const article = await $content('sutras', params.slug).fetch()
    return { article }
  },
  methods: {
    tableOfContentsHeadingClick(link) {
      this.currentlyActiveToc = link.id;
    },
  }
};
</script>

<style>
body {
  font-family: Inter, Raleway, sans-serif;
}

h1, h2, h3, h4 {
  font-family: 'Libre Baskerville',  serif;
}

.prose h1 {
  line-height: 1.3;
}

div.footnotes {
  font-size: small;
}

.footnote-ref {
  font-size: small;
}

</style>
