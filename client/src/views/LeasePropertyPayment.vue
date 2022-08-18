<template>
    <div class="paymentpage">
        <h1 style="text-align:center;margin-top:3%;margin-bottom:2%">Checkout</h1>
        <div class="container">
            <div class="row" style="padding:1%">
                <div class="col-md-8 pt-3">
                    <div class="left">
                    <!-- <h2>Review</h2><br> -->
                        <img class="propertyphoto" :src="photo1URL"  style="margin-top:5%">
                        <h3 style="margin-left: 6%;margin-top: 3%;">Property Details</h3>
                        <div class="property">
                            <div class="leftdetails">
                                
                                <p class="details">Property Type of Host</p>
                                <p>{{ leasedproperty.typeOfHost }}</p>

                                <p class="details">Property Name</p>
                                <p>{{ leasedproperty.nameOfListing }}</p>

                                <p class="details">Property Address</p>
                                <p>{{ leasedproperty.address }}, <br>{{ leasedproperty.city }} </p>

                                <p class="details">Property Type of Listing</p>
                                <p>{{ leasedproperty.typeOfListing }}</p>

                                <p class="details">Property Type of Room</p>
                                <p>{{ leasedproperty.typeOfRoom }}</p>

                                <p class="details">Property Amenities</p>
                                <div style="width:100%;margin-left: 6%">
                                    <ul>
                                        <li v-if="leasedproperty.aircond_value">Air conditioning</li>
                                        <li v-if="leasedproperty.furnished_value">Furnished</li>
                                    
                                        <li v-if="leasedpropertywifi_value" >Wifi</li>
                                        <li v-if="leasedproperty.swimmingpool_value" >Swimming pool</li>
                                    
                                        <li v-if="leasedproperty.gym_value" >Gym</li>
                                        <li v-if="leasedproperty.parking_value" >Parking</li>
                                    </ul>
                                </div><br>
                            </div>

                            <div class="rightdetails">
                                <p class="details">Property No. of Bedrooms</p>
                                <p>{{ leasedproperty.totalBedrooms }}</p>

                                <p class="details">Property No. of Bathrooms</p>
                                <p>{{ leasedproperty.totalBathrooms }}</p>

                                <p class="details">Property Description</p>
                                <p>{{ leasedproperty.description }}</p>

                                <p class="details">Property Rental</p>
                                <p>RM {{ leasedproperty.monthlyRent }}/month</p>

                                <p class="details">Property Rental Deposit</p>
                                <p>RM {{ leasedproperty.deposit }}</p>

                            </div>
                            
                        </div>

                        <h3 style="margin-left: 6%;">Property Preferences</h3>
                        <div class="property">
                            <div class="leftdetails">
                                
                                <p class="details">Preferred Gender</p>
                                <template v-if="leasedproperty.Pgender">
                                    <p>{{ leasedproperty.Pgender }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>

                                <p class="details">Preferred Sex Orientation</p>
                                <template v-if="leasedproperty.Psexorientation">
                                    <p>{{ leasedproperty.Psexorientation }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>

                                <p class="details">Preferred Age</p>
                                <template v-if="leasedproperty.Page">
                                    <p>{{ leasedproperty.Page }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>

                                <p class="details">Preferred Religion</p>
                                <template v-if="leasedproperty.Preligion">
                                    <p>{{ leasedproperty.Preligion }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>
                            </div>

                            <div class="rightdetails">
                                <p class="details">Preferred Occupation</p>
                                <template v-if="leasedproperty.Occupation">
                                    <p>{{ leasedproperty.Poccupation }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>

                                <p class="details">Preferred Pet Status</p>
                                <template v-if="leasedproperty.Ppet">
                                    <p>{{ leasedproperty.Ppet }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>

                                <p class="details">Preferred Smoking Status</p>
                                <template v-if="leasedproperty.Psmoking">
                                    <p>{{ leasedproperty.Psmoking }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>

                                <p class="details">Preferred Children Status</p>
                                <template v-if="leasedproperty.Pchildren">
                                    <p>{{ leasedproperty.Pchildren }}</p> 
                                </template>
                                <template v-else>
                                    <p>Flexible</p>
                                </template>

                            </div>
                        </div>

                        <div style="width:100%">
                            <button class="editpropertybtn">Edit</button>
                        </div>
                            
                        

                    </div>
                </div>  
                <div class="col-md-4 py-3">
                    <div class="right">
                        <h2>Payment</h2><br>
                        <div class="paymentdetails">
                            <p>Basic Plan</p>
                            <p>Service Fees</p>
                            <p>Discount</p>  
                            <p>Total</p>
                        </div>

                        <div class="paymentdetails">
                            <p class="fees">{{(total-transactionfees).toFixed(2)}}</p>
                            <p class="fees">{{transactionfees}}</p>
                            <p class="fees">-{{ (total-0).toFixed(2) }}</p>
                            <p style="text-align:right;font-weight: bold;">MYR {{(total-total).toFixed(2)}}</p>
                        </div>

                        <button class="submitbtn">Submit</button>
                        
                        <!-- <div id="paypal-button-container" style="pointer-events: none;"></div> -->
                </div> 
                </div>
                
            </div>
        </div>
        
        
    </div>
    
</template>

<script>
export default {
    name:'LeastPayment',
    data(){
      return{
        total : 0,
        transactionfees:'',
        leasedproperty:{},
        uploadphoto1: null,
        uploadphoto2: null,
        uploadphoto3: null,
        uploadphoto4: null,
        uploadphoto5: null,
        photo1URL: ''
      }
    },
    mounted(){
        this.paypalpayment();
        this.getLeasedProperty();
    },
    created() {
    this.total = localStorage.total;
    this.transactionfees = ((0.049*this.total)+2).toFixed(2) //https://www.paypal.com/my/webapps/mpp/ua/recpymt-full?locale.x=en_MY
    },
    methods:{
        getLeasedProperty(){
            this.leasedproperty = JSON.parse(sessionStorage.listedplace);

            this.photo1URL= sessionStorage.picture1

            this.uploadphoto1 = this.dataURLtoFile(sessionStorage.picture1, sessionStorage.picture1name)
            console.log(this.uploadphoto1)

            
        
            
        },
        paypalpayment(){
            
        //     let Total = this.total
        //     paypal.Buttons({
                
        //         // Set up the transaction
        //         createOrder: function(data, actions) {
        //             return actions.order.create({
        //                 purchase_units: [{
        //                     amount: {
        //                         value: Total
        //                     }
        //                 }]
        //             });
        //         },

        //         // Finalize the transaction
        //         onApprove: function(data, actions) {
        //             return actions.order.capture().then(function(details) {
        //                 // Show a success message to the buyer
        //                 alert('Transaction completed by ' + details.payer.name.given_name + '!');
        //             });
        //         }


        // }).render('#paypal-button-container');
        
        },
        dataURLtoFile(dataurl, filename) {
            var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
            bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
            while(n--){
            u8arr[n] = bstr.charCodeAt(n);
            }
        return new File([u8arr], filename, {type:mime});
        }
           
    }
}
</script>
<style scoped>
    .paymentpage{
        position: relative;
	    min-height: 100vh;
        background-color: white;
        
    }
    .left{
        padding: 2%;
        box-shadow: 12px 12px 22px grey;
        margin-bottom: 5%;
    }
    .propertyphoto{
        width: 60%;
        display: block;
        margin: 0 auto;
        
    }
    .property{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-evenly;
        padding: 6%;
        min-height: 450px;
        
    }
    .leftdetails{
        
        width: 300px;
        float: left;
    }
    .details{
        font-weight: bold;
    }
    .rightdetails{
        width: 300px;
        float: right;
    }
    .right{
        padding: 5%;
        box-shadow: 12px 12px 22px grey;
    }
    .paymentdetails{
        width: 50%;
        float: left;
        
    }
    .fees{
        text-align: right;
    }

    .submitbtn{
        background-color:#fbd864;
        height: 50px;
        width: 90%;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-sizing: border-box;
        padding: 5px;
        display: block;
        margin: 0 auto;
    }
    .editpropertybtn{
        background-color:#fbd864;
        height: 50px;
        width: 100px;
        border: 1px solid #ccc;
        border-radius: 10px;
        box-sizing: border-box;
        padding: 5px;
        display: block;
        margin: 0 auto;
        }
    
</style>