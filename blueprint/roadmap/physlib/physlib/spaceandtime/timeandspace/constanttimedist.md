---
declaration: module
origin: cited
lean: Space.continuous_time_integral, Space.time_integral_hasFDerivAt, Space.time_integral_differentiable, Space.integrable_fderiv_space, Space.time_integral_contDiff, Space.integrable_time_integral, Space.pow_mul_iteratedFDeriv_norm_le, Space.iteratedFDeriv_norm_mul_pow_integrable
statement: formalized
proof: formalized
---

# Distributions which are constant in time

The module `Physlib.SpaceAndTime.TimeAndSpace.ConstantTimeDist`, [Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean): 23 declarations, 2 with a docstring.

## i. Overview

> in this module given a distribution on `Space d`, we define the associated distribution
> on `Time × Space d` which is constant in time.
>
> This is defined by integrating Schwartz Maps on `Time × Space d` over the time coordinate,
> to get a Schwartz Map on `Space d`.

## ii. Key results

> - `Space.timeIntegralSchwartz` : the integral over time of a Schwartz map on `Time × Space d`
>   to give a Schwartz map on `Space d`.
> - `Space.constantTime` : the distribution on `Time × Space d` associated with a distribution
>   on `Space d`, which is constant in time.

## iv. References

> * None.

## A. Properties of time integrals of Schwartz maps

### A.1. Continuity as a function of space

**`Space.continuous_time_integral`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L87).

```lean
lemma continuous_time_integral {d} (η : 𝓢(Time × Space d, ℝ)) :
    Continuous (fun x : Space d => ∫ t : Time, η (t, x))
```

### A.2. Derivative a function of space

**`Space.time_integral_hasFDerivAt`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L144).

```lean
lemma time_integral_hasFDerivAt {d : ℕ} (η : 𝓢(Time × Space d, ℝ)) (x₀ : Space d) :
    HasFDerivAt (fun x => ∫ (t : Time), η (t, x))
      (∫ (t : Time), fderiv ℝ (fun x : Space d => η (t, x)) x₀) x₀
```

### A.3. Differentiability as a function of space

**`Space.time_integral_differentiable`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L285).

```lean
lemma time_integral_differentiable {d : ℕ} (η : 𝓢(Time × Space d, ℝ)) :
    Differentiable ℝ (fun x => ∫ (t : Time), η (t, x))
```

### A.4. Integrability of the derivative as a function of space

**`Space.integrable_fderiv_space`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L296).

```lean
lemma integrable_fderiv_space {d : ℕ} (η : 𝓢(Time × Space d, ℝ)) (x : Space d) :
    Integrable (fun t => fderiv ℝ (fun x => η (t, x)) x) volume
```

### A.5. Smoothness as a function of space

**`Space.time_integral_contDiff`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L401).

```lean
lemma time_integral_contDiff {d : ℕ} (n : ℕ) (η : 𝓢(Time × Space d, ℝ)) :
    ContDiff ℝ n (fun x => ∫ (t : Time), η (t, x))
```

## B. Properties of schwartz maps at a constant space point

### B.1. Integrability

**`Space.integrable_time_integral`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L456).

```lean
lemma integrable_time_integral {d : ℕ} (η : 𝓢(Time × Space d, ℝ)) (x : Space d) :
    Integrable (fun t => η (t, x)) volume
```

### B.2. Integrability of powers times norm of iterated derivatives

#### B.2.1. Bounds on powers times norm of iterated derivatives

**`Space.pow_mul_iteratedFDeriv_norm_le`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L498).

```lean
lemma pow_mul_iteratedFDeriv_norm_le {n m} {d : ℕ} :
    ∃ rt, ∀ (η : 𝓢(Time × Space d, ℝ)), ∀ (x : Space d),
    Integrable (fun x : Time => ‖((1 + ‖x‖) ^ rt)⁻¹‖) volume ∧
    ∀ t, ‖(t, x)‖ ^m * ‖iteratedFDeriv ℝ n ⇑η (t, x)‖ ≤
        (2 ^ (rt + m, n).1 *
        ((Finset.Iic (rt + m, n)).sup fun m => SchwartzMap.seminorm ℝ m.1 m.2) η) *
        ‖(1 + ‖t‖) ^ (rt)‖⁻¹
```

