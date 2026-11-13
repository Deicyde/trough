---
declaration: section
origin: cited
lean: CategoryTheory.Pretriangulated.exists_iso_preadditiveYoneda_of_compactlyGenerated, CategoryTheory.Pretriangulated.exists_isTriangulated_rightAdjoint_of_compactlyGenerated
statement: formalized
proof: formalized
---

# 13.38 Brown representability

Section 13.38 of the Stacks Project, [Tag 0A8E](https://stacks.math.columbia.edu/tag/0A8E). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A8F, a lemma

[Tag 0A8F](https://stacks.math.columbia.edu/tag/0A8F) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_iso_preadditiveYoneda_of_compactlyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/BrownRepresentability.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/BrownRepresentability.lean#L322).

> **Brown representability**: let `D` be a triangulated category with arbitrary direct sums
> which is compactly generated, i.e. there is a family `E : ι → D` of compact objects (each
> `preadditiveCoyoneda.obj (op (E i))` preserves direct sums) whose direct sum generates `D` (the
> only objects right orthogonal to all shifts of the `E i` are the zero objects). Then every
> contravariant cohomological functor `H : Dᵒᵖ ⥤ AddCommGrpCat` which transforms direct sums into
> products is representable: `H ≅ Hom(-, X)` for some `X : D`.

```lean
public theorem exists_iso_preadditiveYoneda_of_compactlyGenerated
    {ι : Type v} (E : ι → D)
    [∀ (i : ι) (α : Type v),
      PreservesColimitsOfShape (Discrete α) (preadditiveCoyoneda.obj (op (E i)))]
    (hE : ∀ Y : D, ((ofObj E).shiftClosure ℤ).rightOrthogonal Y → IsZero Y)
    (H : Dᵒᵖ ⥤ AddCommGrpCat.{v}) [H.IsHomological]
    [∀ α : Type v, PreservesLimitsOfShape (Discrete α) H] :
    ∃ X : D, Nonempty (H ≅ preadditiveYoneda.obj X)
```

## Tag 0A8G, a proposition

[Tag 0A8G](https://stacks.math.columbia.edu/tag/0A8G) in the Stacks Project.

**`CategoryTheory.Pretriangulated.exists_isTriangulated_rightAdjoint_of_compactlyGenerated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/BrownRepresentability.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/BrownRepresentability.lean#L415). References: SGA 4 XVII (2.2.13.1), “Triangulated case”.

> Let `D` be a triangulated category with arbitrary direct sums which is compactly generated,
> i.e. there is a family `E : ι → D` of compact objects (each `preadditiveCoyoneda.obj (op (E i))`
> preserves direct sums) whose direct sum generates `D` (the only objects right orthogonal to all
> shifts of the `E i` are the zero objects). Let `F : D ⥤ D'` be an exact functor of triangulated
> categories which transforms direct sums into direct sums. Then `F` has a right adjoint `G`,
> which is again exact: the adjunction `F ⊣ G` is a triangulated adjunction for a (unique)
> `Functor.CommShift ℤ` structure on `G`.

```lean
public theorem exists_isTriangulated_rightAdjoint_of_compactlyGenerated
    (F : D ⥤ D') [F.CommShift ℤ] [F.IsTriangulated]
    [∀ α : Type v, PreservesColimitsOfShape (Discrete α) F]
    {ι : Type v} (E : ι → D)
    [∀ (i : ι) (α : Type v),
      PreservesColimitsOfShape (Discrete α) (preadditiveCoyoneda.obj (op (E i)))]
    (hE : ∀ Y : D, ((ofObj E).shiftClosure ℤ).rightOrthogonal Y → IsZero Y) :
    ∃ (G : D' ⥤ D) (adj : F ⊣ G) (_ : G.CommShift ℤ), adj.IsTriangulated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.38, Tag 0A8E](https://stacks.math.columbia.edu/tag/0A8E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
