<template>
    <div class="deleteSection">
        <br>
        <p>If you delete your account, all the account settings, personal information, listings, messages will be removed from our site.</p>
        <button @click="deleteAccount()" id="deleteButton"><b>Deactivate Account</b></button>
    </div>
</template>

<script>
export default {
    name:'DeleteAcc',

    methods: 
    {
        deleteAccount()
        {
            alert("Account Deleted");
            this.$router.push({path: '/'});        }
    },

}

</script>

<style scoped>
    #deleteButton
    {
        font-size: 13px;
        padding: 15px;
        border: none;
        margin-bottom: 10px;
        border-radius: 5px;
        background-color: rgb(250, 95, 95);
    }

    .deleteSection
    {
         display: block;
    margin: 0 auto;
    margin-top: 10px;
    background-color: rgb(255, 255, 255);
    width:50%;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

    
</style>