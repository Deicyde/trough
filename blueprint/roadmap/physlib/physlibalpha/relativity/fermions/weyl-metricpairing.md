---
declaration: module
origin: cited
lean: Fermion.metricPairing, Fermion.exists_eq_vecCons, Fermion.metricPairing_schouten, Fermion.pairingBasis, Fermion.pairingPoint, Fermion.pairingBasis_pairingPoint, Fermion.linearIndependent_pairingBasis, Fermion.upperUnipotent
statement: formalized
proof: formalized
---

# The metric pairings of four Weyl indices

The module `PhyslibAlpha.Relativity.Fermions.Weyl.MetricPairing`, [PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean): 27 declarations, 27 with a docstring.

> The invariants of four left-handed Weyl indices are spanned by two products of Weyl metrics.

## i. Overview

> A coefficient function `C : (Fin n → Fin 2) → ℂ` of `n` left-handed Weyl indices carries the action
> of `M ∈ SL(2, ℂ)` on each index, `SlotAction.act M C`. With four indices the products of two Weyl
> metrics `ε_{ab} = metricRaw`, pairing the slots `ε_{a₀a₁} ε_{a₂a₃}`, `ε_{a₀a₂} ε_{a₁a₃}` and
> `ε_{a₀a₃} ε_{a₁a₂}`, are invariant. They obey the Schouten identity
> `ε₀₁ ε₂₃ - ε₀₂ ε₁₃ + ε₀₃ ε₁₂ = 0` (A), and the first two span all invariants (C).
>
> The argument is infinitesimal. The unipotent elements `1 + z E` and `1 + z F` of `SL(2, ℂ)`, with
> `E = !![0, 1; 0, 0]` and `F = !![0, 0; 1, 0]`, move a fixed coefficient function along a line, so
> it is killed by the infinitesimal actions of `E` and `F`, one slot at a time (B). These
> unipotent elements generate `SL(2, ℂ)`, every element being a product of four of them, which
> `PhyslibAlpha.Relativity.Bispinors.ComplexifiedAction` uses. For four indices those two conditions
> are linear equations on the sixteen coefficients. They force every coefficient with more raised
> than lowered indices, or fewer, to vanish, and leave the six balanced ones in a two-dimensional
> space. The two coefficients at `1100` and `1010` fix all the others
> (`eq_sum_pairingBasis_of_infinitesimalAct_eq_zero`). The right-handed Weyl representation has the
> same invariants, the group acting on it through a reparametrisation of itself (C.3). The components
> of a tensor with four Weyl indices of one chirality are such a coefficient function, so the
> invariant tensors are the span of the two products of metrics (D).

## ii. Key results

> - `Fermion.metricPairing` : a product of two Weyl metrics on four indices.
> - `Fermion.exists_eq_lowerUnipotent_mul_upperUnipotent` : every element of `SL(2, ℂ)` is a product
>   of unipotent elements.
> - `Fermion.metricPairing_schouten` : the Schouten identity.
> - `Fermion.eq_sum_pairingBasis_of_infinitesimalAct_eq_zero` : a coefficient function killed by `E`
>   and `F` is a combination of `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`.
> - `Fermion.infinitesimalAct_eq_zero_of_invariant` : an invariant coefficient function is killed by
>   `E` and `F`.
> - `Fermion.mem_span_pairingBasis_iff` : the invariants of four left-handed Weyl indices are the span
>   of `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`.
> - `Fermion.linearIndependent_pairingBasis` : the two are linearly independent.
> - `Fermion.mem_span_pairingBasis_iff_map_star` : the same for right-handed indices.
> - `complexLorentzTensor.invariants_upL_pow_four_eq_span_range_leftMetricPairing`,
>   `complexLorentzTensor.invariants_upR_pow_four_eq_span_range_rightMetricPairing` : the invariant
>   tensors with four Weyl indices of one chirality.

## iv. References

> * None.

## A. Products of Weyl metrics

**`Fermion.metricPairing`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L86).

