<template>
  <!--  <div class="container my-class">BV</div>-->
  <div class="main-window">
    <div class="h2 mb-0">
      <b-icon icon="arrow-up"></b-icon>
      <b-icon icon="exclamation-triangle"></b-icon>
      <p class="h1 mb-2">
        Icon <b-icon icon="exclamation-circle-fill"></b-icon>
      </p>
      <p class="h2 mb-2">
        Icon <b-icon icon="exclamation-circle-fill"></b-icon>
      </p>
      <p class="h3 mb-2">
        Icon <b-icon icon="exclamation-circle-fill"></b-icon>
      </p>
      <p class="h4 mb-2">
        Icon <b-icon icon="exclamation-circle-fill"></b-icon>
      </p>
      <p class="h5 mb-2">
        Icon <b-icon icon="exclamation-circle-fill"></b-icon>
      </p>
      <b-icon icon="battery-full" style="color: #7952b3"></b-icon>
    </div>
    <!--    <div class="main-window__aside">aside</div>-->
    <!--    <div class="main-window__content">content</div>-->
  </div>
</template>

<script>
export default {
  name: 'Bv',
}
</script>

<style scoped>
.main-window {
  border: 1px solid red;
  padding: 1rem;
  height: 100vh;
  display: flex;
  font-size: 1rem;
}

.main-window__aside {
  background: gray;
  width: 20%;
  margin-right: 1rem;
}

.main-window__content {
  background: black;
  width: 80%;
}

.my-class {
  width: 100%;
  max-width: 100%;
  border: 1px solid black;
  background: gray;
  height: 100vh;
}

@media (max-width: 1400px) {
  .my-class {
    width: 90%;
  }
}

@media (max-width: 1200px) {
  .my-class {
    width: 80%;
  }
}

@media (max-width: 992px) {
  .my-class {
    width: 70%;
  }
}

@media (max-width: 768px) {
  .my-class {
    width: 60%;
  }
}

@media (max-width: 576px) {
  .my-class {
    width: 50%;
  }
}
</style>
