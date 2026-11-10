---
declaration: section
origin: cited
lean: Stacks.Chow.HilbertCycleDatum, Stacks.Chow.cycleClassMap, Stacks.Chow.cycleClassMap_of, Stacks.Chow.comesFromNoetherianBase_iff_hasCompletelyDecomposedCycleClassCover
statement: formalized
proof: formalized
---

# 62.17 Relative cycles in the non-Noetherian case

Section 62.17 of the Stacks Project, [Tag 0H6U](https://stacks.math.columbia.edu/tag/0H6U). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H6V, an equation

[Tag 0H6V](https://stacks.math.columbia.edu/tag/0H6V) in the Stacks Project.

**`Stacks.Chow.HilbertCycleDatum`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HilbertCycleClass.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HilbertCycleClass.lean#L203). The attribute's comment: “the set Hilb(X/S, r)”.

> A member of `Hilb(X/S, r)`: a closed subscheme `Z ⊆ X`, given by its ideal sheaf, whose
> structure morphism `Z ⟶ S` is flat, of finite presentation, and of relative dimension at most `r`.

```lean
structure HilbertCycleDatum {X S : Scheme.{u}} (f : X ⟶ S) (r : ℕ)
```

**`Stacks.Chow.cycleClassMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HilbertCycleClass.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HilbertCycleClass.lean#L265). The attribute's comment: “the homomorphism”.

> The cycle-class homomorphism from the free abelian group on `Hilb(X/S, r)` to the families of
> `r`-cycles on the fibres of `X/S`, sending `∑ nᵢ [Zᵢ]` to `∑ nᵢ [Zᵢ/X/S]_r`.

```lean
def cycleClassMap {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f] (r : ℕ) :
    FreeAbelianGroup (HilbertCycleDatum f r) →+ FamilyOfCycles f r
```

**`Stacks.Chow.cycleClassMap_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HilbertCycleClass.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/HilbertCycleClass.lean#L272). The attribute's comment: “on generators”.

> On a generator the cycle-class homomorphism is the family of cycles `[Z/X/S]_r` of the closed
> subscheme.

```lean
theorem cycleClassMap_of {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (r : ℕ) (Z : HilbertCycleDatum f r) :
    cycleClassMap f r (FreeAbelianGroup.of Z) = Z.cycleFamily f
```

## Tag 0H6W, a lemma

[Tag 0H6W](https://stacks.math.columbia.edu/tag/0H6W) in the Stacks Project.

**`Stacks.Chow.comesFromNoetherianBase_iff_hasCompletelyDecomposedCycleClassCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonNoetherianBase.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonNoetherianBase.lean#L255).

> **Stacks Project, Lemma 0H6W.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ S` be a morphism of finite presentation, let `r ≥ 0` and let `α` be a family of
> `r`-cycles on the fibres of `X/S`. The following are equivalent:
>
> 1. there are a cartesian square with right-hand column a finite type morphism `X₀ ⟶ S₀` of
>    Noetherian schemes and `α₀ ∈ z(X₀/S₀, r)` such that `α` is the base change of `α₀` by
>    `S ⟶ S₀`;
> 2. there is a completely decomposed proper morphism `g : S' ⟶ S` of finite presentation such
>    that `g^*α` is in the image of the cycle class map of Tag 0H6V.
>
> Finite presentation of `f` is spelled `LocallyOfFinitePresentation`, `QuasiCompact` and
> `QuasiSeparated`, as in the source.

```lean
theorem comesFromNoetherianBase_iff_hasCompletelyDecomposedCycleClassCover {X S : Scheme.{u}}
    [CompactSpace S] [QuasiSeparatedSpace S] (f : X ⟶ S) [LocallyOfFinitePresentation f]
    [QuasiCompact f] [QuasiSeparated f] (r : ℕ) (α : FamilyOfCycles f r) :
    ComesFromNoetherianBase f r α ↔ HasCompletelyDecomposedCycleClassCover f r α
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.17, Tag 0H6U](https://stacks.math.columbia.edu/tag/0H6U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
