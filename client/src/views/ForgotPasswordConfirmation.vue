<template>
    <div class="wholepage">
        <div class="container">
            <div class="FormPage">
            <form @submit.prevent="submitForm">
                <h1>Reset Password</h1>
                <div class="form-group">
                    <label for="exampleInputPassword1">New Password</label>
                    <input type="password" v-model="newpassword" class="form-control" id="exampleInputPassword1" placeholder="Password">
                </div>
                <div class="form-group">
                    <label for="exampleInputPassword2">Confirm Password</label>
                    <input type="password" v-model="confirmpassword" class="form-control" id="exampleInputPassword2" placeholder="Confirm Password">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
            
        </div>

        </div>
        

    </div>
</template>

<script>

import axios from 'axios'
export default{
    name: 'ForgotPasswordConfirmation',
    data(){
        return{
            uid:'',
            token:'',
            newpassword:'',
            confirmpassword:''
        }
    },
    mounted(){
        document.title = 'PetHub | Reset Password'
        this.getURL()
    },
    methods:{
        getURL(){
            let url = window.location.href.toString()
            // console.log(url)
            let index = url.indexOf("reset_password")
            // console.log(index)
                
            let indextoken = url.lastIndexOf("/")
            // console.log(indextoken)

            this.uid = url.substring(index+15, indextoken)
            this.token = url.substring(indextoken+1,)

            // console.log(this.uid)
            // console.log(this.token)
        },
        submitForm(){
            console.log(this.newpassword)

            let formData=new FormData();

            formData.append('uid', this.uid);
            formData.append('token', this.token);
            formData.append('new_password', this.newpassword);
            formData.append('re_new_password', this.confirmpassword);

            axios
                .post('/api/v1/users/reset_password_confirm/', formData)
                .then(response => {
                    alert("New Password is Set!")
                    this.$router.push('/')
                })
                .catch(error => {
                    alert("Error happens. Please check your passwords again.")
                    console.log(error)
            })
        }
    }
    }
</script>

<style scoped>
.wholepage{
    position: relative;
	min-height: 85vh;
	background-color: #fff; 
    
}

.FormPage{
    margin: 0 auto;
    margin-top: 5%;
    width: 60%;
}
</style>