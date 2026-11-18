---
declaration: module
origin: cited
lean: StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightOne, StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightTwo, StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightThree, StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightFour, StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightFive, StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightSix, StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightSeven, StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightEight
statement: formalized
proof: formalized
---

# The gauge weight decomposition of the gauge mass-weight submodules

The module `PhyslibAlpha.Particles.StandardModel.IsGaugeSector.MassWeight.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean): 25 declarations, 25 with a docstring.

## i. Overview

> Each mass-weight submodule of the gauge sector up to weight eight has an explicit
> description in terms of the derivative submodules, and the derivative submodules carry
> a gauge weight decomposition.  Transporting the latter along the former decomposes
> every mass-weight submodule up to weight eight: the odd weights and weights two are
> trivial, weight four is the underived field strength, weight six the once-derived one,
> and weight eight the twice-derived one together with the products of two underived
> ones.

## ii. Key results

> - `massWeightSubmoduleGaugeWeightOne` : weight one is trivial
> - `massWeightSubmoduleGaugeWeightTwo` : weight two is trivial
> - `massWeightSubmoduleGaugeWeightThree` : weight three is trivial
> - `massWeightSubmoduleGaugeWeightFour` : weight four is the underived field strength

## iv. References

> * None.

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightOne`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L64).

> Weight one is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightOne :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 1)
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightTwo`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L71).

> Weight two is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightTwo :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 2)
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightThree`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L78).

> Weight three is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightThree :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 3)
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightFour`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L85).

> Weight four is the underived field strength.

```lean
noncomputable def massWeightSubmoduleGaugeWeightFour :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 4)
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightFive`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L92).

> Weight five is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightFive :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 5)
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightSix`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L99).

> Weight six is the once-derived field strength.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSix :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 6)
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightSeven`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L106).

> Weight seven is trivial.

```lean
noncomputable def massWeightSubmoduleGaugeWeightSeven :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 7)
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightEight`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L114).

> Weight eight is the twice-derived field strength together with the products of two
> underived ones.

```lean
noncomputable def massWeightSubmoduleGaugeWeightEight :
    GaugeWeightDecomposition repGauge (h.massWeightSubmodule 8)
```

## A. The weight-zero pieces

**`StandardModel.IsGaugeSector.rangeGaugeWeight_piece_zero`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L131).

> The weight-zero piece of one symbol map's decomposition: the Cartan and `u(1)`
> directions, the only ones the torus fixes.

```lean
lemma rangeGaugeWeight_piece_zero {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (μ ν : Fin 1 ⊕ Fin 3) :
    (h.rangeGaugeWeight l μ ν).piece 0
      = ⨆ c : Fin 4, ℂ ∙ F l μ ν (stdBasis.coord (cartanIdx c))
```

**`StandardModel.IsGaugeSector.derivSubmoduleGaugeWeight_piece_zero`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L148).

> **The weight-zero piece of the gauge derivative submodules**: the spans of the
> field-strength symbols evaluated on the four weight-zero directions of the adjoint —
> the two `su(3)` Cartan generators, the `su(2)` Cartan generator and the `u(1)`
> generator.  The four are distinct, so the join carries no duplicates.

```lean
lemma derivSubmoduleGaugeWeight_piece_zero (n : ℕ) :
    (h.derivSubmoduleGaugeWeight n).piece 0
      = ⨆ (l : Fin n → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3)
          (c : Fin 4),
        ℂ ∙ F l μ ν (stdBasis.coord (cartanIdx c))
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightOne_piece_zero`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L159).

> The weight-zero piece at mass weight 1: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightOne_piece_zero :
    (h.massWeightSubmoduleGaugeWeightOne).piece 0 = ⊥
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightTwo_piece_zero`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L163).

> The weight-zero piece at mass weight 2: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightTwo_piece_zero :
    (h.massWeightSubmoduleGaugeWeightTwo).piece 0 = ⊥
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightThree_piece_zero`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L167).

> The weight-zero piece at mass weight 3: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightThree_piece_zero :
    (h.massWeightSubmoduleGaugeWeightThree).piece 0 = ⊥
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightFive_piece_zero`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L171).

