---
declaration: section
origin: cited
lean: AlgebraicGeometry.relativeAssassin_subset_associatedPoints_tensor_pullback, AlgebraicGeometry.associatedPoints_tensor_pullback_eq_relativeAssassin
statement: formalized
proof: formalized
---

# 31.3 Morphisms and associated points

Section 31.3 of the Stacks Project, [Tag 05DA](https://stacks.math.columbia.edu/tag/05DA). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05DB, a lemma

[Tag 05DB](https://stacks.math.columbia.edu/tag/05DB) in the Stacks Project.

**`AlgebraicGeometry.relativeAssassin_subset_associatedPoints_tensor_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassin/TensorPullback.lean, line 528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassin/TensorPullback.lean#L528). The attribute's comment: “the inclusion”. References: EGA IV (3.3.1), “inclusion (3.3.1.1)”; EGA IV (3.3.6), “⊇ only, one factor =”.

> **Stacks Project, Tag 05DB, inclusion.** The associated points of the tensor
> product with a pulled-back module contain the images of the associated points
> of `F` on scheme-theoretic fibres over associated points of `G`.

```lean
theorem relativeAssassin_subset_associatedPoints_tensor_pullback
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (G : S.Modules)
    [F.IsQuasicoherent] [G.IsQuasicoherent]
    (hF : IsFlatOver f.toLRSHom.toShHom F) :
    (⋃ s ∈ Stacks.Divisors.associatedPoints G,
      f.fiberι s ''
        Stacks.Divisors.associatedPoints
          ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ⊆
    Stacks.Divisors.associatedPoints
        ((((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨((X.toLocallyRingedSpace.toRingedSpace)).presheaf,
            ((X.toLocallyRingedSpace.toRingedSpace)).IsSheaf⟩).obj (F)).obj
              (((Scheme.Modules.pullback f).obj G))))
```

**`AlgebraicGeometry.associatedPoints_tensor_pullback_eq_relativeAssassin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassin/TensorPullback.lean, line 564](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RelativeAssassin/TensorPullback.lean#L564). The attribute's comment: “equality for a locally Noetherian base”. References: EGA IV (3.3.1), “equality (Noetherian)”; EGA IV (3.3.6), “one factor = base”.

> **Stacks Project, Tag 05DB, equality.** Over a locally Noetherian base, the
> associated points of the tensor product are exactly the images of the
> associated points of `F` on fibres over associated points of `G`.

```lean
theorem associatedPoints_tensor_pullback_eq_relativeAssassin
    {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules) (G : S.Modules)
    [F.IsQuasicoherent] [G.IsQuasicoherent]
    (hF : IsFlatOver f.toLRSHom.toShHom F)
    [IsLocallyNoetherian S] :
    Stacks.Divisors.associatedPoints
        ((((Stacks.SheafOfModules.Tensor.sheafTensor
          ⟨((X.toLocallyRingedSpace.toRingedSpace)).presheaf,
            ((X.toLocallyRingedSpace.toRingedSpace)).IsSheaf⟩).obj (F)).obj
              (((Scheme.Modules.pullback f).obj G)))) =
      ⋃ s ∈ Stacks.Divisors.associatedPoints G,
        f.fiberι s ''
          Stacks.Divisors.associatedPoints
            ((Scheme.Modules.pullback (f.fiberι s)).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.3, Tag 05DA](https://stacks.math.columbia.edu/tag/05DA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
