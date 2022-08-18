<template>
    <div class="forgotpasswordpage">
        <div class="container">
            <div class="forgotpasswordform">
                <form @submit.prevent="submitForm">
                    <h2>Find Your PetHub Account</h2>
                    <div class="form-group">
                        <label for="exampleInputEmail1">Please enter your email address to search for your account.</label>
                        <input type="email" class="form-control" v-model="email" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Email Address">
                    </div>
                    <button type="submit" class="btn btn-primary text-light">Search</button>
                </form>
            </div>
            
        </div>
    </div>

</template>

<script>
import axios from 'axios'


export default{
    name: 'ForgotPassword',
    data(){
        return{
            email:''
            // christianoronaldo@test.com
        }
    },
    methods:{
        submitForm(){
            console.log(this.email)

            let formData=new FormData();

            formData.append('email', this.email);

            axios
                .post('/api/v1/users/reset_password/', formData)
                .then(response => {
                    alert("Reset link is sent to your email!")
                    this.$router.push('/')
                })
                
                .catch(error => {
                    alert("ERROR!!!")
                    console.log(error)
                })
        }
    }
}
</script>

<style scoped>

.forgotpasswordpage{
    position: relative;
	min-height: 85vh;
	background-color: #fff;
}

.forgotpasswordform{
    margin: 0 auto;
    margin-top: 5%;
    width: 60%;
}

</style>