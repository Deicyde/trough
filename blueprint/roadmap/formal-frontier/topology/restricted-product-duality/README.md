# Restricted-product duality

> Compact finite-exceptional-stage control under T1 on a cofinite restricted product or openness of its distinguished subsets, singleton principal-stage homeomorphisms with ordinary products, coordinatewise path-component comparison for singleton cofinite products without separation hypotheses, their categorical colimit of ordinary finite Pi products and unique continuous descent from compatible stage maps, compact-map finite restriction, homotopy groups of T1 singleton cofinite restricted products, re-exports of Fundamental Groupoids' maps on path components and based postcomposition on generalized-loop homotopy quotients for arbitrary cube-index types, with identity, composition, based-homotopy and positive-homomorphism laws, together with empty-dimensional path-component naturality and naturality of both restricted-product homotopy comparisons, coordinatewise based homotopies and homotopy-invariant induced maps without separation hypotheses, based coordinate homeomorphisms of singleton cofinite products with their canonical final topologies and both-direction continuous-map, coordinate and chosen-point formulas, homotopy equivalences of canonical singleton cofinite restricted products induced by based coordinate maps and relative inverse homotopies, with forward, inverse and basepoint formulas for arbitrary factor topologies and possibly empty index types, algebraic finite-support coordinates and their composite homotopy comparison under the same T1 hypothesis, circle-valued pairings, conditional character reconstruction and symmetric Pontryagin duality, and contravariant naturality.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/formalization.yaml) of [FormalFrontier/restricted-product-duality](https://github.com/FormalFrontier/restricted-product-duality) at commit [df6cc0bb](https://github.com/FormalFrontier/restricted-product-duality/tree/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d), Apache-2.0.*

