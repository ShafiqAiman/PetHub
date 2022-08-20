<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal modal-content"
        role="dialog" aria-labelledby="modalTitle" aria-describedby="modalDescription">
        <div class="modal-header">
          <h2 class="modal-title" id="exampleModalLongTitle">Filter</h2>
          <button type="button" class="close" @click="$emit('close', HasPet, age, minage, gender, occupation)" aria-label="Close modal" >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <h3 class="modalsection">Guardian Preferences</h3>
        <section class="modal-body" id="modalDescription">
          
          <div class="filter">
            <h5>Guardian Type: </h5>
            <input type="radio" value="Has A Pet" v-model="HasPet" id="haspet"/>
            <label style="margin-left:1%" for="haspet">Has A Pet</label><br>

            <input type="radio" value="Has No Pet" v-model="HasPet"  id="hasnopet"/>
            <label style="margin-left:1%" for="hasnopet">Has No Pet</label><br>

            <input type="radio" value="" v-model="HasPet"  id="hnope"/>
            <label style="margin-left:1%" for="hnope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Age : </h5>
            <input type="radio" value=25 v-model="age" @change="MinAge" id="25yo"/>
            <label style="margin-left:1%" for="25yo">18 - 25</label><br>

            <input type="radio" value=35 v-model="age" @change="MinAge" id="35yo"/>
            <label style="margin-left:1%" for="35yo">26 - 35</label><br>

            <input type="radio" value=500 v-model="age" @change="MinAge" id="45yo"/>
            <label style="margin-left:1%" for="45yo">> 35</label><br>

            <input type="radio" value=1000 v-model="age" @change="MinAge" id="anope"/>
            <label style="margin-left:1%" for="anope">I don't mind</label>
          </div>
          
          <div class="filter">
            <h5>Gender : </h5>
            <input type="radio" value="Male" v-model="gender" id="male"/>
            <label style="margin-left:1%" for="male">Male</label><br>

            <input type="radio" value="Female" v-model="gender"  id="female"/>
            <label style="margin-left:1%" for="female">Female</label><br>

            <input type="radio" value="" v-model="gender"  id="gnope"/>
            <label style="margin-left:1%" for="gnope">I don't mind</label>
          </div>

          <div class="filter">
            <h5>Occupation : </h5>
            <input type="radio" value="Student" v-model="occupation"  id="student"/>
            <label style="margin-left:1%" for="student">Student</label><br>

            <input type="radio" value="Working" v-model="occupation"  id="working"/>
            <label style="margin-left:1%" for="working">Working</label><br>

            <input type="radio" value="Not Working" v-model="occupation"  id="notworking"/>
            <label style="margin-left:1%" for="notworking">Not Working</label><br>

            <input type="radio" value="" v-model="occupation"  id="onope"/>
            <label style="margin-left:1%" for="onope">I don't mind</label>
          </div>

        </section>
        
        <div class="filterbtns">
          <button type="button" class="filter-btn" @click="$emit('close', HasPet, age, minage, gender, occupation)" aria-label="Close modal">
              Apply Filters
          </button>
          <button type="button" style="background-color:red;color:white;" class="filter-btn" @click="reset"  aria-label="Close modal">
              Clear Filters
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: 'ProfileModal',
    data(){
      return{
        HasPet:'',
        age:1000,
        minage:0,
        gender:'',
        religion:'',
        occupation:'',
        
      }
    },
    methods: {
      reset() {
        this.HasPet = '';
        this.age = 1000;
        this.minage = 0;
        this.gender = '';
        this.religion = '';
        this.occupation = '';
        this.pet = '';
        this.orientation = '';
        this.smoking = '';
        this.children = '';
        confirm("All filters are cleared! Please click 'Apply Filters' to proceed")
      },
      MinAge(){
        if (this.age == 25){
          this.minage = 18;
        }else if (this.age == 35){
          this.minage = 26;
        }else if (this.age == 500){
          this.minage = 36;
        }else{
          this.minage = 0;
        }
      }
    },
  };
</script>

<style scoped>
  
  .filterbtns{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }

  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    max-width: 55%;
    min-width: 280px;
    max-height: 80%;
    /* margin-left:20%; */
    margin-top: 5%;
    box-shadow: 2px 2px 20px 1px;
    border-radius: 15px;
    /* display: inherit; */
    flex-direction: column;
    overflow-y: auto;
    padding: 7px; 
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #175B5B;
    justify-content: space-between;
  }

  .modal-body {
      padding-top: 0;
      padding-bottom: 1%;
      display: flex;
      width: 90%;
      flex-wrap: wrap;
      margin: auto;
      justify-content: space-evenly;
  }

  .filter{
    margin-top: 1%;
    width: 200px;
    max-height: 500px;
    margin: 2%;
    text-align:left;
  }

  .filter-btn {
    margin-top: 10px;
    background-color:#fbd864;
    height: 50px;
    width: 100px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-sizing: border-box;
    padding: 5px;
    margin: 2%;
  }

  .modal-fade-enter,
  .modal-fade-leave-to {
    opacity: 0;
  }

  .modal-fade-enter-active,
  .modal-fade-leave-active {
    transition: opacity .5s ease;
  }
</style>