> The product `ε_{a_i a_j} ε_{a_k a_l}` of two Weyl metrics on four Weyl indices, pairing the
> slots `i, j` and `k, l`.

```lean
def metricPairing (i j k l : Fin 4) (a : Fin 4 → Fin 2) : ℂ
```

**`Fermion.exists_eq_vecCons`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L90).

> Every index vector of four slots is a vector literal.

```lean
lemma exists_eq_vecCons {α : Type*} (a : Fin 4 → α) : ∃ w x y z, a = ![w, x, y, z]
```

**`Fermion.metricPairing_schouten`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L95).

> The Schouten identity `ε₀₁ ε₂₃ - ε₀₂ ε₁₃ + ε₀₃ ε₁₂ = 0`. Two-component spinors admit no
> totally antisymmetric tensor of rank three.

```lean
lemma metricPairing_schouten :
    metricPairing 0 1 2 3 - metricPairing 0 2 1 3 + metricPairing 0 3 1 2 = 0
```

**`Fermion.pairingBasis`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L103).

> The two pairings spanning the invariants of four Weyl indices, `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`.

```lean
def pairingBasis : Fin 2 → (Fin 4 → Fin 2) → ℂ
```

**`Fermion.pairingPoint`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L106).

> Two index vectors, `1100` and `1010`, on which `pairingBasis` is the unit matrix.

```lean
def pairingPoint : Fin 2 → Fin 4 → Fin 2
```

**`Fermion.pairingBasis_pairingPoint`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L109).

> The two basis pairings evaluated at the two test points form the unit matrix.

```lean
lemma pairingBasis_pairingPoint (i j : Fin 2) :
    pairingBasis i (pairingPoint j) = if i = j then 1 else 0
```

**`Fermion.linearIndependent_pairingBasis`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L114).

> The two pairings are linearly independent.

```lean
lemma linearIndependent_pairingBasis : LinearIndependent ℂ pairingBasis
```

## B. The unipotent elements

**`Fermion.upperUnipotent`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L128).

> The unipotent element `!![1, z; 0, 1] = 1 + z E` of `SL(2, ℂ)`.

```lean
def upperUnipotent (z : ℂ) : SL(2,ℂ)
```

**`Fermion.lowerUnipotent`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L132).

> The unipotent element `!![1, 0; z, 1] = 1 + z F` of `SL(2, ℂ)`.

```lean
def lowerUnipotent (z : ℂ) : SL(2,ℂ)
```

**`Fermion.exists_eq_lowerUnipotent_mul_upperUnipotent`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L139).

> Every element of `SL(2, ℂ)` is a product of four unipotent elements, alternately lower and
> upper. With `M = !![p, q; r, s]` and `a` chosen so that `r' = a p + r ≠ 0`, the matrix
> `lowerUnipotent a * M` is `upperUnipotent ((p - 1) / r') * lowerUnipotent r' *
> upperUnipotent ((a q + s - 1) / r')`.

```lean
lemma exists_eq_lowerUnipotent_mul_upperUnipotent (M : SL(2,ℂ)) :
    ∃ a x r y : ℂ,
      M = lowerUnipotent a * upperUnipotent x * lowerUnipotent r * upperUnipotent y
```

**`Fermion.one_add_smul_zero_apply`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L165).

> At `t = 0` the line `t ↦ 1 + c t G` is the identity.

```lean
lemma one_add_smul_zero_apply (G : Matrix (Fin 2) (Fin 2) ℂ) (c : ℂ) (p q : Fin 2) :
    (1 + (c * ((0 : ℝ) : ℂ)) • G) p q = if p = q then 1 else 0
```

**`Fermion.hasDerivAt_one_add_smul`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L170).

> The line `t ↦ 1 + c t G` has derivative `c G`.

```lean
lemma hasDerivAt_one_add_smul (G : Matrix (Fin 2) (Fin 2) ℂ) (c : ℂ) (p q : Fin 2) :
    HasDerivAt (fun t : ℝ => (1 + (c * (t : ℂ)) • G) p q) ((c • G) p q) 0
```

