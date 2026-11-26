---
declaration: module
origin: cited
lean: suTensor.epsilon, suTensor.sum_mul_epsilon, suTensor.epsilonPair₁₂, suTensor.epsilonPair₁₃, suTensor.basis_repr_epsilonPair₁₂, suTensor.basis_repr_epsilonPair₁₃, suTensor.sum_fin_four_arrow, suTensor.sum_mul_epsilon_mul_epsilon
statement: formalized
proof: formalized
---

# The pairings of four fundamental indices of `SU(2)` by the Levi-Civita symbol

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Invariants.LeviCivitaPairing`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean): 20 declarations, 18 with a docstring.

> The invariant tensors with four fundamental indices of `SU(2)` are spanned by two pairings of
> antisymmetric symbols.

## i. Overview

> Four fundamental indices of `SU(2)` can be paired off by the antisymmetric symbol in three
> ways, and the Schouten identity is one linear relation between them. The invariant tensors are
> the combinations of the pairings `ε^{ab} ε^{cd}` and `ε^{ac} ε^{bd}`, `epsilonPair₁₂` and
> `epsilonPair₁₃` (A, B).
>
> Three elements of `SU(2)` pin the components `c` of an invariant tensor down (B). The phase
> `diag (ω, ω̄)`, for `ω` a primitive eighth root of unity, scales `c l` by `ω` to the power of the
> number of zeros of `l` plus seven times the number of ones, so only the six balanced components,
> with two labels of each kind, survive. The quarter turn equates each balanced component with its
> complement, leaving three unknowns. The eighth turn carries `c ![0, 0, 0, 0]` to a quarter of the
> sum of the balanced components, which therefore vanishes. Two unknowns remain, and they are the
> coefficients of the two pairings.
>
> For an equivariant map out of these tensors, and for the map `liftComponents T` of a family, the
> invariants reduce to the span of the images of the two pairings (C).

## ii. Key results

> - `suTensor.epsilonPair₁₂`, `suTensor.epsilonPair₁₃` : the two pairings.
> - `suTensor.invariants_fund_pow_four_eq_span_epsilonPairs` : the invariant tensors are the span
>   of the two pairings.
> - `suTensor.reducesInvariantsTo_span_epsilonContractions` : the reduction of the invariants of
>   the span of a family.

## iv. References

> * None.

## A. The two pairings

**`suTensor.epsilon`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L68).

> The antisymmetric symbol of `SU(2)` as a function of two labels.

```lean
def epsilon (a b : Fin 2) : ℂ
```

**`suTensor.sum_mul_epsilon`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L71).

> The antisymmetric symbol is invariant, `∑ g a x g b y ε x y = det g ε a b`.

```lean
lemma sum_mul_epsilon (g : SU 2) (a b : Fin 2) :
    ∑ x, ∑ y, g.1 a x * g.1 b y * epsilon x y = epsilon a b
```

**`suTensor.epsilonPair₁₂`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L82).

> The pairing `ε^{ab} ε^{cd}` of the first index with the second and the third with the
> fourth.

```lean
noncomputable def epsilonPair₁₂ : (suTensor 2).Tensor fun _ : Fin 4 => .fund
```

**`suTensor.epsilonPair₁₃`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L88).

> The pairing `ε^{ac} ε^{bd}` of the first index with the third and the second with the
> fourth.

```lean
noncomputable def epsilonPair₁₃ : (suTensor 2).Tensor fun _ : Fin 4 => .fund
```

**`suTensor.basis_repr_epsilonPair₁₂`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L92).

```lean
lemma basis_repr_epsilonPair₁₂ (l : Fin 4 → Fin 2) :
    (Tensor.basis _).repr epsilonPair₁₂ l = epsilon (l 0) (l 1) * epsilon (l 2) (l 3)
```

**`suTensor.basis_repr_epsilonPair₁₃`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L96).

```lean
lemma basis_repr_epsilonPair₁₃ (l : Fin 4 → Fin 2) :
    (Tensor.basis _).repr epsilonPair₁₃ l = epsilon (l 0) (l 2) * epsilon (l 1) (l 3)
