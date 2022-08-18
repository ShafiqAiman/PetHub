<template>
    <footer>
          <div class="footer py-3 text-center">
            <img src="../assets/pethub.png" width="50" height="50" class="logo d-inline-block align-top" alt="">
            <p>@2022: PetHub</p>
            <p>Terms of Use | Privacy Policy</p>
          </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer',
}
</script>

<style scoped>
    footer{
      background-color: #DB4914;
      color: white;
      
    }

  .logo{
    border-radius: 50%;
    object-fit: cover;
  }
</style>