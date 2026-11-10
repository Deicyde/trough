---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.iSup_eq_top_of_isHypercovering, Stacks.CategoryTheory.Hypercovering.inf_eq_iSup_edges, Stacks.CategoryTheory.Hypercovering.intersection_eq_union_of_isHypercovering, Stacks.CategoryTheory.Hypercovering.exists_hypercovering_of_isTopologicalBasis, Stacks.CategoryTheory.Hypercovering.exists_finite_hypercovering_of_isTopologicalBasis
statement: formalized
proof: formalized
---

# 25.11 Hypercoverings of spaces

Section 25.11 of the Stacks Project, [Tag 01H1](https://stacks.math.columbia.edu/tag/01H1). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01H2, an equation

[Tag 01H2](https://stacks.math.columbia.edu/tag/01H2) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.iSup_eq_top_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Spaces.lean, line 451](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Spaces.lean#L451).

> **Stacks Project, Tag 01H2.** In a hypercovering of a topological space, the opens attached
> to the degree-zero indices cover the whole space.

```lean
theorem iSup_eq_top_of_isHypercovering {X : Type u} [TopologicalSpace X]
    (K : SimplicialObject (FormalCoproduct.{w} (Over (⊤ : Opens X))))
    (hK : IsHypercovering (Opens.pretopology X) K) :
    (⨆ i : (K.obj (Opposite.op ⦋0⦌)).I, ((K.obj (Opposite.op ⦋0⦌)).obj i).left) = ⊤
```

## Tag 01H3, an equation

[Tag 01H3](https://stacks.math.columbia.edu/tag/01H3) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.inf_eq_iSup_edges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Spaces.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Spaces.lean#L468).

> **Stacks Project, Tag 01H3.** In a hypercovering of a topological space, the intersection of
> the opens attached to two vertices is the union of the opens attached to the edges whose zeroth
> and first faces are those vertices.

```lean
theorem inf_eq_iSup_edges {X : Type u} [TopologicalSpace X]
    (K : SimplicialObject (FormalCoproduct.{w} (Over (⊤ : Opens X))))
    (hK : IsHypercovering (Opens.pretopology X) K)
    (i₀ i₁ : (K.obj (Opposite.op ⦋0⦌)).I) :
    ((K.obj (Opposite.op ⦋0⦌)).obj i₀).left ⊓
        ((K.obj (Opposite.op ⦋0⦌)).obj i₁).left =
      ⨆ i : { i : (K.obj (Opposite.op ⦋1⦌)).I //
          (K.δ (0 : Fin 2)).f i = i₀ ∧ (K.δ (1 : Fin 2)).f i = i₁ },
        ((K.obj (Opposite.op ⦋1⦌)).obj i.1).left
```

## Tag 01H4, an equation

[Tag 01H4](https://stacks.math.columbia.edu/tag/01H4) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.intersection_eq_union_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Spaces.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Spaces.lean#L485).

> **Stacks Project, Tag 01H4.** In a hypercovering of a topological space, the intersection of
> a compatible family of `n + 3` degree-`n + 1` opens is the union of the degree-`n + 2` opens whose
> faces are the prescribed family. This is the source's equation in every degree at least one.

```lean
theorem intersection_eq_union_of_isHypercovering
    (X : Type u) [TopologicalSpace X]
    (K : SimplicialObject (FormalCoproduct.{w} (Over (⊤ : Opens X))))
    (hK : IsHypercovering (Opens.pretopology X) K)
    (n : ℕ)
    (i : (a : Fin (n + 3)) → (K.obj (Opposite.op (SimplexCategory.mk (n + 1)))).I)
    (hi : ∀ (a b : Fin (n + 3)) (hab : a < b),
      (K.δ (b.pred (ne_of_gt (lt_of_le_of_lt (Fin.zero_le a) hab)))).f (i a) =
        (K.δ (a.castPred (ne_of_lt (lt_of_lt_of_le hab (Fin.le_last b))))).f (i b)) :
    (⨅ a, ((K.obj (Opposite.op (SimplexCategory.mk (n + 1)))).obj (i a)).left) =
      ⨆ j : { j : (K.obj (Opposite.op (SimplexCategory.mk (n + 2)))).I //
        ∀ a, (K.δ a).f j = i a },
        ((K.obj (Opposite.op (SimplexCategory.mk (n + 2)))).obj j.1).left
```

## Tag 01H6, a lemma

[Tag 01H6](https://stacks.math.columbia.edu/tag/01H6) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercovering_of_isTopologicalBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/TopologicalBasis.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/TopologicalBasis.lean#L260).

> **Stacks Project, Tag 01H6.** Every basis of a topological space supports a hypercovering all
> of whose constituent open subsets belong to that basis.

```lean
theorem exists_hypercovering_of_isTopologicalBasis
    (B : Set (Set X)) (hB : IsTopologicalBasis B) :
    ∃ K : SimplicialObject (FormalCoproduct.{u} (Over (⊤ : Opens X))),
      IsHypercovering (Opens.pretopology X) K ∧
        ∀ n : ℕ, ∀ i : (K.obj (Opposite.op ⦋n⦌)).I,
          ((K.obj (Opposite.op ⦋n⦌)).obj i).left.1 ∈ B
```

## Tag 01H7, a lemma

[Tag 01H7](https://stacks.math.columbia.edu/tag/01H7) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_finite_hypercovering_of_isTopologicalBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/TopologicalBasis.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/Construction/TopologicalBasis.lean#L314).

> **Stacks Project, Tag 01H7.** A quasi-compact topological space with a basis of
> quasi-compact opens and quasi-compact intersections of quasi-compact opens has a hypercovering
> subordinate to that basis whose index type is finite in every degree.

```lean
theorem exists_finite_hypercovering_of_isTopologicalBasis
    (B : Set (Set X)) (hB : IsTopologicalBasis B)
    (hX : IsCompact (Set.univ : Set X))
    (hBcompact : ∀ U ∈ B, IsCompact U)
    (hInter : ∀ U V : Set X, IsOpen U → IsCompact U →
      IsOpen V → IsCompact V → IsCompact (U ∩ V)) :
    ∃ K : SimplicialObject (FormalCoproduct.{u} (Over (⊤ : Opens X))),
      IsHypercovering (Opens.pretopology X) K ∧
        ∀ n : ℕ, Finite (K.obj (Opposite.op (SimplexCategory.mk n))).I ∧
          ∀ i : (K.obj (Opposite.op (SimplexCategory.mk n))).I,
            ((K.obj (Opposite.op (SimplexCategory.mk n))).obj i).left.1 ∈ B
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.11, Tag 01H1](https://stacks.math.columbia.edu/tag/01H1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
