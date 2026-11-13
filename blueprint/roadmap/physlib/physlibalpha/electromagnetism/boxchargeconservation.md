---
declaration: module
origin: cited
lean: Electromagnetism.ThreeDimension.continuityEquation, Space.div_differentiable_time, Space.time_deriv_div_commute, Space.curl_contDiff, Space.div_mk_eq_sum_fderiv, Space.integral_div_box, Electromagnetism.ThreeDimension.continuity_of_gauss_ampere, Electromagnetism.ThreeDimension.magneticField_contDiff_space
statement: formalized
proof: formalized
---

# Charge conservation on a box from Maxwell's equations

The module `PhyslibAlpha.Electromagnetism.BoxChargeConservation`, [PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean): 12 declarations, 8 with a docstring, 1 listed as significant.

## i. Overview

> Let `V` be an electromagnetic potential and `J₄` a Lorentz current density such that `V` is an
> extremum of the free-space action with source `J₄`, i.e. Maxwell's equations hold. Taking the
> divergence of Ampère's law, the divergence of the curl of the magnetic field vanishes, and the
> divergence of the displacement current is, by Gauss's law, the time derivative of the charge
> density. This gives the continuity equation `∂ₜ ρ + ∇ ⬝ J = 0`.
>
> Integrating the continuity equation over a coordinate box `[a, b]` and applying the divergence
> theorem, the net current leaving the box equals minus the rate of change of the charge it
> contains. In particular, if no charge accumulates inside the box, the currents leaving through
> its six faces sum to zero.
>
> This is motivated by Kirchhoff's current law, but is not that law: Kirchhoff's current law is a
> statement about the branch currents meeting at the nodes of a lumped-element circuit, whereas
> the results here are the integral form of charge conservation on a single box.

## ii. Key results

> - `Space.integral_div_box` : the divergence theorem on a coordinate box in `Space`.
> - `Electromagnetism.ThreeDimension.continuityEquation` : the continuity equation.
> - `Electromagnetism.LorentzCurrentDensity.boxFaceCurrent`,
>   `Electromagnetism.LorentzCurrentDensity.boxOutwardCurrent` : the current through a face of a
>   coordinate box, and the net current leaving the box.
> - `Electromagnetism.ThreeDimension.boxOutwardCurrent_eq` : the integral form of charge
>   conservation.
> - `Electromagnetism.ThreeDimension.boxOutwardCurrent_eq_zero_of_steady` : the net current
>   leaving a box in which no charge accumulates is zero.

## iv. References

> * None.

## A. Vector calculus on `Space`

### A.1. Time derivatives and the divergence

**`Space.div_differentiable_time`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L78).

```lean
lemma div_differentiable_time {d} (f : Time → Space d → EuclideanSpace ℝ (Fin d))
    (hf : ContDiff ℝ 2 ↿f) (x : Space d) :
    Differentiable ℝ (fun t => (∇ ⬝ f t) x)
```

**`Space.time_deriv_div_commute`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L87).

> The divergence and the time derivative commute.

```lean
lemma time_deriv_div_commute {d} (f : Time → Space d → EuclideanSpace ℝ (Fin d))
    (hf : ContDiff ℝ 2 ↿f) (t : Time) (x : Space d) :
    ∂ₜ (fun t => (∇ ⬝ f t) x) t = (∇ ⬝ fun x => ∂ₜ (fun t => f t x) t) x
```

### A.2. Smoothness of the curl

**`Space.curl_contDiff`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L109).

```lean
lemma curl_contDiff {n : WithTop ℕ∞} (f : Space → EuclideanSpace ℝ (Fin 3))
    (hf : ContDiff ℝ (n + 1) f) : ContDiff ℝ n (∇ ⨯ f)
```

### A.3. The divergence theorem on a coordinate box

> The box `[a, b]` is given in coordinates, `a b : Fin (n + 1) → ℝ`. Its faces normal to the
> `i`-th axis are parametrized, as in Mathlib's divergence theorem, by the remaining coordinates
> `y ∈ [a ∘ i.succAbove, b ∘ i.succAbove]` through `i.insertNth c y` with `c = a i` or `c = b i`.
>
> The divergence theorem below integrates over the box in coordinates, `x ∈ [a, b]`, rather than
> over the image of the box in `Space`.

**`Space.div_mk_eq_sum_fderiv`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L132).

```lean
lemma div_mk_eq_sum_fderiv {n : ℕ} (f : Space n → EuclideanSpace ℝ (Fin n))
    (hf : Differentiable ℝ f) (x : Fin n → ℝ) :
    (∇ ⬝ f) ⟨x⟩ = ∑ i, fderiv ℝ (fun y : Fin n → ℝ => f ⟨y⟩ i) x (Pi.single i 1)
```

**`Space.integral_div_box`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L145).

> The divergence theorem on a coordinate box in `Space`.

```lean
lemma integral_div_box {n : ℕ} (f : Space (n + 1) → EuclideanSpace ℝ (Fin (n + 1)))
    (hf : ContDiff ℝ 1 f) (a b : Fin (n + 1) → ℝ) (hle : a ≤ b) :
    ∫ x in Icc a b, (∇ ⬝ f) ⟨x⟩ =
      ∑ i, ((∫ y in Icc (a ∘ i.succAbove) (b ∘ i.succAbove), f ⟨i.insertNth (b i) y⟩ i) -
        ∫ y in Icc (a ∘ i.succAbove) (b ∘ i.succAbove), f ⟨i.insertNth (a i) y⟩ i)
```

