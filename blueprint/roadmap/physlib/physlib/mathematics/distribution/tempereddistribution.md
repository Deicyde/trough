---
declaration: module
origin: cited
lean: Physlib.Distribution, Physlib.Distribution.ofLinear, Physlib.Distribution.ofLinear_apply, Physlib.Distribution.fderivD, Physlib.Distribution.fderivD_apply, Physlib.Distribution.integrable_eval_of_bound, Physlib.Distribution.integralOfBound, Physlib.Distribution.integralOfBound_apply
statement: formalized
proof: formalized
---

# Distributions

The module `Physlib.Mathematics.Distribution.TemperedDistribution`, [Physlib/Mathematics/Distribution/TemperedDistribution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean): 28 declarations, 18 with a docstring; 3 private, not shown.

## i. Overview

> Distributions are often used implicitly in physics, for example the correct way to handle
> a dirac delta function is to treat it as a distribution. In this file we will
> define distributions and some properties on them.
>
> The distributions from a space `E` to space `F` can be thought of as a generalization of
> functions from `E` to `F`. We give a more precise definition of distributions below.
>
> In this file we define distributions generally. Properties of distributions directly related to
> `Space` are defined in the `Physlib.SpaceAndTime.Space` directory, for example in
> `Physlib.SpaceAndTime.Space.DistOfFunction`.

## ii. Key results

> - `E →d[𝕜] F` is the type of distributions from `E` to `F`.
> - `Distribution.derivative` and `Distribution.fourierTransform` allow us to make sense of these
>   operations that might not make sense a priori on general functions.
> - `Distribution.toTemperedDistribution` converts a Physlib distribution to a Mathlib
>   tempered distribution.
> - `Distribution.ofFiniteMeasure` is the scalar distribution associated to a finite measure.
> - `Distribution.ofFiniteMeasure_eq_iff` says that finite measures are determined by their
>   associated complex scalar distributions.
> - `Distribution.integralOfBound` integrates a family with an integrable Schwartz seminorm bound.
> - `Distribution.fderivD_integralOfBound_apply` differentiates this integral after evaluation.

## iv. References

> * None.

## A. The definition of a distribution

> In physics, we often encounter mathematical objects like the Dirac delta function `δ(x)`
> that are not functions in the traditional sense.
> Distributions provide a rigorous framework for handling such objects.
>
> The core idea is to define a "generalized function" not by its value at each point,
> but by how it acts on a set of well-behaved "test functions".
>
> These test functions, typically denoted `η`. The choice of test functions depends on the application
> here we choose test functions which are smooth and decay
> rapidly at infinity (called Schwartz maps). Thus really the distributions we are defining here
> are called tempered distributions.
>
> A distribution `u` is a linear map that takes a test function `η` and produces a value,
> which can be a scalar or a vector. This action is written as `⟪u,η⟫`.
>
> Two key examples illustrate this concept:
>
> 1. **Ordinary Functions:** Any well-behaved function `f(x)` can be viewed as a distribution.
>   Its action on a test function `η` is defined by integration:
>   `u_f(η) = ∫ f(x) η(x) dx`
>   This integral "tests" the function `f` using `η`.
>
> 2. **Dirac Delta:** The Dirac delta `δ_a` (centered at `a`) is a distribution whose action is to
>   simply evaluate the test function at `a`:
>   `δ_a(η) = η(a)`
>
> Formally, a distribution is a *continuous linear map* from the space of Schwartz functions
> `𝓢(E, 𝕜)` to a
> vector space `F` over `𝕜`. This definition allows us to rigorously define concepts
> like derivatives and Fourier transforms for these generalized functions, as we will see below.
>
> We use the notation `E →d[𝕜] F` to denote the space of distributions from `E` to `F`
> where `E` is a normed vector space over `ℝ` and `F` is a normed vector space over `𝕜`.

**`Physlib.Distribution`**, an abbrev, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L115).

