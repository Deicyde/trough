---
declaration: section
origin: cited
lean: IsSelfAdjoint.exists_spectralMeasure, MathlibExt.Analysis.InnerProductSpace.BoundedSelfAdjointSpectralWanted.boundedSelfAdjoint_spectral_multiplication
statement: formalized
proof: formalized
---

# Spectral theorem for bounded self-adjoint operators

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-bounded-self-adjoint-operat/index.html).

## Scalar spectral measure of a vector

Let $E$ be a complex Hilbert space, $T$ a bounded
self-adjoint operator on $E$ and $v \in E$. There is a finite regular measure $\mu$ on the
spectrum $\sigma(T) \subseteq \mathbb{C}$ of $T$ such that for every continuous function
$f : \sigma(T) \to \mathbb{R}$,
$\int_{\sigma(T)} f \, d\mu = \operatorname{Re} \langle f(T) v, v \rangle$, where $f(T)$ is the
continuous functional calculus of $T$ applied to $f$ viewed as a complex-valued function.

The measure lives on the complex spectrum. Its support is real because the spectrum of a
self-adjoint operator is real.

Formalized by `IsSelfAdjoint.exists_spectralMeasure`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BoundedSelfAdjointSpectral.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BoundedSelfAdjointSpectral.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-bounded-self-adjoint-operat/index.html#exists-spectral-measure).

## Spectral theorem for bounded self-adjoint operators, multiplication form

Let $E$ be a
complex Hilbert space and $T$ a bounded self-adjoint operator on $E$. Then there are a measure
space $(X, \mu)$, a measurable function $\varphi : X \to \mathbb{R}$ and a linear isometric
isomorphism $U$ of $E$ onto $L^2(X, \mu; \mathbb{C})$ such that for every $x \in E$,
$U(Tx)(a) = \varphi(a)\,(Ux)(a)$ for $\mu$-almost every $a \in X$.

Proof: Scalar measures from the continuous functional calculus identify each cyclic subspace with an
$L^2$ space. A maximal orthogonal family of cyclic subspaces is then assembled over a disjoint-union
measure, where the spectral coordinate acts by multiplication.

## Sources

- W. Rudin, Functional Analysis, 2nd ed., Ch. 12.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BoundedSelfAdjointSpectralWanted.boundedSelfAdjoint_spectral_multiplication`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BoundedSelfAdjointSpectral.lean, line 930](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/BoundedSelfAdjointSpectral.lean#L930). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-bounded-self-adjoint-operat/index.html#bounded-self-adjoint-spectral-multiplica).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectral theorem for bounded self-adjoint operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-bounded-self-adjoint-operat/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/spectral-theory/spectral-theorem-for-bounded-self-adjoint-operat)
