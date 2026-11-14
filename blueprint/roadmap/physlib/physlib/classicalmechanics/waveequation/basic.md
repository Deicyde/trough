---
declaration: module
origin: cited
lean: ClassicalMechanics.planeWave_waveEquation, ClassicalMechanics.WaveEquation, ClassicalMechanics.planeWave, ClassicalMechanics.planeWave_eq, ClassicalMechanics.planeWave_differentiable_time, ClassicalMechanics.planeWave_differentiable_space, ClassicalMechanics.planeWave_differentiable, ClassicalMechanics.planeWave_time_deriv
statement: formalized
proof: formalized
---

# Wave equation

The module `Physlib.ClassicalMechanics.WaveEquation.Basic`, [Physlib/ClassicalMechanics/WaveEquation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean): 21 declarations, 4 with a docstring, 1 listed as significant.

## i. Overview

> In this module we define the wave equation in `d`-dimensional Euclidean space,
> and prove that plane waves are solutions to the wave equation.
> By a plne wave we mean a function of the form `f(t, x) = f₀(⟪x, s⟫_ℝ - c * t)` where
> `s` is a direction vector and `c` is the propagation speed.

## ii. Key results

> - `WaveEquation`: The general form of the wave equation where `c` is the propagation speed.
> - `planeWave`: A vector-valued plane wave travelling in the direction of `s` with
>   propagation speed `c`.
> - `planeWave_waveEquation`: The plane wave satisfies the wave equation.

## iv. References

> * None.

## A. The wave equation

**`ClassicalMechanics.WaveEquation`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L60).

> The general form of the wave equation where `c` is the propagation speed.

```lean
def WaveEquation {d} (f : Time → Space d → EuclideanSpace ℝ (Fin d))
    (t : Time) (x : Space d) (c : ℝ) : Prop
```

## B. Plane wave solutions

### B.1. Definition of a plane wave

**`ClassicalMechanics.planeWave`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L77).

> A vector-valued plane wave travelling in the direction of `s` with propagation speed `c`.

```lean
noncomputable def planeWave (f₀ : ℝ → EuclideanSpace ℝ (Fin d))
    (c : ℝ) (s : Direction d) : Time → Space d → EuclideanSpace ℝ (Fin d)
```

**`ClassicalMechanics.planeWave_eq`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L81).

```lean
lemma planeWave_eq {d f₀ c x} {s : Direction d} :
    planeWave f₀ c s t x = f₀ (⟪x, s.unit⟫_ℝ - c * t)
```

### B.2. Differentiablity conditions

**`ClassicalMechanics.planeWave_differentiable_time`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L92).

```lean
lemma planeWave_differentiable_time {d f₀ c x} {s : Direction d}
    (h' : Differentiable ℝ f₀) :
    Differentiable ℝ (fun t => planeWave f₀ c s t x)
```

**`ClassicalMechanics.planeWave_differentiable_space`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L99).

```lean
lemma planeWave_differentiable_space {d f₀ c t} {s : Direction d}
    (h' : Differentiable ℝ f₀) :
    Differentiable ℝ (fun x => planeWave f₀ c s t x)
```

**`ClassicalMechanics.planeWave_differentiable`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L112).

```lean
lemma planeWave_differentiable {s : Direction d}
    {f₀ : ℝ → EuclideanSpace ℝ (Fin d)}
    (h' : Differentiable ℝ f₀) : Differentiable ℝ ↿(planeWave f₀ c s)
```

### B.3. Time derivatives of plane waves

**`ClassicalMechanics.planeWave_time_deriv`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L130).

```lean
lemma planeWave_time_deriv {d f₀ c x} {s : Direction d}
    (h' : Differentiable ℝ f₀) :
    ∂ₜ (planeWave f₀ c s · x) = -c • fun t => planeWave (fderiv ℝ f₀ · 1) c s t x
```

