---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.expectation, ProbabilisticTheory.UnitalPositiveLinearMap.apply_observable_eq_expectation, ProbabilisticTheory.UnitalPositiveLinearMap.expectation_one, ProbabilisticTheory.UnitalPositiveLinearMap.expectation_nonneg, ProbabilisticTheory.UnitalPositiveLinearMap.centered, ProbabilisticTheory.UnitalPositiveLinearMap.expectation_centered, ProbabilisticTheory.UnitalPositiveLinearMap.centered_add_smul_one, ProbabilisticTheory.UnitalPositiveLinearMap.apply_mul_comm_eq_star
statement: formalized
proof: formalized
---

# Expectation, variance and covariance

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Statistics`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean): 17 declarations, 17 with a docstring.

> Expectation values, centered observables, covariance and variance of observables in a state.

## i. Overview

> A state assigns expectation values `ω⟨a⟩` to observables. Subtracting the expectation gives the
> centered observable, and from it the covariance and the variance of observables in a state. None of
> this needs a norm, and positivity of the variance uses only that `star x * x ≥ 0`.

## ii. Key results

> - `UnitalPositiveLinearMap.expectation` : the expectation value `ω⟨a⟩`.
> - `UnitalPositiveLinearMap.centered` : an observable minus its expectation.
> - `UnitalPositiveLinearMap.covariance`, `UnitalPositiveLinearMap.variance` : covariance and
>   variance.
> - `UnitalPositiveLinearMap.variance_nonneg` : the variance is nonnegative.

## iv. References

> * None.

## A. Expectation

**`ProbabilisticTheory.UnitalPositiveLinearMap.expectation`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L61).

> The expectation `ω⟨a⟩` of observables in the state `ω`: the average of repeated measurements of
> `a` on systems prepared in `ω`.

```lean
noncomputable def expectation (ω : 𝓢[ℂ, A]) : 𝓢[ℝ, Observable A]
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_observable_eq_expectation`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L72).

> The complex-valued state functional agrees with the real expectation notation `ω⟨a⟩` on
> observables: no information is lost, since self-adjoint elements have vanishing imaginary part.

```lean
lemma apply_observable_eq_expectation (ω : 𝓢[ℂ, A]) (a : Observable A) :
    ω (a : A) = (ω⟨a⟩ : ℂ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.expectation_one`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L79).

> The trivial "do-nothing" observable `1` is measured with certainty: probabilities sum to one.

```lean
lemma expectation_one (ω : 𝓢[ℂ, A]) :
    ω⟨(1 : Observable A)⟩ = 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.expectation_nonneg`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L85).

> Positive observables have nonnegative expectation.

```lean
lemma expectation_nonneg (ω : 𝓢[ℂ, A]) {a : Observable A} (ha : 0 ≤ (a : A)) :
    0 ≤ ω⟨a⟩
```

## B. Centering

**`ProbabilisticTheory.UnitalPositiveLinearMap.centered`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L93).

> The fluctuation of an observable around its mean: `a` with `ω⟨a⟩` subtracted off. Its
> statistics (`covariance`, `variance`) describe the spread of `a`'s outcomes.

```lean
noncomputable def centered (ω : 𝓢[ℂ, A]) (a : Observable A) : Observable A
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.expectation_centered`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L99).

> A fluctuation has zero mean by construction: the average deviation from the average is zero.

```lean
lemma expectation_centered (ω : 𝓢[ℂ, A]) (a : Observable A) :
    ω⟨centered ω a⟩ = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.centered_add_smul_one`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L107).

> Shifting an observable by a deterministic constant `c` shifts its mean by `c` too, so the
> fluctuation around the new mean is unchanged.

```lean
lemma centered_add_smul_one (ω : 𝓢[ℂ, A]) (a : Observable A) (c : ℝ) :
    centered ω (a + c • 1) = centered ω a
```

## C. Reversing a product

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_mul_comm_eq_star`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L117).

> Reversing a product of two observables conjugates its value in a state.

```lean
lemma apply_mul_comm_eq_star (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    ω ((b : A) * a) = star (ω ((a : A) * b))
```

## D. Covariance and variance

**`ProbabilisticTheory.UnitalPositiveLinearMap.covariance`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L125).

> The covariance of two observables in the state `ω`, the real part of the expectation of the
> product of their fluctuations.

```lean
noncomputable def covariance (ω : 𝓢[ℂ, A]) (a b : Observable A) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.variance`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L130).

> The spread of `a`'s measurement outcomes about its mean — the quantum analogue of a random
> variable's variance, whose square root is the uncertainty `Δa` in `CStarAlgebra.Uncertainty`.

```lean
noncomputable def variance (ω : 𝓢[ℂ, A]) (a : Observable A) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.covariance_self`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L135).

> Unfolds `variance` as covariance of an observable with itself.

```lean
lemma covariance_self (ω : 𝓢[ℂ, A]) (a : Observable A) :
    covariance ω a a = variance ω a
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.covariance_eq_re_apply_centered_mul`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L142).

> The canonical covariance form on the Jordan algebra of observables is the real part of the
> state applied to the ordinary associative product of the centered observables. This is a
> specialization theorem, not a second definition of covariance.

```lean
lemma covariance_eq_re_apply_centered_mul (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    covariance ω a b = (ω ((centered ω a : A) * centered ω b)).re
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.variance_eq_re_apply_centered_mul_self`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L170).

> The variance is the expectation of the squared fluctuation.

```lean
lemma variance_eq_re_apply_centered_mul_self (ω : 𝓢[ℂ, A]) (a : Observable A) :
    variance ω a = (ω ((centered ω a : A) * centered ω a)).re
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.covariance_comm`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L176).

> Covariance is symmetric: reversing a product of self-adjoint fluctuations conjugates the
> state's value on it, and conjugation does not change the real part.

```lean
lemma covariance_comm (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    covariance ω a b = covariance ω b a
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.covariance_add_smul_one_left`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L183).

> Covariance depends only on fluctuations: shifting the left observable by a constant `c`
> leaves it unchanged.

```lean
lemma covariance_add_smul_one_left (ω : 𝓢[ℂ, A]) (a b : Observable A) (c : ℝ) :
    covariance ω (a + c • 1) b = covariance ω a b
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.covariance_add_smul_one_right`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L197).

> Covariance depends only on fluctuations: shifting the right observable by a constant `c`
> leaves it unchanged.

```lean
lemma covariance_add_smul_one_right (ω : 𝓢[ℂ, A]) (a b : Observable A) (c : ℝ) :
    covariance ω a (b + c • 1) = covariance ω a b
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.variance_nonneg`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean#L211).

> **The variance is nonnegative.**

```lean
lemma variance_nonneg (ω : 𝓢[ℂ, A]) (a : Observable A) :
    0 ≤ variance ω a
```

## Depends on

- [Statistics of a linear functional on a bilinear algebra](../algebra/statistics.md)
- [The Jordan product of observables](jordan.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Statistics.lean)
