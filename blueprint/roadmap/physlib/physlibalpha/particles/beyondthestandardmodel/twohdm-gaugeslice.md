---
declaration: module
origin: cited
lean: TwoHiggsDoublet.sliceHiggs, TwoHiggsDoublet.sliceHiggs_Φ1, TwoHiggsDoublet.sliceHiggs_Φ2, TwoHiggsDoublet.real_smul_fst, TwoHiggsDoublet.real_smul_snd, TwoHiggsDoublet.sliceR, TwoHiggsDoublet.sliceR_apply, TwoHiggsDoublet.repHiggs_eq_sliceHiggs
statement: formalized
proof: formalized
---

# The gauge slice and the hypercharges of the doublet components

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.TwoHDM.GaugeSlice`, [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean): 14 declarations, 9 with a docstring.

> The gauge slice of 2HDM configurations and the gauge-torus phases acting on it.

## i. Overview

> After using `SU(2)` to align the first doublet with the second axis, a configuration lies on the
> *gauge slice* `sliceHiggs z w₀ w₁ = ⟨(0, z), (w₁, w₀)⟩`. The gauge torus acts on the
> three surviving components `z = Φ1₁`, `w₀ = Φ2₁`, `w₁ = Φ2₀` by their hypercharges:
>
> * the Cartan phase `gaugeCartan ā` multiplies the components `z, w₀` along `Φ1` by `a` (and
>   conjugates the would-be charged component of `Φ1`, which vanishes here), giving
>   `(z, w₀, w₁) ↦ (a z, a w₀, ā w₁)`;
> * the residual electromagnetic `U(1)` (`electromagnetismU1 c`) multiplies the charged component
>   `w₁` by `c⁶`, giving `(z, w₀, w₁) ↦ (z, w₀, c⁶ w₁)`.
>
> These two phase rotations are the source of the charge balancing of the effective potential.

## ii. Key results

> - `TwoHiggsDoublet.sliceHiggs` : the gauge slice configuration `⟨(0, z), (w₁, w₀)⟩`.
> - `TwoHiggsDoublet.sliceR` : the slice as a real-linear map from six real field parameters.
> - `TwoHiggsDoublet.gaugeCartan_smul_sliceHiggs` : the hypercharge action of the Cartan phase.
> - `TwoHiggsDoublet.electromagnetismU1_smul_sliceHiggs` : the hypercharge action of the residual
>   electromagnetic `U(1)`.
> - `TwoHiggsDoublet.gaugeCartan_smul_sliceR` : the Cartan phase rotates the real parameters.
> - `TwoHiggsDoublet.electromagnetismU1_smul_sliceR` : the residual `U(1)` rotates only the
>   perpendicular parameter pair.

## iv. References

> * None.

## A. The slice configuration

**`TwoHiggsDoublet.sliceHiggs`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L71).

> The gauge slice configuration `⟨(0, z), (w₁, w₀)⟩`. It specialises to `repHiggs`
> when the components take their real "canonical frame" values.

```lean
def sliceHiggs (z w0 w1 : ℂ) : TwoHiggsDoublet
```

**`TwoHiggsDoublet.sliceHiggs_Φ1`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L75).

```lean
lemma sliceHiggs_Φ1 (z w0 w1 : ℂ) : (sliceHiggs z w0 w1).Φ1 = !₂[0, z]
```

**`TwoHiggsDoublet.sliceHiggs_Φ2`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L76).

```lean
lemma sliceHiggs_Φ2 (z w0 w1 : ℂ) : (sliceHiggs z w0 w1).Φ2 = !₂[w1, w0]
```

**`TwoHiggsDoublet.real_smul_fst`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L78).

```lean
lemma real_smul_fst (c : ℝ) (H : TwoHiggsDoublet) : (c • H).Φ1 = c • H.Φ1
```

**`TwoHiggsDoublet.real_smul_snd`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L79).

```lean
lemma real_smul_snd (c : ℝ) (H : TwoHiggsDoublet) : (c • H).Φ2 = c • H.Φ2
```

**`TwoHiggsDoublet.sliceR`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L83).

> The slice as a real-linear map from the six real field parameters
> `(Re Φ1₁, Im Φ1₁, Re Φ2₁, Im Φ2₁, Re Φ2₀, Im Φ2₀)`.

```lean
def sliceR : (Fin 6 → ℝ) →ₗ[ℝ] TwoHiggsDoublet
```

**`TwoHiggsDoublet.sliceR_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L97).

