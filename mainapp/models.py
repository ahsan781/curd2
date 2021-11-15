from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubDistrict(models.Model):
    SubDistrictname = models.CharField(max_length=100)
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self. SubDistrictname
class Neighbor(models.Model):
  id = models.AutoField(primary_key=True)
  subDistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
  Neighborname = models.CharField(max_length=200)
  def __str__(self):
        return self.Neighborname
class SubNeighbor(models.Model):
  id = models.AutoField(primary_key=True)
  Neigbour = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
  SubNeighborname = models.CharField(max_length=200)
  def __str__(self):
        return self.SubNeighborname
class identification(models.Model):
    id = models.AutoField(primary_key=True)
    IDType =  models.CharField(max_length=200)
    OtherID =  models.PositiveIntegerField(blank=True)
    IDNumber =  models.PositiveIntegerField(blank=True)
    IDissueBy =  models.CharField(max_length=200)
    IDdate =   models.DateField()
    ScanedID = models.FileField(upload_to ='identification/',null=True)
    def __str__(self):
        return self.IDType
class PropertyMap(models.Model):
    id = models.AutoField(primary_key=True)
    RegistrationID = models.ForeignKey(identification,on_delete=models.CASCADE)
    PropertyNumber =  models.PositiveIntegerField(blank=True)
    Parcelmap = models.FileField(upload_to ='parcelmap/',null=True)
    MasterplanMap = models.FileField(upload_to ='masterplanmap/',null=True)
    def __str__(self):
             return "%s" % (self.PropertyNumber)
class Plotmap(models.Model):
    id = models.AutoField(primary_key=True)
    RegistrationID = models.ForeignKey(identification,on_delete=models.CASCADE)
    Lenght = models.CharField(max_length=500)
    Width = models.CharField(max_length=500)
class PlotNo(models.Model):
    id = models.AutoField(primary_key=True)
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    SubDistrict = models.ForeignKey(SubDistrict,on_delete=models.CASCADE)
    Neighbor = models.ForeignKey(Neighbor,on_delete=models.CASCADE)
    SubNeighbor = models.ForeignKey(SubNeighbor,on_delete=models.CASCADE)
    PlotNo =  models.PositiveIntegerField(blank=True)
    identification = models.ForeignKey(identification,on_delete=models.CASCADE)
    Propertymap = models.ForeignKey(PropertyMap,on_delete=models.CASCADE)
    def __str__(self):
             return "%s" % (self.PlotNo)
class Purchaseinfo(models.Model):
    RegistrationNO = models.AutoField(primary_key=True)
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    SubDistrict = models.ForeignKey(SubDistrict,on_delete=models.CASCADE)
    Neighbor = models.ForeignKey(Neighbor,on_delete=models.CASCADE)
    PlotNo = models.ForeignKey(PlotNo,on_delete=models.CASCADE)
    identification = models.OneToOneField(identification,on_delete=models.CASCADE)
    OwnerFirstName =  models.CharField(max_length=500)
    OwnerSecondName  =  models.CharField(max_length=500)
    OwnerLastName =  models.CharField(max_length=500)
    OwnerSurName  =  models.CharField(max_length=500)
    Mobile =  models.CharField(max_length=500)
    Email =  models.CharField(max_length=500)
    OtherProperty =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.RegistrationNO)

class Landtype(models.Model):
    id = models.AutoField(primary_key=True)
    Landtype =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.Landtype)
class Notary(models.Model):
    id = models.AutoField(primary_key=True)
    Notrayname =  models.CharField(max_length=500)
    YearEstablished =  models.CharField(max_length=500)
    Ownername =  models.CharField(max_length=500)
    Address =  models.CharField(max_length=700)
   

    def __str__(self):
             return "%s" % (self.Notrayname)
