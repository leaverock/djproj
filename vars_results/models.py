from django.db import models
from django.contrib.postgres.fields import ArrayField
from data.txt import get_diap, read_string, read_integer, read_float, read_boolean
from . import dbg_vars_results


class TjnHDstruct (models.Model):
    Comment = models.CharField(max_length=50,default='')
    UFile = models.CharField(max_length=50,default='')
    UVersFl = models.IntegerField(default=0)
    TVersFl = models.IntegerField(default=0)
    TVersPrg = models.FloatField(default=0.0)
    DTj = models.FloatField(default=0.0)
    TstrtKm = models.FloatField(default=0.0)
    TskExc = models.IntegerField(default=0)
    mVar = models.IntegerField(default=0)
    mTcb = models.IntegerField(default=0)
    WdirO = models.CharField(max_length=50,default='')
    rsrvT1 = models.CharField(max_length=50, default='')
    rsrvT2 = models.CharField(max_length=50,default='')
    rsrvT3 = models.FloatField(default=0.0)
    rsrvT4 = models.IntegerField(default=0)

    @classmethod
    def from_txt(cls, f):
        Comment_val = read_string(f)
        UFile_val = read_string(f)
        UVersFl_val = read_integer(f)
        TVersFl_val = read_integer(f)
        TVersPrg_val = read_float(f)
        DTj_val = read_float(f)
        TstrtKm_val = read_float(f)
        TskExc_val = read_integer(f)
        mVar_val = read_integer(f)
        mTcb_val = read_integer(f)
        WdirO_val = read_string(f)
        rsrvT1_val = read_string(f)
        rsrvT2_val = read_string(f)
        rsrvT3_val = read_float(f)
        rsrvT4_val = read_integer(f)

        rez = cls( Comment= Comment_val, UFile=UFile_val, UVersFl=UVersFl_val,
            TVersFl=TVersFl_val, TVersPrg=TVersPrg_val, DTj=DTj_val, TstrtKm=TstrtKm_val,
            TskExc=TskExc_val, mVar=mVar_val, mTcb=mTcb_val, WdirO=WdirO_val, rsrvT1=rsrvT1_val,
            rsrvT2=rsrvT2_val, rsrvT3=rsrvT3_val, rsrvT4=rsrvT4_val )
        rez.save()
        return rez

    def __str__(self):
        s = str.format("TjnHDstruct: self.id: %d, Comment: '%s', UFile: '%s', UVersFl: %d\n" %
            (self.id, self.Comment, self.UFile, self.UVersFl))
        s = s + str.format("TVersFl: %d, TVersPrg: %f, DTj: %f, TstrtKm: %f, TskExc: %d, mVar: %d\n" %
            (self.TVersFl, self.TVersPrg, self.DTj, self.TstrtKm, self.TskExc, self.mVar))
        s = s + str.format("mTcb: %d, WdirO: '%s', rsrvT1: '%s', rsrvT2: '%s', rsrvT3: %f, rsrvT4: %d\n" %
            (self.mTcb, self.WdirO, self.rsrvT1, self.rsrvT2, self.rsrvT3, self.rsrvT4))
        return s