```lean
lemma sliceR_apply (a : Fin 6 → ℝ) :
    sliceR a = sliceHiggs (↑(a 0) + Complex.I * ↑(a 1)) (↑(a 2) + Complex.I * ↑(a 3))
      (↑(a 4) + Complex.I * ↑(a 5))
```

**`TwoHiggsDoublet.repHiggs_eq_sliceHiggs`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L102).

> The representative family is the real slice.

```lean
lemma repHiggs_eq_sliceHiggs (X : Fin 4 → ℝ) :
    repHiggs X = sliceHiggs (X 0) ((X 1 : ℂ) + Complex.I * (X 2 : ℂ)) (X 3)
```

## B. Hypercharge action on the slice

**`TwoHiggsDoublet.gaugeCartan_smul_sliceHiggs`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L113).

> Hypercharge action of the Cartan phase `diag(ā, a)` on the slice: it multiplies the components
> along `Φ1` by `a` and the charged component by `ā`.

```lean
lemma gaugeCartan_smul_sliceHiggs (a : unitary ℂ) (z w0 w1 : ℂ) :
    GaugeGroupI.gaugeCartan (star a) • sliceHiggs z w0 w1
      = sliceHiggs ((a : ℂ) * z) ((a : ℂ) * w0) ((star a : ℂ) * w1)
```

**`TwoHiggsDoublet.electromagnetismU1_smul_sliceHiggs`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L126).

> Hypercharge action of the residual electromagnetic `U(1)` on the slice: it multiplies the
> charged component by `c⁶` and leaves the components along `Φ1` fixed.

```lean
lemma electromagnetismU1_smul_sliceHiggs (c : unitary ℂ) (z w0 w1 : ℂ) :
    GaugeGroupI.electromagnetismU1 c • sliceHiggs z w0 w1
      = sliceHiggs z w0 ((c : ℂ) ^ 6 * w1)
```

## C. Gauge action on the real parameters

**`TwoHiggsDoublet.cartanRotParam`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L146).

> The Cartan hypercharge phase `u`, transported to a rotation of the six real field parameters:
> it phases the first-component pairs by `u` and the perpendicular pair by `ū`.

```lean
def cartanRotParam (u : unitary ℂ) (a : Fin 6 → ℝ) : Fin 6 → ℝ
```

**`TwoHiggsDoublet.gaugeCartan_smul_sliceR`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L152).

> Acting by the Cartan phase on a slice configuration is the same as rotating its parameters.

```lean
lemma gaugeCartan_smul_sliceR (u : unitary ℂ) (a : Fin 6 → ℝ) :
    GaugeGroupI.gaugeCartan (star u) • sliceR a = sliceR (cartanRotParam u a)
```

**`TwoHiggsDoublet.resRotParam`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L162).

> The residual `U(1)` phase `c`, transported to a rotation of the perpendicular parameter pair.

```lean
def resRotParam (c : unitary ℂ) (a : Fin 6 → ℝ) : Fin 6 → ℝ
```

**`TwoHiggsDoublet.electromagnetismU1_smul_sliceR`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean#L167).

> Acting by the residual `U(1)` on a slice configuration rotates only the perpendicular pair.

```lean
lemma electromagnetismU1_smul_sliceR (c : unitary ℂ) (a : Fin 6 → ℝ) :
    GaugeGroupI.electromagnetismU1 c • sliceR a = sliceR (resRotParam c a)
```

## Depends on

- [The gauge torus acting on Higgs vectors](twohdm-gaugetorus.md)
- [The Module structure on the two Higgs doublet model](twohdm-module.md)
- [A polynomial family of orbit representatives for the two Higgs doublet model](twohdm-orbitrepresentative.md)

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeSlice.lean)
