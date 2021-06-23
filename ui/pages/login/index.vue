<template>
  <div>
    <div class="login-background"></div>
    <div>
      <el-form
        ref="loginForm"
        class="login-container"
        :model="loginForm"
        :rules="rules"
      >
        <el-form-item prop="userName">
          <el-input
            v-model="loginForm.username"
            size="medium"
            placeholder="请输入用户名"
          >
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="loginForm.password"
            type="password"
            size="medium"
            placeholder="请输入密码"
          >
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            size="medium"
            :loading="loading"
            @click.prevent="tryLogin"
          >
            {{ loading ? '登录中...' : '立即登录' }}
          </el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
const apiVersion = '/v1'

export default {
  name: 'Index',
  layout: 'login',
  data() {
    return {
      loading: false,
      loginForm: {
        userName: '',
        password: '',
      },
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          {
            min: 1,
            max: 15,
            message: '长度在 4 到 10 个字符',
            trigger: 'blur',
          },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 6,
            max: 15,
            message: '长度在 8 到 15 个字符',
            trigger: 'blur',
          },
        ],
      },
    }
  },
  methods: {
    ...mapActions({
      login: 'auth/login',
    }),
    tryLogin() {
      // this.$refs['loginForm'].validate((valid) => {
      this.$refs.loginForm.validate((valid) => {
        if (!valid) {
          console.log('error submit!!')
          this.loading = false
          return
        }
        this.login({
          url: `${apiVersion}/auth/login`,
          username: this.loginForm.username,
          password: this.loginForm.password,
        }).then(() => this.$router.push('/home'))
        // this.$axios
        //   .$post(`${apiVersion}/auth/login`, {
        //     login_type: 'account',
        //     arguments: {
        //       username: this.loginForm.username,
        //       password: this.loginForm.password,
        //     },
        //   })
        //   .then((response) => {
        //     console.log(response.data.user)
        //     this.$router.push('/home')
        //   })
        //   .catch((error) => {
        //     console.log(error.response.data)
        //   })
      })
    },
  },
}
</script>

<style scoped>
.login-background {
  background-image: url('../../assets/钢铁侠.jpg');
  background-size: 100% 100%;
  position: fixed;
  height: 100%;
  width: 100%;
  z-index: -1;
}

.login-container {
  background-color: #000000;
  color: #333;
  text-align: center;
  line-height: 1;
  height: 33%;
  width: 33%;
  position: absolute;
  left: 33%;
  right: 33%;
  top: 33%;
  bottom: 33%;
  overflow: hidden;
}
</style>