**`ClassicalMechanics.planeWave_time_deriv_time_deriv`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L146).

```lean
lemma planeWave_time_deriv_time_deriv {d f₀ c x} {s : Direction d}
    (h' : ContDiff ℝ 2 f₀) :
    ∂ₜ (∂ₜ (planeWave f₀ c s · x)) = c ^ 2 • fun t => planeWave (iteratedDeriv 2 f₀) c s t x
```

### B.4. Space derivatives of plane waves

**`ClassicalMechanics.planeWave_space_deriv`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L173).

```lean
lemma planeWave_space_deriv {d f₀ c} {s : Direction d}
    (h' : Differentiable ℝ f₀) (i : Fin d) :
    ∂[i] (planeWave f₀ c s t) =
    s.unit i • fun x => planeWave (fderiv ℝ f₀ · 1) c s t x
```

**`ClassicalMechanics.planeWave_apply_space_deriv`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L192).

```lean
lemma planeWave_apply_space_deriv {d f₀ c} {s : Direction d}
    (h' : Differentiable ℝ f₀) (i j : Fin d) :
    ∂[i] (fun x => planeWave f₀ c s t x j) =
    s.unit i • fun x => planeWave (fderiv ℝ f₀ · 1) c s t x j
```

**`ClassicalMechanics.planeWave_space_deriv_space_deriv`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L208).

```lean
lemma planeWave_space_deriv_space_deriv {d f₀ c} {s : Direction d}
    (h' : ContDiff ℝ 2 f₀) (i : Fin d) :
    ∂[i] (∂[i] (planeWave f₀ c s t)) =
    s.unit i ^ 2 • fun x => planeWave (iteratedDeriv 2 f₀ ·) c s t x
```

**`ClassicalMechanics.planeWave_apply_space_deriv_space_deriv`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L230).

```lean
lemma planeWave_apply_space_deriv_space_deriv {d f₀ c} {s : Direction d}
    (h' : ContDiff ℝ 2 f₀) (i j : Fin d) :
    ∂[i] (∂[i] (fun x => planeWave f₀ c s t x j)) =
    (s.unit i) ^ 2 • fun x => planeWave (iteratedDeriv 2 f₀ ·) c s t x j
```

### B.5. Laplacian of plane waves

**`ClassicalMechanics.planeWave_laplacian`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L257).

```lean
lemma planeWave_laplacian {d f₀ c} {s : Direction d} (h' : ContDiff ℝ 2 f₀) :
    Δᵥ (planeWave f₀ c s t) = fun x => planeWave (iteratedDeriv 2 f₀ ·) c s t x
```

### B.6. Plane waves satisfy the wave equation

**`ClassicalMechanics.planeWave_waveEquation`**, a theorem, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L277). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The plane wave satisfies the wave equation.

```lean
theorem planeWave_waveEquation (c : ℝ) (s : Direction d)
    (f₀ : ℝ → EuclideanSpace ℝ (Fin d)) (hf₀ : ContDiff ℝ 2 f₀) :
    ∀ t x, WaveEquation (planeWave f₀ c s) t x c
```

## C. Old lemmas used throughout files

> …

**`ClassicalMechanics.wave_differentiable`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L292).

```lean
lemma wave_differentiable {s : Direction d} {c : ℝ} {x : Space d} :
    DifferentiableAt ℝ (fun x => inner ℝ x s.unit - c * t) x
```

**`ClassicalMechanics.wave_dx2`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L298).

```lean
lemma wave_dx2 {u v : Fin d} {s : Direction d}
    {f₀' : ℝ → ℝ →L[ℝ] EuclideanSpace ℝ (Fin d)} {f₀'' : ℝ → ℝ →L[ℝ] EuclideanSpace ℝ (Fin d)}
    (h'' : ∀ x, HasFDerivAt (fun x' => f₀' x' 1) (f₀'' x) x) :
    (fderiv ℝ (fun x' => (inner ℝ ((f₀' (inner ℝ x' s.unit - c * t)) (s.unit u))
    (EuclideanSpace.single v 1))) x) (Space.basis u)
    =
    inner ℝ ((s.unit u) ^ 2 • f₀'' (inner ℝ x s.unit - c * t) 1) (EuclideanSpace.single v 1)
```

