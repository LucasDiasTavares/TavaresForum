<template>
  <div class="not-found">
    <div class="container mt-3">
      <h1 class="text-danger text-center font-weight-bold">{{ message }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  data() {
    return {
      message: "404 - Page not found"
    };
  }
};
</script>
