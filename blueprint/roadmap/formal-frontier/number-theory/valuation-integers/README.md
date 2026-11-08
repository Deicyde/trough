# Valuation integers

> Power divisibility and a Krull-dimension bound for the integers of a rank-at-most-one valuation, a converse producing rank data from a dimension bound, and intersections of valuation subrings with full residue-field maps. Every finite separable extension of the original residue field is realized by a compatible finite simple field extension of the same degree, with a base-compatible residue isomorphism and corresponding power-basis generators. Finite rank-at-most-one intersections have classified primes, dimension at most one and finite spectra whose nonempty opens contain zero. Finite pairwise inequivalent rank-one intersections have a separately hypothesized generic-point fork homeomorphism. Equivalent surjective valuations of a ring into a common cyclic-unit linearly ordered commutative group with zero are equal. A canonical rank-at-most-one valuative topology detects values less than one by convergence of powers; for division rings, the specified identity homeomorphism recognizes equivalence of two rank-at-most-one valuations. Valuations of rank at most one on division rings also have a real absolute-value construction using the specified rank embedding, with comparison lemmas including trivial valuations. Rank-one valuations give nontrivial absolute values, and the associated absolute values are equivalent exactly when the valuations are, even for different ambient value groups. Dense compatible valued-field extensions induce dense integer algebra maps and bijective residue maps, specializing to a reduction-compatible residue equivalence for the uniform completion at arbitrary valuation rank. A dense ring homomorphism preserving raw values exactly identifies the canonical completion of a valued field with a complete separated valued ring over an arbitrary common value group. Dense exactly value-preserving additive maps of valued rings induce uniformities. Bounded submodules of finite-dimensional normed spaces over complete fields are finitely generated over Noetherian coefficient rings whose images contain the norm unit ball, with an extension-integer application. At a positive even index 2k and a prime p with p - 1 dividing 2k, the divided Bernoulli number B_(2k)/(2k) has additive p-adic valuation -1 - v_p(2k) and positive reduced denominator exponent 1 + v_p(2k). For every integer n and positive natural k, the rational expression n^k * (n^k - 1) * (bernoulli k / k) is integral over the integers. More generally, if n^k * (n^k - 1) * q is integral for every natural n, every prime p in the reduced denominator of q satisfies p - 1 divides k. This includes k = 0 and applies to divided Bernoulli numbers at every index. For Henselian valuation integers, a sharp power-root neighborhood has an exact correction value, and the stock power range in the canonical units topology is open when the exponent has nonzero image in the field. For a valuation v on a field with any linearly ordered commutative value group with zero, assume v.valuationSubring is Henselian at its maximal ideal m. For a polynomial f over that subring and a in it, a strict squared-derivative value inequality gives a root b, the exact error/displacement identity, derivative-value equality and uniqueness throughout the original derivative ball. For every natural s, f(a) in m^(2*s+1) and f'(a) not in m^(s+1) give all these conclusions and b-a in m^(s+1), without completeness, rank, discreteness, Noetherianity, monicity or unit-derivative assumptions. For e, d, z in that subring, two algebraic comparisons require no Henselianity: e in m^(2*s+1) and d not in m^(s+1) imply v(e) < v(d)^2, and under the same hypotheses the identity v(e) = v(d) * v(z) implies z in m^(s+1).

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/formalization.yaml) of [FormalFrontier/valuation-integers](https://github.com/FormalFrontier/valuation-integers) at commit [212f1a04](https://github.com/FormalFrontier/valuation-integers/tree/212f1a045abb1dfb6e6da1796d16433db6d72d74), Apache-2.0.*

5 articles: 5 for highlights of its formalization.yaml whose declarations the scan finds. The headline results in its README are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/valuation-integers](https://github.com/FormalFrontier/valuation-integers), read at commit [212f1a04](https://github.com/FormalFrontier/valuation-integers/tree/212f1a045abb1dfb6e6da1796d16433db6d72d74) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “partially-agent-reviewed”.
- Review notes: “The power, dimension, rigidity, topology and intersection results and their clients have independent agent review, as do the real absolute-value definition and theorem statements and the completion-residue definition and headline statements. No human review or source-coverage assessment is claimed. The power-neighborhood statements and proofs, including their independent two-adic inputs and clients, have independent agent review.”
- Automation: agent; framework “Lean 4”; tool setup “Agent-assisted Lean proof development and ordinary-import clients.”; prompting notes “Formal Frontier agents developed proof expressions and examples using mathlib; the module guides distinguish original work and adaptations.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Valuation integers: power divisibility, dimension bound and rank converse* (original-proof; other).
- *Local Fields and Their Extensions*, I. B. Fesenko, S. V. Vostokov, Second edition (2002), Chapter I, (3.5)–(3.6), (4.2)–(4.4), (4.5)(1); Chapter II, §1, Corollary 4 and subsequent Remark, and §2 (book; adapts).
- *Local Fields and Their Extensions*, I. B. Fesenko, S. V. Vostokov, Second edition (2002), Chapter II, §1, Corollary 3, p. 37 (book; adapts).
- *Vector Bundles and K-Theory*, Allen Hatcher, Version 2.2 (November 2017), §4.1, Lemma 4.12, printed p. 117, and the following argument in the proof of Theorem 4.9 (book; adapts).

## Builds on

- [Adic modules](../../commutative-algebra/adic-modules/README.md) (a Lake dependency, pinned at 2fb498d1)
- [Coherent modules](../../commutative-algebra/coherent-modules/README.md) (a Lake dependency, pinned at 0bcb335a)
- [Finite-group Tate cohomology](../../homological-algebra-and-category-theory/finite-group-tate-cohomology/README.md) (a Lake dependency, pinned at c0c9d563)
- [General linear groups](../../group-theory/general-linear-groups/README.md) (a Lake dependency, pinned at ad7c50a0)
- [Group theory](../../group-theory/group-theory/README.md) (a Lake dependency, pinned at 4791da69)
- [Multivariate polynomials](../../commutative-algebra/multivariate-polynomials/README.md) (a Lake dependency, pinned at 5d58abb9)
- [Norm forms](../norm-forms/README.md) (a Lake dependency, pinned at 81579a76)
- [Projective modules](../../ring-theory/projective-modules/README.md) (a Lake dependency, pinned at 78b30587)
- [Spectral Stone duality](../../topology/spectral-stone-duality/README.md) (a Lake dependency, pinned at d7dad16f)

## Highlights

- [Prescribed finite separable residue extensions](prescribed-finite-separable-residue-extensions.md)
- [Residue degree bounded by field degree](residue-degree-bounded-by-field-degree.md)
- [Unique residue and field homomorphism lifts](unique-residue-and-field-homomorphism-lifts.md)
- [A sharp Hensel criterion at arbitrary valuation rank](a-sharp-hensel-criterion-at-arbitrary-valuation.md)
- [Unit norms over Henselian valuation domains](unit-norms-over-henselian-valuation-domains.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/README.md#headline-results) of [FormalFrontier/valuation-integers](https://github.com/FormalFrontier/valuation-integers) at commit [212f1a04](https://github.com/FormalFrontier/valuation-integers/tree/212f1a045abb1dfb6e6da1796d16433db6d72d74), Apache-2.0.*

**Automorphism groups and Galois extensions from residue extensions.** Let `R`
be a Henselian valuation domain with fraction field `F`, and let a local
commutative `R`-algebra `S` embed in a finite extension `L/F`. With compatible
algebra and residue-field actions, suppose the residue degree equals `[L : F]`.
For a separable residue extension, `ValuationRing.residueAutEquivOfFinrankEq`
canonically identifies the field and residue algebra-automorphism groups;
its forward map is restriction and reduction, and its inverse is characterized
by the residue and ambient field squares on every element of `S`. See
[`ValuationIntegers.Valuation.ResidueAut`](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueAut.lean).
If the residue extension is Galois, then `L/F` is Galois; if its
algebra-automorphism group is also cyclic, so is that of `L/F`.
A finite residue field of `R` suffices for both conclusions. See
[`ValuationIntegers.Valuation.ResidueGalois`](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueGalois.lean).

**Scalar multiples of units from independent reductions.** Let `R` be a valuation
domain with fraction field `F`, and let `S` be a local commutative `R`-algebra.
With compatible algebra and residue-field actions, an `F`-basis of a ring `L`
formed by images of elements of `S` whose reductions are linearly independent
over the residue field of `R` expresses every `x : L` as a scalar times the image
of a unit of `S`. The basis index may be arbitrary and `S → L` need not be
injective. See `Module.Basis.exists_isUnit_mul_of_linearIndependent_residue` in
[`ValuationIntegers.Valuation.ResidueUnits`](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueUnits.lean).

The valuation API below uses the dependencies credited in the [references](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/README.md#references).
The generic Henselian-pair estimates come from Adic Modules, positive-power comparison
and polynomial-root inverse-image criteria from Group Theory, and the generic-point
space from Spectral Stone Duality; their valuation applications are developed here.

**Polynomial root-value bounds and inverse images.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/PolynomialValueBounds.lean),
[details](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#polynomial-root-values-and-multiplicative-images)).
Let `D,E` be possibly noncommutative semirings, `f : D →+* E`, and
`ν : E →*₀ Γ` satisfy the max-addition inequality, with `Γ` a linearly ordered
commutative monoid with zero. For an `eval₂ f` root, source-supported coefficient
values bounded by the nonzero mapped leading (respectively constant) value give
`ν x ≤ 1` (respectively `1 ≤ ν x`). With coefficient values at most one, leading
(respectively constant) value one gives the same bound, even if `0 = 1` in `Γ`;
both give `ν x = 1`. No injectivity, coefficient commutation or nonzero root is assumed.
Separately, [Group Theory’s generic criteria](https://github.com/FormalFrontier/group-theory/blob/5b7fccf66358d844869aaefd320f5768f6306cd3/GroupTheory/Algebra/Polynomial/Units.lean)
show that any multiplication-only map `μ : E → T` to an arbitrary monoid sends
a root to a left-invertible element if the mapped constant has a supplied left
inverse; the root image is a unit iff it is right-regular. A left inverse alone
is not a unit in general. Raw unit-constant roots have left inverses over semirings
(hypotheses that force a ring structure); genuinely nonring evaluations are possible
for the generic mapped theorem.

**Finitely many distinct polynomial-root values.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/PolynomialValues.lean),
[details](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#polynomial-root-values-and-multiplicative-images)).
Under the same valuation-like semiring hypotheses, one source-supported coefficient
of nonzero image value bounds the number of distinct root values, including zero,
by the number of positive-degree supported coefficients of nonzero value, hence by
`p.natDegree`. If `A` is the nonempty set of all such active coefficient indices,
the nonzero root values number at most `A.card - 1`; add the zero-value occurrence
for the total bound. Finiteness for nonzero polynomials over a division semiring
also includes collapsed value targets. These count values, not roots or multiplicities.

**Restriction, equivalence and canonical extensions.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#restriction-equivalence-and-canonical-extensions)).
On a division ring, valuations into independent linearly ordered commutative monoids with zero
are equivalent iff their strict unit cuts agree, or iff their zero fibers and closed
unit cuts agree. For a map of arbitrary rings whose range contains a positive power
of every target element, restriction is injective for a fixed value monoid and
reflects equivalence for different value monoids, without injectivity or surjectivity
of the ring map. Purely inseparable field-algebra domains specialize this result.
For fields `F,E`, if every `x : E` has a positive power in the scalar image of `F`,
each valuation subring of `F` has a unique extension to `E`: its integral closure.
Membership is integrality, or scalar membership after any specified positive power;
purely inseparable field extensions supply the power witnesses.

**Compatible valuation-ring extensions and prescribed residue fields.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueExtension.lean)).
Along a field homomorphism, a chosen extension valuation subring restricts to
the original valuation ring and preserves every value-order comparison on the
base field, without identifying value groups. The original local coefficient
map induces a commuting residue map. For any finite separable extension of
the original residue field, a lifted primitive-generator polynomial gives a
finite separable simple field extension of the same degree, an integral generator
in its chosen valuation subring, and a base-compatible isomorphism from the given
extension to its residue field. The selected power-basis generators correspond
under reduction. No Henselianity,
discreteness or completeness hypothesis is imposed.

**Scalar-trivial values and valuation-separated linear independence.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#scalar-values-and-linear-independence)).
In a ring algebra over a commutative ring, a valuation into a linearly ordered commutative
monoid with zero that is trivial on nonzero scalars takes integral elements to zero
or one. Over a field, scalar values at most one give the same conclusion for
algebraic elements; a nonzero polynomial with all supported coefficients of value
one suffices locally. For a field `F`, ring `F`-algebra `A` and valuation `v`, a
family with nonzero values in pairwise distinct scalar-weighted value classes is
linearly independent. In particular, `v x ≠ 0` and separation of `(v x)^n` from
every nonzero scalar value for `0 < n < d` make the first `d` powers independent;
if `A` is finite over `F`, then `d ≤ Module.finrank F A`. No domain on `A` or
group structure on the value monoid is needed.

**Residue degree bounded by field degree.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueDegree.lean)).
Let `R` be a valuation domain with fraction field `F`, `L/F` a finite field
extension, and `S` a commutative local `R`-algebra whose given `algebraMap S L`
is injective, with commuting `R/F/L` and `R/S/L` scalar towers. Write `κR`, `κS`
for the original residue fields. The given `κR`- and `R`-algebra structures
on `κS` satisfy the `R/κR/κS` and `R/S/κS` towers; the residue square follows
from these towers, rather than being an extra premise.
`ValuationRing.finite_residueField` gives finite residue degree, and
`ValuationRing.finrank_residueField_le` gives `[κS : κR] ≤ [L : F]`.
Residue finiteness is a conclusion, not an input, and means finite degree,
not finite cardinality. The domain structure on `S` and its flatness over `R`
are derived from the embeddings and valuation-domain structure.
No valuation-ring structure on `S`, fraction-field structure for `S → L`,
or explicit local-map hypothesis on `R → S` is assumed. Universes are independent;
no Henselianity, completeness, discreteness, separability, residue perfection
or common value group is required.

