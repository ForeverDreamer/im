<template>
  <!--  <div class="container my-class">BV</div>-->
  <div class="main-window">
    <div class="main-window__aside">aside</div>
    <div class="main-window__content">content</div>
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
