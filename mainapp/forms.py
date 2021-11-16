from django import forms
from .models import District , SubDistrict , Neighbor , SubNeighbor , identification , PropertyMap,Plotmap,PlotNo,Purchaseinfo,Landtype,Notary,Parcel,Sellerinfo,Dhaxalayaal,SupportingDOC,DhaxalSubDoc,BussinessRegistration,BussinessRegistrator,BussinessStatus,Coordinates,KalawarejinSubDoc,PropertyRevenu,BussinessRevenu,Charges,ChagreType,Currencies


class DistrictForm(forms.ModelForm):

    class Meta:
        model = District
        fields = ('name',)

class SubDistrictForm(forms.ModelForm):
    
    class Meta:
        model = SubDistrict
        fields = ('SubDistrictname','District',)
    
    def __init__(self, *args, **kwargs):
        super(SubDistrictForm,self).__init__(*args, **kwargs)
        self.fields['District'].empty_label = "Select"
class NeighborForm(forms.ModelForm):
    
    class Meta:
        model = Neighbor
        fields = ('subDistrict','Neighborname',)

    def __init__(self, *args, **kwargs):
        super(NeighborForm,self).__init__(*args, **kwargs)
        self.fields['subDistrict'].empty_label = "Select"
class SubNeigborForm(forms.ModelForm):
    
    class Meta:
        model = SubNeighbor
        fields = ('Neigbour','SubNeighborname',)

    def __init__(self, *args, **kwargs):
        super(SubNeigborForm,self).__init__(*args, **kwargs)
        self.fields['Neigbour'].empty_label = "Select"
class identificationForm(forms.ModelForm):
    ScanedID = forms.FileField(required=False)
    IDdate= forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'IDdate'}),)
  
    class Meta:
        model = identification
        fields = ('IDType','OtherID','IDNumber','IDissueBy','IDdate','ScanedID')
class PropertyMapForm(forms.ModelForm):
    Parcelmap = forms.FileField(required=False)
    MasterplanMap = forms.FileField(required=False)
    class Meta:
        model = PropertyMap
        fields = ('Purchaseinfo','PropertyNumber','Parcelmap','MasterplanMap')
    def __init__(self, *args, **kwargs):
        super(PropertyMapForm,self).__init__(*args, **kwargs)
        self.fields['Purchaseinfo'].empty_label = "Select"
class Plotmapform(forms.ModelForm):

    class Meta:
        model = Plotmap
        fields = ('purchaseinfo', 'Lenght', 'Width')
    def __init__(self, *args, **kwargs):
        super(Plotmapform,self).__init__(*args, **kwargs)
        self.fields['purchaseinfo'].empty_label = "Select"
class Plotnoform(forms.ModelForm):
    
    class Meta:
        model = PlotNo
        fields = ('District', 'SubDistrict', 'Neighbor', 'SubNeighbor','PlotNo')
    def __init__(self, *args, **kwargs):
        super(Plotnoform,self).__init__(*args, **kwargs)
        self.fields['District'].empty_label = "Select"
        self.fields['SubDistrict'].empty_label = "Select"
        self.fields['Neighbor'].empty_label = "Select"
        self.fields['SubNeighbor'].empty_label = "Select"
class Purchaseinfoform(forms.ModelForm):
    
    class Meta:
        model = Purchaseinfo
        fields = ('District', 'SubDistrict', 'Neighbor' , 'PlotNo','identification',  'OwnerFirstName' , 'OwnerSecondName', 'OwnerLastName', 'OwnerSurName', 'Mobile', 'Email', 'OtherProperty')
    def __init__(self, *args, **kwargs):
        super(Purchaseinfoform,self).__init__(*args, **kwargs)
        self.fields['District'].empty_label = "Select"
        self.fields['SubDistrict'].empty_label = "Select"
        self.fields['Neighbor'].empty_label = "Select"
        self.fields['PlotNo'].empty_label = "Select"
        self.fields['identification'].empty_label = "Select"
