from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from mainapp.models import District, SubDistrict,Neighbor, SubNeighbor,identification,PropertyMap,PlotNo,Plotmap, Purchaseinfo,Notary,Landtype,Parcel,Sellerinfo,Dhaxalayaal,DhaxalSubDoc,SupportingDOC,BussinessRegistration,BussinessRegistrator,BussinessStatus,Coordinates,KalawarejinSubDoc,PropertyRevenu,BussinessRevenu,Charges,Currencies,ChagreType
from .forms import Dhaxalform, DistrictForm ,SubDistrictForm, NeighborForm, SubNeigborForm,identificationForm,Plotmapform,Plotnoform,PropertyMapForm, Purchaseinfoform,Landtypeform , Notaryform, Parcelform,sellerinfoform,Dhaxalform,DhaxalSubForm,SupportingDocForm,BussinessRegform,BussinessRegistratorform,Bussinessstatusform,Coordinateform,kalawarejinform,PRform,BReform,Chargeform,Currenciesform,ChagreTypeform

# Create your views here.
def home(request):
     district = District.objects.all()
     context = {'district':district}
     return render(request, "home.html" , context)
def DistrictFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = DistrictForm()
            else:
             district = District.objects.get(pk=id)
             form = DistrictForm(instance=district)
            return render(request, "district_form.html", {'form': form})
      else:
           
           if id == 0:
                form = DistrictForm(request.POST)
           else:
              district = District.objects.get(pk=id)
              form =  DistrictForm(request.POST,instance= district)
           if form.is_valid():
             form.save()
             return redirect('/')

def didelete(request,id):
    employee = District.objects.get(pk=id)
    employee.delete()
    return redirect('/')
def subDistrictFrom(request, id=0):
        if request.method == "GET":
            if id == 0:
                  form = SubDistrictForm()
            else:
             subdistrict = SubDistrict.objects.get(pk=id)
             form = SubDistrictForm(instance = subdistrict)
            return render(request, "subdistrictform.html", {'form': form})
        else:
           
           if id == 0:
                form = SubDistrictForm(request.POST)
           else:
              subdistrict = SubDistrict.objects.get(pk=id)
              form =  SubDistrictForm(request.POST,instance = subdistrict)
           if form.is_valid():
              form.save()
              return redirect('/subdistricthome')
def subdistricthome(request):
     Subdistrict = SubDistrict.objects.all()
     context = {'subdistrict':Subdistrict}
     return render(request, "subdistricthome.html" , context)
def sddelete(request,id):
    subdistrict = SubDistrict.objects.get(pk=id)
    subdistrict.delete()
    return redirect('/subdistricthome')
def neighborhome(request):
     neighbor = Neighbor.objects.all()
     context = {'neighbor':neighbor}
     return render(request, "neighborhome.html" , context)
def neighborFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = NeighborForm()
            else:
             neighbor = Neighbor.objects.get(pk=id)
             form = NeighborForm(instance=neighbor)
            return render(request, "neighborform.html", {'form': form})
      else:
           
           if id == 0:
                form = NeighborForm(request.POST)
           else:
              district = Neighbor.objects.get(pk=id)
              form =  NeighborForm(request.POST,instance= district)
           if form.is_valid():
             form.save()
             return redirect('/neighborhome')

def ndelete(request,id):
    employee = Neighbor.objects.get(pk=id)
    employee.delete()
    return redirect('/neighborhome')
def subneighborhome(request):
     sneighbor = SubNeighbor.objects.all()
     context = {'sneighbor':sneighbor}
     return render(request, "subneighborhome.html" , context)
def subneighborFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = SubNeigborForm()
            else:
             sneighbor = SubNeighbor.objects.get(pk=id)
             form = SubNeigborForm(instance=sneighbor)
            return render(request, "subneighborform.html", {'form': form})
      else:
           
           if id == 0:
                form = SubNeigborForm(request.POST)
           else:
              sneighbor = SubNeighbor.objects.get(pk=id)
              form =  SubNeigborForm(request.POST,instance= sneighbor)
           if form.is_valid():
             form.save()
             return redirect('/subneighborhome')

