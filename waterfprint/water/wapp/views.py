from django.shortcuts import render

# Create your views here.

def page1(request):
    region={"North":["Himachal Pradesh","Haryana","Punjab","Uttar Pradesh","Uttarakhand","Chandigarh","Delhi","Jammu and Kashmir","Ladakh"],"West":["Rajasthan","Gujarat","Dadra and Nagar Haveli and Daman and Diu","Maharashtra","Goa"],"East":["Bihar","West Bengal","Sikkim","Meghalaya","Assam","Arunachal Pradesh","Nagaland","Manipur","Mizoram","Tripura","Odisha"],"South":["Telangana","Karnataka","Andhra Pradesh","Kerala","Tamil Nadu","Puducherry","Andaman and Nicobar Islands","Lakshadweep"],"Middle":["Madhya Pradesh","Chhattisgarh","Jharkhand"]}
    
    state=request.POST['state']
    shower=request.POST['shower']
    flush=request.POST['flush']
    dish=request.POST['dishwasher']
    laun=request.POST['laundry']
    diet=request.POST['diet']
    if request.method=="POST":
        

    return render(request,'page1.html')