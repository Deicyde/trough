---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.FieldEnumeration.size_pos, CompPoly.CPolynomial.Roots.FiniteField.UniformFieldEnumeration, CompPoly.CPolynomial.Roots.FiniteField.UniformFieldEnumeration.q_pos, CompPoly.CPolynomial.Roots.FiniteField.OddUniformFieldModel, CompPoly.CPolynomial.Roots.FiniteField.TrialResult, CompPoly.CPolynomial.Roots.FiniteField.TrialResult.IsSuccess, CompPoly.CPolynomial.Roots.FiniteField.TrialResult.children, CompPoly.CPolynomial.Roots.FiniteField.TrialResult.allFailed, CompPoly.CPolynomial.Roots.FiniteField.eventProbability, CompPoly.CPolynomial.Roots.FiniteField.trialSuccessProbability, CompPoly.CPolynomial.Roots.FiniteField.trialFailureProbability_eq_failed_mass, CompPoly.CPolynomial.Roots.FiniteField.trialSuccessProbability_add_failed_mass, CompPoly.CPolynomial.Roots.FiniteField.trialFailureProbability_le_half_of_success
statement: formalized
proof: formalized
---

# Probability Basics for Las Vegas Root Splitting

`CompPoly.Univariate.Roots.LasVegas.Probability.Basic`, in [CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean), by Valerii Huhnin.

> Shared probability-side vocabulary for the Las Vegas splitter: event
> probabilities, uniform enumeration models, split-trial results, and small PMF
> lemmas about trial success and failure mass.
>
> This module is intentionally separate from the executable splitter modules:
> runtime root search remains pure and deterministic for a fixed `ProbeFamily`,
> while the probability modules model idealized uniform probes. Runtime and
> correctness modules must not import this file or any other probability module.

`CompPoly.CPolynomial.Roots.FiniteField.FieldEnumeration.size_pos` (theorem, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L40))

> A complete field enumeration is nonempty when the field type has a zero.

```lean
theorem size_pos {F : Type*} [Zero F] (enumeration : FieldEnumeration F) :
    0 < enumeration.size
```

`CompPoly.CPolynomial.Roots.FiniteField.UniformFieldEnumeration` (structure, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L51))

> Probability-only strengthening of `FieldEnumeration`: the lazy enumeration has
> no duplicate indices and its size is the finite-field cardinality `q`.

```lean
structure UniformFieldEnumeration (F : Type*) (q : Nat) where
  toFieldEnumeration : FieldEnumeration F
  injective_elem : Function.Injective toFieldEnumeration.elem
  size_eq_q : toFieldEnumeration.size = q
```

`CompPoly.CPolynomial.Roots.FiniteField.UniformFieldEnumeration.q_pos` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L59))

> A probability-uniform enumeration has positive cardinality.

```lean
theorem q_pos {F : Type*} [Zero F] {q : Nat}
    (enumeration : UniformFieldEnumeration F q) :
    0 < q
```

`CompPoly.CPolynomial.Roots.FiniteField.OddUniformFieldModel` (structure, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L74))

> Probability-facing odd-field model: the uniform enumeration size `q` is the
> cardinality of the finite field, and that cardinality is odd.
>
> This intentionally stays separate from the runtime splitter contract
> `lasVegasSplitterInput`, which must not accumulate probability hypotheses.

```lean
structure OddUniformFieldModel (F : Type*) (q : Nat) [Fintype F]
    (enumeration : UniformFieldEnumeration F q) : Prop where
  q_odd : q % 2 = 1
  card_eq : Fintype.card F = q
```

`CompPoly.CPolynomial.Roots.FiniteField.TrialResult` (inductive type, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L80))

> Result of one randomized split trial.

```lean
inductive TrialResult (F : Type*) [Zero F] where
  | split (children : Array (CPolynomial F))
  | failed
```

`CompPoly.CPolynomial.Roots.FiniteField.TrialResult.IsSuccess` (definition, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L87))

> A trial succeeds when it returns proper child factors.

```lean
def IsSuccess {F : Type*} [Zero F] : TrialResult F → Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.TrialResult.children` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L92))

> Child factors returned by a successful trial, or an empty array after failure.

```lean
def children {F : Type*} [Zero F] : TrialResult F → Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.TrialResult.allFailed` (definition, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L97))

> A list of trials has not split the current factor.

```lean
def allFailed {F : Type*} [Zero F] : List (TrialResult F) → Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.eventProbability` (definition, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L104))

> Probability of an event under a PMF, expressed through the PMF outer measure.

```lean
noncomputable def eventProbability {α : Type*} (dist : PMF α) (event : Set α) : ℝ≥0∞
```

`CompPoly.CPolynomial.Roots.FiniteField.trialSuccessProbability` (definition, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L108))

> Probability that a split trial succeeds.

```lean
noncomputable def trialSuccessProbability {F : Type*} [Zero F]
    (dist : PMF (TrialResult F)) :
    ℝ≥0∞
```

`CompPoly.CPolynomial.Roots.FiniteField.trialFailureProbability_eq_failed_mass` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L114))

> Trial failure probability is the PMF mass of the failed outcome.

```lean
theorem trialFailureProbability_eq_failed_mass {F : Type*} [Zero F]
    (dist : PMF (TrialResult F)) :
    eventProbability dist {trial | ¬ trial.IsSuccess} = dist TrialResult.failed
```

`CompPoly.CPolynomial.Roots.FiniteField.trialSuccessProbability_add_failed_mass` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L135))

> Success probability and failed mass of a trial distribution sum to one.

```lean
theorem trialSuccessProbability_add_failed_mass {F : Type*} [Zero F]
    (dist : PMF (TrialResult F)) :
    dist TrialResult.failed + trialSuccessProbability dist = 1
```

`CompPoly.CPolynomial.Roots.FiniteField.trialFailureProbability_le_half_of_success` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean#L149))

> A trial that succeeds with probability at least `1 / 2` fails with at most `1 / 2`.

```lean
theorem trialFailureProbability_le_half_of_success {F : Type*} [Zero F]
    (dist : PMF (TrialResult F))
    (hsuccess : (2 : ℝ≥0∞)⁻¹ ≤ trialSuccessProbability dist) :
    eventProbability dist {trial | ¬ trial.IsSuccess} ≤ (2 : ℝ≥0∞)⁻¹
```

## Depends on

- [Exhaustive Finite-Field Root Enumeration](../../enumeration.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/Basic.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Probability.Basic.json)
