---
declaration: section
origin: cited
lean: hasDerivAt_piecewise_union_of_eqOn, MathlibExt.Analysis.ODE.MaximalSolutionWanted.ode_global_exists_of_global_lipschitz, MathlibExt.Analysis.ODE.MaximalSolutionWanted.ode_maximal_solution_exit_compact
statement: formalized
proof: formalized
---

# Maximal solutions and global existence

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/maximal-solutions-and-global-existence/index.html).

## Gluing solutions of an ODE

Let $E$ be a real normed space, let
$v : \mathbb{R} \times E \to E$, let $I, J \subseteq \mathbb{R}$ be open, and let
$x, y : \mathbb{R} \to E$ satisfy $x'(t) = v(t, x(t))$ for every $t \in I$ and
$y'(t) = v(t, y(t))$ for every $t \in J$, with $x = y$ on $I \cap J$. Then there is
$z : \mathbb{R} \to E$ with $z = x$ on $I$, $z = y$ on $J$ and $z'(t) = v(t, z(t))$ for every
$t \in I \cup J$.

Formalized by `hasDerivAt_piecewise_union_of_eqOn`, a theorem declared in [MathlibExt/Analysis/ODE/MaximalSolution.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/MaximalSolution.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/maximal-solutions-and-global-existence/index.html#has-deriv-at-piecewise-union-of-eq-on).

## Global existence and uniqueness for globally Lipschitz ODEs

Let $E$ be a real Banach
space, let $f : \mathbb{R} \times E \to E$ be continuous, and let $L \ge 0$ be such that
$f(t, \cdot)$ is $L$-Lipschitz for every $t \in \mathbb{R}$. Then for every $t_0 \in \mathbb{R}$
and $x_0 \in E$ there is exactly one function $x : \mathbb{R} \to E$ with $x(t_0) = x_0$ and
$x'(t) = f(t, x(t))$ for every $t \in \mathbb{R}$.

Proof: local Picard--Lindelöf solutions are continued using the Gronwall bound of Teschl's
Theorem 2.17 and the extension criterion of Lemma 2.14.  Time reversal supplies the
negative-time solution, and global Gronwall uniqueness identifies every solution with the glued
one.

## Sources

- G. Teschl, Ordinary Differential Equations and Dynamical Systems, Section 2.2; stable ref https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem.

Formalized by `MathlibExt.Analysis.ODE.MaximalSolutionWanted.ode_global_exists_of_global_lipschitz`, a theorem declared in [MathlibExt/Analysis/ODE/MaximalSolution.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/MaximalSolution.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/maximal-solutions-and-global-existence/index.html#ode-global-exists-of-global-lipschitz).

## Solutions of locally Lipschitz ODEs that leave every compact set

Let $E$ be a real
Banach space, let $U \subseteq \mathbb{R} \times E$ be open, let $(t_0, x_0) \in U$, and let
$f : \mathbb{R} \times E \to E$ be continuous on $U$ and locally Lipschitz in the state variable,
uniformly in time: every $p \in U$ has a neighbourhood $N$ and a constant $C \ge 0$ such that
$\|f(t, u) - f(t, w)\| \le C \|u - w\|$ whenever $(t, u)$ and $(t, w)$ lie in $N \cap U$. Then
there are an open interval $I$ (possibly unbounded) containing $t_0$ and a function
$x : \mathbb{R} \to E$ with $x(t_0) = x_0$ such that $(t, x(t)) \in U$ and
$x'(t) = f(t, x(t))$ for every $t \in I$, and such that for every compact $K \subseteq U$ there
are $c_1, c_2 \in I$ with $(t, x(t)) \notin K$ for every $t \in I$ with $t \ge c_1$ and for
every $t \in I$ with $t \le c_2$.

Proof: local Picard--Lindelöf solutions are glued by uniqueness into Teschl's maximal solution
(Theorem 2.13).  A compactly recurrent finite endpoint extends by Lemma 2.14, giving the two exit
statements of Corollaries 2.15--2.16.

## Sources

- G. Teschl, Ordinary Differential Equations and Dynamical Systems, Section 2.4.

Formalized by `MathlibExt.Analysis.ODE.MaximalSolutionWanted.ode_maximal_solution_exit_compact`, a theorem declared in [MathlibExt/Analysis/ODE/MaximalSolution.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/MaximalSolution.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/maximal-solutions-and-global-existence/index.html#ode-maximal-solution-exit-compact).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximal solutions and global existence](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/maximal-solutions-and-global-existence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/ordinary-differential-equations/maximal-solutions-and-global-existence)