## C. Four Weyl indices

### C.1. The infinitesimal equations

**`Fermion.infinitesimalAct_eq_zero_of_invariant`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L186).

> An invariant coefficient function of `n` Weyl indices is killed by the infinitesimal actions
> of `E` and `F`, the derivatives of the unipotent lines.

```lean
lemma infinitesimalAct_eq_zero_of_invariant {n : ℕ} {C : (Fin n → Fin 2) → ℂ}
    (hC : ∀ M : SL(2,ℂ), act M.1 C = C) :
    infinitesimalAct !![0, 1; 0, 0] C = 0 ∧ infinitesimalAct !![0, 0; 1, 0] C = 0
```

**`Fermion.infinitesimalAct_four`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L196).

> The infinitesimal action at four Weyl indices, written out slot by slot.

```lean
lemma infinitesimalAct_four (N : Fin 2 → Fin 2 → ℂ) (C : (Fin 4 → Fin 2) → ℂ) (w x y z : Fin 2) :
    infinitesimalAct N C ![w, x, y, z] = ∑ q, (N w q * C ![q, x, y, z] + N x q * C ![w, q, y, z]
      + N y q * C ![w, x, q, z] + N z q * C ![w, x, y, q])
```

**`Fermion.eq_sum_pairingBasis_of_infinitesimalAct_eq_zero`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L212).

> A coefficient function of four Weyl indices killed by `E` and `F` is a combination of
> `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`, with its values at `1100` and `1010` as coefficients. The equations
> of `E` at `0111`, of `F` at `1000` and their neighbours kill the unbalanced coefficients, and
> those of `E` at the four index vectors with a single raised slot relate the six balanced ones.

```lean
lemma eq_sum_pairingBasis_of_infinitesimalAct_eq_zero {C : (Fin 4 → Fin 2) → ℂ}
    (hE : infinitesimalAct !![0, 1; 0, 0] C = 0) (hF : infinitesimalAct !![0, 0; 1, 0] C = 0) :
    C = ∑ i, C (pairingPoint i) • pairingBasis i
```

### C.2. The invariants

> The pairings are invariant because `M ε Mᵀ = (det M) ε`, applied to each pair of slots.

**`Fermion.sum_metricRaw_mul`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L256).

> The Weyl metric against two rows of a matrix gives the determinant times the metric.

```lean
lemma sum_metricRaw_mul (M : Matrix (Fin 2) (Fin 2) ℂ) (p q : Fin 2) :
    ∑ x, ∑ z, metricRaw x z * (M p x * M q z) = M.det * metricRaw p q
```

**`Fermion.sum_pi_four`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L261).

> A sum over index vectors of four slots is a fourfold sum.

```lean
lemma sum_pi_four {β : Type*} [AddCommMonoid β] (F : (Fin 4 → Fin 2) → β) :
    ∑ d, F d = ∑ w, ∑ x, ∑ y, ∑ z, F ![w, x, y, z]
```

**`Fermion.act_metricPairing_zero_two`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L279).

> The pairing `ε₀₂ ε₁₃` is invariant.

```lean
lemma act_metricPairing_zero_two (M : SL(2,ℂ)) :
    act M.1 (metricPairing 0 2 1 3) = metricPairing 0 2 1 3
```

**`Fermion.act_metricPairing_zero_one`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L292).

> The pairing `ε₀₁ ε₂₃` is invariant.

```lean
lemma act_metricPairing_zero_one (M : SL(2,ℂ)) :
    act M.1 (metricPairing 0 1 2 3) = metricPairing 0 1 2 3
```

**`Fermion.mem_span_pairingBasis_iff`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L305).

> The invariants of four left-handed Weyl indices are the span of `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`.

```lean
lemma mem_span_pairingBasis_iff (C : (Fin 4 → Fin 2) → ℂ) :
    (∀ M : SL(2,ℂ), act M.1 C = C) ↔ C ∈ Submodule.span ℂ (Set.range pairingBasis)
```