#### B.2.2. Integrability of powers times norm of iterated derivatives

**`Space.iteratedFDeriv_norm_mul_pow_integrable`**, a lemma, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L568).

```lean
lemma iteratedFDeriv_norm_mul_pow_integrable {d : ℕ} (n m : ℕ) (η : 𝓢(Time × Space d, ℝ))
    (x : Space d) :
    Integrable (fun t => ‖(t, x)‖ ^ m * ‖iteratedFDeriv ℝ n ⇑η (t, x)‖) volume
```

### B.3. Integrability of iterated derivatives

**`Space.iteratedFDeriv_norm_integrable`**, a lemma, [line 599](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L599).

```lean
lemma iteratedFDeriv_norm_integrable {n} {d : ℕ} (η : 𝓢(Time × Space d, ℝ))
    (x : Space d) :
    Integrable (fun t => ‖iteratedFDeriv ℝ n ⇑η (t, x)‖) volume
```

**`Space.iteratedFDeriv_integrable`**, a lemma, [line 605](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L605).

```lean
lemma iteratedFDeriv_integrable {n} {d : ℕ} (η : 𝓢(Time × Space d, ℝ)) (x : Space d) :
    Integrable (fun t => iteratedFDeriv ℝ n ⇑η (t, x)) volume
```

## C. Decay results for derivatives of the time integral

### C.1. Moving the iterated derivative inside the time integral

**`Space.time_integral_iteratedFDeriv_apply`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L633).

```lean
lemma time_integral_iteratedFDeriv_apply {d : ℕ} (n : ℕ) (η : 𝓢(Time × Space d, ℝ)) :
    ∀ x, ∀ y, iteratedFDeriv ℝ n (fun x => ∫ (t : Time), η (t, x)) x y =
      ∫ (t : Time), (iteratedFDeriv ℝ n η (t, x)) (fun i => (0, y i))
```

**`Space.time_integral_iteratedFDeriv_eq`**, a lemma, [line 723](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L723).

```lean
lemma time_integral_iteratedFDeriv_eq {d : ℕ} (n : ℕ) (η : 𝓢(Time × Space d, ℝ))
    (x : Space d) :
    iteratedFDeriv ℝ n (fun x => ∫ (t : Time), η (t, x)) x =
      ((∫ (t : Time), iteratedFDeriv ℝ n η (t, x)).compContinuousLinearMap
      (fun _ => ContinuousLinearMap.prod (0 : Space d →L[ℝ] Time)
      (ContinuousLinearMap.id ℝ (Space d))))
```

### C.2. Bound on the norm of iterated derivative

**`Space.time_integral_iteratedFDeriv_norm_le`**, a lemma, [line 741](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L741).

```lean
lemma time_integral_iteratedFDeriv_norm_le {d : ℕ} (n : ℕ) (η : 𝓢(Time × Space d, ℝ))
    (x : Space d) :
    ‖iteratedFDeriv ℝ n (fun x => ∫ (t : Time), η (t, x)) x‖ ≤
        (∫ (t : Time), ‖iteratedFDeriv ℝ n η (t, x)‖) *
        ‖(ContinuousLinearMap.prod (0 : Space d →L[ℝ] Time)
        (ContinuousLinearMap.id ℝ (Space d)))‖ ^ n
```

### C.3. Bound on the norm of iterated derivative mul a power

**`Space.time_integral_mul_pow_iteratedFDeriv_norm_le`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L758).

