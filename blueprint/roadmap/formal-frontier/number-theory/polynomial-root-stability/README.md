# Polynomial root stability

> Fixed-degree stability of polynomial root-generated intermediate fields inside a common Krasner normed extension, including monic, normalized, and ordinary-coefficient versions with derived nearby separability, plus quantitative Newton lifting with convergence and resultant-controlled factorization over complete ultrametric normed fields, together with polynomial estimates for valuations in linearly ordered commutative value monoids with zero.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/formalization.yaml) of [FormalFrontier/polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability) at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), Apache-2.0.*

4 articles: 4 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability), read at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “pending”.
- Automation: agent; framework “Codex CLI”; tool setup “AI-assisted Lean proof development, mathematical examples and documentation with repository-pinned Lean and mathlib compilation.”
- Automation notes: “Automated assistance is not a substitute for proof-term validation, mathematical review or source-correspondence review.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Fixed-ambient-field root-generated-field stability* (original-proof; other).
- *Cohomology of Number Fields, corrected second edition 2.3*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Section 12.1.1; corrected edition 2.3, May 2020 (book; background).
- *Local Fields and Their Extensions, second edition*, Ivan B. Fesenko, Sergei V. Vostokov, Chapter II, Section 1, Proposition 1.1 (p. 36), Corollary 3 (p. 37), Exercise 1 (p. 38) (book; background).

## Builds on

No other Formal Frontier library.

## Used by

