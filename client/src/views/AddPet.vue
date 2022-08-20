<template>
    <div class="container wholepage">
        <div class="createListing">
            <div style="background-color:white">
                <div class="Form" id="form">
                    <h1 style="text-align:center;">Add Pet</h1>
                    <form @submit.prevent="submitForm" enctype="multipart/form-data" class="formcontent">
                        <div class="image-upload">
                            <div class="row">
                                <div class="column">
                                    <label for="file-input1">
                                        <img id="image1" :src="uploadphoto1"/>
                                    </label>
                                    <input id="file-input1" type="file" @change="fileChange1" accept="image/png,image/jpeg, image/jpg, image/heic"/>
                                </div>
                                <div class="column">
                                    <div class="row">
                                        <label for="file-input2">
                                            <img id="image2" :src="uploadphoto2"/>
                                        </label>
                                        <input id="file-input2" type="file" @change="fileChange2" accept="image/png,image/jpeg, image/jpg, image/heic"/>

                                        <label for="file-input3">
                                            <img id="image3" :src="uploadphoto3"/>
                                        </label>
                                        <input id="file-input3" type="file" @change="fileChange3" accept="image/png,image/jpeg, image/jpg, image/heic"/>
                                    </div>
                                    <div class="row">
                                        <label for="file-input4">
                                            <img id="image4" :src="uploadphoto4"/>
                                        </label>
                                        <input id="file-input4" type="file" @change="fileChange4" accept="image/png,image/jpeg, image/jpg, image/heic"/>
                                        <label for="file-input5">
                                            <img id="image5" :src="uploadphoto5"/>
                                        </label>
                                        <input id="file-input5" type="file" @change="fileChange5" accept="image/png,image/jpeg, image/jpg, image/heic"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <br><br>
                        <label for="">Name of Pet</label><br>
                        <input class="form-control" type="text" v-model="nameOfPet" required><br>

                        <label for="">Type of Pet</label><br>
                        <select class="form-control" v-model="typeOfPet" required> 
                            <option disabled value="">Please select one</option>
                            <option>Cat</option>
                            <option>Dog</option>
                            <option>Turtle</option>
                            <option>Fish</option>
                            <option>Rabbit</option>
                        </select><br>

                        <label for="">Pet Species</label><br>
                        <input type="text" class="form-control" id="exampleFormControlTextarea1" maxlength = "500" v-model="petSpecies" required>
                        <br>

                        <label for="">Pet Status</label><br>
                        <select class="form-control" v-model="petStatus" required> 
                            <option disabled value="">Please select one</option>
                            <option>Adopted</option>
                            <option>Looking for a new Guardian</option>
                        </select><br>

                        <template v-if="petStatus == 'Looking for a new Guardian'">
                            <label for="">Price (RM)</label><br>
                            <input class="form-control" type="number" v-model="priceofSelling" required><br>
                        </template>

                        <label for="">Date of Birth<span class="required-field"></span></label><br>
                        <input class="form-control" type="date" v-model="dateofbirth" required><br>

                        <label for="">Health Status</label><br>
                        <select class="form-control" v-model="healthStatus" required> 
                            <option disabled value="">Please select one</option>
                            <option>Healthy</option>
                            <option>Sick</option>
                        </select>
                        <br>

                        <template v-if="healthStatus == 'Sick'">
                            <label for="">Diagnosis</label><br>
                            <input class="form-control" type="text" v-model="sickDiagnosis" required><br>
                        </template>

                        <label for="description">Description <em>(500 characters)</em></label><br>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" maxlength = "500" v-model="description" required></textarea>
                        <br>

                        </form>
                    </div>
                    
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

import uploadphoto1 from '../assets/AddPicture.png'
import uploadphoto2 from '../assets/AddPicture.png'
import uploadphoto3 from '../assets/AddPicture.png'
import uploadphoto4 from '../assets/AddPicture.png'
import uploadphoto5 from '../assets/AddPicture.png'
import axios from 'axios'
import heic2any from "heic2any"

export default {
    name:'AddPet',
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
        file1: null,
        file2: null,
        file3: null,
        file4: null,
        file5: null,
        
        profilephoto: ProfilePhoto,
        nameOfPet:'',
        typeOfPet:'',
        petSpecies:'',
        petStatus:'',
        priceofSelling:0,
        dateofbirth:'',
        healthStatus:'',
        sickDiagnosis:'',
        description:'',
        
        user:null,
        }
    },
    
    
    mounted(){
        document.title = 'PetHub | Add Pet' //Title of the page
        this.getUser();
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
            const house_slug = this.$route.params.house_slug
            // console.log(this.user)
            })
            .catch(error => {
            console.log(error)
            })
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
            
            formData.append('nameOfPet' , this.nameOfPet);
            formData.append('typeOfPet', this.typeOfPet);
            formData.append('petSpecies', this.petSpecies);
            formData.append('petStatus', this.petStatus);
            if(this.petStatus == 'Looking for a new Guardian'){
                formData.append('priceofSelling', this.priceofSelling);
            }else{
                formData.append('priceofSelling', 0.00);
            }
            
            formData.append('dateofbirth', this.dateofbirth);
            formData.append('healthStatus', this.healthStatus);
            if(this.healthStatus == 'Sick'){
                formData.append('sickDiagnosis', this.sickDiagnosis);
            }else{
                formData.append('sickDiagnosis', '');
            }
            
            formData.append('description' , this.description);
            formData.append('AdvertiserID', this.user.id);
             
            axios
                .post("/djangohouses/", formData)
                .then(response =>{
                    axios
                        .get(`/djangohousemates/${this.user.id}/`)
                        .then(response=>
                        {
                            this.housecounter = response.data.petcounter+ 1
                            let formData1 = new FormData();
                            formData1.append('HasPet', 'Has A Pet');
                            formData1.append('petcounter', this.housecounter)

                            axios
                                .put(`/djangohousemates/${this.user.id}/`, formData1)
                        })

                        .catch(error => {
                            alert("ERROR!!!")
                            console.log(error)
                        })

                })
                .catch(error => {
                    alert("ERROR!!!")
                    console.log(error)
                })

            window.confirm("Your Property is Leased Successfully!")
            this.$router.push('/')
            
        }
    }
}
</script>

<style scoped>
    .pay-btn{
        margin-top: 10px;
        background-color:#DB4914;
        color: white;
        height: 50px;
        width: 100px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-sizing: border-box;
        padding: 5px;
        margin: 2%;
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
    /* .photosetup{
        width:200px;
        height:200px;
        display:block;
        margin:0 auto;
        margin-top: 5%;
    } */
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
    .h2,.h3, label{
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
        /* justify-content: center; */
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
    #image1{
        width: 210px;
        height: 210px;
        padding: 10px;
        padding-right: 10px;
        border-radius: 10%;
    }
    #image2,#image3,#image4,#image5{
        width: 100px;
        height: 100px;
        padding: 10px;
        border-radius: 10%;
    }
    button{
        align-self: center;
    }

    .paymentbills{
        display: flex;
        width: 100%;
    }

    .paymentleft{
        width: 50%;
    }

    .paymentright{
        width: 50%;
        text-align: right;
    }
    
    
</style>