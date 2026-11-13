---
declaration: module
origin: cited
lean: Lorentz.RankTwo.metric, Lorentz.RankTwo.metric_invariant, Lorentz.RankTwo.coeffEquiv_symm_minkowskiMatrixZ, Lorentz.RankTwo.ofComponents_metric, Lorentz.RankTwo.exists_halfTurnSign_mul_ne_one, Lorentz.RankTwo.eq_zero_of_ne, Lorentz.RankTwo.apply_inr_inr_eq, Lorentz.RankTwo.apply_inl_inl_add_apply_inr_inr
statement: formalized
proof: formalized
---

# Lorentz invariants among two four-vector indices

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.RankTwo`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean): 12 declarations, 12 with a docstring.

## i. Overview

> A rank-two tensor `T^{μν}` has a single Lorentz invariant up to scale, its contraction with the
> metric: nothing else ties two indices, the Levi-Civita symbol needing four. For an equivariant
> map `f : ℂT(fun _ : Fin 2 => .up) →ₗ[ℂ] B`, `IsLorentzCovariant 2`, every Lorentz invariant in the
> range of `f` is a multiple of `f metric`, the image of the metric `η` (A), and modulo a
> Lorentz-stable submodule `S` the invariants of `LinearMap.range f ⊔ S` reduce to the line through
> it (C). For a given `f` the image may be zero.
>
> The invariants of the range of `f` are the images of invariant tensors, so it is enough that an
> invariant coefficient tensor `c` (`Invariants.Basic`) is a multiple of the Minkowski metric, and
> three kinds of transformation pin `c` down (B). The half turn about each axis has a diagonal
> Lorentz matrix with entries `±1`, and for `μ ≠ ν` one of the three negates `c_{μν}`, so the
> off-diagonal coefficients vanish. The cyclic rotation `x → y → z → x` permutes the spatial
> directions, so `c_xx = c_yy = c_zz`. The boost along `z` scales the light-cone component of `c`
> along `D₀ - D_z` in both slots by `t⁴`, so that component vanishes, and with the off-diagonal
> coefficients gone it is `c_tt + c_zz`. So `c` is `c_tt` times the Minkowski metric.

## ii. Key results

> - `Lorentz.RankTwo.metric` : the metric `η` with the colours of `IsLorentzCovariant 2`.
> - `Lorentz.RankTwo.exists_smul_map_metric_of_invariant` : an invariant in the range of `f` is a
>   multiple of `f metric`.
> - `Lorentz.RankTwo.reducesInvariantsTo_span_metric` : the same modulo a stable submodule.

## iv. References

> * None.

## A. The metric

**`Lorentz.RankTwo.metric`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L70).

> The metric `η` on two contravariant indices, with its colours relabelled from
> `![.up, .up]` to `fun _ => .up`.

```lean
noncomputable def metric : ℂT(fun _ : Fin 2 => Color.up)
```

**`Lorentz.RankTwo.metric_invariant`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L75).

> The metric is Lorentz invariant.

```lean
lemma metric_invariant (g : SL(2,ℂ)) : g • metric = metric
```

**`Lorentz.RankTwo.coeffEquiv_symm_minkowskiMatrixZ`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L79).

> The coefficient tensor of the metric is the Minkowski metric.

```lean
lemma coeffEquiv_symm_minkowskiMatrixZ :
    (coeffEquiv 2).symm (fun d => ((minkowskiMatrixZ (d 0) (d 1) : ℤ) : ℂ)) = metric
```

**`Lorentz.RankTwo.ofComponents_metric`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L91).

> `ofComponents T` sends the metric to the contraction `η_{μν} T^{μν}`.

```lean
lemma ofComponents_metric (T : (Fin 2 → Fin 1 ⊕ Fin 3) → B) :
    ofComponents T metric
      = ∑ d : Fin 2 → Fin 1 ⊕ Fin 3, ((minkowskiMatrixZ (d 0) (d 1) : ℤ) : ℂ) • T d
