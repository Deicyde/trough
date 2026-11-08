# Homological algebra

> Finite Euler sums for chain and cochain complexes, with native exact-sequence, exact-functor and shift results, plus fixed-arrow relative paths of integer cochain maps in preadditive categories with binary biproducts and pullbacks, and an independent chosen-cokernel quotient-intersection pairing in abelian categories. It also constructs native quadrant bicomplex product totals over arbitrary rings and proves all-integer-degree acyclicity when every horizontal row is acyclic, including exactness at horizontal degree p=0 in each row. Includes admissible layers of chosen quotients, a reversed-lower/forward-upper order, and a lower-cut left-adjoint reflector under subobject/product closure and P(cokernel D.arrow), without quotient closure or endpoint admissibility. Also supplies the two exterior snake-sequence maps and proves the four middle exactness positions for an eight-object sequence in abelian categories; the endpoint universal properties and all six interior exactness positions hold without vanishing of the exterior objects. Also gives the canonical Fitting decomposition for endomorphisms of Noetherian and Artinian objects in arbitrary abelian categories, with kernel nilpotence, image invertibility and module-subobject agreement. These decompositions are natural for arbitrary intertwiners on a common tail; the copairing square at each exponent requires only the indicated kernels, images, image map and two biproducts. In a category with zero morphisms, nilpotent-to-monomorphic and epimorphic-to-nilpotent intertwiners vanish. For indecomposable Noetherian and Artinian objects, every endomorphism is nilpotent or a unit and the canonical, possibly noncommutative endomorphism ring is local. In any preadditive category with binary biproducts, locality of the canonical endomorphism ring implies indecomposability, without chain conditions or a chosen zero object. Separately, either an Artinian or a Noetherian object in a category with zero morphisms and finite biproducts admits a finite indecomposable biproduct decomposition, with an empty family for zero. In an abelian category, an object satisfying both chain conditions admits a finite biproduct decomposition with local canonical endomorphism rings on all factors. Such an object cancels from binary biproducts with arbitrary remaining objects. Finite families with local canonical endomorphism rings and isomorphic biproducts have matching factors, assuming only those two biproducts in a preadditive category. Every endomorphism of a Noetherian and Artinian object in an abelian category has a canonical Drazin inverse, with characteristic equations, unique existence, nilpotent, isomorphism and idempotent comparisons, and an idempotent projector. The kernel and image subobjects of sufficiently high powers equal those of f * drazinInverse f, and f * (1 - f * drazinInverse f) is nilpotent.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/formalization.yaml) of [FormalFrontier/homological-algebra](https://github.com/FormalFrontier/homological-algebra) at commit [8bcaebe9](https://github.com/FormalFrontier/homological-algebra/tree/8bcaebe913c50e1c09e347333d21093646101018), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 24 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/homological-algebra](https://github.com/FormalFrontier/homological-algebra), read at commit [8bcaebe9](https://github.com/FormalFrontier/homological-algebra/tree/8bcaebe913c50e1c09e347333d21093646101018) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other: theorem statements have complete proofs”
- Automation: agent; framework “Codex and Hive”
- Automation notes: “Project-wide inference cost, elapsed time and peak memory are not measured.”

## Scope

SES-additive finite-interval chain and cochain Euler identities with both endpoint-image corrections, neighbor-vanishing and term-bounded corollaries, acyclic zero and quasi-isomorphism invariance when both complexes share a term-support bound; finite-length module instance for commutative Noetherian Artinian rings; degreewise-SES signed term and bounded homology additivity; exact-functor transport and mapped homology comparison under finite-limit and finite-colimit preservation; finite-support invariance, native cochain shift by i+n with support shift -n, and negative-degree, torsion and identity-differential examples. The nonempty-interval cochain LES homology sum subtracts both connecting-image corrections and has outer-homology-vanishing and native IsGE/IsLE corollaries without a bound on the middle complex; its rational client is genuinely nonsplit. No empty-interval LES formula, canonical infinite/homology-only Euler invariant, general derived-category result or K0 presentation is claimed. For a fixed arrow, the integer cochain relative path uses preadditivity, binary biproducts and pullbacks and gives strict section/endpoints and chosen-homotopy lifts, with a relative contraction rather than a strict second inverse; the native-cylinder endpoint law requires no pullbacks. No arbitrary-arrow naturality or new quasi-isomorphism instance is claimed. The chosen quotient-intersection pair is monic in arbitrary abelian categories with independent universes for L ≤ U and arbitrary D; neither projection is asserted monic, nor is L ≤ D or quotient lifting assumed. Its property-transfer client uses subobject/product closure. Admissible layers reverse the lower order and have an inclusion requiring no closure and a lower-cut left adjoint, unit and exact reflector identity under subobject/product closure and P(cokernel D.arrow); no upper cut, ambient-D transport, Q-comma or filtration theorem is claimed. Product totals over any Ring use unrestricted diagonal products in degree p-r with horizontal plus signed vertical differential and zero vertical contribution at r=0; map laws need no exactness and acyclicity in every integer degree assumes every horizontal row acyclic including p=0. Chosen primitives are not linear/natural splittings and require no convergence or exact-products assumption. The nonsplit mod-two client repeats a nonzero row infinitely often overall but has zero vertical maps and only finitely many nonzero cells on each diagonal (at most three); it does not test infinitely supported diagonals or nonzero vertical maps. No source-coverage decision follows from these library results. For an arbitrary abelian category and ShortComplex.SnakeInput, the eight-object snake diagram has canonical endpoint maps with kernel and cokernel universal properties; its six interior positions are exact using the Mathlib middle six-term snake lemma. Its mod-three test has nonzero exterior objects and a positive connector different from its negative independently of the full-exactness theorem; the combined example uses that theorem. The Fitting results give eventual complementarity of canonical power kernels and images, the actual binary-biproduct copairing as an isomorphism, nilpotent kernel restriction and invertible image restriction on one common tail; object and morphism universes are independent in the categorical results, and the module bridges retain independent scalar and carrier universes. An arbitrary intertwiner f≫p=p≫g induces a natural square of the power-kernel/image copairings at every exponent, requiring only zero morphisms, the displayed kernels and images, the image map of that square and the two displayed biproducts. When X and Y are each Noetherian and Artinian in an abelian category, their canonical copairings are isomorphisms on one common tail and the coordinate expression of p is the binary biproduct map of its induced kernel and image maps. No monicity, epicity, invertibility or supplied splitting of p is assumed. Separately, in any category with zero morphisms, a morphism intertwining a nilpotent endomorphism with a monomorphic endomorphism is zero; dually, an epimorphic source endomorphism and nilpotent target endomorphism force that morphism to vanish. Object and morphism universes are independent. Categorical Artinianity agrees with module Artinianity under the canonical subobject–submodule order isomorphism. An indecomposable Noetherian and Artinian object has a local canonical endomorphism ring, and each endomorphism is nilpotent or a unit; no commutativity or extra nontriviality hypothesis is required. Conversely, in any preadditive category with binary biproducts, an object with a local canonical endomorphism ring satisfies Mathlib's original Indecomposable predicate. Object and morphism universes are independent; no abelian structure, Noetherianity, Artinianity, chosen zero object or extra nontriviality is assumed. Finite indecomposable decompositions require either one-sided object chain condition, zero morphisms and finite biproducts, with independent object and morphism universes; no preadditivity, abelianity, idempotent completeness or uniqueness is assumed. For an object satisfying both chain conditions in an abelian category, the finite decomposition has local canonical endomorphism rings on every factor, with independent object and morphism universes and the empty decomposition for zero; no commutativity or supplied decomposition is assumed. In any preadditive category, a finite biproduct of objects with local canonical, possibly noncommutative endomorphism rings cancels from binary biproducts with arbitrary remainders. Only the common full sum and the two binary totals are assumed to exist; no intermediate sums, abelian structure, chain conditions or idempotent completeness are required. Object, morphism and index universes are independent, the family may be empty, and no canonical residual isomorphism or residual-block invertibility is asserted. A Noetherian and Artinian object X cancels from X⊞Y≅X⊞Z, yielding Nonempty(Y≅Z) for arbitrary Y and Z. Neither remainder has a locality, chain-condition, finiteness or nonzero premise, and the endomorphism ring of X need not be local. Object and morphism universes remain independent, zero X is included, and no canonical isomorphism is selected. In a preadditive category, two given finite biproducts of factors with local canonical endomorphism rings have matching factors whenever their totals are isomorphic; the index equivalence need not be unique. Object, morphism and both index universes are independent, with no global biproduct or chain-condition assumption. With independent object and morphism universes in an abelian category, every endomorphism f of a fixed Noetherian and Artinian object X has a noncomputable value End.drazinInverse f in the original End X, where p * q = q ≫ p. It is the unique g satisfying Commute f g, g * f * g = g and an existential natural-number power equation f ^ (n + 1) * g = f ^ n. Only g is unique; exponent zero is allowed, and no Drazin index is selected. The value is zero iff f is nilpotent, agrees with CategoryTheory.inv f under IsIso f, fixes idempotents and gives IsIdempotentElem (f * End.drazinInverse f). Existence uses the kernel–image Fitting copairing and invertible image restriction at one common positive power, transported by Mathlib's Iso.conj. No nonzero-object, commutativity, smallness, scalar or supplied-decomposition hypothesis is required. For p = f * End.drazinInverse f, the canonical kernel and image subobjects of f ^ n eventually equal those of p, and f * (1 - p) is nilpotent. No threshold or positive index is supplied; positivity is derived internally, including the characteristic-exponent-zero case.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/formalization.yaml) of [FormalFrontier/homological-algebra](https://github.com/FormalFrontier/homological-algebra) at commit [8bcaebe9](https://github.com/FormalFrontier/homological-algebra/tree/8bcaebe913c50e1c09e347333d21093646101018), Apache-2.0.*

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

The 220 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `CategoryTheory.isNoetherianObject_biprod` | instance | [HomologicalAlgebra/Abelian/ChainConditions.lean, line 38](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/ChainConditions.lean#L38) |  |
| `CategoryTheory.isArtinianObject_biprod` | instance | [HomologicalAlgebra/Abelian/ChainConditions.lean, line 46](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/ChainConditions.lean#L46) |  |
| `CategoryTheory.Limits.biprod.isIso_map_iff` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 54](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L54) |  |
| `CategoryTheory.Limits.biprod.mapIso_asIso` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 108](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L108) |  |
| `CategoryTheory.End.biprod_inl_comp_snd_eq_zero` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 127](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L127) |  |
| `CategoryTheory.End.biprod_inr_comp_fst_eq_zero` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 142](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L142) |  |
| `CategoryTheory.End.biprod_intertwiner_eq_map` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 158](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L158) |  |
| `CategoryTheory.End.biprodLeftIso` | def | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 180](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L180) |  |
| `CategoryTheory.End.biprodRightIso` | def | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 199](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L199) |  |
| `CategoryTheory.End.biprodLeftIso_hom` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 218](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L218) |  |
| `CategoryTheory.End.biprodLeftIso_inv` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 255](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L255) |  |
| `CategoryTheory.End.biprodRightIso_hom` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 230](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L230) |  |
| `CategoryTheory.End.biprodRightIso_inv` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 272](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L272) |  |
| `CategoryTheory.End.biprod_mapIso_eq_asIso` | theorem | [HomologicalAlgebra/Abelian/BiproductIntertwiners.lean, line 241](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/BiproductIntertwiners.lean#L241) |  |
| `CategoryTheory.End.eq_zero_of_isNilpotent_of_mono` | theorem | [HomologicalAlgebra/Abelian/EndomorphismPowers.lean, line 104](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/EndomorphismPowers.lean#L104) |  |
| `CategoryTheory.End.eq_zero_of_epi_of_isNilpotent` | theorem | [HomologicalAlgebra/Abelian/EndomorphismPowers.lean, line 114](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/EndomorphismPowers.lean#L114) |  |
| `CategoryTheory.End.pow_biprod_desc_naturality` | theorem | [HomologicalAlgebra/Abelian/EndomorphismPowers.lean, line 126](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/EndomorphismPowers.lean#L126) |  |
| `CategoryTheory.End.comp_pow_succ` | theorem | [HomologicalAlgebra/Abelian/EndomorphismCyclicProducts.lean, line 41](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/EndomorphismCyclicProducts.lean#L41) |  |
| `CategoryTheory.End.comp_pow_comp_eq_mul_pow_mul` | theorem | [HomologicalAlgebra/Abelian/EndomorphismCyclicProducts.lean, line 52](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/EndomorphismCyclicProducts.lean#L52) |  |
| `CategoryTheory.End.isNilpotent_comp_iff` | theorem | [HomologicalAlgebra/Abelian/EndomorphismCyclicProducts.lean, line 60](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/EndomorphismCyclicProducts.lean#L60) |  |
| `CategoryTheory.End.eventually_exists_pow_biprod_desc_iso_naturality` | theorem | [HomologicalAlgebra/Abelian/FittingNaturality.lean, line 50](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/FittingNaturality.lean#L50) |  |
| `CategoryTheory.End.drazinInverse` | def | [HomologicalAlgebra/Abelian/Drazin.lean, line 203](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L203) |  |
| `CategoryTheory.End.commute_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 216](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L216) |  |
| `CategoryTheory.End.drazinInverse_mul_self_mul` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 221](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L221) |  |
| `CategoryTheory.End.drazinInverse_comp_self_comp` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 228](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L228) |  |
| `CategoryTheory.End.exists_pow_succ_mul_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 235](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L235) |  |
| `CategoryTheory.End.eq_drazinInverse_iff` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 242](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L242) |  |
| `CategoryTheory.End.existsUnique_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 258](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L258) |  |
| `CategoryTheory.End.drazinInverse_eq_zero_iff` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 269](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L269) |  |
| `CategoryTheory.End.drazinInverse_zero` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 286](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L286) |  |
| `CategoryTheory.End.drazinInverse_eq_inv` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 291](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L291) |  |
| `CategoryTheory.End.drazinInverse_of_isIdempotentElem` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 305](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L305) |  |
| `CategoryTheory.End.isIdempotentElem_mul_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 314](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L314) |  |
| `CategoryTheory.End.map_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 479](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L479) |  |
| `CategoryTheory.Functor.map_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 513](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L513) |  |
| `CategoryTheory.End.drazinInverse_comp_eq_comp_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 325](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L325) |  |
| `Commute.drazinInverse_left` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 378](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L378) |  |
| `CategoryTheory.End.drazinInverse_pow` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 388](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L388) |  |
| `Commute.drazinInverse_mul` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 411](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L411) |  |
| `CategoryTheory.End.drazinInverse_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/Drazin.lean, line 451](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean#L451) |  |
| `CategoryTheory.End.drazinInverse_add_of_mul_eq_zero` | theorem | [HomologicalAlgebra/Abelian/DrazinAdditivity.lean, line 49](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinAdditivity.lean#L49) |  |
| `CategoryTheory.End.drazinInverse_sum` | theorem | [HomologicalAlgebra/Abelian/DrazinAdditivity.lean, line 132](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinAdditivity.lean#L132) |  |
| `CategoryTheory.End.drazinInverse_comp` | theorem | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 57](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L57) |  |
| `CategoryTheory.End.mul_drazinInverse_comp` | theorem | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 75](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L75) |  |
| `CategoryTheory.End.imageMulDrazinInverseCompIso` | def | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 85](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L85) |  |
| `CategoryTheory.End.imageMulDrazinInverseCompIso_hom_ι` | theorem | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 147](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L147) |  |
| `CategoryTheory.End.imageMulDrazinInverseCompIso_inv_ι` | theorem | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 155](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L155) |  |
| `CategoryTheory.End.imageMulDrazinInverseCompIso_hom_eq_image_map` | theorem | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 164](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L164) |  |
| `CategoryTheory.End.imageMulDrazinInverseCompIso_inv_eq_image_map` | theorem | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 179](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L179) |  |
| `CategoryTheory.End.imageMulDrazinInverseCompIso_hom_naturality` | theorem | [HomologicalAlgebra/Abelian/DrazinCyclic.lean, line 201](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinCyclic.lean#L201) |  |
| `CategoryTheory.End.eventually_kernelSubobject_pow_eq_mul_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/DrazinProjector.lean, line 72](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinProjector.lean#L72) |  |
| `CategoryTheory.End.eventually_imageSubobject_pow_eq_mul_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/DrazinProjector.lean, line 85](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinProjector.lean#L85) |  |
| `CategoryTheory.End.isNilpotent_mul_one_sub_mul_drazinInverse` | theorem | [HomologicalAlgebra/Abelian/DrazinProjector.lean, line 98](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinProjector.lean#L98) |  |
| `CategoryTheory.End.drazinInverse_add_eq_sum_range` | theorem | [HomologicalAlgebra/Abelian/DrazinPerturbation.lean, line 165](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinPerturbation.lean#L165) |  |
| `CategoryTheory.End.add_mul_drazinInverse_of_isNilpotent` | theorem | [HomologicalAlgebra/Abelian/DrazinPerturbation.lean, line 196](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinPerturbation.lean#L196) |  |
| `CategoryTheory.existsUnique_sylvester` | theorem | [HomologicalAlgebra/Preadditive/Sylvester.lean, line 37](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Preadditive/Sylvester.lean#L37) |  |
| `CategoryTheory.End.eq_comp_inl_drazinInverse_biprod_triangular_snd_iff` | theorem | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 277](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L277) |  |
| `CategoryTheory.End.eq_imageMulDrazinInverseBiprodTriangularIso_inv_ι_iff` | theorem | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 322](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L322) |  |
| `CategoryTheory.End.drazinInverse_biprod_triangular` | theorem | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 74](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L74) |  |
| `CategoryTheory.End.mul_drazinInverse_biprod_triangular` | theorem | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 140](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L140) |  |
| `CategoryTheory.End.imageMulDrazinInverseBiprodTriangularIso` | def | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 183](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L183) |  |
| `CategoryTheory.End.imageMulDrazinInverseBiprodTriangularIso_hom` | theorem | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 211](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L211) |  |
| `CategoryTheory.End.imageMulDrazinInverseBiprodTriangularIso_inv_ι` | theorem | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 241](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L241) |  |
| `CategoryTheory.End.factorThruImage_comp_imageMulDrazinInverseBiprodTriangularIso_hom` | theorem | [HomologicalAlgebra/Abelian/DrazinTriangular.lean, line 261](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/DrazinTriangular.lean#L261) |  |
| `CategoryTheory.cancel_finite_biproduct_of_isLocalRing_end` | theorem | [HomologicalAlgebra/Preadditive/FiniteCancellation.lean, line 106](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Preadditive/FiniteCancellation.lean#L106) |  |
| `CategoryTheory.nonempty_iso_of_biprod_iso_of_isNoetherianObject_of_isArtinianObject` | theorem | [HomologicalAlgebra/Abelian/FiniteLengthCancellation.lean, line 46](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/FiniteLengthCancellation.lean#L46) |  |
| `CategoryTheory.exists_finite_biproduct_isLocalRing_end` | theorem | [HomologicalAlgebra/Abelian/FiniteLength.lean, line 48](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/FiniteLength.lean#L48) |  |
| `CategoryTheory.exists_equiv_of_iso_biproduct_of_isLocalRing_end` | theorem | [HomologicalAlgebra/Preadditive/BiproductUniqueness.lean, line 223](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Preadditive/BiproductUniqueness.lean#L223) |  |
| `CategoryTheory.exists_finite_indecomposable_biproduct_of_isArtinianObject` | theorem | [HomologicalAlgebra/Indecomposable/Artinian.lean, line 39](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Indecomposable/Artinian.lean#L39) |  |
| `CategoryTheory.exists_finite_indecomposable_biproduct_of_isNoetherianObject` | theorem | [HomologicalAlgebra/Indecomposable/Noetherian.lean, line 192](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Indecomposable/Noetherian.lean#L192) |  |
| `CategoryTheory.indecomposable_of_isLocalRing_end` | theorem | [HomologicalAlgebra/Preadditive/Indecomposable.lean, line 45](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Preadditive/Indecomposable.lean#L45) |  |
| `CategoryTheory.isLocalRing_end_of_indecomposable` | theorem | [HomologicalAlgebra/Abelian/LocalEndomorphism.lean, line 73](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/LocalEndomorphism.lean#L73) |  |
| `CategoryTheory.isNilpotent_or_isUnit_of_indecomposable` | theorem | [HomologicalAlgebra/Abelian/LocalEndomorphism.lean, line 50](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/LocalEndomorphism.lean#L50) |  |
| `ModuleCat.isArtinianObject_iff` | lemma | [HomologicalAlgebra/ModuleCat/Subobject.lean, line 36](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/ModuleCat/Subobject.lean#L36) |  |
| `CategoryTheory.eventually_isCompl_kernelSubobject_pow_imageSubobject_pow` | theorem | [HomologicalAlgebra/Abelian/Fitting.lean, line 245](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Fitting.lean#L245) |  |
| `CategoryTheory.eventually_isIso_biprod_desc_kernel_ι_image_ι_pow` | theorem | [HomologicalAlgebra/Abelian/Fitting.lean, line 255](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Fitting.lean#L255) |  |
| `CategoryTheory.End.eventually_isIso_imagePowRestriction` | theorem | [HomologicalAlgebra/Abelian/Fitting.lean, line 267](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Fitting.lean#L267) |  |
| `ModuleCat.isCompl_kernelSubobject_pow_imageSubobject_pow_iff` | lemma | [HomologicalAlgebra/ModuleCat/Subobject.lean, line 75](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/ModuleCat/Subobject.lean#L75) |  |
| `CochainComplex.HomComplex.isZero_homology_iff` | lemma | [HomologicalAlgebra/Cochain/HomComplexVanishing.lean, line 37](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/HomComplexVanishing.lean#L37) |  |
| `CochainComplex.HomComplex.acyclic_iff` | lemma | [HomologicalAlgebra/Cochain/HomComplexVanishing.lean, line 84](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/HomComplexVanishing.lean#L84) |  |
| `CochainComplex.HomComplex.quasiIso_prePostcomp_of_homotopyEquiv` | lemma | [HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean, line 69](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean#L69) |  |
| `CochainComplex.HomComplex.quasiIso_prePostcomp_of_isIso_quotient_map` | lemma | [HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean, line 107](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean#L107) |  |
| `CochainComplex.IsKProjective.quasiIso_prePostcomp` | lemma | [HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean, line 134](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean#L134) |  |
| `CochainComplex.IsKInjective.quasiIso_prePostcomp` | lemma | [HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean, line 208](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/HomComplexQuasiIso.lean#L208) |  |
| `CategoryTheory.ShortComplex.SnakeInput.composableArrowsWithEndpoints_middle_exact` | theorem | [HomologicalAlgebra/Abelian/SnakeLemma.lean, line 139](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/SnakeLemma.lean#L139) |  |
| `CategoryTheory.ShortComplex.SnakeInput.kernelToL₀X₁IsKernel` | def | [HomologicalAlgebra/Abelian/SnakeLemma.lean, line 57](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/SnakeLemma.lean#L57) |  |
| `CategoryTheory.ShortComplex.SnakeInput.L₃X₃ToCokernelIsCokernel` | def | [HomologicalAlgebra/Abelian/SnakeLemma.lean, line 94](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/SnakeLemma.lean#L94) |  |
| `CategoryTheory.ShortComplex.SnakeInput.snake_lemma_with_endpoints` | theorem | [HomologicalAlgebra/Abelian/SnakeLemma.lean, line 148](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/SnakeLemma.lean#L148) |  |
| `CategoryTheory.AdditiveEuler.euler_endpoints` | theorem | [HomologicalAlgebra/AdditiveEuler.lean, line 169](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler.lean#L169) |  |
| `CategoryTheory.AdditiveEuler.euler_eq_homology_of_bounded` | theorem | [HomologicalAlgebra/AdditiveEuler.lean, line 205](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler.lean#L205) |  |
| `CategoryTheory.AdditiveEuler.euler_quasiIso` | theorem | [HomologicalAlgebra/AdditiveEuler.lean, line 227](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler.lean#L227) |  |
| `CategoryTheory.AdditiveEuler.lengthInvariant_ses` | theorem | [HomologicalAlgebra/AdditiveEuler/Length.lean, line 39](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Length.lean#L39) |  |
| `CategoryTheory.AdditiveEuler.term_sum_additive_of_shortExact` | theorem | [HomologicalAlgebra/AdditiveEuler/Functoriality.lean, line 39](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Functoriality.lean#L39) |  |
| `CategoryTheory.AdditiveEuler.homology_sum_additive_of_shortExact` | theorem | [HomologicalAlgebra/AdditiveEuler/Functoriality.lean, line 53](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Functoriality.lean#L53) |  |
| `CategoryTheory.AdditiveEuler.mapHomologyIso` | def | [HomologicalAlgebra/AdditiveEuler/Functoriality.lean, line 99](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Functoriality.lean#L99) |  |
| `CategoryTheory.AdditiveEuler.euler_map_bounded` | theorem | [HomologicalAlgebra/AdditiveEuler/Functoriality.lean, line 132](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Functoriality.lean#L132) |  |
| `CategoryTheory.AdditiveEuler.signed_sum_eq_of_support` | theorem | [HomologicalAlgebra/AdditiveEuler/Shift.lean, line 35](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Shift.lean#L35) |  |
| `CategoryTheory.AdditiveEuler.signed_sum_translate` | theorem | [HomologicalAlgebra/AdditiveEuler/Shift.lean, line 55](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Shift.lean#L55) |  |
| `CategoryTheory.AdditiveEuler.term_sum_eq_of_support` | theorem | [HomologicalAlgebra/AdditiveEuler/Shift.lean, line 87](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Shift.lean#L87) |  |
| `CategoryTheory.AdditiveEuler.cochain_shift_term_support` | theorem | [HomologicalAlgebra/AdditiveEuler/Shift.lean, line 101](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Shift.lean#L101) |  |
| `CategoryTheory.AdditiveEuler.cochain_shift_term_sum` | theorem | [HomologicalAlgebra/AdditiveEuler/Shift.lean, line 110](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Shift.lean#L110) |  |
| `CategoryTheory.AdditiveEuler.cochainShiftHomologyIso` | def | [HomologicalAlgebra/AdditiveEuler/Shift.lean, line 119](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Shift.lean#L119) |  |
| `CategoryTheory.AdditiveEuler.cochain_shift_homology_sum` | theorem | [HomologicalAlgebra/AdditiveEuler/Shift.lean, line 135](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Shift.lean#L135) |  |
| `CategoryTheory.AdditiveEuler.cochain_euler_endpoints` | theorem | [HomologicalAlgebra/AdditiveEuler/Cochain.lean, line 54](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Cochain.lean#L54) |  |
| `CategoryTheory.AdditiveEuler.cochain_euler_eq_homology` | theorem | [HomologicalAlgebra/AdditiveEuler/Cochain.lean, line 77](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Cochain.lean#L77) |  |
| `CategoryTheory.AdditiveEuler.cochain_euler_eq_homology_of_bounded` | theorem | [HomologicalAlgebra/AdditiveEuler/Cochain.lean, line 86](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Cochain.lean#L86) |  |
| `CategoryTheory.AdditiveEuler.cochain_euler_acyclic` | theorem | [HomologicalAlgebra/AdditiveEuler/Cochain.lean, line 96](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Cochain.lean#L96) |  |
| `CategoryTheory.AdditiveEuler.cochain_euler_quasiIso` | theorem | [HomologicalAlgebra/AdditiveEuler/Cochain.lean, line 107](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/Cochain.lean#L107) |  |
| `CategoryTheory.AdditiveEuler.invariant_exact_pair_images` | theorem | [HomologicalAlgebra/AdditiveEuler/HomologySupport.lean, line 41](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/HomologySupport.lean#L41) |  |
| `CategoryTheory.AdditiveEuler.cochain_homology_local_additivity` | theorem | [HomologicalAlgebra/AdditiveEuler/HomologySupport.lean, line 73](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/HomologySupport.lean#L73) |  |
| `CategoryTheory.AdditiveEuler.cochain_homology_euler_endpoints` | theorem | [HomologicalAlgebra/AdditiveEuler/HomologySupport.lean, line 111](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/HomologySupport.lean#L111) |  |
| `CategoryTheory.AdditiveEuler.cochain_homology_sum_additive_of_endpoints` | theorem | [HomologicalAlgebra/AdditiveEuler/HomologySupport.lean, line 137](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/HomologySupport.lean#L137) |  |
| `CategoryTheory.AdditiveEuler.cochain_homology_sum_additive_of_supported` | theorem | [HomologicalAlgebra/AdditiveEuler/HomologySupport.lean, line 155](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/AdditiveEuler/HomologySupport.lean#L155) |  |
| `HomologicalComplex.cylinder.ι₀_comp_πCompι₀Homotopy_hom` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 30](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L30) |  |
| `CochainComplex.RelativePath.path_hom_π₀` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 56](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L56) |  |
| `CochainComplex.RelativePath.obj` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 73](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L73) |  |
| `CochainComplex.RelativePath.fst` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 77](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L77) |  |
| `CochainComplex.RelativePath.snd` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 81](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L81) |  |
| `CochainComplex.RelativePath.toTarget` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 85](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L85) |  |
| `CochainComplex.RelativePath.sectionMap` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 89](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L89) |  |
| `CochainComplex.RelativePath.section_fst` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 92](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L92) |  |
| `CochainComplex.RelativePath.section_snd` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 95](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L95) |  |
| `CochainComplex.RelativePath.section_toTarget` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 99](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L99) |  |
| `CochainComplex.RelativePath.fst_comp` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 104](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L104) |  |
| `CochainComplex.RelativePath.lift` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 109](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L109) |  |
| `CochainComplex.RelativePath.lift_fst` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 113](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L113) |  |
| `CochainComplex.RelativePath.lift_toTarget` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 117](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L117) |  |
| `CochainComplex.RelativePath.isPullbackAt` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 122](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L122) |  |
| `CochainComplex.RelativePath.contraction` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 179](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L179) |  |
| `CochainComplex.RelativePath.contraction_fst_hom` | theorem | [HomologicalAlgebra/Cochain/RelativePath.lean, line 208](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L208) |  |
| `CochainComplex.RelativePath.equivalence` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 213](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L213) |  |
| `CochainComplex.RelativePath.comparison` | def | [HomologicalAlgebra/Cochain/RelativePath.lean, line 220](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Cochain/RelativePath.lean#L220) |  |
| `CategoryTheory.Subobject.quotientIntersectionPair` | def | [HomologicalAlgebra/Abelian/QuotientIntersection.lean, line 46](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/QuotientIntersection.lean#L46) |  |
| `CategoryTheory.Subobject.quotientIntersectionPair_fst` | theorem | [HomologicalAlgebra/Abelian/QuotientIntersection.lean, line 58](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/QuotientIntersection.lean#L58) |  |
| `CategoryTheory.Subobject.quotientIntersectionPair_snd` | theorem | [HomologicalAlgebra/Abelian/QuotientIntersection.lean, line 66](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/QuotientIntersection.lean#L66) |  |
| `CategoryTheory.Subobject.quotientIntersectionPair_fac` | theorem | [HomologicalAlgebra/Abelian/QuotientIntersection.lean, line 74](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/QuotientIntersection.lean#L74) |  |
| `CategoryTheory.Subobject.mono_quotientIntersectionPair` | instance | [HomologicalAlgebra/Abelian/QuotientIntersection.lean, line 129](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/QuotientIntersection.lean#L129) |  |
| `CategoryTheory.QuadrantProductTotal.Bicomplex` | abbrev | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 34](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L34) |  |
| `CategoryTheory.QuadrantProductTotal.Diag` | abbrev | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 38](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L38) |  |
| `CategoryTheory.QuadrantProductTotal.firstRow` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 41](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L41) |  |
| `CategoryTheory.QuadrantProductTotal.firstColumn` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 44](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L44) |  |
| `CategoryTheory.QuadrantProductTotal.diagonalIndex` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 47](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L47) |  |
| `CategoryTheory.QuadrantProductTotal.primitiveIndex` | abbrev | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 53](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L53) |  |
| `CategoryTheory.QuadrantProductTotal.diagonalIndex_surjective` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 58](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L58) |  |
| `CategoryTheory.QuadrantProductTotal.primitiveIndex_of_row` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 68](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L68) |  |
| `CategoryTheory.QuadrantProductTotal.cycleIndex` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 81](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L81) |  |
| `CategoryTheory.QuadrantProductTotal.Product` | abbrev | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 87](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L87) |  |
| `CategoryTheory.QuadrantProductTotal.degree` | abbrev | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 91](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L91) |  |
| `CategoryTheory.QuadrantProductTotal.horizontalIndex` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 95](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L95) |  |
| `CategoryTheory.QuadrantProductTotal.verticalIndex` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 99](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L99) |  |
| `CategoryTheory.QuadrantProductTotal.cycleIndex_horizontal` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 102](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L102) |  |
| `CategoryTheory.QuadrantProductTotal.cycleIndex_vertical` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 107](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L107) |  |
| `CategoryTheory.QuadrantProductTotal.horizontal` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 117](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L117) |  |
| `CategoryTheory.QuadrantProductTotal.vertical` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 123](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L123) |  |
| `CategoryTheory.QuadrantProductTotal.horizontalMap` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 130](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L130) |  |
| `CategoryTheory.QuadrantProductTotal.verticalMap` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 134](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L134) |  |
| `CategoryTheory.QuadrantProductTotal.horizontalMap_apply` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 137](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L137) |  |
| `CategoryTheory.QuadrantProductTotal.verticalMap_apply_zero` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 143](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L143) |  |
| `CategoryTheory.QuadrantProductTotal.verticalMap_apply_pos` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 148](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L148) |  |
| `CategoryTheory.QuadrantProductTotal.differential` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 156](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L156) |  |
| `CategoryTheory.QuadrantProductTotal.differential_eq` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 159](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L159) |  |
| `CategoryTheory.QuadrantProductTotal.differential_apply_zero` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 166](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L166) |  |
| `CategoryTheory.QuadrantProductTotal.differential_apply_pos` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 173](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L173) |  |
| `CategoryTheory.QuadrantProductTotal.horizontal_square` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 182](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L182) |  |
| `CategoryTheory.QuadrantProductTotal.vertical_square` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 196](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L196) |  |
| `CategoryTheory.QuadrantProductTotal.horizontal_vertical_comm` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 224](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L224) |  |
| `CategoryTheory.QuadrantProductTotal.differential_square` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 253](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L253) |  |
| `CategoryTheory.QuadrantProductTotal.productTotal` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 269](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L269) |  |
| `CategoryTheory.QuadrantProductTotal.mapDegree` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 297](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L297) |  |
| `CategoryTheory.QuadrantProductTotal.mapDegree_apply` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 301](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L301) |  |
| `CategoryTheory.QuadrantProductTotal.map_horizontal` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 306](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L306) |  |
| `CategoryTheory.QuadrantProductTotal.map_vertical` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 321](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L321) |  |
| `CategoryTheory.QuadrantProductTotal.map_differential` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 344](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L344) |  |
| `CategoryTheory.QuadrantProductTotal.productTotal_d` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 350](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L350) |  |
| `CategoryTheory.QuadrantProductTotal.nextHorizontalIndex` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 355](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L355) |  |
| `CategoryTheory.QuadrantProductTotal.nextVerticalIndex` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 359](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L359) |  |
| `CategoryTheory.QuadrantProductTotal.productTotal_d_apply_zero` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 363](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L363) |  |
| `CategoryTheory.QuadrantProductTotal.productTotal_d_apply_pos` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 373](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L373) |  |
| `CategoryTheory.QuadrantProductTotal.productTotalMap` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 386](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L386) |  |
| `CategoryTheory.QuadrantProductTotal.productTotalMap_f` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 400](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L400) |  |
| `CategoryTheory.QuadrantProductTotal.mapDegree_id` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 403](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L403) |  |
| `CategoryTheory.QuadrantProductTotal.mapDegree_comp` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 408](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L408) |  |
| `CategoryTheory.QuadrantProductTotal.productTotalMap_id` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 414](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L414) |  |
| `CategoryTheory.QuadrantProductTotal.productTotalMap_comp` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 421](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L421) |  |
| `CategoryTheory.QuadrantProductTotal.row_lift` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 431](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L431) |  |
| `CategoryTheory.QuadrantProductTotal.cycle_equation` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 457](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L457) |  |
| `CategoryTheory.QuadrantProductTotal.horizontal_at_zero` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 474](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L474) |  |
| `CategoryTheory.QuadrantProductTotal.first_kernel` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 482](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L482) |  |
| `CategoryTheory.QuadrantProductTotal.residual_kernel` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 503](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L503) |  |
| `CategoryTheory.QuadrantProductTotal.vertical_square_apply` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 520](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L520) |  |
| `CategoryTheory.QuadrantProductTotal.cycle_equation_step` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 529](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L529) |  |
| `CategoryTheory.QuadrantProductTotal.coordinate` | abbrev | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 541](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L541) |  |
| `CategoryTheory.QuadrantProductTotal.LiftState` | abbrev | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 548](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L548) |  |
| `CategoryTheory.QuadrantProductTotal.initialState_exists` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 555](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L555) |  |
| `CategoryTheory.QuadrantProductTotal.nextState_exists` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 570](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L570) |  |
| `CategoryTheory.QuadrantProductTotal.liftStates` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 606](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L606) |  |
| `CategoryTheory.QuadrantProductTotal.liftStates_first` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 613](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L613) |  |
| `CategoryTheory.QuadrantProductTotal.liftStates_step` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 620](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L620) |  |
| `CategoryTheory.QuadrantProductTotal.primitive` | def | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 633](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L633) |  |
| `CategoryTheory.QuadrantProductTotal.primitive_apply_index` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 641](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L641) |  |
| `CategoryTheory.QuadrantProductTotal.primitive_apply_early` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 665](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L665) |  |
| `CategoryTheory.QuadrantProductTotal.nextHorizontalIndex_diag` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 672](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L672) |  |
| `CategoryTheory.QuadrantProductTotal.nextVerticalIndex_diag_succ` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 676](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L676) |  |
| `CategoryTheory.QuadrantProductTotal.nextVerticalIndex_diag_first_early` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 682](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L682) |  |
| `CategoryTheory.QuadrantProductTotal.primitive_boundary_index` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 690](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L690) |  |
| `CategoryTheory.QuadrantProductTotal.acyclic_productTotal` | theorem | [HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean, line 756](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Homology/ProductTotalAcyclicity.lean#L756) |  |
| `CategoryTheory.AdmissibleLayer` | structure | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 40](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L40) |  |
| `CategoryTheory.AdmissibleLayer.LowerBounded` | abbrev | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 71](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L71) |  |
| `CategoryTheory.AdmissibleLayer.lowerInclusion` | def | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 75](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L75) |  |
| `CategoryTheory.AdmissibleLayer.lowerInclusion_monotone` | theorem | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 80](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L80) |  |
| `CategoryTheory.AdmissibleLayer.lowerCut` | def | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 88](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L88) |  |
| `CategoryTheory.AdmissibleLayer.lowerCut_lower` | theorem | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 100](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L100) |  |
| `CategoryTheory.AdmissibleLayer.lowerCut_upper` | theorem | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 104](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L104) |  |
| `CategoryTheory.AdmissibleLayer.lowerCut_galoisConnection` | theorem | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 109](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L109) |  |
| `CategoryTheory.AdmissibleLayer.lowerCut_monotone` | theorem | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 121](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L121) |  |
| `CategoryTheory.AdmissibleLayer.le_lowerInclusion_lowerCut` | theorem | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 126](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L126) |  |
| `CategoryTheory.AdmissibleLayer.lowerCut_lowerInclusion` | theorem | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 133](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L133) |  |
| `CategoryTheory.AdmissibleLayer.lowerCutAdjunction` | def | [HomologicalAlgebra/Abelian/AdmissibleLayers.lean, line 142](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/AdmissibleLayers.lean#L142) |  |

The scan does not find 2 of them declared in the file the yaml gives: `CategoryTheory.End.drazinInverse_comp_eq_comp_drazinInverse_assoc` ([HomologicalAlgebra/Abelian/Drazin.lean](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/Drazin.lean)), `CategoryTheory.Subobject.quotientIntersectionPair_fac_assoc` ([HomologicalAlgebra/Abelian/QuotientIntersection.lean](https://github.com/FormalFrontier/homological-algebra/blob/8bcaebe913c50e1c09e347333d21093646101018/HomologicalAlgebra/Abelian/QuotientIntersection.lean)).
