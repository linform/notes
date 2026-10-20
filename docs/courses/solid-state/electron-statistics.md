---
title: 第四章（三）　电子统计与运动
description: 固体物理分章笔记，包含学习目标、推导、课件定位、小结与自测。
status: 已整理
tags:
  - 态密度
  - 费米统计
  - 热容
  - 有效质量
---

# 第四章（三）　电子统计与运动

[课程概览](index.md) · [符号约定](index.md#symbols) · [来源与订正](references.md)

!!! abstract "本章课件与配套阅读"
    **原始 PPTX**：[S12 · 31 页 · 8.1 MiB](../../assets/solid-state/slides/s12.pptx){ download="固体物理（2班）4.能带理论（4）.pptx" }。

    **对照阅读**：DOS 与电子热容：Simon；费米面、群速度和有效质量：Tong 第 3 章。

    [Simon 官方全文 PDF](references.md#simon) · [Tong 全文与分章 PDF](references.md#tong) · [全部课件](index.md#course-sources)

## 学习目标

- 统一态密度的总量、体积和自旋约定。
- 固定电子数理解低温热容，并由色散求群速度与质量张量。

## 前置知识

费米分布、定积分、二阶导数；周期势与带号约定见上一页。

## 核心内容

<!-- course:body -->

### 4.12 电子态密度：从整个布里渊区计数

来源：S12，第 2–7 页。

定义样品总态密度 $D(\varepsilon)$，使 $D(\varepsilon)d\varepsilon$ 为能量区间内的单电子态数；若单位体积态密度为 $\mathcal D$，则 $D=\mathcal V\mathcal D$。自旋简并且能带未单独计入自旋时，

$$
D(\varepsilon)=\frac{2\mathcal V}{(2\pi)^3}
\sum_n\int_{\mathrm{BZ}}d^3k\,
\delta(\varepsilon-\varepsilon_n(\mathbf k)).
$$

在非临界等能面上也可写作 $D=2\mathcal V(2\pi)^{-3}\sum_n\int dS/|\nabla_{\mathbf k}\varepsilon_n|$，因此色散平坦处可积聚较多态。驻点处需另行分析奇性。**沿一条高对称线均匀取点，不能代替整个布里渊区的 DOS 积分。**

以三维自由电子带底为零，能量低于 $\varepsilon$ 的态数为

$$
\mathcal N(\varepsilon)=\frac{2\mathcal V}{(2\pi)^3}\frac{4\pi k^3}3
=\frac{\mathcal V}{3\pi^2}\left(\frac{2m_e\varepsilon}{\hbar^2}\right)^{3/2}.
$$

求导得

$$
\boxed{D_{\mathrm{3D}}(\varepsilon)=\frac{\mathcal V}{2\pi^2}
\left(\frac{2m_e}{\hbar^2}\right)^{3/2}\sqrt\varepsilon},\qquad\varepsilon>0.
$$

二维面积 $A$、一维长度 $L$ 的抛物线色散给出（均含自旋 2）

$$
D_{\mathrm{2D}}=\frac{Am_e}{\pi\hbar^2},\qquad
D_{\mathrm{1D}}=\frac L{\pi\hbar}\sqrt{\frac{2m_e}{\varepsilon}}.
$$

一般各向同性单调色散 $\varepsilon=\alpha k^P$（$\alpha,P>0$）在 $d$ 维满足 $D\propto\varepsilon^{d/P-1}$。因此二维 Dirac 锥的 DOS 正比于相对 Dirac 点能量的绝对值。这个幂律不适用于二维鞍点，石墨烯 $M$ 点的 van Hove 奇性需要从鞍点色散单独求得。

### 4.13 费米面、化学势与有限温度占据

来源：S12，第 8–17 页。

对互不作用／有效独立电子，单个自旋态的平均占据为

$$
f(\varepsilon;\mu,T)=\frac1{e^{(\varepsilon-\mu)/(k_BT)}+1},
\qquad
N_e=\int D(\varepsilon)f(\varepsilon;\mu,T)d\varepsilon.
$$

若 $D$ 已含自旋简并，积分外不要再乘 2。$\mu=(\partial F/\partial N_e)_{T,\mathcal V}$ 由固定电子数条件确定；$f(\mu)=1/2$ 是分布函数的性质，并不保证能谱中存在能量恰为 $\mu$ 的态。

零温金属由低到高填充至 $E_F=\mu(0)$。费米面由 $\varepsilon_n(\mathbf k)=E_F$ 定义，一维通常是点、二维是线、三维是面。对于带隙绝缘体，零温化学势可位于禁带内，不能把它简单等同于「最高已占据能级」，也没有穿过禁带的费米面。

三维自由电子令 $n_e=N_e/\mathcal V$，由球内态数得到

$$
\boxed{k_F=(3\pi^2n_e)^{1/3}},\qquad
E_F=\frac{\hbar^2k_F^2}{2m_e},\quad
T_F=\frac{E_F}{k_B},\quad v_F=\frac{\hbar k_F}{m_e}.
$$

当 $T\ll T_F$ 时，热激发主要发生在 $\mu$ 附近宽约 $k_BT$ 的窗口。经典 Boltzmann 极限要求有关能量满足 $\varepsilon-\mu\gg k_BT$，此时 $f\approx e^{-(\varepsilon-\mu)/(k_BT)}$；仅写 $\varepsilon\gg\mu$ 不足以判断。

### 4.14 Sommerfeld 展开与电子热容

来源：S12，第 13–19 页。以下固定 $N_e$ 和体积，并要求 DOS 在 $E_F$ 附近足够平滑，温度远低于相关能量尺度。

Sommerfeld 展开把费米分布积分转化为

$$
\int\Phi(\varepsilon)f\,d\varepsilon
=\int^{\mu}\Phi(\varepsilon)d\varepsilon
+\frac{\pi^2}{6}(k_BT)^2\Phi'(\mu)+O(T^4).
$$

对粒子数取 $\Phi=D$，令 $\mu=E_F+\delta\mu$ 并保留 $T^2$ 项：

$$
0=D(E_F)\delta\mu+\frac{\pi^2}{6}(k_BT)^2D'(E_F),
$$

$$
\boxed{\mu(T)=E_F-\frac{\pi^2}{6}(k_BT)^2\frac{D'(E_F)}{D(E_F)}+O(T^4)}.
$$

三维抛物线带给出 $\mu=E_F[1-\pi^2(T/T_F)^2/12+\cdots]$；一维因 $D'<0$ 而低温先升高。二维常 DOS 的 $T^2$ 修正为零，但考虑带底后精确结果为

$$
\mu(T)=k_BT\ln\left(e^{E_F/(k_BT)}-1\right)
=E_F+k_BT\ln\left(1-e^{-E_F/(k_BT)}\right),
$$

低温有指数小的下降，不能说所有维度的化学势都随温度按同一个公式降低。

总电子能量 $U=\int\varepsilon D(\varepsilon)f\,d\varepsilon$。用 $\Phi=\varepsilon D$ 展开，并代入刚求出的 $\delta\mu$，其中 $E_FD'(E_F)$ 项抵消：

$$
U(T)-U(0)=\frac{\pi^2}{6}D(E_F)(k_BT)^2+O(T^4),
$$

$$
\boxed{C_{V,e}=\gamma T+O(T^3),\qquad
\gamma=\frac{\pi^2}{3}k_B^2D(E_F)}.
$$

三维自由电子有 $U(0)=3N_eE_F/5$、$D(E_F)=3N_e/(2E_F)$，故 $C_{V,e}=(\pi^2/2)N_ek_B T/T_F$。只有费米面附近少量电子参与热激发，是热容远小于经典估计的原因；不能给所有电子套用经典能量均分。

普通三维金属的足够低温区常拟合 $C_V=\gamma T+AT^3$，分别来自电子和声学声子。画 $C_V/T$ 对 $T^2$，截距为 $\gamma$、斜率为 $A$；交叉温度约为 $\sqrt{\gamma/A}$，由材料决定。

### 4.15 能带填充与导电性

来源：S12，第 20–23 页；S11，第 24–26 页。

在普通独立电子能带图像中，金属的化学势切过可导电的部分填充能带；若零温价带全满、导带全空，且二者间有正的全局带隙，则是带绝缘体。半导体与绝缘体没有统一的严格带隙数值分界，还需结合温度、掺杂和应用情境。

「导带」通常指半导体／绝缘体价带上方的能带，零温时可以完全空着，并非「部分填充能带」的同义词。金属在某些能量或某些 $\mathbf k$ 处仍可有带隙；关键是费米能附近的填充结构。石墨烯的理想 Dirac 点又是能带相接的特殊情形，不能用普通有限 DOS 金属图像直接替代。

通常群速度和电流为

$$
\mathbf v_n(\mathbf k)=\frac1\hbar\nabla_{\mathbf k}\varepsilon_n(\mathbf k),
\qquad
\mathbf j=-\frac{2e}{\mathcal V}\sum_{n\mathbf k}f_{n\mathbf k}\mathbf v_n(\mathbf k).
$$

满带对整个 BZ 求和，周期能量在相对边界的贡献相消，因此 $\int_{\mathrm{BZ}}\nabla_{\mathbf k}\varepsilon_n\,d^3k=0$。部分填充带在电场下可改变分布并产生电流。这里讨论通常的带内纵向输运；Berry 曲率的横向响应和带间激发需另行处理。获得稳态 Ohm 电流还需要散射／弛豫机制，不能从无散射的静态能带独自推出电阻率。

直接／间接带隙也有光学意义：光子动量通常很小，直接带间跃迁近似保持 $\mathbf k$；间接带边跃迁往往需要声子等协助动量守恒。实际吸收还取决于跃迁矩阵元与选择定则，能量允许并不保证强吸收。

### 4.16 半经典运动与有效质量

来源：S12，第 24、26–31 页。

在外场缓慢变化、波包主要留在同一孤立能带、忽略 Berry 修正的条件下：

$$
\dot{\mathbf r}=\frac1\hbar\nabla_{\mathbf k}\varepsilon_n,
\qquad \hbar\dot{\mathbf k}=-e(\mathbf E+\dot{\mathbf r}\times\mathbf B),
\quad e>0.
$$

对速度求时间导数，定义逆有效质量张量

$$
\boxed{(m^{*-1})_{ij}=\frac1{\hbar^2}
\frac{\partial^2\varepsilon_n}{\partial k_i\partial k_j}},
\qquad \dot v_i=\sum_j(m^{*-1})_{ij}F_j.
$$

这里 $m^{*-1}$ 是矩阵；求 $m^*$ 需要矩阵求逆，不能对每个非对角元素分别取倒数。主轴坐标下二次带底可写为 $\varepsilon_c+\sum_i\hbar^2q_i^2/(2m_i^*)$。

一维 $m^*=\hbar^2/(d^2\varepsilon/dk^2)$：带底正曲率对应正质量，带顶负曲率对应负电子有效质量。接近满带时，用缺失电子形成的正电荷空穴描述，空穴在价带顶附近有正质量。有效质量描述晶格势已包含在色散中的响应，不应再另加一份相同的周期势力而重复计数。

**实验联系**：各向同性抛物线带的回旋频率 $\omega_c=eB/|m^*|$；椭球色散中若 $\mathbf B\parallel z$，回旋质量为 $\sqrt{m_x^*m_y^*}$（正质量载流子）。DOS 质量、输运质量和回旋质量由不同方向／平均方式决定，一般不能直接混同。回旋共振需散射足够弱，通常要求 $\omega_c\tau\gtrsim1$。

### 4.17 Bloch 振荡：恒力不一定使速度一直增大

来源：S12，第 24–25 页。

一维恒电场下 $\hbar\dot k=-eE$，因能带以 $2\pi/a$ 为周期，速度也随时间周期变化：

$$
\boxed{T_B=\frac{2\pi\hbar}{e|E|a}},\qquad
\omega_B=\frac{e|E|a}{\hbar}.
$$

用最近邻色散 $\varepsilon(k)=\varepsilon_c-2J\cos(ka)$、$J>0$，得

$$
k(t)=k_0-\frac{eEt}{\hbar},\qquad
v(t)=\frac{2Ja}{\hbar}\sin[k(t)a],
$$

$$
x(t)-x(0)=\frac{2J}{eE}\{\cos[k(t)a]-\cos(k_0a)\}.
$$

这里 $J$ 为固定的正跃迁能量，$t$ 为时间。观察条件是 $T_B$ 小于散射时间的量级，同时电场不能强到导致显著带间 Zener 跃迁；仅增大电场并不保证观察成功。

按 $T_B=\tau$ 估计：$a=3\,\text{Å}$、$\tau=10^{-14}\,\mathrm s$ 给出约 $1.38\times10^7\,\mathrm{V/cm}$；超晶格 $a=10\,\mathrm{nm}$、$\tau=10^{-13}\,\mathrm s$ 时约为 $4.14\times10^4\,\mathrm{V/cm}$。较大的周期有利于降低所需电场，数值需保留 $2\pi$ 因子。

<!-- /course:body -->

## 本章小结

电子统计由可用态和占据共同决定。低温热激发集中在化学势附近；半经典运动分别由外场改变波矢和能带梯度决定速度。

## 自测与练习

先独立作答，再展开答案核对。

<!-- quiz:q20,q21,q22,q23,q24,q25,q26 -->

[对应练习与检查方向](exercises.md#ex-09) · [全部闭卷自测](review.md#self-test)

## 下一步

[上一单元：第四章（二）　周期势与带隙](bloch.md) · [下一单元：第四章（四）　紧束缚与石墨烯](tight-binding.md)
