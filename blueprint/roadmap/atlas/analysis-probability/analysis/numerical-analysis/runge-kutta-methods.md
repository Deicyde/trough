---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ODE.RungeKutta.ExplicitRK, MathlibExt.Analysis.ODE.RungeKutta.ExplicitRK.c, MathlibExt.Analysis.ODE.RungeKutta.stageRow, MathlibExt.Analysis.ODE.RungeKutta.stage, MathlibExt.Analysis.ODE.RungeKutta.stageRow_eq_of_lt, MathlibExt.Analysis.ODE.RungeKutta.stage_eq, MathlibExt.Analysis.ODE.RungeKutta.rkStep, MathlibExt.Analysis.ODE.RungeKutta.OrderOne
statement: formalized
proof: formalized
---

# Runge–Kutta methods

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html).

## Explicit Runge–Kutta method

An explicit Runge–Kutta method with $s$ stages consists of
a real $s \times s$ Butcher tableau $a = (a_{ij})$ that is strictly lower triangular, meaning
$a_{ij} = 0$ whenever $i \le j$, and real weights $b_1, \dots, b_s$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.ExplicitRK`, a structure declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#explicit-rk).

## Nodes of a Runge–Kutta method

For an explicit Runge–Kutta method with $s$ stages and
Butcher tableau $a$, the node of stage $i$ is the row sum $c_i = \sum_j a_{ij}$, taken over all
$s$ stages $j$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.ExplicitRK.c`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#c).

## Stages computed row by row