**Prescribed residue lifts give field and ring bases.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueBasis.lean)).
Let `R` be a valuation domain with fraction field `F`, `L/F` a finite field
extension, and `S` a commutative local `R`-algebra with its given injective
`algebraMap S L`. Retain the original `R/S/F/L` algebras and actions, with
commuting `R/F/L` and `R/S/L` scalar towers, and the given `κR`- and
`R`-algebra structures on `κS`, with both `R/κR/κS` and `R/S/κS` towers.
These two residue towers imply the residue square and localness of the
original `R → S` map; neither is an extra premise.
Given a `κR`-basis `b : ι → κS` indexed by a finite type, prescribed lifts
`s : ι → S`, and reduction equations
`residue S (s i) = b i`, assume `card ι = [L : F]`.
`ValuationRing.basisOfResidue` constructs an `F`-basis of `L` with vectors
`algebraMap S L (s i)`, and `ValuationRing.integralBasisOfResidue` constructs
an `R`-basis of `S` with vectors `s i`, for the given actions and maps.
An element of `L` lies in the image of `S → L` iff every field coordinate
lies in the image of `R → F`; it lies in the image of the maximal ideal of
`S` iff every coordinate lies in the image of the maximal ideal of `R`.
For finite sums `∑ i, a i • algebraMap S L (s i)`, the same range and
maximal-ideal criteria test the coefficients `a i` directly. These two
criteria need neither finite ambient dimension nor `card ι = [L : F]`,
while retaining the finite index, given residue basis, prescribed lifts and
reductions, and all original maps, towers and injectivity of `S → L`.
Ring and field coordinates agree under `R → F`, and ring coordinates reduce
to the `b`-coordinates of the residue. Both bases are uniquely characterized
by their prescribed vectors. Membership in the maximal ideal of `S` is
coefficientwise membership in the maximal ideal of `R`; `S` is finite and
free as an `R`-module.
No valuation-ring structure on `S`, fraction-field structure for `S → L`,
or prior finiteness, freeness, flatness or integrality of `S` over `R` is assumed.
The domain structure on `S` and its flatness over `R` are derived.
Universes are independent; no Henselianity, completeness, discreteness,
separability, residue perfection, finite residue-field cardinality or common
value group is required. This is degree exhaustion by the residue-basis size,
not a definition of an unramified extension.

