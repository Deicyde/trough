---
declaration: module
origin: cited
lean: TimeAndSpace, TimeAndSpace.time, TimeAndSpace.space, TimeAndSpace.time_apply, TimeAndSpace.space_apply, TimeAndSpace.dist_time_le, TimeAndSpace.dist_space_le, Space.fderiv_space_eq_fderiv_curry
statement: formalized
proof: formalized
---

# Functions and distributions on Time and Space d

The module `Physlib.SpaceAndTime.TimeAndSpace.Basic`, [Physlib/SpaceAndTime/TimeAndSpace/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean): 36 declarations, 12 with a docstring.

## i. Overview

> In this module we define `TimeAndSpace d` as the product of `Time` and `Space d`, and
> prove basic lemmas about derivatives of functions and distributions on both coordinates.
>
> The derivative and distribution results are in the namespace `Space` by convention.

## ii. Key results

> - `TimeAndSpace d` : Euclidean spacetime as the product of time and space.
> - `TimeAndSpace.time` : The projection from `TimeAndSpace d` to `Time`.
> - `TimeAndSpace.space` : The projection from `TimeAndSpace d` to `Space d`.
> - `distTimeDeriv` : The derivative of a distribution on `Time × Space d` along the
>   temporal coordinate.
> - `distSpaceDeriv` : The derivative of a distribution on `Time × Space d` along the
>   spatial `i` coordinate.
> - `distSpaceGrad` : The spatial gradient of a distribution on `Time × Space d`.
> - `distSpaceDiv` : The spatial divergence of a distribution on `Time × Space d`.
> - `distSpaceCurl` : The spatial curl of a distribution on `Time × Space 3`.

## iv. References

> * None.

## A. The coordinate product and derivatives involving time and space

### A.1. The `TimeAndSpace` coordinate product

**`TimeAndSpace`**, an abbrev, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L76).

> Euclidean spacetime as the product of time and `d`-dimensional space.

```lean
abbrev TimeAndSpace (d : ℕ := 3)
```

**`TimeAndSpace.time`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L83).

> The time-coordinate projection from `TimeAndSpace d`.

```lean
noncomputable def time {d : ℕ} : TimeAndSpace d →L[ℝ] Time
```

**`TimeAndSpace.space`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L87).

> The spatial-coordinate projection from `TimeAndSpace d`.

```lean
noncomputable def space {d : ℕ} : TimeAndSpace d →L[ℝ] Space d
```

**`TimeAndSpace.time_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L91).

```lean
lemma time_apply (tx : TimeAndSpace d) :
    time tx = tx.1
```

**`TimeAndSpace.space_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L95).

```lean
lemma space_apply (tx : TimeAndSpace d) :
    space tx = tx.2
```

**`TimeAndSpace.dist_time_le`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L99).

> The time projection is nonexpanding for the product metric.

```lean
lemma dist_time_le (tx ty : TimeAndSpace d) :
    dist (time tx) (time ty) ≤ dist tx ty
```

**`TimeAndSpace.dist_space_le`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L105).

> The spatial projection is nonexpanding for the product metric.

```lean
lemma dist_space_le (tx ty : TimeAndSpace d) :
    dist (space tx) (space ty) ≤ dist tx ty
```

### A.2. Space and time derivatives in terms of curried functions

**`Space.fderiv_space_eq_fderiv_curry`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L120).

```lean
lemma fderiv_space_eq_fderiv_curry {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → Space d → M) (t : Time) (x dx : Space d)
    (hf : Differentiable ℝ ↿f) :
    fderiv ℝ (fun x' => f t x') x dx = fderiv ℝ ↿f (t, x) (0, dx)
```

**`Space.fderiv_time_eq_fderiv_curry`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L131).

```lean
lemma fderiv_time_eq_fderiv_curry {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → Space d → M) (t dt : Time) (x : Space d)
    (hf : Differentiable ℝ ↿f) :
    fderiv ℝ (fun t' => f t' x) t dt = fderiv ℝ ↿f (t, x) (dt, 0)
```

