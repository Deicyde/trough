# Algebraic direct limits

> Reusable Lean results for constant identity function and ring-homomorphism systems, varying-scalar directed limits, tensor products, countably cofinal inverse systems, simple filtered ring colimits, prime spectra of filtered commutative-ring colimits, Krull dimension under finite-subset capture, for directed colimits and for directed subsemiring unions, localization of countable products, cofinal group completions, monoidal-category object classes with actual-image cofinality, same-topology scalar restriction, linear continuity for coinduced topological modules, module topology under continuous linear injections into semisimple modules, module topology on finite-dimensional strong duals without complete scalars, continuous finite-basis coordinates and binary-product distribution for one-sided tensor products, continuous tensor universal properties, continuous dual tensor contraction and its finite-left equivalence with bounded-convergence Hom spaces, the scalar tensor unit, continuous associativity with whole continuous lift/curry compatibility, compactness for finitely generated tensor coefficients, noncompactness with infinite free coefficients, discreteness for tensors with a discrete right factor, arbitrary-basis and projective tensor Hausdorffness preservation, scalar extension by discrete coefficient algebras with separate base-linear and coefficient-linear views, a continuous unit and functorial continuous maps, and a rational-circle counterexample to flat-coefficient tensor Hausdorff preservation, with an algebraic quotient detector and dense rational-angle tensor-vanishing laws. The coefficient tensor–continuous Hom adjunction preserves existing colimits.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/formalization.yaml) of [FormalFrontier/algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits) at commit [e5d0dea1](https://github.com/FormalFrontier/algebraic-direct-limits/tree/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 16 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits), read at commit [e5d0dea1](https://github.com/FormalFrontier/algebraic-direct-limits/tree/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “unchecked”
- Review notes: “Independent agent reviews cover the existing direct-limit contributions, including the prime-spectrum comparison, the coinduced-module continuity criterion and the one-sided tensor-topology continuity and map API. Tensor universal-property and scalar-unit constructions have characteristic algebraic bridges, uniqueness and naturality laws, with integer-pair and boundary examples. Scalar restriction has characteristic action and forgetful agreements, natural identity and composition comparisons, and a semiring regular-action continuity criterion with Algebra agreement. Discrete scalar extension retains separate scalar views and has characteristic action, map, unit and underlying-module comparisons, with matrix/countable- product and same-ring swapping rank-one clients. The two complementary tensor-Hom naturality laws and nine example conclusions are included. This does not assert source-author endorsement or complete formal coverage of a source. API documentation is partial; see docs/CREDITS.md and docs/README.md.”
- Automation: agent; framework “Codex CLI and Formal Frontier agent workflows”; tool setup “Pinned Lean 4, mathlib, Lake, and Git”
- Automation notes: “AI-assisted Formal Frontier agents developed and assembled this library. A complete list of models used in earlier contributions is unavailable. Independent review is distinct from authorship.”

## Scope

A continuous injective linear map into a semisimple module with module topology gives the original source its module topology and is an embedding. The scalar ring has an arbitrary topology; the monoid source has continuous addition and scalar action, and the target is an additive group. Scalar and carrier universes are independent. Semisimple-ring corollaries retain both additive monoids and include division rings; real-axis and zero-dimensional applications are included. IsModuleTopology.strongDual gives the module topology on the existing bounded-convergence continuous dual of a finite-dimensional topological vector space with the module topology over a normed field, without a norm on the original space, complete scalars or a nontrivial-norm assumption. Rational-plane and dimension-zero applications and complete-field agreement are included. Tensor functoriality in both algebraic coefficients and topological right modules has standard curried, uncurried and flipped presentations, independent scalar and carrier universes and a weighted integer example with a nonzero image detected as six. The coefficient-tensor API includes characteristic identities for concrete Hom, tensor maps, currying, and naturality in algebraic coefficients and continuous targets. The rational-circle library modules are separate imports, reached by the circle clients rather than the public re-export. The examples cover prime spectra, finite-capture, directed-colimit and directed-union dimensions including proper subsemiring traces, coinduced modules, integer-pair tensors, tensor-Hom, the scalar unit, scalar restriction, discrete scalar extension, tensor separation and binary-product distribution with infinite integer coefficients and usual real right factors, infinite-basis and nonfree projective coefficients, tensor associativity with nonfree torsion and empty coefficients, continuous lift/curry compatibility with mixed coordinate detectors, infinite integer coefficients and usual real factors, and nonfree first-axis ideal coefficients, finite torsion tensor compactness, noncompact tensors with infinite free coefficients and a compact Hausdorff right factor, and rational coefficients with the usual real circle. The rational-circle model uses the algebraic integer module of rational numbers, flat by Mathlib's localization theorem, and the compact Hausdorff circle of period one with its jointly continuous integer action. The canonical one-sided tensor has continuous fixed-coefficient generators. Its integer-linear detector has the purely algebraic target of real numbers modulo the rational span of one and detects the nonzero pure tensor with coefficient one and circle class of the square root of two. All rational angles are dense in the usual circle, each has its positive denominator as an integer annihilator, and every rational coefficient tensored with any rational angle is zero. Integer balancing divides only the rational coefficient. The half-angle is nonzero in the circle but is killed by the generator at one; a twelve-conjunct theorem combines the fixed model's supporting properties without additional hypotheses. The circle tensor is not Hausdorff: otherwise the continuous generator at one and the zero map would agree everywhere by equality on dense rational angles, contradicting its nonzero value at the square root of two. This refutes Hausdorff preservation for flat coefficients even with a compact Hausdorff right factor and jointly continuous integer action. No rational action on the circle or topology or continuity for the detector target is asserted. Scalar restriction along a continuous ring homomorphism between arbitrary rings retains each topological module's topology, with functorial continuous-linear maps, natural identity/composition comparisons and both forgetful agreements. Carrier universes for continuous-linear maps are independent. Separately, over arbitrary semirings with supplied topologies, continuity of the scalar map is equivalent to joint continuity of its restricted regular action when target multiplication is continuous. The algebra-map multiplication formula agrees with Algebra scalar multiplication for any supplied topologies. A linear map out of the existing coinduced topological module is continuous exactly when all generating composites are continuous, over any ring with a supplied topology and with an independently leveled target. The one-sided tensor topology is constructed from fixed-coefficient generators, with their characteristic linear continuity criterion, canonical continuous tensor maps and continuous finite-basis coordinates with the product topology and finite-sum inverse. The tensor maps obey whole-map zero, addition, scalar and finite-sum laws in each variable. Infinite-rank integer coefficient projections on the usual real right module give distinct nonzero supported outputs and unequal-weight detectors. Continuous linear maps out of the tensor correspond to algebraic linear families of continuous linear maps on the right factor, with explicit lift/curry constructions and naturality. Two complementary whole-map naturality laws describe lift after both-input precomposition and curry after outgoing postcomposition, with six whole-map and three variable mixed-value example conclusions. Their input maps use complete existing constructors; three tuples retain existing nonzero, distinct, nonfinite, nondiscrete and nonfree control proof values. The lift-precomposition statement is the continuous representation of Mathlib's algebraic lift_comp_map law for the canonical one-sided topology. The scalar tensor unit equips Mathlib's algebraic left identity with continuity and the generator at one as inverse. Both constructions allow independent carrier universes over a commutative ring with a supplied topology and jointly continuous right-factor actions, without a topology on the coefficients or a finiteness hypothesis. Scalar tensor-unit examples on the usual reals give all-input action, two-way inverse recovery, a nonzero tensor at one, path-connectedness and nondiscreteness. They use the existing module, topology and jointly continuous integer action. The binary-product tensor equivalence distributes an algebraic coefficient module over two topological right factors, using their ordinary product topology over a commutative ring with a supplied topology. Its underlying equivalence is Mathlib's algebraic product equivalence; projection, inclusion, inverse reconstruction and naturality laws retain independent carrier universes without a finiteness or separation hypothesis. For a discrete right topological module, the scalar action on the algebraic tensor is jointly continuous at bottom topology, and the canonical one-sided tensor topology is discrete. The commutative ring has a supplied topology; scalar, coefficient and right-factor universes are independent. Neither discrete scalars nor a topology, finite generation, freeness or projectivity of the coefficient module is required. The examples retain mod-two integer coefficients that are not finitely generated, and the usual nondiscrete product ring of integers and reals, acting jointly on a discrete integer module through its first projection. Algebraic unitors detect nonzero, distinct and mixed tensors; continuity of those unitors is not asserted. The continuous dual tensor contraction maps the existing one-sided tensor of the algebraic coefficient module StrongDual κ E and G into bounded-convergence continuous linear maps E to G. The scalar field is nontrivially normed; E only has an additive group, a module structure and a topology, while G has continuous addition and jointly continuous scalar action. Scalar and carrier universes are independent. The rank-one formula and agreement with Mathlib's algebraic dualTensorHom hold without finiteness, completeness, separation or norms on the modules, and without continuity of the operations on E. When E is additionally finite-dimensional with its module topology, the same forward contraction is a continuous linear equivalence, with finite-basis inverse given by coordinate forms tensored with operator values. No further hypothesis on G is needed. Examples reconstruct an independently constructed real two-to-three operator from its column tensor, recover the tensor by the continuous inverse, evaluate the operator to a nonzero vector, and give the forward and inverse zero-dimensional left-source boundary for arbitrary topological right modules. The algebraic associator becomes a continuous linear equivalence between the supplied one-sided tensor topologies, with pure-tensor formulas, inverse identities, threefold extensionality and naturality in all three factors, without finiteness, freeness or separation assumptions. The flat continuous lift of any two-coefficient linear family agrees with its iterated lift after the canonical associator, and currying after reassociation is the algebraic lift of the twice-curried family. These whole map and family identities retain five independent carrier universes over a commutative ring with a supplied topology and jointly continuous right and target scalar actions, without a topology on coefficients or Hom modules. Mixed coordinate clients distinguish nonzero functionals and lifts and preserve boundary property values for infinite integer coefficients with usual real factors and nonfree first-axis ideal coefficients. Basis change remains a type contract without a proof or an exported construction of its realization. The arbitrary product-coordinate map is constructed from the continuous tensor lift and Pi construction. Its characteristic lemmas describe pure tensors and generators, support forgetting from algebraic Finsupp coordinates, injectivity and finite-coordinate agreement. The coordinate equivalences and finite-sum inverses remain finite-only. An arbitrary supplied coefficient basis or projective coefficient module preserves Hausdorffness of the right topological module. The projective case uses a section of the canonical free cover and the induced continuous split tensor maps. These results retain independent carrier and index universes over a commutative ring with a supplied topology and a jointly continuous right action, without a coefficient topology, continuity of ring multiplication, scalar separation, a field, Small or finite-generation hypotheses. Separation examples retain the nonfree right integer module ZMod 3, nonzero pure and mixed tensors, right doubling, the noncompact integer right factor, empty-basis and trivial-ring boundaries and nonreflection. Further examples construct the canonical infinite Finsupp integer coefficients with usual nondiscrete real right module, and the nonfree projective first-axis ideal over the discrete integer product ring, including model properties and explicit disjoint open pullbacks. These are forward Hausdorff preservation results; no Hausdorffness reflection or infinite-product surjectivity is asserted. Scalar extension by a discrete, possibly noncommutative coefficient algebra has separate base-linear and coefficient-linear views with the same primitive tensor topology. Fixed-coefficient continuity gives a jointly continuous coefficient action, a continuous base-linear unit and functorial coefficient-linear maps. For commutative coefficients the underlying module is naturally isomorphic to Mathlib's algebraic scalar extension. Matrix/countable-product examples have nonzero tensors, a tensor moved by extended doubling and an order-sensitive scalar action. A rank-one example uses the same scalar ring for base and coefficients, a swapping nonidentity algebra map, and a separately bundled regular input. Its coefficient-linear comparison detects a nonzero unit, differing base and coefficient scalar actions, and a nonzero nonidentity extended projection. Tensoring a compact topological module with a finitely generated algebraic coefficient module preserves compactness, over a commutative ring with a supplied topology and independent carrier universes. A finite spanning family gives a continuous surjection from a finite power of the right factor. This requires Module.Finite R C, not projectivity alone; neither coefficient freeness nor compactness of the scalar ring is required. The nonfree integer-module example uses ZMod 3 and multiplication to detect a nonzero pure tensor and instantiates this compactness result. Finite generation cannot in general be omitted, even for free/projective coefficients and a nontrivial compact Hausdorff right factor. Over R = ZMod 2, the algebraic coefficient module C = ℕ →₀ R is countably free and projective but not finitely generated. The discrete right self-module M = R is nontrivial, compact and Hausdorff, yet [TensorNoncompactness.not_compactSpace_tensor](AlgebraicDirectLimitsExamples/TensorNoncompactness.lean) shows that their one-sided tensor is not compact. The right unitor gives a homeomorphism with an infinite discrete comparison module D retaining C's algebraic module and action, not a coefficient-topology input. Compactness would make D finite, contradicting the injection from ℕ given by basis tensors. Finite-subset capture in one homomorphism range per finite subset bounds the Krull dimension of a commutative semiring by the supremum of the source dimensions, without injectivity or a directed-system assumption. The dimension values include bottom and top; subsemirings generated by finite subsets give a specialization. Under the same finite-subset capture hypothesis, the dimension of a target subsemiring is bounded by the supremum of the dimensions of its preimages in the stages. Finite-variable polynomial examples establish this hypothesis without any one stage surjecting onto the target or its proper even-variable subsemiring. Constant families with identity transition functions satisfy Mathlib's DirectedSystem laws over arbitrary preorders, with independent index and carrier universes and no directedness or nonemptiness assumption. The constant identity ring-homomorphism system specializes this same law witness for any nonassociative semiring, using Mathlib's identity-coercion API. The topology test client retains linear-continuity, tensor-map, finite-coordinate, basis-change and preservation type contracts without asserting proofs of the remaining realizations. The dimension of a directed colimit of commutative semirings over a nonempty directed preorder is bounded by the supremum of stage dimensions, without injective transitions and with independent index and stage universes. The dimension of the supremum of a nonempty inclusion-directed family of subsemirings of a commutative semiring is bounded by the supremum of stage dimensions. The index carries no order and has a universe independent of the ambient semiring; Noetherianity, domain, nontriviality and finite dimension are not required. A proper integer-to-rational family has stage-dimension supremum one and union dimension zero, so the bound need not be an equality. An empty-index example shows why nonemptiness is needed. Filtered commutative-ring colimits give limits of prime spectra in topological spaces, without injective transition maps or separation hypotheses. Monoidal group completion uses the skeleton and its actual image, with cofinal denominators, stabilization and an injective induced map under full faithfulness. Graded normalization is a type equivalence, not an additive equivalence; cancellation is required only for the degree target in its surjective/equivalence results. This is not a full theory or a source-coverage assessment. Full categorical tensor coherence, a pentagon construction and completed tensor products are outside this API. The underlying linear equivalence of TopModuleCat.tensorProdLeft is Mathlib's TensorProduct.prodLeft, without a topology on the coefficients. Its two continuity fields, all characteristic and naturality laws, and all coefficient-product client laws describe the projection product and inclusion coproduct, with characteristic formulas and naturality in both coefficient maps and the continuous right-factor map.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/algebraic-direct-limits/blob/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c/formalization.yaml) of [FormalFrontier/algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits) at commit [e5d0dea1](https://github.com/FormalFrontier/algebraic-direct-limits/tree/e5d0dea1697c85da3aefbe23ec33c4da2d138a6c), Apache-2.0.*

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
