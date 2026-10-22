---
title: 固体物理 · 复习速查与自测
description: 概念联系、解题流程、易错点与可展开答案的闭卷自测。
status: 已整理
tags:
  - 习题与自测
---

# 复习速查与自测

[课程概览](index.md) · [习题解析](exercises.md) · <a href="../../../downloads/solid-state-anki.csv" download="固体物理-Anki自测卡.csv">下载 Anki 记忆卡（CSV）</a>

<!-- course:body -->

### 需要能独立解释的联系

| 联系 | 核心解释 |
| --- | --- |
| 晶格与衍射 | 周期平移允许特定倒格矢，基元决定相应振幅 |
| 结合与振动 | 平衡点的一阶导数为零，二阶曲率决定简谐力常数 |
| 振动与热容 | 色散决定态密度，量子统计决定每种模式的平均能量 |
| 原胞与模式数 | 每原胞 $s$ 个原子，三维每波矢就有 $3s$ 个振动模式 |
| 声子与电子 | 共用倒格子和布里渊区，但能量、统计及自由度不同 |
| 势阱与能带 | 局域能级经轨道耦合展宽；周期性决定 Bloch 形式，边界决定允许 $k$ |
| 倒格矢与开隙 | 平面波动量相差倒格矢才有周期势耦合；简并处需对角化 |
| DOS 与热容 | DOS 数“有多少态”，费米分布数“占多少态”，只有费米能附近参与低温激发 |
| 色散与动力学 | 一阶导数给群速度，二阶导数给逆有效质量 |
| 轨道与 Dirac 点 | 两子格形成两条 π 带；结构相位和在 $K$ 点抵消，使两带接触 |
| 模型与 DFT | NFE／TB 用给定势或跃迁理解能带；DFT 自洽近似基态有效势和总能量 |

### 能带题的最短解题流程

1. 写出晶格、基底、边界、单位和电子数；先确定求的是能量、态密度还是响应。
2. 弱周期势先作傅里叶分解；局域轨道模型先列在位能与跃迁，保持厄米性。
3. 画零级分支并定位简并；非简并处微扰，多重简并处扩大矩阵。
4. 需要物性时再填充：$D\to N_e,\mu,C_V$，$\varepsilon(\mathbf k)\to\mathbf v,m^*$。
5. 检查自由电子／孤立原子极限、量纲、自旋计数及是否误把局部结论推广为全局。

### 易错点检查

- [ ] 写结构时同时给出布拉维格子、基元种类和坐标。
- [ ] 写坐标与指数时注明采用原胞还是惯用胞基矢。
- [ ] 计算 XRD 时先把 $2\theta$ 除以 2，再检查允许反射。
- [ ] 计算强度用振幅模平方，区分几何条件和结构因子消光。
- [ ] 计算结合能时写清正负约定及每原子／每离子对单位。
- [ ] 双原子链的原胞长度取 $2a$，区边界取 $\pi/(2a)$。
- [ ] 区分经典分立波矢、模式频率和量子化的能量占据。
- [ ] 数模式时使用 $N_c$、$s$ 和 $N_{\mathrm{at}}$，另算声子占据数。
- [ ] 德拜模型先将 $g(\omega)$ 积分归一化，再求热容。
- [ ] 热导公式使用单位体积热容，势阱波函数检查归一化。
- [ ] Bloch 波只要求晶格平移相差相位；全样品周期边界另行施加。
- [ ] 中心方程先列 $V_{\mathbf Q}$，非对角耦合查 $\mathbf G-\mathbf G'$，平均势单独处理。
- [ ] 区分平面波索引与最终带号；多重简并不套单个二阶矩阵。
- [ ] 区分局部反交叉与全局带隙，判断导电性还要给电子填充。
- [ ] DOS 声明总量／每体积和自旋因子；热容在固定电子数下展开。
- [ ] 区分 $E_F$ 与 $\mu(T)$，经典极限比较 $\varepsilon-\mu$ 和 $k_BT$。
- [ ] 有效质量先求能量 Hessian；张量求逆与逐元素倒数不同。
- [ ] 跃迁能量与时间采用不同符号，检查 $T_B$ 的 $2\pi$ 及散射条件。
- [ ] TB 说明轨道相位、跃迁符号、边界条件；非正交轨道保留重叠矩阵。
- [ ] 石墨烯区分 C—C 距离与晶格常数，区分 $sp^2$ 的 σ 键与 $p_z$ 的 π 带。
- [ ] DFT 统一原子单位和外势符号；$E_{xc}$、$v_{xc}$ 与 KS 本征值各不相同。
- [ ] 区分 SCF 自洽、基组／$k$ 网格收敛，以及泛函近似误差。

