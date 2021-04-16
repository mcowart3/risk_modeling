class Territory:
    def __init__(self, continent, connected, owner, count):
        self.continent = continent
        self.connected = connected
        self.count = 0
alaska = Territory(na, [canada_nw, kamchatka, alberta])
canada_nw = Territory(na, [alaska, ontario, alberta, greenland])
alberta = Territory(na, [canada_nw, alaska, ontario, us_w])
ontario = Territory(na, [canada_nw, greenland, alberta, canada_e, us_w, us_e])
canada_e = Territory(na, [ontario, greenland, us_e])
greenland = Territory(na, [canada_nw, ontario, canada_e, iceland])
us_w = Territory(na, [alberta, ontario, us_e, central_am])
us_e = Territory(na, [central_am, us_w, ontario, canada_e])
central_am = Territory(na, [us_w, us_e, venezuela])
venezuela = Territory(sa, [central_am, brazil, peru])