class Parcel(models.Model):
    Registrationid = models.AutoField(primary_key=True)
    Purchaseinfo = models.ForeignKey(Purchaseinfo,on_delete=models.CASCADE)
    Landtype = models.ForeignKey(Landtype,on_delete=models.CASCADE)
    Notary = models.ForeignKey(Notary,on_delete=models.CASCADE)
    Existingbuilding =  models.CharField(max_length=500)
    Landpurchaseamount  =  models.CharField(max_length=500)
    PurchaseDate =   models.DateField()
    FileNO  =  models.PositiveIntegerField(blank=True)
    LandUsetype=  models.CharField(max_length=500)
    Landwidth =  models.CharField(max_length=500)
    landlenght =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.Registrationid)
class Sellerinfo(models.Model):
    Registrationid = models.AutoField(primary_key=True)
    Parcel =  models.ForeignKey(Parcel,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=500)
    SecondName = models.CharField(max_length=500)
    LastName =  models.CharField(max_length=500)
    SurName =  models.CharField(max_length=500)
    DOB =  models.DateField()
    role=(
        ('Male','Male'),
        ('Female','Female')
    )
    Gender =   models.CharField(max_length=100 , choices=role)
    MobileNO1 =  models.CharField(max_length=500)
    MobileNo2 =  models.CharField(max_length=500)
    Email =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.FirstName)
class Dhaxalayaal(models.Model):
    Registrationid = models.AutoField(primary_key=True)
    Parcel =  models.ForeignKey(Parcel,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=500)
    SecondName = models.CharField(max_length=500)
    LastName =  models.CharField(max_length=500)
    DOB =  models.DateField()
    role=(
        ('Male','Male'),
        ('Female','Female')
    )
    Gender =   models.CharField(max_length=100 , choices=role)
    Telephone =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.FirstName)
class DhaxalSubDoc(models.Model):
    RegistrationID = models.AutoField(primary_key=True)
    Parcel =  models.ForeignKey(Parcel,on_delete=models.CASCADE)
    KalawarejinDOC1 =  models.FileField(upload_to ='kalaDOC1/',null=True)
    KalawarejinDOC2 =  models.FileField(upload_to ='kalaDOC2/',null=True)
    KalawarejinDOC3 =  models.FileField(upload_to ='kalaDOC3/',null=True)
    KalawarejinDOC4 =  models.FileField(upload_to ='kalaDOC4/',null=True)
    def __str__(self):
             return "%s" % (self.RegistrationID)
class SupportingDOC(models.Model):
    RegistrationID = models.AutoField(primary_key=True)
    Parcel =  models.ForeignKey(Parcel,on_delete=models.CASCADE)
    IDcard =  models.FileField(upload_to ='IDCARD/',null=True)
    GentalReciptVoucher =  models.FileField(upload_to ='GR/',null=True)
    MasterPlan =  models.FileField(upload_to ='Masterplan/',null=True)
    NotaryAuthorization =  models.FileField(upload_to ='NA/',null=True)
    UploadCustomRegisForm =  models.FileField(upload_to ='UCR/',null=True)
    Hibyan =  models.FileField(upload_to ='Hibyan/',null=True)
    Dhaxal =  models.FileField(upload_to ='Dhaxal/',null=True)
    FileScan =  models.FileField(upload_to ='Filescan/',null=True)
    

    def __str__(self):
             return "%s" % (self.RegistrationID)
class BussinessRegistration(models.Model):
    BussinessID = models.AutoField(primary_key=True)
    PropertyID  =  models.PositiveIntegerField(blank=True)
    District = models.ForeignKey(District,on_delete=models.CASCADE)
    SubDistrict = models.ForeignKey(SubDistrict,on_delete=models.CASCADE)
    Neighbor = models.ForeignKey(Neighbor,on_delete=models.CASCADE)
    PlotNo = models.ForeignKey(PlotNo,on_delete=models.CASCADE)
    licenseNO =  models.CharField(max_length=500)
    BussinessName  =  models.CharField(max_length=500)
    BussinessType =  models.CharField(max_length=500)
    BussinessGrade  =  models.CharField(max_length=500)
    Type =  models.CharField(max_length=500)
    BillingType =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.BussinessName)