**`ClassicalMechanics.space_fderiv_of_inner_product_wave_eq_space_fderiv`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L350).

> If `f₀` is a function of `(inner ℝ x s - c * t)`, the fderiv of its components
> with respect to spatial coordinates is equal to the corresponding component of
> the propagation direction `s` times time derivative.

```lean
lemma space_fderiv_of_inner_product_wave_eq_space_fderiv
    {t : Time} {f₀ : ℝ → EuclideanSpace ℝ (Fin d)}
    {s : Direction d} {u v : Fin d} (h' : Differentiable ℝ f₀) :
    c * ((fun x' => (fderiv ℝ (fun x => inner ℝ (f₀ (inner ℝ x s.unit - c * t))
    (EuclideanSpace.single v 1)) x') ((Space.basis u))) x)
    =
    - s.unit u * ∂ₜ (fun t => f₀ (inner ℝ x s.unit - c * t)) t v
```

**`ClassicalMechanics.time_differentiable_of_eq_planewave`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L367).

```lean
lemma time_differentiable_of_eq_planewave {s : Direction d}
    {f₀ : ℝ → EuclideanSpace ℝ (Fin d)} {f : Time → Space d → EuclideanSpace ℝ (Fin d)}
    (h' : Differentiable ℝ f₀) (hf : f = planeWave f₀ c s) :
    Differentiable ℝ fun t => f t x
```

**`ClassicalMechanics.crossProduct_time_differentiable_of_right_eq_planewave`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L377).

```lean
lemma crossProduct_time_differentiable_of_right_eq_planewave {s : Direction}
    {f₀ : ℝ → EuclideanSpace ℝ (Fin 3)} {f : Time → Space → EuclideanSpace ℝ (Fin 3)}
    (h' : Differentiable ℝ f₀) (hf : f = planeWave f₀ c s) :
    DifferentiableAt ℝ (fun t => Space.basis.repr s.unit ⨯ₑ₃ (f t x)) t
```

**`ClassicalMechanics.crossProduct_differentiable_of_right_eq_planewave`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L390).

```lean
lemma crossProduct_differentiable_of_right_eq_planewave {s : Direction}
    {f₀ : ℝ → EuclideanSpace ℝ (Fin 3)} (h' : Differentiable ℝ f₀) :
    DifferentiableAt ℝ (fun u => Space.basis.repr s.unit ⨯ₑ₃ (f₀ u)) u
```

**`ClassicalMechanics.wave_fderiv_inner_eq_inner_fderiv_proj`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean#L408).

```lean
lemma wave_fderiv_inner_eq_inner_fderiv_proj {f₀ : ℝ → EuclideanSpace ℝ (Fin d)}
    {s : Direction d} {i : Fin d} (h' : Differentiable ℝ f₀) :
    ∀ x y, s.unit i * (fderiv ℝ (fun x => f₀ (inner ℝ x s.unit - c * t)) x) y i
    =
    inner ℝ y s.unit * (fderiv ℝ (fun x => f₀ (inner ℝ x s.unit - c * t) i) x)
    (Space.basis i)
```

## Depends on

- [The Laplacian operator on `Space d`](../../spaceandtime/space/part-01/derivatives-laplacian.md)
- [Time Derivatives](../../spaceandtime/time/derivatives.md)

## Proof depends on

- [The cross product on Euclidean vectors in three dimensions](../../spaceandtime/space/part-01/crossproduct.md)

## Sources

- [Physlib/ClassicalMechanics/WaveEquation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/WaveEquation/Basic.lean)
