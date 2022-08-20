<template>
  <div class="wholepage">
    <header class="jumbotron jumbotron-fluid text-center">
      <div class="container">
        <h3 class="header">Find Pet</h3>
        <form action="">
          <div class="center-block">    
            <SearchAutocomplete
              :items="Results"
              @selected="selectedResult"
              />
              <Modal v-show="isModalVisible" @close="closeModal"/>
          </div>
        </form>
      </div>
    </header>

        <div class ="postgroup">
          <template v-if="filterSearch==''">
            <div class="NoResult">
              <h3 style="margin-left:2%;">No Results</h3>
            </div>
          </template>
          <template v-else>
            <h3 style="margin-left:2%;">Results for '{{search}}'</h3>
          </template>
          
          
          
          <div class="group">
            <div class="filterSort">
              <button type="button" class="my-button" @click="showModal"><img class="filterIcon" src="../assets/FilterIcon.png" alt="">Filters</button><br>
            </div>
            
            <div class="posts" v-for="pet in filteredPosts.slice((currentPage-1) * perPage,(currentPage-1) * perPage+perPage)" :key="pet.id">
              <router-link to="" style="text-decoration:none;" @click="newWindow(pet.get_absolute_url)">
                  <figure class="polaroid">
                    <img v-if="pet.get_uploadphoto1" :src="pet.get_uploadphoto1" style="width:100%;border-top-left-radius: 25px;border-top-right-radius: 25px;max-height:200px;">
                    <img v-else :src="defaultImage" style="width:100%;border-top-left-radius: 25px;border-top-right-radius: 25px;max-height:200px;">
                    <div class="container">
                      <div style="height:80px">
                        <template v-if="pet.nameOfPet.length >18">
                          <h3 class="title">{{ pet.nameOfPet.substring(0,16)+'...' }}, {{ pet.get_age}}</h3>
                        </template>
                        <template v-else>
                          <h3 class="title">{{ pet.nameOfPet }},{{ pet.get_age}}</h3>
                        </template>
                        
                      </div>
                      <div>
                        
                        <b class="postcontent"><mark>{{ pet.petStatus }}</mark></b><br><br>
                        <p class="postcontent">{{ pet.typeOfPet }}</p>
                        <p class="postcontent">{{ pet.petSpecies }}</p>
                        <p class="postcontent">{{ pet.description }}</p>
                      </div>
                    </div>
                </figure>
              </router-link>
            </div>
          </div>
          <div id="pages">
            
          </div>

          

          <nav aria-label="Page navigation example">
            <ul class="pagination justify-content-center">
              <template v-if="currentPage>1">
                <li class="page-item">
                    <a class="page-link" tabindex="-1" @click="previousPage">Previous</a>
                </li>
              </template>
              <template v-else>
                <li class="page-item disabled">
                    <a class="page-link" tabindex="-1">Previous</a>
                </li>
              </template>
              <div v-for="i in range(1, TotalPages)" :key="i">
                <li class="page-item"><a class="page-link" @click="pageChange(i)">{{ i }}</a></li>
              </div>
              <template v-if="currentPage==TotalPages">
                <li class="page-item disabled">
                  <a class="page-link">Next</a>
                </li>
              </template>
              <template v-else>
                <li class="page-item">
                  <a class="page-link" @click="nextPage">Next</a>
                </li>
              </template>
            </ul>
          </nav>

          
        </div>
  </div>
</template>

<script>
import Modal from '../components/Modal.vue';
import SearchAutocomplete from '../components/SearchAutocomplete.vue'

import defaultImage from '../assets/defaultPropertyImage.png'