**Trace and norm for prescribed residue lifts.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueTraceNorm.lean)).
Under the preceding prescribed-lift hypotheses, including finite `L/F` and
`card ι = [L : F]`, ordinary algebraic trace and norm commute with the original
embeddings `R → F` and `S → L`, and with the canonical residue maps.
Finiteness and freeness of `S` over `R` follow from the lifted ring basis;
neither is an extra premise. Residue separability is not required, and there
is no restriction on characteristic.

**Trace-one units and trace surjectivity.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueTraceNorm.lean)).
Let `R` be a valuation domain with fraction field `F`, `L/F` a finite field
extension, and `S` a commutative local `R`-algebra with its given injective
`S → L`. Retain the original ambient and residue algebra actions and the
four compatible scalar towers described above. If `[κS : κR] = [L : F]`
and the given residue extension `κS/κR` is separable,
`ValuationRing.exists_unit_trace_eq_one` gives a unit of the original `S`
whose original `R`-linear trace is one, and `ValuationRing.trace_surjective`
makes `Algebra.trace R S : S →ₗ[R] R` surjective onto all of `R`.
Residue bases, lifts and finite freeness are internal, not caller premises.
No Henselianity, finite residue-field cardinality, invertible degree,
valuation-ring structure on `S`, or fraction-field structure for `S → L`
is required.

