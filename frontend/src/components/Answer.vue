<template>
  <div class="border-bottom">
    <p class="text-muted">
      <strong>{{ answer.author }}</strong>
      &#8901; {{ answer.created_at }}
    </p>
    <p>{{ answer.body }}</p>
    <div class="mt-2 mb-4" v-if="isAnswerAuthor">
      <router-link
        :to="{name: 'answer-editor', params: {id: answer.id}}"
        class="btn btn-sm btn-outline-warning mr-3"
      >Edit</router-link>
      <button @click="triggerDeleteAnswer" class="btn btn-sm btn-outline-danger">Delete</button>
    </div>
  </div>
</template>

<script>
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
  computed: {
    isAnswerAuthor() {
      return this.answer.author === this.requestUser;
    }
  },
  methods: {
    triggerDeleteAnswer() {
      this.$emit("delete-answer", this.answer);
    }
  }
};
</script>