```lean
lemma time_integral_mul_pow_iteratedFDeriv_norm_le {d : ℕ} (n m : ℕ) :
    ∃ rt, ∀ (η : 𝓢(Time × Space d, ℝ)),∀ (x : Space d),
    Integrable (fun x : Time => ‖((1 + ‖x‖) ^ rt)⁻¹‖) volume ∧
    ‖x‖ ^ m * ‖iteratedFDeriv ℝ n (fun x => ∫ (t : Time), η (t, x)) x‖ ≤
        ((∫ (t : Time), ‖((1 + ‖t‖) ^ rt)⁻¹‖) *
        ‖((0 : Space d →L[ℝ] Time).prod (.id ℝ (Space d)))‖ ^ n)
        * (2 ^ (rt + m, n).1 * ((Finset.Iic (rt + m, n)).sup
          fun m => SchwartzMap.seminorm ℝ m.1 m.2) η)
```

## D. The time integral as a schwartz map

**`Space.timeIntegralSchwartz`**, a def, [line 818](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L818).

> The continuous linear map taking Schwartz maps on `Time × Space d` to
> `space d` by integrating over time.

```lean
def timeIntegralSchwartz {d : ℕ} :
    𝓢(Time × Space d, ℝ) →L[ℝ] 𝓢(Space d, ℝ)
```

**`Space.timeIntegralSchwartz_apply`**, a lemma, [line 849](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L849).

```lean
lemma timeIntegralSchwartz_apply {d : ℕ} (η : 𝓢(Time × Space d, ℝ)) (x : Space d) :
    timeIntegralSchwartz η x = ∫ (t : Time), η (t, x)
```

## E. Constant time distributions

**`Space.constantTime`**, a def, [line 860](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L860).

> Distributions on `Time × Space d` from distributions on `Space d`.
> These distributions are constant in time.

```lean
def constantTime {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ} :
    ((Space d) →d[ℝ] M) →ₗ[ℝ] (Time × Space d) →d[ℝ] M
```

**`Space.constantTime_apply`**, a lemma, [line 870](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L870).

```lean
lemma constantTime_apply {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {d : ℕ} (f : (Space d) →d[ℝ] M)
    (η : 𝓢(Time × Space d, ℝ)) :
    constantTime f η = f (timeIntegralSchwartz η)
```

### E.1. Space derivatives of constant time distributions

**`Space.constantTime_distSpaceDeriv`**, a lemma, [line 880](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L880).

```lean
lemma constantTime_distSpaceDeriv {M : Type} {d : ℕ} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (i : Fin d) (f : (Space d) →d[ℝ] M) :
    Space.distSpaceDeriv i (constantTime f) = constantTime (Space.distDeriv i f)
```

### E.2. Space gradient of constant time distributions

**`Space.constantTime_distSpaceGrad`**, a lemma, [line 918](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L918).

```lean
lemma constantTime_distSpaceGrad {d : ℕ} (f : (Space d) →d[ℝ] ℝ) :
    Space.distSpaceGrad (constantTime f) = constantTime (Space.distGrad f)
```

### E.3. Space divergence of constant time distributions

**`Space.constantTime_distSpaceDiv`**, a lemma, [line 931](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L931).

```lean
lemma constantTime_distSpaceDiv {d : ℕ} (f : (Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) :
    Space.distSpaceDiv (constantTime f) = constantTime (Space.distDiv f)
```

### E.4. Space curl of constant time distributions

**`Space.constantTime_spaceCurlD`**, a lemma, [line 947](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L947).

```lean
lemma constantTime_spaceCurlD (f : (Space 3) →d[ℝ] EuclideanSpace ℝ (Fin 3)) :
    Space.distSpaceCurl (constantTime f) = constantTime (Space.distCurl f)
```

### E.5. Time derivative of constant time distributions

**`Space.constantTime_distTimeDeriv`**, a lemma, [line 963](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean#L963).

```lean
lemma constantTime_distTimeDeriv {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ}
    (f : (Space d) →d[ℝ] M) :
    Space.distTimeDeriv (constantTime f) = 0
```

## Depends on

- [Functions and distributions on Time and Space d](basic.md)

## Sources

- [Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/ConstantTimeDist.lean)