> An `F`-valued distribution on `E` (where `E` is a normed vector space over `ℝ` and `F` is a
> normed vector space over `𝕜`) is a continuous linear map `𝓢(E, 𝕜) →L[𝕜] F` where `𝒮(E, 𝕜)` is
> the Schwartz space of smooth functions `E → 𝕜` with rapidly decreasing iterated derivatives. This
> is notated as `E →d[𝕜] F`.
>
> This should be seen as a generalisation of functions `E → F`.

```lean
abbrev Distribution (𝕜 E F : Type) [RCLike 𝕜] [NormedAddCommGroup E] [NormedAddCommGroup F]
    [NormedSpace ℝ E] [NormedSpace 𝕜 F] : Type
```

## B. Construction of distributions from linear maps

> Distributions are defined as **continuous** linear maps from `𝓢(E, 𝕜)` to `F`.
> It is possible to define a constructor of distributions from just linear maps
> `𝓢(E, 𝕜) →ₗ[𝕜] F` (without the continuity requirement) by imposing a condition
> on the size of `u` applied to `η`.

**`Physlib.Distribution.ofLinear`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L150).

> The construction of a distribution from the following data:
> 1. We take a finite set `s` of pairs `(k, n) ∈ ℕ × ℕ` that will be explained later.
> 2. We take a linear map `u` that evaluates the given Schwartz function `η`. At this stage we don't
>   need `u` to be continuous.
> 3. Recall that a Schwartz function `η` satisfies a bound
>   `‖x‖ᵏ * ‖(dⁿ/dxⁿ) η‖ < Mₙₖ` where `Mₙₖ : ℝ` only depends on `(k, n) : ℕ × ℕ`.
> 4. This step is where `s` is used: for each test function `η`, the norm `‖u η‖` is required to be
>   bounded by `C * (‖x‖ᵏ * ‖(dⁿ/dxⁿ) η‖)` for some `x : ℝ` and for some `(k, n) ∈ s`, where
>   `C ≥ 0` is a global scalar.

```lean
def ofLinear (s : Finset (ℕ × ℕ)) (u : 𝓢(E, 𝕜) →ₗ[𝕜] F)
    (hu : ∃ C : ℝ, 0 ≤ C ∧ ∀ η : 𝓢(E, 𝕜), ∃ (k : ℕ) (n : ℕ) (x : E), (k, n) ∈ s ∧
      ‖u η‖ ≤ C * (‖x‖ ^ k * ‖iteratedFDeriv ℝ n η x‖)) : E →d[𝕜] F
```

**`Physlib.Distribution.ofLinear_apply`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L163).

```lean
lemma ofLinear_apply (s : Finset (ℕ × ℕ)) (u : 𝓢(E, 𝕜) →ₗ[𝕜] F)
    (hu : ∃ C : ℝ, 0 ≤ C ∧ ∀ η : 𝓢(E, 𝕜), ∃ (k : ℕ) (n : ℕ) (x : E), (k, n) ∈ s ∧
      ‖u η‖ ≤ C * (‖x‖ ^ k * ‖iteratedFDeriv ℝ n η x‖))
    (η : 𝓢(E, 𝕜)) :
    ofLinear 𝕜 s u hu η = u η
```

## C. Derivatives of distributions

> Given a distribution `u : E →d[𝕜] F`, we can define the derivative of that distribution.
> In general when defining an operation on a distribution, we do it by applying a similar
> operation instead to the Schwartz maps it acts on.
>
> Thus the derivative of `u` is the distribution which takes `η` to `⟪u, - η'⟫`
> where `η'` is the derivative of `η`.
>
> The derivative commutes with finite superpositions of sources: for a family `u` and a finite
> index set `s`, the identity `fderivD 𝕜 (∑ i ∈ s, u i) = ∑ i ∈ s, fderivD 𝕜 (u i)` follows from
> `map_sum (fderivD 𝕜) u s`, since `fderivD 𝕜` is a linear map. Integrals of families of
> distributions are treated in the next subsection.

