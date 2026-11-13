---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.cubicFamily, MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsCriticalPoint, MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.basinOfZero, MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsImmediateBasin, MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.parameterSet, MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsParameterComponent, MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsJordanCurve, MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.conjecture
statement: formalized
---

# Parameter space of cubic polynomials

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html).

## Cubic family

For a parameter $\lambda \in \mathbb{C}$, the cubic polynomial map
$f_\lambda : \mathbb{C} \to \mathbb{C}$ is given by $f_\lambda(z) = \lambda z^2 + z^3$.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.cubicFamily`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#cubic-family).

## Critical points of the cubic family

For $\lambda \in \mathbb{C}$, a point
$c \in \mathbb{C}$ is a critical point of $f_\lambda(z) = \lambda z^2 + z^3$ when $f_\lambda$ has
complex derivative $0$ at $c$, that is, $f_\lambda'(c) = 0$.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsCriticalPoint`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#is-critical-point).

## Basin of attraction of zero

For $\lambda \in \mathbb{C}$, the basin of zero of
$f_\lambda(z) = \lambda z^2 + z^3$ is the set of $z \in \mathbb{C}$ whose forward orbit tends to
$0$, that is, $f_\lambda^{n}(z) \to 0$ as $n \to \infty$, where $f_\lambda^{n}$ denotes the
$n$-th iterate of $f_\lambda$.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.basinOfZero`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#basin-of-zero).

## Immediate basin of zero

For $\lambda \in \mathbb{C}$, a set $V \subseteq \mathbb{C}$ is
the immediate basin of zero of $f_\lambda(z) = \lambda z^2 + z^3$ when $0 \in V$, $V$ is contained
in the basin of zero of $f_\lambda$ (the set of $z$ with $f_\lambda^{n}(z) \to 0$), $V$ is
connected, and every connected set $W \subseteq \mathbb{C}$ with $0 \in W$ that is contained in the
basin of zero of $f_\lambda$ satisfies $W \subseteq V$. Thus $V$ is the connected component of $0$
in the basin of zero.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsImmediateBasin`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#is-immediate-basin).

## Parameters with both critical points in the immediate basin

The parameter set is the set
of $\lambda \in \mathbb{C}$ for which some immediate basin of zero $V$ of
$f_\lambda(z) = \lambda z^2 + z^3$ contains every critical point of $f_\lambda$.

Since $f_\lambda'(z) = z(3z + 2\lambda)$, the critical points of $f_\lambda$ are $0$ and
$-2\lambda/3$ (equal when $\lambda = 0$), so this asks that both finite critical points lie in
the immediate basin of zero.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.parameterSet`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#parameter-set).

## Parameter components

A set $U \subseteq \mathbb{C}$ is a parameter component when it is
a connected component of the parameter set, the set of $\lambda \in \mathbb{C}$ for which every
critical point of $f_\lambda(z) = \lambda z^2 + z^3$ lies in the immediate basin of zero of
$f_\lambda$: $U$ is nonempty, contained in the parameter set and connected, and every connected
set $W \subseteq \mathbb{C}$ with $U \subseteq W$ that is contained in the parameter set equals
$U$.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsParameterComponent`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#is-parameter-component).

## Jordan curves in the plane

A set $S \subseteq \mathbb{C}$ is a Jordan curve when there is
a continuous injective map $f$ from the unit circle $\{z \in \mathbb{C} : |z| = 1\}$ to
$\mathbb{C}$ whose image is exactly $S$.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.IsJordanCurve`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#is-jordan-curve).

## McMullen's question on Jordan boundaries of cubic parameter components

Let
$f_\lambda(z) = \lambda z^2 + z^3$ for $\lambda \in \mathbb{C}$. The statement is that for every
parameter component $U$, that is, every connected component of the set of $\lambda$ for which
every critical point of $f_\lambda$ lies in the immediate basin of zero of $f_\lambda$, the
boundary $\partial U$ of $U$ in $\mathbb{C}$ is a Jordan curve.

The source poses this as an open question.

## Sources

- [AMR-052-0019], Stony Brook open problems (1992), McMullen III.2.

Formalized by `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.conjecture`, a definition declared in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#conjecture).

## Roesch's theorem on the boundaries of cubic parameter components

For the cubic family
$f_\lambda(z) = \lambda z^2 + z^3$ with $\lambda \in \mathbb{C}$, the boundary of every parameter
component is a Jordan curve. Here a parameter component is a connected component of the set of
$\lambda$ for which every critical point of $f_\lambda$ lies in the immediate basin of zero of
$f_\lambda$.

Roesch (Theorem 2) proves that the boundary of every component of
$H = \{a : -a \text{ lies in the basin of } 0\}$ for the family $z^{d-1}(z + da/(d-1))$ is a
Jordan curve; at $d = 3$ the linear change $\lambda = 3a/2$ carries the central component $H_0$
onto the parameter component.

## Sources

- Pascale Roesch, Hyperbolic components of polynomials with a fixed critical point of maximal order, Ann. Sci. Ecole Norm. Sup. (4) 40 (2007), arXiv:math/0612172, https://arxiv.org/abs/math/0612172.

Stated but not proved: `MathlibExt.Dynamics.CubicParameterJordanBoundaryWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/CubicParameterJordanBoundaryWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Parameter space of cubic polynomials](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/complex-dynamics/parameter-space-of-cubic-polynomials)