class TJNtyp (models.Model):
    VarNo = models.IntegerField(default=0)
    Catg = models.IntegerField(default=0)
    LcmFl = models.CharField(max_length=50,default='')
    LcmNam = models.CharField(max_length=50,default='')
    Mloc = models.FloatField(default=0.0)
    CctID = models.IntegerField(default=0)
    Qcoct = models.IntegerField(default=0)
    Qtr = models.IntegerField(default=0)
    Ltr = models.IntegerField(default=0)
    DTc = models.FloatField(default=0.0)
    ToStrt = models.IntegerField(default=0)
    rsrvTj1 = models.IntegerField(default=0)
    rsrvTj2 = models.IntegerField(default=0)
    StHom = models.IntegerField(default=0)
    StEnd = models.IntegerField(default=0)
    Vstrt = models.IntegerField(default=0)
    Vkon = models.IntegerField(default=0)
    Kpsi = models.FloatField(default=0.0)
    UT = models.IntegerField(default=0)
    MxPoz = models.FloatField(default=0.0)
    DPoz = models.FloatField(default=0.0)
    SpdZn = models.IntegerField(default=0)
    OptVbg = models.BooleanField(default=False)
    UsRecp = models.BooleanField(default=False)
    UsMxRcp = models.BooleanField(default=False)
    StOst = ArrayField(ArrayField(models.IntegerField(default=0)))

    @classmethod
    def from_txt(cls, f):
        VarNo_val = read_integer(f)
        Catg_val = read_integer(f)
        LcmFl_val = read_string(f)
        LcmNam_val = read_string(f)
        Mloc_val = read_float(f)
        CctID_val = read_integer(f)
        Qcoct_val = read_integer(f)
        Qtr_val = read_integer(f)
        Ltr_val = read_integer(f)
        DTc_val = read_float(f)
        ToStrt_val = read_integer(f)
        rsrvTj1_val = read_integer(f)
        rsrvTj2_val = read_integer(f)
        StHom_val = read_integer(f)
        StEnd_val = read_integer(f)
        Vstrt_val = read_integer(f)
        Vkon_val = read_integer(f)
        Kpsi_val = read_float(f)
        UT_val = read_integer(f)
        MxPoz_val = read_float(f)
        DPoz_val = read_float(f)
        SpdZn_val = read_integer(f)
        OptVbg_val = read_boolean(f)
        UsRecp_val = read_boolean(f)
        UsMxRcp_val = read_boolean(f)

        StOstDim = get_diap(f)
        i_max = StOstDim[1][0] - StOstDim[0][0] + 1
        j_max = StOstDim[1][1] - StOstDim[0][1] + 1
        StOst_val = [[0.0 for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                StOst_val[i][j] = read_integer(f)

        rez = cls(VarNo=VarNo_val, Catg=Catg_val, LcmFl=LcmFl_val, LcmNam=LcmNam_val, Mloc=Mloc_val, CctID=CctID_val,
                  Qcoct=Qcoct_val, Qtr=Qtr_val, Ltr=Ltr_val,
                  DTc=DTc_val, ToStrt=ToStrt_val, rsrvTj1=rsrvTj1_val,  rsrvTj2=rsrvTj2_val,  StHom=StHom_val,
                  StEnd=StEnd_val,  Vstrt=Vstrt_val, Vkon=Vkon_val,
                  Kpsi=Kpsi_val, UT=UT_val,  MxPoz=MxPoz_val,  DPoz=DPoz_val,  SpdZn=SpdZn_val,  OptVbg=OptVbg_val,
                  UsRecp=UsRecp_val,  UsMxRcp=UsMxRcp_val, StOst=StOst_val)
        rez.save()
        return rez

    def __str__(self):
        s = str.format("TJNtyp: self.id: %d, VarNo: %d, Catg: %d, LcmFl: '%s', LcmNam: '%s'\n" %
            (self.id, self.VarNo, self.Catg, self.LcmFl, self.LcmNam))
        s = s + str.format("Mloc: %f, CctID: %d, Qcoct: %d, Qtr: %d, Ltr: %d, DTc: %f\n" %
            (self.Mloc, self.CctID, self.Qcoct, self.Qtr, self.Ltr, self.DTc))
        s = s + str.format("ToStrt: %d, rsrvTj1: %d, rsrvTj2: %d, StHom: %d, StEnd: %d, Vstrt: %d\n" %
            (self.ToStrt, self.rsrvTj1, self.rsrvTj2, self.StHom, self.StEnd, self.Vstrt))
        s = s + str.format("Vkon: %d, Kpsi: %f, UT: %d, MxPoz: %f, DPoz: %f, SpdZn: %d\n" %
            (self.Vkon, self.Kpsi, self.UT, self.MxPoz, self.DPoz, self.SpdZn))
        s = s + str.format("OptVbg: %r, UsRecp: %r, UsMxRcp: %r\n" %
            (self.OptVbg, self.UsRecp, self.UsMxRcp))
        for i in range(len(self.StOst)):
            for j in range(len(self.StOst[i])):
                    s = s + str.format("StOst[%d,%d]: %d\n" % (i,j,self.StOst[i][j]))
        return s


class TJrSTRUCT(models.Model):
    mRegc = models.IntegerField(default=0)
    RcDkm = models.IntegerField(default=0)
    #Regc = ArrayField(RegcSTRUCT)

    @classmethod
    def from_txt(cls, f):
        mRegc_val = read_integer(f)
        RcDkm_val = read_integer(f)

        RegcDim = get_diap(f)
        i_max = RegcDim[1][0] - RegcDim[0][0] + 1
        Regc_val = [None for i in range(i_max)]
        for i in range(i_max):
            Regc_val[i] = RegcSTRUCT.from_txt(f)

        rez = cls(mRegc=mRegc_val, RcDkm=RcDkm_val)
        rez.save()

        for i in range(i_max):
            Regc_val[i].tt = rez
            Regc_val[i].save()
            if dbg_vars_results: print("TJrSTRUCT constructor: Regc[%d]:\n%s" % (i,Regc_val[i]))

        return rez

    def __str__(self):
        s = str.format("TJrSTRUCT: self.id: %d, mRegc: %f, RcDkm: %f\n" %
                       (self.id, self.mRegc, self.RcDkm))

        for x in self.regcstruct_set.all(): s = s + str(x) + '\n'
        # for i in range(len(self.Regc)):
        #     s = s + str.format("Regc[%d]: %s\n" % (i, self.Regc[i]))
        return s


class RegcSTRUCT (models.Model):
    rcLh = models.FloatField(default=0.0)
    rcLe = models.FloatField(default=0.0)
    rcUT = models.IntegerField(default=0)
    rcPoz = models.FloatField(default=0.0)
    rcReg = models.IntegerField(default=0)
    rcKps = models.FloatField(default=0.0)
    rcVtrm = models.IntegerField(default=0)
    rcPozR = models.FloatField(default=0.0)
    rcKtrm = models.FloatField(default=0.0)
    rcRsrv0 = models.FloatField(default=0.0)
    rcRsrv1 = models.FloatField(default=0.0)
    rcRsrv2 = models.FloatField(default=0.0)
    rcRsrv3 = models.FloatField(default=0.0)
    rcRsrv4 = models.FloatField(default=0.0)
    rcRsrv5 = models.FloatField(default=0.0)
    #cc = models.ForeignKey(CoctavSTRUCT, on_delete=models.CASCADE, default=None)
    tt = models.ForeignKey(TJrSTRUCT, on_delete=models.CASCADE, default=None)

    @classmethod
    def from_txt(cls, f):
        rcLh_val = read_float(f)
        rcLe_val = read_float(f)
        rcUT_val = read_integer(f)
        rcPoz_val = read_float(f)
        rcReg_val = read_integer(f)
        rcKps_val = read_float(f)
        rcVtrm_val = read_integer(f)
        rcPozR_val = read_float(f)
        rcKtrm_val = read_float(f)
        rcRsrv0_val = read_float(f)
        rcRsrv1_val = read_float(f)
        rcRsrv2_val = read_float(f)
        rcRsrv3_val = read_float(f)
        rcRsrv4_val = read_float(f)
        rcRsrv5_val = read_float(f)

        rez = cls( rcLh=rcLh_val,  rcLe=rcLe_val,  rcUT=rcUT_val,  rcPoz=rcPoz_val,  rcReg=rcReg_val,  rcKps=rcKps_val,
            rcVtrm=rcVtrm_val,  rcPozR=rcPozR_val,  rcKtrm=rcKtrm_val, rcRsrv0=rcRsrv0_val, rcRsrv1=rcRsrv1_val,
            rcRsrv2=rcRsrv2_val, rcRsrv3=rcRsrv3_val, rcRsrv4 = rcRsrv4_val, rcRsrv5=rcRsrv5_val)

        return rez

    def __str__(self):
        s = str.format("\nRegcSTRUCT: self.id: %d, rcLh: %f, rcLe: %f, rcUT: %d, rcPoz: %f\n" %
            (self.id, self.rcLh, self.rcLe, self.rcUT, self.rcPoz))
        s = s + str.format("rcReg: %d, rcKps: %f, rcVtrm: %d, rcPozR: %f, rcKtrm: %f, rcRsrv0: %f\n" %
            (self.rcReg, self.rcKps, self.rcVtrm, self.rcPozR, self.rcKtrm, self.rcRsrv0))
        s = s + str.format("rcRsrv1: %f, rcRsrv2: %f, rcRsrv3: %f, rcRsrv4: %f, rcRsrv5: %f" %
            (self.rcRsrv1, self.rcRsrv2, self.rcRsrv3, self.rcRsrv4, self.rcRsrv5))
        return s

