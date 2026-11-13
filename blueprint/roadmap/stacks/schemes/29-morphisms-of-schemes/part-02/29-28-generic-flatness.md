---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_dense_open_flat_finitePresentation_of_isIntegral, AlgebraicGeometry.exists_dense_open_flat_finitePresentation
statement: formalized
proof: formalized
---

# 29.28 Generic flatness

Section 29.28 of the Stacks Project, [Tag 0529](https://stacks.math.columbia.edu/tag/0529). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 052A, a proposition

[Tag 052A](https://stacks.math.columbia.edu/tag/052A) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_flat_finitePresentation_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/GenericFlatnessIntegralBase.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/GenericFlatnessIntegralBase.lean#L52). The attribute's comment: “Deduced from the reduced-base Proposition 052B, which the Stacks Project notes supersedes this one, using that an integral scheme is reduced (01ON).”. References: EGA IV (8.9.4), “more general”; EGA IV (6.9.1), “more general”.

> **Stacks 052A.** For a finite type morphism `f : X ⟶ S` to an integral scheme and a finite
> type quasi-coherent module `F` on `X`, there is a dense open `U ⊆ S` such that `X_U → U` is flat
> and of finite presentation and `F|_{X_U}` is flat over `U` and of finite presentation over
> `𝒪_{X_U}`. An integral scheme is reduced, so this is a case of generic flatness over a reduced
> base.

```lean
public theorem exists_dense_open_flat_finitePresentation_of_isIntegral
    {X S : Scheme.{u}} (f : X ⟶ S) [IsIntegral S]
    [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] :
    ∃ U : S.Opens,
      Dense (U : Set S) ∧
        Flat (f.resLE U (f ⁻¹ᵁ U) le_rfl) ∧
        AlgebraicGeometry.FinitePresentation (f.resLE U (f ⁻¹ᵁ U) le_rfl) ∧
        AlgebraicGeometry.IsFlatOver
          (f.resLE U (f ⁻¹ᵁ U) le_rfl).toLRSHom.toShHom
          (F.restrict (f ⁻¹ᵁ U).ι) ∧
        (F.restrict (f ⁻¹ᵁ U).ι).IsFinitePresentation
```

## Tag 052B, a proposition

[Tag 052B](https://stacks.math.columbia.edu/tag/052B) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_flat_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/GenericFlatness.lean, line 1267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/GenericFlatness.lean#L1267). References: EGA IV (8.9.4), “more general”.

> **Stacks Project, Tag 052B.** A finite type morphism and a finite type
> quasi-coherent module become flat and finitely presented over a common dense
> open of a reduced base.

```lean
public theorem exists_dense_open_flat_finitePresentation
    {X S : Scheme.{u}} (f : X ⟶ S) [IsReduced S]
    [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] :
    ∃ U : S.Opens,
      Dense (U : Set S) ∧
        Flat (f.resLE U (f ⁻¹ᵁ U) le_rfl) ∧
        AlgebraicGeometry.FinitePresentation (f.resLE U (f ⁻¹ᵁ U) le_rfl) ∧
        AlgebraicGeometry.IsFlatOver
          (f.resLE U (f ⁻¹ᵁ U) le_rfl).toLRSHom.toShHom
          (F.restrict (f ⁻¹ᵁ U).ι) ∧
        (F.restrict (f ⁻¹ᵁ U).ι).IsFinitePresentation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.28, Tag 0529](https://stacks.math.columbia.edu/tag/0529)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
