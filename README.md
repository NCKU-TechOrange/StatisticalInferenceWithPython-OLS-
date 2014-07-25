StatisticalInferenceWithPython-OLS-
===================================

using OLS regression analysis as an example to do a basic statistical inference.

這個例子是用python來做基本的統計推論。以下用簡單線性模型的例子，透過最小平方迴歸分析法來做統計推論。
ps.此例子是在 ipython notebook上執行

> **Statistical Inference Procedure:**
> - Import data : 匯入資料
> - Specify an initial model : 透過圖形的觀察來預測適當的模型以配適
> - Estimation for unknown parameters : 用適當的迴歸分析法來估計未知的母體參數
> - Model Checking : 最後去看自己所配適的模型是否符合本身方法的假設，
如果不符合的話那就再回到第二步 **Specify an initial model** 去重新找模型。

Step1. Import data
```
energy = pd.read_csv('/Users/tzeng/Desktop/data_energy.csv')
Wt = energy.Wt.tolist()
Energy = energy.Energy.tolist()
```
將csv檔 data_energy.csv 匯入，匯入後其格式會是pandas上的dataframe格式

接著第二及第三行的目的是將x與y的資料由dataframe的形式轉換成list的形式，以便後面的分析及畫圖。