1 article: 1 for highlights of its formalization.yaml whose declarations the scan finds. The headline results in its README are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/restricted-product-duality](https://github.com/FormalFrontier/restricted-product-duality), read at commit [df6cc0bb](https://github.com/FormalFrontier/restricted-product-duality/tree/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “mathematical content reviewed”.
- Review notes: “The conditional statements for cofinite restricted products require their stated hypotheses. The general locally compact-coordinate proposition, source coverage, source-author endorsement and independent rights clearance are not claimed.”
- Automation: agent; framework “Codex CLI with Hive Tasks”; tool setup “AI agents drafted and checked Lean implementations, examples and documentation with pinned Lean/mathlib builds and separate agent review.”
- Automation notes: “AI agents developed the foundations, character reconstruction, symmetric duality, naturality and client examples with separate agent review.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Cohomology of Number Fields (corrected second edition, version 2.3)*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Proposition (1.1.13), pp. 10–11 (book; background).
- *A Concise Course in Algebraic Topology*, J. P. May (book; background).
- [mathlib4](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5) (software; background).
- [Fundamental Groupoids](https://github.com/FormalFrontier/fundamental-groupoids/tree/ce98f182cebbd2ae549dc9e7de6882a6f860cc7b), Formal Frontier Agents (software; background).

## Builds on

- [Complex analysis](../../analysis/complex-analysis/README.md) (a Lake dependency, pinned at ec0323f8)
- [Fundamental groupoids](../fundamental-groupoids/README.md) (a Lake dependency, pinned at ce98f182)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 221983a8)

## Used by

- [Fundamental groupoids](../fundamental-groupoids/README.md)

## Highlights

- [Compact Pontryagin biduality](compact-pontryagin-biduality.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/README.md#headline-results) of [FormalFrontier/restricted-product-duality](https://github.com/FormalFrontier/restricted-product-duality) at commit [df6cc0bb](https://github.com/FormalFrontier/restricted-product-duality/tree/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d), Apache-2.0.*

**Evaluation with a compact open subgroup.** For a Hausdorff abelian topological
group with a compact open subgroup, canonical Circle-valued compact-open
evaluation is surjective and open on the entire bidual. Evaluation identifies
the compact subgroup homeomorphically with the open annihilator of the
restriction kernel. No countability or metrizability hypothesis is required.
[Evaluation](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/PontryaginDual/CompactOpen.lean)

**Compact containment and finite factorization.** Every compact subset of a
**T1 restricted product** lies in one finite-exceptional stage, for arbitrary
distinguished subsets and index type; only the original restricted product,
not the factors, must be T1. The open-distinguished-subset theorem instead
needs openness, not T1. Continuous maps from compact spaces to a T1 singleton
cofinite product factor by ordinary finite coordinate restriction. No compact
stages or countable exhaustion are asserted.
[Containment](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/CompactStage.lean),
[factorization](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/FiniteStage.lean).

**Ordinary singleton stages and coordinatewise path components.** Restriction
identifies a singleton principal stage on any free set with its ordinary Pi
product; the inverse inserts the chosen points elsewhere. Finite insertions
embed and detect continuity out of the singleton cofinite product.
Its stock path-component quotient is canonically equivalent **as a set** to
the cofinite product of the factor path-component quotients, with finite
inverse reconstruction; no separation or connected-component assertion.
[Stages](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/PrincipalStage.lean),
[path components](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/PathComponents.lean).

**Factorwise connectivity and quotient maps.** For a given family `b i`,
`PointProduct b` is path connected iff every factor is path connected, and
locally path connected iff every factor is locally path connected (no path
connectedness is needed for the latter); forward instances are provided.
Raw coordinate evaluation and the **whole** insertion map from the
topological sum `Σ s : Finset ι, ∀ j : s, X j` are quotient maps. Individual
finite insertions are embeddings, not generally surjective.
[Connectivity](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/Connectivity.lean).

**Finite-stage colimit.** For given points `b i`, the original singleton
cofinite restricted product is the colimit in `TopCat` of its ordinary finite
Pi products under insertion of the given points. Compatible continuous stage
maps descend uniquely, with computation on every finite insertion. The direct
continuous-map API allows an independent, unbased observer universe; categorical
cocones belong to the fixed `TopCat` universe of the diagram. No separation or
nonempty-index assumption is needed.
[Colimit and descent](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/FiniteStageColimit.lean).

**Positive homotopy groups have finite support.** For a **T1 original
singleton cofinite restricted product**, coordinate evaluation gives a
multiplicative equivalence with the bottom-subgroup restricted product of
the factor homotopy groups, hence with
`Multiplicative (DFinsupp (fun i ↦ Additive (HomotopyGroup N (R i) (b i))))`.
The cube index `N` is arbitrary nonempty with decidable equality, not
necessarily finite; no factor T1, CW/CGWH or classification assumption.
[Comparison](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/HomotopyGroups.lean),
[DFinsupp composite](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/HomotopyGroupsFiniteSupport.lean).

**Based maps and empty-dimensional naturality.** The based-postcomposition
API is provided by [Fundamental Groupoids](https://github.com/FormalFrontier/fundamental-groupoids)
and re-exported here. For arbitrary spaces, chosen points `x`, `y` and continuous
`f` with `f x = y`, `HomotopyGroup.mapFun N f hf` acts on the generalized-loop
quotient for any cube-index type `N`, with independent source, target and cube
universes.
Representative, constant-class, identity, composition and relative-to-`{x}`
homotopy laws need no decidable equality or nonemptiness of `N`. Under the
given positive-index dictionaries it is the existing homomorphism's function.
This library supplies the comparison with `ZerothHomotopy.map`, also provided
by Fundamental Groupoids: for empty `N`, including `Fin 0`, the canonical
path-component comparison intertwines the two maps. Discrete Bool negation
computes two distinct quotient/path classes,
four comparison values and the off-basepoint square, not a nontrivial positive
homotopy group.
[Maps on homotopy quotients and zeroth naturality](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/HomotopyMaps.lean).

**Based naturality and joint homotopies.** Continuous coordinate maps preserving every
chosen point give both comparison squares. The path-component square needs
no separation; the positive square requires T1 of **both** original products.
Based postcomposition, its homomorphisms and coordinate `HomotopyRel`s
assembling jointly need no T1; based-homotopic families induce equal maps.
[Naturality](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/HomotopyMaps.lean),
[joint homotopies](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/BasedHomotopy.lean).

**Based coordinate equivalences and contractions.** Homeomorphisms carrying
each `b i` to `c i` give product homeomorphisms. Based continuous `f i`, `g i`
with both inverse homotopies relative to `{b i}`, `{c i}` give product
homotopy equivalences. Chosen factor homotopies `id → const (b i)` fixing
`b i` give a contraction and `ContractibleSpace`; mere unbased factor
contractibility is not the input. None requires separation or finite index.
[Homeomorphisms](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/BasedHomeomorphisms.lean),
[homotopy equivalences](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/HomotopyEquivalences.lean),
[contractions](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/Contractibility.lean).

**Algebraic finite-support coordinates.** At bottom submonoids, `MulOneClass`
factors give a multiplicative equivalence with `Multiplicative (DFinsupp
(fun i ↦ Additive (G i)))`. Bundled evaluation and family maps use `Monoid`;
bottom-subgroup products use `Group`. No topology or commutativity is needed;
this is not a noncommutative categorical coproduct.
[Finite support](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/FiniteSupport.lean).

**Compact abelian character separation.** For a compact Hausdorff abelian
topological group in any universe, every nonidentity element is detected by
a continuous Circle-valued character. No additional countability, probability
normalization or measurable-space input is required.
[Character separation](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/Analysis/HaarCharacter.lean).

**Compact Pontryagin biduality.** For a compact Hausdorff commutative
topological group in any universe, the original evaluation map is a continuous
multiplicative equivalence with its **entire compact-open Pontryagin bidual**.
Its inverse reconstructs every character value of a bidual element. Evaluation
and reconstruction commute with every continuous multiplicative morphism
between such groups, with independent source and target universes.
This does not assert biduality for arbitrary locally compact abelian groups.
[Compact biduality](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/PontryaginDual/Compact.lean).

**Conditional character reconstruction and duality.** For commutative groups,
local circle bicharacters and orthogonality on both distinguished subgroups
give a finite-product pairing. Joint local continuity and **both** subgroup
families open give a jointly continuous pairing and continuous dual map;
local separation gives injectivity, **not** surjectivity. A global continuous
character kills a finite-coordinate tail **of the distinguished product**.
Reconstruction requires bijective actual right local maps onto **all
algebraic** circle characters and exact right annihilator `= V`, not merely
continuous-character perfectness or nondegeneracy. Topological equivalence
additionally needs finite discrete character-domain `X i` and topological
representing `Y i`. Transposition requires finite discrete `Y i`, topological
`X i`, left local perfectness and exact left annihilator; this is not general
biduality or open mapping.
[Pairing](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/Pairing.lean),
[continuity](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/TopologicalPairing.lean),
[reconstruction](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/CharacterReconstruction.lean),
[transpose](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/SymmetricDuality.lean).

**Contravariant duality naturality.** Adjoint continuous coordinate
homomorphisms give the pairing/dual-map square with subgroup preservation
only **cofinitely** (exceptional failures allowed). The equivalence square
retains its stronger local-perfectness, exact-annihilator and finite-discrete
assumptions. [Naturality](https://github.com/FormalFrontier/restricted-product-duality/blob/df6cc0bb4483970cf5eb7d668fc7cc6f2c8e581d/RestrictedProductDuality/Naturality.lean).