### A.3. Commuting time and space derivatives

**`Space.fderiv_time_commute_fderiv_space`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L149).

> Derivatives along space coordinates and time commute.

```lean
lemma fderiv_time_commute_fderiv_space {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Time → Space d → M) (t dt : Time) (x dx : Space d)
    (hf : ContDiff ℝ 2 ↿f) :
    fderiv ℝ (fun t' => fderiv ℝ (fun x' => f t' x') x dx) t dt
    = fderiv ℝ (fun x' => fderiv ℝ (fun t' => f t' x') t dt) x dx
```

**`Space.time_deriv_comm_space_deriv`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L173).

```lean
lemma time_deriv_comm_space_deriv {d i} {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {f : Time → Space d → M} (hf : ContDiff ℝ 2 ↿f) (t : Time) (x : Space d) :
    Time.deriv (fun t' => Space.deriv i (f t') x) t
    = Space.deriv i (fun x' => Time.deriv (fun t' => f t' x') t) x
```

### A.4. Differentiablity conditions

**`Space.space_deriv_differentiable_time`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L187).

```lean
lemma space_deriv_differentiable_time {d i} {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {f : Time → Space d → M} (hf : ContDiff ℝ 2 ↿f) (x : Space d) :
    Differentiable ℝ (fun t => Space.deriv i (f t) x)
```

**`Space.time_deriv_differentiable_space`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L208).

```lean
lemma time_deriv_differentiable_space {d } {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {f : Time → Space d → M} (hf : ContDiff ℝ 2 ↿f) (t : Time) :
    Differentiable ℝ (fun x => Time.deriv (f · x) t)
```

**`Space.curl_differentiable_time`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L229).

```lean
lemma curl_differentiable_time
    (fₜ : Time → Space → EuclideanSpace ℝ (Fin 3))
    (hf : ContDiff ℝ 2 ↿fₜ) (x : Space) :
    Differentiable ℝ (fun t => (∇ ⨯ fₜ t) x)
```

### A.5. Time derivative commute with curl

**`Space.time_deriv_curl_commute`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L245).

> Curl and time derivative commute.

```lean
lemma time_deriv_curl_commute (fₜ : Time → Space → EuclideanSpace ℝ (Fin 3))
    (t : Time) (x : Space) (hf : ContDiff ℝ 2 ↿fₜ) :
    ∂ₜ (fun t => (∇ ⨯ fₜ t) x) t = (∇ ⨯ fun x => (∂ₜ (fun t => fₜ t x) t)) x
```

### A.6. Constant of time deriative and space derivatives zero

**`Space.space_fun_of_time_deriv_eq_zero`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L273).

```lean
lemma space_fun_of_time_deriv_eq_zero {d} {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {f : Time → Space d → M} (hf : Differentiable ℝ ↿f)
    (h : ∀ t x, ∂ₜ (f · x) t = 0) :
    ∃ (g : Space d → M), ∀ t x, f t x = g x
```

**`Space.time_fun_of_space_deriv_eq_zero`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L291).

```lean
lemma time_fun_of_space_deriv_eq_zero {d} {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {f : Time → Space d → M} (hf : Differentiable ℝ ↿f)
    (h : ∀ t x i, Space.deriv i (f t) x = 0) :
    ∃ (g : Time → M), ∀ t x, f t x = g t
```

**`Space.const_of_time_deriv_space_deriv_eq_zero`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L307).

```lean
lemma const_of_time_deriv_space_deriv_eq_zero {d} {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {f : Time → Space d → M} (hf : Differentiable ℝ ↿f)
    (h₁ : ∀ t x, ∂ₜ (f · x) t = 0)
    (h₂ : ∀ t x i, Space.deriv i (f t) x = 0) :
    ∃ (c : M), ∀ t x, f t x = c
```

