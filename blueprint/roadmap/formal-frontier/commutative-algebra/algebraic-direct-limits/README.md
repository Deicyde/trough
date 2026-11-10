# Algebraic direct limits

> Reusable Lean results for constant identity function and ring-homomorphism systems, varying-scalar directed limits, tensor products, countably cofinal inverse systems, simple filtered ring colimits, prime spectra of filtered commutative-ring colimits, Krull dimension under finite-subset capture, for directed colimits and for directed subsemiring unions, localization of countable products, cofinal group completions, monoidal-category object classes with actual-image cofinality, same-topology scalar restriction, linear continuity for coinduced topological modules, module topology under continuous linear injections into semisimple modules, module topology on finite-dimensional strong duals without complete scalars, continuous finite-basis coordinates and binary-product distribution for one-sided tensor products, continuous tensor universal properties, continuous dual tensor contraction and its finite-left equivalence with bounded-convergence Hom spaces, the scalar tensor unit, continuous associativity with whole continuous lift/curry compatibility, compactness for finitely generated tensor coefficients, noncompactness with infinite free coefficients, discreteness for tensors with a discrete right factor, arbitrary-basis and projective tensor Hausdorffness preservation, scalar extension by discrete coefficient algebras with separate base-linear and coefficient-linear views, a continuous unit and functorial continuous maps, and a rational-circle counterexample to flat-coefficient tensor Hausdorff preservation, with an algebraic quotient detector and dense rational-angle tensor-vanishing laws. The coefficient tensor–continuous Hom adjunction preserves existing colimits.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/formalization.yaml) of [FormalFrontier/algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits) at commit [e5d0dea1](https://github.com/FormalFrontier/algebraic-direct-limits/tree/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 16 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits), read at commit [e5d0dea1](https://github.com/FormalFrontier/algebraic-direct-limits/tree/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “unchecked”.
- Review notes: “Independent agent reviews cover the existing direct-limit contributions, including the prime-spectrum comparison, the coinduced-module continuity criterion and the one-sided tensor-topology continuity and map API. Tensor universal-property and scalar-unit constructions have characteristic algebraic bridges, uniqueness and naturality laws, with integer-pair and boundary examples. Scalar restriction has characteristic action and forgetful agreements, natural identity and composition comparisons, and a semiring regular-action continuity criterion with Algebra agreement. Discrete scalar extension retains separate scalar views and has characteristic action, map, unit and underlying-module comparisons, with matrix/countable- product and same-ring swapping rank-one clients. The two complementary tensor-Hom naturality laws and nine example conclusions are included. This does not assert source-author endorsement or complete formal coverage of a source. API documentation is partial; see docs/CREDITS.md and docs/README.md.”
- Automation: agent; framework “Codex CLI and Formal Frontier agent workflows”; tool setup “Pinned Lean 4, mathlib, Lake, and Git”
- Automation notes: “AI-assisted Formal Frontier agents developed and assembled this library. A complete list of models used in earlier contributions is unavailable. Independent review is distinct from authorship.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [Stacks Project, Algebra, Lemma 10.86.3: Mittag-Leffler systems](https://stacks.math.columbia.edu/tag/0597) (web post; background).
- [mathlib4 mathematical library](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5) (software; background).

## Builds on

No other Formal Frontier library.

## Used by

- [Multivariate polynomials](../multivariate-polynomials/README.md)
- [Projective modules](../../ring-theory/projective-modules/README.md)


## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/README.md#headline-results) of [FormalFrontier/algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits) at commit [e5d0dea1](https://github.com/FormalFrontier/algebraic-direct-limits/tree/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c), Apache-2.0.*

**Module direct limits as colimits of types.** For a semimodule system over
a semiring, indexed by a nonempty directed preorder with decidable equality,
the canonical maps into `Module.DirectLimit` form a colimiting cocone of types.
Transition maps need not be injective, and the scalar, index and stage
universes are independent. See
[Module](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Algebra/Colimit/Module.lean).

**Directed Grothendieck additive groups.** A coherent, jointly surjective
family of additive maps over a binary-directed index relation induces a
jointly surjective family on the original Grothendieck additive groups;
transition identity and composition laws are not needed for this conclusion.
Over a directed preorder, if the transitions form a directed system and raw
cocone equality is witnessed at a common stage, equality of arbitrary
completed images is equivalent to equality at a common completed stage.
No cancellation or injectivity of transitions, cocone maps, or canonical
completion maps is assumed. See
[DirectedGroupCompletion](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/DirectedGroupCompletion.lean).

**Finite matrix units.** Over a nonempty directed preorder of semirings
with bundled ring-hom transitions, `DirectLimit.matrixUnitsColimitEquiv`
identifies the limit of square-matrix unit groups with the matrix units
over the coefficient limit. The dimension has `Fintype` and `DecidableEq`
and may be empty; transitions need not be injective. See the
[matrix-units guide](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/docs/MatrixUnits.md) and
[source module](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Matrix/Units.lean).

**Finite dependent products and representatives.** For directed systems of
types over a nonempty directed preorder, `DirectLimit.piEquiv` identifies the
limit of a finite dependent product with the product of the coordinate limits.
Its forward map is the canonical coordinate comparison `DirectLimit.piMap`.
Transition maps may be arbitrary function-like maps and coordinate carriers
may be empty; neither injectivity nor algebraic structure is needed. Every
finite dependent family of limit elements has representatives at one common
stage. See [Pi](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Order/DirectLimit/Pi.lean).
`DirectLimit.forall_mk_eq_iff_exists` characterizes equality of two finite
families of quotient classes by equality of their transported functions at
one common stage. Its `_of_fixed` variant bounds both supplied input stages,
including for an empty family, without a separate nonempty-index assumption.
See [DirectedSystem](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Order/DirectedSystem.lean) and the
[first-order and paired-matrix examples](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimitsExamples/FiniteRepresentatives.lean).

**Finite-support coefficient descent.** Over a nonempty directed preorder,
finitely supported functions commute with direct limits of types with zero
whose selected transition maps preserve zero. The coefficient index may be
arbitrary, and each function has a representative at one stage with exactly
the same support. Neither injective transitions nor additive structure are
required. See [Finsupp](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Data/Finsupp.lean).

**Semilinear quotient descent.** A continuous semilinear map from a module
over a ring to a module over a semiring descends through any submodule in
its kernel, retaining the original module structures and quotient topology.
The codomain need only be an additive commutative monoid; continuity of
module operations is not assumed. See
[Quotient](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Topology/Module/Quotient.lean).

**Varying scalars and tensor products.** For compatible semilinear module
systems over a nonempty directed preorder, the tensor product of the two
module limits over the varying commutative-semiring limit is equivalent to
the limit of the stagewise tensor products. Transition maps need not be
injective. See [VaryingScalar](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/VaryingScalar.lean).

**Mittag--Leffler inverse systems.** A pointwise nonempty, Type-valued
Mittag--Leffler inverse system over a nonempty directed preorder with a
countable cofinal subset has a compatible section. Under the same index and
Mittag--Leffler conditions, each element of an eventual range lifts to a
section without a separate pointwise-nonemptiness assumption. See
[MittagLeffler](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/MittagLeffler.lean).

**Prime spectra of filtered colimits.** For a small filtered category and
any colimit cocone of commutative rings, its spectrum cone is a limit in
topological spaces. The chosen-limit homeomorphism identifies coordinates
with contraction along the cocone maps; no injectivity or nonzero-ring
assumption is required. See
[PrimeSpectrumFilteredColimits](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/PrimeSpectrumFilteredColimits.lean).

**Krull dimension under finite-subset capture.** For homomorphisms
`φ i : A i →+* B` of commutative semirings, if every finite subset of `B`
lies in the range of one `φ i`, then
`ringKrullDim B ≤ ⨆ i, ringKrullDim (A i)`. The family need not be directed
and the maps need not be injective; dimensions include `⊥` and `⊤`. See
[FiniteCapture](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/RingTheory/KrullDimension/FiniteCapture.lean).

**Module topology on finite-dimensional strong duals.** Over any normed
field, the continuous dual of a finite-dimensional topological vector space
with module topology also has module topology, retaining its topology of
uniform convergence on bounded sets. Neither completeness nor a nontrivial
norm on the field is required. This is an explicit theorem, not a global
instance. See [StrongDual](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Topology/StrongDual.lean).

**Flat-coefficient tensor monomorphisms.** Over a commutative ring with a
supplied topology, tensoring the topological module factor with a flat
algebraic coefficient module preserves injectivity of continuous linear
maps and categorical monomorphisms. No coefficient topology is required.
See [TensorFunctor](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Topology/TensorFunctor.lean).

**Coefficient tensor–continuous Hom adjunction.** For a commutative ring
with a supplied topology and a topological module with jointly continuous
scalar action, coefficient tensor is left adjoint to the algebraic
continuous-Hom functor, in a common carrier universe independent of the
scalar universe. It preserves existing colimits of arbitrary diagram size;
neither coefficients nor the Hom module are given a topology. See
[CoefficientTensor](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Topology/CoefficientTensor.lean).

**Continuous tensor quotients.** For a commutative ring `R` with a supplied
topology, an algebraic coefficient module `C`, a topological module `M` with
jointly continuous scalar action and any submodule `P`, there is a continuous
linear equivalence `C ⊗[R] (M ⧸ P) ≃L[R] (C ⊗[R] M) ⧸ K`, where
`K = LinearMap.range (TensorProduct.map LinearMap.id P.subtype)`.
This is the range, not its closure; no flatness or closedness assumption is
required. See [Quotient](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Topology/TensorProduct/Quotient.lean).

**Projective coefficients preserve tensor Hausdorffness.** Over a
commutative ring with a supplied topology, the one-sided tensor of a
projective algebraic coefficient module with a Hausdorff topological module
with jointly continuous scalar action is Hausdorff. No coefficient topology
or finiteness assumption is required. See
[TensorSeparation](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimits/Topology/TensorSeparation.lean).

**Flat coefficients need not preserve tensor Hausdorffness.** The one-sided
tensor `ℚ ⊗[ℤ] AddCircle (1 : ℝ)` is not Hausdorff, although the rational
coefficient module is flat and the usual real circle is compact Hausdorff
with jointly continuous integer action. See the
[rational-circle counterexample](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/AlgebraicDirectLimitsExamples/TensorCircleClient.lean).

For further results and characteristic formulas, see the
[guide's headline results](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/GUIDE.md#headline-results) and the
[coefficient tensor–Hom naturality guide](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/docs/coefficient-tensor-hom-naturality.md).
