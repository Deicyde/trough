# General linear groups

> Finite general linear groups over possibly noncommutative semirings and rings: Kronecker products of matrix units with reversed identity-factor inverse witnesses, elementary units, ordered commutators, relative normal closures inside elementary groups, finite stabilization, Whitehead block factorization and doubled relative membership and lifting; rectangular block units for independent finite indices with explicit diagonal units; reindexing, nil and quasiregular ideals, congruence subgroups and quotient lifting, nonunital unitization, and matrix trace modulo additive commutators. Scalar unit reflection for Ring-to-Semiring homomorphisms forces quasi-regularity of the canonical two-sided kernel without surjectivity; for surjective maps it is equivalent to this kernel condition. Source and target universes are independent, with no commutativity or local-ring hypothesis. A square-zero kernel of any Ring-to-Semiring homomorphism identifies units mapping to 1 with the additive kernel via u - 1 and 1 + x; the inverse unit has value 1 - x. All mixed kernel products must vanish, with no surjectivity assumption. For left ideals I, J with I^2 contained in J, original-ring principal units map to the additive layer I/(I intersect J); Jacobson containment of I makes the map surjective and identifies its kernel quotient with that layer. Neither two-sidedness nor J contained in I is required. Dual-number GL, SL and scalar-unit reduction kernels, determinant/trace, coefficient maps and the left-conjugation adjoint action use commutative rings. The trace quotient is an additive group, not a quotient ring; its corner inverse requires a chosen matrix index. A Steinberg presentation adds elementary-symbol relations, universal lifts and a finite map onto the elementary subgroup, without opposite-root or central-extension assertions. Over iterated dual numbers, Mathlib's GL units have an ordered commutator equal to the mixed lift of the associative matrix bracket; its outer reduction-kernel element has complete pure-inner readback. For trace-zero inputs, the refinement in Mathlib's SL group uses special-linear factors, identifies the ordered mixed commutator and reads back its pure-inner trace-zero coefficient in the outer SL kernel. Elementary unit-pivot diagonalization, product-one diagonal membership, continuous elementary paths and finite special-linear elementary neighborhoods add algebraic and topological interfaces with their respective unit-minor, path-connectedness and open-scalar-unit hypotheses. Zero-product rectangular blocks over any ring yield a unit 1 + AB whose stabilization is an elementary ordered commutator of block shears. Stable general linear groups form a direct limit over semirings; over rings their stable elementary subgroup is perfect and equals the commutator subgroup, with quotient canonically the abelianization. Over commutative rings the stable determinant and its quotient and abelianization factorizations admit rank-one sections; the elementary subgroup lies in the determinant kernel. Ordered products of matrices with entries in a left ideal I over a semiring have entries in I raised to the list length, for independent finite decidable indices, including empty lists and indices. Repeated factors recover the matrix-power bound. Any exponent annihilating the whole ideal also annihilates a matrix whose entries lie in it.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

6 articles: 5 for highlights of its formalization.yaml and 1 for headline results in its README whose declaration link names a declaration the linked file declares. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups), read at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “independent agent review; no human mathematical review claimed”
- Review notes: “Reviews and build evidence concern specific revisions. No complete Weibel source correspondence or source formalization is asserted.”
- Automation: agent; framework “AI agents using Lean and Lake”; tool setup “Formal Frontier Agents developed Lean proofs and ordinary-import clients using mathlib APIs, compiler feedback and Lake. The clients exercise the public interfaces and degenerate examples; the historical API reference does not enumerate all present results.”
- Automation notes: “AI agents produced code, proofs and documentation with compiler feedback; no human mathematical review or source-author endorsement is asserted. AI generation alone does not establish originality, copyright ownership or third-party redistribution rights.”

## Scope