class Parcelform(forms.ModelForm):
    PurchaseDate = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'PurchaseDate'}),)

    class Meta:
        model = Parcel
        fields = ('Purchaseinfo', 'Landtype', 'Notary' , 'Existingbuilding','Landpurchaseamount',  'PurchaseDate' , 'FileNO', 'LandUsetype', 'Landwidth', 'landlenght')
    def __init__(self, *args, **kwargs):
        super(Parcelform,self).__init__(*args, **kwargs)
        self.fields['Purchaseinfo'].empty_label = "Select"
        self.fields['Landtype'].empty_label = "Select"
        self.fields['Notary'].empty_label = "Select"
class Notaryform(forms.ModelForm):
    
    class Meta:
        model = Notary
        fields = ('Notrayname','YearEstablished','Ownername','Address')
class Landtypeform(forms.ModelForm):
    
    class Meta:
        model = Landtype
        fields = ('Landtype',)
class sellerinfoform(forms.ModelForm):
    DOB = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'DOB'}),)
    class Meta:
        model = Sellerinfo
        fields = ('Parcel', 'FirstName','SecondName','LastName','SurName','Gender','DOB','MobileNO1','MobileNo2','Email')
    def __init__(self, *args, **kwargs):
        super(sellerinfoform,self).__init__(*args, **kwargs)
        self.fields['Parcel'].empty_label = "Select"
        self.fields['Gender'].empty_label = "Select"
class Dhaxalform(forms.ModelForm):
    DOB = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'DOB'}),)
    class Meta:
        model = Dhaxalayaal
        fields = ( 'Parcel', 'FirstName','SecondName','LastName','Gender','DOB','Telephone')
    def __init__(self, *args, **kwargs):
        super(Dhaxalform,self).__init__(*args, **kwargs)
        self.fields['Parcel'].empty_label = "Select"
        self.fields['Gender'].empty_label = "Select"

class DhaxalSubForm(forms.ModelForm):
    KalawarejinDOC1  = forms.FileField(required=False)
    KalawarejinDOC2  = forms.FileField(required=False)
    KalawarejinDOC3  = forms.FileField(required=False)
    KalawarejinDOC4  = forms.FileField(required=False)
    class Meta:
        model = DhaxalSubDoc
        fields = ('Parcel','KalawarejinDOC1','KalawarejinDOC2','KalawarejinDOC3','KalawarejinDOC4')
    def __init__(self, *args, **kwargs):
        super(DhaxalSubForm,self).__init__(*args, **kwargs)
        self.fields['Parcel'].empty_label = "Select"
  
class SupportingDocForm(forms.ModelForm):
    IDcard  = forms.FileField(required=False)
    GentalReciptVoucher  = forms.FileField(required=False)
    MasterPlan  = forms.FileField(required=False)
    NotaryAuthorization  = forms.FileField(required=False)
    UploadCustomRegisForm  = forms.FileField(required=False)
    Hibyan  = forms.FileField(required=False)
    Dhaxal = forms.FileField(required=False)
    FileScan  = forms.FileField(required=False)
    class Meta:
        model = SupportingDOC
        fields = ('Parcel','IDcard','GentalReciptVoucher','MasterPlan','NotaryAuthorization','UploadCustomRegisForm','Hibyan','Dhaxal','FileScan')
    def __init__(self, *args, **kwargs):
        super(SupportingDocForm,self).__init__(*args, **kwargs)
        self.fields['Parcel'].empty_label = "Select"
class BussinessRegform(forms.ModelForm):
    
    class Meta:
        model = BussinessRegistration
        fields = ('PropertyID','District', 'SubDistrict', 'Neighbor', 'PlotNo','licenseNO','BussinessName','BussinessType','BussinessGrade','Type','BillingType')
    def __init__(self, *args, **kwargs):
        super(BussinessRegform,self).__init__(*args, **kwargs)
        self.fields['District'].empty_label = "Select"
        self.fields['SubDistrict'].empty_label = "Select"
        self.fields['Neighbor'].empty_label = "Select"