- [Complex analysis](../../analysis/complex-analysis/README.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/README.md#headline-results) of [FormalFrontier/polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability) at commit [efade497](https://github.com/FormalFrontier/polynomial-root-stability/tree/efade497a4cf39e72a20ef94fe4028b82fcb5f80), Apache-2.0.*

**Root-generated fields are locally constant at fixed degree.** Fix normed
fields `K`, `L` with a normed algebra structure `L / K` satisfying
`IsKrasner K L`. For any nonzero separable polynomial `f : K[X]` that splits
in `L`, there is a radius `ε > 0` such that every polynomial `g : K[X]` with
the same `natDegree`, also splitting in `L`, and with
`‖g.coeff i - f.coeff i‖ < ε` for every coefficient index `i`, is separable
and generates exactly the same intermediate field over `K` as `f`.
The [ordinary-coefficient theorem](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Normalization.lean#L214)
applies without monicity and derives comparison nonzeroness internally.

There are also [monic](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Krasner.lean#L565) and
[scale-invariant normalized-coefficient](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Normalization.lean#L45)
versions of this result. The normalized version measures closeness after
dividing each polynomial by its own leading coefficient and requires `g ≠ 0`
explicitly; do not interchange the normalized and ordinary coefficient bounds.

These results let downstream developments perturb coefficients while keeping
the root-generated subfield fixed. The ambient extension and both splitting
assumptions are inputs, not conclusions. Equality is between the subfields
`IntermediateField.adjoin K (f.rootSet L)` and
`IntermediateField.adjoin K (g.rootSet L)` inside that fixed `L`, not an
equivalence of canonical splitting-field objects. Fixed degree is essential;
no stability for arbitrary variable-degree families or nonseparable references
is asserted. Mathlib supplies Krasner's lemma and polynomial-root continuity;
this library combines them with finite-root estimates and coefficient
normalization to obtain the stated local-constancy interfaces. See the
[historical root-field API reference](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/docs/README.md) and the
[generic checked-use clients](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStabilityTest/Normalization.lean).

- [Polynomial root scaling](polynomial-root-scaling.md)
- [Polynomial scaling in valuation balls](polynomial-scaling-in-valuation-balls.md)

**Local polynomial norm scaling.** Let `R` be an ultrametric commutative seminormed ring with multiplicative
seminorm. If `f : R[X]` satisfies `∀ n, ‖f.coeff n‖ ≤ M`, `‖a‖ ≤ 1`, and
`M * ‖b - a‖ < ‖f.derivative.eval a‖`, then

```lean
‖f.eval b - f.eval a‖ = ‖f.derivative.eval a‖ * ‖b - a‖
```

The theorem
[`Polynomial.norm_eval_sub_eq_of_mul_norm_sub_lt_norm_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Ultrametric.lean)
requires no root, division, completeness or separated norm. Only the anchor
`a` is assumed to lie in the unit ball; the bound on `b` follows from the
hypotheses. Zero seminorm distance is allowed without identifying the points.
The [3-adic Newton example](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStabilityTest/NewtonNaturality.lean)
instantiates this identity at `a = 1` and `b = 5 / 2` for `X² - 4`, with
nonzero evaluation-difference norm and displacement norm both equal to `1 / 3`.

The two-point theorem
[`Polynomial.norm_eval_sub_eval_eq_of_mul_norm_sub_lt_norm_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Ultrametric.lean)
gives `‖f.eval c - f.eval b‖ = ‖f.derivative.eval a‖ * ‖c - b‖`
under the same assumptions on `R`, `f`, `M`, and `a` whenever both
`M * ‖b - a‖ < ‖f.derivative.eval a‖` and
`M * ‖c - a‖ < ‖f.derivative.eval a‖`; the derivative factor remains at the
original anchor `a`.

When `R` is a normed commutative ring, the same coefficient and anchor bounds
give injectivity on this strict ball. The theorem
[`Polynomial.injOn_eval_of_mul_norm_sub_lt_norm_derivative`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/RootUniqueness.lean)
expresses this as `Set.InjOn`; the anchor need not be a root.

**Root existence and bounds under coefficient perturbation.** For an ultrametric commutative seminormed ring with multiplicative seminorm, assume
`∀ n, ‖f.coeff n‖ ≤ M`, `‖a‖ ≤ 1`, `f.eval x = 0`, and `g.eval y = 0`.
If `M * ‖x - a‖ < ‖f.derivative.eval a‖` and `M * ‖y - a‖ < ‖f.derivative.eval a‖`,
and `∀ n, ‖f.coeff n - g.coeff n‖ ≤ ε`, then `‖f.derivative.eval a‖ * ‖x - y‖ ≤ ε`.
This is a bound on two given roots. No separation or completeness is needed;
`ε = 0` gives zero seminorm distance, not necessarily equality of roots.

For local root existence, set `D = ‖f.derivative.eval a‖`. In a complete ultrametric
normed commutative ring with multiplicative norm,
`Polynomial.exists_root_of_norm_coeff_sub_le_of_isUnit` takes the coefficient and
anchor bounds, the root `x` of `f`, its strict ball inequality `M * ‖x - a‖ < D`,
the coefficient-difference bound, `M * ε < D ^ 2`, and a unit original derivative.
It constructs a root `y` of `g` in the same original strict derivative ball with
`D * ‖x - y‖ ≤ ε`. Every root of `g` in that ball equals `y`, whether or not a
scaled distance bound was supplied for it. No root of `g` is an input.

Over a complete ultrametric normed field,
`Polynomial.exists_root_of_norm_coeff_sub_le` derives the derivative unit from
the strict ball inequality, so only the six coefficient, anchor, original-root,
strict-ball, difference, and smallness conditions are inputs. These existential
conclusions are the root-construction and characterization API, not a chosen-root
object: use the witness for existence and its uniqueness clause to identify any
other root in the original ball. The ring construction requires inverse data in
the form of a unit original derivative; it does not assert existence over all
complete ultrametric normed rings without such data.

The same `ℚ_[3]` model with `f = X² - 4`, `g = X² - 25/4`, `a = 1`, and `x = -2`
has `M = D = 1` and positive `ε = 1/9`. The constructed root is `y = 5/2`, and
`D * ‖x - y‖ = 1/9`, so the bound is sharp. Zero perturbation is also supported:
with `g = f` and `ε = 0`, the constructed root equals `x`.
See [coefficient perturbation](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/CoefficientPerturbation.lean).

- [Root uniqueness in an ultrametric normed ring](root-uniqueness-in-an-ultrametric-normed-ring.md)

**Quantitative Newton lifting.** For a complete ultrametric normed field `K`, a polynomial `f : K[X]` with
`∀ n, ‖f.coeff n‖ ≤ 1`, and `‖a₀‖ ≤ 1`, the hypothesis
`‖f.eval a₀‖ < ‖f.derivative.eval a₀‖²` gives an integral root at exact distance
`‖f.eval a₀‖ / ‖f.derivative.eval a₀‖`, with derivative-norm stability and
uniqueness in the open initial-derivative-radius ball. The statement also includes
convergence of the explicit iterates `f.newtonMap^[n] a₀`, integrality of all
iterates, nonzero denominators and derivative-norm stability at every iterate. No monicity, characteristic-zero,
nontrivial-norm, or norm-one derivative hypothesis is imposed. This formulation
uses a real-valued norm, not an arbitrary higher-rank valuation.

The theorem [`Polynomial.exists_root_tendsto_iterate_newtonMap`](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStability/Newton.lean)
uses coefficient-controlled ultrametric estimates and Mathlib’s Banach fixed
point theorem. On the closed ball of radius `δ / d`, where `δ` is the initial
error and `d` the initial derivative norm, the Newton map has contraction constant
`δ / d²`. The proof includes zero initial error and trivially normed fields.
The field-target quotient formula and
[boundary examples](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStabilityTest/NewtonContracts.lean) use the
stock polynomial Newton map and function iteration.
The independent [2-adic input calculation](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStabilityTest/Newton.lean)
uses `X² - 17` at `1`, with nonzero error of norm `1 / 16` and derivative of norm
`1 / 2`, a nonunit in `ℤ_[2]`. Its further convergence client applies the general
theorem; the input calculation is independent of the root-existence proof.
The private [p-adic compatibility clients](https://github.com/FormalFrontier/polynomial-root-stability/blob/efade497a4cf39e72a20ef94fe4028b82fcb5f80/PolynomialRootStabilityTest/PadicHensel.lean)
recover the complete existing Hensel interface for arbitrary commutative-semiring
coefficients and the p-adic polynomial distance estimate, without calling the old
root-existence theorem or adding a duplicate public API. The `X² - 1` boundary
calculation shows that uniqueness cannot use the closed derivative-radius ball.

- [Quantitative resultant-controlled factorization](quantitative-resultant-controlled-factorization.md)

## Main results

Its formalization.yaml lists 9 main results, and the scan finds 9 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
