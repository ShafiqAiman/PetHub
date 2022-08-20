<template>
    <div class="container MyAccountPage">
        <div class="page">

              <div class="profilepicture" v-if="myprofile.get_profilephoto">
                <img :src="myprofile.get_profilephoto">
            </div>

            <div class="profilepicture" v-else>
                <img :src="defaultImage">
            </div>

            <div class="row">
                <div class="col-md-8 py-auto">

                    <div class="d-flex justify-content-between">
                        <div>
                            <h2 class="title">{{ myprofile.fullname }}</h2>
                            
                        </div>
                    </div>
                    <hr>

                    <div class="userInfo">
                        <div class="content">
                            <h3>About me</h3>
                            <p>{{ myprofile.aboutme }}</p>
                        </div>
                        <hr>

                        <div class="content">
                            <h3>Details</h3>
                            <table>
                                <tr>
                                    <td class="tdHeader">Gender</td>
                                    <td>{{ myprofile.gender }}</td>
                                </tr>
                                <tr>
                                    <td class="tdHeader">Age</td>
                                    <td>{{ myprofile.age }}</td>
                                </tr>
                                
                                <tr>
                                    <td class="tdHeader">Occupation</td>
                                    <td>{{ myprofile.occupation }}</td>
                                </tr>
                                
                                <tr>
                                    <td class="tdHeader">City Base</td>
                                    <td>{{myprofile.preferredcity}}</td>
                                </tr>
                            </table>
                            <hr>
                        </div>

                        <div class="content">
                            <h3>Contact info</h3>
                            <table>
                                <tr>
                                    <td class="tdHeader">Phone number</td>
                                    <td>{{ myprofile.phonenumber }}</td>
                                </tr>
                                <tr>
                                    <td class="tdHeader">Email</td>
                                    <td>{{ user.email }}</td>
                                </tr>
                            </table>
                            <hr>
                        </div>

                        <div class="content">
                            <h2>Linked profiles</h2>
                            <p>Link your social media accounts to your profile</p>
                            <table>
                                <tr>
                                    <td class="tdHeader">Instagram</td>
                                    <td>{{ myprofile.igAccount }}</td>
                                </tr>
                                <tr>
                                    <td class="tdHeader">Facebook</td>
                                    <td>{{ myprofile.fbAccount }}</td>
                                </tr>
                            </table>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 py-auto">
                    <router-link to="/myaccount/edit"><button class="editbtn">Edit</button></router-link>
                    
                </div>
            </div>

        </div>
    </div>
</template>

<script>

import axios from 'axios'
import defaultImage from '../assets/defaultprofilepicture.png'

export default {
    name: 'MyAccount',
    data(){
        return{
            user: {},
            myprofile:{},
            defaultImage:defaultImage,
        }

    },
    mounted(){
        document.title = 'PetHub | My Account' //Title of the page
        this.getUser()
    },
    methods:{
        async getUser(){
            // console.log(this.$store.state.token)
            this.$store.commit('setIsLoading', true)
            
            await axios 
                .get('/api/v1/users/me/', {
                headers: {
                        Authorization: "Token "+this.$store.state.token
                    }
                }) 
                .then(response => {
                    this.user = response.data

                    axios
                        .get(`/api/guardians/${this.user.id}/`)
                        .then(response => {
                            this.myprofile = response.data
                            
                        })
                        .catch(error => {
                            console.log(error)
                        })
                })
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)

                
        },
    }
}
</script>



<style scoped>
.MyAccountPage{
    min-height: 85vh;
    background-color: white;
    margin-top: 1%;
    margin-bottom: 1%;
}

.page{
    padding: 3%;
}

.fullname{
    margin-top: 3%;
    text-align: center;
}

.profilepicture{
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    background: #e6e6e6;

}
.profilepicture img {
    flex-shrink: 0;
    width: 300px;
    height: 300px;
    object-fit: cover;
}

.row{
    padding: 20px;
    box-shadow: none;
}

hr{
    width: 90%;
}
.container{
    background-color: white;
    padding-top: 20px;
}

.content{
    padding: 20px 0px;
}

.leftcolumn{
    float: left;
    width: 65%;
    padding: 1% 0 0;
}

.rightcolumn{
    float: right;
    width: 35%;
    padding-left: 20px;
}

.styles_userInfo_1{
    display: inline-block;
    border: 1px solid #e8e9ea;
    border-radius: 30px;
    padding: 0.5rem 0.75rem;
    margin-bottom: 0.75rem;
    margin-left: 0;
}

.styles_userInfo_icon{
    line-height: 1.5em;
    display: block;
    float: left;
    margin-right: 0.5rem;
}

.userInfo_content{
    margin-right: 0.25rem;
    line-height: 1.375rem;
    font-size: 1rem;
    color: #2e3a4b;
}

.iconpic{
    text-align: center;
}

.icon{
    width: 30px;
    height: 30px;
    margin-right: 10px;
}

.invitebutton{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 0px;
}

.my-button{
    width: 50%;
    float: right;
    color: white;
    background-color: #DB4914;
    opacity:0.8;
}

h3{
    font-size: 20px;
    color: #2e3a4b;
}

p{
    font-size: 16px;
    color: #2e3a4b;
}

td{
    padding: 0px 40px 10px 0px;
    color: #2e3a4b
}

.tdHeader{
    color: #6d7580;
}

.card{
    text-align: center;
    background-color: #FCFEFD;
    padding: 10px;
    margin: 20px;
    margin-left: 0px;
    border-radius: 5%;
}

.editbtn{
    color: white;
    margin-top: 10px;
    background-color:#DB4914;
    height: 50px;
    width: 70%;
    border: 1px solid #DB4914;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 5px;
    display: block;
    margin: 0 auto;
}

.fa {
    padding: 20px;
    font-size: 30px;
    width: 30px;
    text-align: center;
    text-decoration: none;
    margin: 5px 2px;
    border-radius: 50%;
}

.fa:hover {
    opacity: 0.7;
}

.fa-facebook {
    background: #3B5998;
    color: white;
}
</style>