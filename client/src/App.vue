<template>
  <div id="app">
    <template v-if="$store.state.isAuthenticated">
      <Nav />
    </template>

    <template v-else>
      <VisitorNav />
    </template>

    <div class="is-loading-bar text-center" v-bind:class="{'is-loading': $store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>
      
    <div class="auth-wrapper">
      <!-- nesjkfhes -->
      <router-view />
    </div>
    <Footer />
  </div>
</template>

<script>
import Nav from './components/Nav.vue'
import VisitorNav from './components/VisitorNav.vue'
import Footer from './components/Footer.vue'
import axios from 'axios'

export default {
    name: 'App',
    components:{
        Nav, 
        VisitorNav,
        Footer
    },
    beforeCreate(){
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if(token){
        axios.defaults.headers.common['Authorization'] = "Token" + token
      }else{
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  
}
</script>

<style>
  #app{
    position: relative;
	  /* min-height: 100vh; */
  }
  
  body{

    /* background: url("./assets/Buildings.jpg")0 -350px;  */
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    background-size: cover;

    /* background-color: #fff; */
    /* background-color: rgb(235, 233, 233); */



  }

  /* h3{
    text-align: center;
  } */

  .navbar{
    background-color:#DB4914;
    
  }

  *
		{
			padding: 0;
			margin: 0;
			box-sizing: border-box;
		}


	/* .row
		{
			background: white;
			box-shadow: 12px 12px 22px grey;
		} */
		
	.btn
		{
			border: none;
			outline: none;
			height : 50px;
			width: 100%;
			background-color:#DB4914;
			color: black;
			border-radius: 4px;
			font-weight : bold;
		}
		
	.btn:hover
		{
			background-color: white;
			border: 2px solid;
			color: #424242;
		}
		
	

  .auth-wrapper{
    display: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
    

  }

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}

.is-loading-bar.is-loading{
    height: 80px;
  }

</style>