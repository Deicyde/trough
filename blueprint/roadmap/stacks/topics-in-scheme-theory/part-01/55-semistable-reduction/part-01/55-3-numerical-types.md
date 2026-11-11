---
declaration: section
origin: cited
lean: AlgebraicGeometry.NumericalType, AlgebraicGeometry.NumericalType.Equivalent, AlgebraicGeometry.NumericalType.cast_genus, AlgebraicGeometry.NumericalType.genus, AlgebraicGeometry.NumericalType.intersection_self_eq_zero_of_componentCount_eq_one, AlgebraicGeometry.NumericalType.genus_eq_of_componentCount_eq_one, AlgebraicGeometry.NumericalType.componentGenus_eq_zero_of_genus_neg, AlgebraicGeometry.NumericalType.irreducibleTypes_equiv_factorizations_of_genus_neg
statement: formalized
proof: formalized
---

# 55.3 Numerical types

Section 55.3 of the Stacks Project, [Tag 0C6Y](https://stacks.math.columbia.edu/tag/0C6Y). 16 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C6Z, a definition

[Tag 0C6Z](https://stacks.math.columbia.edu/tag/0C6Z) in the Stacks Project.

**`AlgebraicGeometry.NumericalType`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean#L57).

> A **numerical type**: positive integer multiplicities and weights, nonnegative component
> genera, and a connected symmetric intersection matrix whose weighted rows vanish and whose entries
> in each row are divisible by that row's weight.

```lean
public structure NumericalType
```

## Tag 0C70, a definition

[Tag 0C70](https://stacks.math.columbia.edu/tag/0C70) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.Equivalent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean#L100).

> Two numerical types are **equivalent** if a bijective relabelling of their components preserves
> all four families of numerical data.

```lean
public def Equivalent (T T' : NumericalType) : Prop
```

## Tag 0C71, a lemma

[Tag 0C71](https://stacks.math.columbia.edu/tag/0C71) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.cast_genus`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Genus.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Genus.lean#L87).

> The rational expression defining the genus of a numerical type is the image of
> an integer.

```lean
public lemma cast_genus (T : NumericalType) :
    (genus T : ℚ) =
      1 + ∑ i, (T.multiplicity i : ℚ) *
        ((T.weight i : ℚ) * ((T.componentGenus i : ℚ) - 1) -
          (T.intersection i i : ℚ) / 2)
```

## Tag 0C72, a definition

[Tag 0C72](https://stacks.math.columbia.edu/tag/0C72) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.genus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Genus.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Genus.lean#L80). The attribute's comment: “a numerical type of genus g”.

> The integer genus of a numerical type.

```lean
public def genus (T : NumericalType) : ℤ
```

## Tag 0C73, a lemma

[Tag 0C73](https://stacks.math.columbia.edu/tag/0C73) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.intersection_self_eq_zero_of_componentCount_eq_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L112). The attribute's comment: “diagonal intersection”.

> The diagonal intersection number of the unique component is zero.

```lean
public lemma intersection_self_eq_zero_of_componentCount_eq_one
    (T : NumericalType) (hT : T.componentCount = 1) :
    T.intersection ⟨0, T.componentCount_pos⟩ ⟨0, T.componentCount_pos⟩ = 0
```

**`AlgebraicGeometry.NumericalType.genus_eq_of_componentCount_eq_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L123). The attribute's comment: “genus formula”.

> The genus formula for a one-component numerical type.

```lean
public lemma genus_eq_of_componentCount_eq_one (T : NumericalType)
    (hT : T.componentCount = 1) :
    genus T = 1 + T.multiplicity ⟨0, T.componentCount_pos⟩ *
      T.weight ⟨0, T.componentCount_pos⟩ *
        (T.componentGenus ⟨0, T.componentCount_pos⟩ - 1)
```

**`AlgebraicGeometry.NumericalType.componentGenus_eq_zero_of_genus_neg`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L157). The attribute's comment: “negative genus component”.

> In negative genus, the unique component has genus zero.

```lean
public lemma componentGenus_eq_zero_of_genus_neg (g : ℤ) (hg : g < 0)
    (T : IrreducibleTypes g) :
    T.1.componentGenus ⟨0, T.1.componentCount_pos⟩ = 0
```

**`AlgebraicGeometry.NumericalType.irreducibleTypes_equiv_factorizations_of_genus_neg`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L165). The attribute's comment: “negative genus classification”.

> In negative genus, one-component numerical types correspond exactly to
> positive factorizations of `1 - g`, via multiplicity and weight.

```lean
public lemma irreducibleTypes_equiv_factorizations_of_genus_neg (g : ℤ) (hg : g < 0) :
    ∃ e : IrreducibleTypes g ≃
        {p : ℤ × ℤ // 0 < p.1 ∧ 0 < p.2 ∧ p.1 * p.2 = 1 - g},
      ∀ T, (e T : ℤ × ℤ) =
        (T.1.multiplicity ⟨0, T.1.componentCount_pos⟩,
          T.1.weight ⟨0, T.1.componentCount_pos⟩)
```

**`AlgebraicGeometry.NumericalType.finite_irreducibleTypes_of_genus_neg`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L203). The attribute's comment: “negative genus finiteness”.

> For fixed negative genus there are only finitely many one-component
> numerical types.

```lean
public lemma finite_irreducibleTypes_of_genus_neg (g : ℤ) (hg : g < 0) :
    Set.Finite {T : NumericalType | T.componentCount = 1 ∧ genus T = g}
```

**`AlgebraicGeometry.NumericalType.multiplicity_eq_one_of_genus_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L236). The attribute's comment: “genus zero multiplicity”.

> In genus zero, the unique multiplicity is one.

```lean
public lemma multiplicity_eq_one_of_genus_zero (T : IrreducibleTypes 0) :
    T.1.multiplicity ⟨0, T.1.componentCount_pos⟩ = 1
```

**`AlgebraicGeometry.NumericalType.weight_eq_one_of_genus_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L243). The attribute's comment: “genus zero weight”.

> In genus zero, the unique weight is one.

```lean
public lemma weight_eq_one_of_genus_zero (T : IrreducibleTypes 0) :
    T.1.weight ⟨0, T.1.componentCount_pos⟩ = 1
```

**`AlgebraicGeometry.NumericalType.componentGenus_eq_zero_of_genus_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L250). The attribute's comment: “genus zero component”.

> In genus zero, the unique component has genus zero.

```lean
public lemma componentGenus_eq_zero_of_genus_zero (T : IrreducibleTypes 0) :
    T.1.componentGenus ⟨0, T.1.componentCount_pos⟩ = 0
```

**`AlgebraicGeometry.NumericalType.componentGenus_eq_one_of_genus_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L256). The attribute's comment: “genus one component”.

> In genus one, the unique component has genus one.

```lean
public lemma componentGenus_eq_one_of_genus_one (T : IrreducibleTypes 1) :
    T.1.componentGenus ⟨0, T.1.componentCount_pos⟩ = 1
```

**`AlgebraicGeometry.NumericalType.irreducibleTypes_equiv_positive_pairs_of_genus_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L267). The attribute's comment: “genus one classification”.

> In genus one, multiplicity and weight range independently over all positive
> integers.

```lean
public lemma irreducibleTypes_equiv_positive_pairs_of_genus_one :
    ∃ e : IrreducibleTypes 1 ≃ {p : ℤ × ℤ // 0 < p.1 ∧ 0 < p.2},
      ∀ T, (e T : ℤ × ℤ) =
        (T.1.multiplicity ⟨0, T.1.componentCount_pos⟩,
          T.1.weight ⟨0, T.1.componentCount_pos⟩)
```

**`AlgebraicGeometry.NumericalType.one_lt_componentGenus_of_one_lt_genus`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L295). The attribute's comment: “positive genus component”.

> Above genus one, the unique component has genus greater than one.

```lean
public lemma one_lt_componentGenus_of_one_lt_genus (g : ℤ) (hg : 1 < g)
    (T : IrreducibleTypes g) :
    1 < T.1.componentGenus ⟨0, T.1.componentCount_pos⟩
```

**`AlgebraicGeometry.NumericalType.irreducibleTypes_equiv_factorizations_of_one_lt_genus`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L309). The attribute's comment: “positive genus classification”.

> Above genus one, one-component numerical types correspond exactly to
> positive three-factor factorizations of `g - 1`.

```lean
public lemma irreducibleTypes_equiv_factorizations_of_one_lt_genus (g : ℤ) (hg : 1 < g) :
    ∃ e : IrreducibleTypes g ≃
        {p : (ℤ × ℤ) × ℤ //
          0 < p.1.1 ∧ 0 < p.1.2 ∧ 0 < p.2 ∧ p.1.1 * p.1.2 * p.2 = g - 1},
      ∀ T, (e T : (ℤ × ℤ) × ℤ) =
        ((T.1.multiplicity ⟨0, T.1.componentCount_pos⟩,
            T.1.weight ⟨0, T.1.componentCount_pos⟩),
          T.1.componentGenus ⟨0, T.1.componentCount_pos⟩ - 1)
```

**`AlgebraicGeometry.NumericalType.finite_irreducibleTypes_of_one_lt_genus`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Irreducible.lean#L359). The attribute's comment: “positive genus finiteness”.

> For fixed genus greater than one there are only finitely many one-component
> numerical types.

```lean
public lemma finite_irreducibleTypes_of_one_lt_genus (g : ℤ) (hg : 1 < g) :
    Set.Finite {T : NumericalType | T.componentCount = 1 ∧ genus T = g}
```

## Tag 0C74, a lemma

[Tag 0C74](https://stacks.math.columbia.edu/tag/0C74) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.intersection_self_neg_of_one_lt_componentCount`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean#L57).

> Every diagonal intersection number of a numerical type with more than one
> component is strictly negative.

```lean
public lemma intersection_self_neg_of_one_lt_componentCount
    (T : NumericalType) (hcomponentCount : 1 < T.componentCount)
    (i : Fin T.componentCount) :
    T.intersection i i < 0
```

## Tag 0C75, a lemma

[Tag 0C75](https://stacks.math.columbia.edu/tag/0C75) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.componentGenus_eq_zero_of_contribution_neg`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean#L107). The attribute's comment: “component genus”.

> A component with negative contribution to the genus has component genus zero.

```lean
public lemma componentGenus_eq_zero_of_contribution_neg
    (T : NumericalType) (hn : 1 < T.componentCount) (i : Fin T.componentCount)
    (hi : (T.multiplicity i : ℚ) *
      ((T.weight i : ℚ) * ((T.componentGenus i : ℚ) - 1) -
        (T.intersection i i : ℚ) / 2) < 0) :
    T.componentGenus i = 0
```

**`AlgebraicGeometry.NumericalType.intersection_self_eq_neg_weight_of_contribution_neg`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean#L126). The attribute's comment: “diagonal intersection”.

> The diagonal intersection number of a component with negative contribution to
> the genus is the negative of its weight.

```lean
public lemma intersection_self_eq_neg_weight_of_contribution_neg
    (T : NumericalType) (hn : 1 < T.componentCount) (i : Fin T.componentCount)
    (hi : (T.multiplicity i : ℚ) *
      ((T.weight i : ℚ) * ((T.componentGenus i : ℚ) - 1) -
        (T.intersection i i : ℚ) / 2) < 0) :
    T.intersection i i = -T.weight i
```

## Tag 0C76, a definition

[Tag 0C76](https://stacks.math.columbia.edu/tag/0C76) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.IsMinusOneIndex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean#L112).

> An index is a minus-one index if its component genus is zero and its diagonal intersection
> number is the negative of its weight.

```lean
public abbrev IsMinusOneIndex (T : NumericalType) (i : Fin T.componentCount) : Prop
```

## Tag 0C77, a lemma

[Tag 0C77](https://stacks.math.columbia.edu/tag/0C77) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.contractLast`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contraction.lean, line 613](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contraction.lean#L613).

> The contraction of a numerical type along its last component, together with
> the defining formulas and invariance of its genus.

```lean
public noncomputable def contractLast (T : NumericalType)
    (h : IsMinusOneIndex T (lastIndex T)) : {T' : NumericalType // IsContraction T T'}
```

## Tag 0C78, a lemma

[Tag 0C78](https://stacks.math.columbia.edu/tag/0C78) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.one_sub_componentCount_add_edgeCount_nonneg`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Graph.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Graph.lean#L94).

> For a numerical type, one minus the number of components plus the number of
> positive-intersection pairs is nonnegative.

```lean
public lemma one_sub_componentCount_add_edgeCount_nonneg (T : NumericalType) :
    0 ≤ (1 : ℤ) - T.componentCount + edgeCount T
```

## Tag 0C79, a definition

[Tag 0C79](https://stacks.math.columbia.edu/tag/0C79) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.topologicalGenus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/TopologicalGenus.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/TopologicalGenus.lean#L41).

> The **topological genus** of a numerical type: one minus its number of
> components plus the number of pairs of distinct components whose intersection
> number is positive.

```lean
public def topologicalGenus (T : NumericalType) : ℤ
```

## Tag 0C7A, a definition

[Tag 0C7A](https://stacks.math.columbia.edu/tag/0C7A) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.IsMinimal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean#L118).

> A numerical type is **minimal** if it has no minus-one index.

```lean
public abbrev IsMinimal (T : NumericalType) : Prop
```

## Tag 0C7B, a lemma

[Tag 0C7B](https://stacks.math.columbia.edu/tag/0C7B) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.one_le_genus_of_isMinimal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Minimal.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Minimal.lean#L29).

> A minimal numerical type with more than one component has genus at least one.

```lean
public lemma one_le_genus_of_isMinimal (T : NumericalType) (hT : IsMinimal T)
    (hn : 1 < T.componentCount) :
    1 ≤ genus T
```

## Tag 0C7C, a lemma

[Tag 0C7C](https://stacks.math.columbia.edu/tag/0C7C) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.one_sub_componentCount_add_edgeCount_le_genus_of_isMinimal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/GenusBound.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/GenusBound.lean#L397).

> The topological genus of a minimal numerical type with more than one
> component is at most its genus.

```lean
public lemma one_sub_componentCount_add_edgeCount_le_genus_of_isMinimal
    (T : NumericalType) (hT : IsMinimal T) (hn : 1 < T.componentCount) :
    (1 : ℤ) - T.componentCount + edgeCount T ≤ genus T
```

## Tag 0C7D, a lemma

[Tag 0C7D](https://stacks.math.columbia.edu/tag/0C7D) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.componentGenus_eq_zero_of_contribution_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean#L169). The attribute's comment: “component genus”.

> A component of zero contribution in a numerical type with more than one
> component has component genus zero.

```lean
public lemma componentGenus_eq_zero_of_contribution_eq_zero
    (T : NumericalType) (hn : 1 < T.componentCount) (i : Fin T.componentCount)
    (hi : (T.multiplicity i : ℚ) *
      ((T.weight i : ℚ) * ((T.componentGenus i : ℚ) - 1) -
        (T.intersection i i : ℚ) / 2) = 0) :
    T.componentGenus i = 0
```

**`AlgebraicGeometry.NumericalType.intersection_self_eq_neg_two_mul_weight_of_contribution_eq_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Contribution.lean#L188). The attribute's comment: “diagonal intersection”.

> A component of zero contribution in a numerical type with more than one
> component has diagonal intersection number equal to minus twice its weight.

```lean
public lemma intersection_self_eq_neg_two_mul_weight_of_contribution_eq_zero
    (T : NumericalType) (hn : 1 < T.componentCount) (i : Fin T.componentCount)
    (hi : (T.multiplicity i : ℚ) *
      ((T.weight i : ℚ) * ((T.componentGenus i : ℚ) - 1) -
        (T.intersection i i : ℚ) / 2) = 0) :
    T.intersection i i = -2 * T.weight i
```

## Tag 0C7E, a definition

[Tag 0C7E](https://stacks.math.columbia.edu/tag/0C7E) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.IsMinusTwoIndex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/NumericalType/Defs.lean#L126).

> An index is a minus-two index if its component genus is zero and its diagonal intersection
> number is negative twice its weight.

```lean
public abbrev IsMinusTwoIndex (T : NumericalType) (i : Fin T.componentCount) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.3, Tag 0C6Y](https://stacks.math.columbia.edu/tag/0C6Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
