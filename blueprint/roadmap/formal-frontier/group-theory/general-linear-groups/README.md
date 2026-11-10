# General linear groups

> Finite general linear groups over possibly noncommutative semirings and rings: Kronecker products of matrix units with reversed identity-factor inverse witnesses, elementary units, ordered commutators, relative normal closures inside elementary groups, finite stabilization, Whitehead block factorization and doubled relative membership and lifting; rectangular block units for independent finite indices with explicit diagonal units; reindexing, nil and quasiregular ideals, congruence subgroups and quotient lifting, nonunital unitization, and matrix trace modulo additive commutators. Scalar unit reflection for Ring-to-Semiring homomorphisms forces quasi-regularity of the canonical two-sided kernel without surjectivity; for surjective maps it is equivalent to this kernel condition. Source and target universes are independent, with no commutativity or local-ring hypothesis. A square-zero kernel of any Ring-to-Semiring homomorphism identifies units mapping to 1 with the additive kernel via u - 1 and 1 + x; the inverse unit has value 1 - x. All mixed kernel products must vanish, with no surjectivity assumption. For left ideals I, J with I^2 contained in J, original-ring principal units map to the additive layer I/(I intersect J); Jacobson containment of I makes the map surjective and identifies its kernel quotient with that layer. Neither two-sidedness nor J contained in I is required. Dual-number GL, SL and scalar-unit reduction kernels, determinant/trace, coefficient maps and the left-conjugation adjoint action use commutative rings. The trace quotient is an additive group, not a quotient ring; its corner inverse requires a chosen matrix index. A Steinberg presentation adds elementary-symbol relations, universal lifts and a finite map onto the elementary subgroup, without opposite-root or central-extension assertions. Over iterated dual numbers, Mathlib's GL units have an ordered commutator equal to the mixed lift of the associative matrix bracket; its outer reduction-kernel element has complete pure-inner readback. For trace-zero inputs, the refinement in Mathlib's SL group uses special-linear factors, identifies the ordered mixed commutator and reads back its pure-inner trace-zero coefficient in the outer SL kernel. Elementary unit-pivot diagonalization, product-one diagonal membership, continuous elementary paths and finite special-linear elementary neighborhoods add algebraic and topological interfaces with their respective unit-minor, path-connectedness and open-scalar-unit hypotheses. Zero-product rectangular blocks over any ring yield a unit 1 + AB whose stabilization is an elementary ordered commutator of block shears. Stable general linear groups form a direct limit over semirings; over rings their stable elementary subgroup is perfect and equals the commutator subgroup, with quotient canonically the abelianization. Over commutative rings the stable determinant and its quotient and abelianization factorizations admit rank-one sections; the elementary subgroup lies in the determinant kernel. Ordered products of matrices with entries in a left ideal I over a semiring have entries in I raised to the list length, for independent finite decidable indices, including empty lists and indices. Repeated factors recover the matrix-power bound. Any exponent annihilating the whole ideal also annihilates a matrix whose entries lie in it.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

6 articles: 5 for highlights of its formalization.yaml whose declarations the scan finds and 1 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups), read at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “independent agent review; no human mathematical review claimed”.
- Review notes: “Reviews and build evidence concern specific revisions. No complete Weibel source correspondence or source formalization is asserted.”
- Automation: agent; framework “AI agents using Lean and Lake”; tool setup “Formal Frontier Agents developed Lean proofs and ordinary-import clients using mathlib APIs, compiler feedback and Lake. The clients exercise the public interfaces and degenerate examples; the historical API reference does not enumerate all present results.”; prompting notes “AI-assisted formalization states hypotheses explicitly and uses kernel-checked Lean proofs.”
- Automation notes: “AI agents produced code, proofs and documentation with compiler feedback; no human mathematical review or source-author endorsement is asserted. AI generation alone does not establish originality, copyright ownership or third-party redistribution rights.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- [The K-book: An Introduction to Algebraic K-theory](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf), Charles A. Weibel, Complete-book edition (August 29, 2013): Exercises I.1.10-I.1.12; Chapter II, section 2, trace discussion on displayed page 73 (physical PDF page 81) (book; adapts).
- [Local Fields and Their Extensions](https://ivanfesenko.org/wp-content/uploads/2021/10/vol.pdf), I. B. Fesenko, S. V. Vostokov, Second edition (2002), Chapter I, (5.3) and (5.4)(3) (book; adapts).

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

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/README.md#headline-results) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

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

**Finite coefficient products of stable groups and elementary quotients.**
For arbitrary `Semiring R` and `Semiring S` in independent universes,
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

Its formalization.yaml lists 221 main results, and the scan finds 221 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
