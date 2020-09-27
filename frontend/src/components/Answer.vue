<template>
  <div class="border-bottom">
    <p class="text-muted">
      <strong>{{ answer.author }}</strong>
      &#8901; {{ answer.created_at }}
    </p>
    <p>{{ answer.body }}</p>
    <div class="mt-2 mb-4" v-if="isAnswerAuthor">
      <router-link
        :to="{ name: 'answer-editor', params: { id: answer.id } }"
        class="btn btn-sm btn-outline-warning mr-3"
        >Edit</router-link
      >
      <button
        @click="triggerDeleteAnswer"
        class="btn btn-sm btn-outline-danger"
      >
        Delete
      </button>
    </div>
    <div v-else>
      <button
        @click="toggleLike"
        class="btn btn-sm mb-4 "
        :class="{
          'btn-danger': userLikedAnswer,
          'btn-outline-danger': !userLikedAnswer
        }"
      >
        <strong> Like [{{ likesCounter }}] </strong>
      </button>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "AnswerComponent",
  props: {
    answer: {
      type: Object,
      required: true
    },
    requestUser: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      userLikedAnswer: this.answer.user_has_voted,
      likesCounter: this.answer.likes_count
    };
  },
  computed: {
    isAnswerAuthor() {
      return this.answer.author === this.requestUser;
    }
  },
  methods: {
    triggerDeleteAnswer() {
      this.$emit("delete-answer", this.answer);
    },
    toggleLike() {
      this.userLikedAnswer === false ? this.LikeAnswer() : this.unLikeAnswer;
    },
    unLikeAnswer() {
      this.userLikedAnswer = true;
      this.likesCounter -= 1;
      let endpoint = `/api/answers/${this.answer.id}/like/`;
      apiService(endpoint, "DELETE");
    },
    LikeAnswer() {
      this.userLikedAnswer = true;
      this.likesCounter += 1;
      let endpoint = `/api/answers/${this.answer.id}/like/`;
      apiService(endpoint, "POST");
    }
  }
};
</script>