**`Physlib.Distribution.fderivD`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L208).

> The Fréchet derivative of a distribution.
>
> Informally, for a distribution `u : E →d[𝕜] F`,
> the Fréchet derivative `fderiv u x v` corresponds to the derivative of `u` at the
> point `x` in the direction `v`. For example, if `F = ℝ³`
> then `fderiv u x v` is a vector in `ℝ³` corresponding to
> `(v₁ ∂u₁/∂x₁ + v₂ ∂u₁/∂x₂ + v₃ ∂u₁/∂x₃, v₁ ∂u₂/∂x₁ + v₂ ∂u₂/∂x₂ + v₃ ∂u₂/∂x₃,...)`.
>
> Formally, for a distribution `u : E →d[𝕜] F`, this is actually defined
> the distribution which takes test function `η : E → 𝕜` to
> `- u (SchwartzMap.evalCLM v (SchwartzMap.fderivCLM 𝕜 η))`.
>
> Note that, unlike for functions, the Fréchet derivative of a distribution always exists.

```lean
def fderivD [FiniteDimensional ℝ E] : (E →d[𝕜] F) →ₗ[𝕜] (E →d[𝕜] (E →L[ℝ] F))
```

**`Physlib.Distribution.fderivD_apply`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L261).

```lean
lemma fderivD_apply [FiniteDimensional ℝ E] (u : E →d[𝕜] F) (η : 𝓢(E, 𝕜)) (v : E) :
    fderivD 𝕜 u η v = - u (SchwartzMap.evalCLM (𝕜 := 𝕜) E 𝕜 v (SchwartzMap.fderivCLM 𝕜 E 𝕜 η))
```

### C.1. Differentiating integrals of distributions

> Superpositions of generalized sources can be described by integrating families of distributions.
> We construct this weak integral when evaluations are measurable and bounded by an integrable
> coefficient times a fixed finite maximum of Schwartz seminorms. This bound ensures that the
> integral is continuous on the test functions. Distributional differentiation then commutes with
> the integral after evaluation at a test function and a direction.

**`Physlib.Distribution.integrable_eval_of_bound`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L293).

> Evaluations of a distribution family with an integrable seminorm bound are integrable.

```lean
lemma integrable_eval_of_bound (η : 𝓢(E, 𝕜)) : Integrable (fun a => u a η) μ
```

**`Physlib.Distribution.integralOfBound`**, a def, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L300).

> The weak integral of a family of distributions with an integrable Schwartz seminorm bound.
> It acts on a test function by integrating the evaluations of the family.

```lean
def integralOfBound : E →d[𝕜] F
```

**`Physlib.Distribution.integralOfBound_apply`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L321).

> Evaluation of the weak integral is the integral of the evaluations.

```lean
lemma integralOfBound_apply (η : 𝓢(E, 𝕜)) :
    integralOfBound u s b hb hmeas hbound hb_nonneg η = ∫ a, u a η ∂μ
```

**`Physlib.Distribution.integrable_fderivD_eval_of_bound`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L328).

> Differentiated evaluations of a family with an integrable seminorm bound are integrable.

```lean
lemma integrable_fderivD_eval_of_bound (η : 𝓢(E, 𝕜)) (v : E) :
    Integrable (fun a => fderivD 𝕜 (u a) η v) μ
```

**`Physlib.Distribution.fderivD_integralOfBound_apply`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L335).

> Distributional differentiation commutes with the weak integral after evaluation at a test
> function and a direction.

```lean
lemma fderivD_integralOfBound_apply (η : 𝓢(E, 𝕜)) (v : E) :
    fderivD 𝕜 (integralOfBound u s b hb hmeas hbound hb_nonneg) η v =
      ∫ a, fderivD 𝕜 (u a) η v ∂μ
```

## D. Fourier transform of distributions

