---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.morToModificationCompletion_injective, AlgebraicGeometry.Space.morToModificationCompletion_codRestrict_bijective
statement: formalized
proof: formalized
---

# 88.26 Rig glueing of morphisms

Section 88.26 of the Stacks Project, [Tag 0GI2](https://stacks.math.columbia.edu/tag/0GI2). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GI3, a proposition

[Tag 0GI3](https://stacks.math.columbia.edu/tag/0GI3) in the Stacks Project.

**`AlgebraicGeometry.Space.morToModificationCompletion_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsFromProperModification.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsFromProperModification.lean#L214). The attribute's comment: “injectivity of the comparison map”.

> **Stacks 0GI3**, injectivity. Let `X` be a locally Noetherian algebraic space over `S`, let
> `T ⊆ |X|` be a closed subset with complementary open subspace `U ⊆ X`, and let `f : X' ⟶ X` be a
> proper morphism of algebraic spaces whose base change `f⁻¹(U) ⟶ U` is an isomorphism. For every
> algebraic space `W` over `S` a morphism `X ⟶ W` is determined by its restriction to `X'`
> together with the morphism `X_{/T} ⟶ W` it induces.

```lean
theorem morToModificationCompletion_injective
    {X' X W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (_hX' : IsAlgebraicSpace B S hS X')
    (hW : IsAlgebraicSpace B S hS W)
    (hXnoeth : HasEtaleLocalProperty B S hS X (fun V : Scheme.{u} => IsLocallyNoetherian V))
    {T : Set (points B S hS X)} (hT : IsClosed T)
    (f : X' ⟶ X) (_hfproper : IsProper B S hS f)
    (hfU : IsIso (pullback.snd f (openSubspaceOfPoints B S hS X Tᶜ).ι)) :
    Function.Injective (morToModificationCompletion B S hS f T W)
```

**`AlgebraicGeometry.Space.morToModificationCompletion_codRestrict_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsFromProperModificationExistence.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/MorphismsFromProperModificationExistence.lean#L173).

> **Stacks 0GI3.** Let `S` be a scheme, `X` a locally Noetherian algebraic space over `S`,
> `T ⊆ |X|` a closed subset with complementary open subspace `U ⊆ X`, and `f : X' ⟶ X` a proper
> morphism of algebraic spaces such that `f⁻¹(U) ⟶ U` is an isomorphism. For any algebraic space
> `W` over `S` the map
> `Mor_S(X, W) ⟶ Mor_S(X', W) ×_{Mor_S(X'_{/T}, W)} Mor_S(X_{/T}, W)`, sending `w` to its
> restriction to `X'` and the morphism it induces on the completion `X_{/T}`, is bijective.

```lean
theorem morToModificationCompletion_codRestrict_bijective
    {X' X W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hX' : IsAlgebraicSpace B S hS X')
    (hW : IsAlgebraicSpace B S hS W)
    (hXnoeth : HasEtaleLocalProperty B S hS X (fun V : Scheme.{u} => IsLocallyNoetherian V))
    {T : Set (points B S hS X)} (hT : IsClosed T)
    (f : X' ⟶ X) (hfproper : IsProper B S hS f)
    (hfU : IsIso (pullback.snd f (openSubspaceOfPoints B S hS X Tᶜ).ι)) :
    Function.Bijective (Set.codRestrict (morToModificationCompletion B S hS f T W)
      {p | completionMap B S hS f T ≫ p.2 =
        (completionSubfunctor B S hS X' (pointsMap B S hS X' f ⁻¹' T)).ι ≫
          Functor.whiskerRight p.1 uliftFunctor.{u + 1}}
      (morToModificationCompletion_compatible B S hS f T W))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.26, Tag 0GI2](https://stacks.math.columbia.edu/tag/0GI2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
