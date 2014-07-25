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
**程式中energy_fit所代表的就是根據模型每一個x所會對應到的y**

```
# put the fitted line into the plot
# first : construct the background
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# second : add point into it.
ax.scatter(Wt, Energy)
ax.plot(Wt,energy_fit,color='green')
ax.scatter(x_bar,y_bar,color='red')
ax.set_xlabel('Weight of sheep')
ax.set_ylabel('energy requirements')
ax.set_title('Scatter plot between Weight and Energy requirements')
```

接著此步驟為將模型畫上去上面的資料散布圖，因此這個畫圖的程式碼只是比上面那個畫圖的多了一行:**ax.plot(Wt,energy_fit,color='green')**，目的是透過這個圖形可以透過觀察的方式先去看我們的模型與實際上資料的契合度。
一個配適的好的模型，由圖形上會看得出來其模型的變動大致描述了大部分的資料。

**不過這一切都還是感官的感覺，實際上在統計上會進一步作model checking來看模型到底配適的好不好。**

## step4. Model Checking

model checking的部份，針對模型的一些基本假設進行檢定。在模型: **yi = a * xi + b + ei**中ei代表每個觀察值的殘差，其中ei有幾個簡單的性質:

> - ei~N(0,1) **殘差符合平均數為零標準差為一的常態分配**
> - ei的期望值=0 **E(ei) = 0**

在樣本中，我們用樣本的殘差去看常態性，以及同質性以及線性的關係。（常態性我還不會做XD）
**殘差代表的就是圖形中一個x所對應到的模型配適y和實際觀察值y的差距**

```
#residual
res = []
for i in range(len(Energy)):
    res.append(Energy[i]-energy_fit[i])
res
#residual plot
fig = plt.figure() 
ax = fig.add_subplot(1,1,1)
ax.scatter(energy_fit, res)
```
我們畫residual plot **(fitted value vs. residuals)**來看其殘差分布隨著配適值改變而變動的狀況。
如果隨著配適值的改變，其殘差有著特定的方向改變，則代表此資料不符合線性的模型。
另外若殘差的分布是均勻的，也代表著資料本身具有同質性

**簡單來說殘差圖如果資料看起來愈散佈，不特別往哪個部分集中，或是長得有特定形狀的樣子，那就是愈好。**






