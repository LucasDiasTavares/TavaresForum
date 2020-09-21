<template>
  <div class="single-question mt-2">
    <div class="container">
      <h1>{{ question.content }}</h1>
      <p class="mb-0">
        Posted by:
        <span class="text-danger font-weight-bold">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
    </div>
    <hr />
    <div class="container">
      <AnswerComponent
        v-for="(answer, index) in answers"
        :key="index"
        :answer="answer"
      />
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";
import AnswerComponent from "@/components/Answer";

export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components: {
    AnswerComponent,
  },
  data() {
    return {
      question: {},
      answers: [],
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getQuestionData() {
      let endpoint = `/api/questions/${this.slug}/`;
      apiService(endpoint).then((data) => {
        this.question = data;
        this.setPageTitle(data.content);
      });
    },
    getQuestionAnswers() {
      let endpoint = `/api/questions/${this.slug}/answers/`;
      apiService(endpoint).then((data) => {
        this.answers = data.results;
      });
    },
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
  },
};
</script>

<style scoped></style>
