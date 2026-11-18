---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.harmonicWaveX, Electromagnetism.ElectromagneticPotential.harmonicWaveX_inl_zero, Electromagnetism.ElectromagneticPotential.harmonicWaveX_inr_zero, Electromagnetism.ElectromagneticPotential.harmonicWaveX_differentiable, Electromagnetism.ElectromagneticPotential.harmonicWaveX_contDiff, Electromagnetism.ElectromagneticPotential.harmonicWaveX_scalarPotential_eq_zero, Electromagnetism.ElectromagneticPotential.harmonicWaveX_vectorPotential_zero_eq_zero, Electromagnetism.ElectromagneticPotential.harmonicWaveX_vectorPotential_succ
statement: formalized
proof: formalized
---

# Harmonic Wave in Vacuum

The module `Physlib.Electromagnetism.Vacuum.HarmonicWave`, [Physlib/Electromagnetism/Vacuum/HarmonicWave.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean): 24 declarations, 1 with a docstring.

## i. Overview

> In this module we define the electromagnetic potential for a monochromatic harmonic wave
> travelling in the x-direction in free space, and prove various properties about it,
> including that it satisfies Maxwell's equations in free space, that it is a plane wave.
>
> We work here in a general dimension `d` so we use the magnetic field is the
> form of a matrix rather than a vector.

## ii. Key results

> - `harmonicWaveX` : Definition of the electromagnetic
>   potential for a harmonic wave travelling in the x-direction.
> - `harmonicWaveX_isExtrema` : The harmonic wave satisfies Maxwell's equations in free space.
> - `harmonicWaveX_isPlaneWave` : The harmonic wave is a plane wave.
> - `harmonicWaveX_polarization_ellipse` : The polarization ellipse equation for the harmonic wave.

## iv. References

> * None.

## A. The electromagnetic potential for a harmonic wave

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L78).

> The electromagnetic potential for a Harmonic wave travelling in the `x`-direction
> with wave number `k`.

```lean
noncomputable def harmonicWaveX (𝓕 : FreeSpace) (k : ℝ) (E₀ : Fin d → ℝ)
  (φ : Fin d → ℝ) : ElectromagneticPotential d.succ
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_inl_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L88).

```lean
lemma harmonicWaveX_inl_zero {d} (𝓕 : FreeSpace) (k : ℝ) (E₀ : Fin d → ℝ) (φ : Fin d → ℝ)
    (x : SpaceTime d.succ) :
    harmonicWaveX 𝓕 k E₀ φ x (Sum.inl 0) = 0
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_inr_zero`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L94).

```lean
lemma harmonicWaveX_inr_zero {d} (𝓕 : FreeSpace) (k : ℝ) (E₀ : Fin d → ℝ) (φ : Fin d → ℝ)
    (x : SpaceTime d.succ) :
    harmonicWaveX 𝓕 k E₀ φ x (Sum.inr 0) = 0
```

### A.1. Differentiability of the electromagnetic potential

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_differentiable`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L106).

```lean
lemma harmonicWaveX_differentiable {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) :
    Differentiable ℝ (harmonicWaveX 𝓕 k E₀ φ)
```

### A.2. Smoothness of the electromagnetic potential

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_contDiff`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L124).

```lean
lemma harmonicWaveX_contDiff {d} (n : WithTop ℕ∞) (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) :
    ContDiff ℝ n (harmonicWaveX 𝓕 k E₀ φ)
```

## B. The scalar potential

> The scalar potential of the harmonic wave is zero.

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_scalarPotential_eq_zero`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L145).

```lean
lemma harmonicWaveX_scalarPotential_eq_zero {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) :
    (harmonicWaveX 𝓕 k E₀ φ).scalarPotential 𝓕.c = 0
```

## C. The vector potential