Let $E$ be a real normed space, fix an explicit Runge–Kutta
method with $s$ stages, strictly lower-triangular tableau $a$ and nodes $c_i = \sum_j a_{ij}$, a
vector field $f$ assigning a vector $f(t', x) \in E$ to each time $t' \in \mathbb{R}$ and state
$x \in E$, a time $t$, a state $y \in E$ and a step $h \in \mathbb{R}$. The rows $K^{(n)} \in E^s$,
indexed by $0 \le i < s$, are defined by recursion on $n$: $K^{(0)} = 0$, and $K^{(n+1)}_i$ equals
$f\bigl(t + c_i h,\ y + h \sum_{j < n} a_{ij} K^{(n)}_j\bigr)$ when $i = n$ and equals
$K^{(n)}_i$ when $i \ne n$. Only the entries of $K^{(n)}$ with index less than $n$ are filled in;
the others are $0$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.stageRow`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#stage-row).

## Runge–Kutta stages

Let $E$ be a real normed space, fix an explicit Runge–Kutta method
with $s$ stages, strictly lower-triangular tableau $a$ and nodes $c_i = \sum_j a_{ij}$, a vector
field $f$ assigning a vector $f(t', x) \in E$ to each time $t' \in \mathbb{R}$ and state
$x \in E$, a time $t$, a state $y \in E$ and a step $h \in \mathbb{R}$. Let the rows
$K^{(n)} \in E^s$, indexed by $0 \le i < s$, be defined by $K^{(0)} = 0$, and $K^{(n+1)}_i$ equal
to $f\bigl(t + c_i h,\ y + h \sum_{j < n} a_{ij} K^{(n)}_j\bigr)$ when $i = n$ and to
$K^{(n)}_i$ when $i \ne n$. For $0 \le i < s$, the $i$-th stage $k_i \in E$ is the entry at
index $i$ of the row $K^{(i+1)}$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.stage`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#stage).

## Partial stage rows agree with the stages

Let $E$ be a real normed vector space and
$f(t, y)$ a vector field $\mathbb{R} \times E \to E$, and fix an explicit Runge–Kutta method,
a time $t$, a state $y \in E$ and a step size $h \in \mathbb{R}$. Index the stages from $0$.
For every natural number $m$ and every stage index $i < m$, the $i$-th entry of the $m$-th
partial row for $f$, $t$, $y$ and $h$ (the row-by-row construction that fills in the stages
with index less than $m$ and sets the rest to $0$) equals the $i$-th stage $k_i$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.stageRow_eq_of_lt`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#stage-row-eq-of-lt).

## The defining equation of the stages

Let $E$ be a real normed vector space and $f(t, y)$
a vector field $\mathbb{R} \times E \to E$. For an explicit Runge–Kutta method with tableau $a$
and nodes $c_i = \sum_j a_{ij}$, a time $t$, a state $y \in E$ and a step size $h$, the
stages $k_i$ satisfy
$k_i = f\bigl(t + c_i h, \; y + h \sum_{j < i} a_{ij} k_j\bigr)$ for every stage index $i$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.stage_eq`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#stage-eq).

## One Runge–Kutta step

Let $E$ be a real normed vector space and $f(t, y)$ a vector
field $\mathbb{R} \times E \to E$. For an explicit Runge–Kutta method with weights $b$, a
time $t$, a state $y \in E$ and a step size $h \in \mathbb{R}$, one step of the method
is $y + h \sum_i b_i k_i$, where $k_i$ is the $i$-th stage of the method for $f$, $t$, $y$
and $h$, and the sum runs over the stages.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.rkStep`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#rk-step).

## Order-one condition for Runge–Kutta methods

An explicit Runge–Kutta method with
weights $b_i$ satisfies the order-one condition when $\sum_i b_i = 1$, the sum running
over all of its stages $i$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.OrderOne`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#order-one).

## Order-two conditions for Runge–Kutta methods

An explicit Runge–Kutta method with
tableau $a$, weights $b$ and nodes $c_i = \sum_j a_{ij}$ satisfies the order-two
conditions when it satisfies the order-one condition $\sum_i b_i = 1$ and moreover
$\sum_i b_i c_i = \frac{1}{2}$, all sums running over the stages.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.OrderTwo`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#order-two).

## Order-three conditions for Runge–Kutta methods

An explicit Runge–Kutta method with
tableau $a$, weights $b$ and nodes $c_i = \sum_j a_{ij}$ satisfies the order-three
conditions when it satisfies the order-two conditions $\sum_i b_i = 1$ and
$\sum_i b_i c_i = \frac{1}{2}$, and moreover $\sum_i b_i c_i^2 = \frac{1}{3}$ and
$\sum_{i, j} b_i a_{ij} c_j = \frac{1}{6}$, all sums running over the stages.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.OrderThree`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#order-three).

## Order-four conditions

An explicit Runge–Kutta method with Butcher tableau $a$, weights
$b$ and nodes $c$ satisfies the order-four conditions when it satisfies the order-three
conditions, namely $\sum_i b_i = 1$, $\sum_i b_i c_i = 1/2$, $\sum_i b_i c_i^2 = 1/3$ and
$\sum_{i,j} b_i a_{ij} c_j = 1/6$, together with $\sum_i b_i c_i^3 = 1/4$,
$\sum_{i,j} b_i c_i a_{ij} c_j = 1/8$, $\sum_{i,j} b_i a_{ij} c_j^2 = 1/12$ and
$\sum_{i,j,k} b_i a_{ij} a_{jk} c_k = 1/24$. These are the eight Butcher conditions.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.OrderFour`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#order-four).

## Euler tableau

The explicit Runge–Kutta method with one stage, Butcher tableau
$a = (0)$ and weight $b_1 = 1$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.eulerRK`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#euler-rk).

## Midpoint tableau

The explicit Runge–Kutta method with two stages, Butcher tableau
entries $a_{21} = 1/2$ and $a_{11} = a_{12} = a_{22} = 0$, and weights $b_1 = 0$, $b_2 = 1$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.midpointRK`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#midpoint-rk).

## Heun's tableau

The explicit Runge–Kutta method with two stages, Butcher tableau entries
$a_{21} = 1$ and $a_{11} = a_{12} = a_{22} = 0$, and weights $b_1 = b_2 = 1/2$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.heunRK`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#heun-rk).

## The classical RK4 tableau

The classical fourth-order Runge–Kutta method is the
explicit four-stage Runge–Kutta method whose tableau, with stages indexed $1, \dots, 4$, has
$a_{21} = \frac{1}{2}$, $a_{32} = \frac{1}{2}$, $a_{43} = 1$ and all other $a_{ij} = 0$,
and whose weights are $b = (\frac{1}{6}, \frac{1}{3}, \frac{1}{3}, \frac{1}{6})$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.rk4`, a definition declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#rk4).

## The Euler tableau satisfies the order-one condition

The weights of the Euler
tableau sum to $1$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.eulerRK_orderOne`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#euler-rk-order-one).

## The midpoint tableau satisfies the order-two conditions

For the midpoint tableau, with
weights $b_i$ and nodes $c_i$, we have $\sum_i b_i = 1$ and $\sum_i b_i c_i = 1/2$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.midpointRK_orderTwo`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#midpoint-rk-order-two).

## Heun's tableau satisfies the order-two conditions

For Heun's tableau, with weights
$b_i$ and nodes $c_i$, we have $\sum_i b_i = 1$ and $\sum_i b_i c_i = 1/2$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.heunRK_orderTwo`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#heun-rk-order-two).

## The classical RK4 tableau satisfies all eight order-four conditions

**The classical RK4 tableau satisfies all eight order-four conditions.**

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.rk4_orderFour`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#rk4-order-four).

## The Euler tableau gives the explicit Euler step

Let $E$ be a real normed space and let
$f$ assign to each time $t \in \mathbb{R}$ and state $y \in E$ a vector $f(t, y) \in E$. For all
$t, h \in \mathbb{R}$ and $y \in E$, one Runge–Kutta step of size $h$ from the state $y$ at time
$t$ with the Euler tableau equals $y + h f(t, y)$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.euler_step`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#euler-step).

## Runge–Kutta stages tend to the vector field as the step shrinks

Let $E$ be a real normed
space, fix an explicit Runge–Kutta method with $s$ stages, a vector field $f$ assigning a vector
$f(t', x) \in E$ to each time $t' \in \mathbb{R}$ and state $x \in E$, a time $t$ and a state
$y \in E$, and suppose that $(t', x) \mapsto f(t', x)$ is continuous at $(t, y)$. For a step
$h \in \mathbb{R}$, let $k_i(h)$ be the $i$-th stage of the method with step $h$. Then for every
natural number $n$ and every stage index $i < n$, $k_i(h) \to f(t, y)$ as $h \to 0$ with
$h \ne 0$.

The proof is by strong induction on the stage index, since earlier stages appear in later ones.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.stage_tendsto`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#stage-tendsto).

## Consistency of explicit Runge–Kutta methods

Let $E$ be a real normed vector space,
let $f(t, y)$ be a vector field $\mathbb{R} \times E \to E$, let $t \in \mathbb{R}$ and
$y \in E$, and for an explicit Runge–Kutta method with weights $b$ let $y_1(h)$ be the
result of one step of size $h$ from the state $y$ at time $t$. If $\sum_i b_i = 1$ and $f$
is continuous at $(t, y)$ as a function of both variables, then
$h^{-1} (y_1(h) - y) \to f(t, y)$ as $h \to 0$ with $h \neq 0$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.rkStep_sub_inv_smul_tendsto`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#rk-step-sub-inv-smul-tendsto).

## Stability function of the classical RK4 method

For all real numbers $\lambda$, $y$
and $h$, one step of size $h$ of the classical fourth-order Runge–Kutta method applied to
the scalar linear test equation $u' = \lambda u$ on $\mathbb{R}$, starting from the state
$y$ at time $0$, gives $y \, R(\lambda h)$, where
$R(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24}$.

Formalized by `MathlibExt.Analysis.ODE.RungeKutta.rk4_stability`, a theorem declared in [MathlibExt/Analysis/ODE/RungeKutta.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/RungeKutta.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html#rk4-stability).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Runge–Kutta methods](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/runge-kutta-methods/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/numerical-analysis/runge-kutta-methods)
