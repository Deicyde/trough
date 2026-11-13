---
declaration: section
origin: cited
lean: MathlibExt.Analysis.GleasonWanted.Analysis.IsOrthProj, MathlibExt.Analysis.GleasonWanted.Analysis.FrameFunction, MathlibExt.Analysis.GleasonWanted.Analysis.reTr, MathlibExt.Analysis.GleasonWanted.Analysis.gleason_theorem_finite, MathlibExt.Analysis.GleasonWanted.Analysis.SphereFrameFunction, MathlibExt.Analysis.GleasonWanted.Analysis.gleason_theorem_separable
statement: formalized
---

# Gleason's theorem

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html).

## Orthogonal projection

A continuous linear operator $P$ on a complex Hilbert space $H$ is
an orthogonal projection if it is idempotent, $P^2 = P$, and self-adjoint, $P^* = P$.

Formalized by `MathlibExt.Analysis.GleasonWanted.Analysis.IsOrthProj`, a definition declared in [WantedExt/Analysis/GleasonWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/GleasonWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html#is-orth-proj).

## Frame function on projections

Let $H$ be a complex Hilbert space. A frame function on
the projection lattice of $H$ is a function $\mu$ from the continuous linear operators on $H$ to
$\mathbb{R}$ such that $\mu(P) \ge 0$ for every orthogonal projection $P$ on $H$,
$\mu(P + Q) = \mu(P) + \mu(Q)$ for all orthogonal projections $P$ and $Q$ on $H$ with $PQ = 0$,
and $\mu(I) = 1$ for the identity operator $I$ on $H$.

Only the values of $\mu$ on orthogonal projections are constrained. In finite dimensions every
orthogonal family of nonzero projections is finite, so additivity on orthogonal pairs already
yields countable additivity.

Formalized by `MathlibExt.Analysis.GleasonWanted.Analysis.FrameFunction`, a structure declared in [WantedExt/Analysis/GleasonWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/GleasonWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html#frame-function).

## Real part of the trace

For a continuous linear operator $A$ on a finite-dimensional
complex Hilbert space $H$, let $\operatorname{tr}(A) \in \mathbb{C}$ be the trace of $A$ as a
$\mathbb{C}$-linear map on $H$. The real part of the trace of $A$ is the real number
$\operatorname{Re} \operatorname{tr}(A)$.

Formalized by `MathlibExt.Analysis.GleasonWanted.Analysis.reTr`, a definition declared in [WantedExt/Analysis/GleasonWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/GleasonWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html#re-tr).

## Gleason's theorem in finite dimensions

Let $H$ be a finite-dimensional complex Hilbert
space of dimension at least $3$, write $\operatorname{tr}$ for the trace of a $\mathbb{C}$-linear
map on $H$, and let $\mu$ be a frame function on the projection lattice of $H$. Then there is a
unique continuous linear operator $\rho$ on $H$ such that $\rho$ is positive,
$\operatorname{Re} \operatorname{tr}(\rho) = 1$, and
$\mu(P) = \operatorname{Re} \operatorname{tr}(\rho P)$ for every orthogonal projection $P$ on $H$.

## Sources

- A. M. Gleason, Measures on the closed subspaces of a Hilbert space, J. Math. Mech. 6 (1957), 885-893. Problem `gleason_theorem_finite` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.GleasonWanted.Analysis.gleason_theorem_finite` is written with `theorem_wanted` in [WantedExt/Analysis/GleasonWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/GleasonWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html#gleason-theorem-finite).

## Frame function on the unit sphere

Let $H$ be a complex Hilbert space. A frame function
on the unit sphere of $H$ is a function $f$ from the unit vectors of $H$ to $\mathbb{R}$ such that
$f(x) \ge 0$ for every unit vector $x$ in $H$ and, for every Hilbert basis $(b_i)_{i \in \iota}$
of $H$, the family $(f(b_i))_{i \in \iota}$ is unconditionally summable with sum $1$.

This is Gleason's 1957 notion of a frame function, normalized to weight $1$ and required to be
non-negative.

Formalized by `MathlibExt.Analysis.GleasonWanted.Analysis.SphereFrameFunction`, a structure declared in [WantedExt/Analysis/GleasonWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/GleasonWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html#sphere-frame-function).

## Gleason's theorem for separable Hilbert spaces

Let $H$ be a separable complex Hilbert
space whose dimension over $\mathbb{C}$ is at least $3$, and let $f$ be a frame function on the
unit sphere of $H$. Then there is a positive continuous linear operator $\rho$ on $H$ such that
$f(x) = \operatorname{Re} \langle x, \rho x \rangle$ for every unit vector $x$ in $H$.

The statement does not assert that $\rho$ is trace class with trace $1$, nor that $\rho$ is
unique.

## Sources

- A. M. Gleason, Measures on the closed subspaces of a Hilbert space, J. Math. Mech. 6 (1957), 885-893. Problem `gleason_theorem_separable` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.GleasonWanted.Analysis.gleason_theorem_separable` is written with `theorem_wanted` in [WantedExt/Analysis/GleasonWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/GleasonWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html#gleason-theorem-separable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gleason's theorem](https://deicyde.github.io/atlas-lean/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/QuantumInformation/quantum-foundations/gleason-s-theorem)
