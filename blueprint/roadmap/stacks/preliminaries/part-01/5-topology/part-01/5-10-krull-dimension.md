---
declaration: section
origin: cited
lean: topologicalKrullDim_eq_bot_iff_isEmpty, topologicalKrullDimAt, topologicalKrullDimAt_isLeast, TopologicalSpace.topologicalKrullDim_eq_iSup_localKrullDim, topologicalKrullDim_euclideanSpace_eq_zero, isOpen_upperSet_fin_two_iff, exists_finite_space_of_krullDim, TopologicalSpace.Equidimensional
statement: formalized
proof: formalized
---

# 5.10 Krull dimension

Section 5.10 of the Stacks Project, [Tag 0054](https://stacks.math.columbia.edu/tag/0054). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0055, a definition

[Tag 0055](https://stacks.math.columbia.edu/tag/0055) in the Stacks Project.

**`topologicalKrullDim_eq_bot_iff_isEmpty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/Krull.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/Krull.lean#L38). The attribute's comment: “(3)”.

> **Stacks 0055 (3).** The Krull dimension of `X` is `-∞` exactly when `X` is empty; for a
> nonempty space `closure {x}` is an irreducible closed subset, so the supremum is taken over a
> nonempty family.

```lean
theorem topologicalKrullDim_eq_bot_iff_isEmpty :
    topologicalKrullDim X = ⊥ ↔ IsEmpty X
```

**`topologicalKrullDimAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/Krull.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/Krull.lean#L49). The attribute's comment: “(4)”. References: EGA 0 (14.1.2), “dim\_x formula”; SGA 3 VIB (1.5); SGA 7 XV (1.2).

> **Stacks 0055 (4).** The Krull dimension of `X` at a point `x`: the infimum of the Krull
> dimensions of the open neighbourhoods of `x`. It is a minimum, by
> `topologicalKrullDimAt_isLeast`.

```lean
noncomputable def topologicalKrullDimAt (x : X) : WithBot ℕ∞
```

**`topologicalKrullDimAt_isLeast`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/Krull.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/Krull.lean#L69). The attribute's comment: “(4)”. References: EGA 0 (14.1.2), “dim\_x(X)=inf\_U dim(U)”; SGA 3 VIB (1.5), “partial”.

> **Stacks 0055 (4).** `topologicalKrullDimAt X x` is the *least* element of the set of
> Krull dimensions of open neighbourhoods of `x`, which is Stacks' phrasing of part (4) as a
> minimum. The infimum is attained because `WithBot ℕ∞` is well-founded.

```lean
theorem topologicalKrullDimAt_isLeast (x : X) :
    IsLeast
      {d : WithBot ℕ∞ |
        ∃ U : Set X, x ∈ U ∧ IsOpen U ∧ d = topologicalKrullDim (↥U)}
      (topologicalKrullDimAt X x)
```

## Tag 0B7I, a lemma

[Tag 0B7I](https://stacks.math.columbia.edu/tag/0B7I) in the Stacks Project.

**`TopologicalSpace.topologicalKrullDim_eq_iSup_localKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/LocalKrullDim.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/LocalKrullDim.lean#L142). References: EGA 0 (14.1.6).

> **Stacks 0B7I.** The Krull dimension of a topological space is the supremum of its
> local Krull dimensions over all of its points. When `X` is empty both sides are `⊥ = -∞`.

```lean
theorem topologicalKrullDim_eq_iSup_localKrullDim (X : Type*) [TopologicalSpace X] :
    topologicalKrullDim X = ⨆ x : X, localKrullDim X x
```

## Tag 0056, an example

[Tag 0056](https://stacks.math.columbia.edu/tag/0056) in the Stacks Project.

**`topologicalKrullDim_euclideanSpace_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/Euclidean.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/Euclidean.lean#L49).

> **Stacks 0056.** The Krull dimension of the Euclidean space `ℝ^n` is `0`.

```lean
theorem topologicalKrullDim_euclideanSpace_eq_zero (n : ℕ) :
    topologicalKrullDim (EuclideanSpace ℝ (Fin n)) = 0
```

## Tag 0057, an example

[Tag 0057](https://stacks.math.columbia.edu/tag/0057) in the Stacks Project.

**`isOpen_upperSet_fin_two_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/FiniteSpaces.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/FiniteSpaces.lean#L97).

> **Stacks 0057.** The two-point example: with the upper-set topology on `Fin 2` (so `s = 0`
> and `η = 1`), the open sets are exactly `∅`, `{η}` and the whole space.

```lean
theorem isOpen_upperSet_fin_two_iff (s : Set (Fin 2)) :
    @IsOpen (Fin 2) (Topology.upperSet (Fin 2)) s ↔
      s = ∅ ∨ s = {(1 : Fin 2)} ∨ s = Set.univ
```

**`exists_finite_space_of_krullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/FiniteSpaces.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/FiniteSpaces.lean#L127).

> **Stacks 0057.** For every `n : ℕ` there is a topological space with `n + 1` points whose
> Krull dimension is `n`, namely `Fin (n + 1)` with the upper-set topology.

```lean
theorem exists_finite_space_of_krullDim (n : ℕ) :
    ∃ (X : Type) (_ : TopologicalSpace X) (_ : Fintype X),
      Fintype.card X = n + 1 ∧ topologicalKrullDim X = (n : WithBot ℕ∞)
```

## Tag 0058, a definition

[Tag 0058](https://stacks.math.columbia.edu/tag/0058) in the Stacks Project.

**`TopologicalSpace.Equidimensional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Dimension/Equidimensional.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Dimension/Equidimensional.lean#L33). References: EGA 0 (14.1.3).

> A topological space `X` is *equidimensional* if every irreducible component of `X` has the same
> dimension, i.e. the same topological Krull dimension as a subspace.

```lean
def TopologicalSpace.Equidimensional (X : Type*) [TopologicalSpace X] : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.10, Tag 0054](https://stacks.math.columbia.edu/tag/0054)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