class BussinessRegistrator(models.Model):
    RegistrationID = models.AutoField(primary_key=True)
    BussinessReg = models.ForeignKey(BussinessRegistration,on_delete=models.CASCADE)
    RegFirstName =  models.CharField(max_length=500)
    BussinessSecondName =  models.CharField(max_length=500)
    BussinessLastName =  models.CharField(max_length=500)
    DOB =  models.DateField()
    role=(
        ('Male','Male'),
        ('Female','Female')
    )
    Gender =   models.CharField(max_length=100 , choices=role)
    Telephone =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.RegistrationID)
class BussinessStatus(models.Model):
    BussinessID = models.AutoField(primary_key=True)
    BussinessReg = models.ForeignKey(BussinessRegistration,on_delete=models.CASCADE)
    StatusType =  models.CharField(max_length=500)
    StatusDate = models.DateField()

    def __str__(self):
             return "%s" % (self.BussinessID)
class Coordinates(models.Model):
    RegistrationNo = models.AutoField(primary_key=True)
    SequesnceNo =  models.PositiveIntegerField(blank=True)
    Parcel =  models.ForeignKey(Parcel,on_delete=models.CASCADE)
    Longitude = models.CharField(max_length=500)
    Latitude = models.CharField(max_length=500)
    Attribute =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.RegistrationNo)
class KalawarejinSubDoc(models.Model):
    RegistrationID = models.AutoField(primary_key=True)
    Parcel =  models.ForeignKey(Parcel,on_delete=models.CASCADE)
    DhaxalDOC1 =  models.FileField(upload_to ='DhaxalDOC1/',null=True)
    DhaxalDOC2 =  models.FileField(upload_to ='DhaxalDOC2/',null=True)
    DhaxalDOC3 =  models.FileField(upload_to ='DhaxalDOC3/',null=True)
    DhaxalDOC4 =  models.FileField(upload_to ='DhaxalDOC4/',null=True)
    def __str__(self):
             return "%s" % (self.RegistrationID)
class PropertyRevenu(models.Model):
    RegistrationNo = models.AutoField(primary_key=True)
    Parcel =  models.ForeignKey(Parcel,on_delete=models.CASCADE,default='1')
    TransNo =  models.PositiveIntegerField(blank=True)
    TaransDate =  models.DateField()
    Chargecode =  models.CharField(max_length=500)
    Transcurr =  models.CharField(max_length=500)
    GrNo =  models.CharField(max_length=500)
    Revenuetype =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.RegistrationNo)
class BussinessRevenu(models.Model):
    BussinessID = models.AutoField(primary_key=True)
    BussinessReg =  models.ForeignKey(BussinessRegistration,on_delete=models.CASCADE,default='1')
    TransNo =  models.PositiveIntegerField(blank=True)
    TaransDate =  models.DateField()
    Chargecode =  models.CharField(max_length=500)
    Transcurr =  models.CharField(max_length=500)
    GrNo =  models.CharField(max_length=500)
    Revenuetype =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.BussinessID)
class Charges(models.Model):
    ChargeCode = models.AutoField(primary_key=True)
    BussinessRevenu =  models.ForeignKey(BussinessRevenu,on_delete=models.CASCADE)
    ChargeName =  models.CharField(max_length=500)
    Glnaccount =  models.CharField(max_length=500)
    Chargestatus =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.ChargeCode)
class Currencies(models.Model):
    CurrCode = models.AutoField(primary_key=True)
    BussinessRevenu =  models.ForeignKey(BussinessRevenu,on_delete=models.CASCADE)
    CurrName =  models.CharField(max_length=500)
    ExcRate =  models.CharField(max_length=500)
    def __str__(self):
             return "%s" % (self.CurrCode)
class  ChagreType(models.Model):
    ChagreType = models.AutoField(primary_key=True)
    BussinessReg =  models.ForeignKey(BussinessRegistration,on_delete=models.CASCADE)
    def __str__(self):
             return "%s" % (self.ChagreType)