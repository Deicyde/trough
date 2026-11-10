# Simplicial objects

> Functorial augmented left decalage of simplicial objects with a canonical extra degeneracy, and finite-fiber coproduct, diagram and simplicial chain transfers with induced homology maps, coefficient naturality and sheet identities, together with normalized-chain descent and coefficient comparisons coherent with arbitrary coefficient-valued maps, finite-fiber transfers and transformations of additive coproduct-preserving functors, and an integral tensor presentation of normalized chains for arbitrary simplicial sets and abelian coefficient groups, with integral and tensor degree maps for arbitrary simplicial morphisms, a fixed-coefficient natural tensor-chain comparison and its induced all-arrow cokernel natural isomorphism, additive functoriality, degreewise exactness and preservation of finite limits and finite colimits in abelian coefficients, and chain homotopies induced by simplicial homotopies and equality of the corresponding induced homology maps. Simplicial homotopy inverses induce quasi-isomorphisms of normalized chains and of the original integral tensor complexes with arbitrary abelian coefficients. Degree-zero normalized tensor homology is isomorphic to the coproduct of the lifted coefficient object over simplicial components, with raw vertex and signed boundary formulas, all-map simplicial naturality, and universe-balanced additive coefficient and mixed naturality. Binary products give an isomorphism from the tensor of the two degree-zero homology modules to product homology with tensor coefficients, natural in both simplicial and coefficient variables in each direction, with independent coefficient, simplex and padding universes and vertex-class characterizations. The component fold agrees with collapse to a terminal simplicial set for every source; connected sets have a coefficient isomorphism, and the empty standard boundary has zero degree-zero homology. For terminal simplicial sets, degree-zero tensor homology has mutually inverse comparisons with the lifted coefficient object, natural in coefficients and terminal-set maps; positive-degree tensor homology vanishes, with dimension-bound vanishing for arbitrary simplicial sets. Injective and surjective coefficient maps preserve endpoints, and short exact coefficient pairs give short exact sequences of these chain complexes. For arbitrary simplicial sets, Mathlib's zeroth-homology coproduct isomorphism and its inverse are natural in coefficient morphisms, with an all-degree coefficient-generator law. Integral all-simplex chains have degreewise Finsupp coordinates for every simplicial set and degree, using the universe-lifted integer coefficient object, with morphism-level and unit summand laws.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/formalization.yaml) of [FormalFrontier/simplicial-objects](https://github.com/FormalFrontier/simplicial-objects) at commit [e210890f](https://github.com/FormalFrontier/simplicial-objects/tree/e210890fdc170ec8425587eea91c11d4c60c3b87), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 10 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/simplicial-objects](https://github.com/FormalFrontier/simplicial-objects), read at commit [e210890f](https://github.com/FormalFrontier/simplicial-objects/tree/e210890fdc170ec8425587eea91c11d4c60c3b87) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “unchecked”.
- Automation: agent; framework “Formal Frontier agents and Lean 4”; tool setup “AI-assisted Lean formalization and mathematical documentation.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Standard ordinal and simplicial identities* (folklore; background).
- *A Concise Course in Algebraic Topology*, J. Peter May, Revised author edition, §12.1–2, §13.1, §16.1, §16.4 and §16, Problem 3 (book; background).

## Builds on

- [Projective modules](../../ring-theory/projective-modules/README.md) (a Lake dependency, pinned at 08efdc37)

## Used by

- [Sphere topology](../../topology/sphere-topology/README.md)


## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/README.md#headline-results) of [FormalFrontier/simplicial-objects](https://github.com/FormalFrontier/simplicial-objects) at commit [e210890f](https://github.com/FormalFrontier/simplicial-objects/tree/e210890fdc170ec8425587eea91c11d4c60c3b87), Apache-2.0.*

