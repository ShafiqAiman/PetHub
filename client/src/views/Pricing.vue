<template>
    <div class="container">
        <div class="wrapper">
            <div class="row">
                <div class="col-xs-1 col-md-12">
                    <div class="intro">
                        <h1>Choose the right plan for you.</h1>
                        <p>Keep track of your houses with our packages. Expand your business with us.</p>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-xs-4 col-md-4"><BasicPlanCard/></div>
                <div class="col-xs-4 col-md-4"><SilverPlanCard/></div>
                <div class="col-xs-4 col-md-4"><GoldPlanCard/></div>
            </div>
        </div>
    </div>
</template>

<script>
import Footer from '../components/Footer.vue'
import BasicPlanCard from '../components/SubscriptionPlans/BasicPlanCard.vue'
import GoldPlanCard from '../components/SubscriptionPlans/GoldPlanCard.vue'
import SilverPlanCard from '../components/SubscriptionPlans/SilverPlanCard.vue'
export default {
    name:'ListPlan',
    components:
    {
        Footer,
        BasicPlanCard,
        GoldPlanCard,
        SilverPlanCard
    },
    data()
    {
        return{
        
        }
    },
    mounted(){
        document.title = 'Bed & Buddies | Lease Plan' //Title of the page
    },
    methods:
    {
        payment(){
            this.$router.push({path: '/leasepayment', })
        },
    },
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
h2{
    font-family: "Montserrat", sans-serif;
    font-weight: 600;
    /* font-size:3vw; */
}
p{
    font-family: "Montserrat", sans-serif;
    
}
</style>