### A.7. Equal up to a constant of time and space derivatives equal

**`Space.equal_up_to_const_of_deriv_eq`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L324).

```lean
lemma equal_up_to_const_of_deriv_eq {d} {M} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {f g : Time → Space d → M} (hf : Differentiable ℝ ↿f) (hg : Differentiable ℝ ↿g)
    (h₁ : ∀ t x, ∂ₜ (f · x) t = ∂ₜ (g · x) t)
    (h₂ : ∀ t x i, Space.deriv i (f t) x = Space.deriv i (g t) x) :
    ∃ (c : M), ∀ t x, f t x = g t x + c
```

## B. Derivatives of distributions on Time × Space d

### B.1. Time derivatives

**`Space.distTimeDeriv`**, a def, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L360).

> The time derivative of a distribution dependent on time and space.

```lean
noncomputable def distTimeDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M] :
    ((Time × Space d) →d[ℝ] M) →ₗ[ℝ] (Time × Space d) →d[ℝ] M
```

**`Space.distTimeDeriv_apply`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L375).

```lean
lemma distTimeDeriv_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : (Time × Space d) →d[ℝ] M) (ε : 𝓢(Time × Space d, ℝ)) :
    (distTimeDeriv f) ε = fderivD ℝ f ε (1, 0)
```

**`Space.distTimeDeriv_apply'`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L380).

```lean
lemma distTimeDeriv_apply' {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : (Time × Space d) →d[ℝ] M) (ε : 𝓢(Time × Space d, ℝ)) :
    (distTimeDeriv f) ε =
    -f (SchwartzMap.evalCLM ℝ (Time × Space d) ℝ (1, 0)
    ((fderivCLM ℝ (Time × Space d) ℝ) ε))
```

**`Space.apply_fderiv_eq_distTimeDeriv`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L387).

```lean
lemma apply_fderiv_eq_distTimeDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : (Time × Space d) →d[ℝ] M) (ε : 𝓢(Time × Space d, ℝ)) :
    f (SchwartzMap.evalCLM ℝ (Time × Space d) ℝ (1, 0) ((fderivCLM ℝ (Time × Space d) ℝ) ε)) =
    - (distTimeDeriv f) ε
```

#### B.1.1. Composition with a CLM

**`Space.distTimeDeriv_apply_CLM`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L399).

```lean
lemma distTimeDeriv_apply_CLM {M M2 d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    [NormedAddCommGroup M2] [NormedSpace ℝ M2] (f : (Time × Space d) →d[ℝ] M)
    (c : M →L[ℝ] M2) : distTimeDeriv (c ∘L f) = c ∘L (distTimeDeriv f)
```

### B.2. Space derivatives

**`Space.distSpaceDeriv`**, a def, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L412).

> The space derivative of a distribution dependent on time and space.

```lean
noncomputable def distSpaceDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (i : Fin d) : ((Time × Space d) →d[ℝ] M) →ₗ[ℝ] (Time × Space d) →d[ℝ] M
```

**`Space.distSpaceDeriv_apply`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L427).

```lean
lemma distSpaceDeriv_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (i : Fin d) (f : (Time × Space d) →d[ℝ] M) (ε : 𝓢(Time × Space d, ℝ)) :
    (distSpaceDeriv i f) ε = fderivD ℝ f ε (0, basis i)
```

**`Space.distSpaceDeriv_apply'`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L432).

```lean
lemma distSpaceDeriv_apply' {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (i : Fin d) (f : (Time × Space d) →d[ℝ] M) (ε : 𝓢(Time × Space d, ℝ)) :
    (distSpaceDeriv i f) ε =
    - f ((SchwartzMap.evalCLM ℝ (Time × Space d) ℝ (0, basis i))
    ((fderivCLM ℝ (Time × Space d) ℝ) ε))
```

