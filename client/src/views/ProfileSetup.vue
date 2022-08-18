<template>
    <div style="background-color:white">
        <div class="Form" id="form">
            <h1 style="text-align:center;">Profile Setup</h1>
            <form @submit.prevent="submitForm" enctype="multipart/form-data" class="formcontent" id="profilesetupform">

                
                <img class="photosetup" :src="profilephoto"  alt="">
                <input type="file" style="margin-top:5%" class="inputfile" @change="fileChange" accept="image/png,image/jpeg, image/jpg, image/heic"/>
                <!-- <label for="file">Choose a file</label> -->
                <br><br>
                
                <label for="">Name<span class="required-field"></span></label><br>
                <input class="profileinput" type="text" v-model="fullname" required><br><br>

                <label for="">Phone Number<span class="required-field"></span></label><br>
                <input class="profileinput" type="text" v-model="phonenumber" placeholder="012-3456789" pattern="[0][1][0-9]{1}-[0-9]{7}" required><br><br>

                <label for="">Date of Birth<span class="required-field"></span></label><br>
                <input class="profileinput" type="date" v-model="dateofbirth" required><br><br>

                <label for="">Gender<span class="required-field"></span></label><br>
                <select class="profileinput" v-model="gender" required>
                    <option disabled value="">Please select one</option>
                    <option>Male</option>
                    <option>Female</option>
                </select><br><br>

                <label for="">Occupation<span class="required-field"></span></label><br>
                <select class="profileinput" v-model="occupation" required>
                    <option disabled value="">Please select one</option>
                    <option>Student</option>
                    <option>Working</option>
                    <option>Not Working</option>
                </select><br><br>
                
                <label for="">About Me <small><em>(250 words)</em></small><span class="required-field"></span></label><br>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" maxlength = "250" v-model="aboutme" required></textarea>
                <br>
                <label for="">City Base<span class="required-field"></span></label><br>
                <div id="test1"></div><br>

                <h3>Linked profile</h3>
                <p>Gain others' trust by linking your social profiles</p>
                <label for="">Instagram</label><br>
                <input class="profileinput" type="text" v-model="igAccount" placeholder="Username">
                <br><br>

                <label for="">Facebook</label><br>
                <input class="profileinput" type="text" v-model="fbAccount" placeholder="Username">
                <br><br>
                
                <div class="g-recaptcha" data-sitekey="6Lebw60gAAAAAPmmUgswG8MEhpwJqEWPGyfE7xG8"></div>

                <br><br>
                <button class="submitprofilebtn" id="toastbtn">Submit</button>

            </form>
        </div>
    </div>
</template>
    
<script>
import axios from 'axios'
import ProfilePhoto from '../assets/ProfilePhoto.png'
import heic2any from "heic2any"
export default {
    name:'ProfileSetup',
    data(){
        return{
            profilephoto: ProfilePhoto,
            file: null,
            fullname:'',
            phonenumber:'',
            email:'',
            dateofbirth:'',
            gender:'',
            orientation:'Straight',
            religion:'Muslim',
            occupation:'',
            pet:'Yes',
            smoking:'No',
            children:'No',
            aboutme:'',
            preferredcity:'',
            igAccount:'',
            user: null,
            
        }
    },
    mounted(){
        document.title = 'Bed & Buddies | Profile Setup' //Title of the page
        this.getUser()
        this.getpreferredcity()
        
    },
    methods:{
        getUser(){
            
            axios 
            .get('http://localhost:8000/api/v1/users/me/', {
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
        fileChange(e){
        this.file = e.target.files[0]
        
        if(this.file.name.split('.').pop() == 'heic'){
                let heic = URL.createObjectURL(this.file)
                fetch(heic)
                    .then((res) => res.blob())
                    .then((blob) =>
                        heic2any({
                            blob,
                            toType: "image/jpg",
                        })
                    )
                    .then((conversionResult) => {
                        this.file = new File([conversionResult], "convertedpicture.jpg");
                        this.profilephoto = URL.createObjectURL(this.file)
                        
                    })
                    .catch((e) => {
                        console.log(e)
                        // see error handling section
                    });
            }else{
                this.profilephoto = URL.createObjectURL(this.file)
            }
        },
        submitForm(){
            let recaptcharesponse = grecaptcha.getResponse()

            if(recaptcharesponse.length == 0){
                alert("Recaptcha Validation is Required!")
            }else{
                let formData=new FormData();
            if(this.file){
                formData.append('profilephoto', this.file);
            }
            
            formData.append('fullname', this.fullname);
            formData.append('phonenumber', this.phonenumber);
            formData.append('dateofbirth', this.dateofbirth);
            formData.append('gender', this.gender);
            formData.append('orientation', this.orientation);
            formData.append('religion', this.religion);
            formData.append('occupation', this.occupation);
            formData.append('pet', this.pet);
            formData.append('smoking', this.smoking);
            formData.append('children', this.children);
            formData.append('aboutme', this.aboutme);
            formData.append('preferredcity', sessionStorage.preferredcity);
            formData.append('igAccount', this.igAccount);
            
            axios
                .put(`/djangohousemates/${this.user.id}/`, formData)
                
                .then(response =>{
                    this.profilephoto='https://static.thenounproject.com/png/556457-200.png',
                    this.file= null,
                    this.fullname='',
                    this.phonenumber='',
                    this.dateofbirth='',
                    this.gender='',
                    this.orientation='',
                    this.religion='',
                    this.occupation='',
                    this.pet='',
                    this.smoking='',
                    this.children='',
                    this.aboutme='',
                    this.igAccount=''
                    
                })
            
            window.confirm("Your profile is set up successfully!")
                
            window.location = "http://localhost:8080/"
            }

            
        },
        getpreferredcity(){
            if (sessionStorage.preferredcity){
                sessionStorage.removeItem("preferredcity");
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
            document.getElementById("test1").appendChild(searchBoxHTML);
            ttSearchBox.on('tomtom.searchbox.resultselected', function(event){
                console.log(event.data.result.address.freeformAddress)
                sessionStorage.preferredcity = event.data.result.address.freeformAddress;
                
                //store id of the place inside database and then compare MY/GEO/p0/9504
            })
        }
    }
}
</script>

<style scoped>
    .inputfile{
        display: block;
        margin:0 auto;
        width: 100px;
    }
    
    .photosetup{
        width:200px;
        height:200px;
        display:block;
        margin:0 auto;
        object-fit: cover;
    }
    .Form{
        margin: 0 auto;
        width: 50%;
        margin-top: 5%;
        padding-bottom:5%;
    }
    .formcontent{
        margin: 0 auto;
        margin-top: 10%;
    }
    .required-field::before {
        content: "*";
        color: red;
        margin-left:2px
    }
    .profileinput{
        width: 100%;
        padding: 1%;
    }
    .profileinput>option:hover{
        background-color: seagreen;
    }
    .submitprofilebtn{
        margin-top: 10%;
        
        background-color:#DB4914;
        color: white;
        height: 50px;
        width: 120px;
        border: 1px solid #ccc;
        border-radius: 9px;
        box-sizing: border-box;
        padding: 5px;
        margin: 0 auto;
        display: block;
    }
    select option {
        background: rgb(255, 255, 255); 
        color: rgb(0, 0, 0); 
        box-shadow: inset 20px 20px rgb(226, 4, 4)
    } 
    select option:hover {
        color: rgb(34, 141, 13); 
        box-shadow: inset 20px 20px rgb(47, 168, 17);
    }
    
    /* select{
        cursor: -webkit-zoom-out;
    } */
</style>