### C.3. The other Weyl representations

> On right-handed indices `M` acts through its conjugate, which runs over all of `SL(2, ℂ)` as `M`
> does (`Fermion.map_star_coe_map_starRingEnd`), so their invariants are the same span.

**`Fermion.mem_span_pairingBasis_iff_map_star`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L344).

> The invariants of four right-handed Weyl indices are the span of `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`.

```lean
lemma mem_span_pairingBasis_iff_map_star (C : (Fin 4 → Fin 2) → ℂ) :
    (∀ M : SL(2,ℂ), act (M.1.map star) C = C)
      ↔ C ∈ Submodule.span ℂ (Set.range pairingBasis)
```

## D. Tensors with four Weyl indices of one chirality

> The components of a tensor with four left-handed Weyl indices are a coefficient function of four
> Weyl indices, on which `g` acts by `act g.1`, and those of a tensor with four right-handed ones a
> coefficient function on which `g` acts by `act (g.1.map star)`. The classifications of C are
> thereby classifications of the invariant tensors, through
> `TensorSpecies.invariants_tensorRep_eq_map_componentEquiv`. The dual colours are reached from
> these by `TensorSpecies.invariants_tensorRep_update_eq_map_toDualMapAtIndex`.

**`Fermion.upLPowFourIdx`**, a def, [line 369](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L369).

> The component indices of a tensor with four left-handed Weyl indices, as four spinor
> labels.

```lean
def upLPowFourIdx :
    Tensor.ComponentIdx (S := complexLorentzTensor) (fun _ : Fin 4 => Color.upL) ≃
      (Fin 4 → Fin 2)
```

**`Fermion.upRPowFourIdx`**, a def, [line 376](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L376).

> The component indices of a tensor with four right-handed Weyl indices, as four spinor
> labels.

```lean
def upRPowFourIdx :
    Tensor.ComponentIdx (S := complexLorentzTensor) (fun _ : Fin 4 => Color.upR) ≃
      (Fin 4 → Fin 2)
```

**`Fermion.leftMetricPairing`**, a def, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L383).

> The products of Weyl metrics `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃` as tensors with four left-handed Weyl
> indices.

```lean
noncomputable def leftMetricPairing (i : Fin 2) : ℂT(fun _ : Fin 4 => Color.upL)
```

**`Fermion.rightMetricPairing`**, a def, [line 388](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L388).

> The products of Weyl metrics `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃` as tensors with four right-handed Weyl
> indices.

```lean
noncomputable def rightMetricPairing (i : Fin 2) : ℂT(fun _ : Fin 4 => Color.upR)
```

**`complexLorentzTensor.invariants_upL_pow_four_eq_span_range_leftMetricPairing`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L393).

> The invariant tensors with four left-handed Weyl indices are the span of the two products of
> Weyl metrics `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`.

```lean
lemma _root_.complexLorentzTensor.invariants_upL_pow_four_eq_span_range_leftMetricPairing :
    (complexLorentzTensor.tensorRep (fun _ : Fin 4 => Color.upL)).invariants =
      Submodule.span ℂ (Set.range leftMetricPairing)
```

**`complexLorentzTensor.invariants_upR_pow_four_eq_span_range_rightMetricPairing`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean#L405).

> The invariant tensors with four right-handed Weyl indices are the span of the two products of
> Weyl metrics `ε₀₂ ε₁₃` and `ε₀₁ ε₂₃`.

```lean
lemma _root_.complexLorentzTensor.invariants_upR_pow_four_eq_span_range_rightMetricPairing :
    (complexLorentzTensor.tensorRep (fun _ : Fin 4 => Color.upR)).invariants =
      Submodule.span ℂ (Set.range rightMetricPairing)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Matrices acting slot by slot on coefficient functions](../../mathematics/part-02/representationtheory/slotaction.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [Invariants of two Weyl indices](weyl-metric.md)

## Sources

- [PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Fermions/Weyl/MetricPairing.lean)
