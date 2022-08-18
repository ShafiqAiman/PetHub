<template>
    <div class="container useractivationpage">
        <div id="successfulcontent">
            <img src="../assets/tickactivation.png" class="successfulicon" alt="">
            <h1>Your account has successfully activated!</h1>
            <p>You can sign in to your account to start finding your potential buddies or place to stay!</p>
            <router-link to="/signin"><button class="signinbtn">Sign In</button></router-link>
        </div>

        <div id="failcontent">
            <img src="../assets/failactivation.jpeg" class="successfulicon" alt="">
            <h1>Your account activation is failed!</h1>
            <p>We are sorry to hear that your account activation is failed. Please try again by refreshing this page or contact our support team.</p>
            <router-link to="/help"><button class="signinbtn">Contact Support</button></router-link>
        </div>
        
    </div>
</template>

<script>
    import axios from 'axios'

export default {
    name: 'UserActivation',
	data(){
		return{
			uid:'',
            token:'',
		}
	},
    mounted(){
        document.title = 'Bed & Buddies | User Activation'
        this.getURL()
    },
    methods:{
        getURL(){
            let url = window.location.href.toString()
            // console.log(url)
            let index = url.indexOf("activate")
            // console.log(index)
                
            let indextoken = url.lastIndexOf("/")
            // console.log(indextoken)

            this.uid = url.substring(index+9, indextoken)
            this.token = url.substring(indextoken+1,)

            console.log(this.uid)
            console.log(this.token)

            let formData=new FormData();

            formData.append('uid', this.uid);
            formData.append('token', this.token);

            axios
                .post('/api/v1/users/activation/', formData)
                .then(response => {
                    let x = document.getElementById("successfulcontent");
                    x.style.display = "block"
                })
                .catch(error => {
                    let x = document.getElementById("failcontent");
                    x.style.display = "block"
                    console.log(error)
            })

            // http://localhost:8080/activate/OA/b7ko87-7e40e9337557b421a129660d21f5d414
        },
    }
}
</script>

<style scoped>
    .useractivationpage{
        margin-top: 5%;
        margin-bottom: 1%;
        min-height: 85vh;
        background-color: #fff;
    }
    #successfulcontent{
        text-align: center;
        display: none;
    }

    #failcontent{
        text-align: center;
        display: none;
    }
   .signinbtn{
        background-color:#DB4914;
        color: white;
        height: 50px;
        width: 200px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-sizing: border-box;
        padding: 5px;
        display: block;
        margin: 0 auto;
   }

   .successfulicon{
    height: 10%;
    width:10%;
   }
</style>