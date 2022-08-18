<template>
    
    <nav class="navbar sticky-top navbar-expand-md navbar-light">
        <a class="navbar-brand" href="#">
          <router-link to="/" style="color:white;margin-left:10px;text-decoration:none;" class="navbar-item">
            <img src="../assets/pethub.png" width="30" height="30"  class="logo d-inline-block align-top" alt="">
            PetHub
            </router-link>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation" @click="showMobileMenu = !showMobileMenu">
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
                      <!-- <li class="nav-item">
                        
                        <router-link to="/Pricing" style="color:white;margin-left:10px" class="nav-link">Pricing</router-link>
                      </li> -->
                      <li class="nav-item">
                        <!-- <a href="#" class="nav-link" style="color:white;">Create a Listing</a> -->
                        <router-link to="/signin" style="color:white;margin-left:10px" class="nav-link">Sign In</router-link>
                      </li>
                      <li class="nav-item">
                        <router-link to="/signup" style="color:white;margin-left:10px" class="nav-link">Sign Up</router-link>
                        <!-- <a href="#" class="nav-link" style="color:white;">Messages</a> -->
                      </li>
                      
                    </ul>
                    <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item">Account Settings</a>
                        <a class="dropdown-item">Sign Out</a>
                    </div>
                </li>
            </ul>

        </div>
    </nav>
</template>

<script>
export default {
    name:'VisitorNav',
    data(){
      return{
        
      }
    }
}
</script>
<style scoped>

  .logo{
    border-radius: 50%;
    object-fit: cover;
  }
</style>