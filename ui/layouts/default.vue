<template>
  <div>
    <Nuxt />
  </div>
</template>

<script>
export default {
  middleware: ['init-auth'],
}
</script>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

/*.button--green {*/
/*  display: inline-block;*/
/*  border-radius: 4px;*/
/*  border: 1px solid #3b8070;*/
/*  color: #3b8070;*/
/*  text-decoration: none;*/
/*  padding: 10px 30px;*/
/*}*/

/*.button--green:hover {*/
/*  color: #fff;*/
/*  background-color: #3b8070;*/
/*}*/

/*.button--grey {*/
/*  display: inline-block;*/
/*  border-radius: 4px;*/
/*  border: 1px solid #35495e;*/
/*  color: #35495e;*/
/*  text-decoration: none;*/
/*  padding: 10px 30px;*/
/*  margin-left: 15px;*/
/*}*/

/*.button--grey:hover {*/
/*  color: #fff;*/
/*}*/

.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #2f343d;
  color: #333;
  text-align: center;
  /*line-height: 200px;*/
}

.el-main {
  background-color: #f2f3f5;
  color: #333;
  text-align: center;
  /*line-height: 160px;*/
  position: relative;
  padding: 0;
}

.el-container {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  padding-right: 10px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

.icon {
  cursor: pointer;
  font-size: 20px;
  color: #9ea2a8;
}
</style>
