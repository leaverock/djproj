from django.db import models
from django.contrib.postgres.fields import ArrayField
from data.txt import get_diap, read_string, read_integer, read_float
from . import dbg_train


class FlCctHDRstruct(models.Model):
    Descr = models.CharField(max_length=50, default='')
    Vers = models.FloatField(default=0.0)
    SrtMd = models.IntegerField(default=0)
    KldTyp = ArrayField(models.CharField(max_length=50, default=''))
    Rsrv1 = models.IntegerField(default=0)
    Rsrv2 = models.FloatField(default=0.0)
    Rsrv3 = models.FloatField(default=0.0)
    Rsrv4 = models.FloatField(default=0.0)

    @classmethod
    def from_txt(cls, f):
        Descr_val = read_string(f)
        Vers_val = read_float(f)
        SrtMd_val = read_integer(f)

        KldTypDim = get_diap(f)
        KldTyp_dim = KldTypDim[1][0] - KldTypDim[0][0] + 1
        KldTyp_val = [None for j in range(KldTyp_dim)]
        for i in range(KldTyp_dim):
            KldTyp_val[i] = read_string(f)

        Rsrv1_val = read_integer(f)
        Rsrv2_val = read_float(f)
        Rsrv3_val = read_float(f)
        Rsrv4_val = read_float(f)

        rez = cls(Descr=Descr_val, Vers=Vers_val, SrtMd=SrtMd_val, KldTyp=KldTyp_val,
                  Rsrv1=Rsrv1_val, Rsrv2=Rsrv2_val, Rsrv3=Rsrv3_val, Rsrv4=Rsrv4_val)
        rez.save()
        return rez

    def __str__(self):
        s = str.format("FlCctHDRstruct: self.id: %d, Descr: '%s', Vers: %f, SrtMd: %d\n" %
                       (self.id, self.Descr, self.Vers, self.SrtMd))
        for i in range(len(self.KldTyp)):
            s = s + str.format("KldTyp(%d): '%s'\n" % (i, self.KldTyp[i]))
        s = s + str.format("Rsrv1: %d, Rsrv2: %f, Rsrv3: %f, Rsrv4: %f\n" %
                           (self.Rsrv1, self.Rsrv2, self.Rsrv3, self.Rsrv4))
        return s


class CoctavSTRUCT(models.Model):
    CcID = models.IntegerField(default=0)
    CcNam = models.CharField(max_length=50, default='')
    CcMvg = models.IntegerField(default=0)
    CcMos = models.IntegerField(default=0)
    CcQf = models.FloatField(default=0.0)
    CcLf = models.FloatField(default=0.0)
    CcKldn = models.IntegerField(default=0)
    CcKp = models.FloatField(default=0.0)
    CcPg = models.FloatField(default=0.0)
    CcWo = ArrayField(ArrayField(models.FloatField(default=0.0)))
    CcVgMx = models.IntegerField(default=0)
    # CcVgs(LimCctVg) As CcVgsSTRUCT
    # CcKoef = ArrayField(models.FloatField(default=0.0))
    CcRsv1 = models.FloatField(default=0.0)
    CcRsv2 = models.IntegerField(default=0)

    @classmethod
    def from_txt(cls, f):
        CcID_val = read_integer(f)
        CcNam_val = read_string(f)
        CcMvg_val = read_integer(f)
        CcMos_val = read_integer(f)
        CcQf_val = read_float(f)
        CcLf_val = read_float(f)
        CcKldn_val = read_integer(f)
        CcKp_val = read_float(f)
        CcPg_val = read_float(f)

        CcWoDim = get_diap(f)
        i_max = CcWoDim[1][0] - CcWoDim[0][0] + 1
        j_max = CcWoDim[1][1] - CcWoDim[0][1] + 1
        CcWo_val = [[0.0 for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                CcWo_val[i][j] = read_float(f)

        CcVgMx_val = read_integer(f)

        CcVgsDim = get_diap(f)
        CcVgs_dim = CcVgsDim[1][0] - CcVgsDim[0][0] + 1
        CcVgs_val = [None for i in range(CcVgs_dim)]
        for i in range(CcVgs_dim):
            CcVgs_val[i] = CcVgsSTRUCT.from_txt(f)

        CcRsv1_val = read_float(f)
        CcRsv2_val = read_integer(f)

        rez = cls(CcID=CcID_val, CcNam=CcNam_val, CcMvg=CcMvg_val, CcMos=CcMos_val,
                  CcQf=CcQf_val, CcLf=CcLf_val, CcKldn=CcKldn_val, CcKp=CcKp_val, CcPg=CcPg_val,
                  CcWo=CcWo_val, CcVgMx=CcVgMx_val, CcRsv1=CcRsv1_val, CcRsv2=CcRsv2_val)
        rez.save()

        for i in range(CcVgs_dim):
            CcVgs_val[i].cc = rez
            CcVgs_val[i].save()
            if dbg_train: print("CoctavSTRUCT constructor: CcVgs[%d]:\n%s" % (i, CcVgs_val[i]))

        return rez

    def __str__(self):
        s = str.format("CoctavSTRUCT:self.id: %d, CcID: %d, CcNam: '%s', CcMvg: %d, \n" %
                       (self.id, self.CcID, self.CcNam, self.CcMvg))
        s = s + str.format("CcMos: %d, CcQf: %f, CcLf: %f, CcKldn: %d, CcKp: %f, CcPg: %f\n" %
                           (self.CcMos, self.CcQf, self.CcLf, self.CcKldn, self.CcKp, self.CcPg))

        for i in range(len(self.CcWo)):
            for j in range(len(self.CcWo[i])):
                s = s + str.format("CcWo[%d,%d]: %f\n" % (i, j, self.CcWo[i][j]))

        s = s + str.format("CcVgMx: %d\n" % self.CcVgMx)

        s = s + "item's CcVgs:\n"
        for x in self.ccvgsstruct_set.all(): s = s + str(x) + '\n'

        s = s + str.format("CcRsv1: %f, CcRsv2: %d\n" % (self.CcRsv1, self.CcRsv2))

        return s


class CcVgsSTRUCT(models.Model):
    CvID = models.IntegerField(default=0)
    CvMvg = models.IntegerField(default=0)
    # CvQf = models.CharField(max_length=50,default='')
    CvQf = models.FloatField(default=0.0)
    cc = models.ForeignKey(CoctavSTRUCT, on_delete=models.CASCADE, default=None)

    @classmethod
    def from_txt(cls, f):
        CvID_val = read_integer(f)
        CvMvg_val = read_integer(f)
        CvQf_val = read_float(f)

        rez = cls(CvID=CvID_val, CvMvg=CvMvg_val, CvQf=CvQf_val)
        return rez

    def __str__(self):
        s = str.format("CcVgsSTRUCT:self.id: %d, CvID: %d, CvMvg: %d, CvQf: %f" %
                       (self.id, self.CvID, self.CvMvg, self.CvQf))
        return s

