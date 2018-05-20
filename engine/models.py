from django.db import models
from django.contrib.postgres.fields import ArrayField
from data.txt import get_diap, read_string, read_integer, read_float
from . import dbg_engine


class LocomSTRUCT(models.Model):
    Vers = models.FloatField(default=0.0)
    LocmTyp = models.CharField(max_length=50)
    Rdnz = models.IntegerField(default=0)
    UTnom = models.FloatField(default=0.0)
    Comment = models.CharField(max_length=200)
    Rsrv0 = models.IntegerField(default=0)
    Phor = models.FloatField(default=0.0)
    DvgNam = models.CharField(max_length=50)
    Ploc = models.FloatField(default=0.0)
    Lloc = models.FloatField(default=0.0)
    Vloc = models.FloatField(default=0.0)
    Pbsm = models.FloatField(default=0.0)
    Ibsm = models.FloatField(default=0.0)
    MxPoz = models.IntegerField(default=0)
    # XapSTRUCT[] TGxp;
    LocWo = ArrayField(ArrayField(ArrayField(models.FloatField())))
    Koefs = ArrayField(models.FloatField())
    Tdop = models.FloatField(default=0.0)
    MxTau = models.IntegerField(default=0)
    Tau8 = ArrayField(ArrayField(models.FloatField()))
    MxPozRc = models.IntegerField(default=0)
    # XapSTRUCT[] RCxp;
    Rsrv1 = models.IntegerField(default=0)
    Rsrv2 = models.FloatField(default=0.0)
    Rsrv3 = models.FloatField(default=0.0)
    Rsrv4 = models.FloatField(default=0.0)

    def __str__(self):
        s = str.format("LocomSTRUCT: self.id: %d, Vers: %f, LocmTyp: '%s'\n" % (self.id, self.Vers, self.LocmTyp))
        s = s + str.format("Rdnz: %d, UTnom: %f, Comment: '%s'\n" % (self.Rdnz, self.UTnom, self.Comment))
        s = s + str.format("Rsrv0: %d, Phor: %f, DvgNam: '%s', Ploc: %f\n" % (self.Rsrv0, self.Phor, self.DvgNam, self.Ploc))
        s = s + str.format("Lloc: %f, Vloc: %f, Pbsm: %f, Ibsm: %f, MxPoz: %d\n" % (self.Lloc, self.Vloc, self.Pbsm, self.Ibsm, self.MxPoz))
        s = s + str.format("TGxp: %d items, " % len(self.xapstruct_tgxp_set.all()))
        s = s + str.format("LocWo: %d * %d * %d  items\n" % (len(self.LocWo), len(self.LocWo[0]), len(self.LocWo[0][0])))
        s = s + str.format("Koefs: %d items, Tdop: %f, MxTau: %d, " % (len(self.Koefs), self.Tdop, self.MxTau))
        s = s + str.format("Tau8: %d * %d items, MxPozRc: %d\n" % (len(self.Tau8), len(self.Tau8[0]), self.MxPozRc))
        s = s + str.format("RCxp: %d items, Rsrv1: %d, " % (len(self.xapstruct_rcxp_set.all()), self.Rsrv1))
        s = s + str.format("Rsrv2: %f, Rsrv3: %f, Rsrv4: %f\n" % (self.Rsrv2, self.Rsrv3, self.Rsrv4))
        s = s + "item's xapstruct_tgxp:\n"
        for x in self.xapstruct_tgxp_set.all(): s = s + str(x) + '\n'
        s = s + "item's xapstruct_rcxp:\n"
        for x in self.xapstruct_rcxp_set.all(): s = s + str(x) + '\n'
        return s

    @classmethod
    def from_txt(cls, f):
        Vers_val = read_float(f)
        LocmTyp_val = read_string(f)
        Rdnz_val = read_integer(f)
        UTnom_val = read_float(f)
        Comment_val = read_string(f)
        Rsrv0_val = read_integer(f)
        Phor_val = read_float(f)
        DvgNam_val = read_string(f)
        Ploc_val = read_float(f)
        Lloc_val = read_float(f)
        Vloc_val = read_float(f)
        Pbsm_val = read_float(f)
        Ibsm_val = read_float(f)
        MxPoz_val = read_integer(f)

        lng = get_diap(f)
        TGxp_dim = lng[1][0] - lng[0][0] + 1
        TG_val = [None for j in range(TGxp_dim)]
        for i in range(TGxp_dim):
            TG_val[i] = XapSTRUCT_TGxp.from_txt(f)

        lng = get_diap(f)
        i_max = lng[1][0] - lng[0][0] + 1
        j_max = lng[1][1] - lng[0][1] + 1
        k_max = lng[1][2] - lng[0][2] + 1

        LocWo_val = [[[0.0 for k in range(k_max)] for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                for k in range(k_max):
                    if dbg_engine: print("LocomSTRUCT constructor: LocWo [%d, %d, %d]" % (i, j, k))
                    LocWo_val[i][j][k] = read_float(f)

        lng = get_diap(f)
        i_max = lng[1][0] - lng[0][0] + 1
        Koefs_val = [0.0 for i in range(i_max)]
        for i in range(i_max):
            if dbg_engine: print("LocomSTRUCT constructor: Koefs [%d]" % (i))
            Koefs_val[i] = read_float(f)

        Tdop_val = read_float(f)
        MxTau_val = read_integer(f)

        lng = get_diap(f)
        i_max = lng[1][0] - lng[0][0] + 1
        j_max = lng[1][1] - lng[0][1] + 1
        Tau8_val = [[0.0 for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                if dbg_engine: print("LocomSTRUCT constructor: Tau8_val [%d, %d]" % (i, j))
                Tau8_val[i][j] = read_float(f)

        MxPozRc_val = read_integer(f)

        lng = get_diap(f)
        RCxp_dim = lng[1][0] - lng[0][0] + 1
        RC_val = [None for j in range(RCxp_dim)]
        for i in range(RCxp_dim):
            RC_val[i] = XapSTRUCT_RCxp.from_txt(f)

        Rsrv1_val = read_integer(f)
        Rsrv2_val = read_float(f)
        Rsrv3_val = read_float(f)
        Rsrv4_val = read_float(f)

        rez = cls(Vers=Vers_val, LocmTyp=LocmTyp_val, Rdnz=Rdnz_val, UTnom=UTnom_val, Comment=Comment_val,
                  Rsrv0=Rsrv0_val, Phor=Phor_val, DvgNam=DvgNam_val, Ploc=Ploc_val, Lloc=Lloc_val,
                  Vloc=Vloc_val, Pbsm=Pbsm_val, Ibsm=Ibsm_val, MxPoz=MxPoz_val, LocWo=LocWo_val,
                  Koefs=Koefs_val, Tdop=Tdop_val, MxTau=MxTau_val, Tau8=Tau8_val, MxPozRc=MxPozRc_val,
                  Rsrv1=Rsrv1_val, Rsrv2=Rsrv2_val, Rsrv3=Rsrv3_val, Rsrv4=Rsrv4_val)
        rez.save()

        for i in range(TGxp_dim):
            TG_val[i].xp = rez
            TG_val[i].save()
        for i in range(RCxp_dim):
            RC_val[i].xp = rez
            RC_val[i].save()

            if dbg_engine: print("LocomSTRUCT constructor: rez.id: %d" % (rez.id))
        return rez


class XapSTRUCT_TGxp(models.Model):
    PozNam = models.CharField(max_length=200, default='')
    MxXap = models.IntegerField(default=0)
    Exap = ArrayField(ArrayField(models.FloatField(default=0.0)))
    xp = models.ForeignKey(LocomSTRUCT, on_delete=models.CASCADE, default=None)

    def __str__(self):
        s = str.format("XapSTRUCT_TGxp: PozNam: '%s', MxXap: %s, " % (self.PozNam, self.MxXap))
        s = s + str.format("Exap: %d * %d items" % (len(self.Exap), len(self.Exap[0])))
        return s

    @classmethod
    def from_txt(cls, f):
        PozNam_val = read_string(f)
        MxXap_val = read_integer(f)

        ExapDim = get_diap(f)
        i_max = ExapDim[1][0] - ExapDim[0][0] + 1
        j_max = ExapDim[1][1] - ExapDim[0][1] + 1

        Exap_val = [[0.0 for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                Exap_val[i][j] = read_float(f)

        rez = cls(PozNam=PozNam_val, MxXap=MxXap_val, Exap=Exap_val)

        return rez


class XapSTRUCT_RCxp(models.Model):
    PozNam = models.CharField(max_length=200, default='')
    MxXap = models.IntegerField(default=0)
    Exap = ArrayField(ArrayField(models.FloatField(default=0.0)))
    xp = models.ForeignKey(LocomSTRUCT, on_delete=models.CASCADE, default=None)

    def __str__(self):
        s = str.format("XapSTRUCT_RCxp: PozNam: '%s', MxXap: %s, " % (self.PozNam, self.MxXap))
        s = s + str.format("Exap: %d * %d items" % (len(self.Exap), len(self.Exap[0])))

    @classmethod
    def from_txt(cls, f):
        PozNam_val = read_string(f)
        MxXap_val = read_integer(f)

        ExapDim = get_diap(f)
        i_max = ExapDim[1][0] - ExapDim[0][0] + 1
        j_max = ExapDim[1][1] - ExapDim[0][1] + 1

        Exap_val = [[0.0 for j in range(j_max)] for i in range(i_max)]
        for i in range(i_max):
            for j in range(j_max):
                Exap_val[i][j] = read_float(f)

        rez = cls(PozNam=PozNam_val, MxXap=MxXap_val, Exap=Exap_val)
        return rez


