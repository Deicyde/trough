---
declaration: section
origin: cited
lean: AlgebraicGeometry.NumericalType.isTwoVertexConfiguration_or_swap, AlgebraicGeometry.NumericalType.exists_ordering_of_three_minus_two_indices, AlgebraicGeometry.NumericalType.four_minus_two_indices, AlgebraicGeometry.NumericalType.exists_d4_configuration_of_four_isMinusTwoIndex, AlgebraicGeometry.NumericalType.five_chain_is_A5_or_C5_or_B5, AlgebraicGeometry.NumericalType.not_exists_fourfold_of_five_lt_componentCount, AlgebraicGeometry.NumericalType.exists_weight_eq_d5_of_isMinusTwoIndex, AlgebraicGeometry.NumericalType.multiplicity_le_of_d5_at_zero
statement: formalized
proof: formalized
---

# 55.5 Classification of proper subgraphs

Section 55.5 of the Stacks Project, [Tag 0C7L](https://stacks.math.columbia.edu/tag/0C7L). 17 tags here are carried by 41 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C7M, a lemma

[Tag 0C7M](https://stacks.math.columbia.edu/tag/0C7M) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.isTwoVertexConfiguration_or_swap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/TwoVertices.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/TwoVertices.lean#L178).

> A positively intersecting pair of minus-two indices in a numerical type with
> more than two components has type `A₂`, `B₂`, or `G₂`, up to exchanging the
> indices.

```lean
public lemma isTwoVertexConfiguration_or_swap (T : NumericalType)
    (hn : 2 < T.componentCount) (i j : Fin T.componentCount)
    (hi : IsMinusTwoIndex T i) (hj : IsMinusTwoIndex T j)
    (hij : 0 < T.intersection i j) :
    IsTwoVertexConfiguration T i j ∨ IsTwoVertexConfiguration T j i
```

## Tag 0C7R, a lemma

[Tag 0C7R](https://stacks.math.columbia.edu/tag/0C7R) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.exists_ordering_of_three_minus_two_indices`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/ThreeVertices.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/ThreeVertices.lean#L475).

> Three distinct minus-two indices in a numerical type with more than three
> components, at least two of whose pairwise intersections are nonzero, can be
> ordered so that their numerical data have one of the three listed weighted-path
> forms.

```lean
public theorem exists_ordering_of_three_minus_two_indices
    (T : NumericalType) (hn : 3 < T.componentCount)
    (i j k : Fin T.componentCount)
    (hi : IsMinusTwoIndex T i) (hj : IsMinusTwoIndex T j)
    (hk : IsMinusTwoIndex T k) (hij : i ≠ j) (hik : i ≠ k) (hjk : j ≠ k)
    (hintersections :
      (T.intersection i j ≠ 0 ∧ T.intersection i k ≠ 0) ∨
      (T.intersection i j ≠ 0 ∧ T.intersection j k ≠ 0) ∨
      (T.intersection i k ≠ 0 ∧ T.intersection j k ≠ 0)) :
    ∃ v : Fin 3 → Fin T.componentCount,
      Function.Injective v ∧ Set.range v = {i, j, k} ∧
        ((∃ w : ℤ,
            T.weight (v 0) = w ∧
            T.weight (v 1) = w ∧
            T.weight (v 2) = w ∧
            T.intersection (v 0) (v 0) = -2 * w ∧
            T.intersection (v 0) (v 1) = w ∧
            T.intersection (v 0) (v 2) = 0 ∧
            T.intersection (v 1) (v 0) = w ∧
            T.intersection (v 1) (v 1) = -2 * w ∧
            T.intersection (v 1) (v 2) = w ∧
            T.intersection (v 2) (v 0) = 0 ∧
            T.intersection (v 2) (v 1) = w ∧
            T.intersection (v 2) (v 2) = -2 * w ∧
            T.multiplicity (v 1) ≤ 2 * T.multiplicity (v 0) ∧
            T.multiplicity (v 0) + T.multiplicity (v 2) ≤
              2 * T.multiplicity (v 1) ∧
            T.multiplicity (v 1) ≤ 2 * T.multiplicity (v 2)) ∨
          (∃ w : ℤ,
            T.weight (v 0) = w ∧
            T.weight (v 1) = w ∧
            T.weight (v 2) = 2 * w ∧
            T.intersection (v 0) (v 0) = -2 * w ∧
            T.intersection (v 0) (v 1) = w ∧
            T.intersection (v 0) (v 2) = 0 ∧
            T.intersection (v 1) (v 0) = w ∧
            T.intersection (v 1) (v 1) = -2 * w ∧
            T.intersection (v 1) (v 2) = 2 * w ∧
            T.intersection (v 2) (v 0) = 0 ∧
            T.intersection (v 2) (v 1) = 2 * w ∧
            T.intersection (v 2) (v 2) = -4 * w ∧
            T.multiplicity (v 1) ≤ 2 * T.multiplicity (v 0) ∧
            T.multiplicity (v 0) + 2 * T.multiplicity (v 2) ≤
              2 * T.multiplicity (v 1) ∧
            T.multiplicity (v 1) ≤ 2 * T.multiplicity (v 2)) ∨
          (∃ w : ℤ,
            T.weight (v 0) = 2 * w ∧
            T.weight (v 1) = 2 * w ∧
            T.weight (v 2) = w ∧
            T.intersection (v 0) (v 0) = -4 * w ∧
            T.intersection (v 0) (v 1) = 2 * w ∧
            T.intersection (v 0) (v 2) = 0 ∧
            T.intersection (v 1) (v 0) = 2 * w ∧
            T.intersection (v 1) (v 1) = -4 * w ∧
            T.intersection (v 1) (v 2) = 2 * w ∧
            T.intersection (v 2) (v 0) = 0 ∧
            T.intersection (v 2) (v 1) = 2 * w ∧
            T.intersection (v 2) (v 2) = -2 * w ∧
            T.multiplicity (v 1) ≤ 2 * T.multiplicity (v 0) ∧
            T.multiplicity (v 0) + T.multiplicity (v 2) ≤
              2 * T.multiplicity (v 1) ∧
            T.multiplicity (v 1) ≤ T.multiplicity (v 2)))
```

## Tag 0C7V, a lemma

[Tag 0C7V](https://stacks.math.columbia.edu/tag/0C7V) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.four_minus_two_indices`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FourVertices/Chains.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FourVertices/Chains.lean#L416).

> **Stacks Project, Tag 0C7V.** A proper chain of four minus-two indices has,
> after reordering, one of the four listed weighted intersection matrices.

```lean
public theorem four_minus_two_indices
    (T : NumericalType) (hn : 4 < T.componentCount)
    (i j k l : Fin T.componentCount)
    (hdistinct : Function.Injective ![i, j, k, l])
    (hi : IsMinusTwoIndex T i) (hj : IsMinusTwoIndex T j)
    (hk : IsMinusTwoIndex T k) (hl : IsMinusTwoIndex T l)
    (hij : T.intersection i j ≠ 0) (hjk : T.intersection j k ≠ 0)
    (hkl : T.intersection k l ≠ 0) :
    ∃ (σ : Equiv.Perm (Fin 4)) (w : ℤ),
      let r : Fin 4 → Fin T.componentCount := ![i, j, k, l] ∘ σ
      (((fun p => T.weight (r p)) = ![w, w, w, w] ∧
          (fun p q => T.intersection (r p) (r q)) =
            ![![-2 * w, w, 0, 0],
              ![w, -2 * w, w, 0],
              ![0, w, -2 * w, w],
              ![0, 0, w, -2 * w]] ∧
          2 * T.multiplicity (r 0) ≥ T.multiplicity (r 1) ∧
          2 * T.multiplicity (r 1) ≥ T.multiplicity (r 0) + T.multiplicity (r 2) ∧
          2 * T.multiplicity (r 2) ≥ T.multiplicity (r 1) + T.multiplicity (r 3) ∧
          2 * T.multiplicity (r 3) ≥ T.multiplicity (r 2)) ∨
        ((fun p => T.weight (r p)) = ![w, w, w, 2 * w] ∧
          (fun p q => T.intersection (r p) (r q)) =
            ![![-2 * w, w, 0, 0],
              ![w, -2 * w, w, 0],
              ![0, w, -2 * w, 2 * w],
              ![0, 0, 2 * w, -4 * w]] ∧
          2 * T.multiplicity (r 0) ≥ T.multiplicity (r 1) ∧
          2 * T.multiplicity (r 1) ≥ T.multiplicity (r 0) + T.multiplicity (r 2) ∧
          2 * T.multiplicity (r 2) ≥
            T.multiplicity (r 1) + 2 * T.multiplicity (r 3) ∧
          2 * T.multiplicity (r 3) ≥ T.multiplicity (r 2)) ∨
        ((fun p => T.weight (r p)) = ![2 * w, 2 * w, 2 * w, w] ∧
          (fun p q => T.intersection (r p) (r q)) =
            ![![-4 * w, 2 * w, 0, 0],
              ![2 * w, -4 * w, 2 * w, 0],
              ![0, 2 * w, -4 * w, 2 * w],
              ![0, 0, 2 * w, -2 * w]] ∧
          2 * T.multiplicity (r 0) ≥ T.multiplicity (r 1) ∧
          2 * T.multiplicity (r 1) ≥ T.multiplicity (r 0) + T.multiplicity (r 2) ∧
          2 * T.multiplicity (r 2) ≥ T.multiplicity (r 1) + T.multiplicity (r 3) ∧
          T.multiplicity (r 3) ≥ T.multiplicity (r 2)) ∨
        ((fun p => T.weight (r p)) = ![w, w, 2 * w, 2 * w] ∧
          (fun p q => T.intersection (r p) (r q)) =
            ![![-2 * w, w, 0, 0],
              ![w, -2 * w, 2 * w, 0],
              ![0, 2 * w, -4 * w, 2 * w],
              ![0, 0, 2 * w, -4 * w]] ∧
          2 * T.multiplicity (r 0) ≥ T.multiplicity (r 1) ∧
          2 * T.multiplicity (r 1) ≥
            T.multiplicity (r 0) + 2 * T.multiplicity (r 2) ∧
          2 * T.multiplicity (r 2) ≥ T.multiplicity (r 1) + T.multiplicity (r 3) ∧
          2 * T.multiplicity (r 3) ≥ T.multiplicity (r 2)))
```

## Tag 0C80, a lemma

[Tag 0C80](https://stacks.math.columbia.edu/tag/0C80) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.exists_d4_configuration_of_four_isMinusTwoIndex`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FourVertices/D4Configurations.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FourVertices/D4Configurations.lean#L261).

> Four distinct minus-two components, with one component meeting the other
> three, form a D4 configuration.

```lean
public lemma exists_d4_configuration_of_four_isMinusTwoIndex
    (T : NumericalType) (hn : 4 < T.componentCount)
    (i j k l : Fin T.componentCount)
    (hij : i ≠ j) (hik : i ≠ k) (hil : i ≠ l)
    (hjk : j ≠ k) (hjl : j ≠ l) (hkl : k ≠ l)
    (hi : IsMinusTwoIndex T i) (hj : IsMinusTwoIndex T j)
    (hk : IsMinusTwoIndex T k) (hl : IsMinusTwoIndex T l)
    (haij : T.intersection i j ≠ 0)
    (haik : T.intersection i k ≠ 0)
    (hail : T.intersection i l ≠ 0) :
    ∃ w : ℤ,
      0 < w ∧
      T.weight i = w ∧ T.weight j = w ∧
      T.weight k = w ∧ T.weight l = w ∧
      T.intersection i i = -2 * w ∧
      T.intersection j j = -2 * w ∧
      T.intersection k k = -2 * w ∧
      T.intersection l l = -2 * w ∧
      T.intersection i j = w ∧ T.intersection j i = w ∧
      T.intersection i k = w ∧ T.intersection k i = w ∧
      T.intersection i l = w ∧ T.intersection l i = w ∧
      T.intersection j k = 0 ∧ T.intersection k j = 0 ∧
      T.intersection j l = 0 ∧ T.intersection l j = 0 ∧
      T.intersection k l = 0 ∧ T.intersection l k = 0 ∧
      2 * T.multiplicity i ≥
        T.multiplicity j + T.multiplicity k + T.multiplicity l ∧
      2 * T.multiplicity j ≥ T.multiplicity i ∧
      2 * T.multiplicity k ≥ T.multiplicity i ∧
      2 * T.multiplicity l ≥ T.multiplicity i ∧
      T.multiplicity j ≤ T.multiplicity i ∧
      T.multiplicity k ≤ T.multiplicity i ∧
      T.multiplicity l ≤ T.multiplicity i
```

## Tag 0C82, a lemma

[Tag 0C82](https://stacks.math.columbia.edu/tag/0C82) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.five_chain_is_A5_or_C5_or_B5`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FiveChain/Classification.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FiveChain/Classification.lean#L33).

> Five distinct minus-two indices joined consecutively in a numerical type
> with more than five components form, after reordering, a configuration of type
> `A₅`, `C₅`, or `B₅`.

```lean
public lemma five_chain_is_A5_or_C5_or_B5 (T : NumericalType)
    (hcount : 5 < T.componentCount)
    (v : Fin 5 → Fin T.componentCount) (hv : Function.Injective v)
    (hminus : ∀ r, IsMinusTwoIndex T (v r))
    (hadjacent : ∀ r : Fin 4,
      T.intersection (v r.castSucc) (v r.succ) ≠ 0) :
    ∃ σ : Equiv.Perm (Fin 5), ∃ w : ℤ, 0 < w ∧
      (IsA5Configuration T (fun r ↦ v (σ r)) w ∨
        IsC5Configuration T (fun r ↦ v (σ r)) w ∨
        IsB5Configuration T (fun r ↦ v (σ r)) w)
```

## Tag 0C86, a lemma

[Tag 0C86](https://stacks.math.columbia.edu/tag/0C86) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.not_exists_fourfold_of_five_lt_componentCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FiveVertices.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/FiveVertices.lean#L35).

> **Stacks Project, Tag 0C86.** A numerical type with more than five components
> does not have five distinct minus-two indices with one meeting all four others.

```lean
public theorem not_exists_fourfold_of_five_lt_componentCount
    (T : NumericalType) (hn : 5 < T.componentCount) :
    ¬ ∃ v : Fin 5 → Fin T.componentCount,
      Function.Injective v ∧
        (∀ r, IsMinusTwoIndex T (v r)) ∧
        (∀ r, r ≠ 0 → 0 < T.intersection (v 0) (v r))
```

## Tag 0C87, a lemma

[Tag 0C87](https://stacks.math.columbia.edu/tag/0C87) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.exists_weight_eq_d5_of_isMinusTwoIndex`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean#L180). The attribute's comment: “weights and intersections”.

> Five minus-two indices forming the edges of a `D5` diagram in a numerical
> type with more than five components have equal weights, the standard `D5`
> intersection matrix.

```lean
public lemma exists_weight_eq_d5_of_isMinusTwoIndex (T : NumericalType)
    (hn : 5 < T.componentCount) (v : Fin 5 ↪ Fin T.componentCount)
    (hminus : ∀ r, IsMinusTwoIndex T (v r))
    (h₀₁ : T.intersection (v 0) (v 1) ≠ 0)
    (h₁₂ : T.intersection (v 1) (v 2) ≠ 0)
    (h₂₃ : T.intersection (v 2) (v 3) ≠ 0)
    (h₂₄ : T.intersection (v 2) (v 4) ≠ 0) :
    ∃ w : ℤ,
      (fun r ↦ T.weight (v r)) = ![w, w, w, w, w] ∧
      (fun r s ↦ T.intersection (v r) (v s)) =
        !![-2 * w, w, 0, 0, 0;
           w, -2 * w, w, 0, 0;
           0, w, -2 * w, w, w;
           0, 0, w, -2 * w, 0;
           0, 0, w, 0, -2 * w]
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_d5_at_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean#L368). The attribute's comment: “first multiplicity inequality”.

> The first multiplicity inequality for a proper `D5` subgraph.

```lean
public lemma multiplicity_le_of_d5_at_zero (T : NumericalType)
    (hn : 5 < T.componentCount) (v : Fin 5 ↪ Fin T.componentCount)
    (hminus : ∀ r, IsMinusTwoIndex T (v r))
    (h₀₁ : T.intersection (v 0) (v 1) ≠ 0)
    (h₁₂ : T.intersection (v 1) (v 2) ≠ 0)
    (h₂₃ : T.intersection (v 2) (v 3) ≠ 0)
    (h₂₄ : T.intersection (v 2) (v 4) ≠ 0) :
    T.multiplicity (v 1) ≤ 2 * T.multiplicity (v 0)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_d5_at_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean#L387). The attribute's comment: “second multiplicity inequality”.

> The second multiplicity inequality for a proper `D5` subgraph.

```lean
public lemma multiplicity_le_of_d5_at_one (T : NumericalType)
    (hn : 5 < T.componentCount) (v : Fin 5 ↪ Fin T.componentCount)
    (hminus : ∀ r, IsMinusTwoIndex T (v r))
    (h₀₁ : T.intersection (v 0) (v 1) ≠ 0)
    (h₁₂ : T.intersection (v 1) (v 2) ≠ 0)
    (h₂₃ : T.intersection (v 2) (v 3) ≠ 0)
    (h₂₄ : T.intersection (v 2) (v 4) ≠ 0) :
    T.multiplicity (v 0) + T.multiplicity (v 2) ≤
      2 * T.multiplicity (v 1)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_d5_at_two`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean#L411). The attribute's comment: “third multiplicity inequality”.

> The central multiplicity inequality for a proper `D5` subgraph.

```lean
public lemma multiplicity_le_of_d5_at_two (T : NumericalType)
    (hn : 5 < T.componentCount) (v : Fin 5 ↪ Fin T.componentCount)
    (hminus : ∀ r, IsMinusTwoIndex T (v r))
    (h₀₁ : T.intersection (v 0) (v 1) ≠ 0)
    (h₁₂ : T.intersection (v 1) (v 2) ≠ 0)
    (h₂₃ : T.intersection (v 2) (v 3) ≠ 0)
    (h₂₄ : T.intersection (v 2) (v 4) ≠ 0) :
    T.multiplicity (v 1) + T.multiplicity (v 3) + T.multiplicity (v 4) ≤
      2 * T.multiplicity (v 2)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_d5_at_three`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean#L440). The attribute's comment: “fourth multiplicity inequality”.

> The fourth multiplicity inequality for a proper `D5` subgraph.

```lean
public lemma multiplicity_le_of_d5_at_three (T : NumericalType)
    (hn : 5 < T.componentCount) (v : Fin 5 ↪ Fin T.componentCount)
    (hminus : ∀ r, IsMinusTwoIndex T (v r))
    (h₀₁ : T.intersection (v 0) (v 1) ≠ 0)
    (h₁₂ : T.intersection (v 1) (v 2) ≠ 0)
    (h₂₃ : T.intersection (v 2) (v 3) ≠ 0)
    (h₂₄ : T.intersection (v 2) (v 4) ≠ 0) :
    T.multiplicity (v 2) ≤ 2 * T.multiplicity (v 3)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_d5_at_four`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/D5.lean#L459). The attribute's comment: “fifth multiplicity inequality”.

> The fifth multiplicity inequality for a proper `D5` subgraph.

```lean
public lemma multiplicity_le_of_d5_at_four (T : NumericalType)
    (hn : 5 < T.componentCount) (v : Fin 5 ↪ Fin T.componentCount)
    (hminus : ∀ r, IsMinusTwoIndex T (v r))
    (h₀₁ : T.intersection (v 0) (v 1) ≠ 0)
    (h₁₂ : T.intersection (v 1) (v 2) ≠ 0)
    (h₂₃ : T.intersection (v 2) (v 3) ≠ 0)
    (h₂₄ : T.intersection (v 2) (v 4) ≠ 0) :
    T.multiplicity (v 2) ≤ 2 * T.multiplicity (v 4)
```

## Tag 0C89, a lemma

[Tag 0C89](https://stacks.math.columbia.edu/tag/0C89) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.classify_long_chain_of_minus_two_indices`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/LongChain/Classification.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/LongChain/Classification.lean#L546).

> A proper chain of more than five distinct minus-two indices has one of the
> three long-chain configurations, after possibly reversing the chain.

```lean
public lemma classify_long_chain_of_minus_two_indices {t : ℕ} (T : NumericalType)
    (i : Fin t → Fin T.componentCount) (ht : 5 < t)
    (hproper : t < T.componentCount) (hinj : Function.Injective i)
    (hminusTwo : ∀ j, IsMinusTwoIndex T (i j))
    (hadjacent : ∀ j k, k.val = j.val + 1 → T.intersection (i j) (i k) ≠ 0) :
    IsLongChainConfiguration T i ∨
      IsLongChainConfiguration T (fun j => i (Fin.rev j))
```

## Tag 0C8D, a lemma

[Tag 0C8D](https://stacks.math.columbia.edu/tag/0C8D) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.eq_fork_of_isMinusTwoIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/Fork.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/Fork.lean#L462).

> **Stacks Project, Tag 0C8D.** A fork on more than five minus-two vertices
> inside a proper subset of the components of a numerical type has constant
> weights, with every edge equal to that weight and every other off-diagonal
> intersection equal to zero.

```lean
public theorem eq_fork_of_isMinusTwoIndex
    (T : NumericalType) (t : ℕ) (ht : 4 < t)
    (hn : t + 1 < T.componentCount)
    (i : Fin (t + 1) → Fin T.componentCount)
    (hi : Function.Injective i)
    (hminus : ∀ j, IsMinusTwoIndex T (i j))
    (hchain : ∀ j : Fin (t - 1),
      T.intersection (i ⟨j, by omega⟩) (i ⟨j + 1, by omega⟩) ≠ 0)
    (hbranch : T.intersection (i ⟨t - 2, by omega⟩) (i ⟨t, by omega⟩) ≠ 0) :
    ∃ w : ℤ,
      (∀ j, T.weight (i j) = w) ∧
      (∀ j : Fin (t - 1),
        T.intersection (i ⟨j, by omega⟩) (i ⟨j + 1, by omega⟩) = w) ∧
      T.intersection (i ⟨t - 2, by omega⟩) (i ⟨t, by omega⟩) = w ∧
      (∀ j k : Fin (t + 1), k < j →
          ¬ (j.val = k.val + 1 ∧ k.val < t - 1) →
          ¬ (j.val = t ∧ k.val = t - 2) →
          T.intersection (i j) (i k) = 0)
```

## Tag 0C8F, a lemma

[Tag 0C8F](https://stacks.math.columbia.edu/tag/0C8F) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.weight_eq_of_e6`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean#L140). The attribute's comment: “weights”.

> The weights at six distinct minus-two indices containing the five edges of an
> E6 diagram are all equal.

```lean
public lemma weight_eq_of_e6 (T : NumericalType) (hcount : 6 < T.componentCount)
    (i : Fin 6 → Fin T.componentCount) (hi : Function.Injective i)
    (hminus : ∀ r, IsMinusTwoIndex T (i r))
    (hedge : ∀ r s, IsE6ForwardEdge r s → T.intersection (i r) (i s) ≠ 0) :
    ∀ r, T.weight (i r) = T.weight (i 0)
```

**`AlgebraicGeometry.NumericalType.intersection_eq_e6Matrix`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean#L197). The attribute's comment: “intersection matrix”.

> The intersection matrix on six distinct minus-two indices containing the five
> edges of an E6 diagram is the standard weighted E6 matrix.

```lean
public lemma intersection_eq_e6Matrix (T : NumericalType) (hcount : 6 < T.componentCount)
    (i : Fin 6 → Fin T.componentCount) (hi : Function.Injective i)
    (hminus : ∀ r, IsMinusTwoIndex T (i r))
    (hedge : ∀ r s, IsE6ForwardEdge r s → T.intersection (i r) (i s) ≠ 0) :
    (fun r s => T.intersection (i r) (i s)) = e6IntersectionMatrix (T.weight (i 0))
```

**`AlgebraicGeometry.NumericalType.e6_neighborMultiplicity_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean#L293). The attribute's comment: “multiplicity inequalities”.

> At each vertex of an E6 configuration, the sum of the multiplicities at its
> neighbors is at most twice its own multiplicity.

```lean
public lemma e6_neighborMultiplicity_le (T : NumericalType) (hcount : 6 < T.componentCount)
    (i : Fin 6 → Fin T.componentCount) (hi : Function.Injective i)
    (hminus : ∀ r, IsMinusTwoIndex T (i r))
    (hedge : ∀ r s, IsE6ForwardEdge r s → T.intersection (i r) (i s) ≠ 0) :
    ∀ r, ∑ s with IsE6Adjacent r s, T.multiplicity (i s) ≤ 2 * T.multiplicity (i r)
```

## Tag 0C8H, a lemma

[Tag 0C8H](https://stacks.math.columbia.edu/tag/0C8H) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.not_exists_double_triple_subgraph`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/DoubleTriple.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/DoubleTriple.lean#L369).

> **Stacks Project, Tag 0C8H.** There is no proper double-triple
> configuration consisting of distinct minus-two indices in a numerical type.

```lean
public lemma not_exists_double_triple_subgraph
    (T : NumericalType) (t : ℕ) (ht : 4 ≤ t)
    (hproper : t + 2 < T.componentCount) :
    ¬ ∃ indices : ℕ → Fin T.componentCount,
      Set.InjOn indices (Set.Iio (t + 2)) ∧
        (∀ j < t + 2, IsMinusTwoIndex T (indices j)) ∧
        (∀ j, 1 ≤ j → j ≤ t - 1 →
          0 < T.intersection (indices j) (indices (j + 1))) ∧
        0 < T.intersection (indices 0) (indices 2) ∧
        0 < T.intersection (indices (t - 1)) (indices (t + 1))
```

## Tag 0C8I, a lemma

[Tag 0C8I](https://stacks.math.columbia.edu/tag/0C8I) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.not_exists_seven_minusTwoIndices_with_affineE6_edges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ProperSubgraph/AffineE6.lean#L342).

> **Stacks Project, Tag 0C8I.** A numerical type with more than seven components has no
> seven distinct minus-two indices whose indicated intersections form the edges of the affine
> E6 diagram.

```lean
public theorem not_exists_seven_minusTwoIndices_with_affineE6_edges
    (T : NumericalType) (hn : 7 < T.componentCount) :
    ¬ ∃ f g h i j k l : Fin T.componentCount,
      List.Pairwise (· ≠ ·) [f, g, h, i, j, k, l] ∧
      IsMinusTwoIndex T f ∧ IsMinusTwoIndex T g ∧ IsMinusTwoIndex T h ∧
      IsMinusTwoIndex T i ∧ IsMinusTwoIndex T j ∧ IsMinusTwoIndex T k ∧
      IsMinusTwoIndex T l ∧
      T.intersection f g ≠ 0 ∧ T.intersection g h ≠ 0 ∧
      T.intersection i j ≠ 0 ∧ T.intersection j h ≠ 0 ∧
      T.intersection k l ≠ 0 ∧ T.intersection l h ≠ 0
```

## Tag 0C8J, a lemma

[Tag 0C8J](https://stacks.math.columbia.edu/tag/0C8J) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.e7_subgraph_classification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L297). The attribute's comment: “intersection matrix”.

> **Stacks Project, Tag 0C8J.** The restricted intersection matrix of a
> proper `E₇` subgraph.

```lean
public theorem e7_subgraph_classification :
    (fun p q => T.intersection (i p) (i q)) =
      !![(-2 * T.weight (i 0)), T.weight (i 0), 0, 0, 0, 0, 0;
         T.weight (i 0), (-2 * T.weight (i 0)), T.weight (i 0), 0, 0, 0, 0;
         0, T.weight (i 0), (-2 * T.weight (i 0)), T.weight (i 0), 0, 0, 0;
         0, 0, T.weight (i 0), (-2 * T.weight (i 0)), T.weight (i 0), 0,
           T.weight (i 0);
         0, 0, 0, T.weight (i 0), (-2 * T.weight (i 0)), T.weight (i 0), 0;
         0, 0, 0, 0, T.weight (i 0), (-2 * T.weight (i 0)), 0;
         0, 0, 0, T.weight (i 0), 0, 0, (-2 * T.weight (i 0))]
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_weight_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L338). The attribute's comment: “common weight”.

> **Stacks Project, Tag 0C8J.** The seven weights of a proper `E₇` subgraph
> agree.

```lean
public theorem e7_subgraph_weight_eq :
    (fun p => T.weight (i p)) =
      ![T.weight (i 0), T.weight (i 0), T.weight (i 0), T.weight (i 0),
        T.weight (i 0), T.weight (i 0), T.weight (i 0)]
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_multiplicity_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L349). The attribute's comment: “first multiplicity inequality”.

> **Stacks Project, Tag 0C8J.** The multiplicity inequality at the first
> vertex.

```lean
public theorem e7_subgraph_multiplicity_le_zero :
    T.multiplicity (i 1) ≤ 2 * T.multiplicity (i 0)
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_multiplicity_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L356). The attribute's comment: “second multiplicity inequality”.

> **Stacks Project, Tag 0C8J.** The multiplicity inequality at the second
> vertex.

```lean
public theorem e7_subgraph_multiplicity_le_one :
    T.multiplicity (i 0) + T.multiplicity (i 2) ≤ 2 * T.multiplicity (i 1)
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_multiplicity_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L363). The attribute's comment: “third multiplicity inequality”.

> **Stacks Project, Tag 0C8J.** The multiplicity inequality at the third
> vertex.

```lean
public theorem e7_subgraph_multiplicity_le_two :
    T.multiplicity (i 1) + T.multiplicity (i 3) ≤ 2 * T.multiplicity (i 2)
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_multiplicity_le_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L370). The attribute's comment: “fourth multiplicity inequality”.

> **Stacks Project, Tag 0C8J.** The multiplicity inequality at the branching
> vertex.

```lean
public theorem e7_subgraph_multiplicity_le_three :
    T.multiplicity (i 2) + T.multiplicity (i 4) + T.multiplicity (i 6) ≤
      2 * T.multiplicity (i 3)
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_multiplicity_le_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L378). The attribute's comment: “fifth multiplicity inequality”.

> **Stacks Project, Tag 0C8J.** The multiplicity inequality at the fifth
> vertex.

```lean
public theorem e7_subgraph_multiplicity_le_four :
    T.multiplicity (i 3) + T.multiplicity (i 5) ≤ 2 * T.multiplicity (i 4)
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_multiplicity_le_five`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L385). The attribute's comment: “sixth multiplicity inequality”.

> **Stacks Project, Tag 0C8J.** The multiplicity inequality at the sixth
> vertex.

```lean
public theorem e7_subgraph_multiplicity_le_five :
    T.multiplicity (i 4) ≤ 2 * T.multiplicity (i 5)
```

**`AlgebraicGeometry.NumericalType.e7_subgraph_multiplicity_le_six`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E7.lean#L392). The attribute's comment: “seventh multiplicity inequality”.

> **Stacks Project, Tag 0C8J.** The multiplicity inequality at the seventh
> vertex.

```lean
public theorem e7_subgraph_multiplicity_le_six :
    T.multiplicity (i 3) ≤ 2 * T.multiplicity (i 6)
```

## Tag 0C8L, a lemma

[Tag 0C8L](https://stacks.math.columbia.edu/tag/0C8L) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.e8_submatrix_of_minus_two_indices`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L323). The attribute's comment: “weights and intersections”.

> **Stacks Project, Tag 0C8L.** A proper `E₈`-shaped configuration of
> minus-two indices has constant weight and the weighted `E₈` intersection
> matrix.

```lean
public theorem e8_submatrix_of_minus_two_indices
    (T : NumericalType) (hcard : 8 < T.componentCount)
    (i : Fin 8 → Fin T.componentCount) (hi : Function.Injective i)
    (hminus : ∀ k, IsMinusTwoIndex T (i k))
    (h12 : T.intersection (i 0) (i 1) ≠ 0)
    (h23 : T.intersection (i 1) (i 2) ≠ 0)
    (h34 : T.intersection (i 2) (i 3) ≠ 0)
    (h45 : T.intersection (i 3) (i 4) ≠ 0)
    (h56 : T.intersection (i 4) (i 5) ≠ 0)
    (h67 : T.intersection (i 5) (i 6) ≠ 0)
    (h58 : T.intersection (i 4) (i 7) ≠ 0) :
    ∃ w : ℤ,
      (∀ k, T.weight (i k) = w) ∧
      (fun k l ↦ T.intersection (i k) (i l)) = e8IntersectionMatrix w
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L406). The attribute's comment: “first multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The first multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_zero :
    T.multiplicity (i 1) ≤ 2 * T.multiplicity (i 0)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L414). The attribute's comment: “second multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The second multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_one :
    T.multiplicity (i 0) + T.multiplicity (i 2) ≤
      2 * T.multiplicity (i 1)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L423). The attribute's comment: “third multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The third multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_two :
    T.multiplicity (i 1) + T.multiplicity (i 3) ≤
      2 * T.multiplicity (i 2)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L432). The attribute's comment: “fourth multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The fourth multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_three :
    T.multiplicity (i 2) + T.multiplicity (i 4) ≤
      2 * T.multiplicity (i 3)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L441). The attribute's comment: “fifth multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The fifth multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_four :
    T.multiplicity (i 3) + T.multiplicity (i 5) + T.multiplicity (i 7) ≤
      2 * T.multiplicity (i 4)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_five`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L451). The attribute's comment: “sixth multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The sixth multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_five :
    T.multiplicity (i 4) + T.multiplicity (i 6) ≤
      2 * T.multiplicity (i 5)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_six`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L461). The attribute's comment: “seventh multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The seventh multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_six :
    T.multiplicity (i 5) ≤ 2 * T.multiplicity (i 6)
```

**`AlgebraicGeometry.NumericalType.multiplicity_le_of_e8_at_seven`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/E8.lean#L469). The attribute's comment: “eighth multiplicity inequality”.

> **Stacks Project, Tag 0C8L.** The eighth multiplicity inequality of a
> proper `E₈` subgraph.

```lean
public theorem multiplicity_le_of_e8_at_seven :
    T.multiplicity (i 4) ≤ 2 * T.multiplicity (i 7)
```

## Tag 0C8N, a lemma

[Tag 0C8N](https://stacks.math.columbia.edu/tag/0C8N) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.not_exists_branched_chain_of_eight_minus_two_indices`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/AffineE7.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/AffineE7.lean#L49).

> **Stacks Project, Tag 0C8N.** If a numerical type has more than eight
> components, it has no eight distinct minus-two indices forming a seven-vertex
> chain with an extra vertex joined to the fourth vertex.

```lean
public lemma not_exists_branched_chain_of_eight_minus_two_indices
    (T : NumericalType) (hcount : 8 < T.componentCount) :
    ¬ ∃ i : Fin 8 → Fin T.componentCount,
      Function.Injective i ∧
      (∀ r, IsMinusTwoIndex T (i r)) ∧
      T.intersection (i 0) (i 1) ≠ 0 ∧
      T.intersection (i 1) (i 2) ≠ 0 ∧
      T.intersection (i 2) (i 3) ≠ 0 ∧
      T.intersection (i 3) (i 4) ≠ 0 ∧
      T.intersection (i 4) (i 5) ≠ 0 ∧
      T.intersection (i 5) (i 6) ≠ 0 ∧
      T.intersection (i 7) (i 3) ≠ 0
```

## Tag 0C8P, a lemma

[Tag 0C8P](https://stacks.math.columbia.edu/tag/0C8P) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.not_exists_branched_chain_of_nine_minus_two_indices`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/AffineE8.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/AffineE8.lean#L77).

> If a numerical type has more than nine components, it has no nine distinct
> minus-two indices forming an eight-vertex chain with an extra vertex joined to
> the fifth vertex.
>
> This is the configuration of the source's displayed *formula*: it asks for nine
> distinct `(-2)`-indices `d, e, f, g, h, i, j, k, l` with
> `a_{de}, a_{ef}, a_{fg}, a_{gh}, a_{hi}, a_{ij}, a_{jk}, a_{lh}` nonzero, so the
> chain is `d - e - f - g - h - i - j - k` and the extra index `l` is joined to
> `h`, the fifth vertex of that chain.  The source's displayed *diagram* instead
> hangs the extra vertex below the sixth bullet of the chain; the two readings
> differ, and `not_exists_branched_chain_of_nine_minus_two_indices_at_sixth` is
> the diagram reading.

```lean
public lemma not_exists_branched_chain_of_nine_minus_two_indices
    (T : NumericalType) (hcount : 9 < T.componentCount) :
    ¬ ∃ i : Fin 9 → Fin T.componentCount,
      Function.Injective i ∧
      (∀ r, IsMinusTwoIndex T (i r)) ∧
      T.intersection (i 0) (i 1) ≠ 0 ∧
      T.intersection (i 1) (i 2) ≠ 0 ∧
      T.intersection (i 2) (i 3) ≠ 0 ∧
      T.intersection (i 3) (i 4) ≠ 0 ∧
      T.intersection (i 4) (i 5) ≠ 0 ∧
      T.intersection (i 5) (i 6) ≠ 0 ∧
      T.intersection (i 6) (i 7) ≠ 0 ∧
      T.intersection (i 8) (i 4) ≠ 0
```

**`AlgebraicGeometry.NumericalType.not_exists_branched_chain_of_nine_minus_two_indices_at_sixth`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/AffineE8.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/AffineE8.lean#L232). The attribute's comment: “the configuration of the source's diagram, extra vertex at the sixth chain vertex rather than the fifth of the displayed formula”.

> The configuration drawn in the source's diagram, with the extra vertex
> joined to the sixth vertex of the chain rather than the fifth: the affine Dynkin
> diagram `Ẽ₈`, which likewise does not occur in a numerical type with more than
> nine components.
>
> The source's diagram and its displayed formula disagree about which chain vertex
> carries the extra index: the diagram shows the sixth, the formula writes
> `a_{lh}` with `h` the fifth; `not_exists_branched_chain_of_nine_minus_two_indices`
> is the formula reading.

```lean
public lemma not_exists_branched_chain_of_nine_minus_two_indices_at_sixth
    (T : NumericalType) (hcount : 9 < T.componentCount) :
    ¬ ∃ i : Fin 9 → Fin T.componentCount,
      Function.Injective i ∧
      (∀ r, IsMinusTwoIndex T (i r)) ∧
      T.intersection (i 0) (i 1) ≠ 0 ∧
      T.intersection (i 1) (i 2) ≠ 0 ∧
      T.intersection (i 2) (i 3) ≠ 0 ∧
      T.intersection (i 3) (i 4) ≠ 0 ∧
      T.intersection (i 4) (i 5) ≠ 0 ∧
      T.intersection (i 5) (i 6) ≠ 0 ∧
      T.intersection (i 6) (i 7) ≠ 0 ∧
      T.intersection (i 8) (i 5) ≠ 0
```

## Tag 0C8Q, a proposition

[Tag 0C8Q](https://stacks.math.columbia.edu/tag/0C8Q) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.classify_connected_proper_minusTwo_subgraph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/Classification/BranchedDiagrams.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/Classification/BranchedDiagrams.lean#L692).

> A connected proper subset of minus-two indices has, up to reordering, one
> of the listed A, B, C, D, E, F, or G configurations.

```lean
public theorem classify_connected_proper_minusTwo_subgraph (T : NumericalType)
    (I : Finset (Fin T.componentCount))
    (hcard : 2 ≤ I.card) (hproper : I.card < T.componentCount)
    (hminus : ∀ i ∈ I, IsMinusTwoIndex T i)
    (hconnected : ¬ ∃ J : Finset (Fin T.componentCount),
      J.Nonempty ∧ J ⊂ I ∧
        (∀ i ∈ J, ∀ j ∈ I, j ∉ J → T.intersection i j = 0)) :
    ∃ v : Fin I.card → Fin T.componentCount,
      Function.Injective v ∧ Set.range v = (I : Set (Fin T.componentCount)) ∧
        ∃ (d : DynkinShape) (w : ℤ), IsDynkinConfiguration T v d w
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.5, Tag 0C7L](https://stacks.math.columbia.edu/tag/0C7L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
