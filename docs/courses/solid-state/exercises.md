---
title: 固体物理 · 习题与解析
description: 按章节定位课件作业与解题示例，先做题，再对照解析。
status: 已整理
tags:
  - 习题与自测
---

# 习题与解析

[返回课程概览](index.md) · [复习速查](review.md)

建议先遮住解析独立计算，再检查假设、符号、单位与极限。

| 对应章节 | 例题 |
| --- | --- |
| [晶体结构](structure.md) | [例 1–3](#ex-01) |
| [晶体结合](bonding.md) | [例 4–5](#ex-04) |
| [晶格振动](phonons.md) | [例 6](#ex-06) |
| [周期势与带隙](bloch.md) | [例 7](#ex-07) |
| [紧束缚](tight-binding.md) | [例 8](#ex-08) |
| [电子统计与运动](electron-statistics.md) | [例 9–10](#ex-09) |

<!-- course:body -->

<span id="ex-01"></span>

### 例 1　晶体学限制与正四面体点群

来源：S2，第 34 页。

晶体学限制的证明见 1.5 节。关键是晶格旋转在原始基矢下可表示为整数矩阵，因此其迹是整数；直接说「五边形不能铺满平面」不足以证明三维的一般结论。

正四面体点群 $T_d$ 有 24 个操作，可按类别列为

$$
T_d:\quad E+8C_3+3C_2+6S_4+6\sigma_d.
$$

四条三重轴分别穿过顶点和对面中心，每轴有两种非恒等旋转，得到 $8C_3$；三条穿过对棱中点的二重轴给出 $3C_2$；此外有 6 个旋转反射操作与 6 个对角镜面反射。总数 $1+8+3+6+6=24$。国际点群符号为 $\bar43m$。

<span id="ex-02"></span>

### 例 2　由衍射角求面间距与晶格常数

来源：S3，第 14 页。给定 Cu Kα 波长 $\lambda=0.154\ \mathrm{nm}$。

**Al 的 $(111)$ 峰**：测得 $2\theta=38.4^\circ$，因此 $\theta=19.2^\circ$，按一级反射

$$
d_{111}=\frac{0.154}{2\sin19.2^\circ}\ \mathrm{nm}
\approx0.2341\ \mathrm{nm}.
$$

**Fe 的 $(110)$ 峰**：测得 $2\theta=44.6^\circ$，取 $\theta=22.3^\circ$：

$$
d_{110}=\frac{0.154}{2\sin22.3^\circ}\approx0.2029\ \mathrm{nm},
\quad a=\sqrt2d_{110}\approx0.2870\ \mathrm{nm}.
$$

检查反射是否允许：FCC 的 $(111)$ 为全奇，BCC 的 $(110)$ 指数和为 2，均满足相应选择规则。最常见错误是把实验的 $2\theta$ 直接代入 Bragg 公式。

<span id="ex-03"></span>

### 例 3　证明 FCC 的倒格子是 BCC

来源：S3，第 33 页。

取 1.3 节的 FCC 原始基矢，计算 $\Omega=a^3/4$。例如

$$
\mathbf a_2\times\mathbf a_3=\frac{a^2}{4}(-1,1,1),
\quad\mathbf b_1=\frac{2\pi}{a}(-1,1,1).
$$

另外两根倒基矢是其循环置换。与 BCC 原始基矢 $a^*(-1,1,1)/2$ 比较，得到倒格子惯用边长 $a^*=4\pi/a$，故为 BCC。用 $\Omega^*=(a^*)^3/2=32\pi^3/a^3$ 可再次检查 $\Omega\Omega^*=(2\pi)^3$。

BCC 的倒格子同理为 FCC，惯用边长也为 $4\pi/a$。此处的 $a^*$ 有倒长度单位，不能当作实空间晶格常数。

<span id="ex-04"></span>

### 例 4　一维交替离子链的马德隆常数

来源：S5，第 27 页第 1 题。

令最近邻间距为 $r$，以一个正离子为原点，左右两侧电荷符号交替。它与其他离子的相互作用之和为

$$
U_{\mathrm{one}}=-\frac{q_e^2}{4\pi\varepsilon_0r}
\,2\left(1-\frac12+\frac13-\frac14+\cdots\right).
$$

由 $\ln(1+x)=x-x^2/2+x^3/3-\cdots$ 在 $x=1$ 的交错级数极限，得到

$$
\boxed{M_{\mathrm{1D}}=2\ln2\approx1.38629}.
$$

计算全晶体总能量时，每个离子对别的离子的相互作用会重复计数，需要乘 $1/2$；再按每离子对计量，得到 2.4 节的形式。

<span id="ex-05"></span>

### 例 5　压缩 KCl 晶格常数 1% 需要的压力

来源：S5，第 27 页第 2 题。按题目使用 $r_0=0.314\ \mathrm{nm}$、$M=1.75$、$n=9$ 和一价电荷。

先计算 $A=Me^2/(4\pi\varepsilon_0)$，注意 $r_0=3.14\times10^{-10}\ \mathrm m$。由 2.5 节

$$
K_0=\frac{8A}{18r_0^4}\approx18.46\ \mathrm{GPa}.
$$

线性弹性近似给出 $p\approx0.03K_0\approx0.554\ \mathrm{GPa}$。直接将 $r=0.99r_0$ 代入同一模型的压力表达式得到

$$
p=\frac{A}{6(0.99r_0)^4}
\left[(0.99)^{-8}-1\right]\approx0.603\ \mathrm{GPa}.
$$

两者差别来自截断线性近似；后一数值是给定两体势模型内的直接结果，也不应视为真实 KCl 的精确实验压缩曲线。题目给的是晶格常数减小 1%，相应体积减小 $1-0.99^3\approx2.9701\%$。

<span id="ex-06"></span>

### 例 6　一维单原子链的德拜热容

来源：S8，第 43 页。这里讨论课件中的**一维纵向链**，每个原子只有一个位移自由度，因此共有 $N$ 个模式。

给定

$$
\phi(r)=-\frac Ar+\frac A n\frac{a^{n-1}}{r^n},
\qquad \phi'(a)=0.
$$

求二阶导数得到

$$
\beta=\phi''(a)=\frac{(n-1)A}{a^3},\qquad
v=a\sqrt{\frac\beta m}=\sqrt{\frac{(n-1)A}{ma}}.
$$

链长 $L=Na$，波矢密度为 $L/(2\pi)$。正负 $q$ 共同计入，长波 $\omega=v|q|$ 对应

$$
g_{\mathrm{1D}}(\omega)=\frac{L}{\pi v}=\frac N{\omega_D},
\quad\omega_D=\frac{\pi v}{a},\quad
\Theta_D=\frac{\hbar\pi v}{ak_B}.
$$

截止由 $\int_0^{\omega_D}g(\omega)d\omega=N$ 确定。这里采用德拜线性色散，$\omega_D$ 与真实链的 $\omega_{\max}=2\sqrt{\beta/m}$ 不相同。

含零点能的平均总振动能为

$$
U=\frac{N\hbar\omega_D}{4}
+\frac{Nk_BT^2}{\Theta_D}
\int_0^{\Theta_D/T}\frac{x}{e^x-1}\,dx.
$$

热容为

$$
\boxed{C_V^{\mathrm{1D}}=Nk_B\frac T{\Theta_D}
\int_0^{\Theta_D/T}\frac{x^2e^x}{(e^x-1)^2}\,dx}.
$$

高温时 $C_V\to Nk_B$；低温且可将离散模视为连续谱时

$$
C_V\approx\frac{\pi^2}{3}Nk_B\frac T{\Theta_D}.
$$

把 $v=\sqrt{(n-1)A/(ma)}$ 代入即可得到题目要求的 $A,n,m,a$ 表达式。低温正比于 $T$，不是三维的 $T^3$。有限长度极低温下还要考虑非零模式的离散间隔。

<span id="ex-07"></span>

### 例 7　二维周期势：找耦合、找简并、再求分裂

来源：S10，第 29 页；S11，第 19 页。令 $g=2\pi/a$，给定

$$
V(x,y)=-2U_0[\cos(gx)+\cos(gy)]-2U_1\cos(2gx).
$$

**第一步：列傅里叶分量。** 平均势为零，非零分量只有

$$
V_{(\pm g,0)}=V_{(0,\pm g)}=-U_0,
\qquad V_{(\pm2g,0)}=-U_1.
$$

以整数对 $\mathbf m=(m_x,m_y)$ 标记 $\mathbf G_{\mathbf m}=g(m_x,m_y)$。中心方程每一行只与 $\mathbf m\pm(1,0)$、$\mathbf m\pm(0,1)$、$\mathbf m\pm(2,0)$ 耦合，其余非对角元在本模型中为零。

**第二步：找同能自由电子分支。** 在第一 BZ $-g/2\le k_x,k_y<g/2$ 内，

$$
\varepsilon^{(0)}_{\mathbf m}=E_R\left[
\left(\frac{k_x}{g}+m_x\right)^2+
\left(\frac{k_y}{g}+m_y\right)^2\right],
\quad E_R=\frac{\hbar^2g^2}{2m_e}.
$$

| 耦合分支代表 | 交叉位置 | 两态近似下的一阶局部分裂 |
| --- | --- | --- |
| $(0,m_y)$ 与 $(-1,m_y)$ | $k_x=g/2$，右边界与左边界等价 | $2\lvert U_0\rvert$ |
| $(0,m_y)$ 与 $(1,m_y)$ | $k_x=-g/2$ | $2\lvert U_0\rvert$ |
| $(m_x,0)$ 与 $(m_x,-1)$ 或 $(m_x,1)$ | $k_y=g/2$ 或 $-g/2$ | $2\lvert U_0\rvert$ |
| $(1,m_y)$ 与 $(-1,m_y)$ | $k_x=0$，两条激发分支交叉 | $2\lvert U_1\rvert$ |

表中 $(m_x,m_y)$ 是平面波标签；最终按能量排列的带号会随 $\mathbf k$ 改变。若某振幅恰为零，其对应的一阶分裂也为零；高阶虚跃迁可能产生更小的分裂。

**第三步：检查是否多重简并。** 在角点 $(g/2,g/2)$，$(0,0),(-1,0),(0,-1),(-1,-1)$ 四个分支零级能量均为 $E_R/2$。一阶简并块为

$$
H_{\mathrm{corner}}=\frac{E_R}2I_4+
\begin{pmatrix}
0&-U_0&-U_0&0\\
-U_0&0&0&-U_0\\
-U_0&0&0&-U_0\\
0&-U_0&-U_0&0
\end{pmatrix}.
$$

其本征值为

$$
\frac{E_R}2+\{-2|U_0|,\ 0,\ 0,\ 2|U_0|\}.
$$

中间仍有二重简并，所以不能把两条边上的 $2|U_0|$ 简单解释为角点所有带之间的间隔。在 $k_x=0,k_y=g/2$ 的相应高能四重交叉中，一阶分裂组合为 $\pm|U_1|\pm|U_0|$。条件是势足够弱、这组简并态与外部态能量分离良好；靠近别的多重交叉要扩大矩阵。

**完整性检查**：此势可分离为 $V_x(x)+V_y(y)$，因而整个二维能谱可由一维 $x$、$y$ 本征能量相加得到。角点一阶结果正是两个二能级分裂之和；但全局是否有绝缘带隙仍要结合电子填充，并比较整个 BZ 的带边。

<span id="ex-08"></span>

### 例 8　简单立方三个 p 轨道的能量顺序

来源：S13，第 20 页。取题目的在位修正 $t_0=0$，令 $t_\sigma=t_1$、$t_\pi=t_2$，原子能级为 $\varepsilon_p$。

先按每个轨道的轴向与横向跃迁写出 4.20 节三条色散，再代入 $\cos0=1$、$\cos\pi=-1$，得到

| 点 | $\varepsilon_{p_x}-\varepsilon_p$ | $\varepsilon_{p_y}-\varepsilon_p$ | $\varepsilon_{p_z}-\varepsilon_p$ | 课件 $t_\sigma>0,t_\pi<0$ 下的顺序 |
| --- | --- | --- | --- | --- |
| $\Gamma=(0,0,0)$ | $2t_\sigma+4t_\pi$ | $2t_\sigma+4t_\pi$ | $2t_\sigma+4t_\pi$ | 三重简并 |
| $X=(\pi/a,0,0)$ | $-2t_\sigma+4t_\pi$ | $2t_\sigma$ | $2t_\sigma$ | $p_x$ 低，$p_y,p_z$ 二重简并 |
| $M=(\pi/a,\pi/a,0)$ | $-2t_\sigma$ | $-2t_\sigma$ | $2t_\sigma-4t_\pi$ | $p_x,p_y$ 二重简并且较低，$p_z$ 高 |

例如 $X$ 点能量差 $\varepsilon_{p_y}-\varepsilon_{p_x}=4(t_\sigma-t_\pi)>0$；$M$ 点同样有 $\varepsilon_{p_z}-\varepsilon_{p_x}=4(t_\sigma-t_\pi)>0$。所以排序真正依赖 $t_\sigma-t_\pi$，若改变参数关系需重新判断。这里的“三重／二重”是轨道简并，自旋简并另计；包含 SOC 或降低晶体对称性后结果可能改变。

<span id="ex-09"></span>

### 例 9　由电子密度估算费米温度与热容

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

### 例 10　紧束缚链的带宽、质量与振荡位移

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
