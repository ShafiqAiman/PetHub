<template>
   <div class="container">
      <div class="wrapper">
        <div class="row">
          <div class="col-xs-1 col-md-12">
            <div class="intro">
              <h1>My Listings</h1>
              <a href="/leaseproperty" class="nav-link" style="color:white;">
                <button id="addPropertyButton">
                <img src="../assets/add.png" class="plusIcon">
                Add a property
                </button>
              </a>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-md-12 py-auto">
            <div class="DashboardCards" v-for="myHouse in myHouses" :key="myHouse.id">
              <div class="houseDisplayed p-4">
                <div class="row">
                  <div class="col-md-8">
                    <div class="row">
                      <div class="col-md-6 py-auto">
                        <div class="image">
                          <img class="housePic rounded" v-if="myHouse.get_uploadphoto1" :src="myHouse.get_uploadphoto1">
                          <img class="housePic rounded" v-else :src="defaultImage">
                        </div>
                      </div>

                      <div class="col-md-6">
                        <div class="houseHeader">
                          <template v-if="myHouse.nameOfListing.length >18">
                            <h3 class="title">{{ myHouse.nameOfListing.substring(0,20)+'...' }}</h3>
                          </template>
                          <template v-else>
                            <h3 class="title">{{ myHouse.nameOfListing }}</h3>
                          </template>
                        </div>
                    
                        <div class="houseContent">
                          <b style="color:#175B5B">{{ myHouse.city }}</b><br><br>
                          <p>RM{{ myHouse.monthlyRent }}/month</p>
                          <template v-if="myHouse.typeOfListing == 'Entire Place'">
                            <p>{{ myHouse.typeOfListing }} </p>
                          </template>
                          <template v-else>
                            <p>{{ myHouse.typeOfRoom }} ({{ myHouse.typeOfListing }})</p>
                          </template>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="col-md-4 py-auto" style="padding:5%;">
                    <div class="options" style="text-align: center;">
                      <router-link :to="myHouse.get_editproperty_url"> 
                        <button id="editButton">Edit</button>
                      </router-link>
                      <button id="deleteButton" @click="deleteHouse(myHouse.id)">Delete</button>
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
    name: 'Dashboard',
    data(){
        return{
            user:{},
            Houses:[],
            filterProperty:'',
            temphousecounter:0,
            tempID:'',
            noproperty:'Needs A Place',
        }
    },
    mounted(){
        document.title = 'Bed & Buddies | My Dashboard'
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
            .get('/djangohouses') //to get data that is converted by Django REST with the help of Axios
            .then(response => {
            this.Houses = response.data
            for (var i = 0; i < this.Houses.length; i++) {
                this.Results.push(this.Houses[i].nameOfListing)
                this.Results.push(this.Houses[i].city)
            }
            })
            .catch(error => {
              console.log(error)
            })
        this.$store.commit('setIsLoading', false)

        },

        deleteHouse(tempID)
        {
            axios
            .delete(`/djangohouses/${tempID}/`)
            .then(response=> 
            {
                window.confirm("House deleted")

               axios
                .get(`/djangohousemates/${this.user.id}/`)
                .then(response=>
                {
                    this.temphousecounter = response.data.housecounter
                    this.temphousecounter = this.temphousecounter - 1
                    console.log("before:" +this.temphousecounter)
                      let formData1 = new FormData()
                      formData1.append('housecounter', this.temphousecounter)
                      axios
                        .put(`/djangohousemates/${this.user.id}/`, formData1)
                        .then(response=>
                          {
                            if(this.temphousecounter==0)
                            {
                              axios
                                .put(`/djangohousemates/${this.user.id}/`, {'HasRoom':this.noproperty})
                                .then(response=>
                                  {
                                     console.log(this.user.HasRoom)
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
        myHouses()
        {
        this.filterProperty= this.Houses.filter(myHouse => myHouse.AdvertiserID==this.user.id)
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