<span id="self-test"></span>

### 闭卷自测

先作答，再展开答案。每章末的自测来自这里，同一道题只维护一份答案。

<!-- question:q01 -->
<span id="q01"></span>

??? question "为什么蜂窝格子需要双原子基元？"
    沿连接两个子格的最近邻位移平移，不能使整套原子位置与原排列重合；平移格子是三角格子

<!-- /question -->

<!-- question:q02 -->
<span id="q02"></span>

??? question "BCC 的 WS 原胞和第一布里渊区各是什么形状？"
    实空间 WS 原胞为截角八面体；倒空间第一布里渊区为菱形十二面体

<!-- /question -->

<!-- question:q03 -->
<span id="q03"></span>

??? question "为什么 CsCl 的布拉维格子是 SC？"
    角点与体心原子种类不同，体心位移不是晶格平移

<!-- /question -->

<!-- question:q04 -->
<span id="q04"></span>

??? question "FCC 的 $(100),(110),(111),(200)$ 哪些允许？"
    单原子 FCC 允许 $(111),(200)$

<!-- /question -->

<!-- question:q05 -->
<span id="q05"></span>

??? question "金刚石的 $(200),(220),(222)$ 哪些允许？"
    $(220)$ 允许；$(200),(222)$ 由双原子基元消光

<!-- /question -->

<!-- question:q06 -->
<span id="q06"></span>

??? question "原胞含 4 个原子时有多少声学和光学支？"
    三维共有 12 支，其中 3 支声学、9 支光学

<!-- /question -->

<!-- question:q07 -->
<span id="q07"></span>

??? question "单原子链区边界 $v_g=0$，原子是否静止？"
    仍振动，零群速度表示该模式没有通常波包意义下的传播速度

<!-- /question -->

<!-- question:q08 -->
<span id="q08"></span>

??? question "光学模是否一定红外活性？"
    需要相应偶极变化与选择定则，不能由分支名称直接判断

<!-- /question -->

<!-- question:q09 -->
<span id="q09"></span>

??? question "零点振动存在，为什么简谐零点能不贡献热容？"
    固定频率下零点能不随温度变化，温度导数为零

<!-- /question -->

<!-- question:q10 -->
<span id="q10"></span>

??? question "一维和三维线性色散德拜模型低温热容为何不同？"
    态密度分别为常数与 $\omega^2$，产生 $T$ 与 $T^3$

<!-- /question -->

<!-- question:q11 -->
<span id="q11"></span>

??? question "BO 近似是否允许声子量子化？"
    允许；核经典化是额外近似

<!-- /question -->

<!-- question:q12 -->
<span id="q12"></span>

??? question "无限深势阱为什么没有 $n=0$ 态？"
    它对应处处为零的波函数，不能归一化

<!-- /question -->

<!-- question:q13 -->
<span id="q13"></span>

??? question "Bloch 波函数是否具有原胞周期？"
    一般只有周期部分 $u$ 与密度有原胞周期，$\psi$ 平移后多出相位

<!-- /question -->

<!-- question:q14 -->
<span id="q14"></span>

??? question "每条带可以容纳多少电子？"
    每带 $N_c$ 个 $k$ 态，自旋简并时容纳 $2N_c$ 个电子

<!-- /question -->

<!-- question:q15 -->
<span id="q15"></span>

??? question "准动量是否等于真实动量？"
    一般不等；Bloch 波可含多个 $\hbar(\mathbf k+\mathbf G)$ 分量

<!-- /question -->

<!-- question:q16 -->
<span id="q16"></span>

??? question "把自由电子抛物线折回第一 BZ，会开带隙吗？"
    不会；开隙需要具体耦合，且受简并结构和对称性限制

<!-- /question -->

<!-- question:q17 -->
<span id="q17"></span>

??? question "$V(x)=2v\cos(gx)$ 的第一处区边界分裂是多少？"
    弱势两态近似为 $2\lvert v\rvert$，不是 $4\lvert v\rvert$

<!-- /question -->

