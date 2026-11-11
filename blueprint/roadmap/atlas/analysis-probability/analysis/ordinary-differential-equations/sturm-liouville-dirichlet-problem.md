---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ODE.SturmLiouvilleExistence.sturm_liouville_existence, MathlibExt.Analysis.ODE.SturmLiouvilleUniqueness.sturm_liouville_uniqueness, MathlibExt.Analysis.Distribution.Dirichlet1DWanted.dirichlet_1d_exists, MathlibExt.Analysis.Distribution.Dirichlet1DWanted.dirichlet_1d_unique
statement: formalized
---

# Sturm–Liouville Dirichlet problem

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/sturm-liouville-dirichlet-problem/index.html).

## Existence for the Sturm–Liouville Dirichlet problem on the closed unit interval

Let $V$
and $f$ be continuous real functions on $[0, 1]$ with $V \ge 0$. Then there is a function
$u \colon \mathbb{R} \to \mathbb{R}$ that is $C^2$ on $[0, 1]$, satisfies
$-u''(x) + V(x)\,u(x) = f(x)$ for every $x \in [0, 1]$, with the second derivative taken within
$[0, 1]$, and has $u(0) = u(1) = 0$.

The proof is by the shooting method: let $u_0$ solve the equation with $u_0(0) = u_0'(0) = 0$,
and let $w$ solve the homogeneous equation $-w'' + V w = 0$ with $w(0) = 0$ and $w'(0) = 1$. An
energy argument using $V \ge 0$ shows $w(1) \ne 0$, and $u = u_0 + a w$ with
$a = -u_0(1)/w(1)$ is the required solution.

## Sources

- `SpectralTheory.sturm_liouville_existence` in the v1 formalization, whose formalization is left unproved there; the proof here is original.

Formalized by `MathlibExt.Analysis.ODE.SturmLiouvilleExistence.sturm_liouville_existence`, a theorem declared in [MathlibExt/Analysis/ODE/SturmLiouvilleExistence.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/SturmLiouvilleExistence.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/sturm-liouville-dirichlet-problem/index.html#sturm-liouville-existence).

## Uniqueness for the Sturm–Liouville Dirichlet problem on the closed unit interval

Let $V$
and $f$ be continuous real functions on $[0, 1]$ with $V \ge 0$, and let
$u_1, u_2 \colon \mathbb{R} \to \mathbb{R}$ be $C^2$ on $[0, 1]$. Suppose that for $i = 1, 2$,
$-u_i''(x) + V(x)\,u_i(x) = f(x)$ for every $x \in [0, 1]$, with the second derivative taken
within $[0, 1]$, and $u_i(0) = u_i(1) = 0$. Then $u_1$ and $u_2$ agree on $[0, 1]$.

Formalized by `MathlibExt.Analysis.ODE.SturmLiouvilleUniqueness.sturm_liouville_uniqueness`, a theorem declared in [MathlibExt/Analysis/ODE/SturmLiouvilleUniqueness.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/SturmLiouvilleUniqueness.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/sturm-liouville-dirichlet-problem/index.html#sturm-liouville-uniqueness).

## Existence for the one-dimensional Dirichlet problem

Let $f : \mathbb{R} \to \mathbb{R}$ be
continuous on $[0, 1]$. Then there is a twice continuously differentiable function
$u : \mathbb{R} \to \mathbb{R}$ with $u(0) = u(1) = 0$ and $u''(x) = f(x)$ for every
$x \in (0, 1)$.

## Sources

- L. Evans, *Partial Differential Equations*, Ch. 6.

Stated but not proved: `MathlibExt.Analysis.Distribution.Dirichlet1DWanted.dirichlet_1d_exists` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/Dirichlet1DWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/Dirichlet1DWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/sturm-liouville-dirichlet-problem/index.html#dirichlet-1d-exists).

## Uniqueness for the one-dimensional Dirichlet problem

Let $f : \mathbb{R} \to \mathbb{R}$ be
any function, and let $u_1, u_2 : \mathbb{R} \to \mathbb{R}$ be twice continuously
differentiable functions such that, for $i = 1, 2$, $u_i(0) = u_i(1) = 0$ and
$u_i''(x) = f(x)$ for every $x \in (0, 1)$. Then $u_1(x) = u_2(x)$ for every $x \in [0, 1]$.

## Sources

- L. Evans, *Partial Differential Equations*, Ch. 6.

Stated but not proved: `MathlibExt.Analysis.Distribution.Dirichlet1DWanted.dirichlet_1d_unique` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/Dirichlet1DWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/Dirichlet1DWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/sturm-liouville-dirichlet-problem/index.html#dirichlet-1d-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sturm–Liouville Dirichlet problem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/sturm-liouville-dirichlet-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/ordinary-differential-equations/sturm-liouville-dirichlet-problem)
