<template>
  <div class="single-question mt-2 container">
    <div>
      <h1>{{ question.content }}</h1>
      <p class="mb-0">
        Posted by:
        <span class="text-danger font-weight-bold">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
      <hr />
    </div>
    <div class="border-bottom mb-3" v-if="userHasAnswered">
      <p class="font-weight-bold text-success">
        You've already written an answer!
      </p>
    </div>
    <div v-else-if="showForm">
      <form class="card" @submit.prevent="onSubmit">
        <div class="card-header px-3">
          Answer the question
        </div>
        <div class="card-block">
          <textarea
            placeholder="Share your knowledge!"
            class="form-control"
            v-model="newAnswerBody"
            rows="5"
          ></textarea>
        </div>
        <div class="card-footer px-3">
          <button class="btn btn-sm btn-success" type="submit">
            Submit your answer
          </button>
        </div>
      </form>
      <p class="text-danger mt-2 font-weight-bold">{{ error }}</p>
    </div>
    <div v-else>
      <button @click="showForm = true" class="btn btn-sm btn-success">
        Answer the question
      </button>
    </div>
    <div>
      <AnswerComponent
        v-for="(answer, index) in answers"
        :key="index"
        :answer="answer"
      />
    </div>
    <div class="container my-4">
      <p v-show="loadingAnswers">...loading...</p>
      <button
        class="btn btn-sm btn-outline-success"
        v-show="next"
        @click="getQuestionAnswers"
      >
        Load more answers
      </button>
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
      newAnswerBody: null,
      error: null,
      userHasAnswered: false,
      showForm: false,
      next: null,
      loadingAnswers: false,
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
        this.userHasAnswered = data.user_has_answered;
        this.setPageTitle(data.content);
      });
    },
    getQuestionAnswers() {
      let endpoint = `/api/questions/${this.slug}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingAnswers = true;
      apiService(endpoint).then((data) => {
        this.answers.push(...data.results);
        this.loadingAnswers = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },
    onSubmit() {
      if (this.newAnswerBody) {
        let endpoint = `/api/questions/${this.slug}/answer/`;
        apiService(endpoint, "POST", { body: this.newAnswerBody }).then(
          (data) => {
            this.answers.unshift(data);
          }
        );
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty answer!";
      }
    },
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
  },
};
</script>

<style scoped></style>