<!-- question:q18 -->
<span id="q18"></span>

??? question "$\Gamma$ 点出现简并是否表示最低带简并？"
    未必；空晶格的 $+G$ 与 $-G$ 高能分支可在此简并

<!-- /question -->

<!-- question:q19 -->
<span id="q19"></span>

??? question "高对称路径上有间隔能证明全局禁带吗？"
    不能，需检查整个 BZ 的导带最低点与价带最高点

<!-- /question -->

<!-- question:q20 -->
<span id="q20"></span>

??? question "三维自由电子 DOS 的自旋 2 应计几次？"
    只计一次；若 $D$ 已包含它，粒子数积分外不再乘 2

<!-- /question -->

<!-- question:q21 -->
<span id="q21"></span>

??? question "$f(\mu)=1/2$ 是否说明禁带中有半占据态？"
    不说明；占据函数可以在不存在态的能量处取值

<!-- /question -->

<!-- question:q22 -->
<span id="q22"></span>

??? question "化学势是否总随温度降低？"
    不是；固定电子数时低温趋势取决于 $D'(E_F)$，一维抛物线带先升高

<!-- /question -->

<!-- question:q23 -->
<span id="q23"></span>

??? question "为什么金属电子低温热容是 $T$ 而非经典常数？"
    热激发窗口宽约 $k_BT$，可参与的态数也正比于 $T$

<!-- /question -->

<!-- question:q24 -->
<span id="q24"></span>

??? question "$C_V/T$ 对 $T^2$ 的截距和斜率是什么？"
    在 $C_V=\gamma T+AT^3$ 区间，分别为电子系数 $\gamma$ 与晶格系数 $A$

<!-- /question -->

<!-- question:q25 -->
<span id="q25"></span>

??? question "恒电场为何可能产生振荡而非持续加速？"
    $k$ 线性变化，但群速度由周期能带的一阶导数决定

<!-- /question -->

<!-- question:q26 -->
<span id="q26"></span>

??? question "把 Hessian 的各元素取倒数是否得到质量张量？"
    不是；先除以 $\hbar^2$ 得逆质量张量，再作矩阵求逆

<!-- /question -->

<!-- question:q27 -->
<span id="q27"></span>

??? question "一维最近邻链带宽是多少？"
    $4\lvert t_1\rvert$；简单立方单 $s$ 轨道是 $12\lvert t_1\rvert$

<!-- /question -->

<!-- question:q28 -->
<span id="q28"></span>

??? question "有两个轨道就必然绝缘吗？"
    不必；两带可相交或重叠，石墨烯最近邻 π 模型就是反例

<!-- /question -->

<!-- question:q29 -->
<span id="q29"></span>

??? question "石墨烯中性点 DOS 为零是否意味着整条带没有态？"
    不是；仅 Dirac 点附近线性趋零，其他能量存在大量态和鞍点奇性

<!-- /question -->

<!-- question:q30 -->
<span id="q30"></span>

??? question "KS 本征值求和为什么不等于总能量？"
    Hartree 项重复计数，且 $\int n v_{xc}$ 需换回 $E_{xc}$，还要计核—核能

<!-- /question -->

<!-- question:q31 -->
<span id="q31"></span>

??? question "SCF 收敛是否保证计算结果已可信？"
    还需基组、$k$ 网格等数值收敛，并检查泛函和赝势的适用性

<!-- /question -->

<!-- question:q32 -->
<span id="q32"></span>

??? question "静态基态 DFT 能否直接描述激光实时动力学？"
    不能直接；须使用适当的时间依赖理论及动力学处理

<!-- /question -->

<!-- question:q33 -->
<span id="q33"></span>

??? question "结合能取负值与取正值的约定能否混用？"
    不能。先声明参考态和每原子／每离子对的计量单位，再统一符号后比较。

<!-- /question -->

<!-- question:q34 -->
<span id="q34"></span>

??? question "怎样从势能曲线判断平衡位置与稳定性？"
    平衡位置满足一阶导数为零；沿所考察形变方向的局部稳定还要求二阶导数为正。

<!-- /question -->

对于蜂窝格子，判断平移是否成立要比较整套原子排列，不能只比较一根最近邻连线。对于声子问题，先数自由度、再判断极限，最后检验公式，通常能快速发现漏因子或错误符号。

<!-- /course:body -->
