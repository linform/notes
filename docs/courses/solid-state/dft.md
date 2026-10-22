---
title: 第四章（五）　密度泛函与自洽计算
description: Hartree 与 Hartree-Fock 方法，Hohenberg-Kohn 定理与 Kohn-Sham 自洽方程，总能量双计数修正，以及平面波截断能、k 点采样与赝势方法。
status: 已整理
tags:
  - 近似方法
  - 能带结构
  - 密度泛函理论
  - 自洽计算
---

# 第四章（五）　密度泛函与自洽计算

[课程概览](index.md) · [符号约定](index.md#symbols) · [来源与订正](references.md)

!!! abstract "本章课件与配套阅读"
    **原始 PPTX**：[S14 · 33 页 · 12.9 MiB](../../assets/solid-state/slides/s14.pptx){ download="固体物理（2班）4.能带理论（6）.pptx" }。

    **对照阅读**：KS 方程、平面波与赝势：MIT Lecture 8；公式来源和赝势库见原始论文及 Quantum ESPRESSO。

    [MIT 讲义 PDF](references.md#mit-dft) · [原始论文与工具](references.md#papers) · [全部课件](index.md#course-sources)

## 学习目标

- 区分 Hartree、Hartree–Fock、HK 定理与 KS 辅助体系。
- 说明总能量双计数修正，并区分自洽、数值收敛和近似误差。

## 前置知识

量子变分、反对称波函数、泛函导数和轨道正交；先掌握能带模型。

## 核心内容

<!-- course:body -->

### 4.22 从多电子问题到 Hartree 与 Hartree–Fock

来源：S14，第 5–15 页。

下面统一用 **Hartree 原子单位**：$\hbar=m_e=e=4\pi\varepsilon_0=1$，长度单位为 Bohr 半径，能量单位为 Hartree。固定离子位置后，

$$
H_e=\sum_i\left[-\frac12\nabla_i^2+v_{\mathrm{ext}}(\mathbf r_i)\right]
+\sum_{i<j}\frac1{|\mathbf r_i-\mathbf r_j|},
\qquad
v_{\mathrm{ext}}(\mathbf r)=-\sum_I\frac{Z_I}{|\mathbf r-\mathbf R_I|}.
$$

核—核能 $E_{II}$ 对固定结构是常量，比较结构总能量时仍须加入。多电子波函数依赖 $3N_e$ 个空间变量及自旋，直接在每个坐标方向离散化会遇到维数灾难。这里的困难来自多电子相关，不能仅靠使用一个原胞完全消除。

**独立电子不等于可把电子当作可区分粒子。** 即使没有电子间相互作用，费米子多体态仍需反对称化；正交自旋轨道构成的 Slater 行列式为

$$
\Psi=\frac1{\sqrt{N_e!}}\det[\phi_i(x_j)],
$$

$x_j$ 包含空间和自旋。仅对固定非相互作用单电子哈密顿量，多体能量才直接是所占轨道本征值之和。

Hartree 方法将排斥平均为密度产生的静电势：

$$
v_H[n](\mathbf r)=\int\frac{n(\mathbf r')}{|\mathbf r-\mathbf r'|}d\mathbf r',
\qquad
E_H[n]=\frac12\iint\frac{n(\mathbf r)n(\mathbf r')}{|\mathbf r-\mathbf r'|}d\mathbf r\,d\mathbf r'.
$$

因 $\int n v_H=2E_H$，直接把每个电子受到的 Hartree 势能相加会重复计数。用完整密度还会引入形式上的自作用，需要在相应理论中处理。

Hartree–Fock 在单 Slater 行列式中变分，自动包含同自旋交换。交换算符为非局域算符，对同自旋占据轨道求和：

$$
(\hat v_x\phi_i)(\mathbf r)=
-\sum_{j\in\mathrm{occ}}\phi_j(\mathbf r)
\int\frac{\phi_j^*(\mathbf r')\phi_i(\mathbf r')}{|\mathbf r-\mathbf r'|}d\mathbf r'.
$$

它不能一般写成仅依赖当前位置的乘法势。HF 已有交换引起的费米反关联，但缺少单行列式之外的关联；不能把「HF 不含相关能」解释为两个电子的位置完全统计独立。

### 4.23 密度泛函与 Hohenberg–Kohn 定理

来源：S14，第 16–18 页。

普通函数输入数值并输出数值；泛函输入整个函数并输出一个数。例如 $F[g]=\int_0^2g(x)dx$，输入 $g(x)=3x^2$ 后输出 8。电子密度 $n(\mathbf r)$ 是非负的**粒子数密度**，满足 $\int n=N_e$；电荷密度则为 $-en$。

在固定电子数和相互作用、通常非简并基态的条件下，HK 第一定理表明：基态密度确定外势，至多相差一个加法常数，从而确定哈密顿量与基态性质。它并不表示只看一张密度图就能直接读出所有激发能。

定义普适泛函 $F[n]$ 后，

$$
E_v[n]=F[n]+\int v_{\mathrm{ext}}(\mathbf r)n(\mathbf r)d\mathbf r.
$$

HK 第二定理给出密度变分原理：对适当可表示、归一化的允许试探密度，

$$
\boxed{E_v[n]\ge E_0},\qquad \min_nE_v[n]=E_0.
$$

基态密度取等号，简并情形需相应处理，不能一律写成严格大于。难点是精确的 $F[n]$ 未知：定理在形式上精确，实际计算的误差来自泛函近似及数值处理等环节。

### 4.24 Kohn–Sham 分解与总能量

来源：S14，第 19–22 页；对照 MIT OCW 的 KS 总能量写法。

引入具有相同密度的辅助非相互作用体系，其动能为 $T_s$，把未知部分集中到交换关联泛函：

$$
\boxed{E[n]=T_s[n]+\int n v_{\mathrm{ext}}\,d\mathbf r+E_H[n]+E_{xc}[n]+E_{II}}.
$$

这里 $E_{xc}$ 不仅包含交换，还包含真实相互作用体系与辅助体系的动能差及其余关联修正。本文使用自旋轨道及占据 $0\le f_i\le1$：

$$
n(\mathbf r)=\sum_i f_i|\phi_i(\mathbf r)|^2,\quad
T_s=\sum_i f_i\left\langle\phi_i\left|-\frac{\nabla^2}2\right|\phi_i\right\rangle.
$$

若用不分自旋的空间轨道，需相应改为最大占据 2，避免再重复计入自旋简并。周期晶体的 $i$ 包含能带、$\mathbf k$ 和自旋，使用 BZ 权重时要保持每原胞／全晶体的归一化一致。

在轨道正交约束下变分，得到局域 KS 方程：

$$
\boxed{\left[-\frac{\nabla^2}2+v_{\mathrm{ext}}+v_H[n]+v_{xc}[n]\right]\phi_i
=\epsilon_i\phi_i},\qquad
v_{xc}(\mathbf r)=\frac{\delta E_{xc}}{\delta n(\mathbf r)}.
$$

外势在前文已定义为电子—核吸引的负势，因此总能量中写 **$+\int n v_{\mathrm{ext}}$**，不能再额外加一个负号。$v_{xc}$ 是泛函导数，一般不是普通数值函数的偏导。

将 KS 方程对占据轨道求和，利用 $\int n v_H=2E_H$，得到

$$
\boxed{E_{\mathrm{tot}}=\sum_i f_i\epsilon_i-E_H[n]
+E_{xc}[n]-\int n(\mathbf r)v_{xc}(\mathbf r)d\mathbf r+E_{II}}.
$$

**KS 本征值之和不是总能量。** 上式消除 Hartree 重复计数，并把本征值和中出现的 $\int n v_{xc}$ 换回能量泛函 $E_{xc}$。该写法针对局域 KS 方程；使用非局域杂化交换、赝势等时要按相应实现处理能量项。

### 4.25 交换关联近似、自洽与平面波赝势

来源：S14，第 21–28 页。

| 层次 | 采用的信息 | 例子与注意事项 |
| --- | --- | --- |
| LDA | 局域密度，对照均匀电子气 | $E_{xc}^{\mathrm{LDA}}=\int n\epsilon_{xc}^{\mathrm{unif}}(n)d\mathbf r$，$v_{xc}=d[n\epsilon_{xc}(n)]/dn$ |
| GGA | 密度及其梯度 | 如 PBE；含梯度时要进行泛函变分 |
| meta-GGA | 再引入动能密度等信息 | 如 SCAN；实现与数值收敛需额外关注 |
| 杂化泛函 | 混合部分非局域 HF 交换 | 如 PBE0、B3LYP，通常属于广义 KS 框架 |

不是名称越复杂就对所有材料越准确。比较结果前应明确泛函、自旋状态、结构和数值收敛条件。

自洽场（SCF）的逻辑闭环为

$$
n^{(j)}\ \longrightarrow\ (v_H,v_{xc})\ \longrightarrow\ H_{\mathrm{KS}}
\ \longrightarrow\ (\epsilon_i,\phi_i,f_i)\ \longrightarrow\ n_{\mathrm{out}}^{(j)}.
$$

给定离子与初始密度，先由 $\nabla^2v_H=-4\pi n$ 等求势，解 KS 方程，再按电子数填充更新密度。简单混合可写为

$$
n^{(j+1)}=(1-\alpha)n^{(j)}+\alpha n_{\mathrm{out}}^{(j)},\qquad0<\alpha\le1.
$$

检查密度残差、能量变化和电子数，而不是只看某一次本征值是否稳定。SCF 的非线性来自势依赖于待求密度；混合不当会振荡或收敛到不同亚稳态。周期带电体系的 Poisson 零模、补偿背景等还需专门处理。

晶体中的周期 KS 势同样可以用 Bloch 定理和平面波中心方程处理。通常以

$$
\frac{\hbar^2|\mathbf k+\mathbf G|^2}{2m_e}\le E_{\mathrm{cut}}
$$

截断基底；在 Hartree 单位下左侧为 $|\mathbf k+\mathbf G|^2/2$。核附近全电子轨道快速振荡，需要很高截止能。赝势方法冻结适当的芯电子，并用较平滑的价电子问题保留目标能区的散射性质。

![全电子价轨道与平滑后的赝轨道](../../assets/solid-state/pseudopotential.png){ width="700" }

图源：S14，第 27 页。图示全电子 Si 3s 轨道在核附近含节点，赝化后较平滑；目标参考态在截断半径外匹配。守恒范数、超软赝势与 PAW 的构造不同，不能把一种构造的逐点匹配或范数条件无区别地套到全部方法上。

实际计算至少分别检验 $E_{\mathrm{cut}}$、电荷密度截止、$k$ 网格和目标性质的收敛，不能用一次 SCF 收敛替代基组／BZ 积分收敛。赝势还要检查价电子配置、相对论／自旋处理、泛函兼容性与可迁移性；可参考 [Quantum ESPRESSO 官方赝势说明](https://pseudopotentials.quantum-espresso.org/)。

### 4.26 怎样理解计算出的“能带”

来源：S14，第 24、29–33 页，结合本章模型的适用范围。

| 方法／概念 | 主要输入与所得结果 | 能回答的问题与限制 |
| --- | --- | --- |
| 近自由电子 | 弱周期势的傅里叶分量 | 哪些平面波耦合、何处出现局部分裂 |
| 紧束缚 | 在位能、轨道与跃迁 | 轨道如何展宽、杂化、形成 Dirac 点等 |
| KS DFT | 离子、电子数、交换关联近似及数值设置 | 自洽基态密度、总能量与辅助单电子能谱 |

Bloch 定理是周期性的结论，不是额外的弱势或强束缚近似。NFE 与 TB 是选择不同基底、保留不同物理过程的模型；DFT 则处理有效势从何而来及多电子基态能量如何近似计算。

[KS 轨道](https://doi.org/10.1103/PhysRev.140.A1133)是构造基态密度的辅助对象，其所有本征值不能直接等同于实验加／减电子的准粒子能量。基本带隙 $I-A$、KS 带隙和含激子效应的光学吸收边是不同量；精确局域 KS 框架下基本带隙还涉及交换关联势的[导数不连续修正](https://doi.org/10.1103/PhysRevLett.51.1888)。常用 LDA/GGA 常低估半导体基本带隙，但不能把这一趋势当作所有材料的严格误差公式。使用模型带隙时也要先问清比较的是哪一个量。

课件最后介绍了激光驱动相变、高次谐波、超快自旋等研究方向。这些作为学习动机保留；实际研究涉及实时电子动力学、TDDFT、电子—核运动等扩展，不能仅凭本节静态基态 KS 方程完成。复习时优先掌握“变分泛函—有效势—自洽密度—总能量”的主线，再阅读研究实例。

<!-- /course:body -->

## 本章小结

KS 方程通过密度构造有效势并迭代到自洽。本征值求和不是总能量；数值收敛也不能消除泛函和赝势的近似误差。

## 自测与练习

先独立作答，再展开答案核对。

<!-- quiz:q30,q31,q32 -->

[对应练习与检查方向](review.md#q30) · [全部闭卷自测](review.md#self-test)

## 下一步

[上一单元：第四章（四）　紧束缚与石墨烯](tight-binding.md) · [进入习题解析](exercises.md)
