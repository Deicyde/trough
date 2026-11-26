---
declaration: module
origin: cited
lean: complexLorentzTensor.bispinorMetricTensor, complexLorentzTensor.invariants_upL_upL_upR_upR_eq_span_bispinorMetric, complexLorentzTensor.bispinorPairingTensor, complexLorentzTensor.invariants_upL_pow_four_upR_pow_four_eq_span_range_bispinorPairing, Lorentz.bispinorMetric, Lorentz.pauliTransform_minkowskiMatrix
statement: formalized
proof: formalized
---

# The metric pairings of bispinor indices

The module `PhyslibAlpha.Relativity.Bispinors.MetricPairing`, [PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean): 6 declarations, 6 with a docstring.

> The invariant tensors with left-handed Weyl indices followed by as many right-handed ones are the
> products of Weyl metric pairings of each chirality.

## i. Overview

> By `complexLorentzTensor.invariants_append_eq_map₂_prodT` the invariant tensors with undotted
> indices followed by dotted ones are spanned by the products of an invariant tensor of the undotted
> indices and one of the dotted indices. With two left-handed and two right-handed indices the
> factors are the metrics `ε` and `ε̄`, so the invariant tensors are the line through `ε ⊗ ε̄` (A).
> With four of each they are the two products of metrics of each chirality, so the invariant tensors
> are the span of the four products `bispinorPairingTensor`, `ε ε ⊗ ε̄ ε̄` (B). The latter is what
> the classification of the invariants of four four-vector indices uses, through the Pauli matrices.
>
> On coefficient functions, the Pauli change of indices sends the Minkowski metric to `2 ε ⊗ ε̄`,
> the Fierz identity, matching the single invariant of two four-vector indices with that of two
> bispinor indices (C).

## ii. Key results

> - `complexLorentzTensor.invariants_upL_upL_upR_upR_eq_span_bispinorMetric` : the invariant tensors
>   with two left- and then two right-handed Weyl indices.
> - `complexLorentzTensor.invariants_upL_pow_four_upR_pow_four_eq_span_range_bispinorPairing` : the
>   invariant tensors with four left- and then four right-handed Weyl indices.
> - `Lorentz.pauliTransform_minkowskiMatrix` : the Pauli change sends the Minkowski metric to
>   `2 ε ⊗ ε̄`.

## iv. References

> * None.

## A. Two left- and two right-handed Weyl indices

**`complexLorentzTensor.bispinorMetricTensor`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean#L65).

> The tensor `ε ⊗ ε̄` with two left-handed and then two right-handed Weyl indices, the product of
> the metrics of the two chiralities.

```lean
noncomputable def bispinorMetricTensor : ℂT(Fin.append ![Color.upL, .upL] ![Color.upR, .upR])
```

**`complexLorentzTensor.invariants_upL_upL_upR_upR_eq_span_bispinorMetric`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean#L70).

> The invariant tensors with two left-handed and then two right-handed Weyl indices are the line
> through `ε ⊗ ε̄`.

```lean
lemma invariants_upL_upL_upR_upR_eq_span_bispinorMetric :
    (complexLorentzTensor.tensorRep (Fin.append ![Color.upL, .upL] ![Color.upR, .upR])).invariants =
      ℂ ∙ bispinorMetricTensor
```

## B. Four left- and four right-handed Weyl indices

**`complexLorentzTensor.bispinorPairingTensor`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean#L86).

> The four products `ε ε ⊗ ε̄ ε̄` of a pairing of four left-handed Weyl indices and one of four
> right-handed ones, as tensors with the left-handed indices first.

```lean
noncomputable def bispinorPairingTensor (ij : Fin 2 × Fin 2) :
    ℂT(Fin.append (fun _ : Fin 4 => Color.upL) (fun _ : Fin 4 => Color.upR))
```

**`complexLorentzTensor.invariants_upL_pow_four_upR_pow_four_eq_span_range_bispinorPairing`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean#L92).

> The invariant tensors with four left-handed and then four right-handed Weyl indices are the
> span of the four products of pairings `ε ε ⊗ ε̄ ε̄`.

```lean
lemma invariants_upL_pow_four_upR_pow_four_eq_span_range_bispinorPairing :
    (complexLorentzTensor.tensorRep
      (Fin.append (fun _ : Fin 4 => Color.upL) (fun _ : Fin 4 => Color.upR))).invariants =
      Submodule.span ℂ (Set.range bispinorPairingTensor)
```

## C. The Fierz identity

**`Lorentz.bispinorMetric`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean#L116).

> The product `ε_{α₀α₁} ε_{α̇₀α̇₁}` of the Weyl metrics of the two chiralities on two bispinor
> indices.

```lean
def bispinorMetric (α : Fin 2 → Fin 2 × Fin 2) : ℂ
```

**`Lorentz.pauliTransform_minkowskiMatrix`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean#L121).

> Through the Pauli matrices the Minkowski metric is twice `ε ⊗ ε̄`, the Fierz identity
> `η^{μν} (σ_μ)_{αα̇} (σ_ν)_{ββ̇} = 2 ε_{αβ} ε_{α̇β̇}`.

```lean
lemma pauliTransform_minkowskiMatrix :
    pauliTransform (fun d : Fin 2 → Fin 1 ⊕ Fin 3 => ((minkowskiMatrixZ (d 0) (d 1) : ℤ) : ℂ))
      = (2 : ℂ) • bispinorMetric
```

## Depends on

- [The action of `SL(2, ℂ)` on bispinor indices](bispinormatrix.md)
- [The metric pairings of four Weyl indices](../fermions/weyl-metricpairing.md)

## Proof depends on

- [Peeling the first slot off a sum over tuples](../../mathematics/part-02/formathlib/fin.md)
- [The complexified Lorentz group acting on Weyl tensors](complexifiedaction.md)
- [The metrics are the unique invariant tensors with two indices of one colour](../tensors/complextensor-metrics-basic.md)

## Sources

- [PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/MetricPairing.lean)
