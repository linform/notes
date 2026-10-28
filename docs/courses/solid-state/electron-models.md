---
title: 第四章（一）　单电子模型
description: 绝热近似、平均场与周期场近似，一维自由电子平面波归一化，以及无限深与有限深方势阱的能级与边界匹配。
status: 已整理
tags:
  - 近似方法
  - 费米统计
---

# 第四章（一）　单电子模型

[课程概览](index.md) · [符号约定](index.md#symbols) · [来源与订正](references.md)

!!! abstract "学习导读与配套资料"
    **学习目标**：区分绝热、独立电子与单电子模型中的近似；求自由电子和势阱的允许态，并检验归一化与边界条件。

    **前置知识**：薛定谔方程、波函数归一化、边界条件；简谐近似不等于电子近似。

    **原始 PPTX**：[S9 · 31 页 · 5.7 MiB](../../assets/solid-state/slides/s09.pptx){ download="固体物理（2班）4.能带理论（1）.pptx" }。

    **对照阅读**：自由电子及近似：Simon 的 Drude / Sommerfeld 模型；更系统的理论背景见 Göhmann。

    [Simon 官方全文 PDF](references.md#simon) · [Göhmann 全文 PDF](references.md#gohmann) · [全部课件](index.md#course-sources)

<!-- course:body -->

## 4.1 多体哈密顿量与三种近似

来源：S9，第 4–16、30 页。

电子坐标为 $\mathbf r_i$，原子核坐标为 $\mathbf R_I$，原子核电荷为 $Z_Ie$。非相对论库仑哈密顿量在 SI 制中为

$$
\begin{aligned}
\hat H={}&\sum_i\frac{\hat{\mathbf p}_i^2}{2m_e}
+\sum_I\frac{\hat{\mathbf P}_I^2}{2M_I}
+\frac12\sum_{i\ne j}\frac{e^2}{4\pi\varepsilon_0|\mathbf r_i-\mathbf r_j|}\\
&+\frac12\sum_{I\ne J}\frac{Z_IZ_Je^2}{4\pi\varepsilon_0|\mathbf R_I-\mathbf R_J|}
-\sum_{i,I}\frac{Z_Ie^2}{4\pi\varepsilon_0|\mathbf r_i-\mathbf R_I|}.
\end{aligned}
$$

电子—核项为负，电子—电子与核—核项为正。两个 $1/2$ 避免重复计数，求和排除同一粒子的自相互作用。

**Born–Oppenheimer 近似**：电子与核运动的时间尺度通常差别很大，先固定核位置求电子态及势能面，再处理核在势能面上的运动。

$$
\Phi(\mathbf r,\mathbf R)\approx\Psi_\alpha(\mathbf r;\mathbf R)\Xi_\alpha(\mathbf R).
$$

核坐标在电子方程中是参数。这个近似本身仍允许核的量子力学处理；将核运动写为经典牛顿方程是额外近似。低温声子热容仍需要对核的振动模式量子化。

**平均场／独立电子近似**：用有效单电子势代替显式多电子耦合，求解单粒子轨道，但电子的反对称性、占据和交换关联仍需在相应理论中处理。

**周期场近似**：理想静态周期晶体满足 $V_{\mathrm{eff}}(\mathbf r+\mathbf R)=V_{\mathrm{eff}}(\mathbf r)$。缺陷、表面和瞬时晶格振动可能破坏该理想周期性。

最终得到

$$
\left[-\frac{\hbar^2}{2m_e}\nabla^2+V_{\mathrm{eff}}(\mathbf r)\right]
\varphi(\mathbf r)=\varepsilon\varphi(\mathbf r).
$$

把电子自由度消去后得到的核有效势可能含多体项。因此「基本库仑哈密顿量含两体相互作用」与「经验原子势含三体或多体贡献」并不冲突。

## 4.2 自由电子与归一化

来源：S9，第 18–20 页。

一维自由电子满足

$$
-\frac{\hbar^2}{2m_e}\frac{d^2\varphi}{dx^2}=\varepsilon\varphi,
\quad\varphi_k(x)=Ae^{ikx},\quad
\varepsilon(k)=\frac{\hbar^2k^2}{2m_e}.
$$

无限空间的平面波是广义本征态，不能按普通平方可积函数归一化。可采用 $\delta$ 归一化，或先置于长度 $L$ 的周期盒中：

$$
\varphi_k(x)=\frac1{\sqrt L}e^{ikx},\quad
k=\frac{2\pi j}{L},\quad j\in\mathbb Z.
$$

有限盒中 $k$ 分立，$L\to\infty$ 时变为连续谱。实际局域粒子可用不同 $k$ 的平面波叠加成波包描述。

## 4.3 无限深势阱

来源：S9，第 21–24 页。

取 $V(x)=0$（$0<x<L$），区间外 $V=\infty$。边界条件 $\varphi(0)=\varphi(L)=0$ 给出

$$
\boxed{\varphi_n(x)=\sqrt{\frac2L}\sin\frac{n\pi x}{L}},
\qquad n=1,2,3,\ldots,
$$

$$
\boxed{\varepsilon_n=\frac{n^2\pi^2\hbar^2}{2m_eL^2}}.
$$

归一化来自 $\int_0^L\sin^2(n\pi x/L)dx=L/2$。$n=0$ 只给出零函数，不能作为量子态。波函数是驻波，不是单一动量本征态。

与周期盒比较：硬壁势阱给 $k_n=n\pi/L$，周期边界给 $k_j=2\pi j/L$。边界条件改变允许波矢和态计数。

课件思考题中的等间隔能级 $(n+1/2)\hbar\omega$ 对应谐振子势 $V(x)=m_e\omega^2x^2/2$，它与盒中粒子的 $n^2$ 能级规律不同。

## 4.4 有限深势阱

来源：S9，第 25–29 页。

取对称势阱，阱内 $V=0$（$|x|<L/2$），阱外 $V=V_0>0$。对于束缚态 $0<\varepsilon<V_0$，定义

$$
k=\frac{\sqrt{2m_e\varepsilon}}\hbar,\qquad
\alpha=\frac{\sqrt{2m_e(V_0-\varepsilon)}}\hbar.
$$

阱内解为正弦／余弦，阱外解为随 $|x|$ 增大而衰减的指数函数。对于相同质量、有限跳变的势能，波函数及一阶导数在边界连续。

偶宇称与奇宇称的匹配条件分别为

$$
k\tan\frac{kL}{2}=\alpha,\qquad
-k\cot\frac{kL}{2}=\alpha.
$$

令 $z=kL/2$、$z_0=(L/2)\sqrt{2m_eV_0}/\hbar$，则

$$
z\tan z=\sqrt{z_0^2-z^2}\quad\text{（偶态）},
$$

$$
-z\cot z=\sqrt{z_0^2-z^2}\quad\text{（奇态）},\qquad0<z<z_0.
$$

交点决定允许能量 $\varepsilon=2\hbar^2z^2/(m_eL^2)$。有限阱外部波函数非零，存在指数尾部；阱越深、越宽，束缚态通常越多。

一维有限宽吸引方势阱至少有一个束缚态，即使阱很浅。这一结论依赖一维模型，不能直接推广到任意三维势阱。$\varepsilon\ge V_0$ 时还存在散射态的连续谱。

## 4.5 从势阱走向周期晶体

| 模型 | 波函数 | 能谱 | 主要学习点 |
| --- | --- | --- | --- |
| 无限空间自由电子 | 平面波／波包 | 连续 | $\varepsilon\propto k^2$，广义归一化 |
| 无限深势阱 | 归一化驻波 | 离散，$\varepsilon_n\propto n^2$ | 硬壁边界限制允许态 |
| 有限深势阱 | 阱内振荡、阱外指数衰减 | 离散束缚态和连续散射态 | 边界匹配、穿透、宇称 |

孤立势阱展示束缚态；许多等价势阱周期排列时，局域轨道之间的耦合使能级展宽为能带。下一步先用对称性确定波函数形式，再选择合适的基底求能量。

<!-- /course:body -->

## 本章小结

先声明模型和边界，再求允许能级。有限体系的能级离散不能直接推出宏观电导结论。

## 自测与练习

先独立作答，再展开答案核对。

<!-- quiz:q12 -->

[对应练习与检查方向](review.md#q12) · [全部闭卷自测](review.md#self-test)

## 下一步

[上一单元：第三章　晶格振动](phonons.md) · [下一单元：第四章（二）　周期势与带隙](bloch.md)
