<template>
    <div class='div' id='wholePage'>
        <div class="HousematePage container">
            <!-- <div>
                <div>
                    <template v-if="housemate.get_profilephoto==''">
                        <img src="../assets/defaultprofilepicture.png">
                    </template>
                    <template v-else>
                        <img :src="housemate.get_profilephoto">
                    </template>
                    
                    <h1 class="title">{{ housemate.fullname }}</h1>
                    <p>{{ housemate.bio }}</p>
                </div>
            </div> -->
            <div class="header">
                
                <template v-if="housemate.get_profilephoto==''">
                    <img src="../assets/defaultprofilepicture.png" class="profilephoto">
                </template>
                <template v-else>
                    <img :src="housemate.get_profilephoto" class="profilephoto">
                </template>
            </div>

            <div class="row">
                <div class="col-md-8 py-auto">

                    <div class="d-flex justify-content-between">
                        <div>
                            <h2 class="title">{{ housemate.fullname }}</h2>
                            <h4 class="title"><mark>{{ housemate.HasPet }}</mark></h4>
                            
                            <p>{{ housemate.gender }}, {{ housemate.age }}</p>
                        </div>
                    </div>
                    <hr>

                    <div class="userInfo">
                        <div class="content">
                            <h3>About me</h3>
                            <p>{{ housemate.aboutme }}</p>
                            
                        </div>
                         <hr>
                    </div>

                    <div class="searchPreferences">
                        <div class="content">
                            <h3>More info</h3>
                            <table>
                                <tr>
                                    <td class="tdHeader">Occupation</td>
                                    <td>{{housemate.occupation}}</td>
                                </tr>

                                <tr>
                                    <td class="tdHeader">City Base</td>
                                    <td>{{housemate.preferredcity}}</td>
                                </tr>
                            </table>
                            <br>
                            <div id="map-div"></div>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 py-auto">
                    
                    <div class="card">
                        <h3>{{ housemate.fullname }}'s contact info</h3>
                        <div class="card-body">
                            <div class="mb-3">
                                <img class="mr-2" :src="phonenumber" width="20" height="20" alt="">
                                <span>{{ housemate.phonenumber }}</span>
                            </div>
                            <template v-if="housemate.igAccount!=='-' || housemate.fbAccount!=='-'">
                                <h6 class="card-title">Linked social media</h6>
                                <template v-if="housemate.igAccount!=='-'">
                                    <a :href="housemate.get_igAccount" target="_blank">
                                        <span>
                                            <img src="../assets/instagram.png" class="icon">
                                        </span>
                                    </a>
                                </template>
                                <template v-else>
                                </template>
                                <template v-if="housemate.fbAccount!=='-'">
                                    <a :href="housemate.get_fbAccount" target="_blank">
                                        <span>
                                            <img src="../assets/facebook.png" class="icon">
                                        </span></a>
                                </template>
                                <template v-else>
                                </template>
                            </template>
                            <template v-else>
                                <p style="text-align:center;"><i>Social Media info is not available</i></p>
                            </template>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import phonenumber from '../assets/telephone.png'

export default {
    name: 'Guardian',
    data() {
        return {
            housemate: {},
            phonenumber: phonenumber
        }
    },
    mounted() {
        this.getHousemate()
    },
    methods: {
        async getHousemate() {
            this.$store.commit('setIsLoading', true)
            const housemate_slug = this.$route.params.housemate_slug
            
            await axios
                .get(`/api/guardian/${housemate_slug}`) //from django REST API       ${variable} -> insert variable inside a string
                .then(response => {
                    this.housemate = response.data
                    
                    document.title = 'PetHub | ' + this.housemate.fullname

                    tt.services.fuzzySearch({
                    key: 'Krt6AzTDcWZRX5OQYcRJmGxCj5XCvi4h',
                    query: this.housemate.preferredcity
                    })
                    
                    .then(function(response) {
                    var map = tt.map({
                        key: 'Krt6AzTDcWZRX5OQYcRJmGxCj5XCvi4h',
                        container: 'map-div',
                        center: response.results[0].position,
                        zoom: 16
                    });
                    });
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
@media screen and (max-width: 800px) {
    .leftcolumn, .rightcolumn {
        width: 100%;
        padding: 0;
  }
}
/* #wholePage{
    background-color: white;
} */

.HousematePage{
    background-color: white; 
    margin-top:1%; 
    margin-bottom:1%
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
.header{
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    background: #e6e6e6;
}
.header img {
    flex-shrink: 0;
    width: 300px;
    height: 300px;
}
.content{
    padding: 20px 0px;
    text-align: justify;
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
    margin-bottom: 10px;
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
    background-color: #008080;
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
td {
  padding: 0px 40px 10px 0px;
  color: #2e3a4b
}
.tdHeader{
    color: #6d7580;
}
.card {
    text-align: center;
    background-color: #FCFEFD;
    padding: 10px;
    margin: 20px;
    margin-left: 0px;
    border-radius: 5%;
}
.card-body{
    text-align: left;
}

.profilephoto{
    object-fit: cover;
}

#map-div { width: 100%; height: 300px; }
</style>