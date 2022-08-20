<template>
  <div class="wholepage">
    <header class="jumbotron jumbotron-fluid text-center">
      <h3 class="header">Find Guardian</h3>
      <form action="">
            <div class="center-block">
                <SearchAutocomplete
                  :items="names"
                  @selected="selectedResult"
                  
                />

                <ProfileModal v-show="isModalVisible" @close="closeModal"
                />
            </div>
        </form>
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
            
            <div class="posts" v-for="guardian in filteredPosts.slice((currentPage-1) * perPage,(currentPage-1) * perPage+perPage)" :key="guardian.id">
              <router-link to="" style="text-decoration:none;" @click="newWindow(guardian.get_absolute_url)">
                <figure class="polaroid">
                  <template v-if="guardian.get_profilephoto==''">
                    <img src="../assets/defaultprofilepicture.png" class="profilephoto">
                  </template>
                  <template v-else>
                    <img :src="guardian.get_profilephoto" class="profilephoto">
                  </template>
                    <div class="container">
                      <div style="height:80px">
                        <h3 class="title">{{ guardian.fullname }}, {{ guardian.age }}</h3>
                      </div>
                      
                      
                      <b class="profilepostcontent"><mark>{{ guardian.HasPet }}</mark></b><br><br>
                      <p class="profilepostcontent" style="font-style:italic">{{ guardian.occupation }}</p>
                      
                      <div style="height:60px">
                      <template v-if="guardian.aboutme.length > 75">
                          <p class="profilepostcontent" style="font-size: 14px;font-style:italic">{{ guardian.aboutme.substring(0,75)+'...' }}</p>
                      </template>
                      <template v-else>
                          <p class="profilepostcontent" style="font-size: 14px;font-style:italic">{{ guardian.aboutme }}</p>
                      </template>
                        
                      </div>
                    </div>
                </figure>
              </router-link>
            </div>
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
        <!-- <Footer /> -->
        
  </div>
</template>

<script>
import SearchAutocomplete from '../components/SearchAutocomplete.vue'
import ProfileModal from '../components/ProfileModal.vue';
import Footer from '../components/Footer.vue'
import axios from 'axios'
export default {
  name: 'FindGuardian',
  components: {
      ProfileModal,
      Footer,
      SearchAutocomplete,
    },
  data(){
    return{
      user: {},
      isModalVisible: false,
      search:'',
      Guardians:[],
      names:[],

      perPage:6,
      currentPage: 1,
      TotalPages: 1,

      HasPet:'',
      Age:1000,
      MinAge:0,
      Gender:'',
      Occupation:'',
      
      
      

      filterhaspet:'',
      filterage:'',
      filtergender:'',
      filteroccupation:'',
      filterSearch:'',
      filteroutmyprofile: '',
      filteroutdefault: '',

    }
  },
  mounted(){
    
    this.getUser()
    this.getHouses()
    
    document.title = 'PetHub | Find Guardian' //Title of the page
    
    
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

      await axios  
         .get('/api/guardians') //to get data that is converted by Django REST with the help of Axios
        .then(response => {
          this.Guardians = response.data
          for (var i = 0; i < this.Guardians.length; i++) {
            this.names.push(this.Guardians[i].fullname)
            this.names.push(this.Guardians[i].preferredcity)
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
      closeModal(HasPet, age, minage, gender, occupation) {
        this.isModalVisible = false;
        this.HasPet = HasPet;
        this.Age = age;
        this.MinAge = minage;
        this.Gender = gender;
        this.Occupation = occupation;

      },
      selectedResult(e){
        this.search = e;
      },

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
                    

                })
                .catch(error => {
                    console.log(error)
                })

                
        },
        newWindow(url){
        window.open(url)
      }
      
    
  },
  computed:{
    filteredPosts(){

      
        
      //Filter Results (guardian Type)                             //Data from database                   //Data from Modal
      this.filterhaspet = this.Guardians.filter(guardian => guardian.HasPet.toLowerCase().includes(this.HasPet.toLowerCase()))

      //Filter Results (Age) 
      this.filterage = this.filterhaspet.filter(guardian => (guardian.age <= this.Age) && (guardian.age >= this.MinAge))

      //Filter Results (Gender)
      this.filtergender = this.filterage.filter(guardian => guardian.gender.includes(this.Gender))


      //Filter Results (Occupation)
      this.filteroccupation = this.filtergender.filter(guardian => guardian.occupation.toLowerCase().includes(this.Occupation.toLowerCase()))

      
      this.filteroutmyprofile = this.filteroccupation.filter(guardian => guardian.id != this.user.id)

      this.filteroutdefault = this.filteroutmyprofile.filter(guardian => guardian.fullname != "Buddy")

      // Filter Results (Search)
      this.filterSearch = this.filteroutdefault.filter(guardian => guardian.fullname.toLowerCase().includes(this.search.toLowerCase()) 
      || guardian.preferredcity.toLowerCase().includes(this.search.toLowerCase())
      )

      //Return Final Results
      this.TotalPages = Math.ceil(this.filterSearch.length/this.perPage)
      
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
      object-fit: cover;
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
        padding: 3%;
        margin: auto;
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

    .profilepostcontent{
        text-align: center;
        color: black;
    }

    .title{
        color: black;
    }
</style>
