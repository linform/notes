---
title: 第三章　晶格振动
description: 固体物理分章笔记，包含学习目标、推导、课件定位、小结与自测。
status: 已整理
updated: "2026-10-19"
---

# 第三章　晶格振动

[课程概览](index.md) · [符号约定](index.md#symbols) · [来源与订正](references.md)

## 学习目标

- 从一维链方程推导色散并检查长波与区边界极限。
- 正确数模式，解释声子和爱因斯坦、德拜热容模型。

## 前置知识

牛顿方程、简谐振子、复指数与玻色分布；倒格子见第一章。

## 核心内容

<!-- course:body -->

### 3.1 简谐近似与一维单原子链

来源：S6，第 3–23、39 页。

本节每个原子质量为 $m$，相邻平衡间距及原胞长度都为 $a$，仅保留最近邻相互作用。第 $\ell$ 个原子坐标为 $x_\ell=\ell a+u_\ell$。

把相邻原子的势能在平衡处展开，忽略常数并保留二阶：

$$
\phi(a+u_{\ell+1}-u_\ell)
\approx\phi(a)+\frac12\beta(u_{\ell+1}-u_\ell)^2,
\quad\beta=\phi''(a).
$$

这里 $\phi'(a)=0$ 是无预应力的最近邻链模型的假设；一般晶体只要求总力在平衡处为零。

运动方程为

$$
m\ddot u_\ell=\beta(u_{\ell+1}+u_{\ell-1}-2u_\ell).
$$

代入 $u_\ell=Ae^{i(q\ell a-\omega t)}$，消去共同相位，得到

$$
-m\omega^2=\beta(e^{iqa}+e^{-iqa}-2)
=-4\beta\sin^2\frac{qa}{2},
$$

$$
\boxed{\omega(q)=2\sqrt{\frac\beta m}\left|\sin\frac{qa}{2}\right|}.
$$

实际位移取复数解的实部。非负频率必须保留绝对值，或先明确只讨论 $q\ge0$。

### 3.2 波矢、模式数量与传播速度

来源：S6，第 12–23 页。

Born–von Kármán 边界条件 $u_{\ell+N_c}=u_\ell$ 给出

$$
e^{iqN_ca}=1,\qquad q=\frac{2\pi j}{N_ca}.
$$

取第一布里渊区 $-\pi/a\le q<\pi/a$，其中恰有 $N_c$ 个不同波矢。两端点等价，不能重复计数。

由于 $e^{i(q+2\pi/a)\ell a}=e^{iq\ell a}$，$q$ 与 $q+G$ 描述相同的格点位移。分立波矢来自有限尺寸和周期边界，属于经典结果；模式能量的量子化是另一件事。

相速度 $v_p=\omega/q$，群速度 $v_g=d\omega/dq$。对正波矢区间

$$
v_g=a\sqrt{\frac\beta m}\cos\frac{qa}{2}.
$$

| 极限 | 频率 | 振动与传播 |
| --- | --- | --- |
| $q\to0$ | $\omega\approx v_s\lvert q\rvert$，$v_s=a\sqrt{\beta/m}$ | 相邻原子近同相，成为连续弹性波 |
| $\lvert q\rvert=\pi/a$ | $\omega_{\max}=2\sqrt{\beta/m}$ | 相邻原子反相，群速度为 0 |

区边界的群速度为零，原子仍在振动。用第一布里渊区的波矢代表定义波长时，最短代表波长为 $2a$。

### 3.3 一维双原子链

来源：S6，第 24–32、40–47 页。

本节严格沿用课件：最近邻距离为 $a$，原胞长度为 $2a$，质量 $m,M$ 交替排列，且 $M>m$，力常数均为 $\beta$。因此

$$
-\frac\pi{2a}\le q<\frac\pi{2a}.
$$

令轻、重原子振幅分别为 $A,B$，取

$$
u_{2\ell}=Ae^{i(2\ell aq-\omega t)},\qquad
u_{2\ell+1}=Be^{i((2\ell+1)aq-\omega t)}.
$$

代入牛顿方程：

$$
\begin{pmatrix}
2\beta-m\omega^2&-2\beta\cos(qa)\\
-2\beta\cos(qa)&2\beta-M\omega^2
\end{pmatrix}
\begin{pmatrix}A\\B\end{pmatrix}=0.
$$

非零解要求行列式为零，即

$$
mM\omega^4-2\beta(m+M)\omega^2+4\beta^2\sin^2(qa)=0.
$$

两条色散支为

$$
\boxed{
\omega_\pm^2(q)=\beta\left(\frac1m+\frac1M\right)
\pm\beta\sqrt{\left(\frac1m+\frac1M\right)^2
-\frac4{mM}\sin^2(qa)}
}.
$$

减号为声学支，正号为光学支，每支含 $N_c$ 个模式，总共 $2N_c$ 个，等于这个一维模型的自由度数。

| 情形 | 声学支 | 光学支 |
| --- | --- | --- |
| $q\to0$ | $\omega_-\approx a\sqrt{2\beta/(M+m)}\lvert q\rvert$；$B/A\to1$ | $\omega_+\to\sqrt{2\beta(1/m+1/M)}$；$B/A\to-m/M$ |
| $\lvert q\rvert=\pi/(2a)$ | $\omega_-^2=2\beta/M$；轻原子静止、重原子振动 | $\omega_+^2=2\beta/m$；重原子静止、轻原子振动 |

长波光学模满足 $mA+MB=0$，原胞质心不动。两支之间的频率禁带为

$$
\sqrt{2\beta/M}<\omega<\sqrt{2\beta/m}.
$$

在 $m=M$ 且力常数相同时，禁带闭合，结果相当于单原子链用更大原胞进行区折叠。

![双原子链的声学支和光学支色散](../../assets/solid-state/diatomic-dispersion.png){ width="460" }

图源：S6，第 26–27 页。横轴边界为 $\pm\pi/(2a)$，这里的 $a$ 是最近邻间距。

光学支的名称来自极性晶体中的相对离子位移可产生振荡偶极，从而与光耦合。光学模是否红外活性或 Raman 活性，仍取决于对称性与选择定则。

### 3.4 三维晶体、动力学矩阵与简正坐标

来源：S6，第 33–37 页；S7，第 4–16、38–40 页。

三维晶体有 $N_c$ 个原胞，每胞 $s$ 个原子。每个波矢有 $3s$ 条振动支，其中 3 条声学支、$3s-3$ 条光学支，总模式数为 $3sN_c=3N_{\mathrm{at}}$。

在高对称方向或近各向同性极限下，声学模可分为 1 条纵向 LA 和 2 条横向 TA；一般方向上极化可能混合。

令 $u_{\kappa\alpha}(\mathbf R)$ 为第 $\kappa$ 个原子在 $\alpha$ 方向的位移，力常数矩阵为

$$
\Phi_{\kappa\alpha,\kappa'\beta}(\mathbf R,\mathbf R')
=\left.\frac{\partial^2U}
{\partial u_{\kappa\alpha}(\mathbf R)\partial u_{\kappa'\beta}(\mathbf R')}\right|_{u=0}.
$$

势能是位移的二次型，各原子运动相互耦合。采用质量加权和傅里叶变换，问题化为

$$
D(\mathbf q)\vec{\xi}_{\mathbf q\nu}
=\omega_{\mathbf q\nu}^2\vec{\xi}_{\mathbf q\nu}.
$$

例如采用 $e^{i\mathbf q\cdot\mathbf R}$ 的胞相位约定，

$$
D_{\kappa\alpha,\kappa'\beta}(\mathbf q)
=\frac1{\sqrt{m_\kappa m_{\kappa'}}}
\sum_{\mathbf R}\Phi_{\kappa\alpha,\kappa'\beta}(0,\mathbf R)
e^{i\mathbf q\cdot\mathbf R}.
$$

$D$ 是 $3s\times3s$ 矩阵，本征矢是极化矢量，本征值是 $\omega^2$。把基元位置也放入相位会改变矩阵及本征矢的表达，但不改变频率。

对应简正坐标可定义为

$$
Q_{\mathbf q\nu}=\frac1{\sqrt{N_c}}
\sum_{\mathbf R,\kappa,\alpha}
\sqrt{m_\kappa}\,\xi_{\kappa\alpha}^*(\mathbf q\nu)
u_{\kappa\alpha}(\mathbf R)e^{-i\mathbf q\cdot\mathbf R}.
$$

逆变换为

$$
u_{\kappa\alpha}(\mathbf R)=\frac1{\sqrt{N_cm_\kappa}}
\sum_{\mathbf q\nu}\xi_{\kappa\alpha}(\mathbf q\nu)
Q_{\mathbf q\nu}e^{i\mathbf q\cdot\mathbf R}.
$$

自由度由「原胞、原子、方向」改用「波矢、分支」描述，总数不变。实位移对应 $\pm\mathbf q$ 的复共轭约束，不能把每个复数坐标当作两个额外独立自由度。

选取独立的实简正坐标后，哈密顿量成为独立振子的和：

$$
H=\frac12\sum_j(P_j^2+\omega_j^2Q_j^2).
$$

动力学矩阵出现 $\omega^2<0$ 表示在该模型和参考结构下存在不稳定方向，通常以虚频表示。稳定晶体在 $\mathbf q=0$ 有三种整体平移零频模。

### 3.5 晶格振动的量子化与声子

来源：S7，第 17–26 页。

对每个非零频简正模进行量子化：

$$
[\hat Q_j,\hat P_{j'}]=i\hbar\delta_{jj'},\qquad
\hat H_j=\hbar\omega_j\left(\hat n_j+\frac12\right),
$$

$$
E_j(n_j)=\left(n_j+\frac12\right)\hbar\omega_j,
\qquad n_j=0,1,2,\ldots.
$$

声子是晶格振动的一份激发量子：每增加一个声子，模式能量增加 $\hbar\omega$。模式数固定，占据数可变；零点能 $\hbar\omega/2$ 属于该模式，即使声子数为零也存在。

声子具有晶格准动量 $\hbar\mathbf q$，其定义允许相差 $\hbar\mathbf G$。它描述晶体内部的集体激发，不能脱离介质作为同一种自由粒子存在。

热平衡下声子数不守恒，化学势为零：

$$
\bar n_j=\frac1{e^{\hbar\omega_j/(k_BT)}-1},\qquad
\langle E_j\rangle=\hbar\omega_j\left(\bar n_j+\frac12\right).
$$

对于质量加权坐标，

$$
\langle Q_j^2\rangle=\frac\hbar{\omega_j}\left(\bar n_j+\frac12\right).
$$

低温时非零频模式的 $\bar n$ 指数减小，仍保留零点涨落；高温 $k_BT\gg\hbar\omega$ 时 $\langle E_j\rangle\approx k_BT$，恢复经典能量均分。

高温展开时要保持相同精度：$\bar n=1/x-1/2+O(x)$，其中 $x=\hbar\omega/(k_BT)$。因此 $\hbar\omega(\bar n+1/2)$ 的常数项互相抵消；只取 $\bar n\approx1/x$ 再保留零点项，容易得到不一致的次阶近似。

### 3.6 非简谐效应、热膨胀与热传导

来源：S7，第 27–30 页。

严格简谐势关于平衡位置对称，升温增大位移涨落，但不改变平均位置。考虑三阶、四阶等非简谐项后，势能的不对称性及振动频率对体积的依赖才能产生热膨胀。

![对称简谐势和非对称实际势的示意对照](../../assets/solid-state/anharmonic-potential.png){ width="460" }

图源：S7，第 27 页。绿色曲线为简谐势，蓝色为非简谐势示意；水平线表示不同振动能级。

简谐模型中简正模互不散射。真实晶体的非简谐作用、缺陷和边界限制传播距离，使晶格热导有限。各向同性动力学近似为

$$
\mathbf j_Q=-\kappa\nabla T,\qquad
\kappa\approx\frac13c_Vv\ell,
$$

其中 $c_V$ 是单位体积热容，$v$ 是代表性群速度，$\ell$ 是平均自由程。使用样品总热容时应先除以体积。

**补充**：声子散射中，正常过程的波矢和不需要加倒格矢，Umklapp 过程需要加减非零倒格矢。正常过程单独并不等同于直接弛豫全部热流；热导计算还依赖其他散射机制及边界条件。

对于有限尺寸、边界限制平均自由程的普通三维绝缘晶体，低温 $c_V\propto T^3$，常得到晶格热导也趋近于零。无限理想简谐体系需用弹道输运理解，不能直接套用有限平均自由程的扩散公式。

### 3.7 声子谱的实验测量

来源：S7，第 31–36 页。

| 手段 | 主要信息 | 适用范围与限制 |
| --- | --- | --- |
| 非弹性中子散射 | 能量与动量转移，重建声子色散 | 可覆盖广泛波矢，需要中子源及合适样品 |
| Raman 散射 | 通常探测区中心附近的 Raman 活性振动 | 常用于光学声子、薄膜和二维材料表征 |
| Brillouin 散射 | 低频声学声子、声速和弹性信息 | 光学几何与穿透深度限制可测模式 |
| 泵浦—探测／超快电子衍射 | 非平衡晶格动力学和时间演化 | 需要结合激发、选择定则和时域模型分析 |

散射测量遵循能量守恒与晶格准动量守恒。普通一阶光散射因光子波矢较小，主要探测 $q\approx0$；高阶、多声子、缺陷辅助过程可以扩展这个范围。

### 3.8 热容与杜隆—珀蒂定律

来源：S8，第 3–19 页。

总等容热容为 $C_V=(\partial U/\partial T)_V$，等压热容为 $C_P=(\partial H/\partial T)_p$。许多固体中二者接近，但并非恒等。

每个经典谐振子的动能和势能各贡献 $k_BT/2$，三维晶体有 $3N_{\mathrm{at}}$ 个模式，因此

$$
U_{\mathrm{vib}}\approx3N_{\mathrm{at}}k_BT,\qquad
C_V\approx3N_{\mathrm{at}}k_B.
$$

每摩尔**原子**为 $3R\approx24.94\ \mathrm{J\,mol^{-1}K^{-1}}$；含 $s$ 个原子的化学式单位对应每摩尔化学式单位 $3sR$。

这一经典极限要求主要振动模式满足 $k_BT\gg\hbar\omega$。金刚石等高特征频率材料即使在室温也不一定达到该极限。

### 3.9 爱因斯坦热容模型

来源：S8，第 20–26 页。

假设 $3N_{\mathrm{at}}$ 个模式均有相同频率 $\omega_E$，定义 $\Theta_E=\hbar\omega_E/k_B$。则

$$
U_E=3N_{\mathrm{at}}\hbar\omega_E
\left(\frac12+\frac1{e^{\Theta_E/T}-1}\right),
$$

$$
\boxed{C_V^E=3N_{\mathrm{at}}k_B
\left(\frac{\Theta_E}{T}\right)^2
\frac{e^{\Theta_E/T}}{(e^{\Theta_E/T}-1)^2}}.
$$

高温恢复 $3N_{\mathrm{at}}k_B$；低温为

$$
C_V^E\approx3N_{\mathrm{at}}k_B(\Theta_E/T)^2e^{-\Theta_E/T}.
$$

它说明能量量子化能使低温热容下降，但单频谱缺少趋于零频率的声学模，因而不能给出普通三维晶体的低温 $T^3$ 律。它可近似描述窄频率范围的光学模，但模型本身并未逐一建立真实的光学分支。

### 3.10 德拜态密度与截止频率

来源：S8，第 27–31、37–42 页。

德拜模型用各向同性连续弹性波近似振动谱：一条纵支、两条横支，$\omega=v_Lq$ 或 $v_Tq$。每支在波矢空间的模式密度为 $V/(2\pi)^3$，所以

$$
g(\omega)=\frac{V\omega^2}{2\pi^2}
\left(\frac1{v_L^3}+\frac2{v_T^3}\right).
$$

定义平均声速 $v_D$：

$$
\frac1{v_D^3}=\frac13\left(\frac1{v_L^3}+\frac2{v_T^3}\right),
\qquad g(\omega)=\frac{3V\omega^2}{2\pi^2v_D^3}.
$$

截止频率通过模式总数归一化确定：

$$
\int_0^{\omega_D}g(\omega)d\omega=3N_{\mathrm{at}},
$$

$$
q_D=\left(\frac{6\pi^2N_{\mathrm{at}}}{V}\right)^{1/3},
\quad\omega_D=v_Dq_D,\quad
\Theta_D=\frac{\hbar\omega_D}{k_B}.
$$

也可写成 $g(\omega)=9N_{\mathrm{at}}\omega^2/\omega_D^3$，定义在 $0\le\omega\le\omega_D$。

![三维波矢空间中半径 q、厚度 dq 的球壳](../../assets/solid-state/debye-q-shell.png){ width="420" }

图源：S8，第 29 页。球壳体积为 $4\pi q^2dq$，乘上每支波矢密度及分支数，才得到总模式数。

这是一种将全部 $3N_{\mathrm{at}}$ 个振动自由度用等效声学谱近似的热容模型。对于多原子原胞，真实声学支只有 $3N_c$ 个模式，光学支另占其余模式；德拜截止不等于真实晶体允许激发的严格边界。

### 3.11 德拜热容及高低温极限

来源：S8，第 32–36 页。

总振动能为

$$
U_D=\int_0^{\omega_D}g(\omega)\hbar\omega
\left(\frac12+\frac1{e^{\hbar\omega/(k_BT)}-1}\right)d\omega.
$$

在频率不随温度变化的模型中，零点能与温度无关，不贡献热容。令 $x=\hbar\omega/(k_BT)$，得

$$
\boxed{C_V^D=9N_{\mathrm{at}}k_B\left(\frac T{\Theta_D}\right)^3
\int_0^{\Theta_D/T}\frac{x^4e^x}{(e^x-1)^2}\,dx}.
$$

高温时 $e^x-1\approx x$，积分约为 $(\Theta_D/T)^3/3$，得到 $C_V^D\to3N_{\mathrm{at}}k_B$。

低温时将上限延至无穷大，使用

$$
\int_0^\infty\frac{x^4e^x}{(e^x-1)^2}dx=\frac{4\pi^4}{15},
$$

$$
\boxed{C_V^D\approx\frac{12\pi^4}{5}N_{\mathrm{at}}k_B
\left(\frac T{\Theta_D}\right)^3}.
$$

$T^3$ 来自三维线性色散声学模的 $g(\omega)\propto\omega^2$。低温晶格贡献由长波声学模主导，不代表所有温度下光学模都可忽略。

**补充：金属低温热容**常写为 $C_V\approx\gamma T+AT^3$。第一项来自电子，第二项来自晶格；这不是把电子项纳入德拜模型。

### 3.12 热容模型比较

| 模型 | 谱的假设 | 高温晶格热容 | 低温行为 | 主要适用意义 |
| --- | --- | --- | --- | --- |
| 经典均分 | 能量连续 | $3N_{\mathrm{at}}k_B$ | 错误地保持常数 | 高温极限 |
| 爱因斯坦 | 单一非零频率 | $3N_{\mathrm{at}}k_B$ | 指数减小 | 体现量子化，近似窄谱模式 |
| 德拜 | 连续线性色散，$g\propto\omega^2$ | $3N_{\mathrm{at}}k_B$ | $T^3$ | 普通三维晶体低温晶格热容 |

<!-- /course:body -->

## 本章小结

先数晶格自由度，再求各支色散；声子数随温度变化，模式数由结构决定。低温热容的幂律来自低频态密度。

## 自测与练习

先独立作答，再展开答案核对。

<!-- quiz:q06,q07,q08,q09,q10,q11 -->

[对应练习与检查方向](exercises.md#ex-06) · [全部闭卷自测](review.md#self-test)

## 下一步

[上一单元：第二章　晶体结合](bonding.md) · [下一单元：第四章（一）　单电子模型](electron-models.md)
