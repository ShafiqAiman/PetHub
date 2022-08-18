<template>
    <div class="container wholepage">
        <div class="editListing" style="background-color:white">
            <div class="Form" id="form">
                <h1 style="text-align:center;">Edit Property</h1>
                <form @submit.prevent="submitForm" enctype="multipart/form-data" class="formcontent">

                    <div class="image-upload">
                        <div class="row">
                            <div class="column">
                                <label for="file-input1">
                                    <div class="propertypicsMain" v-if="uploadphoto1">
                                            <img class="propertyimagebig" :src="uploadphoto1" alt="no pictures"/>
                                        </div>
                                        <div class="propertypicsMain" v-else>
                                            <img class="propertyimagebig" :src="defaultImage"/>
                                        </div>
                                </label>
                                <input id="file-input1" type="file" @change="fileChange1" accept="image/png,image/jpeg, image/jpg, image/heic"/>

                            </div>

                            <div class="column">
                                <div class="row">

                                    <label for="file-input2">
                                        <div class="propertypics" v-if="uploadphoto2">
                                            <img class="propertyimage" :src="uploadphoto2" alt="no pictures"/>
                                        </div>
                                        <div class="propertypics" v-else>
                                            <img class="propertyimage" :src="defaultImage"/>
                                        </div>
                                    </label>
                                    <input id="file-input2" type="file" @change="fileChange2" accept="image/png,image/jpeg, image/jpg, image/heic"/>

                                    <label for="file-input3">
                                        <div class="propertypics" v-if="uploadphoto3">
                                            <img class="propertyimage" :src="uploadphoto3" alt="no pictures"/>
                                        </div>
                                        <div class="propertypics" v-else>
                                            <img class="propertyimage" :src="defaultImage"/>
                                        </div>
                                    </label>
                                    <input id="file-input3" type="file" @change="fileChange3" accept="image/png,image/jpeg, image/jpg, image/heic"/>

                                </div>

                                <div class="row">

                                    <label for="file-input4">
                                        <div class="propertypics" v-if="uploadphoto4">
                                            <img class="propertyimage" :src="uploadphoto4" alt="no pictures"/>
                                        </div>
                                        <div class="propertypics" v-else>
                                            <img class="propertyimage" :src="defaultImage"/>
                                        </div>
                                    </label>
                                    <input id="file-input4" type="file" @change="fileChange4" accept="image/png,image/jpeg, image/jpg, image/heic"/>

                                    <label for="file-input5">
                                        <div class="propertypics" v-if="uploadphoto5">
                                            <img class="propertyimage" :src="uploadphoto5" alt="no pictures"/>
                                        </div>
                                        <div class="propertypics" v-else>
                                            <img class="propertyimage" :src="defaultImage"/>
                                        </div>
                                    </label>
                                    <input id="file-input5" type="file" @change="fileChange5" accept="image/png,image/jpeg, image/jpg, image/heic"/>
                                    
                                </div>

                            </div>
                        </div>
                    </div>

                    <br><br>
                    <label for="">Name of Listing</label><br>
                    <input class="listingInput" type="text" v-model="nameOfListing" required><br><br>
                    <label for="">What type of host are you?</label><br>
                    <select class="listingInput" v-model="typeOfHost" required> 
                        <option disabled value="">Please select one</option>
                        <option>Student</option>
                        <option>Owner</option>
                        <option>Agent</option>
                    </select><br><br>

                    <br><h2>About My Property</h2>
                    <hr>
                    <label for="">Street Address<small><em> (House or Building Name, Street Name)</em></small></label><br>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" maxlength = "500" v-model="address" required></textarea><br>
                    <label for="">City</label><br>
                    <div id="test1"></div><br>
                    <!-- <input class="listingInput" type="text" v-model="city" required><br><br> -->


                    <!-- <label for="">State</label><br>
                    <input class="listingInput" type="text" v-model="state" required><br><br> -->
                    <label for="">Zip Code</label><br>
                    <input class="listingInput" type="text" v-model="zipcode" required><br><br>
                    <div class="row">
                        <div class="col-md-6 py-auto">
                            <label for="">Type of Listing</label><br>
                            <select class="listingInput" v-model="typeOfListing" required> 
                                <option disabled value="">Please select one</option>
                                <option>Private Room</option>
                                <option>Shared Room</option>
                                <option>Entire Place</option>
                            </select><br><br>

                            <template v-if="typeOfListing != 'Entire Place'">
                                <label for="">Type of Room</label><br>
                                <select class="listingInput" v-model="typeOfRoom"> 
                                    <option disabled value="">Please select one</option>
                                    <option>Master Bedroom</option>
                                    <option>Middle Bedroom</option>
                                    <option>Single Bedroom</option>
                                </select><br><br>
                            </template>

                            <label for="">Total Bedrooms</label><br>
                            <input type="radio" class="ListingInput" id="1" value ="1" v-model="totalBedrooms" required>
                            <label style="margin-right: 5%" for="1">1</label>
                    
                            <input type="radio" class="ListingInput" id="2" value ="2" v-model="totalBedrooms" required>
                            <label style="margin-right: 5%" for="2">2</label>
                    
                            <input type="radio" class="ListingInput" id="3" value ="3" v-model="totalBedrooms" required>
                            <label style="margin-right: 5%" for="3">3</label>
                    
                            <input type="radio" class="ListingInput" id="4" value ="4" v-model="totalBedrooms" required>
                            <label style="margin-right: 5%" for="4">4</label>
                    
                            <input type="radio" class="ListingInput" id="4+" value ="4+" v-model="totalBedrooms" required>
                            <label style="margin-right: 5%" for="4+">4+</label>
                    
                            
                            <br><br>

                            <label for="">Total Bathrooms</label><br>
                            <input type="radio" class="ListingInput" id="1" value ="1" v-model="totalBathrooms" required>
                            <label style="margin-right: 5%" for="1">1</label>
                    
                            <input type="radio" class="ListingInput" id="2" value ="2" v-model="totalBathrooms" required>
                            <label style="margin-right: 5%" for="2">2</label>
                    
                            <input type="radio" class="ListingInput" id="3" value ="3" v-model="totalBathrooms" required>
                            <label style="margin-right: 5%" for="3">3</label>
                    
                            <input type="radio" class="ListingInput" id="4" value ="4" v-model="totalBathrooms" required>
                            <label style="margin-right: 5%" for="4">4</label>
                    
                            <input type="radio" class="ListingInput" id="4+" value ="4+" v-model="totalBathrooms" required>
                            <label style="margin-right: 5%" for="4+">4+</label>

                            <br><br>
                        </div>
                            
                        <div class="col-md-6 py-auto">
                            <div id="rightcolumn-content">
                                <label for="">Choose Amenities</label><br>
                                <input type="checkbox" class="ListingInput" id="wifi" value="true" v-model="wifi_value">
                                <img class="amenitiesIcon" style="margin-right: 10%; margin-bottom: 5%" :src="wifi"  alt="">

                                <input type="checkbox" class="ListingInput" id="parking" value="true" v-model="parking_value">
                                <img class="amenitiesIcon" style="margin-right: 10%; margin-bottom: 5%" :src="parking"  alt="wiif">

                                <input type="checkbox" class="ListingInput" id="gym" value="true" v-model="gym_value">
                                <img class="amenitiesIcon" style="margin-right: 10%; margin-bottom: 5%" :src="gym"  alt="gym">
                                <br>
                                <input type="checkbox" class="ListingInput" id="airconditioning" value="true" v-model="aircond_value">
                                <img class="amenitiesIcon" style="margin-right: 10%" :src="aircond"  alt="air conditioned">

                                <input type="checkbox" class="ListingInput" id="swimmingpool" value="true" v-model="swimmingpool_value">
                                <img class="amenitiesIcon" style="margin-right: 10%" :src="swimmingpool"  alt="swimming pool">

                                <input type="checkbox" class="ListingInput" id="furnished" value="true" v-model="furnished_value">
                                <img class="amenitiesIcon" style="margin-right: 10%" :src="furnished"  alt="furnished">

                                <br><br>
                                <label for="description">Description <em>(500 words)</em></label><br>
                                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" maxlength = "500" v-model="description" required></textarea>
                                <br><br>
                            </div>
                        </div>
                    </div>

                    
                        
                    <br><h2>Price</h2>
                    <hr>
                    <div class="row">
                        <div class="col-md-6 py-auto">
                            <label for="">Monthly Rent</label><br>
                            <input class="listingInput" type="number" v-model.number="monthlyRent" required>MYR/month
                            <br><br>

                            <label for="">Deposit</label><br>
                            <input class="listingInput" type="number" v-model.number="deposit" required>MYR
                            <br><br>
                        </div>
                    </div>

                    
                    <!-- <input class="profileinput" style="height:100px" type="text" maxlength = "50" v-model="bio" required><br><br> -->


                    <br><h2>Preferences</h2>
                    <hr>
                    <div class="row">
                            <div class="col-md-6 py-auto" id="Pleftcolumn">
                                <label for="">Gender (optional)</label><br>
                                <select class="listingInput" v-model="Pgender">
                                    <option disabled value="">Please select one</option>
                                    <option>Male</option>
                                    <option>Female</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                                <label for="">Orientation (optional)</label><br>
                                <select class="listingInput" v-model="Psexorientation">
                                    <option disabled value="">Please select one</option>
                                    <option>Straight</option>
                                    <option>Gay</option>
                                    <option>Lesbian</option>
                                    <option>Bisexual</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                                <label for="">Age (optional)</label><br>
                                <select class="listingInput" v-model="Page">
                                    <option disabled value="">Please select one</option>
                                    <option>18 - 25</option>
                                    <option>26 - 35</option>
                                    <option>> 35</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                                <label for="">Religion (optional)</label><br>
                                <select class="listingInput" v-model="Preligion">
                                    <option disabled value="">Please select one</option>
                                    <option>Muslim</option>
                                    <option>Buddha</option>
                                    <option>Hindu</option>
                                    <option>Christian</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                            </div>
                            <div class="col-md-6 py-auto">
                                <label for="">Occupation (optional)</label><br>
                                <select class="listingInput" v-model="Poccupation">
                                    <option disabled value="">Please select one</option>
                                    <option>Student</option>
                                    <option>Working</option>
                                    <option>Not Working</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                                <label for="">Pet Status (optional)</label><br>
                                <select class="listingInput" v-model="Ppet">
                                    <option disabled value="">Please select one</option>
                                    <option>Yes</option>
                                    <option>No</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                                <label for="">Smoking (optional)</label><br>
                                <select class="listingInput" v-model="Psmoking">
                                    <option disabled value="">Please select one</option>
                                    <option>Yes</option>
                                    <option>No</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                                <label for="">Children (optional)</label><br>
                                <select class="listingInput" v-model="Pchildren">
                                    <option disabled value="">Please select one</option>
                                    <option>Yes</option>
                                    <option>No</option>
                                    <option>I don't mind</option>
                                </select><br><br>
                            </div>
                    </div>
                </form>
                <!-- <button type="submit" class="btn" @click="submitForm">Save</button> -->
            </div>
        </div>
        <div class="paymentsection">
            <button type="submit" class="pay-btn" @click="submitForm" required>Submit</button>
            
        </div>
    </div>
