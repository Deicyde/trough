---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_smooth_stratification_at_generic_point, AlgebraicGeometry.hasSmoothStratificationAfterFiniteLocallyFreeCover
statement: formalized
proof: formalized
---

# 37.55 Stratifying a morphism

Section 37.55 of the Stacks Project, [Tag 0H42](https://stacks.math.columbia.edu/tag/0H42). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H43, a lemma

[Tag 0H43](https://stacks.math.columbia.edu/tag/0H43) in the Stacks Project.

**`AlgebraicGeometry.exists_smooth_stratification_at_generic_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericFlatness/SmoothStratification.lean, line 1279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericFlatness/SmoothStratification.lean#L1279).

> **Stacks Project, Tag 0H43.** Smooth stratification near the generic
> point of an irreducible component of a reduced base.

```lean
theorem exists_smooth_stratification_at_generic_point
    {X S : Scheme.{u}} (f : X ⟶ S) (hf : FinitePresentation f)
    [IsReduced S] (η : S)
    (hη : ∃ C ∈ irreducibleComponents S, IsGenericPoint η C) :
    ∃ (U : S.Opens) (_ : η ∈ U) (V : Scheme.{u}) (g : V ⟶ U.toScheme),
      Function.Surjective g ∧ UniversallyInjective g ∧
        Stacks.Morphisms.IsFiniteLocallyFree g ∧
        ∃ (t : ℕ) (Z : Fin (t + 1) → Scheme.{u})
            (j : (i : Fin (t + 1)) → Z i ⟶ pullback f (g ≫ U.ι))
            (k : (i : Fin t) → Z i.succ ⟶ Z i.castSucc)
            (W : (i : Fin t) → (Z i.castSucc).Opens),
          (∀ i, IsClosedImmersion (j i)) ∧
          (∀ i, (Stacks.ClosedImmersion.idealSheaf (j i).toLRSHom.toShHom).IsFiniteType) ∧
          Stacks.Thickenings.IsThickening (j 0) ∧
          IsEmpty (Z (Fin.last t)) ∧
          (∀ i : Fin t, IsClosedImmersion (k i)) ∧
          (∀ i : Fin t, k i ≫ j i.castSucc = j i.succ) ∧
          (∀ (i : Fin t) (x : Z i.castSucc),
            x ∈ W i ↔ j i.castSucc x ∉ Set.range (j i.succ)) ∧
          (∀ i : Fin t, Smooth ((W i).ι ≫ j i.castSucc ≫
            pullback.snd f (g ≫ U.ι)))
```

## Tag 0H44, a lemma

[Tag 0H44](https://stacks.math.columbia.edu/tag/0H44) in the Stacks Project.

**`AlgebraicGeometry.hasSmoothStratificationAfterFiniteLocallyFreeCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GenericFlatness/SmoothStratificationQcqs.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GenericFlatness/SmoothStratificationQcqs.lean#L359).

> **Stacks Project, Tag 0H44.** Let `f : X ⟶ S` be a morphism of finite presentation between
> quasi-compact and quasi-separated schemes. Then there are a `t ≥ 0` and closed subschemes
> `S ⊇ S₀ ⊇ S₁ ⊇ ⋯ ⊇ S_t = ∅` such that each `S_i → S` is defined by a finite type ideal sheaf,
> `S₀ ⊆ S` is a thickening, each stratum `S_i ∖ S_{i+1}` carries a surjective finite locally free
> morphism `T_i → S_i ∖ S_{i+1}`, and `X ×_S T_i` carries closed subschemes
> `X ×_S T_i ⊇ Z_{i,0} ⊇ ⋯ ⊇ Z_{i,t_i} = ∅`, each defined by a finite type ideal sheaf, with
> `Z_{i,0} ⊆ X ×_S T_i` a thickening and each `Z_{i,j} ∖ Z_{i,j+1} → T_i` smooth.

```lean
theorem hasSmoothStratificationAfterFiniteLocallyFreeCover {X S : Scheme.{u}}
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace S] [QuasiSeparatedSpace S]
    (f : X ⟶ S) (hf : FinitePresentation f) :
    HasSmoothStratificationAfterFiniteLocallyFreeCover f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.55, Tag 0H42](https://stacks.math.columbia.edu/tag/0H42)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
