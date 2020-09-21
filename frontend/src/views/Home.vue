<template>
  <div class="home mt-4">
    <div class="container">
      <div v-for="question in questions" :key="question.pk">
        <p class="mb-0">
          Posted by:
          <span class="text-danger font-weight-bold">{{
            question.author
          }}</span>
        </p>
        <router-link
          class="question-link text-dark"
          :to="{ name: 'question', params: { slug: question.slug } }"
        >
          <h2>{{ question.content }}</h2>
        </router-link>
        <p>Answers: {{ question.answers_count }}</p>
        <hr />
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">...loading</p>
        <button
          class="btn btn-sm btn-outline-success"
          v-show="next"
          @click="getQuestions"
        >
          Load more
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "Home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false,
    };
  },
  methods: {
    getQuestions() {
      let endpoint = "api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint).then((data) => {
        this.questions.push(...data.results);
        this.loadingQuestions = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
  },
  created() {
    this.getQuestions();
    document.title = "TavaresForum";
  },
};
</script>

<style scoped>
a h2 {
  font-weight: bold !important;
}
a:hover {
  text-decoration: none;
}
</style>
