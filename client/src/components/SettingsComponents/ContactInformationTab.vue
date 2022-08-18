<template>
    <div class="ContactInfoTab">
        <br>
        <h2>Contact Information</h2>
        <br>
        <label><b>Email</b></label>
        <br>
            <input type="email" placeholder="" v-model="newEmail">
            <br>
            <button @click="reviewEmail(newEmail)">
                Update Email
            </button>
        <br>
        <br>
        <br>
            <label><b>Contact Number</b></label>
        <br>
            <input type="" v-model="newContactNumber">
            <br>
            <button @click="reviewNumber(newContactNumber)">
                Update Contact Number
            </button>
    </div>
</template>

<script>
export default {
    name:'ContactInformationTab',
    data()
    {
        return{
            Email:'ahmadarifhazman@gmail.com',
            newEmail:'',
            contactNumber:'0172318894',
            newContactNumber:'',
        }
    },

    methods:
    {
        reviewEmail(newEmail)
        {
            if( this.newEmail!==this.Email)
            {
                alert("Email Approved");
                this.Email=this.newEmail;
            }
            else
            {
                alert("Email cannot be the same as before!")
            }
        },

        reviewNumber(newContactNumber)
        {
            if(this.newContactNumber!==this.contactNumber)
            {
                alert("Contact Number Approved");
                this.contactNumber=this.newContactNumber;
            }
            else
            {
                alert("Contact number cannot be the same as before!")
            }
        }
    }
}
</script>

<style scoped>
.ContactInfoTab
{
    display: block;
    margin: 0 auto;
    margin-top: 10px;
    background-color: rgb(255, 255, 255);
    width:50%;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
label
{
    font-size: 20px;
}
input
{
    padding: 10px;
    font-size: 15px;
    width: 300px;
    border-radius: 5px;
    border-width: 0.2px;
}

button
{
        margin-top: 20px;
        padding: 9px;
        border: none;
        width: 300px;
        margin-bottom: 10px;
        border-radius: 5px;
        background-color: rgb(164, 217, 250);
}

button:hover
{
    color: white;
}
</style>