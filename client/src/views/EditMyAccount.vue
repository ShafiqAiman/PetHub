<template>
    <div style="background-color:white">
        <div class="Form" id="form">
            <h1 style="text-align:center;">Edit Account</h1>
            <form @submit.prevent="submitForm" enctype="multipart/form-data" class="formcontent">
                
                <template v-if="profilephoto==''">
                    <img class="photosetup" src='../assets/defaultprofilepicture.png'  alt="">
                </template>
                <template v-else>
                    <img class="photosetup" :src="profilephoto"  alt="">
                </template>
                
                <input type="file" style="margin-top:5%" class="inputfile" @change="fileChange" accept="image/png,image/jpeg, image/jpg, image/heic"/>
                <!-- <label for="file">Choose a file</label> -->
                <br><br>
                
                <label for="">Name</label><br>
                <input class="profileinput" type="text" v-model="fullname" required><br><br>

                <label for="">Phone Number</label><br>
                <input class="profileinput" type="text" v-model="phonenumber" placeholder="012-3456789" pattern="[0][1][0-9]{1}-[0-9]{7}" required><br><br>

                <label for="">Date of Birth</label><br>
                <input class="profileinput" type="date" v-model="dateofbirth" required><br><br>

                <label for="">Gender</label><br>
                <select class="profileinput" v-model="gender" required>
                    <option disabled value="">Please select one</option>
                    <option>Male</option>
                    <option>Female</option>
                </select><br><br>

                <label for="">Orientation</label><br>
                <select class="profileinput" v-model="orientation" required>
                    <option disabled value="">Please select one</option>
                    <option>Straight</option>
                    <option>Gay</option>
                    <option>Lesbian</option>
                    <option>Bisexual</option>
                </select><br><br>

                <label for="">Religion</label><br>
                <select class="profileinput" v-model="religion" required>
                    <option disabled value="">Please select one</option>
                    <option>Muslim</option>
                    <option>Buddha</option>
                    <option>Hindu</option>
                    <option>Christian</option>
                    <option>Others</option>
                </select><br><br>
                <label for="">Occupation</label><br>
                <select class="profileinput" v-model="occupation" required>
                    <option disabled value="">Please select one</option>
                    <option>Student</option>
                    <option>Working</option>
                    <option>Not working</option>
                </select><br><br>
                <label for="">Do you have pet?</label><br>
                <select class="profileinput" v-model="pet" required>
                    <option disabled value="">Please select one</option>
                    <option>Yes</option>
                    <option>No</option>
                </select><br><br>
                <label for="">About Me <small><em>(250 words)</em></small></label><br>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" maxlength = "250" v-model="aboutme" required></textarea>

                <br>
                <label for="">Preferred City</label><br>
                <div id="test1"></div><br><br>

                <label for="">Instagram</label><br>
                <input class="profileinput" type="text" v-model="igAccount" ><br><br>

                <label for="">Facebook</label><br>
                <input class="profileinput" type="text" v-model="fbAccount" ><br><br>
                
                <br><br>
                <button class="submitprofilebtn" id="toastbtn">Update</button>
                <div id="toastNotice" class="toast fixed-bottom end-0 p-3" style="margin-bottom:100px;margin-left:auto;margin-right:30px;">
                    <div class="toast-header">
                        <img src="../assets/RoomahLogo.png" width="30" height="30" alt="">
                        <strong class="mr-auto" style="margin-left:10px;">Roomah</strong>
                        <small>5 seconds ago</small>
                        <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="toast-body">
                        Your Profile is submitted!
                    </div>
                </div>
            </form>
            <!-- <button class="submitprofilebtn" @click="toast">Toast</button> -->
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import heic2any from "heic2any"

export default {
    name:'EditMyAccount',
    data(){
        return{
            profilephoto: '',
            file: null,
            fullname: '',
            phonenumber:'',
            dateofbirth:'',
            gender:'',
            orientation:'',
            religion:'',
            occupation:'',
            pet:'',
            aboutme:'',
            igAccount:'',
            fbAccount:'',

            preferredgender:null,
            preferredorientation:null,
            preferredage:null,
            preferredreligion:null,
            preferredoccupation:null,
            preferredlocation:null,
            preferredmaxrent:0,
            preferredaccommodationtype:null,

            user: null
            
        }
    },
    components:{
        
        
    },
    mounted(){
        document.title = 'Roomah | Edit Account' //Title of the page
        this.getUser()
        this.getpreferredcity()
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

                    axios
                        .get(`/djangohousemates/${this.user.id}/`)
                        .then(response => {
                            this.myprofile = response.data
                            this.profilephoto = this.myprofile.get_profilephoto;
                            this.fullname = this.myprofile.fullname;
                            this.phonenumber = this.myprofile.phonenumber;
                            this.dateofbirth = this.myprofile.dateofbirth;
                            this.gender = this.myprofile.gender;
                            this.orientation = this.myprofile.orientation;
                            this.religion = this.myprofile.religion;
                            this.occupation = this.myprofile.occupation;
                            this.pet = this.myprofile.pet;
                            this.aboutme = this.myprofile.aboutme;
                            this.igAccount = this.myprofile.igAccount;
                            this.fbAccount = this.myprofile.fbAccount;
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
        toast(){
            
            let option = {
                    animation: true,
                    delay: 5000
                }
            let toast = document.getElementById('toastNotice');
            let successtoast = new bootstrap.Toast(toast, option);
            successtoast.show();
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
            
            let userid = 67
            
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
            formData.append('aboutme', this.aboutme);
            formData.append('preferredcity', sessionStorage.preferredcity)
            formData.append('igAccount', this.igAccount)
            formData.append('fbAccount', this.fbAccount)

            axios
                .put(`/djangohousemates/${this.user.id}/`, formData)
                
                .then(response =>{
                    window.confirm("Your Profile is updated!");
                    window.location = "http://localhost:8080/myaccount"

                })
                .catch(error => {
                console.log(error)
                })

            
            
                
                
        },
        getpreferredcity(){
            if (sessionStorage.preferredcity){
                sessionStorage.removeItem("preferredcity");
            }
            var options = {
                searchOptions: {
                    key: 'ksOo37MbE1U8YFbHGiKR1O4OcRrEvuJY',
                    language: 'en-GB',
                    limit: 5,
                },
                autocompleteOptions: {
                    key: 'ksOo37MbE1U8YFbHGiKR1O4OcRrEvuJY',
                    language: 'en-GB',
                    
                }
            };
        var ttSearchBox = new tt.plugins.SearchBox(tt.services, options);
        var searchBoxHTML = ttSearchBox.getSearchBoxHTML();
        // document.body.appendChild(searchBoxHTML);
        document.getElementById("test1").appendChild(searchBoxHTML);
        ttSearchBox.on('tomtom.searchbox.resultselected', function(event){
            // console.log(event.data.result.id)
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

    .profileinput{
        width: 100%;
        padding: 1%;
    }

    .submitprofilebtn{
        margin-top: 10%;
        
        background-color:#175B5B;
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
    

</style>