> As with derivatives of distributions we can define the fourier transform of a distribution
> by taking the fourier transform of the underlying Schwartz maps. Thus the fourier transform
> of the distribution `u` is the distribution which takes `η` to `⟪u, F[η]⟫` where `F[η]` is the
> fourier transform of `η`.

**`Physlib.Distribution.fourierTransform`**, a def, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L361).

> Definition of Fourier transform of distribution: Let `u` be a distribution. Then its Fourier
> transform is `F{u}` where given a test function `η`, `F{u}(η) := u(F{η})`.

```lean
def fourierTransform : (E →d[ℂ] F) →ₗ[ℂ] (E →d[ℂ] F)
```

**`Physlib.Distribution.fourierTransform_apply`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L366).

```lean
lemma fourierTransform_apply (u : E →d[ℂ] F) (η : 𝓢(E, ℂ)) :
    u.fourierTransform E F η = u (fourierTransformCLM ℂ η)
```

### D.1. Bridge to Mathlib tempered distributions

> Mathlib's tempered distributions use the pointwise convergence topology on the same underlying
> continuous linear maps. The following construction converts Physlib distributions to that API.

**`Physlib.Distribution.toTemperedDistribution`**, a def, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L385).

> The Mathlib tempered distribution associated to a Physlib distribution.

```lean
def toTemperedDistribution (u : E →d[ℂ] F) : 𝓢'(E, F)
```

**`Physlib.Distribution.toTemperedDistribution_apply`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L389).

```lean
lemma toTemperedDistribution_apply (u : E →d[ℂ] F) (η : 𝓢(E, ℂ)) :
    u.toTemperedDistribution η = u η
```

**`Physlib.Distribution.toTemperedDistribution_fourierTransform`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L402).

> Conversion to Mathlib tempered distributions commutes with the Fourier transform.

```lean
lemma toTemperedDistribution_fourierTransform (u : E →d[ℂ] F) :
    (u.fourierTransform E F).toTemperedDistribution = 𝓕 u.toTemperedDistribution
```

## E. Specific distributions

> We now define specific distributions, which are used throughout physics. In particular, we define:
> - The constant distribution.
> - Distributions associated to finite measures.
> - The dirac delta distribution.
> - The heaviside step function.

### E.1. The constant distribution

> The constant distribution is the distribution which corresponds to a constant function,
> it takes `η` to the integral of `η` over the volume measure.

**`Physlib.Distribution.const`**, a def, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L438).

> The constant distribution `E →d[𝕜] F`, for a given `c : F` this corresponds
> to the integral `∫ x, η x • c ∂MeasureTheory.volume`.

```lean
def const [hμ : Measure.HasTemperateGrowth (volume (α := E))] (c : F) : E →d[𝕜] F
```

**`Physlib.Distribution.const_apply`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L481).

```lean
lemma const_apply [hμ : Measure.HasTemperateGrowth (volume (α := E))] (c : F)
    (η : 𝓢(E, 𝕜)) :
    const 𝕜 E c η = ∫ x, η x • c ∂MeasureTheory.volume
```

**`Physlib.Distribution.fderivD_const`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L491).

```lean
lemma fderivD_const [hμ : Measure.IsAddHaarMeasure (volume (α := E))]
    [FiniteDimensional ℝ E] (c : F) :
    fderivD ℝ (const ℝ E c) = 0
```

### E.2. Distributions associated to finite measures

> Every finite measure has temperate growth, so integrating Schwartz maps against it defines a
> scalar distribution.

**`Physlib.Distribution.ofFiniteMeasure`**, a def, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L527).

> The scalar distribution associated to a finite measure, acting on a Schwartz map by
> integration.

```lean
def ofFiniteMeasure (μ : Measure E) [IsFiniteMeasure μ] : E →d[𝕜] 𝕜
```

**`Physlib.Distribution.ofFiniteMeasure_apply`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L531).

```lean
lemma ofFiniteMeasure_apply (μ : Measure E) [IsFiniteMeasure μ] (η : 𝓢(E, 𝕜)) :
    ofFiniteMeasure 𝕜 μ η = ∫ x, η x ∂μ
```

