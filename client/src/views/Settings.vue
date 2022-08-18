<template>
<div class="container SettingsPage">
            <div class="row">
                <div class="col-md-4 mb-5">
                    <div class="list-group" id="list-tab" role="tablist">
                        <a class="list-group-item list-group-item-action active" id="list-security-list" data-toggle="list" href="#list-security" role="tab" aria-controls="security">Security</a>
                        <a class="list-group-item list-group-item-action disabled" id="list-notification-list" data-toggle="list" href="#list-notification" role="tab" aria-controls="notification" disabled>Notification</a>
                        <a class="list-group-item list-group-item-action disabled" id="list-myvouchers-list" data-toggle="list" href="#list-myvouchers" role="tab" aria-controls="myvouchers">My Vouchers</a>
                        <a class="list-group-item list-group-item-action" id="list-deactivate-list" data-toggle="list" href="#list-deactivate" role="tab" aria-controls="deactivate">Deactivate Account</a>
                    </div>
                </div>
                <div class="col-md-8">
                    <div class="tab-content" id="nav-tabContent">
                    <div class="tab-pane fade show active" id="list-security" role="tabpanel" aria-labelledby="list-security-list">
                        <div class="passwordChange" id="passwordmanagement">
                            <div class="titleDescription">
                                <h3>
                                    Change Password
                                </h3>
                                <p>
                                    This password is used to log into your account.
                                </p>
                            </div>
                            <div class="contents">
                                <form @submit.prevent="changePassword">
                                    <h6>
                                        Enter Current Password
                                    </h6>
                                    <input class="form-control" type="password" v-model="CurrentPassword" required><br>
                                    <h6>
                                        Enter New Password
                                    </h6>
                                    <input class="form-control" type="password" v-model="NewPassword" required>
                                    <button class="confirmButton" type="submit">Submit</button>
                                </form>
                                
                            </div>
                        </div>

                        <!-- <div class="emailChange" id="emailmanagement">
                            <div class="titleDescription">
                                <h3>
                                    Change Email
                                </h3>
                                <p>
                                    This email is used to log into your account or receive emails from us.
                                </p>
                            </div>
                            <div class="contents">
                                <form @submit.prevent="changeEmail">
                                    <h6>
                                        Enter New Email
                                    </h6>
                                    <input class="form-control" type="email" v-model="newEmail" required>
                                    <button class="confirmButton">Submit</button>
                                </form>
                            </div>
                        </div> -->

                        <div class="usernameChange" id="usernamemanagement">
                            <div class="titleDescription">
                                <h3>
                                    Change Username
                                </h3>
                                <p>
                                    This username is used to log into your account.
                                </p>
                            </div>
                            <div class="contents">
                                <form @submit.prevent="changeUsername">
                                    <h6>
                                        Enter New Username
                                    </h6>
                                    <input class="form-control" type="username" v-model="newUsername" required>
                                    <button class="confirmButton">Submit</button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="list-notification" role="tabpanel" aria-labelledby="list-notification-list">Notification</div>
                    <div class="tab-pane fade" id="list-myvouchers" role="tabpanel" aria-labelledby="list-myvouchers-list">My Vouchers</div>
                    <div class="tab-pane fade" id="list-deactivate" role="tabpanel" aria-labelledby="list-deactivate-list">
                        <div class="usernameChange" id="usernamemanagement">
                            <div class="titleDescription">
                                <h3>
                                    Deactivate Account
                                </h3>
                                <p>
                                    This survey is conducted to improve the website
                                </p>
                            </div>
                            <div class="contents">
                                <form @submit.prevent="deactivateAccount">
                                    <h6>
                                        Your Reason to Deactivate
                                    </h6>
                                    
                                    <input type="radio" id="reason1" value="Just need a break" v-model="deactivatereason" />
                                    <label for="reason1">Just need a break</label><br>

                                    <input type="radio" id="reason2" value="Too busy/distracting" v-model="deactivatereason" />
                                    <label for="reason2">Too busy/distracting</label><br>

                                    <input type="radio" id="reason3" value="Concerned about my data" v-model="deactivatereason" />
                                    <label for="reason3">Concerned about my data</label><br>

                                    <input type="radio" id="reason4" value="Too many ads" v-model="deactivatereason" />
                                    <label for="reason4">Too many ads</label><br>

                                    <input type="radio" id="reason5" value="Privacy concerns" v-model="deactivatereason" />
                                    <label for="reason5">Privacy concerns</label><br>

                                    <input type="radio" id="reason6" value="Trouble getting started" v-model="deactivatereason" />
                                    <label for="reason6">Trouble getting started</label><br>

                                    <input type="radio" id="reason7" value="Others" v-model="deactivatereason" />
                                    <label for="reason7">Others</label>
                                    <button class="confirmButton">Submit</button>
                                </form>
                                
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
    </div>