**Perfectness of the integral trace pairing.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/TracePairing.lean)).
For a valuation domain `R` with fraction field `F` and a local `R`-algebra
`S` embedded by its given algebra map in a field `L` finite over `F`, retain
the compatible original ambient and residue algebras and scalar towers.
If `[κS : κR] = [L : F]` and the given residue extension is separable,
`ValuationRing.bijective_traceForm_of_finrank_eq` makes the canonical map
`Algebra.traceForm R S : S →ₗ[R] Module.Dual R S` bijective. Thus every
original `R`-linear functional on `S` is uniquely represented by multiplication
under the trace. Finite freeness is derived, not a caller premise; no
Henselianity, finite residue-field cardinality, or invertibility of the degree
is assumed.

**Unit discriminants from separable residue-degree exhaustion.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/Discriminant.lean)).
In the same compatible valuation-domain and local embedded-algebra setting,
if `[L : F] = [κS : κR]` and the given residue extension is separable,
`ValuationRing.discr_isUnit_of_finrank_eq` makes the discriminant of every
finite `R`-basis of the original `S` a unit in the original `R`.
Finite freeness and the extended maximal-ideal equality are derived internally;
no Henselianity, finite residue-field cardinality or invertible degree is required.

**Ambient membership detected by the trace pairing.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueTraceNorm.lean)).
Let `R` be a commutative valuation domain with fraction field `F`, and let
`S` be a commutative local ring embedded by its given algebra map in a field
`L` finite over `F`. Keep the seven given algebras `R → F`, `F → L`,
`R → S`, `S → L`, `R → L`, `κR → κS`, `R → κS`, and the four scalar towers
`R/F/L`, `R/S/L`, `R/κR/κS`, `R/S/κS`, in independent carrier universes.
If `[κS : κR] = [L : F]` and the given residue extension is separable,
`ValuationRing.mem_range_algebraMap_iff_forall_trace_mul_mem_range` states,
for every `x : L`,
`x ∈ range(algebraMap S L) ↔ ∀ y : S, Algebra.trace F L
(x * algebraMap S L y) ∈ range(algebraMap R F)`.
The tests range over all of `S`, not just `1`. The conclusion
is membership in the given image, without assuming an integral-closure
presentation of `S`. Residue bases, lifts and finite freeness are internal.
No Henselianity, finite residue-field cardinality, invertible degree,
ambient separability, valuation-ring or fraction-field structure on `S`,
value-group, discreteness or completeness hypothesis is added.