**Integral all-simplex chain coordinates**
([`chainGroupIsoFinsupp`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/ChainCoordinates.lean),
[`chainComplexIsoFinsupp`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/ChainComplexCoordinates.lean)).
For any ring `R`, `AlgebraicTopology.finsuppChainComplexFunctor R` gives the
ordinary-Finsupp alternating-face chain complex, with independent ring and
simplex universes. Over `ℤ`, `chainComplexIsoFinsupp` is a natural isomorphism
from the existing `SSet.chainComplexFunctor` at the original coefficient object
`(ModuleCat.uliftFunctor.{u} ℤ).obj (ModuleCat.of ℤ ℤ)` to this functor.
For every `X : SSet.{u}` and degree `n`, its evaluation isomorphism is exactly
`chainGroupIsoFinsupp X n`: both forward and inverse degree maps are the
original maps on every chain, not merely on generators. The two summand laws
still compute lifted integers and unit basis chains. Naturality holds for
every simplicial map and every chain; pushforwards add coefficients of
coincident images, without finite-fiber or injectivity assumptions.
In every degree the [boundary coordinates](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/ChainBoundaryCoordinates.lean)
are the signed sum of face pushforwards. This comparison concerns all simplices,
not normalized chains or homology. The
[standard-point chain](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjectsTest/ChainCoordinates.lean) is nonzero;
the [identity edge of `Δ[1]`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjectsTest/ChainBoundaryCoordinates.lean)
has boundary `[v₁] - [v₀]`, nonzero as a chain, not as a homology class.

**Augmented left décalage and its canonical extra degeneracy**
([`LeftDecalage`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/LeftDecalage.lean)).
For every simplicial object in any category, `P(X)ₙ = Xₙ₊₁` augments to `X₀`,
with `ε₀ = X.δ 1`, not in general the ordinary projection `X.δ 0`.
No terminal/zero objects, additivity or limits are required. Functoriality and
naturality are explicit; Mathlib supplies the section and combinatorial homotopy.

**Finite-fiber transfers and coefficient comparison**
([`FiniteFiberTransfer`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/FiniteFiberTransfer.lean)).
In a preadditive category with simplex-indexed coproducts, equifibered simplicial
maps with finite vertex fibers admit reverse-composing transfers. No fixed sheet
number is needed. A constant vertex-fiber cardinality `d` gives pushforward
after transfer equal to `d • id` on chains and, with homology, in every degree.
Additive functors preserving those coproducts commute with transfer; no exactness
or homology preservation is assumed. Pullback and coefficient laws are included.

**Normalized descent and change of coefficient category**
([`Normalization`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/Normalization.lean)).
Morphisms between split simplicial objects in a preadditive category descend
without preserving chosen nondegenerate summands. For preadditive coefficient
categories with `HasCoproducts.{w}`, additive functors preserving exactly
`Discrete T` colimits for `T : Type w` compare normalized chains naturally,
compatibly with projection, section, transfers and natural transformations.
All five category/simplex universes are independent; no exactness or Abelian
assumption is needed. These are distinct from the integral tensor presentation.

**Integral tensor chains, simplicial maps and homotopies**
([`TensorCoefficients`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorCoefficients.lean),
[`TensorMaps`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorMaps.lean),
[`TensorHomotopies`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorHomotopies.lean)).
For every abelian group `A` and simplicial set `S`, the independently defined
alternating tensor boundary gives a complex naturally isomorphic to normalized
chains with lifted coefficients. Coefficient, simplex and padding universes are
independent; no finiteness, flatness, field or nonemptiness is assumed.
Simplicial monomorphisms give monic chain maps without flatness of `A`.
Combinatorial or cylinder homotopies give chain homotopies and equal homology maps;
two-sided simplicial homotopy inverses and extra-degenerate augmentations give
quasi-isomorphisms. For normalized chains the coefficient category need only be
preadditive with coproducts and homology; augmentation targets need not be terminal.
[Cokernel comparison](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorCokernels.lean) applies to all arrows;
its nonzero omitted-vertex example concerns chain cokernels, not homology.

