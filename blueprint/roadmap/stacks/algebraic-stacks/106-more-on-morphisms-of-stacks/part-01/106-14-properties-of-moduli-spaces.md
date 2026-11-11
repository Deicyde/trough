---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isLocallyOfFiniteType_of_isCategoricalModuliSpace_of_isFinite_inertia, AlgebraicGeometry.Stack.isAbsolutelyQuasiSeparated_and_isAbsolutelySeparated_of_isFinite_inertia, AlgebraicGeometry.Stack.isAbsolutelyQuasiSeparated_and_isAbsolutelySeparated_of_universalHomeomorphism, AlgebraicGeometry.Stack.isProper_of_isCategoricalModuliSpace_of_isFinite_inertia
statement: formalized
proof: formalized
---

# 106.14 Properties of moduli spaces

Section 106.14 of the Stacks Project, [Tag 0DUW](https://stacks.math.columbia.edu/tag/0DUW). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DUX, a lemma

[Tag 0DUX](https://stacks.math.columbia.edu/tag/0DUX) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyOfFiniteType_of_isCategoricalModuliSpace_of_isFinite_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/KeelMori/ModuliFiniteType.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/KeelMori/ModuliFiniteType.lean#L54).

> **Stacks 0DUX.** Let `p : 𝒳 ⟶ Y` be a 1-morphism from an algebraic stack to an algebraic
> space such that the inertia `I_𝒳 ⟶ 𝒳` is finite, `Y` is locally Noetherian and `p` is locally
> of finite type, and let `f : 𝒳 ⟶ M` be a categorical moduli space (for instance the moduli
> space of Stacks 0DUT). Then `p` factors as `f` followed by a unique morphism `M ⟶ Y`, up to a
> 2-isomorphism, and that morphism `M ⟶ Y` is locally of finite type.

```lean
theorem isLocallyOfFiniteType_of_isCategoricalModuliSpace_of_isFinite_inertia
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hI : AlgebraicStacks.IsFinite B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (Y : AlgebraicSpaces B S hS)
    (hY : Space.HasEtaleLocalProperty B S hS Y.obj (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (p : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS Y.obj Y.property)
    (hp : AlgebraicStacks.IsLocallyOfFiniteType B S hS p)
    (M : AlgebraicSpaces B S hS) (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M.obj M.property)
    (hf : IsCategoricalModuliSpace B S hS M f.hom) :
    (∃! q : M ⟶ Y, Nonempty (f.hom ≫ (associatedMap B S hS q.hom).1 ≅ p.hom)) ∧
      ∀ q : M ⟶ Y, Nonempty (f.hom ≫ (associatedMap B S hS q.hom).1 ≅ p.hom) →
        Space.IsLocallyOfFiniteType B S hS q.hom
```

## Tag 0DUY, a lemma

[Tag 0DUY](https://stacks.math.columbia.edu/tag/0DUY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiSeparated_and_isAbsolutelySeparated_of_isFinite_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliSeparation/KeelMoriModuliSpaceSeparation.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliSeparation/KeelMoriModuliSpaceSeparation.lean#L77).

> **Stacks 0DUY.** Let `𝒳` be an algebraic stack whose inertia `I_𝒳 ⟶ 𝒳` is finite, and let
> `f : 𝒳 ⟶ M` be a categorical moduli space — for instance the moduli space constructed in
> Stacks 0DUT, which every categorical moduli space of `𝒳` is up to unique isomorphism. Then
> 1. if `𝒳` is quasi-separated, then `M` is quasi-separated;
> 2. if `𝒳` is separated, then `M` is separated.
>
> Both properties are absolute, over the terminal scheme `Spec ℤ` (Stacks 050D parts (8), (7) and
> Stacks 03BS parts (3), (1)). Part (3) of the source ("Add more here") asserts nothing.

```lean
theorem isAbsolutelyQuasiSeparated_and_isAbsolutelySeparated_of_isFinite_inertia
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hI : AlgebraicStacks.IsFinite B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (M : AlgebraicSpaces B S hS) (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M.obj M.property)
    (hf : IsCategoricalModuliSpace B S hS M f.hom) :
    (AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳 →
        Space.IsAbsolutelyQuasiSeparated B S hS hZ M.obj) ∧
      (AlgebraicStacks.IsAbsolutelySeparated.{u, w} B S hS hZ 𝒳 →
        Space.IsAbsolutelySeparated B S hS hZ M.obj)
```

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiSeparated_and_isAbsolutelySeparated_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliSeparation/ModuliSpaceSeparation.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliSeparation/ModuliSpaceSeparation.lean#L148).

> **Stacks 0DUY.** Let `f : 𝒳 ⟶ M` be a universal homeomorphism (Stacks 0CI7) from an algebraic
> stack over `S` to an algebraic space over `S` — for instance the moduli space of the Keel–Mori
> theorem (Stacks 0DUT) of an algebraic stack with finite inertia, which is a universal
> homeomorphism. Then
> 1. if `𝒳` is quasi-separated, then `M` is quasi-separated;
> 2. if `𝒳` is separated, then `M` is separated.
>
> Both properties are absolute (Stacks 050D parts (7), (8) and Stacks 03BS parts (1), (3)). Part (3)
> of the source ("Add more here") asserts nothing.

```lean
theorem isAbsolutelyQuasiSeparated_and_isAbsolutelySeparated_of_universalHomeomorphism
    {𝒳 : AlgebraicStacks.{u, w} B S hS} {M : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hM : IsAlgebraicSpace B S hS M) (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M hM)
    (hf : AlgebraicStacks.UniversalHomeomorphism B S hS f) :
    (AlgebraicStacks.IsAbsolutelyQuasiSeparated.{u, w} B S hS hZ 𝒳 →
        Space.IsAbsolutelyQuasiSeparated B S hS hZ M) ∧
      (AlgebraicStacks.IsAbsolutelySeparated.{u, w} B S hS hZ 𝒳 →
        Space.IsAbsolutelySeparated B S hS hZ M)
```

## Tag 0DUZ, a lemma

[Tag 0DUZ](https://stacks.math.columbia.edu/tag/0DUZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isProper_of_isCategoricalModuliSpace_of_isFinite_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuliProperness/ModuliSpaceProper.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuliProperness/ModuliSpaceProper.lean#L74).

> **Stacks 0DUZ.** Let `p : 𝒳 ⟶ Y` be a 1-morphism from an algebraic stack to an algebraic
> space. Assume
> 1. `I_𝒳 ⟶ 𝒳` is finite,
> 2. `p` is proper, and
> 3. `Y` is locally Noetherian.
>
> Let `f : 𝒳 ⟶ M` be a categorical moduli space — for instance the moduli space constructed in
> Stacks 0DUT, which every categorical moduli space of `𝒳` is up to unique isomorphism. Then `p`
> factors as `f` followed by a unique morphism `M ⟶ Y` of algebraic spaces, up to a 2-isomorphism,
> and `M ⟶ Y` is proper.

```lean
theorem isProper_of_isCategoricalModuliSpace_of_isFinite_inertia
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hI : AlgebraicStacks.IsFinite B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (Y : AlgebraicSpaces B S hS)
    (hY : Space.HasEtaleLocalProperty B S hS Y.obj (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (p : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS Y.obj Y.property)
    (hp : AlgebraicStacks.IsProper B S hS p)
    (M : AlgebraicSpaces B S hS) (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M.obj M.property)
    (hf : IsCategoricalModuliSpace B S hS M f.hom) :
    (∃! g : M ⟶ Y, Nonempty (f.hom ≫ (associatedMap B S hS g.hom).1 ≅ p.hom)) ∧
      ∀ g : M ⟶ Y, Nonempty (f.hom ≫ (associatedMap B S hS g.hom).1 ≅ p.hom) →
        Space.IsProper B S hS g.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.14, Tag 0DUW](https://stacks.math.columbia.edu/tag/0DUW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
