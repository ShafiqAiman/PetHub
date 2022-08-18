<template>
<div>
<div>
    <div class="PasswordChangingTab">
        <br>
        <h2>Change Password</h2>
        <p style="font-size: 13px">You can change your password only once a month.<br>Password must consist of: </p>
        <ul style="text-align: center; list-style: inside;">
            <li style="font-size: 13px">
                8 CHARACTERS.
            </li>
            <li style="font-size: 13px">
                at least ONE uppercase.
            </li>
        </ul>
        <b>Initial Password :</b>
        <input v-model="CurrentPassword" placeholder="" type="password" style="margin-left: 10px"><br>
        <br>
        <b>New Password :</b>
        <input v-model="NewPassword" placeholder="" type="password" style="margin-left: 18px"><br><br>
        <button id="confirmButton" @click="checkInitialPassword(CurrentPassword, NewPassword)">Confirm Password</button>
    </div>

    </div>
</div>
    
</template>

<script>
import axios from 'axios';
import Toast from '../Toast.vue'
export default {
    name:'PasswordTab',

components:
{
    Toast,
},


data()
{
    return{
        NewPasswordInput:null,

        CurrentPassword:null,
        NewPassword:null,

        NewPass:'',
        NewPassLength:0,
        containsEightCharacters:false,
        containsUpperCase:false,
        initialPasswordApproved:false,
        newPasswordApproved:false,
        passwordLength:0,
        noticeHeader:'Password Management',
    }
},

methods:
    {
        
        checkInitialPassword(CurrentPassword, NewPassword)
        {
            console.log("Current Password= "+CurrentPassword);
            console.log("New Password= "+NewPassword);

            let formData =new FormData();

            formData.append('current_password', CurrentPassword)
            formData.append('new_password', NewPassword)


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
                    alert("Your password is changed!");
                    

                })
                .catch(err=>{
                    alert(err);
                    this.CurrentPassword= null;
                    this.NewPassword= null;
                })

                

            

        },

}
}

</script>

<style scoped>
.PasswordChangingTab
{
    display: block;
    margin: 0 auto;
    margin-top: 10px;
    background-color: rgb(255, 255, 255);
    width:50%;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

#confirmButton
{
      margin-top: 20px;
        padding: 9px;
        border: none;
        width: 300px;
        margin-bottom: 10px;
        border-radius: 5px;
        background-color: rgb(170, 217, 247);
}

input
{
    border-width: 0.5px;
    border-radius: 5px;
}

button:hover
{
    background-color: rgb(187, 221, 241);
    color: white;
}

</style>