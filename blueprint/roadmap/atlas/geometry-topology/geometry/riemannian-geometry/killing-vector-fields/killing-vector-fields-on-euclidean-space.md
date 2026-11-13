---
declaration: section
origin: cited
lean: Manifold.isKillingVectorField_vectorSpace_iff, Manifold.isKillingVectorField_const, Manifold.isKillingVectorField_continuousLinearMap_iff
statement: formalized
proof: formalized
---

# Killing vector fields on Euclidean space

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-euclidean-space/index.html).

## Killing fields on Euclidean space

Let $F$ be a finite-dimensional real inner product
space, viewed as a Riemannian manifold with the metric given by its inner product. A vector field
$V$ on $F$ is Killing if and only if $V$ is $C^\infty$ and its derivative is skew-adjoint at every
point: for all $x, u, w \in F$, $\langle DV(x)\,u, w \rangle + \langle u, DV(x)\,w \rangle = 0$.

Formalized by `Manifold.isKillingVectorField_vectorSpace_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/VectorSpace.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/VectorSpace.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-euclidean-space/index.html#is-killing-vector-field-vector-space-iff).

## Translations are Killing

Let $F$ be a finite-dimensional real inner product space,
viewed as a Riemannian manifold with the metric given by its inner product. For every $c \in F$,
the constant vector field $y \mapsto c$ on $F$ is Killing.

Formalized by `Manifold.isKillingVectorField_const`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/VectorSpace.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/VectorSpace.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-euclidean-space/index.html#is-killing-vector-field-const).

## Linear Killing fields on Euclidean space

Let $F$ be a finite-dimensional real inner
product space, viewed as a Riemannian manifold with the metric given by its inner product, and let
$A \colon F \to F$ be a continuous linear map. The linear vector field $y \mapsto A y$ is Killing
if and only if $A$ is skew-adjoint: $\langle A u, w \rangle + \langle u, A w \rangle = 0$ for all
$u, w \in F$.

Formalized by `Manifold.isKillingVectorField_continuousLinearMap_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/VectorSpace.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/VectorSpace.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-euclidean-space/index.html#is-killing-vector-field-continuous-linea).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Killing vector fields on Euclidean space](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-euclidean-space/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-euclidean-space)