**Valuation of a norm under residue-degree exhaustion.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/NormValuation.lean)).
Let `L/F` be a finite field extension with given valuations `v`, `w` and
original integer rings `R`, `S`. Retain the compatible ambient and residue
algebra structures and scalar towers above, and assume `[L : F] = [κS : κR]`.
For any monoid-with-zero homomorphism `j` between their independent value groups
satisfying `w (algebraMap F L a) = j (v a)` for every `a : F`,
`Valuation.map_norm_eq_pow_of_finrank_eq_residueField` gives
`j (v (Algebra.norm F x)) = (w x) ^ Module.finrank F L` for every `x : L`.
No injectivity or order preservation of `j`, Henselianity, separability,
discreteness or finite residue-field cardinality is assumed.

**Unit norms over a Henselian valuation domain.** ([principal congruences](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/NormUnits.lean),
[finite residue fields](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/UnitNorm.lean)).
In the preceding compatible valuation-domain and local embedded-algebra setting,
assume `R` Henselian, `[L : F] = [κS : κR]`, and the given residue extension
separable. For every ideal `I ≤ maximalIdeal R` and `u : R` with `u - 1 ∈ I`,
there is a unit `s : S` with `s - 1 ∈ I.map (algebraMap R S)` and
`Algebra.norm R s = u`. No primitive element, basis, finite/free module or
trace-unit witness is a premise. For every such ideal `I`,
`ValuationRing.map_norm_units_ker_quotient` identifies the image under the unit
norm of the kernel of reduction modulo `I.map (algebraMap R S)` with the kernel
of reduction modulo `I`. Its positive-power specialization maps the kernel
modulo `maximalIdeal S ^ n` onto the corresponding kernel for `R`, for every
`n > 0`. No Galois, prime-degree, invertible-degree, discreteness or
completeness hypothesis is required.
If the base residue field is finite, every unit of `R` is the norm of a unit
of the original `S`, and the kernel-image equality holds for every `n`,
including zero. Residue separability is derived from finiteness, rather than
assumed. This combines finite-field unit norm surjectivity, the residue norm
comparison and the principal-congruence correction.

