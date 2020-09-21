<template>
  <div class="home">
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
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
  name: "Home",
  data() {
    return {
      questions: []
    };
  },
  methods: {
    getQuestions() {
      let endpoint = "api/questions/";
      apiService(endpoint).then(data => {
        this.questions.push(...data.results);
      });
    }
  },
  created() {
    this.getQuestions();
    document.title = "TavaresForum";
  }
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
