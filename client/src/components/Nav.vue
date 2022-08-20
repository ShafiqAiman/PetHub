<template>
    <nav class="navbar sticky-top navbar-expand-md navbar-light">
        <a class="navbar-brand" href="#">
            
            <router-link to="/" style="color:white;margin-left:10px;text-decoration:none;" class="navbar-item">
            <img src="../assets/pethub.png" width="30" height="30"  class="logo d-inline-block align-top" alt="">
            PetHub
            </router-link>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div id="navbar" class="collapse navbar-collapse" :class="{'is-active': showMobileMenu}">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <!-- <router-link to="/" style="color:white;margin-left:10px" class="nav-link">Home</router-link> -->
                    <!-- <a class="nav-link" style="color:white;" href="#">Home <span class="sr-only"></span></a> -->
                </li>
                
            </ul>
            
            <ul class="navbar-nav ml-auto">
                <li class="nav-item dropdown">
                    <ul class="listing navbar-nav ml-auto" style="margin-top:3px;">
                      <li class="nav-item">
                        <router-link to="/" style="color:white;" class="nav-link">Home</router-link>
                      </li>
                      
                      <li class="nav-item">
                        <router-link to="/findpet" style="color:white;" class="nav-link">Find Pet</router-link>
                        <!-- <router-link to="/Pricing" style="color:white;margin-left:10px" class="nav-link"><img class="icon" src="../assets/LeasePropertyIcon.png" title="Lease Property"></router-link> -->
                      </li>
                      <li class="nav-item">
                        <router-link to="/findguardian" style="color:white;" class="nav-link">Find Guardian</router-link>
                        <!-- <router-link to="/Pricing" style="color:white;margin-left:10px" class="nav-link"><img class="icon" src="../assets/LeasePropertyIcon.png" title="Lease Property"></router-link> -->
                      </li>
                      <li class="nav-item">

                        <router-link to="" class="nav-link" style="color:white;" @click="profileSetupValidation('/addpet')">Add Pet</router-link>
                        <!-- <router-link to="/Pricing" style="color:white;margin-left:10px" class="nav-link"><img class="icon" src="../assets/LeasePropertyIcon.png" title="Lease Property"></router-link> -->
                      </li>
                          <li class="nav-item dropdown">
                              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  <template v-if="profilephoto==null">
                                    <img src="../assets/defaultprofilepicture.png" width="30" height="30" class="profilepicture d-inline-block align-top">
                                  </template>
                                  <template v-else>
                                    <img :src="profilephoto" width="30" height="30"  class="profilepicture d-inline-block align-top" alt="">
                                  </template>
                                  
                                  <!-- <span class="myaccount">{{fullname}}</span> -->
                              </a>
                              <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">

                                <router-link to="" class="dropdown-item" @click="profileSetupValidation('/myaccount')">My Account</router-link>
                                <router-link to="" class="dropdown-item" @click="profileSetupValidation('/mypets')">My Pets</router-link>
                                <router-link to="/settings" class="dropdown-item">Settings</router-link>
                                <router-link to="/help" class="dropdown-item">Help</router-link>
                                <router-link to="" class="dropdown-item" @click="logout">Logout</router-link>

                              </div>
                          </li>
                    </ul>
                </li>
            </ul>
          
        </div>
    </nav>
</template>

<script>
import axios from 'axios'

export default {
    name:'Nav',
    data(){
      return{
        profilephoto:'',
        fullname: '',
        showMobileMenu:false,
        user: null,
        myprofile: null
      }
    },
    mounted(){
        this.getUser()
    },
    methods:{
        getUser(){
            
            axios 
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
                            this.profilephoto = this.myprofile.profilephoto;
                            let index = (this.myprofile.fullname).indexOf(" ")
                            
                            this.fullname = (this.myprofile.fullname).substring(0, index);
                            
                        })
                        .catch(error => {
                            console.log(error)
                        })
                })
                .catch(error => {
                    console.log(error)
                })

                
        },
        profileSetupValidation(x){
            if(this.myprofile.gender === '-' || this.myprofile.occupation === '-' || this.myprofile.orientation === '-' || this.myprofile.religion === '-' || this.myprofile.pet === '-'){
				alert("Please set up your profile first!")
                window.location = "http://localhost:8080/profilesetup"	
			}else{
                this.$router.push(x)
            }
        },
        logout(){
            // console.log("Logout")
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')
            // window.confirm("You are logged out");
            this.$router.push('/')
        }
    }
}
</script>
<style scoped>

    .icon{
    width: 27px;
    height: 27px;
    /* margin-right: 10px; */
    }

    sup {
    vertical-align: super;
    font-size: smaller;
    background-color: red;
    font-weight: bold;
    border-radius: 10px;
    padding: 0 6px;
    }

    .profilepicture{
        border-radius: 50%;
        object-fit: cover;
    }

    .myaccount{
        color:white;
        margin-left: 5px;
        
    }

    .logo{
    border-radius: 50%;
    object-fit: cover;
  }

</style>