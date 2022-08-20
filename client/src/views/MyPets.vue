<template>
   <div class="container">
      <div class="wrapper">
        <div class="row">
          <div class="col-xs-1 col-md-12">
            <div class="intro">
              <h1>My Pets</h1>
              <a href="/addpet" class="nav-link" style="color:white;">
                <button id="addPropertyButton">
                <img src="../assets/add.png" class="plusIcon">
                Add a pet
                </button>
              </a>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-md-12 py-auto">
            <div class="DashboardCards" v-for="myPet in myPets" :key="myPet.id">
              <div class="houseDisplayed p-4">
                <div class="row">
                  <div class="col-md-8">
                    <div class="row">
                      <div class="col-md-6 py-auto">
                        <div class="image">
                          <img class="housePic rounded" v-if="myPet.get_uploadphoto1" :src="myPet.get_uploadphoto1">
                          <img class="housePic rounded" v-else :src="defaultImage">
                        </div>
                      </div>

                      <div class="col-md-6">
                        <div class="houseHeader">
                          <template v-if="myPet.nameOfPet.length >18">
                            <h3 class="title">{{ myPet.nameOfPet.substring(0,20)+'...' }}</h3>
                          </template>
                          <template v-else>
                            <h3 class="title">{{ myPet.nameOfPet }}</h3>
                          </template>
                        </div>
                    
                        <div class="houseContent">
                          <b style="color:#175B5B">{{ myPet.petStatus }}</b><br><br>
                          
                          <template v-if="myPet.petStatus == 'Looking for a new Guardian'">
                            <p>RM{{ myPet.priceofSelling }}</p>
                          </template>
                          
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="col-md-4 py-auto" style="padding:5%;">
                    <div class="options" style="text-align: center;">
                      <router-link :to="myPet.get_editproperty_url"> 
                        <button id="editButton">Edit</button>
                      </router-link>
                      <button id="deleteButton" @click="deleteHouse(myPet.id)">Delete</button>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>

      </div>
   </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'MyPets',
    data(){
        return{
            user:{},
            Pets:[],
            filterProperty:'',
            temphousecounter:0,
            tempID:'',
            noproperty:'Needs A Place',
        }
    },
    mounted(){
        document.title = 'PetHub | My Pets'
        this.getUser()
        this.getHouses()
    },
    methods:{
        getUser(){
            this.$store.commit('setIsLoading', true)
            axios 
                .get('/api/v1/users/me/', {
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

                this.$store.commit('setIsLoading', false)          
        },

        async getHouses(){
        this.$store.commit('setIsLoading', true)
       
        await axios  //localhost:8000/djangohouses
            .get('/api/pets') //to get data that is converted by Django REST with the help of Axios
            .then(response => {
            this.Pets = response.data
            console.log(this.Pets)
            
            })
            .catch(error => {
              console.log(error)
            })
        this.$store.commit('setIsLoading', false)

        },

        deleteHouse(tempID)
        {
            axios
            .delete(`/api/pets/${tempID}/`)
            .then(response=> 
            {
                window.confirm("Pet is deleted")

               axios
                .get(`/api/guardians/${this.user.id}/`)
                .then(response=>
                {
                    this.temphousecounter = response.data.petcounter - 1
                      let formData1 = new FormData()
                      formData1.append('petcounter', this.temphousecounter)
                      axios
                        .put(`/api/guardians/${this.user.id}/`, formData1)
                        .then(response=>
                          {
                            if(this.temphousecounter==0)
                            {
                              axios
                                .put(`/api/guardians/${this.user.id}/`, {'HasPet':'Has No Pet'})
                                .then(response=>
                                  {
                                     
                                     location.reload()
                                  })
                            }
                            else
                            {
                                location.reload()
                            }
                          })  
                })
            })
        }  
    },
    computed:{
        myPets()
        {
        this.filterProperty= this.Pets.filter(myPet => myPet.AdvertiserID==this.user.id)
        return this.filterProperty
        }
    }
}
</script>
<style scoped>

.wrapper{
  height: 100%;
  margin: 0  auto;
  padding: 5% 0 5% 0;
  min-height: 85vh;
  background-color: white;
}

.intro{
  text-align: center;
}

.DashboardCards{
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 100%;
}

.image{
  position: relative;
  width: 100%;
  height: 150px;
  overflow: hidden;
  background-color: #e7eeec;
  margin-bottom: 10px;
}

.housePic{
  width: 100%;
  height: 100%;
  object-fit: scale-down;
  object-fit: cover;

}

.houseDisplayed{
  margin: 1%;
  background-color: rgb(238, 238, 238);
  padding: 2% 2% 0.5% 2%;
  width: 100%;
}

.houseHeader{
  width: 100%;
}

#editButton{
  background-color:#fbd864;
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 2%;
  text-align: center;
  width: 30%;
}

#deleteButton{
  background-color:rgb(228, 226, 226);
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 2%;
  text-align: center;
  width: 30%;
  margin-left: 10%;
}

.container #addPropertyButton{
  width:200px;
  margin-bottom: 2%;
  display: block;
  margin: auto;
  padding: .5%;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-sizing: border-box;
  border-width: 2px;
  background-color: white;
  border-radius: 4%;
}

.plusIcon{
  width:15px;
  margin-right:10%;
}
</style>
