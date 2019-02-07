from django.db import models
from django.contrib.postgres.fields import ArrayField
from data.txt import get_diap, read_string, read_integer, read_float, read_boolean
from . import dbg_track


class UchSTRUCT(models.Model):
    KodDor = models.IntegerField(default=0)
    KodUch = models.IntegerField(default=0)
    DorNam = models.CharField(max_length=50, default='')  # название дороги
    UchNam = models.CharField(max_length=50, default='')  # название участка
    Comment = models.CharField(max_length=50, default='')  # примечание
    RsrvU1 = models.CharField(max_length=50, default='')  # видимо, зарезервированное поле
    VersFile = models.IntegerField(default=0)
    VersProg = models.FloatField(default=0.0)
    mGput = models.IntegerField(default=0)  # число главных путей минус 1
    Difl = models.BooleanField(default=False)  # различие профилей и длин перегонов путей
    RsrvU2 = models.FloatField(default=0.0)  # видимо, зарезервированное поле
    mStan = models.IntegerField(default=0)  # количество станций ?
    # Stans()  As StansSTRUCT
    NechSt = models.IntegerField(default=0)  # считать последнюю станцию в списке началом пути (нечетный путь)
    mCtg = models.IntegerField(default=0)  # количество категорий и типов поездов минус 1. не использую
    # CATEGS() As CategSTRUCT
    mVorp = models.IntegerField(default=0)  # количество ограничений скоростей минус 3
    VorpMx = models.IntegerField(default=0)  # самое большое ограничение скорости
    Vorp = ArrayField(ArrayField(ArrayField(ArrayField(models.FloatField(default=0.0)))))
    mPrf = models.IntegerField(default=0)  # количество Prof минус 2
    Prof = ArrayField(ArrayField(ArrayField(models.FloatField(default=0.0))))

    def __str__(self):
        s = str.format("UchSTRUCT: self.id: %d, KodDor: %d, KodUch: %d\n" % (self.id, self.KodDor, self.KodUch))
        s = s + str.format("DorNam: '%s', UchNam: '%s'\nComment: '%s', RsrvU1: '%s'" % (
        self.DorNam, self.UchNam, self.Comment, self.RsrvU1))
        s = s + str.format(
            ", VersFile: %d, VersProg: %f\nmGput: %d, Difl: %r" % (self.VersFile, self.VersProg, self.mGput, self.Difl))
        s = s + str.format("RsrvU2: %f, mStan: %d\n" % (self.RsrvU2, self.mStan))
        s = s + "item's StansSTRUCTs:\n"
        for x in self.stansstruct_set.all(): s = s + str(x) + '\n'
        s = s + str.format("NechSt: %d, mCtg: %d" % (self.NechSt, self.mCtg))
        s = s + "item's CategSTRUCTs:\n"
        for x in self.categstruct_set.all(): s = s + str(x) + '\n'
        s = s + str.format("mVorp: %d, VorpMx: %d\n" % (self.mVorp, self.VorpMx))
        for i in range(len(self.Vorp)):
            for j in range(len(self.Vorp[i])):
                for k in range(len(self.Vorp[i][j])):
                    for l in range(len(self.Vorp[i][j][k])):
                        s = s + str.format("Vorp[%d,%d,%d,%d]: %f\n" % (i, j, k, l, self.Vorp[i][j][k][l]))
        s = s + str.format("mPrf: %d" % self.mPrf)
        for i in range(len(self.Prof)):
            for j in range(len(self.Prof[i])):
                for k in range(len(self.Prof[i][j])):
                    s = s + str.format("Prof[%d,%d,%d]: %f\n" % (i, j, k, self.Prof[i][j][k]))
        return s

    @classmethod
    def from_txt(cls, f):
        KodDor_val = read_integer(f)
        KodUch_val = read_integer(f)
        DorNam_val = read_string(f)
        UchNam_val = read_string(f)
        Comment_val = read_string(f)
        RsrvU1_val = read_string(f)
        VersFile_val = read_integer(f)
        VersProg_val = read_float(f)
        mGput_val = read_integer(f)
        Difl_val = read_boolean(f)
        RsrvU2_val = read_float(f)
        mStan_val = read_integer(f)

        StansDim = get_diap(f)
        Stans_dim = StansDim[1][0] - StansDim[0][0] + 1
        Stans_val = [None for j in range(Stans_dim)]
        for i in range(Stans_dim):
            Stans_val[i] = StansSTRUCT.from_txt(f)

        NechSt_val = read_integer(f)
        mCtg_val = read_integer(f)

        CATEGSDim = get_diap(f)
        CATEGS_dim = CATEGSDim[1][0] - CATEGSDim[0][0] + 1
        CATEGS_val = [None for i in range(CATEGS_dim)]
        for i in range(CATEGS_dim):
            CATEGS_val[i] = CategSTRUCT.from_txt(f)

        mVorp_val = read_integer(f)
        VorpMx_val = read_integer(f)

        lng = get_diap(f)
        i_max = lng[1][0] - lng[0][0] + 1
        j_max = lng[1][1] - lng[0][1] + 1
        k_max = lng[1][2] - lng[0][2] + 1
        l_max = lng[1][3] - lng[0][3] + 1
        Vorp_val = [[[[0.0 for l in range(l_max)] for k in range(k_max)] for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                for k in range(k_max):
                    for l in range(l_max):
                        if dbg_track: print("UchSTRUCT constructor: Vorp [%d, %d, %d, %d]" % (i, j, k, l))
                        Vorp_val[i][j][k][l] = read_float(f)

        mPrf_val = read_integer(f)

        lng = get_diap(f)
        i_max = lng[1][0] - lng[0][0] + 1
        j_max = lng[1][1] - lng[0][1] + 1
        k_max = lng[1][2] - lng[0][2] + 1
        Prof_val = [[[0.0 for k in range(k_max)] for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                for k in range(k_max):
                    if dbg_track: print("UchSTRUCT constructor: Prof [%d, %d, %d]" % (i, j, k))
                    Prof_val[i][j][k] = read_float(f)

        rez = cls(KodDor=KodDor_val, KodUch=KodUch_val, DorNam=DorNam_val, UchNam=UchNam_val, Comment=Comment_val,
                  RsrvU1=RsrvU1_val, VersFile=VersFile_val, VersProg=VersProg_val, mGput=mGput_val, Difl=Difl_val,
                  RsrvU2=RsrvU2_val,
                  mStan=mStan_val, NechSt=NechSt_val, mCtg=mCtg_val, mVorp=mVorp_val, VorpMx=VorpMx_val, Vorp=Vorp_val,
                  mPrf=mPrf_val,
                  Prof=Prof_val)

        rez.save()

        for i in range(Stans_dim):
            Stans_val[i].uch = rez
            Stans_val[i].save()
            if dbg_track: print("UchSTRUCT constructor: Stans[%d]:\n%s" % (i, Stans_val[i]))

        for i in range(CATEGS_dim):
            CATEGS_val[i].uch = rez
            CATEGS_val[i].save()
            if dbg_track: print("UchSTRUCT constructor: CATEGS[%d]:\n%s" % (i, CATEGS_val[i]))

        return rez


class StansSTRUCT(models.Model):
    Nam = models.CharField(max_length=50, default='')
    Kod = models.IntegerField(default=0)
    Obg = models.IntegerField(default=0)
    MputPrg = models.IntegerField(default=0)
    RsrvS1 = models.IntegerField(default=0)
    Kml = ArrayField(ArrayField(models.FloatField(default=0.0)))
    uch = models.ForeignKey(UchSTRUCT, on_delete=models.CASCADE, default=None)

    def __str__(self):
        s = str.format(
            "id:%d;Nam:%s;Kod:%d;Obg:%d;" % (self.id, self.Nam, self.Kod, self.Obg))
        s = s + str.format("MputPrg:%d;RsrvS1:%d;Kml:" % (self.MputPrg, self.RsrvS1))
        for i in range(len(self.Kml)):
            s = s + str.format(";[%d]:%f" % (i, self.Kml[i][0]))
        return s

    @classmethod
    def from_txt(cls, f):
        Nam_val = read_string(f)
        Kod_val = read_integer(f)
        Obg_val = read_integer(f)
        MputPrg_val = read_integer(f)
        RsrvS1_val = read_integer(f)

        KmlDim = get_diap(f)
        i_max = KmlDim[1][0] - KmlDim[0][0] + 1
        j_max = KmlDim[1][1] - KmlDim[0][1] + 1
        Kml_val = [[0.0 for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                Kml_val[i][j] = read_float(f)

        rez = cls(Nam=Nam_val, Kod=Kod_val, Obg=Obg_val, MputPrg=MputPrg_val, RsrvS1=RsrvS1_val, Kml=Kml_val)
        return rez


class CategSTRUCT(models.Model):
    CatgNam = models.CharField(max_length=50, default='')
    PutSpec = models.IntegerField(default=0)
    RsrvC1 = models.FloatField(default=0.0)
    TrTYP = ArrayField(ArrayField(models.IntegerField(default=0)))
    uch = models.ForeignKey(UchSTRUCT, on_delete=models.CASCADE, default=None)

    def __str__(self):
        s = str.format("CategSTRUCT: self.id: %d, CatgNam: %s, PutSpec: %d, RsrvC1: %f\n" % (
        self.id, self.CatgNam, self.PutSpec, self.RsrvC1))
        for i in range(len(self.TrTYP)):
            for j in range(len(self.TrTYP[i])):
                s = s + str.format("TrTYP[%d,%d]: %d\n" % (i, j, self.TrTYP[i][j]))
        return s

    @classmethod
    def from_txt(cls, f):
        CatgNam_val = read_string(f)
        PutSpec_val = read_integer(f)
        RsrvC1_val = read_float(f)

        TrTYPDim = get_diap(f)
        i_max = TrTYPDim[1][0] - TrTYPDim[0][0] + 1
        j_max = TrTYPDim[1][1] - TrTYPDim[0][1] + 1
        TrTYP_val = [[0 for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                TrTYP_val[i][j] = read_integer(f)

        rez = cls(CatgNam=CatgNam_val, PutSpec=PutSpec_val, RsrvC1=RsrvC1_val, TrTYP=TrTYP_val)
        return rez