**The field norm group.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/NormRange.lean)).
In the preceding compatible valuation-domain and local embedded-algebra setting,
assume `R` Henselian with finite residue field and `[L : F] = [κS : κR]`.
`ValuationRing.mem_range_norm_units_iff` identifies the usual norm subgroup
`(Units.map (Algebra.norm F : L →* F)).range` of `Fˣ`: its elements are exactly
`a ^ [L : F] * image(u)` for `a : Fˣ` and `u : Rˣ`, using the given `R → F` map.
Residue bases and lifts are chosen internally. No valuation-ring structure on
`S`, fraction-field structure for `S → L`, separability or degree invertibility
is assumed. This is the norm on `Lˣ`, not the zero-inclusive range on `L`.

**The field norm quotient over a discrete valuation ring.** ([module](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/NormQuotient.lean)).
In the preceding field-norm setting, additionally suppose that the base `R`
is a discrete valuation ring. `ValuationRing.normQuotientEquivZMod` identifies
`Fˣ / N(Lˣ)` with the additive group `ZMod [L : F]`, written multiplicatively.
Its value on a representative is the exponent of the canonical maximal-ideal
valuation, reduced modulo the degree; a uniformizer has exponent `-1`.
`ValuationRing.isCyclic_normQuotient` and `ValuationRing.card_normQuotient`
give cyclicity and cardinality `[L : F]`. No discrete valuation ring structure
on `S`, Galois assumption or restriction on the characteristic or degree is added.

**Power bases and minimal polynomials from arbitrary primitive residue lifts.** ([power bases](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResiduePowerBasis.lean),
[polynomial comparisons](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResiduePolynomial.lean),
[derivatives and separability](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueSeparability.lean)).
In the preceding valuation-domain, local embedded-algebra setting, assume
`[L : F] = [κS : κR]`. For every `α : κS` with
`Algebra.adjoin κR {α} = ⊤` and every `θ : S` reducing to `α`,
`ValuationRing.integralPowerBasisOfPrimitiveResidue` constructs a power
basis of the original `S/R`, and `ValuationRing.powerBasisOfPrimitiveResidue`
constructs a power basis of the original `L/F` with generator `algebraMap S L θ`.
Both dimensions are `natDegree (minpoly κR α)`, equal to the field and residue
degrees. Their full bases are the prescribed-lift bases above, formed from
the stock residue power basis and the same family `θ ^ i`, without reindexing.
The stock power-basis generation theorem gives `S = R[θ]` and
`L = F[algebraMap S L θ]`. For the integral power basis `pbR`, the monic
polynomial `pbR.minpolyGen = minpoly R θ` maps under `R → F` exactly to
`minpoly F (algebraMap S L θ)` and reduces under `R → κR` exactly to
`minpoly κR α`. These are coefficientwise equalities, not just association
of polynomials. Residue finiteness is derived; no power basis, finite
`R`-module structure or integrality of `S` is assumed. Neither comparison
requires separability. No Henselianity, discreteness, completeness or common
value group is required. If `minpoly κR α` is separable, then
`pbR.minpolyGen.derivative` evaluates at the same prescribed `θ` to a unit
in the original `S`, and the original extension `L/F` is separable.
Under this separability hypothesis, for a commutative local `R`-algebra `T`
with the given `R/κR/κT` and `R/T/κT` residue towers and a value
`hT : HenselianLocalRing T`, every `κR`-algebra
homomorphism `φ : κS →ₐ[κR] κT` lifts uniquely to an `R`-algebra homomorphism
`S → T` whose reduction agrees with `φ` on every element of `S`
([residue homomorphisms](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHom.lean)).