```

## B. The classification of the invariant coefficient tensors

> The half turns kill the off-diagonal coefficients, the cyclic rotation equates the three
> spatial diagonal ones, and the boost along `z` relates the spatial diagonal to the time
> diagonal. Together these leave `c_tt` times the metric.

**`Lorentz.RankTwo.exists_halfTurnSign_mul_ne_one`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L108).

> Two distinct directions are told apart by the half turn about some axis: it keeps one and
> negates the other, a finite check.

```lean
lemma exists_halfTurnSign_mul_ne_one :
    ∀ μ ν : Fin 1 ⊕ Fin 3, μ ≠ ν → ∃ k, halfTurnSign k μ * halfTurnSign k ν ≠ 1
```

**`Lorentz.RankTwo.eq_zero_of_ne`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L114).

> An invariant coefficient tensor has no off-diagonal coefficients: for `μ ≠ ν` some half
> turn multiplies `c_{μν}` by `-1`.

```lean
lemma eq_zero_of_ne {c : (Fin 2 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c)
    {d : Fin 2 → Fin 1 ⊕ Fin 3} (hd : d 0 ≠ d 1) : c d = 0
```

**`Lorentz.RankTwo.apply_inr_inr_eq`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L121).

> The three spatial diagonal coefficients of an invariant coefficient tensor agree: the
> cyclic rotation carries `c_xx` to `c_yy` to `c_zz`.

```lean
lemma apply_inr_inr_eq {c : (Fin 2 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c)
    (j : Fin 3) : c ![Sum.inr j, Sum.inr j] = c ![Sum.inr 2, Sum.inr 2]
```

**`Lorentz.RankTwo.apply_inl_inl_add_apply_inr_inr`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L135).

> The time and spatial diagonal coefficients of an invariant coefficient tensor are opposite.
> The boost along `z` scales the light-cone component along `D₀ - D_z` in both slots by `t⁴`, so
> that component, `c_tt - c_tz - c_zt + c_zz`, vanishes, and the mixed terms are `0`.

```lean
lemma apply_inl_inl_add_apply_inr_inr {c : (Fin 2 → Fin 1 ⊕ Fin 3) → ℂ}
    (hc : IsInvariantCoeff c) : c ![Sum.inl 0, Sum.inl 0] + c ![Sum.inr 2, Sum.inr 2] = 0
```

**`Lorentz.RankTwo.eq_smul_minkowskiMatrixZ`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L145).

> An invariant coefficient tensor is `c_tt` times the Minkowski metric.

```lean
lemma eq_smul_minkowskiMatrixZ {c : (Fin 2 → Fin 1 ⊕ Fin 3) → ℂ} (hc : IsInvariantCoeff c)
    (d : Fin 2 → Fin 1 ⊕ Fin 3) :
    c d = c ![Sum.inl 0, Sum.inl 0] * ((minkowskiMatrixZ (d 0) (d 1) : ℤ) : ℂ)
```

## C. The invariants of an equivariant map

**`Lorentz.RankTwo.reducesInvariantsTo_span_metric`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L175).

> The invariants of the range of `f` reduce to the line through the image `f metric` of the
> metric: a Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, is
> a multiple of `f metric` plus an element of `S`.

```lean
lemma reducesInvariantsTo_span_metric (hf : IsLorentzCovariant 2 B repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
      (ℂ ∙ f metric)
```

**`Lorentz.RankTwo.exists_smul_map_metric_add_of_invariant`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L186).

> Every Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, is a
> multiple of the image `f metric` of the metric plus an element of `S`.

```lean
lemma exists_smul_map_metric_add_of_invariant (hf : IsLorentzCovariant 2 B repLorentz f)
    (S : Submodule ℂ B) (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ LinearMap.range f ⊔ S) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) :
    ∃ a : ℂ, ∃ y ∈ S, x = a • f metric + y
```

**`Lorentz.RankTwo.exists_smul_map_metric_of_invariant`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean#L197).

> Every Lorentz invariant in the range of `f` is a multiple of the image `f metric` of the
> metric.

```lean
lemma exists_smul_map_metric_of_invariant (hf : IsLorentzCovariant 2 B repLorentz f) {x : B}
    (hx : x ∈ LinearMap.range f) (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) :
    ∃ a : ℂ, x = a • f metric
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Metrics.Basic](../../../physlib/relativity/tensors/part-01/complextensor-metrics-basic.md)
- [Equivariant maps out of tensors with four-vector indices](invariants-lorentzcovariance.md)
- [The Minkowski matrix over the integers](../minkowskimatrix.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/RankTwo.lean)