</template>


<script>
import axios from 'axios';

export default 
{
    name:'Settings',

    data()
    {
        return{
            CurrentPassword:null,
            NewPassword:null,
            email:'',
            newEmail:'',
            newUsername:'',
            user:null,
            deactivatereason:''
        }
    },mounted(){
      document.title = 'Bed & Buddies | Settings' //Title of the page
      this.getUser()
    },
    methods:{
        getUser(){
            // console.log(this.$store.state.token)
            axios 
                .get('/api/v1/users/me/', {
                    headers: {
                    Authorization: "Token "+this.$store.state.token
                },
                }) 
                .then(response => {
                    this.user = response.data
                })
                .catch(error => {
                    console.log(error)
                })

                
        },
        changePassword()
        {

            let formData =new FormData();

            formData.append('current_password', this.CurrentPassword)
            formData.append('new_password', this.NewPassword)


            axios
                .post('/api/v1/users/set_password/',formData,
                {
                    headers: {
                    Authorization: "Token "+this.$store.state.token
                    }
                }
                
                )
                
                .then(response =>{
                    this.CurrentPassword= null;
                    this.NewPassword= null;
                    window.confirm("Your password is changed!");
                    

                })
                .catch(err=>{
                    alert(err);
                    this.CurrentPassword= null;
                    this.NewPassword= null;
                })


        },
        changeEmail(){

            //login credentials should be entered first for security purposes
            

            let Username = this.user.username
            let Password = prompt("Please enter your password to proceed:")
            const formData = {
                username: Username,
                password: Password
            }

            axios
                .post("/api/v1/token/login/", formData)
                .then(response=>{
                    axios
                        .patch("/api/v1/users/me/", {email:this.newEmail}, {
                        headers: {
                                Authorization: "Token "+this.$store.state.token
                            }
                        })
                        .then(response =>{
                            this.newEmail='';
                            window.confirm("Your email is changed!");
                        })
                        .catch(error => { 
                            console.log(error)
                        })
                })
                .catch(error => { 
                    alert(error)
                })
        },
        changeUsername(){

            let Password = prompt("Please enter your password to proceed:")

            const usernameParams = {
                'new_username': this.newUsername,
                'current_password' : Password
            }

            axios
                .post('/api/v1/users/set_username/',usernameParams,
                {
                    headers: {
                    Authorization: "Token "+this.$store.state.token
                    }
                }
                
                )
                
                .then(response =>{
                    this.newUsername= null;
                    window.confirm("Your username is changed!");
                    

                })
                .catch(err=>{
                    alert(err);
                    this.CurrentPassword= null;
                    this.NewPassword= null;
                })


        },
        deactivateAccount(){
            // console.log(this.deactivatereason)
            
            const config = {
                headers: {
                    Authorization: "Token "+this.$store.state.token
                }
            }
            
            let Password = prompt("Please enter your password to proceed:")

            console.log(config)

            axios
                .delete("/api/v1/users/me/", {data:{current_password: Password}, config})
                .then(response =>{
                    this.$store.commit('removeToken')
                    this.$router.push('/')
                    window.confirm("Your Account Deactivation is Successful!");
                })
                .catch(error => { 
                    alert(error)
                })
        }
    }
}
</script>

<style scoped>

.SettingsPage{
    min-height: 85vh;
    background-color: white;
    margin-top: 5%;
    margin-bottom: 1%;
}

.PersonalInfo
{
    margin-bottom:5%;
    margin-top:5%;
}

.leftColumn
{
    border-radius: 5%;
    background-color: rgba(113, 133, 66, 0);
    float:left;
    position: fixed;
    /* box-shadow: 2px 2px 2px grey;  */
    /* width: 50%;  */
}
 .rightColumn
{
    float:right;
    margin-left:30%;
    /* border-radius: 5%; */
    background-color: rgba(240, 224, 83, 0);
    width: 50%;
    
 }  
ul
{
    list-style: none;
}
button
{
    margin-top: 5%;
    border: none;
    background-color: rgba(211, 49, 49, 0);
}
button:active
{
    background-color: lightgray
}

.contents
{
    flex:50%;
    background-color: rgb(192, 190, 184);
    width:50%;
    padding:5%;
}

.titleDescription
{
    flex:50%;
    background-color: rgb(231, 229, 229);
    width:50%;
    padding:5%;
}

.passwordChange, .emailChange, .usernameChange
{
    display:flex;
    margin-bottom:10%;
    box-shadow: 2px 2px 2px grey;
    width:100%;
    position:relative;
}

.confirmButton
{
    
    background-color:#fbd864;
    height: 50px;
    width: 100px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 5px;
    display: block;
    margin: 0 auto;
    margin-top: 5%;
}



</style>