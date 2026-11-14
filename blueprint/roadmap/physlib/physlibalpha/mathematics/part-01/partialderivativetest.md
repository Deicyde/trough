---
declaration: module
origin: cited
lean: QuadraticMap.toMultilinearMap_continuous, QuadraticMap.toMultilinearMapHalfPolarBilin_continuous, QuadraticMap.toContinuousMultilinearMap_apply, QuadraticMap.toContinuousMultilinearMap_applyHalf, le_of_littleO, isLocalMin_of_posDef_of_littleo, second_derivative_test, second_derivative_test_analyticAt
statement: formalized
proof: formalized
---

# The Second Partial Derivatives Test

The module `PhyslibAlpha.Mathematics.PartialDerivativeTest`, [PhyslibAlpha/Mathematics/PartialDerivativeTest.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean): 24 declarations, 23 with a docstring, 8 listed as significant.

> A positive definite Hessian at a critical point of an analytic function gives a local minimum.

## i. Overview

> We prove a version of the second partial derivative test from calculus for
> analytic functions `f : V → ℝ`, where `V` is a finite-dimensional vector space.
>
> The second iterated Fréchet derivative is packaged as a quadratic map, a positive definite
> quadratic map is shown to be coercive, and a little-o form of the test is combined with the
> quadratic approximation coming from a power series.
>
> Tags: partial derivative test, calculus.

## ii. Key results

> - `iteratedFDerivQuadraticMap` : the second iterated Fréchet derivative as a quadratic map.
> - `coercive_of_posdef` : positive definiteness implies coercivity.
> - `isLocalMin_of_posDef_of_littleo` : the second partial derivative test, "little oh" form.
> - `second_derivative_test` : Suppose `f` is a real-valued function on a finite-dimensional inner
>   product space that has vanishing gradient at `x₀`, and has a power series on a ball of positive
>   radius around `x₀`. If the second Fréchet derivative is positive definite at `x₀` then `f` has a
>   local minimum at `x₀`.
> - `second_derivative_test_analyticAt` : the same test, assuming only that `f` is analytic at `x₀`.

## iv. References

> * None.

## A. Updating vectors of length two

**`Function.update₀`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L62).

> Update a vector of length 2 in coordinate 0.

```lean
lemma Function.update₀ {α : Type*} {a b c : α} : Function.update ![a,b] 0 c = ![c,b]
```

**`Function.update₁`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L67).

> Update a vector of length 2 in coordinate 1.

```lean
lemma Function.update₁ {α : Type*} {a b c : α} : Function.update ![a,b] 1 c = ![a,c]
```

## B. Quadratic maps from the second derivative

**`hessianBilinearCompanion`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L80).

> The Hessian companion as a bilinear map.

```lean
noncomputable def hessianBilinearCompanion {V : Type*} [NormedAddCommGroup V]
    [NormedSpace ℝ V] (f : V → ℝ) (x₀ : V) : V →ₗ[ℝ] V →ₗ[ℝ] ℝ
```

**`iteratedFDerivQuadraticMap`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L107).

> The second iterated Frechét derivative as a quadratic map.

```lean
noncomputable def iteratedFDerivQuadraticMap {V : Type*} [NormedAddCommGroup V]
    [NormedSpace ℝ V] (f : V → ℝ) (x₀ : V) : QuadraticMap ℝ V ℝ
```

**`continuousBilinearMapOfContinuousMultilinearMap`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L130).

> A continuous multilinear map is bilinear.

```lean
noncomputable def continuousBilinearMapOfContinuousMultilinearMap
    {𝕜 : Type*} [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜]
    {V : Type*}
    [NormedAddCommGroup V] [NormedSpace 𝕜 V] [FiniteDimensional 𝕜 V]
    (g : ContinuousMultilinearMap 𝕜 (fun _ : Fin 2 => V) 𝕜) : V →L[𝕜] V →L[𝕜] 𝕜
```

**`QuadraticMap.toMultilinearMap`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L147).

> .

```lean
def QuadraticMap.toMultilinearMap {V : Type*} [AddCommGroup V] [Module ℝ V]
    (Q : QuadraticMap ℝ V ℝ) : MultilinearMap ℝ (fun _ : Fin 2 => V) ℝ
```

**`QuadraticMap.toMultilinearMapHalfPolarBilin`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L155).

> .

```lean
noncomputable def QuadraticMap.toMultilinearMapHalfPolarBilin
    {V : Type*} [AddCommGroup V] [Module ℝ V]
    (Q : QuadraticMap ℝ V ℝ) :
    MultilinearMap ℝ (fun _ : Fin 2 => V) ℝ
```

