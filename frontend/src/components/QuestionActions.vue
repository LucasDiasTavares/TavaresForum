<template>
  <div class="question-actions">
    <router-link
      :to="{ name: 'question-editor', params: { slug: slug } }"
      class="btn btn-sm btn-outline-warning mr-3"
      >Edit</router-link
    >
    <button @click="deleteQuestion" class="btn btn-sm btn-outline-danger">
      Delete
    </button>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "QuestionActions",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    async deleteQuestion() {
      let endpoint = `/api/questions/${this.slug}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$router.push("/");
      } catch (err) {
        console.log(err);
      }
    }
  }
};
</script>