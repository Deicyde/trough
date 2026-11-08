# Norm forms

> Field-norm/spectral-norm comparison over complete ultrametric fields; coordinate norms over finite field extensions and universal finite-free norms under commutative base change; unbounded attained-degree anisotropic forms; polynomial padding and finite-system K-point zero-set compression; conditional homogeneous-system zeros and single-form zeros over algebraic, rational-function and finite-transcendence-degree extensions; finite-field common-zero theorems; and scalar sums annihilating positive tensor powers.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/formalization.yaml) of [FormalFrontier/norm-forms](https://github.com/FormalFrontier/norm-forms) at commit [4b2893fb](https://github.com/FormalFrontier/norm-forms/tree/4b2893fb313bbd209a319dc920d49075d7e509a7), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 11 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/norm-forms](https://github.com/FormalFrontier/norm-forms), read at commit [4b2893fb](https://github.com/FormalFrontier/norm-forms/tree/4b2893fb313bbd209a319dc920d49075d7e509a7) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Review notes: “The coordinate and universal norm results, polynomial-system common-zero theorems, field-extension transfer and positive-tensor-power annihilation results have been independently reviewed. Their material hypotheses and limitations are described in the README and mathematical guides. This status does not claim complete coverage of a selected source or settle unrelated third-party rights.”
- Automation: agent; framework “Codex CLI and Formal Frontier Hive Tasks”; tool setup “AI-assisted formalization with repository-pinned Lean/mathlib and separate independent review.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Local Fields and Their Extensions*, Ivan Fesenko, Sergei Vostokov, Second edition, Chapter II, §2 (book; formalizes).
- *Non-Archimedean Analysis*, Siegfried Bosch, Ulrich Güntzer, Reinhold Remmert, Sections 3.1–3.2 (book; background).
- *Finite-basis field norm and coordinate norm-form constructions* (folklore; independently-proves).
- *Finite-free universal coordinate norm under scalar extension* (folklore; independently-proves).
- *Finite polynomial-system zero-set compression over non-algebraically-closed fields* (folklore; independently-proves).
- *Equal-degree homogeneous-system nontrivial zeros from a uniform single-form bound* (folklore; independently-proves).
- *Homogeneous-form nontrivial zeros over algebraic field extensions* (folklore; independently-proves).
- *Homogeneous-form nontrivial zeros over rational-function fields* (folklore; independently-proves).
- *Homogeneous-form nontrivial zeros over finite-transcendence-degree extensions* (folklore; independently-proves).
- *Finite-field polynomial-system common zeros from Chevalley–Warning* (folklore; independently-proves).
- *Finite-field scalar sums annihilating positive tensor powers* (folklore; independently-proves).
- *Cohomology of Number Fields*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Chapter VI (book; background).

## Builds on

- [Algebraic groups](../../algebraic-geometry/algebraic-groups/README.md) (a Lake dependency, pinned at 6c7f4a5a)
- [Multivariate polynomials](../../commutative-algebra/multivariate-polynomials/README.md) (a Lake dependency, pinned at 6a042767)
- [Sequence growth](../../analysis/sequence-growth/README.md) (a Lake dependency, pinned at c5c4dbfa)

## Used by

- [Valuation integers](../valuation-integers/README.md)


## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/README.md#headline-results) of [FormalFrontier/norm-forms](https://github.com/FormalFrontier/norm-forms) at commit [4b2893fb](https://github.com/FormalFrontier/norm-forms/tree/4b2893fb313bbd209a319dc920d49075d7e509a7), Apache-2.0.*

**First-order norm–trace congruence.** For commutative rings `R`, `S`, an
`R`-algebra `S`, any ideal `I` of `R` and `x ∈ I.map (algebraMap R S)`,
`Algebra.norm_one_add_sub_one_sub_trace_mem_ideal_sq` proves
`Algebra.norm R (1 + x) - 1 - Algebra.trace R S x ∈ I ^ 2`.
On finite-free algebras this is the usual first-order norm formula,
including rank zero, characteristic two and nonreduced base rings.
No finite/free hypotheses are required: if there is no finite basis,
Mathlib's norm is constantly one and its trace is zero. This convention
is not a new arithmetic norm theory for nonfree or infinite algebras.
See [`NormForms.TraceCongruence`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/TraceCongruence.lean).

**Field norms and spectral norms.** For a finite field extension `L / K`
of a complete ultrametric normed field,
`Algebra.norm_norm_eq_spectralNorm_pow_finrank` proves
`‖Algebra.norm K x‖ = spectralNorm K L x ^ Module.finrank K L`.
The base norm may be trivial, the extension may be inseparable, and no norm
or topology on `L` is assumed. This is the exactly extending absolute-value
formula with exponent `1/[L:K]`, not the discrete normalized-valuation
formula with exponent `1/f`; it does not assert discreteness or `ef=[L:K]`.
See [`NormForms.SpectralNorm`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/SpectralNorm.lean) and the
[ramified quadratic 5-adic example](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormFormsTests/SpectralNorm.lean).

**Universal coordinate norms.** For a finite-free `R`-algebra `B` (which need
not be commutative), a commutative ring `R`, a commutative `R`-algebra `A` and
a finite basis `b`, `Algebra.norm_coordinates_baseChange b x` identifies the
native norm after base change with evaluation of the signed constant
characteristic-coefficient polynomial. `Algebra.norm_universalCoordinates b`
gives an **equality of polynomials** for the universal tensor, not just an
equality of evaluations. These work over finite coefficient fields and even
trivial coefficient algebras. See
[`NormForms.UniversalCoordinates`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/UniversalCoordinates.lean) and
the [universal-coordinate guide](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/UniversalCoordinateNorm.md).

**Norm congruences.** For commutative rings `R` and `S` with a finite free
`R`-algebra structure on `S`, `Algebra.norm_sub_norm_mem_ideal` states that
`x - y ∈ I.map (algebraMap R S)` implies `Algebra.norm R x - Algebra.norm R y ∈ I`.
The ideal is arbitrary, and neither ring needs to be a domain or local.
See [`NormForms.IdealCongruence`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/IdealCongruence.lean).

**Norm forms and basis changes.** For a finite field extension `L / K` with
finite `K`-basis `b` indexed by `ι`, `NormForms.coordinateNormPolynomial b`
evaluates to the field norm, is homogeneous of **actual total degree**
`Fintype.card ι`, and vanishes precisely at the zero coordinate vector.
`NormForms.coordinateChange` converts *new* coordinates into *old* ones;
changing or reindexing the basis gives structural polynomial identities,
including over finite fields where evaluation alone cannot establish
polynomial equality. See [`NormForms.Coordinate`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/Coordinate.lean),
[its clients](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormFormsTests/Coordinate.lean) and the
[historical coordinate signatures](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/API.md).

**Unbounded attained anisotropic degrees.** If `K` is not algebraically
closed, `MvPolynomial.exists_anisotropic_homogeneous_of_not_isAlgClosed`
produces, for every bound, a homogeneous anisotropic form whose *actual*
degree exceeds that bound. It does **not** produce a form in every prescribed
degree. See
[`NormForms.CoordinateNormIteration`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/CoordinateNormIteration.lean)
and the [iteration guide](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/CoordinateNormIteration.md).

**Fixed-polynomial padding and system compression.** For a commutative
semiring, an embedding of index types and a fixed outer polynomial,
[`NormForms.PaddedSubstitution`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/PaddedSubstitution.lean) transfers
zero conditions and proves the homogeneous-substitution label law `d * e`
without finiteness or field assumptions. Over any non-algebraically-closed
field, the public
`MvPolynomial.exists_common_zero_polynomial` compresses a finite family's
**K-point** common zeros to one equation. Its homogeneous variant takes a
common degree label `d` and produces label `d * m` for some
`m > Fintype.card ι`, not a claim about actual total degree. Neither
theorem asserts equality of ideals, radicals, schemes or zeros over every
extension field. See
[`NormForms.CommonZeroCompression`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/CommonZeroCompression.lean),
the [padding guide](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/PaddedSubstitution.md) and the
[compression guide](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/PolynomialCommonZeroCompression.md).

**Common zeros under a direct single-form hypothesis.** Over any field,
`MvPolynomial.exists_nonzero_common_zero_of_single_form_bound` converts a
**direct uniform all-positive-degree** single-form nontrivial-zero premise
into a nonzero common zero for `s` forms of the same positive homogeneous
label `d` in `n` variables, provided `s * d ^ r < n`. Zero and repeated
forms and `s = 0`, `r = 0`, `d = 1` are included. This conditional existence
theorem is distinct from K-point zero-set compression. See
[`NormForms.HomogeneousSystemZeros`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/HomogeneousSystemZeros.lean)
and the [system guide](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/HomogeneousSystemZeros.md).

**Field-extension zeros.** With the same direct *base-field*
all-positive-degree premise, a positive-degree `d`-homogeneous-labelled
form has a nonzero zero over any algebraic extension if `d ^ r < n`;
no finite, separable or perfect-extension hypothesis is needed. Over
`RatFunc k` the strict bound becomes `d ^ (r + 1) < m`. For an extension
`k → K` of transcendence degree `t` the bound is `d ^ (r + t) < m`,
without finite-generation or separability assumptions. These are
single-form theorems, not simultaneous-zero statements. See
[`NormForms.AlgebraicExtensionFormZeros`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/AlgebraicExtensionFormZeros.lean),
[`NormForms.RatFuncFormZeros`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/RatFuncFormZeros.lean),
[`NormForms.FiniteTranscendenceFormZeros`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/FiniteTranscendenceFormZeros.lean)
and their [algebraic](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/AlgebraicExtensionFormZeros.md),
[rational-function](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/RatFuncFormZeros.md) and
[finite-transcendence](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/FiniteTranscendenceFormZeros.md) guides.

**Finite-field common zeros.** Over a finite field,
`MvPolynomial.exists_ne_common_zero_of_sum_totalDegree_lt` returns a second
common point distinct from a known one when the strict sum of **actual
total degrees** is below the number of variables; homogeneity is not
required. Positive, possibly different homogeneous *labels* with strict
sum bound give a nonzero common point via
`MvPolynomial.exists_nonzero_common_zero_of_sum_degrees_lt` and the
single-form specialization
`MvPolynomial.exists_nonzero_zero_of_isHomogeneous_of_degree_lt`.
Zero and repeated forms and the empty family are allowed. A finite-base-
field transcendence-degree example in the tests is **private**, not another
public extension theorem. See
[`NormForms.FiniteFieldFormZeros`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/FiniteFieldFormZeros.lean)
and the [finite-field guide](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/FiniteFieldFormZeros.md).

**Tensor scalar-sum annihilation.** Over a finite field `K`, a nonzero
`a : ι → K` makes `TensorPower.scalarSum (M := M) a` surjective. For `0 < s`,
arbitrary prescribed tensors indexed by finite `τ`, and a
finite-dimensional **target** `W = (TensorPower K s M) ⊗[K] N`,
`TensorPower.exists_nonzero_scalarSumTensor_annihilates` finds one such `a`
whose **actual tensor map** annihilates every tensor when
`s * Fintype.card τ * Module.finrank K W < Fintype.card ι`. The source
tensor space need not be finite-dimensional; no surjectivity of the
tensor map, `s = 0` case or actual-total-degree-`s` equality is claimed.
See [`NormForms.TensorScalarSumAnnihilation`](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormForms/TensorScalarSumAnnihilation.lean),
[five public checked-use clients](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/NormFormsTests/TensorScalarSumAnnihilation.lean)
and the [tensor guide](https://github.com/FormalFrontier/norm-forms/blob/4b2893fb313bbd209a319dc920d49075d7e509a7/docs/TensorScalarShrinking.md).