**`QuadraticMap.toMultilinearMap_continuous`**, a theorem, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L185). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The multilinear map associated to a quadratic map is continuous.

```lean
theorem QuadraticMap.toMultilinearMap_continuous {V : Type*}
    [NormedAddCommGroup V] [NormedSpace ℝ V]
    [FiniteDimensional ℝ V] (Q : QuadraticMap ℝ V ℝ) : Continuous Q.toMultilinearMap
```

**`QuadraticMap.toMultilinearMapHalfPolarBilin_continuous`**, a theorem, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L214). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> .

```lean
theorem QuadraticMap.toMultilinearMapHalfPolarBilin_continuous {V : Type*}
    [NormedAddCommGroup V] [NormedSpace ℝ V]
    [FiniteDimensional ℝ V] (Q : QuadraticMap ℝ V ℝ) :
    Continuous Q.toMultilinearMapHalfPolarBilin
```

**`QuadraticMap.toContinuousMultilinearMap`**, a def, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L291).

> Construct a continuous multilinear map from a quadratic map on a finite dimensional space.

```lean
def QuadraticMap.toContinuousMultilinearMap {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
    [FiniteDimensional ℝ V] (Q : QuadraticMap ℝ V ℝ) :
    ContinuousMultilinearMap ℝ (fun _ : Fin 2 ↦ V) ℝ
```

**`QuadraticMap.toContinuousMultilinearMapHalfPolarBilin`**, a def, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L298).

> .

```lean
noncomputable def QuadraticMap.toContinuousMultilinearMapHalfPolarBilin {V : Type*}
    [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] (Q : QuadraticMap ℝ V ℝ) :
    ContinuousMultilinearMap ℝ (fun _ : Fin 2 ↦ V) ℝ
```

**`QuadraticMap.toContinuousMultilinearMap_apply`**, a theorem, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L307). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The constructed continuous multilinear map agrees with the polar bilinear form.

```lean
theorem QuadraticMap.toContinuousMultilinearMap_apply {V : Type*} [NormedAddCommGroup V]
    [NormedSpace ℝ V] [FiniteDimensional ℝ V] (Q : QuadraticMap ℝ V ℝ) (x y : V) :
    Q.toContinuousMultilinearMap ![x, y] = Q.polarBilin x y
```

**`QuadraticMap.toContinuousMultilinearMap_applyHalf`**, a theorem, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L313). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> .

```lean
theorem QuadraticMap.toContinuousMultilinearMap_applyHalf {V : Type*} [NormedAddCommGroup V]
    [NormedSpace ℝ V] [FiniteDimensional ℝ V] (Q : QuadraticMap ℝ V ℝ) (x y : V) :
    Q.toContinuousMultilinearMapHalfPolarBilin ![x, y] = (1/2) * Q.polarBilin x y
```

## C. Coercivity of positive definite forms

**`coercive_of_posdefHalf`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L326).

> .

```lean
lemma coercive_of_posdefHalf {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
    [FiniteDimensional ℝ V] {F : QuadraticMap ℝ V ℝ}
    (hf' : F.PosDef) :
    IsCoercive (continuousBilinearMapOfContinuousMultilinearMap
        F.toContinuousMultilinearMapHalfPolarBilin)
```

**`polarBilin_iteratedFDerivQuadraticMap`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L402).

> The polar bilinear form of the second-derivative quadratic map is the symmetrized
> Hessian.

```lean
lemma polarBilin_iteratedFDerivQuadraticMap {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (f : V → ℝ) (x₀ : V) (x y : V) :
    (iteratedFDerivQuadraticMap f x₀).polarBilin x y
      = iteratedFDeriv ℝ 2 f x₀ ![x, y] + iteratedFDeriv ℝ 2 f x₀ ![y, x]
```

**`iteratedFDeriv_two_swap`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L415).

> Symmetry of the second iterated Fréchet derivative (Schwarz's theorem).

```lean
lemma iteratedFDeriv_two_swap {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
    {f : V → ℝ} {x₀ : V} (hf : ContDiffAt ℝ ⊤ f x₀) (x y : V) :
    iteratedFDeriv ℝ 2 f x₀ ![y, x] = iteratedFDeriv ℝ 2 f x₀ ![x, y]
```

**`coercive_of_posdef_of_contdiff`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L432).

> Positive definiteness implies coercivity.
> The proof uses the general fact `coercive_of_posdefHalf`
> but requires a differentiability assumption on `f`.