**`Physlib.Distribution.toTemperedDistribution_ofFiniteMeasure`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L538).

> The finite-measure distribution agrees with Mathlib's tempered distribution associated to the
> same measure.

```lean
lemma toTemperedDistribution_ofFiniteMeasure (μ : Measure E) [IsFiniteMeasure μ] :
    (ofFiniteMeasure ℂ μ).toTemperedDistribution = μ.toTemperedDistribution
```

**`Physlib.Distribution.ofFiniteMeasure_eq_iff`**, a lemma, [line 638](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L638).

> The complex scalar distribution associated to a finite measure determines the measure.

```lean
lemma ofFiniteMeasure_eq_iff
    {E : Type} [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E]
    [BorelSpace E] [SecondCountableTopology E] [FiniteDimensional ℝ E]
    {μ ν : Measure E} [IsFiniteMeasure μ] [IsFiniteMeasure ν] :
    ofFiniteMeasure ℂ μ = ofFiniteMeasure ℂ ν ↔ μ = ν
```

### E.3. The dirac delta distribution

> The dirac delta distribution centered at `a : E` is the distribution which takes
> `η` to `η a`. We also define `diracDelta'` which takes in an element of `v` of `F` and
> outputs `η a • v`.

**`Physlib.Distribution.diracDelta`**, a def, [line 668](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L668).

> Dirac delta distribution `diracDelta 𝕜 a : E →d[𝕜] 𝕜` takes in a test function `η : 𝓢(E, 𝕜)`
> and outputs `η a`. Intuitively this is an infinite density at a single point `a`.

```lean
def diracDelta (a : E) : E →d[𝕜] 𝕜
```

**`Physlib.Distribution.diracDelta_apply`**, a lemma, [line 672](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L672).

```lean
lemma diracDelta_apply (a : E) (η : 𝓢(E, 𝕜)) :
    diracDelta 𝕜 a η = η a
```

**`Physlib.Distribution.diracDelta'`**, a def, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L679).

> Dirac delta in a given direction `v : F`. `diracDelta' 𝕜 a v` takes in a test function
> `η : 𝓢(E, 𝕜)` and outputs `η a • v`. Intuitively this is an infinitely intense vector field
> at a single point `a` pointing at the direction `v`.

```lean
def diracDelta' (a : E) (v : F) : E →d[𝕜] F
```

**`Physlib.Distribution.diracDelta'_apply`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L682).

```lean
lemma diracDelta'_apply (a : E) (v : F) (η : 𝓢(E, 𝕜)) :
    diracDelta' 𝕜 a v η = η a • v
```

### E.4. The heaviside step function

> The heaviside step function on `EuclideanSpace ℝ (Fin d.succ)` is the distribution
> from `EuclideanSpace ℝ (Fin d.succ)` to `ℝ` which takes a `η` to the integral of `η` in the
> upper-half plane (determined by the last coordinate in `EuclideanSpace ℝ (Fin d.succ)`).

**`Physlib.Distribution.heavisideStep`**, a def, [line 700](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L700).

> The Heaviside step distribution defined on `(EuclideanSpace ℝ (Fin d.succ)) `
> equal to `1` in the positive `z`-direction and `0` in the negative `z`-direction.

```lean
def heavisideStep (d : ℕ) : (EuclideanSpace ℝ (Fin d.succ)) →d[ℝ] ℝ
```

**`Physlib.Distribution.heavisideStep_apply`**, a lemma, [line 739](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean#L739).

```lean
lemma heavisideStep_apply (d : ℕ) (η : 𝓢(EuclideanSpace ℝ (Fin d.succ), ℝ)) :
    heavisideStep d η = ∫ x in {x : EuclideanSpace ℝ (Fin d.succ) | 0 < x (Fin.last d)},
      η x ∂MeasureTheory.volume
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Distribution/TemperedDistribution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/TemperedDistribution.lean)
