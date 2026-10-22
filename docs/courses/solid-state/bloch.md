---
title: 第四章（二）　周期势与带隙
description: Bloch 定理与晶体准动量，三种能带图示方案，平面波展开中心方程，以及近自由电子模型在布里渊区边界的简并微扰开隙。
status: 已整理
tags:
  - 倒格子
  - 布里渊区
  - 色散关系
  - 能带结构
  - 微扰论
---

# 第四章（二）　周期势与带隙

[课程概览](index.md) · [符号约定](index.md#symbols) · [来源与订正](references.md)

!!! abstract "本章课件与配套阅读"
    **原始 PPTX**：[S10 · 29 页 · 6.3 MiB](../../assets/solid-state/slides/s10.pptx){ download="固体物理（2班）4.能带理论（2）.pptx" }；[S11 · 26 页 · 7.1 MiB](../../assets/solid-state/slides/s11.pptx){ download="固体物理（2班）4.能带理论（3）.pptx" }。

    **对照阅读**：Bloch 定理与弱周期势：Tong 第 2 章；进一步推导与练习见 Sigrist。

    [Tong 全文与分章 PDF](references.md#tong) · [Sigrist 全文 PDF 与练习](references.md#sigrist) · [全部课件](index.md#course-sources)

## 学习目标

- 区分 Bloch 相位、周期部分和全样品周期边界条件。
- 由中心方程寻找耦合，在简并处用正确维数的矩阵求开隙。

## 前置知识

第一章倒格子、傅里叶级数、厄米矩阵和微扰论。

## 核心内容

<!-- course:body -->

### 4.6 Bloch 定理：周期势中的电子态

来源：S10，第 5–17 页。

**问题**：晶格势破坏了连续平移对称性，为什么仍可以用波矢标记电子态？因为离散晶格平移仍与哈密顿量对易。约定平移算符作用为 $T_{\mathbf R}\psi(\mathbf r)=\psi(\mathbf r+\mathbf R)$，它们可与 $H$ 同时对角化。平移的乘法关系要求本征值满足

$$
\lambda(\mathbf R+\mathbf R')=\lambda(\mathbf R)\lambda(\mathbf R'),
\qquad \lambda(\mathbf R)=e^{i\mathbf k\cdot\mathbf R}.
$$

于是可以选取如下形式的一组能量本征态：

$$
\boxed{\psi_{n\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r}u_{n\mathbf k}(\mathbf r)},
\qquad u_{n\mathbf k}(\mathbf r+\mathbf R)=u_{n\mathbf k}(\mathbf r).
$$

因此 $\psi(\mathbf r+\mathbf R)=e^{i\mathbf k\cdot\mathbf R}\psi(\mathbf r)$，而 $|\psi|^2$ 具有晶格周期。**周期的是 $u$ 和概率密度，波函数一般只相差相位。** 简并空间内任意线性组合未必已对角化平移算符，定理保证可以选出 Bloch 基底。

一维 Born–von Karman 边界条件为 $\psi(x+N_ca)=\psi(x)$，结合 Bloch 相位得

$$
k=\frac{2\pi j}{N_ca},\qquad
-\frac\pi a\le k<\frac\pi a.
$$

第一布里渊区内每条能带有 $N_c$ 个独立 $k$ 态；若自旋简并，则可容纳 $2N_c$ 个电子。有限样品的能级分立是边界量子化的结果，不能据此判断电导为零；是否有费米能附近的可用态、散射和测量尺度都很重要。

$\mathbf k$ 与 $\mathbf k+\mathbf G$ 给出相同的平移本征值，可以只选第一布里渊区中的代表。对应态的规范可选为 $u_{n,\mathbf k+\mathbf G}=e^{-i\mathbf G\cdot\mathbf r}u_{n\mathbf k}$，从而表示同一物理态；相位和简并带的标号需要一致选择。$\hbar\mathbf k$ 称为**晶体动量／准动量**，通常不等于真实动量的确定值：Bloch 波含有多个 $\hbar(\mathbf k+\mathbf G)$ 平面波分量。

### 4.7 将全晶体问题化为原胞问题

来源：S10，第 12–14 页。

将 Bloch 形式代入单电子方程，并使用

$$
\nabla(e^{i\mathbf k\cdot\mathbf r}u)
=e^{i\mathbf k\cdot\mathbf r}(\nabla+i\mathbf k)u,
$$

得到作用在周期函数上的算符

$$
\boxed{H(\mathbf k)=\frac{(-i\hbar\nabla+\hbar\mathbf k)^2}{2m_e}+V(\mathbf r)},
\qquad H(\mathbf k)u_{n\mathbf k}=\varepsilon_n(\mathbf k)u_{n\mathbf k}.
$$

对每个 $\mathbf k$，在一个原胞中求不同本征值，便得到不同能带 $n$。不同 $\mathbf k$ 对应不同算符 $H(\mathbf k)$，不能把不同 $k$ 的周期部分直接当成同一算符的正交本征函数。

本文采用全晶体体积 $\mathcal V=N_c\Omega$，并约定 $\int_{\mathcal V}|\psi|^2d\mathbf r=1$，则 $\int_\Omega|u|^2d\mathbf r=1/N_c$。若改用原胞归一化 $\int_\Omega|\tilde u|^2=1$，Bloch 波应写成 $e^{i\mathbf k\cdot\mathbf r}\tilde u/\sqrt{N_c}$。两种约定等价，不能混用其前因子。

### 4.8 平面波展开与中心方程

来源：S10，第 18–21、28 页。

周期函数可以按倒格矢作傅里叶展开：

$$
V(\mathbf r)=\sum_{\mathbf Q}V_{\mathbf Q}e^{i\mathbf Q\cdot\mathbf r},
\qquad
V_{\mathbf Q}=\frac1\Omega\int_\Omega V(\mathbf r)e^{-i\mathbf Q\cdot\mathbf r}d\mathbf r.
$$

这里 $V_{\mathbf Q}$ 的单位是能量，$\bar V=V_{\mathbf0}$ 是平均势；实势满足 $V_{-\mathbf Q}=V_{\mathbf Q}^*$。取全晶体归一化平面波基底：

$$
\psi_{n\mathbf k}=\frac1{\sqrt{\mathcal V}}
\sum_{\mathbf G}C_{n\mathbf k}(\mathbf G)e^{i(\mathbf k+\mathbf G)\cdot\mathbf r},
\qquad \sum_{\mathbf G}|C_{n\mathbf k}(\mathbf G)|^2=1.
$$

逐个比较傅里叶分量，得到中心方程

$$
\boxed{\sum_{\mathbf G'}\left[
\frac{\hbar^2|\mathbf k+\mathbf G|^2}{2m_e}\delta_{\mathbf G\mathbf G'}
+V_{\mathbf G-\mathbf G'}\right]C_{n\mathbf k}(\mathbf G')
=\varepsilon_n(\mathbf k)C_{n\mathbf k}(\mathbf G)}.
$$

**读矩阵的方法**：行列分别代表平面波，而不是最终能带；非对角元只由两平面波相差的倒格矢决定。保留有限个 $\mathbf G$ 后，逐个 $\mathbf k$ 对角化，才得到按能量排序的 $\varepsilon_n(\mathbf k)$。势能矩阵具有平移索引结构，完整哈密顿矩阵因动能对角项而一般不是 Toeplitz 矩阵。

例如课件的 $V(x)=U_0[\cos(gx)-1]$、$g=2\pi/a$，有

$$
\bar V=-U_0,\qquad V_{\pm g}=U_0/2,
\qquad V_Q=0\ \text{（其余 }Q\text{）}.
$$

在 $G_m=mg$ 基底下，只有相邻索引耦合，矩阵为三对角。可以将所有能量整体加 $U_0$ 而去掉平均势，但必须声明能量零点改变，不能把 $\bar V$ 当作不存在。

**单位提醒**：正文至 4.20 节保留 SI 形式的 $\hbar^2/(2m_e)$。课件中令其数值为 1 是一种无量纲化／Rydberg 型单位约定；Hartree 原子单位 $\hbar=m_e=e=4\pi\varepsilon_0=1$ 中动能是 $-\nabla^2/2$，两者不可直接混用。

### 4.9 空晶格：先学会折叠，再谈开隙

来源：S10，第 22–27 页。

令势的非零波矢分量全部为零，得到空晶格能谱

$$
\varepsilon_{\mathbf G}^{(0)}(\mathbf k)=
\frac{\hbar^2|\mathbf k+\mathbf G|^2}{2m_e}+\bar V.
$$

一维是不同 $G_m=2\pi m/a$ 对应的抛物线。$m$ 是平面波分支标签，不能始终等同于按能量从低到高排序的能带编号 $n$。它们交叉时排序会交换。

| 表示方式 | 横轴如何选取 | 应如何理解 |
| --- | --- | --- |
| 扩展区 | 把分支安排到连续的多个布里渊区 | 便于联系自由电子抛物线 |
| 简约区 | 全部折回第一布里渊区，用多个带号区分 | 便于逐 $k$ 对角化和计数 |
| 重复区 | 将简约区的能带周期重复 | 显示 $\varepsilon_n(\mathbf k+\mathbf G)=\varepsilon_n(\mathbf k)$ |

**折叠本身不会开带隙。** 只有引入能够耦合交叉态的周期势分量后，才可能出现反交叉。三维高对称路径上的一条曲线只取样整个布里渊区的很小部分，不能仅凭路径上看见间隔就断言存在全局禁带。

**解中心方程的三问**：平均势是否已经移入零点？所选行列标签是哪些平面波？截断扩大后目标能带是否稳定？先回答这三问，再使用微扰或数值对角化。

### 4.10 近自由电子：远离简并点的微扰

来源：S11，第 5–11 页。

近自由电子近似把势的周期起伏看作较弱微扰，平均势先并入零级能量。对一条与其他分支充分分离的平面波分支 $\mathbf G$：

$$
\varepsilon_{\mathbf G}(\mathbf k)\approx\varepsilon_{\mathbf G}^{(0)}(\mathbf k)
+\sum_{\mathbf G'\ne\mathbf G}
\frac{|V_{\mathbf G-\mathbf G'}|^2}
{\varepsilon_{\mathbf G}^{(0)}-\varepsilon_{\mathbf G'}^{(0)}}.
$$

相应波函数的一阶修正含有

$$
\frac{V_{\mathbf G'-\mathbf G}}
{\varepsilon_{\mathbf G}^{(0)}-\varepsilon_{\mathbf G'}^{(0)}}
\frac{e^{i(\mathbf k+\mathbf G')\cdot\mathbf r}}{\sqrt{\mathcal V}}.
$$

适用条件是所保留耦合满足 $|V_{\mathbf G-\mathbf G'}|\ll|\varepsilon_{\mathbf G}^{(0)}-\varepsilon_{\mathbf G'}^{(0)}|$。分母接近零时，微扰公式的发散表示**方法失效**，不表示电子能量真的发散。远离 Bragg 条件时散射和能量修正一般较小，也并非严格等于零。

### 4.11 简并微扰、驻波与带隙

来源：S11，第 12–18、20–23 页。

保留两条接近简并的分支，中心方程化为

$$
H_2=\begin{pmatrix}\varepsilon_1^{(0)}&V_{\mathbf G_1-\mathbf G_2}\\
V_{\mathbf G_1-\mathbf G_2}^*&\varepsilon_2^{(0)}\end{pmatrix}.
$$

令 $W=V_{\mathbf G_1-\mathbf G_2}$，解二阶行列式得

$$
\boxed{\varepsilon_\pm=\frac{\varepsilon_1^{(0)}+\varepsilon_2^{(0)}}2
\pm\sqrt{\left(\frac{\varepsilon_1^{(0)}-\varepsilon_2^{(0)}}2\right)^2+|W|^2}}.
$$

在零级交叉点 $\varepsilon_1^{(0)}=\varepsilon_2^{(0)}$，局部分裂为 $\boxed{\Delta=2|W|}$。寻找交叉点应解

$$
|\mathbf k+\mathbf G_1|^2=|\mathbf k+\mathbf G_2|^2.
$$

一维给出 $k=-(G_1+G_2)/2$，再筛选第一布里渊区内的解。$G_1=0,G_2=-g$ 对应 $k=g/2$；$G_1=g,G_2=-g$ 对应 $k=0$ 的**高能分支**交叉，并不是说最低自由电子分支在 $\Gamma$ 点必然简并。

在一维区边界，互为反向的平面波叠加为驻波，两种驻波的密度峰位不同，在离子势中获得不同势能。势越能区分这两种密度分布，分裂越大。对 $V(x)=2v\cos(gx)$、实数 $v$，$\cos(gx/2)$ 与 $\sin(gx/2)$ 的能量相差 $2|v|$；哪一个较低由 $v$ 的符号决定。

![空晶格折叠与周期势引起的反交叉](../../assets/solid-state/nfe-gap.png){ width="800" }

图按中心方程数值绘制：能量单位 $E_R=\hbar^2g^2/(2m_e)$，$\bar V=0$、$V_{\pm g}=0.06E_R$，保留 $m=-6,\ldots,6$。虚线为空晶格，实线为前三条能带；区边界最低两带的分裂接近 $0.12E_R$。高阶虚过程也可引起更小的分裂。

**局部分裂不等于全局绝缘带隙**：多重简并时必须对整个简并子空间对角化；其他 $\mathbf k$ 处的带可能重叠。全局带隙需比较 $\min_{\mathbf k}\varepsilon_c(\mathbf k)-\max_{\mathbf k}\varepsilon_v(\mathbf k)$。直接带隙的两极值在同一 $\mathbf k$，间接带隙则不在同一 $\mathbf k$。三维 Bragg 面上的法向群速度可为零，切向速度不必为零。

<!-- /course:body -->

## 本章小结

空晶格折叠本身不开隙。周期势把满足倒格矢差的分量耦合，简并结构和对称性决定局部分裂；全局带隙还须检查整个布里渊区。

## 自测与练习

先独立作答，再展开答案核对。

<!-- quiz:q13,q14,q15,q16,q17,q18,q19 -->

[对应练习与检查方向](exercises.md#ex-07) · [全部闭卷自测](review.md#self-test)

## 下一步

[上一单元：第四章（一）　单电子模型](electron-models.md) · [下一单元：第四章（三）　电子统计与运动](electron-statistics.md)