### C.1. Components of the vector potential

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_vectorPotential_zero_eq_zero`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L165).

```lean
lemma harmonicWaveX_vectorPotential_zero_eq_zero {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) :
    (harmonicWaveX 𝓕 k E₀ φ).vectorPotential 𝓕.c t x 0 = 0
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_vectorPotential_succ`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L171).

```lean
lemma harmonicWaveX_vectorPotential_succ {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (i : Fin d) :
    (harmonicWaveX 𝓕 k E₀ φ).vectorPotential 𝓕.c t x i.succ =
    - E₀ i * 1 / (𝓕.c * k) * Real.sin (k * (t.val * 𝓕.c - x 0) + φ i)
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_vectorPotential_succ'`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L179).

```lean
lemma harmonicWaveX_vectorPotential_succ' {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (i : ℕ)
    (hi : i.succ < d.succ) :
    (harmonicWaveX 𝓕 k E₀ φ).vectorPotential 𝓕.c t x ⟨i.succ, hi⟩ =
    - E₀ ⟨i, by grind⟩ * 1 / (𝓕.c * k) * Real.sin (k * (t.val * 𝓕.c - x 0) + φ ⟨i, by grind⟩)
```

### C.2. Space derivatives of the vector potential

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_vectorPotential_space_deriv_succ`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L196).

```lean
lemma harmonicWaveX_vectorPotential_space_deriv_succ {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (j : Fin d)
    (i : Fin d.succ) :
    Space.deriv j.succ (fun x => vectorPotential 𝓕.c (harmonicWaveX 𝓕 k E₀ φ) t x i) x
    = 0
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_vectorPotential_succ_space_deriv_zero`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L217).

```lean
lemma harmonicWaveX_vectorPotential_succ_space_deriv_zero {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (i : Fin d) :
    Space.deriv 0 (fun x => vectorPotential 𝓕.c (harmonicWaveX 𝓕 k E₀ φ) t x i.succ) x
    = E₀ i / 𝓕.c.val * Real.cos (𝓕.c.val * k * t.val - k * x 0 + φ i)
```

## D. The electric field

### D.1. Components of the electric field

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_electricField_zero`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L244).

```lean
lemma harmonicWaveX_electricField_zero {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) :
    (harmonicWaveX 𝓕 k E₀ φ).electricField 𝓕.c t x 0 = 0
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_electricField_succ`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L252).

```lean
lemma harmonicWaveX_electricField_succ {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (i : Fin d) :
    (harmonicWaveX 𝓕 k E₀ φ).electricField 𝓕.c t x i.succ =
    E₀ i * Real.cos (k * 𝓕.c * t.val - k * x 0 + φ i)
```

### D.2. Spatial derivatives of the electric field

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_electricField_space_deriv_same`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L274).

```lean
lemma harmonicWaveX_electricField_space_deriv_same {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (i : Fin d.succ) :
    Space.deriv i (fun x => electricField 𝓕.c (harmonicWaveX 𝓕 k E₀ φ) t x i) x
    = 0
```

### D.3. Time derivatives of the electric field

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_electricField_succ_time_deriv`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L300).

```lean
lemma harmonicWaveX_electricField_succ_time_deriv {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (i : Fin d) :
    Time.deriv (fun t => electricField 𝓕.c (harmonicWaveX 𝓕 k E₀ φ) t x i.succ) t
    = - k * 𝓕.c * E₀ i * Real.sin (k * 𝓕.c * t.val - k * x 0 + φ i)
```

### D.4. Divergence of the electric field

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_div_electricField_eq_zero`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L324).

```lean
lemma harmonicWaveX_div_electricField_eq_zero {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) :
    Space.div (fun x => electricField 𝓕.c (harmonicWaveX 𝓕 k E₀ φ) t x) x = 0
```

## E. The magnetic field matrix for a harmonic wave

### E.1. Components of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_magneticFieldMatrix_succ_succ`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L343).

```lean
lemma harmonicWaveX_magneticFieldMatrix_succ_succ {d} (𝓕 : FreeSpace) (k : ℝ)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ)
    (i j : Fin d) :
    (harmonicWaveX 𝓕 k E₀ φ).magneticFieldMatrix 𝓕.c t x (i.succ, j.succ) = 0
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_magneticFieldMatrix_zero_succ`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L350).