```lean
lemma coercive_of_posdef_of_contdiff {V : Type*}
    [NormedAddCommGroup V] [NormedSpace ℝ V]
    [FiniteDimensional ℝ V] {f : V → ℝ} {x₀ : V}
    (hf : ContDiffAt ℝ ⊤ f x₀)
    (hf' : (iteratedFDerivQuadraticMap f x₀).PosDef) :
    IsCoercive (continuousBilinearMapOfContinuousMultilinearMap
        (iteratedFDeriv ℝ 2 f x₀))
```

**`coercive_of_posdef`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L455).

> Positive definiteness implies coercivity.

```lean
lemma coercive_of_posdef {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
    [FiniteDimensional ℝ V] {f : V → ℝ} {x₀ : V}
    (hf' : (iteratedFDerivQuadraticMap f x₀).PosDef) :
    IsCoercive (continuousBilinearMapOfContinuousMultilinearMap
        (iteratedFDeriv ℝ 2 f x₀))
```

## D. The second derivative test

**`le_of_littleO`**, a theorem, [line 514](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L514). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> .

```lean
theorem le_of_littleO {V : Type*}
    [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    {f : V → ℝ} {x₀ x : V} {C : ℝ}
    (hx : C * (‖x - x₀‖ ^ 2) ≤ iteratedFDeriv ℝ 2 f x₀ fun _ ↦ x - x₀)
    (hx₀ : fderiv ℝ f x₀ x = fderiv ℝ f x₀ x₀)
    (h₁ : ‖f x - ∑ i ∈ range 3, 1 / ↑i ! * iteratedFDeriv ℝ i f x₀ fun _ ↦ x - x₀‖
      ≤ C / 2 * ‖x - x₀‖ ^ 2) :
  f x₀ ≤ f x
```

**`isLocalMin_of_posDef_of_littleo`**, a theorem, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L534). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Second partial derivative test, "little oh" form.

```lean
theorem isLocalMin_of_posDef_of_littleo {V : Type*} [NormedAddCommGroup V]
    [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {f : V → ℝ} {x₀ : V}
    (h : (fun x => f x - ∑ i ∈ range 3, 1 / (i)! * iteratedFDeriv ℝ i f x₀ fun _ => x - x₀)
      =o[nhds x₀] fun x => ‖x - x₀‖ ^ 2) (h₀ : gradient f x₀ = 0) (hcd : ContDiffAt ℝ ⊤ f x₀)
    (hf : (iteratedFDerivQuadraticMap f x₀).PosDef) : IsLocalMin f x₀
```

**`littleO_of_powerseries`**, a lemma, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L558).

> Having a power series implies quadratic approximation.

```lean
lemma littleO_of_powerseries {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]
    {f : V → ℝ} {x₀ : V} {p : FormalMultilinearSeries ℝ V ℝ}
    {r : NNReal} (h : HasFPowerSeriesOnBall f p x₀ r) :
    (fun x => f x - p.partialSum 3 (x - x₀)) =o[nhds x₀] fun x => ‖x - x₀‖ ^ 2
```

**`isLocalMin.of_subsingleton`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L571).

```lean
lemma isLocalMin.of_subsingleton {V : Type*} [TopologicalSpace V]
    [Subsingleton V] {f : V → ℝ} {x₀ : V} : IsLocalMin f x₀
```

**`second_derivative_test`**, a theorem, [line 576](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L576). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The second partial derivative test.

```lean
theorem second_derivative_test {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    [FiniteDimensional ℝ V] {f : V → ℝ} {x₀ : V} {p : FormalMultilinearSeries ℝ V ℝ}
    (h₀ : gradient f x₀ = 0) {r : NNReal}
    (h₁ : HasFPowerSeriesOnBall f p x₀ r)
    (hf : (iteratedFDerivQuadraticMap f x₀).PosDef) : IsLocalMin f x₀
```

**`second_derivative_test_analyticAt`**, a theorem, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean#L600). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A more convenient form of the second partial derivative test: it suffices that `f`
> is analytic at `x₀` (so that an explicit power series need not be produced by hand).

```lean
theorem second_derivative_test_analyticAt {V : Type*} [NormedAddCommGroup V]
    [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {f : V → ℝ} {x₀ : V}
    (h₀ : gradient f x₀ = 0) (han : AnalyticAt ℝ f x₀)
    (hf : (iteratedFDerivQuadraticMap f x₀).PosDef) : IsLocalMin f x₀
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/PartialDerivativeTest.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/PartialDerivativeTest.lean)
