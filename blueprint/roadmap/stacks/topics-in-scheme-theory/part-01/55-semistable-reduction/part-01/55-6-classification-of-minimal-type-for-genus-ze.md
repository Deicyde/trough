---
declaration: section
origin: cited
lean: AlgebraicGeometry.NumericalType.componentCount_eq_one_of_isMinimal_of_genus_eq_zero, AlgebraicGeometry.NumericalType.existsUnique_minimal_genus_zero, AlgebraicGeometry.NumericalType.data_of_isMinimal_of_genus_eq_zero, AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_neighborCount_le_two, AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_of_isGenusOneConfiguration, AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_componentCount_eq_one, AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_componentCount_eq_two, AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_componentCount_eq_four
statement: formalized
proof: formalized
---

# 55.6 Classification of minimal type for genus zero and one

Section 55.6 of the Stacks Project, [Tag 0C8R](https://stacks.math.columbia.edu/tag/0C8R). 2 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C8S, a lemma

[Tag 0C8S](https://stacks.math.columbia.edu/tag/0C8S) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.componentCount_eq_one_of_isMinimal_of_genus_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroOne.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroOne.lean#L47). The attribute's comment: “component count”.

> A minimal numerical type of genus zero has exactly one component.

```lean
public lemma componentCount_eq_one_of_isMinimal_of_genus_eq_zero
    (T : NumericalType) (hminimal : IsMinimal T) (hgenus : genus T = 0) :
    T.componentCount = 1
```

**`AlgebraicGeometry.NumericalType.existsUnique_minimal_genus_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroOne.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroOne.lean#L58). The attribute's comment: “existence and uniqueness”.

> There is exactly one minimal numerical type of genus zero.

```lean
public lemma existsUnique_minimal_genus_zero :
    ∃! T : NumericalType, IsMinimal T ∧ genus T = 0
```

**`AlgebraicGeometry.NumericalType.data_of_isMinimal_of_genus_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroOne.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroOne.lean#L76). The attribute's comment: “explicit numerical type”.

> The minimal numerical type of genus zero, explicitly: a minimal numerical
> type of genus zero has a single component, of multiplicity one, self-intersection
> number zero, weight one and component genus zero. Together with
> `AlgebraicGeometry.NumericalType.existsUnique_minimal_genus_zero` this identifies
> the only minimal numerical type of genus zero as `n = 1`, `m₁ = 1`, `a₁₁ = 0`,
> `w₁ = 1`, `g₁ = 0`.

```lean
public lemma data_of_isMinimal_of_genus_eq_zero
    (T : NumericalType) (hminimal : IsMinimal T) (hgenus : genus T = 0) :
    T.componentCount = 1 ∧ (∀ i, T.multiplicity i = 1) ∧
      (∀ i j, T.intersection i j = 0) ∧ (∀ i, T.weight i = 1) ∧
      (∀ i, T.componentGenus i = 0)
```

## Tag 0C8T, a lemma

[Tag 0C8T](https://stacks.math.columbia.edu/tag/0C8T) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_neighborCount_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneChain.lean, line 1243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneChain.lean#L1243). The attribute's comment: “the classification when every component meets at most two others and there are at least five of them: the cycle, cases (16) and (25), and the chains, cases (17)-(21) for five components and cases (26), (27) and (28) for six or more”.

> **Stacks Project, Tag 0C8T** for a numerical type each of whose components meets at most two
> others. With at least five components it is minimal of genus one exactly when it is the cycle —
> case (16) for five components and case (25) for six or more — or one of the chains: cases (17)
> to (21) for five components, and cases (26), (27) and (28) for six or more. From six components
> on, which of the three chains occurs is decided by the two end weights: both twice the interior
> weight gives (28), one half and one twice gives (26), both half gives (27), and an end weight
> equal to the interior weight is impossible.

```lean
public theorem isMinimal_and_genus_eq_one_iff_of_neighborCount_le_two (T : NumericalType)
    (hn : 5 ≤ T.componentCount) (hdeg : ∀ i, neighborCount T i ≤ 2) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_of_isGenusOneConfiguration`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/Basic.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/Basic.lean#L353). The attribute's comment: “every numerical type on the list is minimal of genus one”.

> **Stacks Project, Tag 0C8T**, the direction from the list to minimality and genus one.
> Every configuration on the genus-one list is a minimal numerical type of genus one.

```lean
public lemma isMinimal_and_genus_eq_one_of_isGenusOneConfiguration (T : NumericalType)
    (h : IsGenusOneConfiguration T) : IsMinimal T ∧ genus T = 1
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_componentCount_eq_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/Basic.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/Basic.lean#L402). The attribute's comment: “the classification for one component, case (1)”.

> **Stacks Project, Tag 0C8T**, case (1). A numerical type with a single component is
> minimal of genus one exactly when it is the one-component genus-one configuration: diagonal
> intersection number zero, component genus one, and arbitrary positive multiplicity and
> weight.

```lean
public lemma isMinimal_and_genus_eq_one_iff_of_componentCount_eq_one (T : NumericalType)
    (hn : T.componentCount = 1) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_componentCount_eq_two`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/Basic.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/Basic.lean#L556). The attribute's comment: “the classification for two components, cases (2) and (3)”.

> **Stacks Project, Tag 0C8T**, cases (2) and (3). A numerical type with two components is
> minimal of genus one exactly when it is one of the first two exceptional configurations.

```lean
public lemma isMinimal_and_genus_eq_one_iff_of_componentCount_eq_two (T : NumericalType)
    (hn : T.componentCount = 2) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_componentCount_eq_four`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/FourComponents.lean, line 687](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/FourComponents.lean#L687). The attribute's comment: “the classification for four components, cases (10)-(15)”.

> **Stacks Project, Tag 0C8T**, cases (10)-(15). A numerical type with four components is
> minimal of genus one exactly when it is one of the six four-component exceptional
> configurations: the affine cycle, the three affine chains and the two affine forks.

```lean
public lemma isMinimal_and_genus_eq_one_iff_of_componentCount_eq_four (T : NumericalType)
    (hn : T.componentCount = 4) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_componentCount_eq_three`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/ThreeComponents.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneConfiguration/ThreeComponents.lean#L459). The attribute's comment: “the classification for three components, cases (4)-(9)”.

> **Stacks Project, Tag 0C8T**, cases (4)-(9). A numerical type with three components is
> minimal of genus one exactly when it is one of the six three-component exceptional
> configurations: the affine cycle and the five affine chains.

```lean
public lemma isMinimal_and_genus_eq_one_iff_of_componentCount_eq_three (T : NumericalType)
    (hn : T.componentCount = 3) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_two_le_neighborCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneCycle.lean, line 1229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneCycle.lean#L1229). The attribute's comment: “the classification when every component meets at least two others and there are at least five of them: the n-cycle, case (16) for five components and case (25) for six or more”.

> **Stacks Project, Tag 0C8T** for a numerical type each of whose components meets at least
> two others and which has at least five components: it is minimal of genus one exactly when it
> is the `n`-cycle, case (16) for five components and case (25) for six or more.

```lean
public theorem isMinimal_and_genus_eq_one_iff_of_two_le_neighborCount (T : NumericalType)
    (hn : 5 ≤ T.componentCount) (hdeg : ∀ i, 2 ≤ neighborCount T i) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.exists_affine_extension_of_three_le_neighborCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneFork.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneFork.lean#L132). The attribute's comment: “the reduction for at least five components one of which meets three or more others — cases (22), (23), (24), (29), (30), (31), (32), (33) and (34): deleting a component that meets exactly one other leaves a Dynkin configuration whose shape, attachment vertex and level are one of seven explicit possibilities”.

> **Stacks Project, Tag 0C8T**, the reduction for a component meeting three or more others.
> In a minimal numerical type of genus one with at least five components, one of which meets three
> or more others, some component `l` meets exactly one other component `x`; the remaining
> components carry a Dynkin configuration `v` of shape `d` and scale `w` with `x = v r₀`, their
> multiplicities are annihilated by the weighted Cartan matrix of `d` away from `r₀` and satisfy
> `2 (M m)_{r₀} = k wf(r₀) m_{r₀}` there; and the shape, the attachment vertex and the level are
> one of seven explicit possibilities.

```lean
public theorem exists_affine_extension_of_three_le_neighborCount (T : NumericalType)
    (hmin : IsMinimal T) (hgenus : genus T = 1) (hn : 5 ≤ T.componentCount)
    (i₀ : Fin T.componentCount) (hdeg : 3 ≤ neighborCount T i₀) :
    ∃ (l x : Fin T.componentCount) (t : ℕ) (v : Fin t → Fin T.componentCount)
      (d : DynkinShape) (w : ℤ) (r₀ : Fin t) (k : ℤ),
      t + 1 = T.componentCount ∧ l ≠ x ∧
        (∀ y, y ≠ l → T.intersection l y ≠ 0 → y = x) ∧
        Function.Injective v ∧ (∀ r, v r ≠ l) ∧ (∀ y, y ≠ l → ∃ r, v r = y) ∧
        IsDynkinConfiguration T v d w ∧ v r₀ = x ∧
        (∀ r, r ≠ r₀ → ∑ s, d.weightedCartan r s * T.multiplicity (v s) = 0) ∧
        2 * ∑ s, d.weightedCartan r₀ s * T.multiplicity (v s)
          = k * d.weightFactor r₀ * T.multiplicity (v r₀) ∧
        ((d = .D ∧ ((r₀.val = 0 ∧ k = 2) ∨ (r₀.val = 1 ∧ k = 1) ∨
              ((r₀.val + 1 = t ∨ r₀.val + 2 = t) ∧ k * t = 8))) ∨
          (d = .B ∧ r₀.val = 1 ∧ k = 1) ∨ (d = .C ∧ r₀.val = 1 ∧ k = 1) ∨
          (d = .A ∧ k = 1 ∧ ((t = 7 ∧ r₀.val = 3) ∨ (t = 8 ∧ (r₀.val = 2 ∨ r₀.val = 5)))) ∨
          (d = .E6 ∧ r₀.val = 5 ∧ k = 1) ∨ (d = .E7 ∧ r₀.val = 5 ∧ k = 1) ∨
          (d = .E8 ∧ r₀.val = 0 ∧ k = 1))
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_three_le_neighborCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneForkClassification.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneForkClassification.lean#L119). The attribute's comment: “the classification when some component meets three or more others and there are at least five of them: cases (22), (23) and (24) for five components, the unbounded fork families (29), (30) and (31) for six or more, and the exceptional configurations (32), (33) and (34) on seven, eight and nine components”.

> **Stacks Project, Tag 0C8T** for a numerical type with at least five components one of
> which meets three or more others: it is minimal of genus one exactly when it is one of the forks
> and stars on the list, cases (22), (23), (24), (29), (30), (31), (32), (33) and (34).

```lean
public theorem isMinimal_and_genus_eq_one_iff_of_three_le_neighborCount (T : NumericalType)
    (hn : 5 ≤ T.componentCount) (i₀ : Fin T.componentCount) (hdeg : 3 ≤ neighborCount T i₀) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff_of_five_le_componentCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneForkClassification.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneForkClassification.lean#L134). The attribute's comment: “the classification for at least five components: cases (16)-(34)”.

> **Stacks Project, Tag 0C8T** for five or more components. A numerical type with at least
> five components is minimal of genus one exactly when it is one of the configurations on the
> list. Whether some component meets three or more others decides which half of the list it lies
> in: if none does, the type is the cycle or one of the chains — cases (16) to (21) for five
> components and cases (25) to (28) for six or more — and otherwise it is one of the forks and
> stars, cases (22), (23), (24), (29), (30), (31), (32), (33) and (34).

```lean
public theorem isMinimal_and_genus_eq_one_iff_of_five_le_componentCount (T : NumericalType)
    (hn : 5 ≤ T.componentCount) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

**`AlgebraicGeometry.NumericalType.isMinimal_and_genus_eq_one_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneForkClassification.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/GenusOneForkClassification.lean#L149). The attribute's comment: “the classification: a numerical type is minimal of genus one exactly when it is one of the thirty-four configurations listed, cases (1)-(34)”.

> **Stacks Project, Tag 0C8T.** A numerical type is minimal of genus one exactly when it is
> one of the thirty-four configurations of the list: the single component of genus one, case (1);
> the twenty-six exceptional coefficient tables on two to nine components, cases (2)-(24) and
> (32)-(34); and the seven unbounded families on six or more, cases (25)-(31).

```lean
public theorem isMinimal_and_genus_eq_one_iff (T : NumericalType) :
    (IsMinimal T ∧ genus T = 1) ↔ IsGenusOneConfiguration T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.6, Tag 0C8R](https://stacks.math.columbia.edu/tag/0C8R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
