# WSMethods
Finisar Waveshaper公式Pythonライブラリ。ま、ただのデータ転送ライブラリだわな。

createWSPString: 単にnumpy arrayで入れた、各周波数の減衰量、位相シフト、各ポート情報を、よくある.wspファイル形式でStringに変換する。
0dB~60dBの減衰しかできない。まあ十分。この関数にはお世話になるかもしれないし、ならないかもしれない。WSPファイル形式で保存するときにお世話になるかも。

splitWspString: .wspファイル形式でかかれたStringを、それぞれのカラムに分解する。使うかもしれない。

uploadPredefinedProfile: 予め端末上で決められたフィルタープロファイルで設定する。(たとえばガウシアンモードとか)。使わない。仕様が不明

uploadProfile: numpy array形式で、減衰量、位相シフトのフィルタプロファイルをアップロードする。

