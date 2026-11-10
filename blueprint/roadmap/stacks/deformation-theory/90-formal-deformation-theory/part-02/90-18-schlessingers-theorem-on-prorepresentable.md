---
declaration: section
origin: cited
lean: Deformation.isIso_of_isSmooth_of_tangent_bijective, Deformation.isProrepresentable_iff_isDeformationFunctor
statement: formalized
proof: formalized
---

# 90.18 Schlessinger's theorem on prorepresentable functors

Section 90.18 of the Stacks Project, [Tag 06JK](https://stacks.math.columbia.edu/tag/06JK). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06JL, a lemma

[Tag 06JL](https://stacks.math.columbia.edu/tag/06JL) in the Stacks Project.

**`Deformation.isIso_of_isSmooth_of_tangent_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Smoothness/TangentIsomorphism.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/LiftsOfObjects/Smoothness/TangentIsomorphism.lean#L410).

> **Stacks Project, Tag 06JL.** A smooth morphism of deformation functors whose differential
> is bijective is an isomorphism.

```lean
public theorem isIso_of_isSmooth_of_tangent_bijective
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F G : ArtinianLocalAlgCat.{u, w, w} Λ k ⥤ Type t}
    (hF : IsDeformationFunctor F)
    (hG : IsDeformationFunctor G)
    (φ : F ⟶ G)
    (hφ : IsSmooth (elementsBasedFunctor φ))
    (hdφ : Function.Bijective
      (φ.app (augmentedDualNumbers (Λ := Λ) (k := k)))) :
    IsIso φ
```

## Tag 06JM, a theorem

[Tag 06JM](https://stacks.math.columbia.edu/tag/06JM) in the Stacks Project.

**`Deformation.isProrepresentable_iff_isDeformationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Prorepresentable.lean, line 1216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Prorepresentable.lean#L1216). References: SGA 7 VI (2.18).

> **Schlessinger's theorem.** A set-valued functor on the category of Artinian local
> `Λ`-algebras with residue field `k` is prorepresentable exactly when it is a deformation
> functor, its tangent space is a finite-dimensional `k`-vector space, and the canonical map
> from the `Λ`-derivations of `k` to that tangent space is injective.

```lean
public theorem isProrepresentable_iff_isDeformationFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [IsNoetherianRing Λ]
    [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type (max v w)) :
    IsProrepresentable F ↔
      ∃ hF : IsDeformationFunctor F,
        let p := CategoryOfElements.π F
        let 𝓕 := BasedCategory.ofFunctor p
        let hD := (isDeformationCategory_iff F).2 hF
        let hS2 := Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory
          𝓕 hD
        letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
        letI : Fact (SchlessingerConditionS2
          (CategoryOfElements.π
            (isomorphismClasses 𝓕 hD.predeformation.cofibered))) := ⟨hS2⟩
        let T := tangentSpaceArtinian Λ k
          (isomorphismClasses 𝓕 hD.predeformation.cofibered)
        letI : AddCommGroup T := associatedTangentSpaceAddCommGroup 𝓕
        letI : Module k T := associatedTangentSpaceModule 𝓕
        FiniteDimensional k T ∧
          Function.Injective (derivationToTangentSpace p hD.predeformation)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.18, Tag 06JK](https://stacks.math.columbia.edu/tag/06JK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
