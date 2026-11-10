# Homological algebra

> Finite Euler sums for chain and cochain complexes, with native exact-sequence, exact-functor and shift results, plus fixed-arrow relative paths of integer cochain maps in preadditive categories with binary biproducts and pullbacks, and an independent chosen-cokernel quotient-intersection pairing in abelian categories. It also constructs native quadrant bicomplex product totals over arbitrary rings and proves all-integer-degree acyclicity when every horizontal row is acyclic, including exactness at horizontal degree p=0 in each row. Includes admissible layers of chosen quotients, a reversed-lower/forward-upper order, and a lower-cut left-adjoint reflector under subobject/product closure and P(cokernel D.arrow), without quotient closure or endpoint admissibility. Also supplies the two exterior snake-sequence maps and proves the four middle exactness positions for an eight-object sequence in abelian categories; the endpoint universal properties and all six interior exactness positions hold without vanishing of the exterior objects. Also gives the canonical Fitting decomposition for endomorphisms of Noetherian and Artinian objects in arbitrary abelian categories, with kernel nilpotence, image invertibility and module-subobject agreement. These decompositions are natural for arbitrary intertwiners on a common tail; the copairing square at each exponent requires only the indicated kernels, images, image map and two biproducts. In a category with zero morphisms, nilpotent-to-monomorphic and epimorphic-to-nilpotent intertwiners vanish. For indecomposable Noetherian and Artinian objects, every endomorphism is nilpotent or a unit and the canonical, possibly noncommutative endomorphism ring is local. In any preadditive category with binary biproducts, locality of the canonical endomorphism ring implies indecomposability, without chain conditions or a chosen zero object. Separately, either an Artinian or a Noetherian object in a category with zero morphisms and finite biproducts admits a finite indecomposable biproduct decomposition, with an empty family for zero. In an abelian category, an object satisfying both chain conditions admits a finite biproduct decomposition with local canonical endomorphism rings on all factors. Such an object cancels from binary biproducts with arbitrary remaining objects. Finite families with local canonical endomorphism rings and isomorphic biproducts have matching factors, assuming only those two biproducts in a preadditive category. Every endomorphism of a Noetherian and Artinian object in an abelian category has a canonical Drazin inverse, with characteristic equations, unique existence, nilpotent, isomorphism and idempotent comparisons, and an idempotent projector. The kernel and image subobjects of sufficiently high powers equal those of f * drazinInverse f, and f * (1 - f * drazinInverse f) is nilpotent.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/formalization.yaml) of [FormalFrontier/homological-algebra](https://github.com/FormalFrontier/homological-algebra) at commit [8bcaebe9](https://github.com/FormalFrontier/homological-algebra/tree/8bcaebe913c50e1c09e347333d21093646101018), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 24 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/homological-algebra](https://github.com/FormalFrontier/homological-algebra), read at commit [8bcaebe9](https://github.com/FormalFrontier/homological-algebra/tree/8bcaebe913c50e1c09e347333d21093646101018) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other: theorem statements have complete proofs”.
- Automation: agent; framework “Codex and Hive”; prompting notes “AI-assisted mathematical exposition, Lean formalization and documentation with interactive Lean feedback; Codex and Hive supported the work.”
- Automation notes: “Project-wide inference cost, elapsed time and peak memory are not measured.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *The K-book*, Charles A. Weibel, Chapter II, Section 6 (additive functions and Euler characteristics) (book; adapts).
- *Cohomology of Number Fields*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Corrected second edition, (1.3.1) (book; adapts).
- *Original proof exposition for SES-additive Euler invariants*, Formal Frontier Agents (original-proof; adapts).
- *Original fixed-arrow cochain relative-path exposition and Lean implementation*, Formal Frontier Agents (original-proof; adapts).
- *Original chosen-cokernel quotient-intersection construction and Lean implementation*, Formal Frontier Agents (original-proof; adapts).
- *Original quadrant product-total assembly and Lean implementation*, Formal Frontier Agents (original-proof; adapts).
- *Original admissible-layer lower-cut reflector and Lean construction*, Formal Frontier Agents (original-proof; adapts).

## Builds on

- [Stable range](../../ring-theory/stable-range/README.md) (a Lake dependency, pinned at 70231e01)

## Used by

- [Coherent modules](../../commutative-algebra/coherent-modules/README.md)
- [Group theory](../../group-theory/group-theory/README.md)
- [Projective modules](../../ring-theory/projective-modules/README.md)
- [Scheme properties](../../algebraic-geometry/scheme-properties/README.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/README.md#headline-results) of [FormalFrontier/homological-algebra](https://github.com/FormalFrontier/homological-algebra) at commit [8bcaebe9](https://github.com/FormalFrontier/homological-algebra/tree/8bcaebe913c50e1c09e347333d21093646101018), Apache-2.0.*

**Uniqueness of finite biproduct factors.** In a preadditive category, two
finite families with local canonical, possibly noncommutative endomorphism
rings and isomorphic biproducts have equivalent index types and matching
isomorphic factors. Only the two given biproducts are needed, with independent
object, morphism and both index universes; no abelian structure, chain
conditions or idempotent completeness is assumed. Repeated factors are allowed;
the matching need not be unique or make the supplied isomorphism diagonal.
[Statement and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#uniqueness-of-finite-biproduct-factors).

**Finite indecomposable decompositions.** An Artinian object, or separately
a Noetherian object, in a category with zero morphisms and finite biproducts
is isomorphic to a finite biproduct of nonzero indecomposables; zero has the
empty decomposition. No preadditivity, abelian structure, second chain condition or
idempotent completeness is needed; this is existence, not uniqueness.
[Statements and modules](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#finite-indecomposable-decompositions).

**Finite-length decompositions with local endomorphism rings.** A Noetherian
**and** Artinian object in any abelian category is isomorphic to a finite
biproduct with local canonical, possibly noncommutative endomorphism rings
on its factors. Object and morphism universes are independent; zero has the
empty decomposition. This asserts existence and locality, not uniqueness.
Its local-End factors also satisfy the generic uniqueness theorem above.
[Statement and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#finite-length-decompositions-with-local-endomorphism-rings).

**Cancellation of finite local-End families.** In a preadditive category,
a finite biproduct of objects with local canonical, possibly noncommutative
endomorphism rings cancels from binary biproducts with arbitrary remaining
objects. Only the common full sum and the two binary totals are required;
no intermediate sums, chain conditions or idempotent completeness are assumed.
The object, morphism and index universes are independent, and the empty family
is allowed. The residual isomorphism is not canonical.
[Statement and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#cancellation-of-finite-local-end-families).

**Cancellation of finite-length summands.** In any abelian category, if
`X` is Noetherian **and** Artinian, `X ⊞ Y ≅ X ⊞ Z` implies
`Nonempty (Y ≅ Z)` for unrestricted `Y, Z`. No locality of `End X`
is required; zero is allowed and the isomorphism is not canonical.
[Statement and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#cancellation-of-finite-length-summands).

**Subobject correspondence and modularity.** Canonical subobject lattices
in any abelian category are modular. Pullback along an epimorphism identifies
codomain subobjects with domain subobjects containing its kernel, with direct
image as inverse; the cokernel case is included. No smallness is assumed.
[Statements and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#subobject-correspondence-and-modularity).

**Composition series and Jordan–Hölder.** A Noetherian **and** Artinian
object in any abelian category has a finite composition series from `⊥`
to `⊤` with simple quotient factors. Any two given series with equal heads
and lasts have equal lengths and isomorphic factors after a bijection,
without chain conditions or bottom/top assumptions for uniqueness.
[Statements and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#composition-series-and-jordanhölder).

**Categorical object length.** In any category, `objectLength X : ℕ∞`
measures strict steps in the canonical subobject order and is invariant under
isomorphisms and monotone under monomorphisms. In an abelian category it is
additive on every short exact sequence, including infinite lengths, and is
finite exactly for Noetherian **and** Artinian objects. Full composition
series compute it; over any ring it agrees with `Module.length`, with
independent scalar and carrier universes.
[Statements and modules](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#categorical-object-length).

**Fitting decomposition and intertwiners.** For an endomorphism of a
Noetherian **and** Artinian object in any abelian category, all sufficiently
high powers have complementary kernels and images, with canonical copairing
an isomorphism. The original endomorphism has a nilpotent restriction to the
kernel and an invertible restriction to the image, with a common-tail
block-intertwining equation. Arbitrary intertwiners between two such objects
are block diagonal in these canonical coordinates on one common tail.
Complementarity agrees with linear-map power kernels and ranges over
arbitrary, possibly noncommutative rings. Separately, generic block-intertwiner
and mixed-Hom vanishing laws need only zero morphisms and the displayed
biproducts, nilpotence and mono/epi conditions, not abelian structure.
[Statements and modules](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#fitting-decomposition).

**Canonical finite-length power bounds.** If `objectLength X ≠ ⊤`, put
`L = (objectLength X).toNat`. Power kernels stabilize by `L` with zero
morphisms and kernels; nilpotent endomorphisms satisfy `g ^ L = 0`.
Power images stabilize by `L` with images and image maps. On a Noetherian
**and** Artinian object in an abelian category, kernels and images of
`f ^ n` agree with those of the Drazin projector for every `n ≥ L`;
`f ^ (L + 1) * drazinInverse f = f ^ L` and
`(f * (1 - f * drazinInverse f)) ^ L = 0`. Zero length is included;
these are uniform mathematical bounds, not least exponents or runtime bounds.
Over any ring, a module of finite composition length `L` has
`ker (f ^ n) = ker (f ^ L)` for every endomorphism and every `n ≥ L`;
finite generation alone is not the hypothesis.
[Equations and hypotheses](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#canonical-finite-length-power-bounds).

**Canonical Drazin inverses.** Every endomorphism of a Noetherian **and**
Artinian object in an abelian category has a unique commuting Drazin inverse.
Its characteristic equations, nilpotent and idempotent cases, and
preservation by arbitrary multiplicative maps and functors are included.
For preservation both relevant objects must be Noetherian and Artinian;
functors need not be additive or exact. Intertwiners also intertwine the
inverses, and taking the inverse respects every natural power, including zero,
and products of commuting endomorphisms. Double inversion gives the group part
`f * drazinInverse f * f`, not generally `f`.
[Equations and hypotheses](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#canonical-drazin-inverses).

**Drazin sums, projectors and perturbations.** On a Noetherian **and**
Artinian object in an abelian category, mutually annihilating endomorphisms
in **both** product orders have additive Drazin inverses, also on finite
supports. A commuting nilpotent perturbation preserves the stable-image
projector and has an explicit finite geometric inverse formula; the Drazin
inverse itself generally changes. The projector has the stable power kernel
and image; `f * (1 - f * drazinInverse f)` is nilpotent, not necessarily
the complementary idempotent itself. These are conditional laws, not general
additivity or perturbation invariance of the inverse.
[Formulas and hypotheses](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#drazin-sums-projectors-and-perturbations).

**Cyclic and triangular Drazin formulas.** Between two Noetherian **and**
Artinian objects of an abelian category, arbitrary `a : X ⟶ Y`, `b : Y ⟶ X`
satisfy Cline's cyclic-product formula, with a canonical isomorphism between
the images of their Drazin projectors. For such `X, Y`, a unit `f : End X`,
nilpotent `g : End Y` with any witness `g ^ n = 0`, and arbitrary
`h : X ⟶ Y` give a finite-sum formula for the inverse of
`Biprod.ofComponents f h 0 g`; no intertwining condition on `h` is imposed.
The canonical image of its stable-image projector is isomorphic to `X`,
with the isomorphism's inverse given by a graph map.
The witness may be zero or nonminimal. Separately, cyclic powers need only
a category, and cyclic nilpotence only zero morphisms.
[Cyclic formulas](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#cyclic-products-and-projector-images),
[triangular formula](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#triangular-biproduct-formula).

**Sylvester equation and invariant graphs.** In any preadditive category,
invertible `f : X ⟶ X`, nilpotent `g : End Y` and arbitrary `h : X ⟶ Y`
give a unique `u : X ⟶ Y` with `f ≫ u = h + u ≫ g`. No biproducts,
scalar action or chain conditions are needed; object and morphism universes
are independent. Under the abelian, Noetherian **and** Artinian triangular
hypotheses above, this identifies the canonical graph slope, including its
factor of `f`, and the unique section of the first projection that intertwines
`f` with the triangular endomorphism.
[Equation and canonical graph](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#sylvester-equation-and-canonical-invariant-graph).

**Nilpotence in short complexes.** For a compatible endomorphism of a
short exact complex in any category with zero morphisms, the middle component
is nilpotent exactly when both outer components are. Exactness alone gives
the explicit middle exponent `m + n` from outer exponents `m, n`; a monic
first arrow and an epic second arrow reflect a middle exponent to the left
and right components, respectively, without changing it. All natural
exponents, including zero, are allowed; no abelian, additive, splitting or
chain-condition premise is needed.
[Statements and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#nilpotence-in-short-complexes).

**Local endomorphism rings.** An indecomposable Noetherian **and** Artinian
object in any abelian category has a local canonical, possibly noncommutative
endomorphism ring; every endomorphism is nilpotent or a unit.
Indecomposability excludes zero, with no extra nontriviality premise.
[Statements and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#local-endomorphism-rings).

**Indecomposability from locality.** In any preadditive category with binary
biproducts, a local canonical ring `End X` implies Mathlib's original
`Indecomposable X`. No abelian structure, chain conditions, chosen zero
object or separate nonzero hypothesis is required; the ring may be
noncommutative.
[Statement and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#indecomposability-from-locality).

**Finite Euler identities.** In an abelian category, an invariant valued in
any additive commutative group and additive on every native short exact
sequence gives finite integer-interval Euler identities for chains and
cochains with explicit endpoint-image corrections. Quasi-isomorphism
invariance requires both complexes to have term support in the same nonempty
interval; homology-sum SES additivity for chains requires this of all three
complexes. Cochain LES additivity instead has connecting-image corrections
removable by neighboring homology vanishing. Exact-functor transport,
finite-support and native-shift formulas, and length for finitely generated
modules over a commutative Noetherian Artinian ring are included.
[Formulas and hypotheses](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#finite-euler-identities),
[Euler guide](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/AdditiveEuler.md).

**Unrestricted Hom complexes and K-objects.** For integer cochains in any
preadditive category, the canonical Hom complex uses unrestricted products
of **abelian groups**, not products in the coefficient category. Homotopies
act in both variables; a contraction in either contracts the Hom complex,
and degree-`n` cohomology vanishes exactly when every map `K ⟶ L⟦n⟧` is
null-homotopic. In an **abelian** category, K-projectivity and K-injectivity
are characterized by acyclicity of Hom complexes against acyclic tests,
even by vanishing in one fixed degree. They descend along one-sided homotopy
retracts, are invariant under categorical equivalences, and are detected
componentwise on supplied coproducts and products, respectively, including
empty families. Hom-complex quasi-isomorphism criteria, diagonal homotopy
criteria with evaluation-preservation hypotheses, and canonical preimages
of supplied homotopy equivalences under fully faithful additive functors
complement these results; no boundedness or enough-projectives/injectives
assumption is imposed.
[Detailed statements and modules](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#hom-complexes-and-k-objects),
[Hom-complex guide](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HomComplexHomotopy.md).

**Ordinary disks and bounded-below projective chains.** In a category with
zero morphisms and a zero object, an integer cochain identity disk in degrees
`n,n+1` is ordinarily projective or injective exactly when its coefficient is;
no preadditivity is required. Separately, in any abelian category, a
particular map between integer chain complexes with projective terms and
possibly different termwise lower bounds is a quasi-isomorphism exactly
when it is the forward map of a homotopy equivalence. There is no upper-bound
or enough-projectives assumption. Ordinary projectivity is distinct from
K-projectivity.
[Statements and modules](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#ordinary-disks-and-bounded-below-projective-chains).

**Chain conditions and homology.** A functor between arbitrary categories
preserving monomorphisms and reflecting isomorphisms reflects Noetherian and,
separately, Artinian objects, with four independent universes; fullness and
faithfulness are not required. In an abelian category, a short complex with
Noetherian middle object has Noetherian homology. Epimorphic Noetherian and
monomorphic Artinian endomorphisms are isomorphisms. Both module criteria use
the original scalar action over any ring, with independent scalar and carrier
universes. No smallness, well-poweredness, Noetherian-ring or whole-category
chain condition is assumed. In an abelian category, binary biproducts
preserve each chain condition separately from that condition on both factors.
[Statements and modules](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#noetherian-objects).

**Quotients, admissible layers and snake sequences.** In any abelian
category, for subobjects `L ≤ U` of `B` and any `D`, the chosen-cokernel map
`U/(L ⊓ D) ⟶ (U/L) × (B/D)` is monic, without `L ≤ D`. Layers admissible
for a quotient property `P` have reversed lower and forward upper order;
subobject and binary-product closure and `P(B/D)` make the lower cut
`(L,U) ↦ (L ⊓ D,U)` **left** adjoint to inclusion of layers with lower
endpoint at most `D`. Separately, snake inputs with exact rows, epic upper
second arrow and monic lower first arrow give an eight-object sequence exact
at all six interior objects.
Neither exterior object is required to vanish; the four middle exactness
positions use Mathlib's snake lemma.
[Statements and modules](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#quotients-admissible-layers-and-snake-sequences),
[quotient guide](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/QuotientIntersection.md), [layer guide](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/AdmissibleLayers.md).

**Fixed-arrow relative paths.** For integer cochains in a preadditive
category with binary biproducts and **pullbacks**, the pullback of a fixed
`f : B₁ ⟶ B` along the first native path endpoint has a strict section,
lifts from chosen homotopies with strict endpoint equations, and a homotopy
equivalence to `B₁` whose inverse homotopy vanishes over the first projection.
The object depends only on `f`; no arbitrary-arrow naturality or new
quasi-isomorphism instance is asserted.
[Statement and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#fixed-arrow-relative-paths),
[relative-path guide](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/CochainRelativePath.md).

**Quadrant product totals.** For any ring `R`, native quadrant bicomplexes
in `ModuleCat.{u} R`, with `R : Type u`, have signed unrestricted product
totals in integer degrees `p-r`. Acyclic horizontal rows at **every** row
and horizontal degree, including the boundary `p=0`, imply total acyclicity
in **all integer degrees**. Chosen elementwise lifts are not linear or
natural splittings; this is not an arbitrary-unbounded total theorem.
[Statement and module](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md#quadrant-product-totals),
[product-total guide](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/ProductTotalAcyclicity.md).

The [complete headline catalogue](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/docs/HeadlineResults.md) retains the individual
results, signs, universe parameters and qualifications. In particular, object
and morphism universes are independent in the general categorical results;
index universes are independent in the family-limit results.

## Main results

Its formalization.yaml lists 220 main results, and the scan finds 218 of them declared in the file the yaml gives; they are on their own page, not made articles. The scan does not find `CategoryTheory.End.drazinInverse_comp_eq_comp_drazinInverse_assoc` ([HomologicalAlgebra/Abelian/Drazin.lean](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean)), `CategoryTheory.Subobject.quotientIntersectionPair_fac_assoc` ([HomologicalAlgebra/Abelian/QuotientIntersection.lean](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/QuotientIntersection.lean)).

- [Main results](main-results/README.md)