import axios from 'axios'
export default {
  name: 'FindPet',
  components: {
      Modal,
      SearchAutocomplete,
    },
  data(){
    return{
      isModalVisible: false,
      search:'',
      Pets:[],
      Results:[],

      perPage:6,
      currentPage: 1,
      TotalPages: 1,
      
      TypeOfPet:'',
      PetStatus:'',
      HealthStatus:'',
      PetAge:1000,
      MinAge:0,
      

      filterSearch:'',
      filtertypeOfPet:'',
      filterpetStatus:'',
      filterhealthStatus:'',
      filterage:'',
      

      defaultImage:defaultImage,
    }
  },
  mounted(){
    document.title = 'PetHub | Find Pet' //Title of the page
    this.getHouses()
  },
  methods:{
    pageChange(page){
      this.currentPage = page;
    },

    nextPage(){
      this.currentPage++;
    },

    previousPage(){
      if(this.currentPage!=1){
        this.currentPage--;
      }
    },

    range : function (start, end) {
      return Array(end - start + 1).fill().map((_, idx) => start + idx)
   },

    async getHouses(){
      this.$store.commit('setIsLoading', true)

      await axios  //localhost:8000/djangohouses
         .get('/api/pets') //to get data that is converted by Django REST with the help of Axios
        .then(response => {
          this.Pets = response.data

          for (var i = 0; i < this.Pets.length; i++) {
            this.Results.push(this.Pets[i].nameOfPet)
            this.Results.push(this.Pets[i].typeOfPet)
            
          }
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)

      },
      showModal() {
          this.isModalVisible = true;
      },
      closeModal(typeOfPet, petStatus, healthStatus, petAge, minage) {
        this.isModalVisible = false;
        
        this.TypeOfPet = typeOfPet;
        this.PetStatus = petStatus;
        this.HealthStatus = healthStatus;
        this.PetAge = petAge;
        this.MinAge = minage;
        
      
      },
      selectedResult(e){
        this.search = e;
      },
      newWindow(url){
        window.open(url)
      }
    
  },
  computed:{
    filteredPosts(){
      //Filter Results (Pet)
      
      
      
      this.filtertypeOfPet = this.Pets.filter(pet => pet.typeOfPet.toLowerCase().includes(this.TypeOfPet.toLowerCase()))
      this.filterpetStatus = this.filtertypeOfPet.filter(pet => pet.petStatus.toLowerCase().includes(this.PetStatus.toLowerCase()))
      this.filterhealthStatus = this.filterpetStatus.filter(pet => pet.healthStatus.toLowerCase().includes(this.HealthStatus.toLowerCase()))
      this.filterage = this.filterhealthStatus.filter(pet => (pet.get_age <= this.PetAge) && (pet.get_age >= this.MinAge))
      this.filterSearch = this.filterage.filter(pet => pet.nameOfPet.toLowerCase().includes(this.search.toLowerCase()))

      this.TotalPages = Math.ceil(this.filterhealthStatus.length/this.perPage)
      


      //Return Final Results
      return this.filterSearch
    }
  }
}
</script>

<style scoped>

  .wholepage{
    min-height: 85vh;
	  
  }

  header{
    background-image: linear-gradient(rgba(0, 0, 0, 0.527),rgba(0, 0, 0, 0.5)) , url("../assets/header_bg.jpg");
    background-attachment: scroll;
    background-repeat:no-repeat;
    background-size: cover;
    height:25%;
    background-position: 0 70%;
  }

  .filterSort{
    width: 100%;
    height: 100px;
    padding: 30px;
  }

  .filterIcon{
    width: 20px;
    height: 20px;
    margin-right: 5px;
  }

  .profilephoto{
      width:100%;
      border-top-left-radius: 25px;
      border-top-right-radius: 25px;
      height:200px;
    }

    figure.polaroid {
      width: 100%;
      height: 100%;
      background-color: white;
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
      margin-bottom: 25px;
      border-radius: 25px;
    }

    div.container {
      text-align: center;
      padding: 10px 20px;
    }
    .center-block{
      display: flex;
      margin: auto;
      max-width: 900px;
      flex-wrap: wrap;
      justify-content: space-evenly;
    }

    .posts{
        margin-top: 1%;
        width: 300px;
        height: 450px;
        margin: 2%;
        
    }

    .postgroup{
        /* margin-top: 3%; */
        padding-top: 3%;
        /* background-color: white; */
        height: 100%;
        position: relative;
        
        
    }

    .group{
        padding-top: 10px;
        padding-bottom: 3%;
        display: flex;
        width: 85%;
        flex-wrap: wrap;
        margin: auto;
        /* align-items: center;
        justify-content: center; */
        justify-content: space-evenly;
    }

    .header{
        color: white;
        margin-bottom:3%;
        font-weight: bold;
        text-align: center;
        font-size: 4vh;
    }

    .search
		{
      margin-top: 10px;
			display: inline-block;
      padding: 8px;
			width :90%;
      height:50px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-sizing: border-box;
		}
		
		
		.my-button
		{
      float: right;
			margin-top: 10px;
      background-color:#DB4914;
      color: white;
      margin-left:2px;
      width :100px;
      height: 50px;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-sizing: border-box;
		}

    .postcontent{
        text-align: center;
        color: black;
    }

    .title{
        color: black;
    }
</style>
