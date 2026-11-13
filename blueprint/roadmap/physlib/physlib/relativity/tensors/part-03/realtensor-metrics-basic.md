---
declaration: module
origin: cited
lean: realLorentzTensor.coMetric, realLorentzTensor.contrMetric, realLorentzTensor.coMetric_eq_fromConstPair, realLorentzTensor.contrMetric_eq_fromConstPair, realLorentzTensor.coMetric_eq_fromPairT, realLorentzTensor.contrMetric_eq_fromPairT, realLorentzTensor.actionT_coMetric, realLorentzTensor.actionT_contrMetric
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.RealTensor.Metrics.Basic

The module `Physlib.Relativity.Tensors.RealTensor.Metrics.Basic`, [Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean): 13 declarations, 7 with a docstring.

## Metrics as real Lorentz tensors

## Definitions.

**`realLorentzTensor.coMetric`**, an abbrev, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L33).

> The metric `ηᵢᵢ` as a real Lorentz tensor.

```lean
abbrev coMetric (d : ℕ := 3) : ℝT[d, .down, .down]
```

**`realLorentzTensor.contrMetric`**, an abbrev, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L37).

> The metric `ηⁱⁱ` as a real Lorentz tensor.

```lean
abbrev contrMetric (d : ℕ := 3) : ℝT[d, .up, .up]
```

## Notation

## Equivalent forms of the metrics

**`realLorentzTensor.coMetric_eq_fromConstPair`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L60).

```lean
lemma coMetric_eq_fromConstPair {d : ℕ} :
    η' d = fromConstPair (S := realLorentzTensor d) (c1 := .down) (c2 := .down)
      (Lorentz.CoMod.metric d)
```

**`realLorentzTensor.contrMetric_eq_fromConstPair`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L65).

```lean
lemma contrMetric_eq_fromConstPair {d : ℕ} :
    η d = fromConstPair (S := realLorentzTensor d)
      (c1 := .up) (c2 := .up) (Lorentz.ContrMod.metric d)
```

**`realLorentzTensor.coMetric_eq_fromPairT`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L70).

```lean
lemma coMetric_eq_fromPairT {d : ℕ} :
    η' d = fromPairT (S := realLorentzTensor d) (c1 := .down) (c2 := .down)
      (Lorentz.CoMod.metricVal d)
```

**`realLorentzTensor.contrMetric_eq_fromPairT`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L75).

```lean
lemma contrMetric_eq_fromPairT {d : ℕ} :
    η d = fromPairT (S := realLorentzTensor d) (c1 := .up) (c2 := .up)
        (Lorentz.ContrMod.metricVal d)
```

**`realLorentzTensor.actionT_coMetric`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L88).

> The tensor `coMetric` is invariant under the action of `LorentzGroup d`.

```lean
lemma actionT_coMetric {d : ℕ} (g : LorentzGroup d) :
    g • η' d = η' d
```

**`realLorentzTensor.actionT_contrMetric`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L94).

> The tensor `contrMetric` is invariant under the action of `LorentzGroup d`.

```lean
lemma actionT_contrMetric {d} (g : LorentzGroup d) : g • η d = η d
```

**`realLorentzTensor.coMetric_repr_apply_eq_minkowskiMatrix`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L103).

```lean
lemma coMetric_repr_apply_eq_minkowskiMatrix {d : ℕ}
    (b : ComponentIdx (S := realLorentzTensor d) ![Color.down, Color.down]) :
    (Tensor.basis _).repr (coMetric d) b =
    minkowskiMatrix (b 0) (b 1)
```

**`realLorentzTensor.contrMetric_repr_apply_eq_minkowskiMatrix`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L119).

```lean
lemma contrMetric_repr_apply_eq_minkowskiMatrix {d : ℕ}
    (b : ComponentIdx (S := realLorentzTensor d) ![Color.up, Color.up]) :
    (Tensor.basis _).repr (contrMetric d) b =
    minkowskiMatrix (b 0) (b 1)
```

**`realLorentzTensor.metricTensor_repr_apply_eq_minkowskiMatrix`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L136).

> The component matrix of either real Lorentz metric tensor is the Minkowski matrix.

```lean
lemma metricTensor_repr_apply_eq_minkowskiMatrix {d : ℕ} (c : Color)
    (φ : ComponentIdx (S := realLorentzTensor d) ![c, c]) :
    (Tensor.basis _).repr (metricTensor (S := realLorentzTensor d) c) φ =
      minkowskiMatrix (φ 0) (φ 1)
```

**`realLorentzTensor.toDualMapAtIndex_basis_repr_apply`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L147).

> Raising or lowering one index of a real Lorentz tensor contracts that slot's components with
> the Minkowski matrix.

```lean
lemma toDualMapAtIndex_basis_repr_apply {d n : ℕ} {c : Fin (n + 1) → Color}
    (i : Fin (n + 1)) (t : ℝT(d, c))
    (φ : ComponentIdx (S := realLorentzTensor d)
      (Function.update c i ((realLorentzTensor d).τ (c i)))) :
    (Tensor.basis _).repr (Tensor.toDualMapAtIndex (S := realLorentzTensor d) i t) φ =
      ∑ x : Fin 1 ⊕ Fin d,
        (Tensor.basis c).repr t (i.insertNth x (fun m => φ (i.succAbove m))) *
          minkowskiMatrix x (φ i)
```

**`realLorentzTensor.toDualMapAtIndex_basis_repr_apply_eq_mul`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean#L177).

> In the standard Lorentz basis, raising or lowering an index multiplies the component with that
> index fixed by the corresponding diagonal entry of the Minkowski metric.

```lean
lemma toDualMapAtIndex_basis_repr_apply_eq_mul {d n : ℕ} {c : Fin (n + 1) → Color}
    (i : Fin (n + 1)) (t : ℝT(d, c))
    (φ : ComponentIdx (S := realLorentzTensor d)
      (Function.update c i ((realLorentzTensor d).τ (c i)))) :
    (Tensor.basis _).repr (Tensor.toDualMapAtIndex (S := realLorentzTensor d) i t) φ =
      (Tensor.basis c).repr t φ * minkowskiMatrix (φ i) (φ i)
```

## Depends on

- [Dual tensors](../part-01/dual.md)
- [Physlib.Relativity.Tensors.RealTensor.Basic](realtensor-basic.md)

## Proof depends on

- [Components of real Lorentz cross contractions](realtensor-contraction-crosstoend.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Metrics/Basic.lean)
