---
title: 固体物理 · 课件作业与解析
description: 汇总 14 份课件中的全部明确作业：晶体结构、晶体结合、一维德拜模型、二维周期势和 p 轨道能带，附题目、推导与答案。
status: 已整理
tags:
  - 习题与自测
---

# 习题与解析

[返回课程概览](index.md) · [复习速查](review.md) · [原始课件索引](index.md#course-sources)

<div class="notes-section-jump" markdown="1">

**按章定位**：[题目索引](#homework-index) · [第一章（例 1–3）](#ex-01) · [第二章（例 4–5）](#ex-04) · [第三章（例 6）](#ex-06) · [第四章（例 7–8）](#ex-07) · [预习与课堂练习](#preparation-tasks) · [补充练习（例 9–10）](#extra-practice)

</div>

本页按课件原题整理，先读每题的“题目”，独立作答后再核对解析。需要的基础可从[晶体结构](structure.md)、[晶体结合](bonding.md)、[晶格振动](phonons.md)、[周期势与带隙](bloch.md)和[紧束缚](tight-binding.md)查阅。

<!-- course:body -->

<span id="homework-index"></span>

## 作业范围与题目索引

逐页核对现有 S1–S14 共 551 页课件中的作业、课后任务和课堂练习。明确标为“作业”的共有 **8 页**；S10 第 29 页与 S11 第 19 页是同一道二维周期势题，合并后为 **7 组作业**。其中 S5 一页有两道独立题，本页依次整理成**例 1–8**，保留所有小问。以下页码均为 PPTX 文件内的幻灯片序号。

| 课件与页码（点击下载原件） | 原课件标注 | 本页题目与覆盖内容 |
| --- | --- | --- |
| [S2，第 34 页](../../assets/solid-state/slides/s02.pptx) | 课后作业，需上交 | [例 1](#ex-01)：晶体学限制、准晶五重对称、正四面体群的全部操作 |
| [S3，第 14 页](../../assets/solid-state/slides/s03.pptx) | 作业，需要上交 | [例 2](#ex-02)：Al 面间距、Fe 晶格常数 |
| [S3，第 33 页](../../assets/solid-state/slides/s03.pptx) | 作业，需要上交 | [例 3](#ex-03)：FCC／BCC 倒格子及正倒晶格常数关系 |
| [S5，第 27 页](../../assets/solid-state/slides/s05.pptx) | 作业，需要上交 | [例 4](#ex-04)：一维马德隆常数；[例 5](#ex-05)：KCl 压缩压力 |
| [S8，第 43 页](../../assets/solid-state/slides/s08.pptx) | 作业，需要上交 | [例 6](#ex-06)：群速度、德拜态密度与截止、平均能量、热容及高低温极限 |
| [S10，第 29 页](../../assets/solid-state/slides/s10.pptx)；[S11，第 19 页](../../assets/solid-state/slides/s11.pptx) | 作业，同题重复 | [例 7](#ex-07)：中心方程全部非零非对角元、开隙原因、位置、分支与大小 |
| [S13，第 20 页](../../assets/solid-state/slides/s13.pptx) | 作业 | [例 8](#ex-08)：三个 p 轨道色散及 Γ、X、M 点的能量顺序和简并 |

题目按原课件整理为便于独立作答的表述，解析为本笔记推导，**并非教师提供的标准答案**。S2 的“本周日截止”属于原课件历史通知，本页不据此推断当前提交期限。作业中用到的模型前提、能量单位及参数符号在各题说明。

[预习任务与课堂练习](#preparation-tasks)单独收录 S1、S2 的“不需要上交”任务和 S4 的课堂结构因子练习。[例 9–10](#extra-practice)是原笔记的补充练习。

<span id="ex-01"></span>

## 例 1　晶体学限制与正四面体点群

来源：[S2](../../assets/solid-state/slides/s02.pptx)，第 34 页「课后作业（需上交）」。本题含原课件的三个小问。

**题目**

1. 证明：由于平移对称性的存在，三维周期晶体中的旋转对称轴只可能是 1、2、3、4、6 重轴。
2. 为什么准晶可以存在 5 重旋转对称轴？
3. 写出正四面体点群 $T_d$ 的所有对称操作，可使用 Schoenflies 记号或国际记号。

**解析一：用晶格整数矩阵证明晶体学限制**

设三维布拉维格子的原始基矢组成矩阵 $A=(\mathbf a_1,\mathbf a_2,\mathbf a_3)$，格点为 $\mathbf R=A\mathbf n$，其中 $\mathbf n\in\mathbb Z^3$。若纯旋转 $Q$ 保持格子，则每根 $Q\mathbf a_j$ 仍是格矢，因而

$$
QA=AM,\qquad M=A^{-1}QA,
$$

其中 $M$ 的元素全是整数；逆旋转也保持格子，所以 $M^{-1}$ 同样为整数矩阵。特别地，$\operatorname{tr}M$ 为整数。

绕某轴转动 $\theta$ 的三维纯旋转矩阵，其本征值为 $1,e^{i\theta},e^{-i\theta}$。矩阵相似变换不改变迹，故

$$
\operatorname{tr}M=\operatorname{tr}Q=1+2\cos\theta\in\mathbb Z.
$$

又有 $-2\le2\cos\theta\le2$，所以

$$
2\cos\theta\in\{-2,-1,0,1,2\}.
$$

对 $n$ 重轴，取最小正旋转角 $\theta=2\pi/n$（$n=1$ 时为恒等操作），得到

| $n$ | $1$ | $2$ | $3$ | $4$ | $6$ |
| --- | --- | --- | --- | --- | --- |
| $\theta$ | $2\pi$，等价于 $0$ | $\pi$ | $2\pi/3$ | $\pi/2$ | $\pi/3$ |
| $2\cos\theta$ | $2$ | $-2$ | $-1$ | $0$ | $1$ |

因此

$$
\boxed{n=1,2,3,4,6.}
$$

这个论证直接适用于三维周期晶格，不要求旋转轴恰好平行于某根原始基矢。若讨论整个周期晶体，其旋转对称操作也必须保持其布拉维平移格子，因此同样受此限制。

**解析二：准晶为什么允许五重对称**

准晶具有长程有序，但没有能将整体表示成 $A\mathbb Z^3$ 的三维周期平移格子。因此上面的「三根原始基矢下旋转表示为整数矩阵」这一前提不成立，不能据此排除五重旋转。具有适当非周期有序排列的准晶可以出现五重对称；这并不表示所有非周期结构都一定具有五重对称，也不表示周期晶体的限制被推翻。

**解析三：完整列出 $T_d$ 的 24 个操作**

取正四面体的四个顶点为

$$
\mathbf v_1=(1,1,1),\quad
\mathbf v_2=(1,-1,-1),\quad
\mathbf v_3=(-1,1,-1),\quad
\mathbf v_4=(-1,-1,1).
$$

整体尺度不影响点群。下表明确给出每种操作的轴、镜面和转角，因而不仅是操作数目的汇总。

| 操作类别 | 轴、镜面和具体操作 | 个数 |
| --- | --- | ---: |
| $E$ | 恒等操作 | 1 |
| $C_3,C_3^2$ | 沿 $[111]$、$[1\bar1\bar1]$、$[\bar11\bar1]$、$[\bar1\bar11]$ 四根轴，各作 $+120^\circ$ 和 $-120^\circ$ 旋转；每根轴通过一个顶点与对面中心 | 8 |
| $C_2$ | 绕 $x,y,z$ 三根轴，各转 $180^\circ$；各轴连接一对对棱的中点 | 3 |
| $S_4,S_4^3$ | 绕 $x,y,z$ 三根轴，各转 $+90^\circ$ 或 $-90^\circ$，再关于垂直该轴、通过原点的平面反射 | 6 |
| $\sigma_d$ | 分别关于 $x=y$、$x=-y$、$y=z$、$y=-z$、$z=x$、$z=-x$ 六个平面反射 | 6 |

表中转角按右手定则约定。三根 $C_2$ 轴也同时是 $S_4$ 轴，**轴是几何对象，绕轴的不同变换才是不同操作**。例如关于 $z$ 轴的两个 $S_4$ 操作为

$$
(x,y,z)\mapsto(-y,x,-z),\qquad
(x,y,z)\mapsto(y,-x,-z).
$$

为使所有操作都能直接核对，三根轴上的六个 $S_4$ 操作可写成

$$
\begin{aligned}
S_{4x}^{\pm}:&\quad (x,y,z)\mapsto(-x,\mp z,\pm y),\\
S_{4y}^{\pm}:&\quad (x,y,z)\mapsto(\pm z,-y,\mp x),\\
S_{4z}^{\pm}:&\quad (x,y,z)\mapsto(\mp y,\pm x,-z).
\end{aligned}
$$

还可用一个坐标规则无遗漏地生成全体 24 个操作：任选坐标置换 $p\in S_3$，再选取 $\epsilon_i=\pm1$ 且 $\epsilon_1\epsilon_2\epsilon_3=+1$，令

$$
(x_1,x_2,x_3)\mapsto
(\epsilon_1x_{p(1)},\epsilon_2x_{p(2)},\epsilon_3x_{p(3)}).
$$

四个顶点都满足 $x_1x_2x_3=1$，故上述变换保持顶点集合。共有 $6\times4=24$ 个不同操作；另一方面，任何正四面体对称操作都置换四个顶点，至多有 $4!=24$ 种，所以已经列全。偶置换给出 12 个纯旋转 $E+8C_3+3C_2$，奇置换给出 12 个非正常操作 $6S_4+6\sigma_d$。

最终为

$$
\boxed{T_d:\quad E+8C_3+3C_2+6S_4+6\sigma_d,\qquad |T_d|=24.}
$$

该点群的国际记号是 $\bar43m$。

**易错点**：只说「正五边形不能铺满平面」不足以证明三维的一般限制；$T_d$ 不含中心反演 $i$，也不含单独的 $90^\circ$ 纯旋转 $C_4$；$S_4$ 是旋转与反射的复合操作，不能把两步各算一次。只列纯旋转会得到 12 阶的 $T$ 群，遗漏 $T_d$ 的其余 12 个操作。

<span id="ex-02"></span>

## 例 2　由衍射角求面间距与晶格常数

来源：[S3](../../assets/solid-state/slides/s03.pptx)，第 14 页「作业（需要上交）」第 1 题。

**题目**

使用波长 $\lambda=0.154\ \mathrm{nm}$ 的 Cu Kα X 射线照射晶体：

1. FCC 结构 Al 的 $(111)$ 峰，实验衍射角为 $38.4^\circ$，求 $d_{111}$。
2. BCC 结构 Fe 的 $(110)$ 峰，实验衍射角为 $44.6^\circ$，求其惯用立方单胞晶格常数 $a$。

这里实验所称的衍射角是 $2\theta$。按给定峰指标使用一级 Bragg 形式，级次已经吸收到晶面指标中。

**解析**

相邻晶面散射波的光程差为 $2d\sin\theta$，相长干涉给出

$$
2d_{hkl}\sin\theta=\lambda,
\qquad
d_{hkl}=\frac{\lambda}{2\sin\theta}.
$$

立方晶系还满足

$$
d_{hkl}=\frac{a}{\sqrt{h^2+k^2+l^2}}.
$$

**（1）Al 的 $(111)$ 面间距。** 先将实验角减半：

$$
\theta=\frac{38.4^\circ}{2}=19.2^\circ,
$$

$$
\boxed{d_{111}^{\mathrm{Al}}
=\frac{0.154}{2\sin19.2^\circ}\ \mathrm{nm}
\approx0.2341\ \mathrm{nm}.}
$$

本小问求的是面间距；若继续求 Al 的惯用胞边长，则为 $a=\sqrt3d_{111}\approx0.4055\ \mathrm{nm}$，不能把这两个量混为一谈。

**（2）Fe 的晶格常数。** 同理，

$$
\theta=\frac{44.6^\circ}{2}=22.3^\circ,\qquad
d_{110}^{\mathrm{Fe}}=
\frac{0.154}{2\sin22.3^\circ}\ \mathrm{nm}
\approx0.2029\ \mathrm{nm}.
$$

因为 $d_{110}=a/\sqrt2$，所以

$$
\boxed{a_{\mathrm{Fe}}=\sqrt2d_{110}
\approx0.2870\ \mathrm{nm}
=2.870\times10^{-10}\ \mathrm m.}
$$

**核对与易错点**：FCC 的 $(111)$ 指数全奇，BCC 的 $(110)$ 指数和为偶数，均满足相应中心化选择规则。数值结果分别约为 $2.34\ \text{Å}$ 和 $2.87\ \text{Å}$，数量级合理。最常见错误是把 $2\theta$ 直接代入 Bragg 公式、将计算器设为弧度模式却输入角度值，或将 Fe 的 $d_{110}$ 直接当成 $a$。

<span id="ex-03"></span>

## 例 3　证明 FCC 的倒格子是 BCC

来源：[S3](../../assets/solid-state/slides/s03.pptx)，第 33 页「作业（需要上交）」第 2 题。

**题目**

1. 证明面心立方（FCC）格子的倒格子是体心立方（BCC）格子。
2. 求 FCC 的正格子晶格常数与倒格子晶格常数之间的关系；BCC 情形又如何？

本题的 $a$ 和 $a^*$ 分别指正格子、倒格子的**惯用立方单胞边长**，采用课件约定 $\mathbf a_i\cdot\mathbf b_j=2\pi\delta_{ij}$。

**解析一：FCC → BCC**

选 FCC 原始基矢

$$
\mathbf a_1=\frac a2(0,1,1),\quad
\mathbf a_2=\frac a2(1,0,1),\quad
\mathbf a_3=\frac a2(1,1,0).
$$

它们围成的原胞体积为

$$
\Omega=\mathbf a_1\cdot(\mathbf a_2\times\mathbf a_3)
=\frac{a^3}{4},\qquad
\mathbf a_2\times\mathbf a_3=\frac{a^2}{4}(-1,1,1).
$$

由 $\mathbf b_1=2\pi(\mathbf a_2\times\mathbf a_3)/\Omega$ 及循环置换，得到

$$
\begin{aligned}
\mathbf b_1&=\frac{2\pi}{a}(-1,1,1),\\
\mathbf b_2&=\frac{2\pi}{a}(1,-1,1),\\
\mathbf b_3&=\frac{2\pi}{a}(1,1,-1).
\end{aligned}
$$

这正是边长为 $a^*$ 的 BCC 格子的一组原始基矢

$$
\frac{a^*}{2}(-1,1,1),\quad
\frac{a^*}{2}(1,-1,1),\quad
\frac{a^*}{2}(1,1,-1),
$$

比较系数得

$$
\boxed{\mathrm{FCC}(a)\text{ 的倒格子为 }\mathrm{BCC}(a^*),\qquad
a^*=\frac{4\pi}{a}.}
$$

也可以检查所有倒格点：$\mathbf G=\sum_i m_i\mathbf b_i$ 在 $2\pi/a$ 单位下的三个坐标为

$$
(-m_1+m_2+m_3,\;m_1-m_2+m_3,\;m_1+m_2-m_3).
$$

它们必定全偶或全奇；反过来，任意全偶或全奇三元组都能由整数 $m_i$ 得到。全偶给出边长 $4\pi/a$ 立方胞的顶点格点，全奇给出其体心格点，从而确认得到的是整个 BCC 格子。

**解析二：BCC → FCC**

选 BCC 原始基矢

$$
\mathbf a_1=\frac a2(-1,1,1),\quad
\mathbf a_2=\frac a2(1,-1,1),\quad
\mathbf a_3=\frac a2(1,1,-1).
$$

此时

$$
\Omega=\frac{a^3}{2},\qquad
\mathbf a_2\times\mathbf a_3=\frac{a^2}{2}(0,1,1),
$$

所以

$$
\mathbf b_1=\frac{2\pi}{a}(0,1,1),\quad
\mathbf b_2=\frac{2\pi}{a}(1,0,1),\quad
\mathbf b_3=\frac{2\pi}{a}(1,1,0).
$$

将其与 FCC 原始基矢 $a^*(0,1,1)/2$ 等比较，得到

$$
\boxed{\mathrm{BCC}(a)\text{ 的倒格子为 }\mathrm{FCC}(a^*),\qquad
a^*=\frac{4\pi}{a}.}
$$

**体积核对**

| 正格子 | $\Omega$ | 倒格子 | $\Omega^*$ |
| --- | --- | --- | --- |
| FCC | $a^3/4$ | BCC，$a^*=4\pi/a$ | $(a^*)^3/2=32\pi^3/a^3$ |
| BCC | $a^3/2$ | FCC，$a^*=4\pi/a$ | $(a^*)^3/4=16\pi^3/a^3$ |

两行均有 $\Omega\Omega^*=(2\pi)^3$；再取一次倒格子，惯用胞边长回到 $4\pi/(4\pi/a)=a$。

**易错点**：$a^*$ 是倒长度，若 $a$ 用 $\mathrm{nm}$，则 $a^*$ 用 $\mathrm{nm^{-1}}$；$|\mathbf b_i|$ 是倒格子原始基矢的长度，一般不等于惯用胞边长 $a^*$。$2\pi/a$ 是简单立方正倒惯用胞边长之间的关系，不能直接用于 FCC/BCC。原胞体积也不能一律写成 $a^3$。

<span id="ex-04"></span>

## 例 4　一维交替离子链的马德隆常数

来源：[S5，第 27 页第 1 题](../../assets/solid-state/slides/s05.pptx)（需要上交）。

**题目**：证明一价正、负离子等间距交替排列的一维晶格，其马德隆常数为 $2\ln2$。

**解析**：设相邻离子间距为 $r$，电荷为 $\pm e$，取一个正离子为原点。距离原点 $jr$ 的左右两个离子，电荷都为 $(-1)^je$。原点离子与其余离子的库仑相互作用之和为

$$
u_0=2\frac{e^2}{4\pi\varepsilon_0r}
\sum_{j=1}^{\infty}\frac{(-1)^j}{j}
=-\frac{e^2}{4\pi\varepsilon_0r}
\,2\left(1-\frac12+\frac13-\frac14+\cdots\right).
$$

求和按距离向两侧扩展，保持正负离子交替的物理次序。交错调和级数为 $\ln2$，与定义 $u_0=-Me^2/(4\pi\varepsilon_0r)$ 对照，得到

$$
\boxed{M_{\mathrm{1D}}=2\ln2\approx1.38629}.
$$

若有 $2N$ 个离子，忽略边界效应，总库仑能为 $U_{\mathrm{C}}=\tfrac12(2N)u_0=Nu_0$。所以**每离子对**的库仑能为 $u_0$，**每离子**则为 $u_0/2$。这也解释了为什么计算总能量时要去掉重复计数，却不能把马德隆常数误写为 $\ln2$。

**检查**：$M$ 无量纲；库仑能为负；左右两侧的因子 2 与总能量去重的因子 $1/2$ 来自不同计数步骤。

<span id="ex-05"></span>

## 例 5　压缩 KCl 晶格常数 1% 需要的压力

来源：[S5，第 27 页第 2 题](../../assets/solid-state/slides/s05.pptx)（需要上交）；模型见该课件第 23–25 页。

**题目**：挤压 KCl 晶体，多大压强可使其晶格常数减小 $1\%$？已知平衡时最近邻 K、Cl 离子距离 $r_0=0.314\ \mathrm{nm}$，马德隆常数 $M=1.75$，重叠排斥能指数 $n=9$。使用课件的离子晶体结合能模型，并由 FCC 原胞体积与 $r$ 的关系求导。

**解析（1）：统一能量与体积的计量单位。** 以一对 K、Cl 离子为单位，写

$$
u(r)=-\frac Ar+\frac B{r^n},\qquad
A=\frac{Me^2}{4\pi\varepsilon_0}.
$$

NaCl 型结构的惯用立方胞边长 $a=2r$，每惯用胞含 4 对离子，故每离子对体积为

$$
v=\frac{a^3}{4}=2r^3,\qquad\frac{dv}{dr}=6r^2.
$$

对含 $N$ 对离子的样品，$U=Nu$、$V=Nv$，于是 $p=-dU/dV=-du/dv$，样品大小消去。

**解析（2）：用平衡条件消去 $B$，求有限压缩的压力。** 忽略初始大气压和热效应，$u'(r_0)=0$ 给出

$$
\frac A{r_0^2}-\frac{nB}{r_0^{n+1}}=0,
\qquad B=\frac A n r_0^{n-1}.
$$

因此

$$
p=-\frac{u'(r)}{6r^2}
=\frac A{6r^4}\left[\left(\frac{r_0}{r}\right)^{n-1}-1\right].
$$

晶格常数减小 $1\%$ 等价于 $r=0.99r_0$。取 $e=1.602176634\times10^{-19}\ \mathrm C$、$1/(4\pi\varepsilon_0)\approx8.98755\times10^9\ \mathrm{N\,m^2/C^2}$，则

$$
A\approx4.0374\times10^{-28}\ \mathrm{J\,m},\qquad
r_0=3.14\times10^{-10}\ \mathrm m,
$$

$$
\boxed{p=\frac{A}{6(0.99r_0)^4}\left[(0.99)^{-8}-1\right]
\approx6.03\times10^8\ \mathrm{Pa}=0.603\ \mathrm{GPa}}.
$$

这是给定势能模型内的有限压缩结果。

**解析（3）：核对小应变近似。** 平衡体积模量为

$$
K_0=-v\left.\frac{dp}{dv}\right|_{r_0}
=\frac{(n-1)A}{18r_0^4}\approx18.46\ \mathrm{GPa}.
$$

线性化 $\Delta V/V\approx3\Delta a/a=-0.03$，得到

$$
\boxed{p_{\mathrm{linear}}\approx0.03K_0\approx0.554\ \mathrm{GPa}}.
$$

实际几何体积变化为 $1-0.99^3=2.9701\%$；将它代入线性体积公式会得到约 $0.548\ \mathrm{GPa}$，仍属于线性估算，不能替代上面的有限压缩公式。两个主要答案应分别注明“模型内直接计算”和“小应变线性近似”。

**检查**：压缩时 $p>0$；$A/r^4$ 的单位为 $\mathrm{J/m^3}=\mathrm{Pa}$。不要把最近邻距离 $r_0$ 当成惯用胞边长，也不要把每离子对能量与整个惯用胞体积混用。真实材料的压力还受热效应和势能模型精度影响。

<span id="ex-06"></span>

## 例 6　一维单原子链的德拜热容

来源：[S8](../../assets/solid-state/slides/s08.pptx)，第 43 页，「作业（需要上交）」。最近邻链的模型约定见 S6，第 7–10 页及 S7，第 3 页。

**题目**：一维简单晶格的晶格常数为 $a$，原子质量为 $m$，原子数为 $N$，原子间两体势为

$$
\phi(r)=-\frac Ar+\frac A n\frac{a^{n-1}}{r^n}.
$$

用含 $A,n,m,a$ 的表达式求：（1）长波弹性波的群速度；（2）德拜态密度、德拜频率和德拜温度；（3）平均振动能；（4）等容热容及其高、低温极限。

**模型与条件**：沿用 S6 的最近邻、纵向、简谐单原子链，取 $A>0,n>1$、$L=Na$；每个原子只有一个位移自由度，共 $N$ 个模式。S8 题面没有重写「最近邻」，但 S6 及 S7 第 3 页已明确采用这一条件，并以两体势在平衡点的二阶导数定义力常数。若改为对所有原子对保留长程相互作用，就必须重新建立各邻居的力常数和声速，不能直接沿用下面的结果。热力学积分采用大 $N$ 连续谱近似。

**解析（1）：力常数、色散与声速。**

先检查给定的 $a$ 确为该最近邻键势的平衡点：

$$
\phi'(r)=\frac A{r^2}-\frac{Aa^{n-1}}{r^{n+1}},\qquad
\phi'(a)=0,
$$

$$
\beta=\phi''(a)=\left[-\frac{2A}{r^3}
+\frac{(n+1)Aa^{n-1}}{r^{n+2}}\right]_{r=a}
=\frac{(n-1)A}{a^3}>0.
$$

由 $m\ddot u_\ell=\beta(u_{\ell+1}+u_{\ell-1}-2u_\ell)$，代入格波得到

$$
\omega(q)=2\sqrt{\frac{(n-1)A}{ma^3}}
\left|\sin\frac{qa}{2}\right|.
$$

在 $0<q<\pi/a$ 上，

$$
v_g(q)=\sqrt{\frac{(n-1)A}{ma}}\cos\frac{qa}{2}.
$$

因此长波声速为

$$
\boxed{v_s=\lim_{q\to0^+}v_g(q)
=\sqrt{\frac{(n-1)A}{ma}}}.
$$

负 $q$ 的群速度为负，长波时 $v_g\to-v_s$；声速指其大小。德拜模型把整条支近似为 $\omega=v_s|q|$。

**解析（2）：先数模式，再定截止。**

周期边界条件给出波矢间隔 $2\pi/L$。正、负 $q$ 都要计入，故

$$
g(\omega)d\omega=2\frac L{2\pi}dq
=\frac L{\pi v_s}d\omega.
$$

这里 $g(\omega)$ 是整个链每单位角频率的模式数密度，并非每单位长度的密度。由 $\int_0^{\omega_D}g(\omega)d\omega=N$ 得

$$
\boxed{g(\omega)=\frac N\pi
\sqrt{\frac{ma^3}{(n-1)A}}=\frac N{\omega_D},
\quad 0\le\omega\le\omega_D},
$$

$$
\boxed{q_D=\frac\pi a,\qquad
\omega_D=\pi\sqrt{\frac{(n-1)A}{ma^3}},\qquad
\Theta_D=\frac{\pi\hbar}{k_B}
\sqrt{\frac{(n-1)A}{ma^3}}}.
$$

截止外德拜态密度取零。$\omega_D$ 是线性色散模型的截止；实际最近邻链的最高频率是 $2\sqrt{(n-1)A/(ma^3)}$，二者不应混同。

**解析（3）：平均振动能。**

一个非零频模式的平均能量为 $\hbar\omega[1/2+(e^{\hbar\omega/(k_BT)}-1)^{-1}]$。总振动能以静态平衡晶格能为零点，包括零点振动能：

$$
U=\int_0^{\omega_D}g(\omega)\hbar\omega
\left(\frac12+\frac1{e^{\hbar\omega/(k_BT)}-1}\right)d\omega.
$$

记 $y=\Theta_D/T=\dfrac{\pi\hbar}{k_BT}\sqrt{\dfrac{(n-1)A}{ma^3}}$，换元 $x=\hbar\omega/(k_BT)$，得

$$
\boxed{U=\frac{N\pi\hbar}{4}\sqrt{\frac{(n-1)A}{ma^3}}
+\frac{Nk_B^2T^2}{\pi\hbar}\sqrt{\frac{ma^3}{(n-1)A}}
\int_0^y\frac{x}{e^x-1}dx}.
$$

第一项 $U_{\mathrm{zp}}=N\hbar\omega_D/4$ 与温度无关。若约定能量不含零点能，只删去第一项；每原子的平均振动能为 $U/N$。

**解析（4）：热容与极限。**

固定 $a$ 并对模式平均能量求温度导数，再积分，得到

$$
\boxed{C_V=\frac{Nk_B^2T}{\pi\hbar}
\sqrt{\frac{ma^3}{(n-1)A}}
\int_0^y\frac{x^2e^x}{(e^x-1)^2}dx
=Nk_B\frac T{\Theta_D}
\int_0^{\Theta_D/T}\frac{x^2e^x}{(e^x-1)^2}dx}.
$$

高温 $T\gg\Theta_D$ 时，积分的被积函数趋于 1，

$$
\boxed{U\sim Nk_BT,\qquad C_V\to Nk_B}.
$$

更细致地，$C_V=Nk_B[1-(\Theta_D/T)^2/36+O((\Theta_D/T)^4)]$。高温总振动能的展开中，玻色占据的常数项与零点能相抵消，不能在 $Nk_BT$ 后另加一份零点能当作同阶近似。

低温 $T\ll\Theta_D$ 时将上限延至无穷大，利用

$$
\int_0^\infty\frac{x}{e^x-1}dx=\frac{\pi^2}6,\qquad
\int_0^\infty\frac{x^2e^x}{(e^x-1)^2}dx=\frac{\pi^2}3,
$$

得到完全写成题目参数的结果

$$
\boxed{U\simeq\frac{N\pi\hbar}{4}\sqrt{\frac{(n-1)A}{ma^3}}
+\frac{N\pi k_B^2T^2}{6\hbar}\sqrt{\frac{ma^3}{(n-1)A}}},
$$

$$
\boxed{C_V\simeq\frac{N\pi k_B^2T}{3\hbar}
\sqrt{\frac{ma^3}{(n-1)A}}
=\frac{\pi^2}3Nk_B\frac T{\Theta_D}}.
$$

该 $T$ 律还要求热激发跨越许多离散模式，即 $\hbar v_s(2\pi/L)\ll k_BT\ll k_B\Theta_D$。有限链在更低温度下须恢复离散求和；通常固定质心，去掉整体平移的零频模，其 $O(1)$ 模式数差异不改变上述热力学极限。

**易错点**：套用三维的 $3N$ 模式数或 $T^3$ 律；只计正波矢导致少一倍；把实际色散的最高频率当作德拜截止；把零点能求导为非零；写出 $v_s,\Theta_D$ 后未代回参数而遗漏题目要求。

<span id="ex-07"></span>

## 例 7　二维周期势：找耦合、找简并、再求分裂

来源：[S10](../../assets/solid-state/slides/s10.pptx)，第 29 页；[S11](../../assets/solid-state/slides/s11.pptx)，第 19 页。两页为同一道作业，合并解析。

**题目**：晶格常数为 $a$ 的二维正方晶格具有周期势

$$
V(x,y)=-2U_0\left[\cos\frac{2\pi x}{a}+\cos\frac{2\pi y}{a}\right]
-2U_1\cos\frac{4\pi x}{a},
$$

$U_0,U_1$ 已知。（1）找出中心方程中所有非零非对角元的位置与数值；（2）用近自由电子近似解释为何开隙，给出开隙的波矢坐标、相互耦合的 Bloch 分支标签和分裂大小。

**符号与近似**：令 $g=2\pi/a$、$E_R=\hbar^2g^2/(2m_e)$。以整数对 $\mathbf m=(m_x,m_y)$ 标记 $\mathbf G_{\mathbf m}=g(m_x,m_y)$，零级 Bloch 基底为 $e^{i(\mathbf k+\mathbf G_{\mathbf m})\cdot\mathbf r}$。这些是课件中心方程的分支序号；二维中不能脱离 $\mathbf k$，将它们固定改称最终由低到高排列的第几条能带。以下分裂是弱势的一阶结果，多重简并另行处理。

**解析（1）：全部傅里叶分量与矩阵元。**

利用 $2\cos\alpha=e^{i\alpha}+e^{-i\alpha}$，

$$
V_{\mathbf0}=0,\qquad
V_{(\pm g,0)}=V_{(0,\pm g)}=-U_0,\qquad
V_{(\pm2g,0)}=-U_1,
$$

其余傅里叶分量全部为零。中心方程为

$$
\sum_{\mathbf l}\left[\varepsilon^{(0)}_{\mathbf m}(\mathbf k)
\delta_{\mathbf m\mathbf l}+V_{\mathbf G_{\mathbf m}-\mathbf G_{\mathbf l}}\right]
C_{\mathbf l}=\varepsilon C_{\mathbf m},
$$

$$
\varepsilon^{(0)}_{\mathbf m}(\mathbf k)=E_R
\left[\left(\frac{k_x}g+m_x\right)^2+
\left(\frac{k_y}g+m_y\right)^2\right].
$$

所以对任意整数对 $\mathbf m,\mathbf l$，所有非零非对角元可完整写成

$$
\boxed{H_{\mathbf m\mathbf l}=
\begin{cases}
-U_0,&\mathbf m-\mathbf l=(\pm1,0),(0,\pm1),\\
-U_1,&\mathbf m-\mathbf l=(\pm2,0),\\
0,&\text{其余 }\mathbf m\ne\mathbf l.
\end{cases}}
$$

这表示每一行与横、纵相邻索引及横向隔一个的索引耦合，并非全矩阵只有 6 个非零元。若某给定振幅为零，对应矩阵元也应删去。

**解析（2）：两态分裂的起源与位置。**

对两条隔离于其他同能分支的零级态，令 $W=H_{\mathbf m\mathbf l}$，有

$$
H_2=\begin{pmatrix}\varepsilon_{\mathbf m}^{(0)}&W\\
W^*&\varepsilon_{\mathbf l}^{(0)}\end{pmatrix},
\qquad
\varepsilon_\pm=\frac{\varepsilon_{\mathbf m}^{(0)}+\varepsilon_{\mathbf l}^{(0)}}2
\pm\sqrt{\left(\frac{\varepsilon_{\mathbf m}^{(0)}-\varepsilon_{\mathbf l}^{(0)}}2\right)^2+|W|^2}.
$$

在 $|\mathbf k+\mathbf G_{\mathbf m}|^2=|\mathbf k+\mathbf G_{\mathbf l}|^2$ 处，两态混合成不同空间分布的组合，势能期望不同，原有交叉被分裂为 $\Delta=2|W|$。这也可理解为 Bragg 散射把等能平面波相干耦合。对二维边界，法向可形成驻波而切向仍可传播，不必所有方向的群速度都为零。

例如取 $\mathbf l=\mathbf m+(s,0)$，交叉条件为

$$
\frac{k_x}g=-m_x-\frac s2,
$$

纵向索引差同理。筛选第一布里渊区 $-g/2\le k_x,k_y\le g/2$ 内的解，得到所有由上述非零元直接产生的一阶交叉线：

| 波矢位置 | 相互耦合的分支标签（$r\in\mathbb Z$） | 非对角元 | 孤立两态的局部分裂 |
| --- | --- | --- | --- |
| $k_x=g/2=\pi/a$，$k_y$ 任意 | $(0,r)$ 与 $(-1,r)$ | $-U_0$ | $2\lvert U_0\rvert$ |
| $k_x=-g/2=-\pi/a$，$k_y$ 任意 | $(0,r)$ 与 $(1,r)$ | $-U_0$ | $2\lvert U_0\rvert$ |
| $k_y=g/2=\pi/a$，$k_x$ 任意 | $(r,0)$ 与 $(r,-1)$ | $-U_0$ | $2\lvert U_0\rvert$ |
| $k_y=-g/2=-\pi/a$，$k_x$ 任意 | $(r,0)$ 与 $(r,1)$ | $-U_0$ | $2\lvert U_0\rvert$ |
| $k_x=0$，$k_y$ 任意 | $(1,r)$ 与 $(-1,r)$ | $-U_1$ | $2\lvert U_1\rvert$ |

相对边界代表等价 Bloch 波矢，不重复计态。$k_x=0$ 一项涉及横向激发分支 $m_x=\pm1$；不能据此声称最低自由电子分支在 $\Gamma$ 必开隙。矩阵元为零的其他交叉在一阶不直接分裂，但多步虚跃迁可产生高阶修正。

**多重简并检查：表格中的两态公式有适用条件。**

在角点 $\mathbf k=(g/2,g/2)$，最低的四个零级分支

$$
(0,0),\ (-1,0),\ (0,-1),\ (-1,-1)
$$

均有能量 $E_R/2$。在这一顺序的基底内，必须共同对角化

$$
H_{\mathrm{corner}}=\frac{E_R}2I_4+
\begin{pmatrix}
0&-U_0&-U_0&0\\
-U_0&0&0&-U_0\\
-U_0&0&0&-U_0\\
0&-U_0&-U_0&0
\end{pmatrix}.
$$

一阶本征能量为

$$
\boxed{\frac{E_R}2+\{-2\lvert U_0\rvert,0,0,2\lvert U_0\rvert\}}.
$$

角点中间两态仍一阶简并；不能说每一对相邻能带都相隔 $2\lvert U_0\rvert$。$U_1$ 在该四态块中没有直接矩阵元，但可经外部态产生高阶修正，一阶简并并不保证在更高阶仍存在。

在 $\Gamma=(0,0)$，能量为 $E_R$ 的激发态也有四个：$(1,0),(-1,0),(0,1),(0,-1)$。一阶只有前两个由 $-U_1$ 直接耦合，因而该簇为

$$
\boxed{E_R+\{-\lvert U_1\rvert,0,0,\lvert U_1\rvert\}}.
$$

因此所谓 $2\lvert U_1\rvert$ 是横向两分支的分裂；该能量范围内另有两个态，不能将它当作隔开所有能带的空白能区。纵向两态的简并也只是在本次一阶计算中保留。

另一个典型四重交叉位于 $(k_x,k_y)=(0,g/2)$，分支为 $(1,0),(-1,0),(1,-1),(-1,-1)$，共同零级能量为 $5E_R/4$，一阶结果为

$$
\boxed{\frac{5E_R}4+\{\,\pm\lvert U_1\rvert\pm\lvert U_0\rvert\,\}}.
$$

两个正负号独立选取；当 $\lvert U_1\rvert=\lvert U_0\rvert$ 时中间两态仍一阶简并。更高分支若出现其他同能态，同样应扩大简并子空间。以上微扰结果均要求与外部零级态的能量间隔远大于所取势振幅。

**结果检查与易错点**：该势可分离为 $V_x(x)+V_y(y)$，二维能量可由一维两个谱相加，四态分裂正是两个两态分裂的组合。局部分裂不等于全局绝缘带隙；后者需比较整个 BZ 的带边及电子填充。不要漏掉 $\pm2g$ 傅里叶项、把 $2\cos$ 多除一次、把平面波索引当成固定的能量排序带号，或在四重简并处只对角化一个 $2\times2$ 块。

<span id="ex-08"></span>

## 例 8　简单立方三个 p 轨道的能量顺序

来源：[S13](../../assets/solid-state/slides/s13.pptx)，第 20 页，「作业：简单立方格子的 p 轨道能带」；跃迁符号见第 19 页。

**题目**：晶格常数为 $a$ 的简单立方晶格，每格点有 $p_x,p_y,p_z$ 三个轨道。在位修正 $t_0=0$，沿轨道轴向的最近邻跃迁为 $t_1$，垂直方向为 $t_2$。推导三条能带，讨论 $\Gamma=(0,0,0)$、$X=(\pi/a,0,0)$、$M=(\pi/a,\pi/a,0)$ 的能量顺序与简并性。

**模型约定**：三个孤立原子 $p$ 轨道能级同为 $\varepsilon_p$，采用正交近似、轴向最近邻跃迁，忽略不同 $p$ 轨道间跃迁和自旋轨道耦合。课件取带符号的 $t_1>0,t_2<0$，与正文的 $t_\sigma=t_1,t_\pi=t_2$ 一致。$t_0=0$ 只删去在位能修正，并不自动令 $\varepsilon_p=0$；若将原子能级设为能量零点，再整体减去 $\varepsilon_p$ 即可。

**解析（1）：按方向相加最近邻跃迁。**

对 $p_x$ 轨道，$\pm a\hat x$ 两个最近邻贡献 $t_1(e^{ik_xa}+e^{-ik_xa})$；$\pm a\hat y$、$\pm a\hat z$ 四个最近邻各取 $t_2$。于是

$$
\boxed{\begin{aligned}
\varepsilon_{p_x}(\mathbf k)&=\varepsilon_p+2t_1\cos(k_xa)
+2t_2[\cos(k_ya)+\cos(k_za)],\\
\varepsilon_{p_y}(\mathbf k)&=\varepsilon_p+2t_1\cos(k_ya)
+2t_2[\cos(k_xa)+\cos(k_za)],\\
\varepsilon_{p_z}(\mathbf k)&=\varepsilon_p+2t_1\cos(k_za)
+2t_2[\cos(k_xa)+\cos(k_ya)].
\end{aligned}}
$$

此模型的 $3\times3$ Bloch 哈密顿量以这三条色散为对角元，非对角元为零，因此它们已是本征能量。每一方向的正、负最近邻共同给出因子 2。

**解析（2）：代入高对称点并判断简并。**

使用 $\cos0=1$、$\cos\pi=-1$：

| 点 | $\varepsilon_{p_x}-\varepsilon_p$ | $\varepsilon_{p_y}-\varepsilon_p$ | $\varepsilon_{p_z}-\varepsilon_p$ |
| --- | --- | --- | --- |
| $\Gamma=(0,0,0)$ | $2t_1+4t_2$ | $2t_1+4t_2$ | $2t_1+4t_2$ |
| $X=(\pi/a,0,0)$ | $-2t_1+4t_2$ | $2t_1$ | $2t_1$ |
| $M=(\pi/a,\pi/a,0)$ | $-2t_1$ | $-2t_1$ | $2t_1-4t_2$ |

所以 $\Gamma$ 点始终轨道三重简并；$X$ 点的 $p_y,p_z$ 等能；$M$ 点的 $p_x,p_y$ 等能。排序由

$$
\varepsilon_{p_y}(X)-\varepsilon_{p_x}(X)
=\varepsilon_{p_z}(M)-\varepsilon_{p_x}(M)
=4(t_1-t_2)
$$

直接决定：

| 参数条件 | $X$ 点顺序 | $M$ 点顺序 |
| --- | --- | --- |
| $t_1>t_2$，包括课件的 $t_1>0,t_2<0$ | $p_x<p_y=p_z$ | $p_x=p_y<p_z$ |
| $t_1<t_2$ | $p_y=p_z<p_x$ | $p_z<p_x=p_y$ |
| $t_1=t_2$ | 三重简并 | 三重简并 |

在 $t_1=t_2$ 的各向同性特例中，三条色散在整个 BZ 都相同。这里的二重、三重均指轨道简并；忽略 SOC 且保持自旋简并时，每个轨道态另乘自旋因子 2。

**易错点**：把 $p_x$ 的 $t_1$ 误用于 $y,z$ 方向；在 $X$、$M$ 漏掉一个 $\cos\pi$ 的负号；把 $t_0=0$ 写成所有在位能为零；未说明 $t_1,t_2$ 的符号就固定排序；把轨道简并与自旋简并混为一谈。

<span id="preparation-tasks"></span>

## 不需上交的预习任务与课堂练习

**（1）点群、空间群、七大晶系和 14 类布拉维格子。** 来源：[S1，第 45 页](../../assets/solid-state/slides/s01.pptx)，课件明确标注“不需要上交”。

预习时应能说明：点群是保持晶体不变且有公共不动点的一组对称操作，周期晶体共有 32 种晶体学点群；空间群描述完整周期结构的对称性，以 $\{R\mid\mathbf t\}$ 表示旋转／反射部分与平移部分，也包括螺旋轴和滑移面等复合操作。在通常三维周期结构的分类下有 230 种空间群。

七大晶系为三斜、单斜、正交、四方、三方、六方和立方。统计 14 类布拉维格子时则按下表的**晶格系统**分类。P 为简单格子，C 为底心（其他底心设置可通过换轴表示），I 为体心，F 为面心，R 为菱方格子。

| 晶格系统 | 布拉维格子 | 数目 |
| --- | --- | ---: |
| 三斜 | P | 1 |
| 单斜 | P、C | 2 |
| 正交 | P、C、I、F | 4 |
| 四方 | P、I | 2 |
| 菱方 | R | 1 |
| 六方 | P | 1 |
| 立方 | P、I、F | 3 |
| 合计 |  | 14 |

晶系按点群对称性分类，晶格系统按布拉维格子的对称性分类，二者并非逐一对应：三方晶系可以具有六方 P（hP）或菱方 R（hR）格子，六方晶系具有六方 P 格子。具体原子基元还须另行说明。分类定义可对照 [IUCr：晶系](https://dictionary.iucr.org/Crystal_system)与[晶格系统](https://dictionary.iucr.org/Lattice_system)。

**（2）倒格子与布里渊区。** 来源：[S2，第 58 页](../../assets/solid-state/slides/s02.pptx)，课件明确标注“不需要上交”。

倒格矢满足 $e^{i\mathbf G\cdot\mathbf R}=1$，一组倒基矢由 $\mathbf a_i\cdot\mathbf b_j=2\pi\delta_{ij}$ 定义。第一布里渊区是倒格子原点的 Wigner–Seitz 原胞：从原点连向各倒格点，作垂直平分面，取离原点最近的一域。其条件可写为

$$
\mathbf k\cdot\mathbf G\le\frac{|\mathbf G|^2}{2}
\quad\text{对所有非零倒格矢 }\mathbf G.
$$

区边界上的等号就是相应的 Bragg 平面。练习时可先画二维正方格子的第一布里渊区，再用例 3 检查 FCC／BCC 的倒格子。

**（3）简单立方结构因子。** 来源：[S4，第 24 页](../../assets/solid-state/slides/s04.pptx)“Have a try!”，原课件该页已附解答。

题目为：简单立方惯用胞只有一个原子，分数坐标 $(0,0,0)$，求结构因子及衍射峰强度。代入

$$
S_{hkl}=\sum_j f_j\exp[-2\pi i(hx_j+ky_j+lz_j)]
$$

得到 $S_{hkl}=f$，所以 $I_{hkl}\propto|f|^2$。单原子简单立方结构没有由中心化或基元干涉引起的系统消光；这不表示所有峰的实测强度相同，原子散射因子随散射矢量变化，实验强度也受几何因子等影响。

<span id="extra-practice"></span>

## 补充练习

以下两题用于联系电子统计和半经典运动，参数由原笔记设置，未在课件中标为需提交的作业。

<span id="ex-09"></span>

## 例 9　由电子密度估算费米温度与热容

对应 S12 的应用练习，给定三维自由电子密度 $n_e=8.0\times10^{28}\,\mathrm{m^{-3}}$。

$$
k_F=(3\pi^2n_e)^{1/3}\approx1.333\times10^{10}\,\mathrm{m^{-1}},
$$

$$
E_F\approx6.77\,\mathrm{eV},\qquad T_F\approx7.86\times10^4\,\mathrm K.
$$

在 $T=300\,\mathrm K$，$T/T_F\approx3.82\times10^{-3}\ll1$，电子仍高度简并。单位体积电子热容为

$$
c_{V,e}=\frac{\pi^2}2 n_ek_B\frac T{T_F}
\approx2.08\times10^4\,\mathrm{J\,m^{-3}K^{-1}}.
$$

这是自由电子模型的电子贡献，不是样品包含声子的总热容；不能把 $T_F$ 当成材料需被加热到的实际工作温度。

<span id="ex-10"></span>

## 例 10　紧束缚链的带宽、质量与振荡位移

对应 S12、S13 的综合练习。取 $\varepsilon(k)=\varepsilon_c-2J\cos(ka)$，$J=1\,\mathrm{eV}>0$，$a=0.30\,\mathrm{nm}$。

在带底 $ka\ll1$，$\cos ka\approx1-(ka)^2/2$，因此

$$
\varepsilon\approx\varepsilon_c-2J+Ja^2k^2,
\quad W=4J=4\,\mathrm{eV},
\quad m^*=\frac{\hbar^2}{2Ja^2}\approx0.423m_e.
$$

同一色散在恒电场下的空间振荡峰—峰位移为

$$
\Delta x_{\mathrm{pp}}=\frac{4J}{e|E|}=\frac W{e|E|}.
$$

检查单位：带宽用焦耳、电场用 $\mathrm{V/m}$ 时，右侧为米。增大带宽会增大振荡位移，但周期 $T_B=2\pi\hbar/(e|E|a)$ 与带宽无关；实际是否可见还受散射和带间跃迁限制。

<!-- /course:body -->
