<template>
    <div class="signinpage">
    <div class="container" id="container">
        <div class="form-container sign-in-container d-flex align-items-center">
            <form  @submit.prevent="submitForm" action="#">
                <h1 class="title">Login to continue</h1>
                <input type="text" placeholder="Username" v-model="username" required/>
                <input type="password" placeholder="Password" v-model="password" required/>
                <p><span>Forgot your password? </span><router-link to="/forgotpassword" class="links">Click here</router-link></p>
                <button>Log In</button>
                
				<!-- <div class="notification is-danger" style="background:red;" v-show="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
                <div class="social-container">
                    <p class="altmethods">or login using</p>
                    <a href="#" class="fa fa-google"></a>
                    <a href="#" class="fa fa-facebook"></a>
                    <a href="#" class="fa fa-twitter"></a>
                </div> -->
                <p><span>Don't have an account? </span><router-link to="/signup" class="links">Create one!</router-link></p>
            </form> 
        </div>
        <div class="overlay-container">
            <div class="overlay">
                <div class="overlay-panel overlay-right">
                    <img class="logo" src="../assets/pethub.png" id="logo" alt="Roomah-Logo">
                    <h3>PetHub</h3>
                    <p class="desc">The first Pet Social Media in the World!</p>
                </div>
            </div>
        </div>
    </div>
</div>

</template>

<script>
import axios from 'axios'
export default {
    name: 'SignIn',
	data(){
		return{
			username: '',
			password: '',
			errors:[],
			user:null
		}
	},
	mounted(){
		document.title = 'Bed & Buddies | Sign In'
	},
	methods:{
		async submitForm(){
			axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")

			const formData = {
                username: this.username,
                password: this.password
            }

			await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    // const toPath = this.$route.query.to || '/cart'

					axios 
						.get('/api/v1/users/me/', {
							headers: {
							Authorization: "Token "+ token
						},
						}) 
						.then(response => {
						this.user = response.data
						
						axios
							.get(`/djangohousemates/${this.user.id}/`)
							.then(response =>{
								let profile = response.data

								if(profile.gender !== '-' || profile.occupation !== '-' || profile.orientation !== '-' || profile.religion !== '-' || profile.pet !== '-'){
									this.$router.push('/')
									// this.$router.go(-1);
								}else{
									// this.$router.push('/profilesetup')
									window.location = "http://localhost:8080/profilesetup"
								}

							})

						
						})
						.catch(error => {
						console.log(error)
						})

                    // this.$router.push('/')
					
                })
                .catch(error => {
                    if (error.response) {
						this.errors = []
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }

					alert(this.errors)
                })
		}
	}
}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css?family=Montserrat:400,800');

* {
	box-sizing: border-box;
}

html, body {
	justify-content: center;
	align-items: center;
	flex-direction: column;
	font-family: 'Montserrat', sans-serif;
	/* margin: -20px 0 50px; */
	height: 100%;
	
} 

.logo{
    border-radius: 50%;
    object-fit: cover;
  }

.signinpage{
    position: relative;
	min-height: 85vh;
	background-color: #fff;
}

h1.title {
	margin-top: 5rem;
	font-size: 20px;
	left:0%;
}

h2 {
	text-align: center;
}

h3{
	color: black;
}

p {
	font-size: 14px;
	font-weight: 100;
	line-height: 20px;
	margin: 10px 30px;
}

p.altmethods {
	margin:5px;
	font-size: 12px;
}

p.desc {
	color: black;
}

span {
	font-size: 12px;
}

a {
	color: #333;
	font-size: 12px;
	text-decoration: none;
	margin: 5px 0;
}

a:hover{
	text-decoration: none;


}
button {
	border-radius: 20px;
	border: 1px solid #DB4914;
	background-color: #DB4914;
	color: #FFFFFF;
	font-size:70%;
	font-weight: bold;
	padding: 0.75vw 1.6px;
	margin:0.7rem;
	letter-spacing: 1px;
	text-transform: uppercase;
	width: 60%;
}

button:active {
	transform: scale(0.95);
}

button:focus {
	outline: none;
}

button.ghost {
	background-color: transparent;
	border-color: #FFFFFF;
}

form {
	background-color: #FFFFFF;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 50px 10%;
	height: 100%;
	text-align: center;
	width:100%;
}

input {
	font-size:15px;
	background-color: #eee;
	border: none;
	padding: 12px 15px;
	margin: 5px 0;
	width: 100%;
}

.container {
    margin-top: 7%;
    margin-bottom: 7%;
	background-color: white;
	border-radius: 10px;
	box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
			0 10px 10px rgba(0,0,0,0.22);
	position: relative;
	overflow: hidden;
	width: 768px;
	max-width: 100%;
	min-height: 480px;
	max-height: 100%;
}

.form-container {
	position: absolute;
	top: 0;
	height: 100%;
}

.sign-in-container {
	left: 50%;
	width: 50%;
	z-index: 2;
}

@media only screen and (max-width: 760px) {
	.container{
	width:368px;
	}

.overlay-container{
	display: none;
}
.form-container.sign-in-container  {
	left:0%;
		width:100%;
		position: relative;
	}
}

.overlay-container {
	position: absolute;
	top: 0;
	left: 0%;
	width: 50%;
	height: 100%;
	overflow: hidden;
	transition: transform 0.6s ease-in-out;
	z-index: 100;
}

.overlay {
	background-color: lightgray;

	background-repeat: no-repeat;
	background-size: cover;
	background-position: 0 0;
	color: #FFFFFF;
	position: relative;
	left: -100%;
	height: 100%;
	width: 200%;
	transform: translateX(0);
}

.overlay-panel {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	padding: 0 40px;
	text-align: center;
	top: 0;
	height: 100%;
	width: 50%;
	transform: translateX(0);
	transition: transform 0.6s ease-in-out;
}

.overlay-left {
	transform: translateX(-20%);
}

.container.right-panel-active .overlay-left {
	transform: translateX(0);
}

.overlay-right {
	right: 0;
	transform: translateX(0);
}

.container.right-panel-active .overlay-right {
	transform: translateX(20%);
}

.social-container{
	margin: 15px 0px;
	border-top: 1px solid rgb(182, 180, 180);
}

.social-container a {
	
	border-radius: 50%;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	margin: 0 10px;
	height: 40px;
	width: 40px;
	box-shadow: 1px 1px 3px black;
} 

	.fa{
	padding: 10px;
	font-size: 20px;
	width: 1.7em;
	text-align: center;
	text-decoration: none;
	margin: 25px;
	border-radius: 50%;
	}

	.fa:hover {
		opacity: 0.7;
	}

	.fa-google {
	background: #dd4b39;
	color: white;
	}

	.fa-facebook {
	background: #3B5998;
	color: white;
	}

	.fa-twitter {
	background: #55ACEE;
	color: white;
	}

	.links{
		color:#03B3E1;
		display: inline-block;
		margin:0;
	}

	footer {
		background-color: #222;
		color: #fff;
		font-size: 14px;
		bottom: 0;
		position: fixed;
		left: 0;
		right: 0;
		text-align: center;
		z-index: 999;
	}

	footer p {
		margin: 10px 0;
	}

	footer i {
		color: red;
	}

	footer a {
		color: #3c97bf;
		text-decoration: none;
	}

	#logo{
		width:40%;	
	}


</style>