**`Space.apply_fderiv_eq_distSpaceDeriv`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L439).

```lean
lemma apply_fderiv_eq_distSpaceDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (i : Fin d) (f : (Time × Space d) →d[ℝ] M) (ε : 𝓢(Time × Space d, ℝ)) :
    f ((SchwartzMap.evalCLM ℝ (Time × Space d) ℝ (0, basis i))
    ((fderivCLM ℝ (Time × Space d) ℝ) ε)) =
    - (distSpaceDeriv i f) ε
```

#### B.2.1. Space derivatives commute

**`Space.distSpaceDeriv_commute`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L452).

```lean
lemma distSpaceDeriv_commute {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (i j : Fin d) (f : (Time × Space d) →d[ℝ] M) :
    distSpaceDeriv i (distSpaceDeriv j f) = distSpaceDeriv j (distSpaceDeriv i f)
```

#### B.2.2. Composition with a CLM

**`Space.distSpaceDeriv_apply_CLM`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L474).

```lean
lemma distSpaceDeriv_apply_CLM {M M2 d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    [NormedAddCommGroup M2] [NormedSpace ℝ M2]
    (i : Fin d) (f : (Time × Space d) →d[ℝ] M)
    (c : M →L[ℝ] M2) : distSpaceDeriv i (c ∘L f) = c ∘L (distSpaceDeriv i f)
```

### B.3. Time and space derivatives commute

**`Space.distTimeDeriv_commute_distSpaceDeriv`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L487).

```lean
lemma distTimeDeriv_commute_distSpaceDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (i : Fin d) (f : (Time × Space d) →d[ℝ] M) :
    distTimeDeriv (distSpaceDeriv i f) = distSpaceDeriv i (distTimeDeriv f)
```

### B.4. The spatial gradient

**`Space.distSpaceGrad`**, a def, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L510).

> The spatial gradient of a distribution dependent on time and space.

```lean
noncomputable def distSpaceGrad {d} :
    ((Time × Space d) →d[ℝ] ℝ) →ₗ[ℝ] (Time × Space d) →d[ℝ] (EuclideanSpace ℝ (Fin d))
```

**`Space.distSpaceGrad_apply`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L524).

```lean
lemma distSpaceGrad_apply {d} (f : (Time × Space d) →d[ℝ] ℝ) (ε : 𝓢(Time × Space d, ℝ)) :
    distSpaceGrad f ε = fun i => distSpaceDeriv i f ε
```

### B.5. The spatial divergence

**`Space.distSpaceDiv`**, a def, [line 535](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L535).

> The spatial divergence of a distribution dependent on time and space.

```lean
noncomputable def distSpaceDiv {d} :
    ((Time × Space d) →d[ℝ] (EuclideanSpace ℝ (Fin d))) →ₗ[ℝ] (Time × Space d) →d[ℝ] ℝ
```

**`Space.distSpaceDiv_apply_eq_sum_distSpaceDeriv`**, a lemma, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L549).

```lean
lemma distSpaceDiv_apply_eq_sum_distSpaceDeriv {d}
    (f : (Time × Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) (η : 𝓢(Time ×Space d, ℝ)) :
    distSpaceDiv f η = ∑ i, distSpaceDeriv i f η i
```

### B.6. The spatial curl

**`Space.distSpaceCurl`**, a def, [line 560](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean#L560).

> The curl of a distribution dependent on time and space.

```lean
noncomputable def distSpaceCurl : ((Time × Space 3) →d[ℝ] (EuclideanSpace ℝ (Fin 3))) →ₗ[ℝ]
    (Time × Space 3) →d[ℝ] (EuclideanSpace ℝ (Fin 3))
```

## Depends on

- [Curl on Space](../space/part-01/derivatives-curl.md)
- [Time Derivatives](../time/derivatives.md)

## Sources

- [Physlib/SpaceAndTime/TimeAndSpace/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/TimeAndSpace/Basic.lean)