def sndelete(request,id):
    employee = SubNeighbor.objects.get(pk=id)
    employee.delete()
    return redirect('/subneighborhome')
def identificationhome(request):
     ident = identification.objects.all()
     context = {'ident':ident}
     return render(request, "identificationhome.html" , context)
def identificationFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = identificationForm()
            else:
             ident = identification.objects.get(pk=id)
             form = identificationForm(instance=ident)
            return render(request, "identificationform.html", {'form': form})
      else:
           
           if id == 0:
                form = identificationForm(request.POST, request.FILES)
           else:
              sneighbor = identification.objects.get(pk=id)
              form =  identificationForm(request.POST, request.FILES,instance= sneighbor)
           if form.is_valid():
             form.save()
             return redirect('/identificationhome')

def identificationdelete(request,id):
    employee = identification.objects.get(pk=id)
    employee.delete()
    return redirect('/identificationhome')
def PMhome(request):
     PM = PropertyMap.objects.all()
     context = {'PM':PM}
     return render(request, "propertymaphome.html" , context)
def PMFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = PropertyMapForm()
            else:
             ident = PropertyMap.objects.get(pk=id)
             form = PropertyMapForm(instance=ident)
            return render(request, "propertymapform.html", {'form': form})
      else:
           
           if id == 0:
                form = PropertyMapForm(request.POST,request.FILES)
           else:
              sneighbor = PropertyMap.objects.get(pk=id)
              form =  PropertyMapForm(request.POST, request.FILES,instance= sneighbor,)
           if form.is_valid():
             form.save()
             return redirect('/PMhome')

def PMdelete(request,id):
    employee = PropertyMap.objects.get(pk=id)
    employee.delete()
    return redirect('/PMhome')
def PNhome(request):
     PN = PlotNo.objects.all()
     context = {'PN':PN}
     return render(request, "PlotNohome.html" , context)
def PNFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Plotnoform()
            else:
             ident = PlotNo.objects.get(pk=id)
             form = Plotnoform(instance=ident)
            return render(request, "PlotNofrom.html", {'form': form})
      else:
           
           if id == 0:
                form = Plotnoform(request.POST,request.FILES)
           else:
              sneighbor = PlotNo.objects.get(pk=id)
              form =  Plotnoform(request.POST, request.FILES,instance= sneighbor,)
           if form.is_valid():
             form.save()
             return redirect('/PNhome')

def PNdelete(request,id):
    employee = PlotNo.objects.get(pk=id)
    employee.delete()
    return redirect('/PNhome')
def PLMhome(request):
     PLM = Plotmap.objects.all()
     context = {'PLM':PLM}
     return render(request, "plotmaphome.html" , context)
def PLMFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Plotmapform()
            else:
             ident = Plotmap.objects.get(pk=id)
             form = Plotmapform(instance=ident)
            return render(request, "plotmapform.html", {'form': form})
      else:
           
           if id == 0:
                form = Plotmapform(request.POST,request.FILES)
           else:
              sneighbor = Plotmap.objects.get(pk=id)
              form =  Plotmapform(request.POST, request.FILES,instance= sneighbor,)
           if form.is_valid():
             form.save()
             return redirect('/PLMhome')

def PLMdelete(request,id):
    employee = Plotmap.objects.get(pk=id)
    employee.delete()
    return redirect('/PLMhome')
def PIhome(request):
     PI= Purchaseinfo.objects.all()
     context = {'PI':PI}
     return render(request, "purchaseinfohome.html" , context)