> The weight-zero piece at mass weight 5: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightFive_piece_zero :
    (h.massWeightSubmoduleGaugeWeightFive).piece 0 = ⊥
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightSeven_piece_zero`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L175).

> The weight-zero piece at mass weight 7: the submodule itself is trivial.

```lean
lemma massWeightSubmoduleGaugeWeightSeven_piece_zero :
    (h.massWeightSubmoduleGaugeWeightSeven).piece 0 = ⊥
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightFour_piece_zero`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L180).

> The weight-zero piece at mass weight four: the undifferentiated field strength on
> the four fixed directions of the adjoint.

```lean
lemma massWeightSubmoduleGaugeWeightFour_piece_zero :
    (h.massWeightSubmoduleGaugeWeightFour).piece 0
      = ⨆ (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3) (c : Fin 4),
        ℂ ∙ F ![] μ ν (stdBasis.coord (cartanIdx c))
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightSix_piece_zero`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L192).

> The weight-zero piece at mass weight six: the once-differentiated field strength on
> the four fixed directions of the adjoint.

```lean
lemma massWeightSubmoduleGaugeWeightSix_piece_zero :
    (h.massWeightSubmoduleGaugeWeightSix).piece 0
      = ⨆ (l : Fin 1 → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3)
          (c : Fin 4),
        ℂ ∙ F l μ ν (stdBasis.coord (cartanIdx c))
```

**`StandardModel.IsGaugeSector.piece_mul_comm`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L201).

> Any two weight pieces of a gauge derivative submodule commute: the gauge sector is
> bosonic, and every piece sits inside the derivative submodule.

```lean
lemma piece_mul_comm (n : ℕ) (w w' : GaugeWeight) :
    (h.derivSubmoduleGaugeWeight n).piece w * (h.derivSubmoduleGaugeWeight n).piece w'
      = (h.derivSubmoduleGaugeWeight n).piece w' * (h.derivSubmoduleGaugeWeight n).piece w
```

## B. The gauge-component pieces

> At mass weight eight the weight-zero content splits by gauge group factor.  A product
> of two underived symbols has weight zero exactly when the two weights are opposite, so
> the contributions are indexed by the root directions: the roots `0`, `1` and `2` are the
> `su(3)` roots and give the gluon contribution, the root `3` is the `su(2)` root and
> gives the isospin contribution, and the weight-zero directions pair with themselves to
> give the neutral contribution of the two `su(3)` Cartan directions, the `su(2)` Cartan
> direction and hypercharge.

**`StandardModel.IsGaugeSector.rootRaisingSpan`**, a def, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L228).

> The span of the underived raising vectors along the `r`-th root direction.

```lean
noncomputable def rootRaisingSpan (r : Fin 4) : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.rootLoweringSpan`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L233).

> The span of the underived lowering vectors along the `r`-th root direction.

```lean
noncomputable def rootLoweringSpan (r : Fin 4) : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.cartanSpan`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L239).

> The span of the underived weight-zero vectors: the two `su(3)` Cartan directions,
> the `su(2)` Cartan direction and the `u(1)` direction.

```lean
noncomputable def cartanSpan : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.gluonRootPart`**, a def, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L245).

> The gluon contribution to the weight-zero piece: the three products pairing an
> `su(3)` raising vector against the matching lowering vector.

```lean
noncomputable def gluonRootPart : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.isospinRootPart`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L252).

> The isospin contribution to the weight-zero piece: the single product pairing the
> `su(2)` raising vector against the matching lowering vector.

```lean
noncomputable def isospinRootPart : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.neutralCartanPart`**, a def, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L258).

> The neutral contribution to the weight-zero piece: the products of the weight-zero
> directions with themselves, namely the two `su(3)` Cartan directions, the `su(2)`
> Cartan direction and hypercharge.

```lean
noncomputable def neutralCartanPart : Submodule ℂ B
```

**`StandardModel.IsGaugeSector.massWeightSubmoduleGaugeWeightEight_piece_zero`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean#L263).

> The weight-zero piece at mass weight eight, split into the contributions of the
> three gauge group factors: the twice-differentiated field strength on the four fixed
> directions of the adjoint, joined with the gluon, isospin and neutral parts.

```lean
lemma massWeightSubmoduleGaugeWeightEight_piece_zero :
    (h.massWeightSubmoduleGaugeWeightEight).piece 0
      = (⨆ (l : Fin 2 → Fin 1 ⊕ Fin 3) (μ : Fin 1 ⊕ Fin 3) (ν : Fin 1 ⊕ Fin 3)
          (c : Fin 4),
          ℂ ∙ F l μ ν (stdBasis.coord (cartanIdx c)))
        ⊔ (h.gluonRootPart ⊔ (h.isospinRootPart ⊔ h.neutralCartanPart))
```

## Depends on

- [The gauge weight decomposition of the gauge sector](isgaugesector-deriv-gaugeweight.md)
- [The mass-weight grading of the gauge sector](isgaugesector-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsGaugeSector/MassWeight/GaugeWeight.lean)