```

**`suTensor.sum_fin_four_arrow`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L101).

> A sum over four labels is a fourfold sum.

```lean
lemma sum_fin_four_arrow {M : Type*} [AddCommMonoid M] (F : (Fin 4 → Fin 2) → M) :
    ∑ ψ : Fin 4 → Fin 2, F ψ = ∑ x, ∑ y, ∑ z, ∑ w, F ![x, y, z, w]
```

**`suTensor.sum_mul_epsilon_mul_epsilon`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L116).

> A product of two invariant pairings of labels is invariant.

```lean
lemma sum_mul_epsilon_mul_epsilon (g : SU 2) (l : Fin 4 → Fin 2) (i j k m : Fin 4)
    (hijkm : ∀ ψ : Fin 4 → Fin 2, (∏ r, g.1 (l r) (ψ r))
      = g.1 (l i) (ψ i) * g.1 (l j) (ψ j) * (g.1 (l k) (ψ k) * g.1 (l m) (ψ m)))
    (F : Fin 2 → Fin 2 → Fin 2 → Fin 2 → Fin 4 → Fin 2) (hF : ∀ x y z w, F x y z w i = x ∧
      F x y z w j = y ∧ F x y z w k = z ∧ F x y z w m = w)
    (hsum : ∀ G : (Fin 4 → Fin 2) → ℂ, ∑ ψ, G ψ = ∑ x, ∑ y, ∑ z, ∑ w, G (F x y z w)) :
    ∑ ψ : Fin 4 → Fin 2, (∏ r, g.1 (l r) (ψ r)) * (epsilon (ψ i) (ψ j) * epsilon (ψ k) (ψ m))
      = epsilon (l i) (l j) * epsilon (l k) (l m)
```

**`suTensor.epsilonPair₁₂_invariant`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L136).

> The pairing `ε^{ab} ε^{cd}` is invariant.

```lean
lemma epsilonPair₁₂_invariant (g : SU 2) : g • epsilonPair₁₂ = epsilonPair₁₂
```

**`suTensor.epsilonPair₁₃_invariant`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L144).

> The pairing `ε^{ac} ε^{bd}` is invariant.

```lean
lemma epsilonPair₁₃_invariant (g : SU 2) : g • epsilonPair₁₃ = epsilonPair₁₃
```

## B. The invariant tensors

**`suTensor.eq_zero_of_not_dvd`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L169).

> The phase `diag (ω, ω̄)`, with `ω` a primitive eighth root of unity, scales the component at
> `l` by `ω` to the power of the number of zeros of `l` plus seven times the number of ones, so
> the component vanishes unless that power is a multiple of eight.

```lean
lemma eq_zero_of_not_dvd (l : Fin 4 → Fin 2) (hl : ¬ 8 ∣ ∑ i, ![1, 7] (l i)) : c l = 0
```

**`suTensor.quarterTurn_relations`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L195).

> The quarter turn equates each balanced component with its complement.

```lean
lemma quarterTurn_relations :
    c ![0, 0, 1, 1] = c ![1, 1, 0, 0] ∧ c ![0, 1, 0, 1] = c ![1, 0, 1, 0] ∧
      c ![0, 1, 1, 0] = c ![1, 0, 0, 1]
```

**`suTensor.unbalanced_eq_zero`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L208).

> The ten unbalanced components vanish.

```lean
lemma unbalanced_eq_zero :
    c ![0, 0, 0, 0] = 0 ∧ c ![0, 0, 0, 1] = 0 ∧ c ![0, 0, 1, 0] = 0 ∧ c ![0, 1, 0, 0] = 0 ∧
      c ![1, 0, 0, 0] = 0 ∧ c ![0, 1, 1, 1] = 0 ∧ c ![1, 0, 1, 1] = 0 ∧ c ![1, 1, 0, 1] = 0 ∧
      c ![1, 1, 1, 0] = 0 ∧ c ![1, 1, 1, 1] = 0
```

**`suTensor.sum_balanced_eq_zero`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L218).

> The eighth turn carries the component at `![0, 0, 0, 0]` to a quarter of the sum of the
> balanced components, so that sum vanishes.

```lean
lemma sum_balanced_eq_zero :
    c ![0, 0, 1, 1] + c ![0, 1, 0, 1] + c ![0, 1, 1, 0] + c ![1, 0, 0, 1] + c ![1, 0, 1, 0]
      + c ![1, 1, 0, 0] = 0
