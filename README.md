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

以下會針對程式碼每一個部分進行比較詳細的解釋。


## Step1. Import data
```
energy = pd.read_csv('/Users/tzeng/Desktop/data_energy.csv')
Wt = energy.Wt.tolist()
Energy = energy.Energy.tolist()
```
第一行是將csv檔 data_energy.csv 匯入，匯入後其格式會是pandas上的dataframe格式，
接著第二及第三行的目的是將x與y的資料由dataframe的形式轉換成list的形式，以便後面的分析及畫圖。

接著在進入第二步之前，我想先知道這筆資料的樣本平均數以便可以在第二步的時候同時放進圖形中觀察。

```
x_bar = 0
for i in Wt:
    x_bar = x_bar + i
x_bar = x_bar/len(Wt)
print(x_bar)

y_bar = 0
for i in Energy:
    y_bar = y_bar + i
y_bar = y_bar/len(Energy)
print(y_bar)
```
x_bar及y_bar分別為資料中 Weights(x)及Energy requirements(y)的樣本平均數，透過for迴圈將每一項
加起來再除上樣本個數(即為list的長度)，即為樣本平均數。

## Step2. Specify an initial model
```
# first : construct the background
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# second : add point into it.
ax.scatter(Wt, Energy)
ax.scatter(x_bar,y_bar,color='red')
ax.set_xlabel('Weight of sheep')
ax.set_ylabel('energy requirements')
ax.set_title('Scatter plot between Weight and Energy requirements')
```
畫圖主要分成兩個部分，第一個是架構外面的框框，第二個部分是將資料丟進去描點。

透過圖形可以看出隨著weights變大 energy requirements有變大的趨勢，因此我們用簡單線性模型來當我們的初步模型，也就是：
**y = a * x + b**

完成初步模型的假設之後，接著我們嘗試用ordinal least square (OLS)的迴歸分析下去預估**a**和**b**

## Step3. Estimation for unknown parameters
```
# run an OLS regression analysis
result = sm.ols(formula='Energy ~ Wt', data=energy)
fitted = result.fit()
print (fitted.summary())
```
執行完上述的程式後，會有一整個看起來很複雜的表格，不過實際上在看 estimasted parameters只要看下面那個表格關係：

            |coef.
------------|-------
Intercept   |0.1329
Wt          |0.0434

這個部分0.0434為模型中a的估計值，0.1329為模型中b的估計值。

```
# put the estimated parameters into the model
a = 0.0434
b = 0.1329
energy_fit = []
for i in Wt:
    i = i * a + b
    energy_fit.append(i)
energy_fit2 = []
```

接著將估計好的值放回模型中: **y = 0.0434 * x + 0.1329**

再將配適的模型畫到圖形上之前，我們先將每一個x在模型上所應該對應到的配適值y : 
<!--- 程式中energy_fit所代表的就是根據模型每一個x所會對應到的y -->





