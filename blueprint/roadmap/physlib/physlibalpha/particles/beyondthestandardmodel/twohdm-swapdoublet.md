---
declaration: module
origin: cited
lean: TwoHiggsDoublet.EffectivePotential.swapDoublet, TwoHiggsDoublet.EffectivePotential.swapDoublet_Φ1, TwoHiggsDoublet.EffectivePotential.swapDoublet_Φ2, TwoHiggsDoublet.EffectivePotential.swapDoublet_swapDoublet, TwoHiggsDoublet.EffectivePotential.swapDoublet_smul, TwoHiggsDoublet.EffectivePotential.gramVector_swapDoublet_inl, TwoHiggsDoublet.EffectivePotential.gramVector_swapDoublet_inr0, TwoHiggsDoublet.EffectivePotential.gramVector_swapDoublet_inr1
statement: formalized
proof: formalized
---

# Swapping the two Higgs doublets

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.TwoHDM.SwapDoublet`, [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean): 11 declarations, 2 with a docstring.

> The doublet swap Φ1 ↔ Φ2 commutes with gauge action, preserving invariance and mass dimension.

## i. Overview

> Exchanging the two doublets `Φ1 ↔ Φ2` is an `ℝ`-linear map `swapDoublet` that commutes with the
> gauge action. It therefore preserves gauge invariance and the maximum mass dimension, while turning
> the alignment of `Φ1` into the alignment of `Φ2`. This is precisely the symmetry used to clear the
> `‖Φ2‖²` factor when writing the potential through the gauge invariants, mirroring the `‖Φ1‖²`
> clearing.

## ii. Key results

> * `swapDoublet` — the doublet exchange, as an `ℝ`-linear map.
> * `swapDoublet_smul` — it commutes with the gauge action.
> * `gramVector_swapDoublet_*` — its effect on the Gram vector (a sign flip on the imaginary and
>   difference components).
> * `IsInvariant.comp_swapDoublet`, `HasMaxMassDimLE.comp_swapDoublet` — it preserves gauge invariance
>   and bounded mass dimension.

## iv. References

> * None.

## A. The doublet-swap map and its components

**`TwoHiggsDoublet.EffectivePotential.swapDoublet`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L61).

> Swapping the two doublets, as an `ℝ`-linear map. It commutes with the gauge action, so it sends
> gauge-invariant polynomial potentials to gauge-invariant polynomial potentials, but turns the
> alignment of `Φ1` into the alignment of `Φ2`.

```lean
def swapDoublet : TwoHiggsDoublet →ₗ[ℝ] TwoHiggsDoublet
```

**`TwoHiggsDoublet.EffectivePotential.swapDoublet_Φ1`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L66).

```lean
lemma swapDoublet_Φ1 (φ : TwoHiggsDoublet) : (swapDoublet φ).Φ1 = φ.Φ2
```

**`TwoHiggsDoublet.EffectivePotential.swapDoublet_Φ2`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L67).

```lean
lemma swapDoublet_Φ2 (φ : TwoHiggsDoublet) : (swapDoublet φ).Φ2 = φ.Φ1
```

**`TwoHiggsDoublet.EffectivePotential.swapDoublet_swapDoublet`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L69).

```lean
lemma swapDoublet_swapDoublet (φ : TwoHiggsDoublet) : swapDoublet (swapDoublet φ) = φ
```

## B. Commutation with the gauge action

**`TwoHiggsDoublet.EffectivePotential.swapDoublet_smul`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L76).

```lean
lemma swapDoublet_smul (g : StandardModel.GaugeGroupI) (φ : TwoHiggsDoublet) :
    swapDoublet (g • φ) = g • swapDoublet φ
```

## C. The action on the Gram vector

**`TwoHiggsDoublet.EffectivePotential.gramVector_swapDoublet_inl`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L86).

> Swapping the doublets sends the gram vector through the sign flip of the imaginary and
> difference components.

```lean
lemma gramVector_swapDoublet_inl (φ : TwoHiggsDoublet) :
    (swapDoublet φ).gramVector (Sum.inl 0) = φ.gramVector (Sum.inl 0)
```

**`TwoHiggsDoublet.EffectivePotential.gramVector_swapDoublet_inr0`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L90).

```lean
lemma gramVector_swapDoublet_inr0 (φ : TwoHiggsDoublet) :
    (swapDoublet φ).gramVector (Sum.inr 0) = φ.gramVector (Sum.inr 0)
```

**`TwoHiggsDoublet.EffectivePotential.gramVector_swapDoublet_inr1`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L95).

```lean
lemma gramVector_swapDoublet_inr1 (φ : TwoHiggsDoublet) :
    (swapDoublet φ).gramVector (Sum.inr 1) = -φ.gramVector (Sum.inr 1)
```

**`TwoHiggsDoublet.EffectivePotential.gramVector_swapDoublet_inr2`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L100).

```lean
lemma gramVector_swapDoublet_inr2 (φ : TwoHiggsDoublet) :
    (swapDoublet φ).gramVector (Sum.inr 2) = -φ.gramVector (Sum.inr 2)
```

## D. Effect on gauge invariance and mass dimension

**`TwoHiggsDoublet.EffectivePotential.HasMaxMassDimLE.comp_swapDoublet`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L108).

```lean
lemma HasMaxMassDimLE.comp_swapDoublet {V : EffectivePotential} {n : ℕ}
    (h : HasMaxMassDimLE V n) : HasMaxMassDimLE (fun φ => V (swapDoublet φ)) n
```

**`TwoHiggsDoublet.EffectivePotential.IsInvariant.comp_swapDoublet`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean#L117).

```lean
lemma IsInvariant.comp_swapDoublet {V : EffectivePotential} (hI : IsInvariant V) :
    IsInvariant (fun φ => V (swapDoublet φ))
```

## Depends on

- [The gram matrix for the two Higgs doublet model](../../../physlib/particles/beyondthestandardmodel/twohdm/grammatrix.md)
- [The effective potential of the two Higgs doublet model](twohdm-effectivepotential.md)

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/SwapDoublet.lean)
