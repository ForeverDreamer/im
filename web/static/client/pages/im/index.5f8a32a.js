(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{385:function(t,n,e){"use strict";e.r(n);var o={name:"Index",data:function(){return{socket:null,current_msg:"",received_msg_arr:[],username:"",accountLoginInfo:{username:"",password:""}}},computed:{received_msgs:function(){return this.received_msg_arr.map((function(t){return t.msg})).join("\n")}},mounted:function(){this.init_data()},methods:{init_data:function(){var t=this;this.socket=this.$socketIo("http://127.0.0.1:5000/events",{}),this.socket.on("connect",(function(){console.log("连接")})),this.socket.on("disconnect",(function(){console.log("断开连接, 请登录后操作")})),this.socket.on("data",(function(n,e){t.received_msg_arr.push(n),e&&e()})),this.socket.on("error",(function(t){console.log(t.code),console.log(t.msg)}))},sendMsg:function(){this.current_msg&&(this.socket.emit("data",this.current_msg),this.current_msg="")},enterLobby:function(){this.socket.emit("join_room",{username:"阿升"+Math.random(),room:"lobby"}),console.log("进入大厅")},accountLogin:function(){var t=this;this.$axios.$post("".concat("/v1","/auth/account_login"),{username:this.accountLoginInfo.username,password:this.accountLoginInfo.password}).then((function(n){console.log(n.data),t.username=n.data.username})).catch((function(t){console.log(t.response.data)}))},logout:function(){var t=this;this.$axios.$delete("".concat("/v1","/auth/account_login")).then((function(n){console.log(n.data),t.username=""})).catch((function(t){console.log(t.response.data)}))}}},c=e(48),component=Object(c.a)(o,(function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("div",{staticClass:"container mt-3"},[e("h1",{staticClass:"text-center",staticStyle:{color:"blue"}},[t._v("\n    欢迎使用中经网即时通信软件\n  ")]),t._v(" "),e("div",{staticClass:"mb-3"},[e("p",{staticClass:"text-success",class:t.username?"text-success":"text-danger"},[t._v("\n      "+t._s(t.username?t.username+"已登录":"请登录后操作")+"\n    ")])]),t._v(" "),e("div",{staticClass:"border d-flex p-3 mb-3"},[e("div",{staticClass:"w-100"},[e("el-input",{staticClass:"mb-3 w-50",attrs:{placeholder:"请输入要发送的消息",size:"medium"},model:{value:t.current_msg,callback:function(n){t.current_msg=n},expression:"current_msg"}}),t._v(" "),e("div",{staticClass:"text-center"},[e("el-button",{staticClass:"w-10 ml-3",attrs:{type:"primary"},on:{click:t.sendMsg}},[t._v("\n          发送消息\n        ")]),t._v(" "),e("el-button",{staticClass:"w-10 ml-3",attrs:{type:"primary"},on:{click:t.enterLobby}},[t._v("\n          进入大厅\n        ")])],1),t._v(" "),e("el-input",{staticClass:"w-50 mt-3",attrs:{type:"textarea",autosize:{minRows:10},placeholder:"还没有消息"},model:{value:t.received_msgs,callback:function(n){t.received_msgs=n},expression:"received_msgs"}})],1)]),t._v(" "),e("h3",{staticClass:"text-center mt-3"},[t._v("登录(/v1/auth/login)")]),t._v(" "),e("div",{staticClass:"border p-3"},[e("el-button",{staticClass:"w-10 ml-5",attrs:{type:"primary"},on:{click:t.accountLogin}},[t._v("\n      账号登录\n    ")]),t._v(" "),e("el-input",{staticClass:"w-25 ml-3",attrs:{placeholder:"用户名"},model:{value:t.accountLoginInfo.username,callback:function(n){t.$set(t.accountLoginInfo,"username",n)},expression:"accountLoginInfo.username"}}),t._v(" "),e("el-input",{staticClass:"w-25 ml-3",attrs:{placeholder:"密码"},model:{value:t.accountLoginInfo.password,callback:function(n){t.$set(t.accountLoginInfo,"password",n)},expression:"accountLoginInfo.password"}}),t._v(" "),e("el-button",{staticClass:"w-10 ml-5",attrs:{type:"primary"},on:{click:t.logout}},[t._v("\n      退出登录\n    ")])],1)])}),[],!1,null,"3bb4ce99",null);n.default=component.exports}}]);