```

**`suTensor.eq_add_of_pairings`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L232).

> An invariant function of four labels is a combination of the two pairings, with the
> components at `![0, 1, 0, 1]` and `![0, 0, 1, 1]` as coefficients.

```lean
lemma eq_add_of_pairings (l : Fin 4 → Fin 2) :
    c l = c ![0, 1, 0, 1] * (epsilon (l 0) (l 1) * epsilon (l 2) (l 3))
      + c ![0, 0, 1, 1] * (epsilon (l 0) (l 2) * epsilon (l 1) (l 3))
```

**`suTensor.invariants_fund_pow_four_eq_span_epsilonPairs`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L251).

> The invariant tensors with four fundamental indices of `SU(2)` are the span of the two
> pairings of their indices by the antisymmetric symbol.

```lean
lemma invariants_fund_pow_four_eq_span_epsilonPairs :
    ((suTensor 2).tensorRep fun _ : Fin 4 => .fund).invariants
      = Submodule.span ℂ {epsilonPair₁₂, epsilonPair₁₃}
```

## C. The invariants of the span of a family

**`suTensor.reducesInvariantsTo_span_map_epsilonPairs`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L277).

> For any equivariant linear map out of the tensors with four fundamental indices of `SU(2)`,
> the invariants of its range reduce to the span of the images of the two pairings.

```lean
lemma reducesInvariantsTo_span_map_epsilonPairs
    {f : (suTensor 2).Tensor (fun _ : Fin 4 => .fund) →ₗ[ℂ] B}
    (hf : (suTensor 2).IsEquivariant (fun _ => .fund) ρ f) :
    ReducesInvariantsTo (fun g : SU 2 => ρ g) (LinearMap.range f)
      (Submodule.span ℂ {f epsilonPair₁₂, f epsilonPair₁₃})
```

**`suTensor.liftComponents_epsilonPair₁₂`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L288).

> The map of a family sends the first pairing to the contraction pairing the first label with
> the second and the third with the fourth.

```lean
lemma liftComponents_epsilonPair₁₂ (T : (Fin 4 → Fin 2) → B) :
    liftComponents (S := suTensor 2) (c := fun _ : Fin 4 => .fund) T epsilonPair₁₂
      = T ![0, 1, 0, 1] - T ![0, 1, 1, 0] - T ![1, 0, 0, 1] + T ![1, 0, 1, 0]
```

**`suTensor.liftComponents_epsilonPair₁₃`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L301).

> The map of a family sends the second pairing to the contraction pairing the first label with
> the third and the second with the fourth.

```lean
lemma liftComponents_epsilonPair₁₃ (T : (Fin 4 → Fin 2) → B) :
    liftComponents (S := suTensor 2) (c := fun _ : Fin 4 => .fund) T epsilonPair₁₃
      = T ![0, 0, 1, 1] - T ![0, 1, 1, 0] - T ![1, 0, 0, 1] + T ![1, 1, 0, 0]
```

**`suTensor.reducesInvariantsTo_span_epsilonContractions`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean#L314).

> For a family with four fundamental labels of `SU(2)` whose map is equivariant, the invariants
> of the span of the family reduce to the span of its two epsilon contractions.

```lean
lemma reducesInvariantsTo_span_epsilonContractions {T : (Fin 4 → Fin 2) → B}
    (hT : (suTensor 2).IsEquivariant (fun _ => .fund) ρ (liftComponents T)) :
    ReducesInvariantsTo (fun g : SU 2 => ρ g) (Submodule.span ℂ (Set.range T))
      (Submodule.span ℂ
        {T ![0, 1, 0, 1] - T ![0, 1, 1, 0] - T ![1, 0, 0, 1] + T ![1, 0, 1, 0],
          T ![0, 0, 1, 1] - T ![0, 1, 1, 0] - T ![1, 0, 0, 1] + T ![1, 1, 0, 0]})
```

## Depends on

- [The complex tensor species of `SU(N)`](globalgaugegroup-su-tensorspecies.md)

## Proof depends on

- [The Levi-Civita tensors of `SU(N)`](globalgaugegroup-su-invariants-levicivita.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/LeviCivitaPairing.lean)
