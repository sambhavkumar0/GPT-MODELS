from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.

def page1(request):
    region={"North":["Himachal Pradesh","Haryana","Punjab","Uttar Pradesh","Uttarakhand","Chandigarh","Delhi","Jammu and Kashmir","Ladakh"],"West":["Rajasthan","Gujarat","Dadra and Nagar Haveli and Daman and Diu","Maharashtra","Goa"],"East":["Bihar","West Bengal","Sikkim","Meghalaya","Assam","Arunachal Pradesh","Nagaland","Manipur","Mizoram","Tripura","Odisha"],"South":["Telangana","Karnataka","Andhra Pradesh","Kerala","Tamil Nadu","Puducherry","Andaman and Nicobar Islands","Lakshadweep"],"Middle":["Madhya Pradesh","Chhattisgarh","Jharkhand"]}
    
   
    if request.method=="POST":
        st=request.POST['state']
        shower=int(request.POST['shower'])
        flush=int(request.POST['flush'])
        dish=int(request.POST['dishwasher'])
        laun=int(request.POST['laundry'])
        diet=int(request.POST['diet'])
        local=int(request.POST['local'])
        showertime=8*shower
        flushtime=6*flush
        launtime=52*laun
        dishtime=9*dish
        totalwater=showertime+flushtime+launtime+dishtime+diet


        # for k,v in region.items():
        #     if(state in v ):
        if( totalwater>local ):
            messages.info(request,'Follow water conservation techniques')
        else:
            messages.info(request,'You have good waterfootprint')
        return render(request,'result.html',{'totalwater':totalwater})
        
    else:
        return render(request,'page1.html')
def resultpage(request):
    return render(request,'result.html')