class BussinessRegistratorform(forms.ModelForm):
    DOB = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'DOB'}),)
    class Meta:
        model = BussinessRegistrator
        fields = ( 'BussinessReg', 'RegFirstName','BussinessSecondName','BussinessLastName','DOB','Gender','Telephone')
    def __init__(self, *args, **kwargs):
        super(BussinessRegistratorform,self).__init__(*args, **kwargs)
        self.fields['BussinessReg'].empty_label = "Select"
class Bussinessstatusform(forms.ModelForm):
    StatusDate = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'StatusDate'}),)

    class Meta:
        model = BussinessStatus
        fields = ( 'BussinessReg', 'StatusType','StatusDate')
    def __init__(self, *args, **kwargs):
        super(Bussinessstatusform,self).__init__(*args, **kwargs)
        self.fields['BussinessReg'].empty_label = "Select"
class Coordinateform(forms.ModelForm):


    class Meta:
        model = Coordinates
        fields = ( 'SequesnceNo', 'Parcel','Longitude','Latitude','Attribute')
    def __init__(self, *args, **kwargs):
        super(Coordinateform,self).__init__(*args, **kwargs)
        self.fields['Parcel'].empty_label = "Select"
class kalawarejinform(forms.ModelForm):
    DhaxalDOC1   = forms.FileField(required=False)
    DhaxalDOC2  = forms.FileField(required=False)
    DhaxalDOC3   = forms.FileField(required=False)
    DhaxalDOC4  = forms.FileField(required=False)
    class Meta:
        model = KalawarejinSubDoc
        fields = ('Parcel','DhaxalDOC1','DhaxalDOC2','DhaxalDOC3','DhaxalDOC4')
    def __init__(self, *args, **kwargs):
        super(kalawarejinform,self).__init__(*args, **kwargs)
        self.fields['Parcel'].empty_label = "Select"
class PRform(forms.ModelForm):
    TaransDate = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'TaransDate'}),)
    class Meta:
        model = PropertyRevenu
        fields = ('Parcel','TransNo','TaransDate','Chargecode','Transcurr','GrNo','Revenuetype')
    def __init__(self, *args, **kwargs):
        super(PRform,self).__init__(*args, **kwargs)
        self.fields['Parcel'].empty_label = "Select"
class BReform(forms.ModelForm):
    TaransDate = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'TaransDate'}),)
    class Meta:
        model = BussinessRevenu
        fields = ('BussinessReg','TransNo','TaransDate','Chargecode','Transcurr','GrNo','Revenuetype')
    def __init__(self, *args, **kwargs):
        super(BReform,self).__init__(*args, **kwargs)
        self.fields['BussinessReg'].empty_label = "Select"
class Chargeform(forms.ModelForm):

    class Meta:
        model = Charges
        fields = ('BussinessRevenu','ChargeName','Glnaccount','Chargestatus')
    def __init__(self, *args, **kwargs):
        super(Chargeform,self).__init__(*args, **kwargs)
        self.fields['BussinessRevenu'].empty_label = "Select"
class Currenciesform(forms.ModelForm):
    
    class Meta:
        model = Currencies
        fields = ('BussinessRevenu','CurrName','ExcRate')
    def __init__(self, *args, **kwargs):
        super(Currenciesform,self).__init__(*args, **kwargs)
        self.fields['BussinessRevenu'].empty_label = "Select"
class ChagreTypeform(forms.ModelForm):
    
    class Meta:
        model =   ChagreType
        fields = ('BussinessReg',)
    def __init__(self, *args, **kwargs):
        super(ChagreTypeform,self).__init__(*args, **kwargs)
        self.fields['BussinessReg'].empty_label = "Select"