**Unique residue and field homomorphism lifts.** ([lifting](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFinite.lean),
[identity and composition](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFunctorial.lean)).
Let `R` be a valuation domain with fraction field `F`, and let a commutative
local `R`-algebra `S` embed by its given algebra map in a finite extension
`L/F`. Assume `[L : F] = [κS : κR]` and explicitly
`[Algebra.IsSeparable κR κS]`. Let `T` be a commutative local `R`-algebra
with its given compatible residue scalar towers and an ordinary value
`hT : HenselianLocalRing T`.
`ValuationRing.existsUnique_residueAlgHom_lift_of_finrank_eq` gives, for every
`φ : κS →ₐ[κR] κT`, a unique `ψ : S →ₐ[R] T` satisfying
`residue T (ψ s) = φ (residue S s)` for every `s : S`.
Given a semiring `F`-algebra `E` and the compatible original maps and towers
for `T → E` and `R → E`,
`ValuationRing.existsUnique_fieldAlgHom_lift_of_finrank_eq` also gives a unique
`ι : L →ₐ[F] E` admitting such a `ψ` with
`algebraMap T E (ψ s) = ι (algebraMap S L s)` for every `s : S`.
The semiring `E` may be noncommutative or trivial, so no unconditional
embedding into it is asserted. No base Henselianity, target integrality,
domain, injectivity, finiteness or degree equality is assumed.
Identity and composition compare already-given compatible maps using local
simple-root uniqueness, without any Henselianity or target size hypothesis;
both ambient algebras in composition need only be semirings. A finite
separable source residue extension supplies a primitive generator and its
lift internally. For integral targets over a Henselian base, Adic Modules
supplies the required target Henselianity along the original map. All
universes are independent, and the given maps, actions and towers are retained.
The source degree equality and residue separability remain restrictions;
this is not a full unramified-extension equivalence.