Reusable finite general-linear-group mathematics over rings, including elementary and relative groups, block factorizations, congruence and quasi-regular quotients, additive trace, a Steinberg presentation, and dual-number kernels in Mathlib's GL/SL groups and ordered mixed commutators. Core rings may be noncommutative; the dual-number layer requires CommRing. The additional elementary algebra/topology layer covers unit-pivot diagonalization, product-one diagonals, local-ring elementary generation, elementary paths and neighborhoods in Mathlib's SL group, each with its stated hypotheses. Scalar unit-reflecting Ring-to-Semiring homomorphisms have quasi-regular canonical two-sided kernels without surjectivity; for surjective maps, this kernel condition is also sufficient for unit reflection. Source and target universes are independent, with no commutativity, local-ring, nontriviality or nil-kernel assumption. Stable general linear groups over semirings have finite representatives, injective stages, compatible lifts and coefficient maps. Over rings the stable elementary subgroup is the commutator subgroup, is intrinsically perfect, and has abelian quotient canonically equivalent to the abelianization. Over commutative rings the stable determinant and its quotient and abelianization factorizations have rank-one sections; elementary matrices are contained in the determinant kernel. The abelian stable elementary quotient is the product of its determinant kernel and the unit group, compatibly with coefficient maps. Over commutative local rings, invertible matrices admit two-sided elementary diagonalization, finite elementary membership is equivalent to determinant one in every rank, stable elementary equals the stable determinant kernel, and the quotient determinant identifies the elementary quotient with the coefficient units via the rank-one section. Fintype and DecidableEq hypotheses apply to matrix index types where stated. The results do not establish stable K1 or K2, a source-complete K-theory formalization, or source-passage coverage.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [The K-book: An Introduction to Algebraic K-theory](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf), Charles A. Weibel, Complete-book edition (August 29, 2013): Exercises I.1.10-I.1.12; Chapter II, section 2, trace discussion on displayed page 73 (physical PDF page 81). (book; adapts).
- [Local Fields and Their Extensions](https://ivanfesenko.org/wp-content/uploads/2021/10/vol.pdf), I. B. Fesenko, S. V. Vostokov, Second edition (2002), Chapter I, (5.3) and (5.4)(3). (book; adapts).

## Builds on

- [Adic modules](../../commutative-algebra/adic-modules/README.md) (a Lake dependency, pinned at d0ce9c7e)

## Used by

- [Algebraic groups](../../algebraic-geometry/algebraic-groups/README.md)
- [Group rings](../../ring-theory/group-rings/README.md)
- [Projective modules](../../ring-theory/projective-modules/README.md)
- [Stable range](../../ring-theory/stable-range/README.md)
- [Valuation integers](../../number-theory/valuation-integers/README.md)

## Highlights

- [Principal-unit quotients and Jacobson lifting](principal-unit-quotients-and-jacobson-lifting.md)
- [Square-zero unit kernels and conjugation](square-zero-unit-kernels-and-conjugation.md)
- [Nilpotent principal-unit groups](nilpotent-principal-unit-groups.md)
- [Positive principal-unit layer commutator pairings](positive-principal-unit-layer-commutator-pairing.md)
- [Functorial symbols and Jacobson equivalences](functorial-symbols-and-jacobson-equivalences.md)

## Headline results

**Elementary generation over Euclidean domains.** For any `EuclideanDomain R`,
an invertible finite matrix belongs to the elementary subgroup exactly when
its determinant is one, including empty and singleton index types. The stable
elementary quotient is multiplicatively equivalent to `Rˣ`, with the existing
quotient determinant as forward map and the existing rank-one section as inverse.
Both directions commute with arbitrary ring homomorphisms between Euclidean
domains. [Euclidean elementary generation](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/EuclideanElementaryGeneration.lean).

**Signed swaps and even permutation matrices.** Over any possibly noncommutative
`Ring R`, the word `e_ij(1) e_ji(-1) e_ij(1)` gives the signed coordinate swap
with block `[0,1;-1,0]`. Every even permutation of a finite decidable basis gives
an element of the original finite elementary subgroup, including ranks zero,
one and two and zero rings. The permutation unit sends `e_i` to `e_(σ i)`;
no parity converse is asserted in characteristic two. The argument follows
Weibel, *The K-book*, III.1.2.1, using Mathlib's permutation units and generation
of the alternating group by three-cycles.
[Signed coordinate swaps and even permutations](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryPermutation.lean).

**Upper-triangular semiring nilpotence.** For an arbitrary, possibly
noncommutative `Semiring R` and an independently-universed finite linearly ordered
index type, an upper triangular matrix is nilpotent if and only if every diagonal
entry is nilpotent. Given `e : ι → ℕ` killing the corresponding diagonal entries,
the bound is `A ^ (∑ i, e i) = 0`, including empty indices and zero exponents.
The strict `Fin n` predicate uses only `Zero`; its support bound holds over
`NonUnitalNonAssocSemiring` and its nilpotence over `NonUnitalSemiring`.
Positive-power index `n` means `n + 1` factors, not an exact `n`th-power bound.
The unitization and relative general linear constructions require
`NonUnitalRing`.
[Upper-triangular nilpotence](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UpperTriangularNilpotent.lean),
[nonunital powers and strict triangularity](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/NonUnitalNilpotent.lean).

**Finite block-triangular units.** Over any possibly noncommutative `Ring`,
a block-triangular matrix on a finite decidable index type is a unit if each
equality-fiber diagonal block is a unit and its represented labels form a
strict chain in a `Preorder`. For a `PartialOrder`, a chain for `≤` suffices.
The index, label and coefficient universes are independent. Labels have
decidable equality but need not be finite or globally linearly ordered,
and block sizes may differ. Empty indices, empty fibers and zero rings are
included. Over a `Semiring`, the converse holds if each original
diagonal-block matrix monoid is Dedekind-finite: an ambient matrix unit
then has unit diagonal blocks. Separately, given `[Invertible M]` and unit
diagonal blocks, the given inverse `⅟M` is block triangular over a semiring,
with no direct-finiteness assumption. Both directions retain the same
represented-chain hypotheses; neither asserts semiring sufficiency from
diagonal units or derives matrix direct finiteness from scalar direct
finiteness.
[Block-unit criterion](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/BlockTriangularUnits.lean).

**Matrix ideal-power bounds and nilpotence.** For a `Semiring R` and a left
ideal `I : Ideal R`, an ordered list `As` of square matrices with entries in
`I` has `(As.prod) i j ∈ I ^ As.length`. The finite decidable index type has
a universe independent of the coefficients. Repeated factors recover
`(A ^ k) i j ∈ I ^ k`. Any exponent annihilating
the whole ideal also annihilates the matrix, so `IsNilpotent I` implies
`IsNilpotent A`. Empty lists, empty indices and zero semirings are included,
without two-sidedness or commutativity. Right-append induction matches
`I ^ (k + 1) = I ^ k * I`, without a multiplicative monoid on arbitrary
left ideals; pointwise nilness of an arbitrary ideal does not give a
uniform exponent. For a `CommSemiring R`, however, a finite
square matrix with nilpotent entries is nilpotent: its finitely generated
entry ideal is contained in the nilradical and is therefore nilpotent.
This needs no Noetherian hypothesis and includes empty indices and zero semirings.
[Ordered-product bound and nilpotence](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixNilpotentIdeal.lean),
[nilpotent entries](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixNilpotentEntries.lean),
[nonzero dual-number diagonal](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/MatrixNilpotentIdeal.lean),
[nonzero matrix over `ZMod 4`](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/MatrixNilpotentEntriesClient.lean).

**Kronecker products of matrix units.** Over any `Semiring`, the Kronecker
product of two unit matrices is a unit, for independently-universed finite
decidable square indices, including empty indices and zero semirings. The
ordered factorization `(A ⊗ₖ 1) * (1 ⊗ₖ B)`, for chosen input units with
stored inverse values `A'` and `B'`, supplies the reversed inverse witness
`(1 ⊗ₖ B') * (A' ⊗ₖ 1)`; tensoring input inverses is not valid in general
over noncommutative coefficients. The rectangular mixed identity
needs only a `NonAssocSemiring` and finite, decidable middle indices. Over
commutative coefficients, the extracted unit agrees with mathlib's general
linear Kronecker construction.
[Unit preservation](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/KroneckerUnits.lean),
[operational examples](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/KroneckerUnits.lean).

**Single-entry matrix corners.** For a `Semiring R`, finite decidable indices
and a chosen index `i`, the corner of `Matrix ι ι R` at the diagonal matrix
unit `single i i 1` is ring-equivalent to `R` by extracting the `(i,i)` entry;
its inverse inserts a coefficient there. The corner identity is the matrix
unit, which need not be the ambient matrix identity. The equivalence also
covers noncommutative and zero semirings.
[Corner equivalence](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixCorner.lean),
[concrete clients](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/MatrixCornerClient.lean).

**Whitehead factorization and doubled lifting.** Over any `Ring`, the
block diagonal `diag(g, g⁻¹)` of a unit is elementary. A surjective ring
homomorphism lifts this *doubled* block as a unit; it need not lift the
original same-rank unit. For separately finite block indices, explicitly
supplied diagonal units also give rectangular upper-triangular units with
ordered inverse block `-(A⁻¹ * B * D⁻¹)`.
[Factorization](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Whitehead.lean),
[doubled lift](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Whitehead.lean#L164),
[elementary membership](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L117),
[rectangular guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/RectangularBlockUnits.md).

**Stable general linear and elementary groups.** Initial-segment stabilization
defines a coherent system of finite general linear groups over any `Semiring`,
whose noncommutative direct limit has finite representatives, an eventual
equality criterion, compatible lifts and coefficient maps. Over any `Ring`, the
directed union of finite elementary images is the stable commutator subgroup;
it is perfect in its own right and normal in stable general linear groups.
Its quotient is canonically the abelianization, naturally under coefficient
maps. No finite ambient elementary normality or commutativity hypothesis is needed.
[Stable general linear group](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableGeneralLinear.lean),
[stable elementary group](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableElementary.lean),
[boundary and quotient clients](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/StableElementaryClient.lean).

**Opposite coefficients.** Over any `Semiring R`, inverse-transpose gives
`GL ι R ≃* GL ι Rᵐᵒᵖ` for finite decidable indices and an equivalence of the
original stable groups. Its entries are `op ((g⁻¹) j i)`, using the unit inverse.
Both directions commute with stabilization and arbitrary unital coefficient maps;
double application is canonical double-opposite coefficient transport. Over a
`Ring R`, it identifies the original stable elementary subgroups and induces an
equivalence of their quotients, with representative and coefficient-naturality
formulas. Empty ranks and zero semirings are allowed.
[Finite inverse-transpose](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Opposite.lean),
[stable inverse-transpose](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableOpposite.lean),
[elementary quotients](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableElementaryOpposite.lean).

**Finite coefficient products of stable groups and elementary quotients.** For arbitrary `Semiring R` and `Semiring S` in independent universes,
coefficient projections give `StableGL (R × S) ≃* (StableGL R × StableGL S)`.
For `[Finite ι]` and a family of semirings `R i`, evaluation gives
`StableGL (∀ i, R i) ≃* (∀ i, StableGL (R i))`, including the empty family.
Over arbitrary rings these comparisons carry the stable elementary subgroup
onto the product of the elementary subgroups and induce equivalences of the
existing elementary quotients. All comparisons commute with arbitrary
coefficient maps; inverse-stage computations allow unequal representative
ranks after passage to any common upper bound. Zero rings and rank zero are
included; no unrestricted infinite-product stable-group equivalence is asserted.
These extend the binary ring example in Weibel, *The K-book*, Example III.1.1.3.
[Finite coefficient products](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableProduct.lean).

**Matrix invariance of stable groups and elementary quotients.** For `0 < n`,
fixed row-major flattening gives
`StableGL (Matrix (Fin n) (Fin n) R) ≃* StableGL R` over any `Semiring R`.
Over a `Ring R`, it induces an equivalence of the existing stable elementary
quotients. Over a `CommRing R`, the transported quotient determinant on a
matrix-ring unit is its ordinary finite determinant.
[Matrix invariance](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableMatrix.lean).

**Stable determinant.** Over a commutative ring, finite determinants induce
homomorphisms on stable general linear groups, their elementary quotient and
their abelianization. Rank-one units provide determinant sections; the
elementary subgroup lies in the determinant kernel. The abelian elementary quotient
splits as the product of its
determinant kernel and the units, naturally under coefficient maps; this
does not assert a product splitting of stable general linear groups.
For commutative local rings, elementary matrices equal the determinant kernel,
and the existing quotient determinant is an equivalence with the units.
The rank-one map itself is defined over any semiring.
[Determinant and rank-one maps](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean),
[integer and boundary examples](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/StableDeterminantClient.lean).

**Zero-product elementary stabilization.** For rectangular `A`, `B` over any
`Ring` with `B * A = 0`, the unit `1 + A * B` has inverse `1 - A * B`.
Stabilizing by the identity on the other block gives exactly the ordered
commutator of the upper shear of `A` and lower shear of `B`, hence an
elementary unit. Both index types may be empty.
[Construction and factorization](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ZeroProductStabilization.lean),
[integer and boundary examples](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/ZeroProductStabilizationClient.lean).

**Rectangular complement isomorphisms.** In any preadditive category
`C : Type u` with `Category.{v} C`, for arbitrary objects `X`, `Y` and
morphisms `a : X ⟶ Y`, `b : Y ⟶ X`, the complements are simultaneously
isomorphisms:
`IsIso (𝟙 X - a ≫ b) ↔ IsIso (𝟙 Y - b ≫ a)`. Their canonical inverse is
`inv (𝟙 X - a ≫ b) = 𝟙 X + a ≫ inv (𝟙 Y - b ≫ a) ≫ b` under only
`IsIso (𝟙 Y - b ≫ a)`. The universes `u`, `v` are independent; no
finiteness, biproduct or nonzero-object hypothesis is imposed. The
rectangular unit-switch inverse below is a finite-matrix specialization.
[Criterion and inverse](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularIsomorphisms.lean).

**Rectangular unit switch.** Over any `Ring`, for independently finite,
decidable index types, a unit `g = 1 + A * B` determines a unit
`h = 1 + B * A` with inverse `1 - B * g⁻¹ * A`. Its diagonal pair
`diag(g, h⁻¹)` is the ordered product
`U(A) L(B) U(-(g⁻¹ * A)) L(-(B * g))`, hence elementary.
Empty blocks and the zero ring are allowed; `B * A = 0` recovers the
zero-product stabilization commutator above.
[Construction and factorization](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularUnitSwitch.lean),
[integer and boundary examples](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/RectangularUnitSwitchClient.lean).

**Ring Schur reduction.** For independently finite, decidable block indices
over any `Ring`, an invertible northwest block `A` makes
`[[A, B], [C, D]]` a unit exactly when the ordered residual
`D - C * ⅟A * B` is a unit. Given a unit residual, the corresponding block
unit has an explicit ordered inverse; homomorphisms killing the elementary
subgroup see only the diagonal pivot and residual, with no condition on
the target group. Empty blocks and the zero ring are included.
[Construction and criterion](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/SchurReduction.lean),
[noncommutative and boundary clients](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/SchurReductionClient.lean).

**Unit-pivot reduction and elementary diagonals.** Over any `CommRing`,
unit ordered leading minors permit two-sided elementary diagonalization;
a product-one diagonal is elementary, and the unit-pivot, determinant-one
criterion puts a finite GL unit in `E`. This is not a general `SL = E`
theorem; the minor hypothesis is stronger than nonvanishing. More generally,
if an elementary left factor can produce a unit leading
entry for every invertible matrix at every successor rank, the same
two-sided reduction exists at every finite rank. The latter theorem is
conditional on that all-rank pivot property; it does not assert an
unconditional elementary generation theorem.
[Unit-pivot guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/UnitPivotDiagonalization.md),
[conditional pivot induction](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UnitPivotInduction.lean),
[diagonal guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/ElementaryDiagonal.md).

**Elementary generation over local rings.** Every invertible finite matrix
over a commutative local ring has elementary left and right factors reducing
it to a diagonal of units, without a leading-minor hypothesis. At every
finite rank, determinant one characterizes the elementary subgroup. The
stable elementary subgroup is the determinant kernel, and the elementary
quotient is canonically the coefficient units via the existing determinant
and rank-one section. Over a field, Mathlib transvection lists give an
invertible diagonal factorization.
[Local generation](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalElementaryGeneration.lean),
[nonfield and rank-boundary clients](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/LocalElementaryGenerationClient.lean).

**Elementary paths and SL neighborhoods.** Over a topological ring,
elementary GL units vary continuously with coefficients, even when the
coefficient ring is noncommutative. Path-connected coefficients make the
elementary subgroup path connected. For commutative coefficients, an open
scalar-unit locus makes its comap in Mathlib's special linear group open
and closed; additionally path-connected coefficients identify it with the
identity path component.
[Paths guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/ElementaryPaths.md),
[neighborhood guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/ElementaryNeighborhood.md).

- [Scalar unit reflection and canonical quasi-regular kernels](scalar-unit-reflection-and-canonical-quasi-regul.md)

**Lifting modulo quasi-regular ideals.** For a two-sided ideal, its
unitization general linear group identifies with the congruence kernel;
quasi-regularity of *every* ideal element additionally makes the quotient
GL map surjective. The Jacobson radical is the greatest quasi-regular
ideal, and pointwise nil ideals provide examples without a shared nilpotence
exponent.
[Kernel equivalence](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/CongruenceSubgroup.lean#L292),
[quotient lifting](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L139),
[ideal characterization](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularIdeal.lean#L207).

**Trace modulo additive commutators.** For a chosen index `p : n`,
trace gives an additive equivalence from square matrices modulo additive
commutators to the coefficient ring modulo additive commutators; its inverse
inserts a scalar in the `p,p` corner. The forward map also works at empty
rank. These are *additive groups*, not quotient rings or a `K₀` descent.
[Equivalence and forward map](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixTrace.lean).
The following characteristic laws use weaker hypotheses:
[cyclic representatives and unit conjugation](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/AdditiveCommutator.lean)
require `AddCommGroup` with `Mul`, respectively `Monoid`, without distributivity;
[raw block trace](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixTrace.lean) requires only
`AddCommMonoid` and two independently-universed finite index types, without
decidable equality or nonemptiness. The raw `Sum`-indexed block shape
complements mathlib's dependent `trace_blockDiagonal'` formula.

**Finite elementary and relative structure.** Off-diagonal elementary
units generate `E`; ordered commutator laws prove that `E` is perfect at
rank at least three. A two-sided ideal defines the relative normal closure
*inside `E`*, not a claimed same-rank normal subgroup of ambient `GL`.
Congruence units become relatively elementary after Whitehead doubling;
stabilization preserves elementary, relative and congruence inclusions.
[Perfectness](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryCommutator.lean#L80),
[relative subgroup](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L98),
[relative Whitehead](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhitehead.lean#L134),
[guides](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/README.md).

**A Steinberg presentation and universal maps.** Over any `Ring`, for an
arbitrary index type, symbols satisfy precisely the additive, disjoint-root
and ordered-composable-root relations, and compatible maps extend uniquely.
Finite decidable indices additionally give a surjection onto `E`, not
onto all of `GL`. The reverse relation has coefficient `-(b * a)`; no
opposite-root, central-kernel or `K₂` theorem is claimed.
[Universal lift](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L121),
[onto-`E` map](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L206),
[presentation guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/FiniteRankSteinberg.md).

**Units over square-zero kernels.** For a homomorphism from any `Ring` to
any `Semiring`, a square-zero kernel identifies the units mapping to `1`
with the additive kernel, written multiplicatively. The coordinates are
`u ↦ u - 1` and `x ↦ 1 + x`, with inverse unit `1 - x`. The hypothesis
kills every mixed product of kernel elements; no commutativity or
surjectivity is needed. The scalar dual-number equivalence is a
specialization with its explicit lift and readback preserved. This is the
algebraic ingredient of Fesenko–Vostokov, Chapter I (5.4)(3), not a
unit-lifting or valuation-layer quotient theorem.
[Equivalence and coordinate API](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/SquareZeroUnits.lean),
[dual-number comparison](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberSquareZeroUnits.lean).

**Principal-unit ideal layers on original-ring units.** For left ideals
`I, J` in any `Ring`, with `I ^ 2 ≤ J`, the stock stabilizer of `[1]` in
the quotient left module `R / I` maps by `u ↦ [u - 1]` to the additive
layer `I / (I ∩ J)`, written multiplicatively. Its kernel is exactly the
relative stabilizer modulo `J`, which is therefore normal. If additionally
`I ≤ Ring.jacobson R`, the map is surjective and its kernel quotient is
isomorphic to that additive layer, with inverse `[x] ↦ [1 + x]` in the
original ring. Neither ideal needs to be two-sided, and `J ≤ I` is not
assumed. For two-sided `I`, the carrier agrees with the kernel of reduction
on units. The nonzero-denominator model uses `(3)/(9)` in `ZMod 27`;
the integer boundary explains the original-unit lifting hypothesis.
[Equivalence and characteristic laws](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean),
[models and boundary](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/PrincipalUnitsClient.lean).
For a commutative domain `R`, a nonzero principal ideal
`I = Ideal.span {π}` contained in `Ideal.jacobson ⊥`, and `n ≥ 1`,
the original-ring unit stabilizer at `I ^ n`, modulo its exact coordinate
kernel (the relative deeper stabilizer at `I ^ (n + 1)`), is equivalent
to `Multiplicative (R ⧸ I)`. It sends `[1 + a * π ^ n]` to `[a]`;
the inverse returns that original-ring unit class. The target is the additive
coefficient **ring**, not necessarily a field. Replacing `π` by `u * π`
for `u : Rˣ` with residue unit `ū` multiplies a fixed class's forward coefficient
by `(ū⁻¹) ^ n`; the inverse at a fixed coefficient uses the old inverse
with parameter multiplied by `ū ^ n`. Normality and surjectivity are
conclusions, not assumptions; exponent zero instead gives multiplicative
reduction.
[Coefficients and generator-change laws](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Powers.lean),
[coefficient clients](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/tests/GeneralLinearGroupsTests/PrincipalUnitsPowersClient.lean).

**Principal-unit commutators and nilpotence.** Over any `Ring R`, including
noncommutative and zero rings, write `U(I)` for the stock `Rˣ`-stabilizer
of `1` in the quotient left module `R ⧸ I`. For two-sided `I`, this is
the kernel of reduction on units to the quotient ring. Arbitrary left ideals
`A, B` satisfy `[U(A), U(B)] ≤ U(A * B + B * A)`. For two-sided `I`,
`[U(I ^ a), U(I ^ b)] ≤ U(I ^ (a + b))` for all `a, b : ℕ`, including
zero, without a nilpotence assumption. For any left ideal `I`, the lower
central series has `LCS(k) ≤ U(I ^ (k + 1))`, with zeroth term `U(I)`.
If `I ^ N = ⊥`, then `U(I)` is nilpotent of class at most `N - 1`
(natural subtraction); `N = 0` and `N = 1` give the trivial subgroup.
This is not a nilpotence claim about the full unit group. Positive additive
layers use the preceding ideal-layer and power-coordinate API, not an
additive equivalence at exponent zero.
[Commutator bounds and nilpotence](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean).

**Leading coordinates of principal-unit commutators.** For any left ideal
`I` in any `Ring R` and positive `a, b`, let `x = u - 1 ∈ I ^ a` and
`y = v - 1 ∈ I ^ b` for original-ring units `u, v`. Then
`[u, v] - 1 - (x * y - y * x) ∈ I ^ (a + b + min a b)`.
In particular, `[u, v] - 1` and `x * y - y * x` have the same class
in the quotient **left module** `R ⧸ I ^ (a + b + 1)`.
No two-sidedness, commutativity or nilpotence is needed; the commutator
is `u * v * u⁻¹ * v⁻¹`, with no degree-dependent sign.
[Coordinate estimate and quotient equality](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean),
[API guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/README.md#principal-unit-commutator-coordinates).

**Positive principal-unit layer pairings.** For any left ideal `I` in any
`Ring R` and `a, b : ℕ+`, the bracket `xy - yx` descends to an
**integer-bilinear** pairing of successive ideal layers in degrees
`a`, `b` and `a + b`. The additive positive unit layers embed in these
ideal layers by the injective symbol `[u] ↦ [u - 1]`; their pairing is
represented by the ordered commutator of original-ring units. Both pairings
are alternating, with ordinary negation under swapping and the canonical
degree cast. No two-sidedness, Jacobson condition or symbol surjectivity
is assumed, and no degree-zero additive layer is asserted.
[Pairings and characteristic laws](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Commutator.lean),
[API guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/README.md#positive-principal-unit-layer-pairings).

**Functorial symbols and Jacobson equivalences.** A unital ring map
carrying a left ideal `I` into `J` induces integer-linear maps on their
positive ideal and unit layers, preserving symbols and both commutator
pairings. The maps respect identities and composition, without injectivity,
surjectivity or radical assumptions on the ring map. If
`I ≤ Ring.jacobson R`, its symbol is an integer-linear equivalence, with
inverse represented by the original-ring unit `1 + x`. Inverse naturality
requires the Jacobson condition on **both** source and target ideals.
Symbols are also surjective when every element of the left ideal is
nilpotent, or when `I ^ N = ⊥`, including `N = 0, 1`; no two-sidedness
or common exponent is assumed for the pointwise-nil result.
[Forward maps and naturality](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Naturality.lean),
[Equivalences and nil lifting](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/LayerEquivalence.lean),
[API guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/README.md#functorial-symbols-and-jacobson-equivalences).

**Images of principal-unit subgroups.** For a ring homomorphism
`f : R →+* S` with `Ring R` and `Ring S` in independent universes,
and a left ideal `I ≤ Ideal.jacobson ⊥`, a unit `u : Sˣ` lies in the image
under `Units.map f.toMonoidHom` of the original `R`-unit stabilizer of
`[1]` in the quotient left module `R ⧸ I` exactly when
`∃ a ∈ I, f a = (u : S) - 1`.
This uses the set image of ideal elements, not the extended ideal
`Ideal.map f I`. The map need not be injective, and neither ring needs
to be commutative; no domain, local-ring or valuation hypothesis is needed.
[Image membership criterion](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Images.lean).

**Finite exponential and logarithm coordinates.** Over a possibly noncommutative
or zero rational algebra, Mathlib's finite exponential, packaged as a unit,
and a concrete logarithm give a plain equivalence between nilpotent elements
and units `u` with nilpotent coordinate `u - 1`. This restricts to the elements
of any pointwise-nil left ideal `I` and its principal-unit stabilizer of `1`
in the quotient left module `R ⧸ I`; neither two-sidedness nor a uniform
nilpotence exponent is required. Addition and product laws require commuting
inputs; integer multiples correspond to integer powers in the unit group.
These are equivalences of types, not group equivalences.
[Exponential units and logarithm](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/NilpotentExpLog.lean),
[principal-unit restriction](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/ExpLog.lean).

**First-order dual-number kernels and conjugation.** Over any `CommRing`,
the *multiplicative* reduction identity fibers of Mathlib's GL and SL groups
and of scalar units identify with additive matrices, trace-zero matrices
and scalars. The determinant corresponds to trace; arbitrary ring-hom
coefficient maps commute with these constructions without being implicitly
`R`-linear. Unit **left conjugation** corresponds to `g * X * g⁻¹`,
even for nonconstant dual-number units; the SL-kernel action uses SL
conjugators. First-order fiber groups are abelian, so their commutator is
not the generally nonzero matrix Lie bracket.
[Kernel equivalences](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L145),
[determinant/trace](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L316),
[adjoint guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/DualNumberKernelAdjoint.md).

**Mixed dual-number GL and SL commutators.** For finite matrices over a
`CommRing`, units over iterated dual numbers satisfy the ordered
identity `[1 + εX, 1 + ηY] = 1 + εη(XY - YX)` with full outer-kernel
readback. When *each input* is trace zero, special-linear factors
yield the analogous identity in Mathlib's SL group and trace-zero readback.
The ε-factor reduces to the inner lift `liftGL X` (in SL, `liftSL X`), usually
not `1`: this is not a bracket of two elements of the abelian first-order
outer kernel, nor a global Lie- or scheme-tangent theorem.
[GL identity](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L155),
[SL identity](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L93),
[GL guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/DualNumberMixedCommutator.md),
[SL guide](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/docs/DualNumberMixedSLCommutator.md).

## Main results

The 221 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `CategoryTheory.isIso_id_sub_comp_iff` | theorem | [GeneralLinearGroups/RectangularIsomorphisms.lean, line 71](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularIsomorphisms.lean#L71) | In a preadditive category with independent object and morphism universes, for arbitrary objects X, Y and morphisms a:X->Y, b:Y->X, IsIso (𝟙 X - a ≫ b) iff IsIso (𝟙 Y - b ≫ a). No finiteness, biproduct or nonzero-object hypothesis is imposed. |
| `CategoryTheory.inv_id_sub_comp` | theorem | [GeneralLinearGroups/RectangularIsomorphisms.lean, line 85](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularIsomorphisms.lean#L85) | Assuming only IsIso (𝟙 Y - b ≫ a), the canonical inverse of 𝟙 X - a ≫ b is 𝟙 X + a ≫ inv (𝟙 Y - b ≫ a) ≫ b. The left IsIso proof is derived from the criterion, not a second premise. |
| `Matrix.list_prod_apply_mem_ideal_pow` | theorem | [GeneralLinearGroups/MatrixNilpotentIdeal.lean, line 62](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixNilpotentIdeal.lean#L62) | Over a Semiring, an ordered list As of square matrices with entries in the same left ideal I has each product entry in I^As.length, for independently-universed finite decidable indices. Empty lists and indices are included. Right-append induction matches I^(k+1)=I^k*I; no commutativity, two-sidedness or monoid on left ideals is assumed. |
| `Matrix.pow_apply_mem_ideal_pow` | theorem | [GeneralLinearGroups/MatrixNilpotentIdeal.lean, line 85](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixNilpotentIdeal.lean#L85) | The replicate specialization gives entries of A^k in I^k for every natural k, including zero, over a Semiring with finite decidable indices. |
| `Matrix.isNilpotent_of_isNilpotent_ideal` | theorem | [GeneralLinearGroups/MatrixNilpotentIdeal.lean, line 93](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixNilpotentIdeal.lean#L93) | Uniform nilpotence of the left ideal containing all matrix entries implies matrix nilpotence, with the same vanishing exponent, even when that exponent is zero. No two-sidedness, Nonempty, commutativity, additive inverses or nontriviality premise is imposed; pointwise nilness of an ideal is not asserted to suffice. |
| `Matrix.GeneralLinearGroup.StableGL` | abbrev | [GeneralLinearGroups/StableGeneralLinear.lean, line 193](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableGeneralLinear.lean#L193) | Direct limit of finite GL groups under injective initial-segment stabilization over any Semiring, including the zero semiring and empty rank; finite representatives have an eventual equality criterion. |
| `Matrix.GeneralLinearGroup.StableGL.map` | def | [GeneralLinearGroups/StableGeneralLinear.lean, line 265](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableGeneralLinear.lean#L265) | Semiring-hom coefficient maps on stable GL commute with finite stages and respect identities and composition; compatible finite maps lift. |
| `Matrix.GeneralLinearGroup.stableElementarySubgroup_eq_commutator` | theorem | [GeneralLinearGroups/StableElementary.lean, line 200](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableElementary.lean#L200) | Over any Ring, the directed union of finite elementary images equals the commutator subgroup of stable GL. This does not assert same-rank ambient normality or commutator containment for finite GL. |
| `Matrix.GeneralLinearGroup.stableElementarySubgroup_isPerfect` | instance | [GeneralLinearGroups/StableElementary.lean, line 256](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableElementary.lean#L256) | The stable elementary subgroup is perfect as a group in its own right over any Ring, without a lower-rank restriction on stable GL. |
| `Matrix.GeneralLinearGroup.stableElementaryAbelianizationEquiv` | def | [GeneralLinearGroups/StableElementary.lean, line 340](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableElementary.lean#L340) | Over any Ring, the stable elementary quotient is an abelian group canonically equivalent to the abelianization; this equivalence is natural under ring-hom coefficient maps. |
| `Matrix.GeneralLinearGroup.StableGL.rankOneUnits_injective` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 40](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L40) | Rank-one units inject into stable GL over any Semiring, including noncommutative coefficients; their map is natural under semiring homs. |
| `Matrix.GeneralLinearGroup.StableGL.quotientRankOneUnits_map` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 235](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L235) | The rank-one map into the stable elementary quotient is natural over Rings; commutativity is needed only for its determinant retraction. |
| `Matrix.GeneralLinearGroup.StableGL.abelianizationRankOneUnits_map` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 259](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L259) | The rank-one map into the stable abelianization is natural over Semirings; commutativity is needed only for its determinant retraction. |
| `Matrix.GeneralLinearGroup.StableGL.det` | def | [GeneralLinearGroups/StableDeterminant.lean, line 71](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L71) | Compatible finite determinants define the stable determinant to units over any CommRing, including empty rank and the zero ring; it is natural under commutative-ring coefficient maps. |
| `Matrix.GeneralLinearGroup.StableGL.det_comp_rankOneUnits` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 86](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L86) | Over any CommRing, rank-one units give a right inverse to the stable determinant, hence the determinant is surjective. |
| `Matrix.GeneralLinearGroup.StableGL.elementary_le_ker_det` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 113](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L113) | Over any CommRing, stable elementary matrices lie in the determinant kernel; this is only an inclusion, not an equality. |
| `Matrix.GeneralLinearGroup.StableGL.quotientDet_eq_abelianizationDet` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 192](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L192) | Over any CommRing, determinant factorizations through the stable elementary quotient and the abelianization agree under their canonical equivalence; neither factorization identifies the kernel. |
| `Matrix.GeneralLinearGroup.StableGL.quotientDet_quotientRankOneUnits` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 141](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L141) | Over any CommRing, the ring-level quotient rank-one map is a section of the determinant induced on the stable elementary quotient. |
| `Matrix.GeneralLinearGroup.StableGL.quotientDetKernelMulEquiv` | def | [GeneralLinearGroups/StableDeterminant.lean, line 267](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L267) | Over any CommRing, including the zero ring, the abelian stable elementary quotient splits as its quotient determinant kernel times the units via the rank-one section. Its coordinate and coefficient-map laws do not identify or trivialize the kernel. |
| `Matrix.GeneralLinearGroup.StableGL.abelianizationDet_abelianizationRankOneUnits` | theorem | [GeneralLinearGroups/StableDeterminant.lean, line 180](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/StableDeterminant.lean#L180) | Over any CommRing, the semiring-level abelianization rank-one map is a section of the determinant induced on the abelianization. |
| `Matrix.GeneralLinearGroup.elementaryUnit` | def | [GeneralLinearGroups/Elementary.lean, line 42](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Elementary.lean#L42) | Off-diagonal unit 1 + single i j c over any Ring, with inverse, coefficient-addition product and a CommRing-only comparison with Mathlib transvections. It requires a finite decidable index type and i different from j, not a commutative coefficient ring. |
| `Matrix.GeneralLinearGroup.elementarySubgroup` | def | [GeneralLinearGroups/Elementary.lean, line 74](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Elementary.lean#L74) | Closure of elementary units, including generator and ordered-list product membership. It is bottom for subsingleton indices without implying that the entire GL group is trivial. |
| `Matrix.GeneralLinearGroup.upperUnit_mem_elementarySubgroup` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 73](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L73) | Upper block units lie in the elementary subgroup by single-entry decomposition, including empty indices and noncommutative rings. |
| `Matrix.GeneralLinearGroup.lowerUnit_mem_elementarySubgroup` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 86](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L86) | Lower block units use the negative lower-left block over any Ring. |
| `Matrix.GeneralLinearGroup.blockDiagonalUnit_mem_elementarySubgroup` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 117](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L117) | Doubled diag(g, g⁻¹) lies in the elementary subgroup using the signed swap membership and the existing ordered Whitehead factorization. |
| `Matrix.GeneralLinearGroup.zeroProductUnit` | def | [GeneralLinearGroups/ZeroProductStabilization.lean, line 31](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ZeroProductStabilization.lean#L31) | For independent finite index types and B * A = 0 over any Ring, constructs the unit 1 + A * B with inverse 1 - A * B. |
| `Matrix.GeneralLinearGroup.zeroProductUnit_val` | theorem | [GeneralLinearGroups/ZeroProductStabilization.lean, line 41](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ZeroProductStabilization.lean#L41) | Reads back the underlying matrix as 1 + A * B. |
| `Matrix.GeneralLinearGroup.zeroProductUnit_inv_val` | theorem | [GeneralLinearGroups/ZeroProductStabilization.lean, line 47](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ZeroProductStabilization.lean#L47) | Reads back the inverse matrix as 1 - A * B. |
| `Matrix.GeneralLinearGroup.stabilize_zeroProductUnit_eq` | theorem | [GeneralLinearGroups/ZeroProductStabilization.lean, line 56](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ZeroProductStabilization.lean#L56) | Stabilization of the zero-product unit equals the ordered commutator of rectangular upper and lower block shears, including empty blocks. |
| `Matrix.GeneralLinearGroup.stabilize_zeroProductUnit_mem_elementarySubgroup` | theorem | [GeneralLinearGroups/ZeroProductStabilization.lean, line 70](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ZeroProductStabilization.lean#L70) | The stabilized unit lies in the existing elementary subgroup over any Ring, including noncommutative and zero rings. |
| `Matrix.GeneralLinearGroup.mapRingHom` | def | [GeneralLinearGroups/Whitehead.lean, line 31](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Whitehead.lean#L31) | Coefficient maps on finite general linear groups over arbitrary semirings. |
| `Matrix.GeneralLinearGroup.blockDiagonalUnit_eq` | theorem | [GeneralLinearGroups/Whitehead.lean, line 115](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Whitehead.lean#L115) | Signed four-factor decomposition of diag(g, inverse g) over arbitrary rings. |
| `Matrix.GeneralLinearGroup.mapRingHom_liftBlockDiagonal` | theorem | [GeneralLinearGroups/Whitehead.lean, line 183](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Whitehead.lean#L183) | A surjective ring homomorphism lifts this doubled block diagonal. It need not induce a surjection on the original finite GL. |
| `Matrix.GeneralLinearGroup.reindexEquiv` | def | [GeneralLinearGroups/Reindex.lean, line 31](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Reindex.lean#L31) | Equivalence along a finite-index-type equivalence, with identity, composition, inverse and coefficient-map laws; not stabilization between unequal cardinalities. |
| `TwoSidedIdeal.isQuasiregular_iff_isRightQuasiregular` | theorem | [GeneralLinearGroups/QuasiregularIdeal.lean, line 119](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularIdeal.lean#L119) | The right-quasi-inverse condition is quantified over every element of the two-sided ideal. A single right inverse is not asserted to be two-sided in an arbitrary ring. |
| `TwoSidedIdeal.ringJacobson_isGreatest_isQuasiregular` | theorem | [GeneralLinearGroups/QuasiregularIdeal.lean, line 207](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularIdeal.lean#L207) | The Jacobson radical is the greatest quasiregular two-sided ideal. |
| `TwoSidedIdeal.IsNil.le_ringJacobson` | theorem | [GeneralLinearGroups/NilIdeal.lean, line 55](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/NilIdeal.lean#L55) | Pointwise nil ideals are quasiregular and contained in the Jacobson radical; no common exponent or nilpotence of the whole ideal is assumed. |
| `TwoSidedIdeal.IsQuasiregular.matrix` | theorem | [GeneralLinearGroups/MatrixQuasiregular.lean, line 30](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixQuasiregular.lean#L30) | Entrywise finite matrix ideals preserve quasiregularity, including empty indices. |
| `TwoSidedIdeal.quotientDivisionRing` | abbrev | [GeneralLinearGroups/LocalQuotient.lean, line 49](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalQuotient.lean#L49) | A proper two-sided ideal with unit complement gives a maximal left ideal and a division-ring quotient; commutativity and uniqueness of maximal ideals are not assumed. |
| `Matrix.GeneralLinearGroup.idealGeneralLinearGroupEquivCongruence` | def | [GeneralLinearGroups/CongruenceSubgroup.lean, line 301](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/CongruenceSubgroup.lean#L301) | The ideal-unitization augmentation kernel is equivalent to the ambient congruence subgroup. Ambient injectivity and multiplicative exactness hold for every two-sided ideal, independently of quotient surjectivity. |
| `RingHom.isQuasiregular_ker` | theorem | [GeneralLinearGroups/QuasiregularQuotient.lean, line 202](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L202) | For R : Type u and S : Type v with Ring R and Semiring S, a map f : R →+* S with IsLocalHom f has quasi-regular canonical two-sided kernel TwoSidedIdeal.ker f, without surjectivity. The universes are independent; no commutativity, local-ring, nontriviality or nilness assumption is needed. |
| `RingHom.isLocalHom_iff_isQuasiregular_ker` | theorem | [GeneralLinearGroups/QuasiregularQuotient.lean, line 214](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L214) | For a surjective f : R →+* S from a possibly noncommutative Ring to a Semiring, IsLocalHom f is equivalent to quasi-regularity of the canonical two-sided kernel TwoSidedIdeal.ker f. Source and target universes are independent; no local-ring or nontriviality hypothesis is imposed. Surjectivity is essential for this equivalence: the inclusion of integers into rationals has zero kernel but fails to reflect units. |
| `RingHom.isLocalHom_of_surjective_of_isQuasiregular_ker` | theorem | [GeneralLinearGroups/QuasiregularQuotient.lean, line 181](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L181) | A surjective homomorphism from a possibly noncommutative Ring to a Semiring with quasi-regular canonical two-sided kernel gives Mathlib's IsLocalHom, with independent source and target universes and no commutativity, locality or nontriviality assumption. Existing APIs give unit reflection and surjectivity of the induced units map; nil kernels specialize through TwoSidedIdeal.IsNil.isQuasiregular. |
| `Matrix.GeneralLinearGroup.isUnit_of_mapMatrix_quotient_isUnit` | theorem | [GeneralLinearGroups/QuasiregularQuotient.lean, line 77](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L77) | A specified finite square matrix is a unit if its image modulo a quasiregular two-sided ideal is a unit; empty indices are allowed. |
| `Matrix.GeneralLinearGroup.idealGeneralLinearGroupToRing_shortExact` | theorem | [GeneralLinearGroups/QuasiregularQuotient.lean, line 147](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L147) | The three injective, multiplicatively exact and surjective assertions hold under quasiregularity. This is not arbitrary quotient GL surjectivity. |
| `NonUnital.positivePow` | def | [GeneralLinearGroups/NonUnitalNilpotent.lean, line 41](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/NonUnitalNilpotent.lean#L41) | positivePow x k multiplies k+1 copies, without a multiplicative identity; NonUnital.IsNilpotent asks for such a positive power to vanish. |
| `Matrix.IsStrictlyUpperTriangular.isNilpotent` | theorem | [GeneralLinearGroups/NonUnitalNilpotent.lean, line 186](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/NonUnitalNilpotent.lean#L186) | Strictly upper triangular Fin n matrices over nonunital rings are nilpotent. The uniform n+1-copy witness includes the empty matrix. |
| `Matrix.GeneralLinearGroup.nilpotentMatrixElement` | def | [GeneralLinearGroups/NonUnitalNilpotent.lean, line 293](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/NonUnitalNilpotent.lean#L293) | A vanishing power after entrywise unitization constructs a kernel element with value 1+x and an explicit finite alternating geometric inverse. The supplied exponent may be zero only when its power equation holds. |
| `Matrix.GeneralLinearGroup.isUnit_one_add_unitizationMatrix_iff_isQuasiregular` | theorem | [GeneralLinearGroups/NonUnitalQuasiregular.lean, line 83](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/NonUnitalQuasiregular.lean#L83) | Nonunital quasiregularity is equivalent to invertibility of 1+x after unitization, and to representability in the augmentation kernel. No coefficient commutativity or nontriviality is inserted. |
| `Unitization.ringEquivProd` | def | [GeneralLinearGroups/UnitalComparison.lean, line 36](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UnitalComparison.lean#L36) | A unital algebra's unitization is the product of its commutative scalar ring and the algebra; the coefficient algebra need not be commutative. |
| `Matrix.GeneralLinearGroup.nonUnitalGeneralLinearGroupEquiv` | def | [GeneralLinearGroups/UnitalComparison.lean, line 135](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UnitalComparison.lean#L135) | For a unital ring, the augmentation-kernel group is the ordinary finite GL. |
| `Ring.additiveCommutators` | def | [GeneralLinearGroups/AdditiveCommutator.lean, line 50](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/AdditiveCommutator.lean#L50) | Additive-subgroup closure of a*b-b*a in a unital ring. It is not defined as a two-sided ideal. |
| `Matrix.trace_mul_sub_trace_mul_commutators` | theorem | [GeneralLinearGroups/MatrixTrace.lean, line 55](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixTrace.lean#L55) | A rectangular cyclic trace difference is a finite sum of scalar commutators, not generally zero in a noncommutative coefficient ring. |
| `Matrix.traceOnCommutatorQuotient` | def | [GeneralLinearGroups/MatrixTrace.lean, line 85](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixTrace.lean#L85) | Trace descends through the full additive commutator closure, even for empty indices. |
| `Matrix.traceQuotientEquiv` | def | [GeneralLinearGroups/MatrixTrace.lean, line 191](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/MatrixTrace.lean#L191) | For a chosen index p, trace is an additive equivalence with corner inverse r mapped to single p p r. Matrix-unit decomposition gives a membership criterion, inverse/representative laws and corner independence. No ring equivalence or empty-index inverse is asserted. |
| `Matrix.GeneralLinearGroup.elementaryUnit_commute_disjoint` | theorem | [GeneralLinearGroups/ElementaryCommutator.lean, line 31](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryCommutator.lean#L31) | Elementary units commute when neither off-diagonal position composes with the other. |
| `Matrix.GeneralLinearGroup.elementaryUnit_commutator` | theorem | [GeneralLinearGroups/ElementaryCommutator.lean, line 59](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryCommutator.lean#L59) | The ordered elementary commutator relation, valid for noncommutative rings. |
| `Matrix.GeneralLinearGroup.elementaryUnit_eq_commutator` | theorem | [GeneralLinearGroups/ElementaryCommutator.lean, line 72](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryCommutator.lean#L72) | A third index expresses every elementary generator as a commutator of generators. |
| `Matrix.GeneralLinearGroup.elementarySubgroup_isPerfect_of_three_le_card` | theorem | [GeneralLinearGroups/ElementaryCommutator.lean, line 80](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryCommutator.lean#L80) | The finite-rank elementary subgroup is perfect as soon as there are three indices. |
| `Matrix.GeneralLinearGroup.mapRingHom_elementaryUnit` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 32](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L32) | Entrywise coefficient mapping sends an elementary unit to an elementary unit. |
| `Matrix.GeneralLinearGroup.mapRingHom_elementarySubgroup_le` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 41](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L41) | Entrywise coefficient mapping preserves the absolute elementary subgroup. |
| `Matrix.GeneralLinearGroup.mapElementarySubgroup` | def | [GeneralLinearGroups/RelativeElementary.lean, line 52](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L52) | The restricted map on elementary subgroups. |
| `Matrix.GeneralLinearGroup.mapElementarySubgroup_coe` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 60](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L60) | The restricted coefficient map has the same ambient GL value as mapRingHom. |
| `Matrix.GeneralLinearGroup.mapElementarySubgroup_elementaryUnit` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 65](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L65) | The restricted coefficient map sends an elementary generator to its mapped-coefficient generator. |
| `Matrix.GeneralLinearGroup.mapElementarySubgroup_id` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 76](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L76) | Identity ring hom induces the identity restricted elementary map. |
| `Matrix.GeneralLinearGroup.mapElementarySubgroup_comp` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 83](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L83) | Composition of ring homs agrees with composition of restricted elementary maps. |
| `Matrix.GeneralLinearGroup.relativeElementaryGenerators` | def | [GeneralLinearGroups/RelativeElementary.lean, line 91](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L91) | Elementary generators with coefficients in `I`, viewed as members of `E(R)`. |
| `Matrix.GeneralLinearGroup.relativeElementarySubgroup` | def | [GeneralLinearGroups/RelativeElementary.lean, line 98](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L98) | The normal closure of the ideal-coefficient generators **inside** `E(R)`. |
| `Matrix.GeneralLinearGroup.elementaryUnit_mem_relativeElementarySubgroup` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 103](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L103) | Every ideal-coefficient elementary unit belongs to the relative subgroup. |
| `Matrix.GeneralLinearGroup.relativeElementarySubgroup_normal` | instance | [GeneralLinearGroups/RelativeElementary.lean, line 109](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L109) | The relative subgroup is normal inside the absolute elementary group. |
| `Matrix.GeneralLinearGroup.relativeElementarySubgroup_mono` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 115](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L115) | Enlarging the ideal enlarges its relative elementary subgroup. |
| `Matrix.GeneralLinearGroup.relativeElementarySubgroup_bot` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 123](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L123) | The zero ideal has trivial relative elementary subgroup, including in rank zero or one. |
| `Matrix.GeneralLinearGroup.relativeElementarySubgroup_le_congruenceSubgroup` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 133](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L133) | Relative elementary elements reduce to the identity modulo their ideal. |
| `Matrix.GeneralLinearGroup.relativeElementarySubgroup_map_subtype_le_congruenceSubgroup` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 151](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L151) | The image of the relative group in the ambient GL lies in the existing congruence kernel. This is an image inclusion, not a claim of ambient normality. |
| `Matrix.GeneralLinearGroup.mapElementarySubgroup_relativeElementarySubgroup_le` | theorem | [GeneralLinearGroups/RelativeElementary.lean, line 161](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeElementary.lean#L161) | Compatible coefficient maps carry relative elementary groups into relative elementary groups, without any surjectivity assumption. |
| `Matrix.GeneralLinearGroup.upperUnit_zero` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 30](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L30) | The upper block unit with zero off-diagonal block is the identity. |
| `Matrix.GeneralLinearGroup.lowerUnit_zero` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 36](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L36) | The lower block unit with zero off-diagonal block is the identity. |
| `Matrix.GeneralLinearGroup.upperUnit_add` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 42](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L42) | Upper block units turn matrix addition into group multiplication. |
| `Matrix.GeneralLinearGroup.lowerUnit_add` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 48](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L48) | Lower block units turn matrix addition into group multiplication. |
| `Matrix.GeneralLinearGroup.upperUnit_single` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 54](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L54) | A single upper-block entry is an off-block elementary unit. |
| `Matrix.GeneralLinearGroup.lowerUnit_single` | theorem | [GeneralLinearGroups/ElementaryWhitehead.lean, line 63](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryWhitehead.lean#L63) | A single lower-block entry is elementary with coefficient `-c`. |
| `Matrix.GeneralLinearGroup.upperUnit_mem_relativeElementarySubgroup` | theorem | [GeneralLinearGroups/RelativeWhitehead.lean, line 32](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhitehead.lean#L32) | An ideal-valued upper block unit belongs to the doubled relative elementary subgroup; this also holds for an empty index type. |
| `Matrix.GeneralLinearGroup.lowerUnit_mem_relativeElementarySubgroup` | theorem | [GeneralLinearGroups/RelativeWhitehead.lean, line 71](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhitehead.lean#L71) | An ideal-valued lower block unit belongs to the doubled relative elementary subgroup. Its lower-left block is `-a`, so its elementary generators use `-a i j`. |
| `Matrix.GeneralLinearGroup.blockDiagonalUnit_eq_five` | theorem | [GeneralLinearGroups/RelativeWhitehead.lean, line 110](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhitehead.lean#L110) | The five-factor block identity; `lowerUnit b` has lower-left block `-b`. No ideal hypothesis is needed. |
| `Matrix.GeneralLinearGroup.blockDiagonalUnit_mem_relativeElementarySubgroup` | theorem | [GeneralLinearGroups/RelativeWhitehead.lean, line 137](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhitehead.lean#L137) | The Whitehead diagonal of a congruence unit is relative elementary after doubling, with conjugation only inside the existing elementary subgroup. |
| `Matrix.GeneralLinearGroup.stabilize` | def | [GeneralLinearGroups/ElementaryStabilization.lean, line 36](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L36) | Extend an invertible matrix by an identity block, with no positivity assumption on the sizes of either block. |
| `Matrix.GeneralLinearGroup.stabilize_apply_inl_inl` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 50](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L50) | Stabilization agrees with the original unit on the upper-left block. |
| `Matrix.GeneralLinearGroup.stabilize_apply_inl_inr` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 54](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L54) | Stabilization has zero upper-right block. |
| `Matrix.GeneralLinearGroup.stabilize_apply_inr_inl` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 58](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L58) | Stabilization has zero lower-left block. |
| `Matrix.GeneralLinearGroup.stabilize_apply_inr_inr` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 62](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L62) | Stabilization has the identity lower-right block. |
| `Matrix.GeneralLinearGroup.stabilize_injective` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 66](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L66) | The original matrix can be recovered from the upper-left block. |
| `Matrix.GeneralLinearGroup.mapRingHom_stabilize` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 80](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L80) | Stabilization commutes with entrywise mapping of coefficients. |
| `Matrix.GeneralLinearGroup.stabilize_elementaryUnit` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 97](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L97) | Stabilization sends an elementary generator exactly to the corresponding generator on the first summand. |
| `Matrix.GeneralLinearGroup.stabilize_elementarySubgroup_le` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 107](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L107) | The image of the absolute elementary group under stabilization remains elementary. |
| `Matrix.GeneralLinearGroup.stabilizeElementarySubgroup` | def | [GeneralLinearGroups/ElementaryStabilization.lean, line 121](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L121) | Stabilization restricted to the existing elementary subgroups. |
| `Matrix.GeneralLinearGroup.stabilizeElementarySubgroup_coe` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 129](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L129) | Restricted stabilization has the same ambient value as the unit-group monoid hom. |
| `Matrix.GeneralLinearGroup.stabilizeElementarySubgroup_elementaryUnit` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 134](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L134) | Restricted stabilization evaluates on existing elementary generators. |
| `Matrix.GeneralLinearGroup.stabilize_relativeElementarySubgroup_le` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 148](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L148) | Relative elementary normal closures are preserved by stabilization as an image inclusion, without asserting surjectivity of the restricted map. |
| `Matrix.GeneralLinearGroup.stabilize_congruenceSubgroup_le` | theorem | [GeneralLinearGroups/ElementaryStabilization.lean, line 162](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryStabilization.lean#L162) | Stabilization preserves the existing quotient-reduction congruence kernel. |
| `Matrix.GeneralLinearGroup.stabilize_conj_eq_blockDiagonalUnit_conj` | theorem | [GeneralLinearGroups/RelativeWhiteheadConsequences.lean, line 31](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhiteheadConsequences.lean#L31) | Stabilized conjugation by `g` is conjugation by its elementary Whitehead diagonal, with no congruence assumption on `g`. |
| `Matrix.GeneralLinearGroup.stabilize_commutator_eq_blockDiagonalUnit_mul` | theorem | [GeneralLinearGroups/RelativeWhiteheadConsequences.lean, line 39](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhiteheadConsequences.lean#L39) | The ordered commutator has a three-diagonal factorization after doubling. The final diagonal is indexed by `(h * g)⁻¹`, not `(g * h)⁻¹`. |
| `Matrix.GeneralLinearGroup.stabilize_conj_mem_relativeElementarySubgroup` | theorem | [GeneralLinearGroups/RelativeWhiteheadConsequences.lean, line 47](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhiteheadConsequences.lean#L47) | An arbitrary general linear conjugator preserves relative elementary membership after doubling, in the ambient general linear group. |
| `Matrix.GeneralLinearGroup.stabilize_commutator_mem_relativeElementarySubgroup` | theorem | [GeneralLinearGroups/RelativeWhiteheadConsequences.lean, line 71](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RelativeWhiteheadConsequences.lean#L71) | The ordered commutator of two congruence units is relative elementary after doubling, with no original-rank commutator containment asserted. |
| `Matrix.GeneralLinearGroup.diagonalPairUnit` | def | [GeneralLinearGroups/RectangularBlockUnits.lean, line 35](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L35) | Assembles explicit diagonal GL units over independent finite X and Y using existing stabilization and reindexing; works over Semiring and includes empty blocks. |
| `Matrix.GeneralLinearGroup.diagonalPairUnit_val` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 41](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L41) | The assembled unit is the diagonal block matrix with zero off-diagonal blocks. |
| `Matrix.GeneralLinearGroup.diagonalPairUnit_inv` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 56](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L56) | The inverse is the diagonal pair of the supplied inverse units. |
| `Matrix.GeneralLinearGroup.diagonalPairUnit_one_right` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 64](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L64) | An identity right block recovers the existing stabilization map. |
| `Matrix.GeneralLinearGroup.diagonalPairUnit_one_left` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 70](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L70) | An identity left block recovers reindexed stabilization of the right unit. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit` | def | [GeneralLinearGroups/RectangularBlockUnits.lean, line 82](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L82) | Upper off-block unipotent GL unit for rectangular C over any Ring; its inverse has block -C. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit_val` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 89](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L89) | Reads the upper off-diagonal C and identity diagonal blocks. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit_inv` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 113](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L113) | The inverse upper unit has off-block -C. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit_zero` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 119](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L119) | The zero rectangular block gives the identity unit. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit_add` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 125](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L125) | Addition of rectangular blocks becomes ordered multiplication of upper units. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit_single` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 131](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L131) | A single off-block entry is the existing elementary generator. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit_mem_elementarySubgroup` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 140](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L140) | Every upper rectangular unit lies in the existing finite elementary subgroup, including empty-block cases. |
| `Matrix.GeneralLinearGroup.triangularUnit` | def | [GeneralLinearGroups/RectangularBlockUnits.lean, line 153](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L153) | Uses explicit diagonal units A and D and ordered B * D⁻¹ to assemble an upper triangular unit over any Ring. |
| `Matrix.GeneralLinearGroup.triangularUnit_eq_upper_mul_diagonal` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 158](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L158) | First factorization is upper unit of B * D⁻¹ times the diagonal pair. |
| `Matrix.GeneralLinearGroup.triangularUnit_val` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 165](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L165) | Reads the upper triangular block matrix A, B, 0, D. |
| `Matrix.GeneralLinearGroup.triangularUnit_eq_diagonal_mul_upper` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 175](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L175) | Complementary ordered factorization is diagonal pair times upper unit of A⁻¹ * B. |
| `Matrix.GeneralLinearGroup.triangularUnit_inv_val` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 190](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L190) | Ordered inverse off-block is -(A⁻¹ * B * D⁻¹), not a reversed or unsigned product. |
| `Matrix.GeneralLinearGroup.map_triangularUnit_eq_diagonalPairUnit` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 205](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L205) | A group hom killing E forgets the off-block, with no abelian-target or ambient-normality hypothesis. |
| `Matrix.GeneralLinearGroup.rectangularUpperUnit_eq_upperUnit` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 217](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L217) | Equal-index rectangular upper units agree with existing Whitehead upperUnit. |
| `Matrix.GeneralLinearGroup.diagonalPairUnit_inv_pair` | theorem | [GeneralLinearGroups/RectangularBlockUnits.lean, line 223](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/RectangularBlockUnits.lean#L223) | Equal-index inverse diagonal pairs agree with existing blockDiagonalUnit. |
| `Ideal.principalUnitsQuotientEquiv` | def | [GeneralLinearGroups/PrincipalUnits.lean, line 212](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L212) | For arbitrary left ideals in a Ring with I^2 contained in J and I contained in the Jacobson radical, the quotient of original units principal modulo I by the coordinate kernel is the additive layer I/(I intersect J), written multiplicatively. The inverse on a representative is the original-ring unit with value 1+x. |
| `Ideal.principalUnitsToQuotient_ker` | theorem | [GeneralLinearGroups/PrincipalUnits.lean, line 175](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L175) | Under I^2 contained in J alone, the coordinate kernel is the relative J-stabilizer inside the I-stabilizer. Its normality is derived, not assumed; no J contained in I or two-sidedness is needed. |
| `Ideal.commutator_stabilizer_quotient_one_le` | theorem | [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 135](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L135) | For arbitrary left ideals A, B in any Ring, including noncommutative and zero rings, the commutator of their principal-unit subgroups lies in the principal units at A*B+B*A. Principal units use the stock R-unit stabilizer of 1 in the quotient left module R/I; for two-sided I this agrees with the kernel of reduction on units to the quotient ring. The commutator inclusion requires neither two-sidedness nor ambient normality. |
| `Ideal.commutator_stabilizer_quotient_one_pow_le` | theorem | [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 215](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L215) | For a two-sided ideal I in a Ring, the commutator of principal units at I^a and I^b lies in those at I^(a+b) for all natural indices a, b, including zero. No nilpotence assumption is imposed; two-sidedness is required for this all-index bound. |
| `Ideal.stabilizer_quotient_one_lowerCentralSeries_le_pow` | theorem | [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 229](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L229) | For any left ideal I in a Ring and k a natural number, the kth lower central term of its principal-unit subgroup, computed in the ambient unit group, lies in the principal units at I^(k+1). The zeroth term is the principal-unit subgroup itself; no two-sidedness or ambient normality is assumed. |
| `Ideal.stabilizer_quotient_one_lowerCentralSeries_eq_bot_of_pow_eq_bot` | theorem | [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 249](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L249) | If a left ideal I in a Ring satisfies I^N=bot, the lower central series of its principal-unit subgroup is bot at index N-1, using natural subtraction. N=0 and N=1 are included and give a trivial zeroth term. |
| `Ideal.isNilpotent_stabilizer_quotient_one_of_pow_eq_bot` | theorem | [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 267](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L267) | For any left ideal I in a Ring with I^N=bot, its principal-unit subgroup is a nilpotent group. This includes N=0 and N=1 and asserts no nilpotence of the full ambient unit group. |
| `Ideal.nilpotencyClass_stabilizer_quotient_one_le_of_pow_eq_bot` | theorem | [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 278](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L278) | For any left ideal I in a Ring with I^N=bot, the nilpotency class of its principal-unit subgroup is at most N-1, using natural subtraction. Nilpotence is supplied by isNilpotent_stabilizer_quotient_one_of_pow_eq_bot; N=0 and N=1 give the trivial subgroup and class zero. |
| `Ideal.mem_map_stabilizer_quotient_one_iff` | theorem | [GeneralLinearGroups/PrincipalUnits/Images.lean, line 45](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Images.lean#L45) | For a ring homomorphism f from a Ring R to a Ring S in independent universes and a left ideal I contained in Ideal.jacobson bot, a unit u of S lies in the image under Units.map f.toMonoidHom of the original R-unit stabilizer of [1] in the quotient left module R/I if and only if there is a in I with f(a) = u - 1. This is the set image of ideal elements, not membership in Ideal.map f I; neither injectivity of f nor commutativity of either ring is required, and there is no domain, local-ring or valuation hypothesis. |
| `RingHom.unitsKerEquivOfSquareZero` | def | [GeneralLinearGroups/SquareZeroUnits.lean, line 59](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/SquareZeroUnits.lean#L59) | Square-zero kernel, Ring domain and Semiring codomain; algebraic unit coordinates, not a quotient-unit lifting theorem. |
| `DualNumber.fstRingHom_ker_sq` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 38](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L38) |  |
| `Matrix.DualNumberKernels.unitsKerEquiv_eq_unitsKerEquivOfSquareZero_symm` | theorem | [GeneralLinearGroups/DualNumberSquareZeroUnits.lean, line 36](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberSquareZeroUnits.lean#L36) | Pointwise comparison on every coefficient through the canonical inr inclusion. |
| `DualNumber.mapRingHom` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 44](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L44) |  |
| `Matrix.DualNumberKernels.glKerEquiv` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 145](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L145) |  |
| `Matrix.DualNumberKernels.unitsKerEquiv` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 250](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L250) |  |
| `Matrix.DualNumberKernels.det_liftMatrix` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 291](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L291) |  |
| `Matrix.DualNumberKernels.detKer` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 305](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L305) |  |
| `Matrix.DualNumberKernels.detKer_glKerEquiv` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 316](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L316) |  |
| `Matrix.DualNumberKernels.slKerEquiv` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 374](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L374) |  |
| `Matrix.DualNumberKernels.slToGL` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 337](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L337) |  |
| `Matrix.DualNumberKernels.slToGL_slKerEquiv` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 409](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L409) |  |
| `Matrix.DualNumberKernels.glKernel_mul_comm` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 169](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L169) |  |
| `Matrix.DualNumberKernels.slKernel_mul_comm` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 403](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L403) |  |
| `Matrix.DualNumberKernels.glKerMap` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 421](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L421) |  |
| `Matrix.DualNumberKernels.slKerMap` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 445](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L445) |  |
| `Matrix.DualNumberKernels.unitsKerMap` | def | [GeneralLinearGroups/DualNumberKernels.lean, line 433](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L433) |  |
| `Matrix.DualNumberKernels.glKerMap_glKerEquiv` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 489](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L489) |  |
| `Matrix.DualNumberKernels.slKerMap_slKerEquiv` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 511](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L511) |  |
| `Matrix.DualNumberKernels.unitsKerMap_unitsKerEquiv` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 500](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L500) |  |
| `Matrix.DualNumberKernels.detKer_natural` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 522](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L522) |  |
| `Matrix.DualNumberKernels.slToGL_natural` | theorem | [GeneralLinearGroups/DualNumberKernels.lean, line 531](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernels.lean#L531) |  |
| `Matrix.DualNumberKernels.slAdjoint` | def | [GeneralLinearGroups/DualNumberKernelAdjoint.lean, line 29](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernelAdjoint.lean#L29) |  |
| `Matrix.DualNumberKernels.slAdjoint_val` | theorem | [GeneralLinearGroups/DualNumberKernelAdjoint.lean, line 48](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernelAdjoint.lean#L48) |  |
| `Matrix.DualNumberKernels.glKerEquiv_conj` | theorem | [GeneralLinearGroups/DualNumberKernelAdjoint.lean, line 114](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernelAdjoint.lean#L114) |  |
| `Matrix.DualNumberKernels.glReadback_conj` | theorem | [GeneralLinearGroups/DualNumberKernelAdjoint.lean, line 136](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernelAdjoint.lean#L136) |  |
| `Matrix.DualNumberKernels.slToGL_conj` | theorem | [GeneralLinearGroups/DualNumberKernelAdjoint.lean, line 147](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernelAdjoint.lean#L147) |  |
| `Matrix.DualNumberKernels.slReadback_conj` | theorem | [GeneralLinearGroups/DualNumberKernelAdjoint.lean, line 158](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernelAdjoint.lean#L158) |  |
| `Matrix.DualNumberKernels.glKerMap_conj` | theorem | [GeneralLinearGroups/DualNumberKernelAdjoint.lean, line 173](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberKernelAdjoint.lean#L173) |  |
| `Steinberg.Presented` | abbrev | [GeneralLinearGroups/Steinberg.lean, line 58](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L58) |  |
| `Steinberg.generator_add` | theorem | [GeneralLinearGroups/Steinberg.lean, line 65](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L65) |  |
| `Steinberg.generator_commutator_disjoint` | theorem | [GeneralLinearGroups/Steinberg.lean, line 91](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L91) |  |
| `Steinberg.generator_commutator` | theorem | [GeneralLinearGroups/Steinberg.lean, line 99](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L99) |  |
| `Steinberg.generator_commutator_reverse` | theorem | [GeneralLinearGroups/Steinberg.lean, line 112](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L112) |  |
| `Steinberg.lift` | def | [GeneralLinearGroups/Steinberg.lean, line 121](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L121) |  |
| `Steinberg.lift_generator` | theorem | [GeneralLinearGroups/Steinberg.lean, line 141](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L141) |  |
| `Steinberg.hom_ext` | theorem | [GeneralLinearGroups/Steinberg.lean, line 148](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L148) |  |
| `Steinberg.lift_unique` | theorem | [GeneralLinearGroups/Steinberg.lean, line 155](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L155) |  |
| `Steinberg.toElementary` | def | [GeneralLinearGroups/Steinberg.lean, line 174](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L174) |  |
| `Steinberg.toElementary_surjective` | theorem | [GeneralLinearGroups/Steinberg.lean, line 206](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L206) |  |
| `Steinberg.toGL_range` | theorem | [GeneralLinearGroups/Steinberg.lean, line 217](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/Steinberg.lean#L217) |  |
| `Matrix.DualNumberMixedCommutator.innerConstant` | def | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 28](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L28) |  |
| `Matrix.DualNumberMixedCommutator.innerPure` | def | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 32](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L32) |  |
| `Matrix.DualNumberMixedCommutator.epsilonLiftGL` | def | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 36](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L36) |  |
| `Matrix.DualNumberMixedCommutator.etaLiftGL` | def | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 46](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L46) |  |
| `Matrix.DualNumberMixedCommutator.epsilonLiftGL_val` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 51](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L51) |  |
| `Matrix.DualNumberMixedCommutator.epsilonLiftGL_inv_val` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 56](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L56) |  |
| `Matrix.DualNumberMixedCommutator.etaLiftGL_val` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 62](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L62) |  |
| `Matrix.DualNumberMixedCommutator.etaLiftGL_inv_val` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 67](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L67) |  |
| `Matrix.DualNumberMixedCommutator.epsilon_reduce` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 140](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L140) |  |
| `Matrix.DualNumberMixedCommutator.eta_reduce` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 148](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L148) |  |
| `Matrix.DualNumberMixedCommutator.epsilon_eta_commutator` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 154](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L154) |  |
| `Matrix.DualNumberMixedCommutator.mixedKernel` | def | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 180](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L180) |  |
| `Matrix.DualNumberMixedCommutator.mixedKernel_val` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 184](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L184) |  |
| `Matrix.DualNumberMixedCommutator.mixedKernel_readback` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 190](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L190) |  |
| `Matrix.DualNumberMixedCommutator.mixedKernel_fst` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 198](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L198) |  |
| `Matrix.DualNumberMixedCommutator.mixedKernel_snd_fst` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 205](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L205) |  |
| `Matrix.DualNumberMixedCommutator.mixedKernel_snd_snd` | theorem | [GeneralLinearGroups/DualNumberMixedCommutator.lean, line 212](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedCommutator.lean#L212) |  |
| `Matrix.DualNumberMixedSLCommutator.innerPureSL` | def | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 29](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L29) |  |
| `Matrix.DualNumberMixedSLCommutator.epsilonLiftSL` | def | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 38](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L38) |  |
| `Matrix.DualNumberMixedSLCommutator.etaLiftSL` | def | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 44](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L44) |  |
| `Matrix.DualNumberMixedSLCommutator.epsilonLiftSL_val` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 49](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L49) |  |
| `Matrix.DualNumberMixedSLCommutator.etaLiftSL_val` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 54](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L54) |  |
| `Matrix.DualNumberMixedSLCommutator.epsilonLiftSL_toGL` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 62](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L62) |  |
| `Matrix.DualNumberMixedSLCommutator.etaLiftSL_toGL` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 68](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L68) |  |
| `Matrix.DualNumberMixedSLCommutator.epsilonLiftSL_reduce` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 74](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L74) |  |
| `Matrix.DualNumberMixedSLCommutator.etaLiftSL_reduce` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 87](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L87) |  |
| `Matrix.DualNumberMixedSLCommutator.epsilon_eta_SL_commutator` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 93](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L93) |  |
| `Matrix.DualNumberMixedSLCommutator.mixedSLKernel` | def | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 108](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L108) |  |
| `Matrix.DualNumberMixedSLCommutator.mixedSLKernel_val` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 113](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L113) |  |
| `Matrix.DualNumberMixedSLCommutator.mixedSLKernel_readback` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 119](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L119) |  |
| `Matrix.DualNumberMixedSLCommutator.mixedSLKernel_snd_snd` | theorem | [GeneralLinearGroups/DualNumberMixedSLCommutator.lean, line 126](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/DualNumberMixedSLCommutator.lean#L126) |  |
| `Matrix.GeneralLinearGroup.reindexEquiv_mem_elementarySubgroup` | theorem | [GeneralLinearGroups/UnitPivotDiagonalization.lean, line 41](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UnitPivotDiagonalization.lean#L41) | Ring-level reindexing of the existing elementary subgroup. |
| `Matrix.leadingPrincipalMinor` | def | [GeneralLinearGroups/UnitPivotDiagonalization.lean, line 162](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UnitPivotDiagonalization.lean#L162) | Ordered Fin.castLE minor, including the empty minor. |
| `Matrix.exists_elementary_diagonalization_of_unit_leadingPrincipalMinors` | theorem | [GeneralLinearGroups/UnitPivotDiagonalization.lean, line 424](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UnitPivotDiagonalization.lean#L424) | Two-sided elementary reduction under all positive unit leading minors over a CommRing. |
| `Matrix.exists_elementary_diagonalization_of_unit_pivot` | theorem | [GeneralLinearGroups/UnitPivotDiagonalization.lean, line 311](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/UnitPivotDiagonalization.lean#L311) | A unit first pivot lifts an elementary factorization of its Schur residual. |
| `Matrix.GeneralLinearGroup.exists_elementary_diagonalization_local` | theorem | [GeneralLinearGroups/LocalElementaryGeneration.lean, line 92](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalElementaryGeneration.lean#L92) | Invertible matrices over commutative local rings reduce to a unit diagonal without a minor condition, including in rank zero. |
| `Matrix.GeneralLinearGroup.mem_elementarySubgroup_iff_det_eq_one_local` | theorem | [GeneralLinearGroups/LocalElementaryGeneration.lean, line 106](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalElementaryGeneration.lean#L106) | Finite elementary membership is equivalent to determinant one on any finite decidable index type. |
| `Matrix.GeneralLinearGroup.StableGL.elementary_eq_ker_det_local` | theorem | [GeneralLinearGroups/LocalElementaryGeneration.lean, line 130](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalElementaryGeneration.lean#L130) | The stable elementary subgroup is the stable determinant kernel over commutative local rings. |
| `Matrix.GeneralLinearGroup.StableGL.quotientDet_ker_eq_bot_local` | theorem | [GeneralLinearGroups/LocalElementaryGeneration.lean, line 141](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalElementaryGeneration.lean#L141) | The existing quotient determinant has trivial kernel under the local-ring hypothesis. |
| `Matrix.GeneralLinearGroup.StableGL.quotientDetMulEquiv` | def | [GeneralLinearGroups/LocalElementaryGeneration.lean, line 154](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalElementaryGeneration.lean#L154) | The existing quotient determinant and rank-one section form a natural multiplicative equivalence with coefficient units over local rings. |
| `Matrix.GeneralLinearGroup.exists_elementary_transvection_diagonalization_field` | theorem | [GeneralLinearGroups/LocalElementaryGeneration.lean, line 226](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/LocalElementaryGeneration.lean#L226) | Mathlib transvection lists yield elementary GL factors and a unit diagonal for invertible field matrices. |
| `Matrix.GeneralLinearGroup.elementaryUnitPathSubtype` | def | [GeneralLinearGroups/ElementaryPaths.lean, line 74](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryPaths.lean#L74) | Path within the elementary subgroup over a topological Ring. |
| `Matrix.GeneralLinearGroup.elementarySubgroup_pathConnectedSpace` | theorem | [GeneralLinearGroups/ElementaryPaths.lean, line 85](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryPaths.lean#L85) | Subgroup path-connectedness additionally requiring PathConnectedSpace R. |
| `Matrix.GeneralLinearGroup.diagonalUnit_mem_elementarySubgroup` | theorem | [GeneralLinearGroups/ElementaryDiagonal.lean, line 186](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryDiagonal.lean#L186) | Product-one unit diagonal membership over a CommRing, including empty indices. |
| `Matrix.GeneralLinearGroup.mem_elementarySubgroup_of_det_one_of_unit_leadingPrincipalMinors` | theorem | [GeneralLinearGroups/ElementaryDiagonal.lean, line 252](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryDiagonal.lean#L252) | Determinant-one membership requiring separately all positive unit leading minors. |
| `Matrix.SpecialLinearGroup.elementarySubgroup` | def | [GeneralLinearGroups/ElementaryNeighborhood.lean, line 37](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryNeighborhood.lean#L37) | SL comap of the existing GL elementary subgroup, not the GL subgroup itself. |
| `Matrix.SpecialLinearGroup.isOpen_elementarySubgroup` | theorem | [GeneralLinearGroups/ElementaryNeighborhood.lean, line 87](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryNeighborhood.lean#L87) | Openness requiring an open scalar unit locus, not coefficient path-connectedness. |
| `Matrix.SpecialLinearGroup.elementarySubgroup_eq_pathComponentOne` | theorem | [GeneralLinearGroups/ElementaryNeighborhood.lean, line 122](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/ElementaryNeighborhood.lean#L122) | Identity path-component equality requiring both open scalar units and PathConnectedSpace R. |