```lean
lemma harmonicWaveX_magneticFieldMatrix_zero_succ {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ)
    (i : Fin d) :
    (harmonicWaveX 𝓕 k E₀ φ).magneticFieldMatrix 𝓕.c t x (0, i.succ) =
    (- E₀ i / 𝓕.c.val) * cos (𝓕.c.val * k * t.val - k * x 0 + φ i)
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_magneticFieldMatrix_succ_zero`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L363).

```lean
lemma harmonicWaveX_magneticFieldMatrix_succ_zero {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ)
    (i : Fin d) :
    (harmonicWaveX 𝓕 k E₀ φ).magneticFieldMatrix 𝓕.c t x (i.succ, 0) =
    (E₀ i / 𝓕.c.val) * cos (𝓕.c.val * k * t.val - k * x 0 + φ i)
```

### E.2. Space derivatives of the magnetic field matrix

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_magneticFieldMatrix_space_deriv_succ`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L380).

```lean
lemma harmonicWaveX_magneticFieldMatrix_space_deriv_succ {d} (𝓕 : FreeSpace) (k : ℝ)
    (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ)
    (i j : Fin d.succ) (l : Fin d) :
    Space.deriv l.succ (fun x => magneticFieldMatrix 𝓕.c (harmonicWaveX 𝓕 k E₀ φ) t x (i, j)) x
    = 0
```

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_magneticFieldMatrix_zero_succ_space_deriv_zero`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L415).

```lean
lemma harmonicWaveX_magneticFieldMatrix_zero_succ_space_deriv_zero {d} (𝓕 : FreeSpace) (k : ℝ)
    (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ)
    (i : Fin d) :
    Space.deriv 0 (fun x => magneticFieldMatrix 𝓕.c (harmonicWaveX 𝓕 k E₀ φ) t x (0, i.succ)) x
    = -E₀ i * k / 𝓕.c.val * sin (𝓕.c.val * k * t.val - k * x 0 + φ i)
```

## F. Maxwell's equations for a harmonic wave

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_isExtrema`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L444).

```lean
lemma harmonicWaveX_isExtrema {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) :
    IsExtrema 𝓕 (harmonicWaveX 𝓕 k E₀ φ) 0
```

## G. The harmonic wave is a plane wave

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_isPlaneWave`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L486).

```lean
lemma harmonicWaveX_isPlaneWave {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) :
    IsPlaneWave 𝓕 (harmonicWaveX 𝓕 k E₀ φ) ⟨Space.basis 0, by simp⟩
```

## H. Polarization ellipse of the harmonic wave

**`Electromagnetism.ElectromagneticPotential.harmonicWaveX_polarization_ellipse`**, a lemma, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean#L549).

```lean
lemma harmonicWaveX_polarization_ellipse {d} (𝓕 : FreeSpace) (k : ℝ) (hk : k ≠ 0)
    (E₀ : Fin d → ℝ) (φ : Fin d → ℝ) (t : Time) (x : Space d.succ) (hi : ∀ i, E₀ i ≠ 0) :
    2 * d * ∑ i : Fin d, ((harmonicWaveX 𝓕 k E₀ φ).electricField 𝓕.c t x i.succ / E₀ i) ^ 2 -
    2 * ∑ i, ∑ j, ((harmonicWaveX 𝓕 k E₀ φ).electricField 𝓕.c t x i.succ / E₀ i) *
      ((harmonicWaveX 𝓕 k E₀ φ).electricField 𝓕.c t x j.succ / E₀ j) *
      Real.cos (φ j - φ i) =
    ∑ i, ∑ j, Real.sin (φ j - φ i) ^ 2
```

## Depends on

- [Electromagnetic wave equation](isplanewave.md)

## Sources

- [Physlib/Electromagnetism/Vacuum/HarmonicWave.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Vacuum/HarmonicWave.lean)