**Absolute values and rank-at-most-one realizations.** ([generic layer](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/AbsoluteValues.md),
[rank and topology details](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#rank-dimension-and-real-absolute-values)).
Nonarchimedean real absolute values on nontrivial rings and zero-reflecting
`NNReal`-valued valuations on rings convert in both directions with round-trip laws.
Pullbacks and rational restriction are included. Unit bounds for division semirings
and bounded-range criteria for real absolute values are also provided.
On a division ring, rank-at-most-one valuation data (with a linearly ordered
commutative value group with zero) give a real absolute value
reflecting the preorder and unit ball, with an ultrametric uniform equivalence
`WithVal v ≃ᵤ WithAbs v.absoluteValue`. Trivial valuations are included; rank one
gives nontriviality and, on valued fields, Mathlib's `Valued.toNormedField` norm.

**Scalar and binomial valuation formulas.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#scalar-and-binomial-estimates)).
Multiplication-preserving, nonnegative nonarchimedean maps on a nonassociative ring
satisfy natural prime-power formulas at a prime `p` with `f p < f 1`, retaining
the factor `f 1`. The target needs `MulOneClass`, natural powers with `NatPowAssoc`,
zero, a linear order and two-sided positive-multiplication monotonicity, not
preservation of zero or one by the map. For valuations on arbitrary rings into
linearly ordered commutative monoids with zero, prime-binomial and prime-power upper bounds
hold without integrality or cancellation. If `p` is prime, `v p < 1` and both
`v (x-1)^(p-1), v (z-1)^(p-1) < v p`, then
`v (x^m-z^m) = v m * v (x-z)` for all natural `m`; for units it holds for all
integer powers as well. No commutation is needed, and zero distances are included.
Natural powers with `v m = 1` preserve distances in the strict unit ball about one.

**Rank, dimension, normalization and bounded modules.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#rank-dimension-and-real-absolute-values)).
For a field valuation into a linearly ordered commutative group with zero and a
commutative local integer presentation `hv : val.Integers O`,
rank at most one gives positive-power divisibility `y ∣ x^n` for maximal-ideal `x`
and nonzero `y`, and `Ring.KrullDimLE 1 O`. Conversely that dimension bound gives
rank-at-most-one data. Rank concerns the restricted value group; dimension zero and
trivial valuations are included. Surjective valuations on any ring into a common
linearly ordered commutative group with zero with cyclic units are equivalent iff equal.
Integer presentations and DVR valuations have comparison laws. A bounded submodule
of a finite-dimensional normed space over complete `K` is finitely generated over
commutative Noetherian `R` with compatible actions whose image contains `K`'s closed
unit ball. For a finite-dimensional normed `K`-algebra that is a normed ring,
`v.HasExtension w`, Noetherian base integers, a `v`-integral base norm unit ball
and norm-at-most-one `w`-integers give finite extension-integer modules.

**Valuative topologies, Cauchy filters and completions.** ([topology and Cauchy details](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#valuative-topologies-and-cauchy-filters),
[completion details](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#completions-and-residue-transport)).
Here value groups are arbitrary linearly ordered commutative groups with zero.
Powers tend to zero iff `x <ᵥ 1` in rank-at-most-one valuative rings; on division
rings, the identity homeomorphism recognizes equivalence of two such valuations.
Supplied integer-valued uniformities have integer-threshold Cauchy, limit and
completeness criteria. In any valuative additive uniformity on a ring, Cauchy
filters have bounded compatible valuation values and either converge to a fixed
center or stabilize at a positive difference value. A supplied valued ring is
complete iff its inherited integer subring is complete, at arbitrary rank.
A compatible field valuation extends to its given uniform completion with the same
value group and induces its topology. A dense exactly value-preserving ring homomorphism
from a valued field to a complete separated valued ring identifies that ring with the completion.
Dense `HasExtension` field algebra maps induce dense integer maps and bijective
residue maps, also for different value groups; integer surjectivity is not asserted.

**Finite intersections, approximation and spectra.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#intersections-and-spectra)).
Arbitrary families of valuations on a field into a common linearly ordered
commutative group with zero have intersection integers and full residue maps.
Finite pointwise rank-at-most-one families have denominator, localization and
fraction-field results, residue surjectivity at each selected nontrivial place,
dimension at most one and finite spectra whose opens are empty or contain zero.
Every maximal ideal is contracted for nonempty finite families, even without rank
assumptions. Finite pairwise inequivalent rank-one families have weak approximation
at positive restricted-value radii, residue-product surjectivity and a spectrum
homeomorphism with `Topology.WithGenericPoint`. Diagonal uniformizers additionally
require discreteness; repeated or trivial places need the separate boundaries below.

**Laurent-series integers and approximation.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#laurent-series-and-approximation)).
Over a field `K`, maximal-ideal powers in the standard Laurent-series valuation
subring are detected by vanishing coefficients at natural indices below the power;
units are exactly those with nonzero zeroth coefficient, and maximal-ideal elements
exactly those with zero zeroth coefficient. The residue field is `K`, with reduction
given by that coefficient. Laurent series over a type
with zero have finite support below every integer cutoff; over a semiring a Laurent
polynomial matches those coefficients, and over a field these polynomials are dense.

**Henselian roots with sharp valuation precision.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#henselian-roots-and-power-neighborhoods)).
For a field valuation into a linearly ordered commutative group with zero whose integers
`O` are Henselian at their maximal ideal `𝔪`, `v(f(a)) < v(f′(a))²` for `f : O[X]`,
`a : O`, gives a root with exact error identity, derivative-value stability and uniqueness
in the strict derivative ball. For natural `s`, the conditions `f(a) ∈ 𝔪^(2*s+1)` and
`f′(a) ∉ 𝔪^(s+1)` give correction in `𝔪^(s+1)`. Applied to powers,
`v(a-1) < v(m : K)²` gives `b^m = a`, `v b = 1` and exact correction value;
nonzero exponent casts give open power ranges in `Kˣ`. No completeness, rank,
discreteness, monicity or unit-derivative assumption is required.

**Bernoulli integrality and complete denominators.** ([details and modules](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/docs/Guide.md#bernoulli-numbers-and-discrete-roots)).
For every integer `n` and positive natural `k`, `n^k*(n^k-1)*B_k/k` is integral
over `ℤ`, including `B₁ = -1/2`. For the divided Bernoulli number
`B_(2*k)/(2*k)` with positive natural `k`, selected primes `p` satisfying
`p-1 ∣ 2*k` give additive `p`-adic valuation `-1-padicValNat p (2*k)` and
reduced-denominator exponent `1+padicValNat p (2*k)`. The complete-denominator
API gives zero factorization coordinates otherwise and expresses that same
reduced denominator as a finite prime product. The product formula also includes
`k = 0`, when the denominator and product are one. A separate rational-integrality
criterion bounds prime denominator support.
For an integer-valued valuation on any ring, an element with a `q^n`-th root
at every depth, for natural `q > 1`, has value zero or one; compatible roots are not required.