## B. The continuity equation

### B.1. The continuity equation from Gauss's and Ampère's laws

**`Electromagnetism.ThreeDimension.continuity_of_gauss_ampere`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L178).

> Fields `E`, `B`, `ρ` and `J` obeying Gauss's law for the electric field and Ampère's law
> obey the continuity equation.

```lean
lemma continuity_of_gauss_ampere (𝓕 : FreeSpace)
    {E B J : Time → Space → EuclideanSpace ℝ (Fin 3)} {ρ : Time → Space → ℝ}
    (hE : ContDiff ℝ 2 ↿E) (hB : ∀ t, ContDiff ℝ 2 (B t))
    (hGauss : ∀ t x, (∇ ⬝ E t) x = ρ t x / 𝓕.ε₀)
    (hAmpere : ∀ t x, (∇ ⨯ B t) x = 𝓕.μ₀ • J t x + 𝓕.μ₀ • 𝓕.ε₀ • ∂ₜ (fun t => E t x) t)
    (t : Time) (x : Space) :
    ∂ₜ (fun t => ρ t x) t + (∇ ⬝ J t) x = 0
```

### B.2. The continuity equation for an electromagnetic potential

**`Electromagnetism.ThreeDimension.magneticField_contDiff_space`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L211).

```lean
lemma magneticField_contDiff_space (hV : ContDiff ℝ ∞ V) (t : Time) :
    ContDiff ℝ 2 (V.magneticField 𝓕.c t)
```

**`Electromagnetism.ThreeDimension.continuityEquation`**, a theorem, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L218). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The continuity equation: Maxwell's equations imply local conservation of charge.

```lean
theorem continuityEquation (t : Time) (x : Space)
    (h : IsExtrema 𝓕 V J₄) (hV : ContDiff ℝ ∞ V) (hJ : ContDiff ℝ ∞ J₄) :
    ∂ₜ (fun t => J₄.chargeDensity 𝓕.c t x) t + (∇ ⬝ J₄.currentDensity 𝓕.c t) x = 0
```

## C. Charge conservation on a box

### C.1. Currents through a box

**`Electromagnetism.LorentzCurrentDensity.boxFaceCurrent`**, a def, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L235).

> The electric current at time `t` through the face `x i = s` of the coordinate box `[a, b]`,
> counted positively in the direction of increasing `x i`.

```lean
noncomputable def _root_.Electromagnetism.LorentzCurrentDensity.boxFaceCurrent
    (c : SpeedOfLight) (J : LorentzCurrentDensity 3) (t : Time) (a b : Fin 3 → ℝ) (i : Fin 3)
    (s : ℝ) : ℝ
```

**`Electromagnetism.LorentzCurrentDensity.boxOutwardCurrent`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L242).

> The net electric current at time `t` leaving the coordinate box `[a, b]` through its six
> faces.

```lean
noncomputable def _root_.Electromagnetism.LorentzCurrentDensity.boxOutwardCurrent
    (c : SpeedOfLight) (J : LorentzCurrentDensity 3) (t : Time) (a b : Fin 3 → ℝ) : ℝ
```

### C.2. The integral form of charge conservation

**`Electromagnetism.ThreeDimension.boxOutwardCurrent_eq`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L254).

> The net current leaving the coordinate box `[a, b]` equals minus the rate of change of the
> charge inside it.

```lean
lemma boxOutwardCurrent_eq (t : Time) (a b : Fin 3 → ℝ) (hle : a ≤ b)
    (h : IsExtrema 𝓕 V J₄) (hV : ContDiff ℝ ∞ V) (hJ : ContDiff ℝ ∞ J₄) :
    J₄.boxOutwardCurrent 𝓕.c t a b =
      - ∫ x in Icc a b, ∂ₜ (fun t => J₄.chargeDensity 𝓕.c t ⟨x⟩) t
```

### C.3. Steady charge in a box

**`Electromagnetism.ThreeDimension.boxOutwardCurrent_eq_zero_of_steady`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean#L277).

> If no charge accumulates inside the coordinate box `[a, b]`, the net current leaving through
> its six faces is zero. This is motivated by Kirchhoff's current law, with the box enclosing a
> node of a circuit.

```lean
lemma boxOutwardCurrent_eq_zero_of_steady (t : Time) (a b : Fin 3 → ℝ) (hle : a ≤ b)
    (h : IsExtrema 𝓕 V J₄) (hV : ContDiff ℝ ∞ V) (hJ : ContDiff ℝ ∞ J₄)
    (hsteady : ∀ x ∈ Icc a b, ∂ₜ (fun t => J₄.chargeDensity 𝓕.c t ⟨x⟩) t = 0) :
    J₄.boxOutwardCurrent 𝓕.c t a b = 0
```

## Depends on

- [Extrema of the Lagrangian density](../../physlib/electromagnetism/dynamics/isextrema.md)

## Proof depends on

- [A. Maxwell's equations in three dimensions](../../physlib/electromagnetism/threedimension/maxwellequations.md)

## Sources

- [PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/BoxChargeConservation.lean)
