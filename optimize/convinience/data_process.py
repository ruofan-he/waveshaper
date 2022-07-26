
class data_class:
    data = None
    def __init__(self, data):
        self.data = data

    def apply(self, func, **kwarg):
        self.data = func(self.data, **kwarg)
        return self


# 使用例はこんなかんじ。メソッドチェーンが使用できないデータにも、メソッドチェーン記法を無理やり使えるようにする、ゴリ押しのやり方。
# ワンライナーで処理ラムダ式を使えていいね笑。
# extract        = lambda volts: data_class(volts[150:300]).apply(np.sum, axis = 0).data
# extract        = lambda volts: PCA().fit(volts.T).transform(volts.T)[:,0]
# sub_mean       = lambda volts: volts - volts.mean()
# get_clipped    = lambda volts: volts * (volts > -1) * (volts < 1)
# get_quadrature = lambda volts: data_class(volts).apply(extract).apply(sub_mean).apply(get_clipped).data