def PIFrom(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Purchaseinfoform()
            else:
             ident = Purchaseinfo.objects.get(pk=id)
             form = Purchaseinfoform(instance=ident)
            return render(request, "purchaseinfoform.html", {'form': form})
      else:
           
           if id == 0:
                form = Purchaseinfoform(request.POST,request.FILES)
           else:
              sneighbor = Purchaseinfo.objects.get(pk=id)
              form =  Purchaseinfoform(request.POST, request.FILES,instance= sneighbor,)
           if form.is_valid():
             form.save()
             return redirect('/PIhome')

def PIdelete(request,id):
    employee = Purchaseinfo.objects.get(pk=id)
    employee.delete()
    return redirect('/PIhome')
def Nohome(request):
     No = Notary.objects.all()
     context = {'No':No}
     return render(request, "Notrayhome.html" , context)
def NoForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Notaryform()
            else:
             ident = Notary.objects.get(pk=id)
             form = Notaryform(instance=ident)
            return render(request, "Notrayform.html", {'form': form})
      else:
           
           if id == 0:
                form = Notaryform(request.POST,request.FILES)
           else:
              sneighbor =Notary.objects.get(pk=id)
              form =  Notaryform(request.POST, request.FILES,instance= sneighbor,)
           if form.is_valid():
             form.save()
             return redirect('/Nohome')

def Nodelete(request,id):
    employee = Notary.objects.get(pk=id)
    employee.delete()
    return redirect('/Nohome')
def Lanhome(request):
     Lan = Landtype.objects.all()
     context = {'Lan':Lan}
     return render(request, "Landtypehome.html" , context)
def LanForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Landtypeform()
            else:
             ident = Landtype.objects.get(pk=id)
             form = Landtypeform(instance=ident)
            return render(request, "Landtypeform.html", {'form': form})
      else:
           
           if id == 0:
                form = Landtypeform(request.POST,request.FILES)
           else:
              sneighbor =Landtype.objects.get(pk=id)
              form =  Landtypeform(request.POST, request.FILES,instance= sneighbor,)
           if form.is_valid():
             form.save()
             return redirect('/Lanhome')

def Landelete(request,id):
    employee = Landtype.objects.get(pk=id)
    employee.delete()
    return redirect('/Lanhome')
def phome(request):
     P = Parcel.objects.all()
     context = {'P':P}
     return render(request, "parcelhome.html" , context)
def pForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Parcelform()
            else:
             ident = Parcel.objects.get(pk=id)
             form = Parcelform(instance=ident)
            return render(request, "parcelform.html", {'form': form})
      else:
           
           if id == 0:
                form = Parcelform(request.POST)
           else:
              sneighbor = Parcel.objects.get(pk=id)
              form = Parcelform(request.POST,instance= sneighbor)
           if form.is_valid():
              form.save()
              return redirect('/phome')

def pdelete(request,id):
    employee = Parcel.objects.get(pk=id)
    employee.delete()
    return redirect('/phome')

def slhome(request):
     Sl = Sellerinfo.objects.all()
     context = {'Sl':Sl}
     return render(request, "sellerinfohome.html" , context)
def slForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = sellerinfoform()
            else:
             ident = Sellerinfo.objects.get(pk=id)
             form = sellerinfoform(instance=ident)
            return render(request, "sellerinfoform.html", {'form': form})
      else:
           
           if id == 0:
                form = sellerinfoform(request.POST,request.FILES)
           else:
              sneighbor = Sellerinfo.objects.get(pk=id)
              form = sellerinfoform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/slhome')

def sldelete(request,id):
    employee = Sellerinfo.objects.get(pk=id)
    employee.delete()
    return redirect('/slhome')
def dhome(request):
     Da = Dhaxalayaal.objects.all()
     context = {'Da':Da}
     return render(request, "Dhaxalayaalhome.html" , context)
def dForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Dhaxalform()
            else:
             ident = Dhaxalayaal.objects.get(pk=id)
             form = Dhaxalform(instance=ident)
            return render(request, "Dhaxalayaalform.html", {'form': form})
      else:
           
           if id == 0:
                form = Dhaxalform(request.POST)
           else:
              sneighbor = Dhaxalayaal.objects.get(pk=id)
              form = Dhaxalform(request.POST,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/dhome')

def ddelete(request,id):
    employee = Dhaxalayaal.objects.get(pk=id)
    employee.delete()
    return redirect('/dhome')
def dshome(request):
     Da = DhaxalSubDoc.objects.all()
     context = {'Da':Da}
     return render(request, "Dhaxalsubhome.html" , context)
def dsForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = DhaxalSubForm()
            else:
             ident = DhaxalSubDoc.objects.get(pk=id)
             form = DhaxalSubForm(instance=ident)
            return render(request, "Dhaxayaalsubform.html", {'form': form})
      else:
           
           if id == 0:
                form = DhaxalSubForm(request.POST,request.FILES,)
           else:
              sneighbor = DhaxalSubDoc.objects.get(pk=id)
              form = DhaxalSubForm(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/dshome')

def dsdelete(request,id):
    employee = DhaxalSubDoc.objects.get(pk=id)
    employee.delete()
    return redirect('/dshome')
def sphome(request):
     Da = SupportingDOC.objects.all()
     context = {'Da':Da}
     return render(request, "supportingdochome.html" , context)
def spForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = SupportingDocForm()
            else:
             ident = SupportingDOC.objects.get(pk=id)
             form = SupportingDocForm(instance=ident)
            return render(request, "supportingdocform.html", {'form': form})
      else:
           
           if id == 0:
                form = SupportingDocForm(request.POST,request.FILES,)
           else:
              sneighbor = SupportingDOC.objects.get(pk=id)
              form = SupportingDocForm(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/sphome')

def spdelete(request,id):
    employee = SupportingDOC.objects.get(pk=id)
    employee.delete()
    return redirect('/sphome')
def bphome(request):
     Da = BussinessRegistration.objects.all()
     context = {'Da':Da}
     return render(request, "BussinessReghome.html" , context)
def bForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = BussinessRegform()
            else:
             ident = BussinessRegistration.objects.get(pk=id)
             form = BussinessRegform(instance=ident)
            return render(request, "BussinessRegform.html", {'form': form})
      else:
           
           if id == 0:
                form = BussinessRegform(request.POST,request.FILES,)
           else:
              sneighbor = BussinessRegistration.objects.get(pk=id)
              form = BussinessRegform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/bhome')

def bdelete(request,id):
    employee = BussinessRegistration.objects.get(pk=id)
    employee.delete()
    return redirect('/bhome')
def brhome(request):
     Da = BussinessRegistrator.objects.all()
     context = {'Da':Da}
     return render(request, "BRhome.html" , context)
def brForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = BussinessRegistratorform()
            else:
             ident = BussinessRegistrator.objects.get(pk=id)
             form = BussinessRegistratorform(instance=ident)
            return render(request, "BRform.html", {'form': form})
      else:
           
           if id == 0:
                form = BussinessRegistratorform(request.POST,request.FILES,)
           else:
              sneighbor = BussinessRegistrator.objects.get(pk=id)
              form = BussinessRegistratorform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/brhome')

def brdelete(request,id):
    employee = BussinessRegistrator.objects.get(pk=id)
    employee.delete()
    return redirect('/brhome')
def bshome(request):
     Da = BussinessStatus.objects.all()
     context = {'Da':Da}
     return render(request, "BShome.html" , context)
def bsForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Bussinessstatusform()
            else:
             ident = BussinessStatus.objects.get(pk=id)
             form = Bussinessstatusform(instance=ident)
            return render(request, "BSform.html", {'form': form})
      else:
           
           if id == 0:
                form = Bussinessstatusform(request.POST,request.FILES,)
           else:
              sneighbor = BussinessStatus.objects.get(pk=id)
              form = Bussinessstatusform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/bshome')

def bsdelete(request,id):
    employee = BussinessStatus.objects.get(pk=id)
    employee.delete()
    return redirect('/bshome')
def brdelete(request,id):
    employee = BussinessRegistrator.objects.get(pk=id)
    employee.delete()
    return redirect('/brhome')
def chome(request):
     Da = Coordinates.objects.all()
     context = {'Da':Da}
     return render(request, "coordinatehome.html" , context)
def cForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Coordinateform()
            else:
             ident = Coordinates.objects.get(pk=id)
             form = Coordinateform(instance=ident)
            return render(request, "coordinateform.html", {'form': form})
      else:
           
           if id == 0:
                form = Coordinateform(request.POST,request.FILES,)
           else:
              sneighbor = Coordinates.objects.get(pk=id)
              form = Coordinateform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/chome')

def cdelete(request,id):
    employee = Coordinates.objects.get(pk=id)
    employee.delete()
    return redirect('/chome')
def khome(request):
     Da = KalawarejinSubDoc.objects.all()
     context = {'Da':Da}
     return render(request, "kalawrejinhome.html" , context)
def kForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = kalawarejinform()
            else:
             ident = KalawarejinSubDoc.objects.get(pk=id)
             form = kalawarejinform(instance=ident)
            return render(request, "kalawrejinform.html", {'form': form})
      else:
           
           if id == 0:
                form = kalawarejinform(request.POST,request.FILES,)
           else:
              sneighbor = KalawarejinSubDoc.objects.get(pk=id)
              form = kalawarejinform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/khome')

def kdelete(request,id):
    employee = KalawarejinSubDoc.objects.get(pk=id)
    employee.delete()
    return redirect('/khome')
def prhome(request):
     Da = PropertyRevenu.objects.all()
     context = {'Da':Da}
     return render(request, "PRhome.html" , context)
def prForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = PRform()
            else:
             ident = PropertyRevenu.objects.get(pk=id)
             form = PRform(instance=ident)
            return render(request, "PRform.html", {'form': form})
      else:
           
           if id == 0:
                form = PRform(request.POST,request.FILES,)
           else:
              sneighbor = PropertyRevenu.objects.get(pk=id)
              form = PRform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/prhome')

def prdelete(request,id):
    employee = PropertyRevenu.objects.get(pk=id)
    employee.delete()
    return redirect('/prhome')
def brehome(request):
     Da = BussinessRevenu.objects.all()
     context = {'Da':Da}
     return render(request, "Brevenuehome.html", context)
def breForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = BReform()
            else:
             ident = BussinessRevenu.objects.get(pk=id)
             form = BReform(instance=ident)
            return render(request, "Brevenueform.html", {'form': form})
      else:
           
           if id == 0:
                form = BReform(request.POST,request.FILES,)
           else:
              sneighbor = BussinessRevenu.objects.get(pk=id)
              form = BReform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/brehome')

def bredelete(request,id):
    employee = BussinessRevenu.objects.get(pk=id)
    employee.delete()
    return redirect('/brehome')
def cuhome(request):
     Da = Currencies.objects.all()
     context = {'Da':Da}
     return render(request, "currencieshome.html", context)
def cuForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Currenciesform()
            else:
             ident = Currencies.objects.get(pk=id)
             form = Currenciesform(instance=ident)
            return render(request, "currenciesform.html", {'form': form})
      else:
           
           if id == 0:
                form = Currenciesform(request.POST,request.FILES,)
           else:
              sneighbor = Currencies.objects.get(pk=id)
              form = Currenciesform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/cuhome')

def cudelete(request,id):
    employee = Currencies.objects.get(pk=id)
    employee.delete()
    return redirect('/cuhome')
def chhome(request):
     Da = Charges.objects.all()
     context = {'Da':Da}
     return render(request, "chargehome.html", context)
def chForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = Chargeform()
            else:
             ident = Charges.objects.get(pk=id)
             form = Chargeform(instance=ident)
            return render(request, "chargeform.html", {'form': form})
      else:
           
           if id == 0:
                form = Chargeform(request.POST,request.FILES,)
           else:
              sneighbor = Charges.objects.get(pk=id)
              form = Chargeform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/chhome')

def chdelete(request,id):
    employee = Charges.objects.get(pk=id)
    employee.delete()
    return redirect('/chhome')
def cthome(request):
     Da = ChagreType.objects.all()
     context = {'Da':Da}
     return render(request, "chargetypehome.html", context)
def ctForm(request, id=0):
      if request.method == "GET":
            if id == 0:
              form = ChagreTypeform()
            else:
             ident = ChagreType.objects.get(pk=id)
             form = ChagreTypeform(instance=ident)
            return render(request, "chargetypeform.html", {'form': form})
      else:
           
           if id == 0:
                form = ChagreTypeform(request.POST,request.FILES,)
           else:
              sneighbor = ChagreType.objects.get(pk=id)
              form = ChagreTypeform(request.POST,request.FILES,instance= sneighbor,)
           if form.is_valid():
              form.save()
           return redirect('/cthome')

def ctdelete(request,id):
    employee = ChagreType.objects.get(pk=id)
    employee.delete()
    return redirect('/cthome')