</template>

<script>
import Footer from '../components/Footer.vue'
import ProfilePhoto from '../assets/ProfilePhoto.png'
import wifi from '../assets/wifi.png'
import parking from '../assets/parking.png'
import aircond from '../assets/air-conditioner.png'
import furnished from '../assets/furnitures.png'
import gym  from '../assets/dumbbell.png'
import swimmingpool from '../assets/swimmer.png'
import uploadphoto1 from '../assets/AddPicture.png'
import uploadphoto2 from '../assets/AddPicture.png'
import uploadphoto3 from '../assets/AddPicture.png'
import uploadphoto4 from '../assets/AddPicture.png'
import uploadphoto5 from '../assets/AddPicture.png'
import defaultImage from '../assets/defaultPropertyImage.png'
import axios from 'axios'
import heic2any from "heic2any"

export default {
    name:'EditProperty',
    components: {
      Footer
    },
    data(){
      return{
        user: null,
        uploadphoto1:uploadphoto1,
        uploadphoto2:uploadphoto2,
        uploadphoto3:uploadphoto3,
        uploadphoto4:uploadphoto4,
        uploadphoto5:uploadphoto5,
        defaultImage:defaultImage,
        file1: null,
        file2: null,
        file3: null,
        file4: null,
        file5: null,
        wifi:wifi,
        parking:parking,
        aircond:aircond,
        gym:gym,
        furnished:furnished,
        swimmingpool:swimmingpool,
        profilephoto: ProfilePhoto,
        totalBathrooms:'',
        totalBedrooms:'',
        typeOfHost:'',
        nameOfListing:'',
        city:'',
        // city:localStorage.city,
        state:'',
        address:'',
        zipcode:'',
        typeOfListing:'',
        typeOfRoom:'',
        monthlyRent:0,
        deposit:0,
        description:'',
        wifi_value:'',
        parking_value:'',
        gym_value:'',
        aircond_value:'',
        swimmingpool_value:'',
        furnished_value:'',

        Pgender:'',
        Psexorientation:'',
        Page:'',
        Preligion:'',
        Poccupation:'',
        Ppet:'',
        Psmoking:'',
        Pchildren:'',

        user:null,
        advertiser:{},
        advertiserURL:''
        }
    },
    
    
    mounted(){
        document.title = 'Bed & Buddies | Lease Property' //Title of the page
        this.getUser();
        if (localStorage.city){
                localStorage.removeItem("preferredcity");
            }
            var options = {
                searchOptions: {
                    key: 'ksOo37MbE1U8YFbHGiKR1O4OcRrEvuJY',
                    language: 'en-GB',
                    limit: 5
                },
                autocompleteOptions: {
                    key: 'ksOo37MbE1U8YFbHGiKR1O4OcRrEvuJY',
                    language: 'en-GB'
                }
            };
            var ttSearchBox = new tt.plugins.SearchBox(tt.services, options);
            var searchBoxHTML = ttSearchBox.getSearchBoxHTML();
            // document.body.appendChild(searchBoxHTML);
            document.getElementById("test1").appendChild(searchBoxHTML);
            ttSearchBox.on('tomtom.searchbox.resultselected', function(event){
                // console.log(event.data.result.id)
                console.log(event.data.result.address.freeformAddress)
                localStorage.city = event.data.result.address.freeformAddress;
                
                //store id of the place inside database and then compare MY/GEO/p0/9504
            })
      },
    
    methods:{
        async getUser(){

            this.$store.commit('setIsLoading', true)

            await axios 
                .get('/api/v1/users/me/', {
                    headers: {
                    Authorization: "Token "+this.$store.state.token
                },
                }) 
                .then(response => {
                    this.user = response.data
                    const house_slug = this.$route.params.house_slug

                    axios
                        .get(`/djangohouses/${house_slug}`)
                        .then(response => {
                            this.myproperty = response.data
                            this.id = this.myproperty.get_id;
                            this.uploadphoto1 = this.myproperty.get_uploadphoto1;
                            this.uploadphoto2 = this.myproperty.get_uploadphoto2;
                            this.uploadphoto3 = this.myproperty.get_uploadphoto3;
                            this.uploadphoto4 = this.myproperty.get_uploadphoto4;
                            this.uploadphoto5 = this.myproperty.get_uploadphoto5;

                            this.nameOfListing = this.myproperty.nameOfListing;
                            this.typeOfHost = this.myproperty.typeOfHost;
                            this.address = this.myproperty.address;
                            this.city = this.myproperty.city;
                            this.state = this.myproperty.state;
                            this.zipcode = this.myproperty.zipcode;
                            this.typeOfListing = this.myproperty.typeOfListing;
                            this.typeOfRoom = this.myproperty.typeOfRoom;
                            this.totalBathrooms = this.myproperty.totalBathrooms;
                            this.totalBedrooms = this.myproperty.totalBedrooms;
                            this.monthlyRent = this.myproperty.monthlyRent;
                            this.deposit = this.myproperty.deposit;
                            this.wifi_value = this.myproperty.wifi_value;
                            this.parking_value = this.myproperty.parking_value;
                            this.gym_value = this.myproperty.gym_value;
                            this.aircond_value = this.myproperty.aircond_value;
                            this.swimmingpool_value = this.myproperty.swimmingpool_value;
                            this.furnished_value = this.myproperty.furnished_value;
                            this.description = this.myproperty.description;
                            this.AdvertiserID = this.myproperty.AdvertiserID;

                            this.Pgender = this.myproperty.Pgender;
                            this.Psexorientation = this.myproperty.Psexorientation;
                            this.Page = this.myproperty.Page;
                            this.Preligion = this.myproperty.Preligion;
                            this.Poccupation = this.myproperty.Poccupation;
                            this.Ppet = this.myproperty.Ppet;
                            this.Psmoking = this.myproperty.Psmoking;
                            this.Pchildren = this.myproperty.Pchildren;
                            console.log(response.data)
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

        setDefaultImg(event){
            event.target.src = "defaultImage"
        },
    
        fileChange1(e){
            this.file1 = e.target.files[0]
            
            if(this.file1.name.split('.').pop() == 'heic'){
                let heic = URL.createObjectURL(this.file1)

                fetch(heic)
                    .then((res) => res.blob())
                    .then((blob) =>
                        heic2any({
                            blob,
                            toType: "image/jpg",
                        })
                    )
                    .then((conversionResult) => {
                        this.file1 = new File([conversionResult], "convertedpicture.jpg");
                        this.uploadphoto1 = URL.createObjectURL(this.file1)
                        
                    })
                    .catch((e) => {
                        console.log(e)
                        // see error handling section
                    });
            }else{
                this.uploadphoto1 = URL.createObjectURL(this.file1)
            }
            

        },
        fileChange2(e){
            this.file2 = e.target.files[0]
            if(this.file2.name.split('.').pop() == 'heic'){
                let heic = URL.createObjectURL(this.file2)

                fetch(heic)
                    .then((res) => res.blob())
                    .then((blob) =>
                        heic2any({
                            blob,
                            toType: "image/jpg",
                        })
                    )
                    .then((conversionResult) => {
                        this.file2 = new File([conversionResult], "convertedpicture.jpg");
                        this.uploadphoto2 = URL.createObjectURL(this.file2)
                        
                    })
                    .catch((e) => {
                        console.log(e)
                        // see error handling section
                    });
            }else{
                this.uploadphoto2 = URL.createObjectURL(this.file2)
            }
        
        },
        fileChange3(e){
            this.file3 = e.target.files[0]
            if(this.file3.name.split('.').pop() == 'heic'){
                let heic = URL.createObjectURL(this.file3)

                fetch(heic)
                    .then((res) => res.blob())
                    .then((blob) =>
                        heic2any({
                            blob,
                            toType: "image/jpg",
                        })
                    )
                    .then((conversionResult) => {
                        this.file3 = new File([conversionResult], "convertedpicture.jpg");
                        this.uploadphoto1 = URL.createObjectURL(this.file3)
                        
                    })
                    .catch((e) => {
                        console.log(e)
                        // see error handling section
                    });
            }else{
                this.uploadphoto3 = URL.createObjectURL(this.file3)
            }
        },
        fileChange4(e){
            this.file4 = e.target.files[0]
            
            if(this.file4.name.split('.').pop() == 'heic'){
                let heic = URL.createObjectURL(this.file4)

                fetch(heic)
                    .then((res) => res.blob())
                    .then((blob) =>
                        heic2any({
                            blob,
                            toType: "image/jpg",
                        })
                    )
                    .then((conversionResult) => {
                        this.file4 = new File([conversionResult], "convertedpicture.jpg");
                        this.uploadphoto4 = URL.createObjectURL(this.file4)
                        
                    })
                    .catch((e) => {
                        console.log(e)
                        // see error handling section
                    });
            }else{
                this.uploadphoto4 = URL.createObjectURL(this.file4)
            }
        },
        fileChange5(e){
            this.file5 = e.target.files[0]

            if(this.file5.name.split('.').pop() == 'heic'){
                let heic = URL.createObjectURL(this.file5)

                fetch(heic)
                    .then((res) => res.blob())
                    .then((blob) =>
                        heic2any({
                            blob,
                            toType: "image/jpg",
                        })
                    )
                    .then((conversionResult) => {
                        this.file5 = new File([conversionResult], "convertedpicture.jpg");
                        this.uploadphoto5 = URL.createObjectURL(this.file5)
                        
                    })
                    .catch((e) => {
                        console.log(e)
                        // see error handling section
                    });
            }else{
                this.uploadphoto5 = URL.createObjectURL(this.file5)
            }
        },
        
        submitForm(){

            let formData = new FormData();
            if(this.file1){
                formData.append('uploadphoto1', this.file1);
            }
            if(this.file2){
                formData.append('uploadphoto2' , this.file2);
            }
            if(this.file3){
                formData.append('uploadphoto3', this.file3);
            }
            if(this.file4){
                formData.append('uploadphoto4' , this.file4);
            }
            if(this.file5){
                formData.append('uploadphoto5', this.file5);
            }
            
            formData.append('nameOfListing' , this.nameOfListing);
            formData.append('typeOfHost', this.typeOfHost);
            formData.append('address', this.address);
            formData.append('city', localStorage.city);
            formData.append('state', this.state);
            formData.append('zipcode', this.zipcode);
            formData.append('typeOfListing', this.typeOfListing);

            if(this.typeOfListing !='Entire Place'){
                formData.append('typeOfRoom', this.typeOfRoom);
            }else{
                formData.append('', this.typeOfRoom);
            }

            formData.append('totalBathrooms', this.totalBathrooms);
            formData.append('totalBedrooms', this.totalBedrooms);
            formData.append('monthlyRent', this.monthlyRent);
            formData.append('deposit', this.deposit);
            formData.append('wifi_value' , this.wifi_value);
            formData.append('parking_value' , this.parking_value);
            formData.append('gym_value' , this.gym_value);
            formData.append('aircond_value' , this.aircond_value);
            formData.append('swimmingpool_value' , this.swimmingpool_value);
            formData.append('furnished_value' , this.furnished_value);
            formData.append('description' , this.description);
            formData.append('AdvertiserID', this.user.id);

            formData.append('Pgender', this.Pgender);
            formData.append('Psexorientation', this.Psexorientation);
            formData.append('Page', this.Page);
            formData.append('Preligion', this.Preligion);
            formData.append('Poccupation', this.Poccupation);
            formData.append('Ppet', this.Ppet);
            formData.append('Psmoking', this.Psmoking);
            formData.append('Pchildren', this.Pchildren);


            const house_slug = this.$route.params.house_slug
            axios
                .put(`/djangohouses/${house_slug}/`, formData)
                .then(response =>{

                    this.uploadphoto1=uploadphoto1,
                    this.uploadphoto2=uploadphoto2,
                    this.uploadphoto3=uploadphoto3,
                    this.uploadphoto4=uploadphoto4,
                    this.uploadphoto5=uploadphoto5,
                    this.file1= null,
                    this.file2=null,
                    this.file3= null,
                    this.file4=null,
                    this.file5= null,

                    this.nameOfListing='',
                    this.typeOfHost='',
                    this.address='',
                    this.city='',
                    this.state='',
                    this.zipcode='',
                    this.typeOfListing='',
                    this.typeOfRoom='',
                    
                    this.totalBathrooms=0,
                    this.totalBedrooms=0,
                    this.monthlyRent=0,
                    this.deposit=0,
                    this.description='',

                    this.wifi_value='',
                    this.parking_value='',
                    this.gym_value='',
                    this.aircond_value='',
                    this.swimmingpool_value='',
                    this.furnished_value=''
                    window.confirm("Your property is updated!")
                    this.$router.push('/dashboard')
                    
                })

                .catch(error => {
                    alert("ERROR!!!")
                    console.log(error)
                })

                
                
                    
            // axios
            //     .put(`/djangopreferences/${this.user.id}/`, formData1)

            //     .then(response =>{
            //         this.Pgender='',
            //         this.Psexorientation='',
            //         this.Page='',
            //         this.Preligion='',
            //         this.Poccupation='',
            //         this.Ppet='',
            //         this.Psmoking='',
            //         this.Pchildren=''


                    // let option = {
                    //         animation: true,
                    //         delay: 5000
                    //     }
                    // let toast = document.getElementById('toastNotice');
                    // let successtoast = new bootstrap.Toast(toast, option);
                    // successtoast.show();
                    // document.documentElement.scrollTop = 0;

                    // localStorage.leaseproperty = formData1;
                    // setTimeout(function () {
                    //     if (newState == -1) {
                    //         alert('VIDEO HAS STOPPED');
                    //     }
                    // }, 5000);
                    // this.$router.push('/leasepayment');
            
            // })

            // .catch(error => {
            //     alert("ERROR!!!")
            //     console.log(error)
            // })
            
        }
    }
}
</script>

<style scoped>
    .pay-btn{
        margin-top: 10px;
        background-color:#fbd864;
        height: 50px;
        width: 100px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-sizing: border-box;
        padding: 5px;
        margin: 2%;
        align-self: center;
    }
    .wholepage{
        position: relative;
	    min-height: 85vh;
        background-color: white;
        padding: 3%;
        margin-bottom: 1%;
    }
    .paymentsection{
        display: block;
        align-items: center;
        margin: 10px auto;
        margin-top: 2%;
        max-width: 100px;
    }
    .listingInput{
        width: 100%;
        padding-left: 1%;
        /* border-radius: 10px; */
        border-width: 1px;
        height: 35px;
    }
    .ListingInput{
        margin-right:2%;
        border-radius: 10px;
        border-width: 1px;
    }
    .inputfile{
        display: block;
        margin:0 auto;
        width: 100px;
    }
    .amenitiesIcon{
        width: 10%;
        height: 10%;
    }
    .rightcolumn{
        width: 50%;
        position:relative;
        padding-left:10%;
    }
    .rightcolumn > .listingInput{
        width: 100%;
    }
    .leftcolumn{
        width: 50%;
    }
    #Pleftcolumn > .listingInput{
        width: 100%;
        padding: 1%;
    }
    .h2, label{
        color: #2e3a4b;
    }
    .image-upload{
        border-style: solid;
        border-width: 0.5px;
        border-color: #ccc;
        background-color: rgb(240, 239, 239);
        margin-top: 2%;
        overflow: auto;
    }
    .image-upload>input, .column>input, .row>input{
        display: none;
    }
    .column{
        float: left;
    }
    .row:after{
        content: "";
        display: table;
        clear: both;
    }
    .image-upload > .row{
        justify-content: center;
        margin: auto;
        height: 100%;
    }
    .image-upload > .row > .column{
        margin: 1%;
    }
    .propertypicsMain{
        width: 250px;
        height: 250px;
        /* width: 80%;
        height: 80%; */
        padding: 10px;
        background-size: cover;
        padding-right: 10px;
        border-radius: 15px;
    }
    .propertypics{
        width: 120px;
        height: 120px;
        /* width: 60%;
        height: 60%; */
        background-size: cover;
        overflow: hidden;
        padding: 10px;
    }
    .propertyimagebig, .propertyimage{
        width: 100%;
        height: 100%;
        border-radius: 15%;
        object-fit: scale-down;
        object-fit: cover;
    }
</style>