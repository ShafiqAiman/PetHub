<template>
    <div class='div' id='wholePage'>
        <div class='HousePage container'>

            <div class="header">
                <div id="carousel" class="carousel slide" data-ride="carousel" data-interval="false">
                    <ol class="carousel-indicators">
                        <li data-target="#carousel" data-slide-to="0" class="active" v-if="pet.get_uploadphoto1"></li>
                        <li data-target="#carousel" data-slide-to="1" v-if="pet.get_uploadphoto2"></li>
                        <li data-target="#carousel" data-slide-to="2" v-if="pet.get_uploadphoto3"></li>
                        <li data-target="#carousel" data-slide-to="3" v-if="pet.get_uploadphoto4"></li>
                        <li data-target="#carousel" data-slide-to="4" v-if="pet.get_uploadphoto5"></li>
                    </ol>

                    <div class="carousel-inner" v-if="pet.get_uploadphoto1 
                                                    ||pet.get_uploadphoto2
                                                    ||pet.get_uploadphoto3
                                                    ||pet.get_uploadphoto4
                                                    ||pet.get_uploadphoto5">
                        <div class="carousel-item active" v-if="pet.get_uploadphoto1">
                            <img :src="pet.get_uploadphoto1" class="d-block w-100 pic" alt="image 1">
                        </div>
                        <div class="carousel-item" v-if="pet.get_uploadphoto2">
                            <img :src="pet.get_uploadphoto2" class="d-block w-100 pic" alt="image 2">
                        </div>
                        <div class="carousel-item" v-if="pet.get_uploadphoto3">
                            <img :src="pet.get_uploadphoto3" class="d-block w-100 pic" alt="image 3">
                        </div>
                        <div class="carousel-item" v-if="pet.get_uploadphoto4">
                            <img :src="pet.get_uploadphoto4" class="d-block w-100 pic" alt="image 4">
                        </div>
                        <div class="carousel-item" v-if="pet.get_uploadphoto5">
                            <img :src="pet.get_uploadphoto5" class="d-block w-100 pic" alt="image 5">
                        </div>
                    </div>

                    <div class="carousel-inner" v-else>
                        <div class="carousel-item active">
                            <img :src="defaultImage" class="d-block w-100" alt="image 5">
                        </div>
                    </div>

                    <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                    </a>
                    <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                    </a>
                </div>
            </div>

            <div class="row">

                <div class="col-md-8 py-auto">

                    <div class="d-flex justify-content-between">
                        <div>
                            <h2 class="title">{{ pet.nameOfPet }}</h2>
                            <h3 class="title">{{ pet.get_age }} years old</h3>
                            <h3 class="title"><mark>{{ pet.petStatus }}</mark></h3>
                            <template v-if="pet.petStatus == 'Looking for a new Guardian'">
                                    <p class="title">RM {{ pet.priceofSelling }}</p><br>
                            </template>
                            
                        </div>
                    </div>
                    <hr>

                    <div class="productInfo">
                        <div class="content">
                            <h3>Description</h3><br>
                            <p>{{ pet.description }}</p>
                        </div>
                        <hr>

                        <div class="info">

                            <div class="content">
                                
                                <div class="row">
                                    <div class="col-6 col-md-4">
                                        <h4>Type of Pet</h4>
                                        <p>{{ pet.typeOfPet }}</p><br>
                                    </div>
                                    <div class="col-6 col-md-4">
                                        <h4>Species of Pet</h4>
                                        <p>{{ pet.petSpecies }}</p><br>
                                    </div>
                                    
                                </div>
                                <hr>
                            </div>

                            <div class="content">
                                
                                <div class="row">
                                    <div class="col-6 col-md-4">
                                        <h4>Health Status</h4>
                                        <p>{{ pet.healthStatus }}</p><br>
                                    </div>
                                    
                                    <template v-if="pet.healthStatus == 'Sick'">
                                        <div class="col-6 col-md-4">
                                            <h4>Species of Pet</h4>
                                            <p>{{ pet.sickDiagnosis }}</p><br>
                                        </div>
                                    </template>
                                    
                                </div>
                                
                            </div>
                            

                            
                            


                        </div>
                        <div id="map-div"></div>
                    </div>
                </div>

                <div class="col-md-4 py-auto">
                    <div class="card" id="ownerinfo">
                        <div class="image">
                            <router-link :to="`${advertiserURL}`" style="text-decoration:none;">
                                <img class="ownerimage" :src="advertiser.profilephoto" alt="Picture of Owner">
                            </router-link>
                        </div>
                        <div class="card-body">
                            <h3 class="card-title">{{ advertiser.fullname }}</h3>
                            <p class="card-text">{{ advertiser.gender }}, {{ advertiser.occupation }}</p><hr>
                            <h4 class="card-title">About me</h4>
                            <p class="card-text">{{ advertiser.aboutme }}</p><hr>
                            <h4 class="card-title">Contact</h4>
                            <p class="card-text">{{ advertiser.phonenumber }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import defaultImage from '../assets/defaultPropertyImage.png'

export default {
    name: 'Pet',
    data() {
        return {
            pet: {},
            defaultImage:defaultImage,
            advertiser:{},
            advertiserURL:''
        }
    },
    components: {
    },
    mounted() {
        this.getProduct()

    },
    methods: {
        async getProduct() {
            
            this.$store.commit('setIsLoading', true)
            const house_slug = this.$route.params.house_slug
            await axios
                .get(`/api/pet/${house_slug}`) //from django REST API       ${variable} -> insert variable inside a string
                .then(response => {
                    this.pet = response.data
                    
                    document.title = 'PetHub | ' + this.pet.nameOfPet
                    axios
                        .get(`/api/guardians/${this.pet.AdvertiserID}`) 
                        .then(response =>{
                            this.advertiser = response.data
                            this.advertiserURL = this.advertiser.get_absolute_url
                            
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
@media screen and (max-width: 800px) {
  .leftcolumn, .rightcolumn {
    width: 100%;
    padding: 0;
  }
}

.HousePage{
    background-color: white; 
    margin-top:1%; 
    margin-bottom:1%
}
.row{
    padding: 20px;
    box-shadow: none;
}
.content > .row{
    padding: 0px;
}
hr{
    width: 90%;
}
.header {
  padding: 2%;
}
.carousel-inner > .carousel-item > img{
    position: relative;
    width:100%;
    height:382px;
    overflow: hidden;
}
.priceStyle > a{
    padding: 10px;
}
a:hover{
    text-decoration: none;
}
h2{
    color: #2e3a4b;
}
h3{
    font-size: 20px;
    color: #2e3a4b;
}
h4{
    font-size: 18px;
    color: #2e3a4b;
}
.content{
    padding: 20px 0px;
    text-align: justify;
}


.icon{
    width: 40px;
    height: 40px;
    margin-right: 10px;
}
td {
  padding: 0px 40px 10px 0px;
  color: #2e3a4b
}
.tdHeader{
    color: #6d7580;
}
.leftcolumn {
    float: left;
    width: 65%;
    padding: 1% 0 0 20px;
}
.rightcolumn{
    width: 35%;
    padding-left: 20px;
}
.card{
    padding: 10px;
    margin: 20px 0px 20px 20px;
    border-radius: 5%;
}
.image{
    position: relative;
    width:100%;
    height:150px;
    overflow: hidden;
    border-radius: 5%;
    background-color: #e7eeec;
}
.ownerimage{
    width:100%;
    height:100%;
    object-fit: scale-down;
    object-fit: cover;
}
.row:after {
    content: "";
    display: table;
    clear: both;
}
.card-title{
    color: #044B4B;
}
.card-text{
    text-align: justify;
}
button{
    margin-top: 10px;
    background-color:#fbd864;
    height: 40px;
    width: 100px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 5px;
    margin: 2%;
}

.title{
    text-align: justify;
}

#map-div { width: 100%; height: 300px; }

.pic{
    object-fit: cover;
}
</style>