**Additive and exact change of abelian coefficients**
([`TensorCoefficientMaps`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorCoefficientMaps.lean),
[`TensorCoefficientFunctor`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorCoefficientFunctor.lean),
[`TensorCoefficientSequences`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorCoefficientSequences.lean)).
Arbitrary additive maps act by `id ⊗ g`, naturally in both variables, on the
original tensor carriers and boundary. The coefficient-curried functor is
additive and preserves finite limits and colimits. Any exact coefficient pair
stays exact degreewise; injective and surjective endpoints give chain Mono/Epi
and short exactness. Universes remain independent with common balanced padding;
no coefficient flatness or endpoint assumption is added to middle exactness.
This is exactness of a chain-valued functor, not exactness after homology.

**Degree-zero homology, components and path components**
([`TensorHomologyZero`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorHomologyZero.lean),
[`SingularHomologyZero`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/SingularHomologyZero.lean)).
For every abelian `A` and simplicial set `S`, tensor `H₀` is the coproduct of
`ModuleCat.of ℤ (ULift.{max w p} A)` over `SSet.π₀ S`, naturally in simplicial
and additive coefficient maps, with independent `a`, `w`, `p` and no finiteness,
flatness, field, basis or nonemptiness hypotheses. For singular simplices of any
topological space this gives the coproduct over `ZerothHomotopy X`, naturally in
continuous and coefficient maps, without local path connectedness. The direct
[path-component functor](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/PathComponents.lean) agrees naturally
with singular components via Mathlib's equivalence.

**Degree-zero normalized homology of binary products**
([`tensorNormalizedHomologyZeroProductIso`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorHomologyZeroProducts.lean)).
For arbitrary abelian groups `A`, `B` and simplicial sets `K`, `L`,
`H₀ᴺ(K; A) ⊗ℤ H₀ᴺ(L; B) ≅ H₀ᴺ(K × L; A ⊗ℤ B)`, using canonical
universe lifts with independent coefficient, simplex and padding universes.
Pure tensors of vertex classes map to the paired vertex class with pure tensor
coefficient; inverse formulas, extensionality and uniqueness characterize the maps.
[Forward and inverse naturality](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorHomologyZeroProductNaturality.lean)
hold for simplicial maps in both factors and arbitrary additive maps in both
coefficient groups, with balanced padding for coefficient change. No finiteness,
flatness, connectedness or nonemptiness is assumed. A
[discrete two-by-two example](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjectsTest/TensorHomologyZeroProducts.lean)
distinguishes the four nonzero vertex tensors and their four product classes,
and evaluates simplicial and coefficient maps on them.

**Component folds, terminal sets and dimension vanishing**
([`TensorHomologyZeroConnected`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorHomologyZeroConnected.lean),
[`TensorHomologyZeroEmpty`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/TensorHomologyZeroEmpty.lean),
[`PointHomology`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/PointHomology.lean)).
The fold agrees with collapse and terminal coefficient evaluation for every
source, including the empty one. Connectedness makes the fold an isomorphism.
Terminal sets have the lifted coefficient object in degree zero and zero
positive homology. More generally `S.HasDimensionLT d` gives vanishing in
degrees `n ≥ d`; `H₀(∂Δ[0])` is zero. Arbitrary abelian coefficients and independent
coefficient/simplex/padding universes are retained.

**Coefficient naturality of ordinary simplicial `H₀`**
([`HomologyZero`](https://github.com/FormalFrontier/simplicial-objects/blob/e210890fdc170ec8425587eea91c11d4c60c3b87/SimplicialObjects/HomologyZero.lean)).
Mathlib's `SSet.homology₀Iso` and its inverse commute with every coefficient
morphism in any preadditive category with `HasCoproducts.{w}` and homology,
with independent object, morphism and simplex universes. The all-degree
coefficient-generator law needs no homology assumption. This is separate from
normalized tensor homology and asserts no singular or relative comparison.
