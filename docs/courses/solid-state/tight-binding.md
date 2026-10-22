---
title: 第四章（四）　紧束缚与石墨烯
description: 局域轨道 Bloch 和与跃迁矩阵元，一维链与简单立方 s 带色散，以及石墨烯双子格紧束缚哈密顿量、Dirac 锥线性色散与能带接触条件。
status: 已整理
tags:
  - 色散关系
  - 能带结构
  - 紧束缚
  - 石墨烯
---

# 第四章（四）　紧束缚与石墨烯

[课程概览](index.md) · [符号约定](index.md#symbols) · [来源与订正](references.md)

!!! abstract "本章课件与配套阅读"
    **原始 PPTX**：[S13 · 27 页 · 7.4 MiB](../../assets/solid-state/slides/s13.pptx){ download="固体物理（2班）4.能带理论（5）.pptx" }。

    **对照阅读**：紧束缚：Tong 第 2 章；石墨烯：第 3 章。Sigrist 适合继续学习多轨道模型。

    [Tong 全文与分章 PDF](references.md#tong) · [Sigrist 全文 PDF 与练习](references.md#sigrist) · [全部课件](index.md#course-sources)

## 学习目标

- 从局域轨道、邻居和跃迁矩阵建立紧束缚模型。
- 区分轨道数、能带数、局部接触点和全局绝缘条件。

## 前置知识

Bloch 定理、轨道正交与矩阵本征值；注意跃迁符号约定。

## 核心内容

<!-- course:body -->

### 4.18 紧束缚：从局域轨道到能带

来源：S13，第 2–15 页。

近自由电子从平面波出发，紧束缚则从原子附近的局域轨道出发。首先考虑两个等价、已正交化的轨道 $\phi_B,\phi_C$，取实跃迁矩阵元 $t_1$：

$$
H=\begin{pmatrix}\varepsilon_c&t_1\\t_1&\varepsilon_c\end{pmatrix},
\quad
\psi_s=\frac{\phi_B+\phi_C}{\sqrt2},\quad
\psi_a=\frac{\phi_B-\phi_C}{\sqrt2}.
$$

两态能量分别为 $\varepsilon_c+t_1$ 和 $\varepsilon_c-t_1$。在常用的同相 $s$ 轨道约定下 $t_1<0$，对称组合为较低的成键态，反对称组合为较高的反键态，分裂恒为 $2|t_1|$。轨道相位改变会改变矩阵元符号和组合写法，物理能谱不变。

若直接用有重叠 $s=\langle\phi_B|\phi_C\rangle$ 的实轨道，则归一化需改为 $\sqrt{2(1\pm s)}$，能量为 $(\varepsilon_c\pm t_1)/(1\pm s)$；矩阵问题为 $Hc=\varepsilon Sc$。不能一面保留显著重叠，一面按正交基直接对角化 $H$。

周期晶体中，对每种局域轨道构造 Bloch 和：

$$
\chi_{\alpha\mathbf k}(\mathbf r)=\frac1{\sqrt{N_c}}
\sum_{\mathbf R}e^{i\mathbf k\cdot\mathbf R}
\phi_\alpha(\mathbf r-\mathbf R-\vec\tau_\alpha).
$$

平移并重新编号 $\mathbf R$ 可验证 $\chi(\mathbf r+\mathbf R_0)=e^{i\mathbf k\cdot\mathbf R_0}\chi(\mathbf r)$。波函数在这些 Bloch 和中展开，矩阵元为局域轨道间实空间跃迁的傅里叶和：

$$
H_{\alpha\beta}(\mathbf k)=\sum_{\mathbf R}
t_{\alpha\beta}(\mathbf R)e^{i\mathbf k\cdot\mathbf R},
\qquad t_{\alpha\beta}(\mathbf R)=\langle\phi_{\alpha\mathbf0}|H|\phi_{\beta\mathbf R}\rangle.
$$

有 $M$ 个空间轨道基函数便得到 $M$ 条能带（未计自旋）；非正交基用 $H(\mathbf k)c=\varepsilon S(\mathbf k)c$。在位能修正 $t_0$ 是对角项，不能称为跨原胞的跃迁积分。

### 4.19 一维链与简单立方 s 带

来源：S13，第 10–11、16–18、21–23 页。

在位能 $\varepsilon_c=\varepsilon_{\mathrm{at}}+t_0$，最近邻实跃迁为带符号的 $t_1$。一维均匀链有

$$
\boxed{\varepsilon(k)=\varepsilon_c+2t_1\cos(ka)},\qquad W=4|t_1|.
$$

$t_1<0$ 时带底在 $\Gamma$、带顶在 $\pi/a$。孤立原子极限 $t_1\to0$，整条带收缩为一个原子能级；波函数重叠增大通常使 $|t_1|$ 增大、带宽变宽，但具体符号由轨道和相位约定决定。

有限开边界 $N$ 原子链的本征能量是

$$
\varepsilon_j=\varepsilon_c+2t_1\cos\frac{j\pi}{N+1},\qquad j=1,\ldots,N.
$$

这些能级一般不等间隔；原子数很大时才形成稠密的带。周期链的离散 $k$ 与开链的正弦本征态属于不同边界条件，不能混合计数。

简单立方格子每原胞一个 $s$ 轨道，六个最近邻给出

$$
\boxed{\varepsilon_s(\mathbf k)=\varepsilon_c+2t_1
[\cos(k_xa)+\cos(k_ya)+\cos(k_za)]},\quad W=12|t_1|.
$$

对 $t_1<0$，$\Gamma$ 为带底、$R=(\pi/a,\pi/a,\pi/a)$ 为带顶；$X=(\pi/a,0,0)$ 的能量为 $\varepsilon_c+2t_1$。在 $\Gamma$ 展开得到 $m^*=\hbar^2/(2|t_1|a^2)$，把跃迁强度与电子响应联系起来。

多轨道形成多条带，但**不保证存在全局带隙**：杂化在局部可能开隙，其他动量处仍可重叠或受对称性保护相接。不能仅以「有多个轨道」判断绝缘。

### 4.20 简单立方 p 轨道：方向决定跃迁

来源：S13，第 19–20 页。完整作业结果见例 8。

沿 $p$ 轨道轴向的最近邻跃迁记为 $t_\sigma$，垂直方向记为 $t_\pi$。忽略自旋轨道耦合，并在立方轴向最近邻模型中忽略不同 $p$ 轨道间的跃迁：

$$
\begin{aligned}
\varepsilon_{p_x}&=\varepsilon_p+2t_\sigma\cos(k_xa)
+2t_\pi[\cos(k_ya)+\cos(k_za)],\\
\varepsilon_{p_y}&=\varepsilon_p+2t_\sigma\cos(k_ya)
+2t_\pi[\cos(k_xa)+\cos(k_za)],\\
\varepsilon_{p_z}&=\varepsilon_p+2t_\sigma\cos(k_za)
+2t_\pi[\cos(k_xa)+\cos(k_ya)].
\end{aligned}
$$

课件取 $t_\sigma>0,t_\pi<0$，符合其轨道相位约定。方向重叠解释各向异性，但仅凭「距离更近」不能推出跃迁积分的正负；相对波函数相位、节点和哈密顿量均参与积分。

### 4.21 石墨烯：两个子格与 Dirac 锥

来源：S13，第 24–27 页；联系 1.1 节。

石墨烯的平面内 $sp^2$ 杂化轨道主要形成 $\sigma$ 键；课件的双轨道最近邻模型保留每个碳原子的一个垂直平面的 $p_z$ 轨道，描述费米能附近的 **$\pi$ 与 $\pi^*$ 能带**。两个子格并非两种元素。

沿用 1.1 节的最近邻距离 $d$ 和原始基矢，不把 $d$ 与晶格常数 $\sqrt3d$ 混淆。在原胞相位规范下，

$$
f(\mathbf k)=1+e^{-i\mathbf k\cdot\mathbf a_1}
+e^{-i\mathbf k\cdot\mathbf a_2}
=1+2e^{-3idk_x/2}\cos\frac{\sqrt3dk_y}{2}.
$$

若跃迁为实数 $t_1$，在位能为 $\varepsilon_A,\varepsilon_B$：

$$
H(\mathbf k)=\begin{pmatrix}\varepsilon_A&t_1f(\mathbf k)\\
t_1f^*(\mathbf k)&\varepsilon_B\end{pmatrix},
\quad
\varepsilon_\pm=\bar\varepsilon\pm\sqrt{\Delta^2+t_1^2|f|^2},
$$

其中 $\bar\varepsilon=(\varepsilon_A+\varepsilon_B)/2$、$\Delta=(\varepsilon_A-\varepsilon_B)/2$。等价碳子格有 $\Delta=0$，且

$$
|f|^2=1+4\cos^2\frac{\sqrt3dk_y}{2}
+4\cos\frac{\sqrt3dk_y}{2}\cos\frac{3dk_x}{2}.
$$

在 $\mathbf K_\pm=(0,\pm4\pi/(3\sqrt3d))$ 有 $f=0$，两带接触。令 $\mathbf k=\mathbf K_\pm+\mathbf q$，最低阶为

$$
\boxed{\varepsilon_\pm\approx\bar\varepsilon\pm\hbar v_F|\mathbf q|},
\qquad v_F=\frac{3|t_1|d}{2\hbar}.
$$

这便是 Dirac 锥。若两子格在位能不等，则该模型在 Dirac 点开隙 $2|\Delta|$。两条带、两个子格并不自动意味着绝缘体；是否开隙由对称性与具体矩阵决定。

![石墨烯最近邻模型的能带与 Dirac 锥](../../assets/solid-state/graphene-bands.png){ width="800" }

图由上式绘制，取 $\bar\varepsilon=\Delta=0$，能量单位为 $|t_1|$。左图路径 $\Gamma\to M\to K\to\Gamma$，$M=(\pi/(3d),\pi/(\sqrt3d))$、$K=(0,4\pi/(3\sqrt3d))$，$M$ 是与该 $K$ 相邻的区边中点。右图显示一个 $K$ 点附近的双锥面。

含自旋 2 与谷简并 2，低能总 DOS 为 $D(\varepsilon)=2A|\varepsilon-\bar\varepsilon|/[\pi(\hbar v_F)^2]$。它在理想中性 Dirac 点为零；$M$ 附近的鞍点导致另一种 van Hove 奇性，不能把整个能带的 DOS 都近似为线性。

**与第一章的联系**：蜂窝结构的两原子基元在这里成为两分量轨道基底，三角布拉维格子给出 $\mathbf k$ 的周期性。结构因子决定衍射振幅，$f(\mathbf k)$ 决定本模型的子格间跃迁；二者都来自带相位求和，但分别属于不同物理量。

<!-- /course:body -->

## 本章小结

紧束缚把原胞轨道间的跃迁变成波矢依赖矩阵。轨道方向、基元和对称性共同决定色散，多个轨道不自动产生绝缘带隙。

## 自测与练习

先独立作答，再展开答案核对。

<!-- quiz:q27,q28,q29 -->

[对应练习与检查方向](exercises.md#ex-08) · [全部闭卷自测](review.md#self-test)

## 下一步

[上一单元：第四章（三）　电子统计与运动](electron-statistics.md) · [下一单元：第四章（五）　密度泛函与自洽计算](dft.md)
