---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.essSurj_baseChangeFunctor, AlgebraicGeometry.Space.isEquivalence_baseChangeFunctor, AlgebraicGeometry.Space.faithful_baseChangeFunctor, AlgebraicGeometry.Space.full_baseChangeFunctor, AlgebraicGeometry.Space.fullyFaithful_baseChangeFunctor, AlgebraicGeometry.Space.baseChangeFunctor, AlgebraicGeometry.Space.isQuasiCompact_iff_baseChangeFunctor_obj, AlgebraicGeometry.Space.isQuasiSeparated_iff_baseChangeFunctor_obj
statement: formalized
proof: formalized
---

# 70.19 Application to modifications

Section 70.19 of the Stacks Project, [Tag 0BGX](https://stacks.math.columbia.edu/tag/0BGX). 3 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BGY, a lemma

[Tag 0BGY](https://stacks.math.columbia.edu/tag/0BGY) in the Stacks Project.

**`AlgebraicGeometry.Space.essSurj_baseChangeFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionEquivalence.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionEquivalence.lean#L138). The attribute's comment: “the base-change functor is essentially surjective”.

> **Stacks 0BGY, essential surjectivity of the base-change functor.** Let `f : V ⟶ W` be a
> separated étale morphism of algebraic spaces over `S` and let `T` be a closed subspace of `W`
> whose preimage is carried isomorphically onto `T`. Then every modification of `V` outside
> `f⁻¹W⁰` is isomorphic to the base change of a modification of `W` outside `W⁰`, namely of the
> dependent product `Π_f Y`, the isomorphism being the counit.

```lean
theorem essSurj_baseChangeFunctor (f : V ⟶ W) (T : Subfunctor W.obj)
    (hT : IsClosedSubspace B S hS T) (hfT : IsIso (T.fromPreimage f.hom))
    (hf : IsEtale B S hS f.hom) (hsep : IsSeparated B S hS f.hom) :
    (baseChangeFunctor B S hS f (openComplement B S hS T)).1.EssSurj
```

**`AlgebraicGeometry.Space.isEquivalence_baseChangeFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionEquivalence.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionEquivalence.lean#L159). The attribute's comment: “equivalence of categories”.

> **Stacks 0BGY.** Let `f : V ⟶ W` be a separated étale morphism of algebraic spaces over a
> scheme `S` and let `T ⊂ W` be a closed subspace such that `f⁻¹T → T` is an isomorphism. Write
> `W⁰` for the complement of `T` and `V⁰ = f⁻¹W⁰`. Then base change along `f` is an equivalence
> from the category of morphisms `g : X ⟶ W` of algebraic spaces with `g⁻¹W⁰ → W⁰` an
> isomorphism to the category of morphisms `h : Y ⟶ V` of algebraic spaces with `h⁻¹V⁰ → V⁰` an
> isomorphism.
>
> Faithfulness is `AlgebraicGeometry.Space.faithful_baseChangeFunctor`, fullness is
> `AlgebraicGeometry.Space.full_baseChangeFunctor` and essential surjectivity is
> `AlgebraicGeometry.Space.essSurj_baseChangeFunctor`.

```lean
theorem isEquivalence_baseChangeFunctor (f : V ⟶ W) (T : Subfunctor W.obj)
    (hT : IsClosedSubspace B S hS T) (hfT : IsIso (T.fromPreimage f.hom))
    (hf : IsEtale B S hS f.hom) (hsep : IsSeparated B S hS f.hom) :
    (baseChangeFunctor B S hS f (openComplement B S hS T)).1.IsEquivalence
```

**`AlgebraicGeometry.Space.faithful_baseChangeFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionFaithful.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionFaithful.lean#L199). The attribute's comment: “the base-change functor is faithful”.

> **Stacks 0BGY, faithfulness of the base-change functor.** Let `f : V ⟶ W` be an étale
> morphism of algebraic spaces over `S` and let `T` be a closed subspace of `W` whose preimage
> is carried isomorphically onto `T`. Then the functor of Stacks 0BGY, base change along `f`
> from the modifications of `W` outside the open complement `W⁰` of `T` to the modifications of
> `V` outside `f⁻¹W⁰`, is faithful.
>
> Two morphisms of modifications which agree after base change agree on `X ×_W V`, and they
> agree over `W⁰` because the target is an isomorphism there; those two parts cover the source
> locally, which is a sheaf, so the morphisms are equal.

```lean
theorem faithful_baseChangeFunctor (f : V ⟶ W) (T : Subfunctor W.obj)
    (hT : IsClosedSubspace B S hS T) (hfT : IsIso (T.fromPreimage f.hom))
    (hf : IsEtale B S hS f.hom) :
    (baseChangeFunctor B S hS f (openComplement B S hS T)).1.Faithful
```

**`AlgebraicGeometry.Space.full_baseChangeFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionFull.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionFull.lean#L315). The attribute's comment: “the base-change functor is full”.

> **Stacks 0BGY, fullness of the base-change functor.** Let `f : V ⟶ W` be a separated étale
> morphism of algebraic spaces over `S` and let `T` be a closed subspace of `W` whose preimage is
> carried isomorphically onto `T`. Then the functor of Stacks 0BGY, base change along `f` from the
> modifications of `W` outside the open complement `W⁰` of `T` to the modifications of `V` outside
> `f⁻¹W⁰`, is full.

```lean
theorem full_baseChangeFunctor (f : V ⟶ W') (T : Subfunctor W'.obj)
    (hT : IsClosedSubspace B S hS T) (hfT : IsIso (T.fromPreimage f.hom))
    (hf : IsEtale B S hS f.hom) (hsep : IsSeparated B S hS f.hom) :
    (baseChangeFunctor B S hS f (openComplement B S hS T)).1.Full
```

**`AlgebraicGeometry.Space.fullyFaithful_baseChangeFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionFull.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionFull.lean#L326). The attribute's comment: “the base-change functor is fully faithful”.

> **Stacks 0BGY, full faithfulness of the base-change functor.**

```lean
noncomputable def fullyFaithful_baseChangeFunctor (f : V ⟶ W') (T : Subfunctor W'.obj)
    (hT : IsClosedSubspace B S hS T) (hfT : IsIso (T.fromPreimage f.hom))
    (hf : IsEtale B S hS f.hom) (hsep : IsSeparated B S hS f.hom) :
    (baseChangeFunctor B S hS f (openComplement B S hS T)).1.FullyFaithful
```

**`AlgebraicGeometry.Space.baseChangeFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean#L198). The attribute's comment: “the base-change functor”.

> **Stacks 0BGY.** Pullback of modifications, canonically identified with pullback of
> their underlying presheaves over the base.

```lean
noncomputable def baseChangeFunctor {V W : AlgebraicSpaces B S hS}
    (f : V ⟶ W) (W₀ : Subfunctor W.obj) :
    Σ F : Modification B S hS W₀ ⥤ Modification B S hS (W₀.preimage f.hom),
      F ⋙ ObjectProperty.ι (IsModification B S hS (W₀.preimage f.hom)) ≅
        ObjectProperty.ι (IsModification B S hS W₀) ⋙ Over.pullback f.hom
```

## Tag 0BGZ, a lemma

[Tag 0BGZ](https://stacks.math.columbia.edu/tag/0BGZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L207). The attribute's comment: “quasi-compactness”.

> A modification of `W` outside the complement of `T` is
> quasi-compact exactly when its base change to `V` is.

```lean
theorem isQuasiCompact_iff_baseChangeFunctor_obj :
    IsQuasiCompact B S hS g.obj.hom ↔
      IsQuasiCompact B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isQuasiSeparated_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L229). The attribute's comment: “quasi-separatedness”.

> A modification of `W` outside the complement of `T`
> is quasi-separated exactly when its base change to `V` is.

```lean
theorem isQuasiSeparated_iff_baseChangeFunctor_obj :
    IsQuasiSeparated B S hS g.obj.hom ↔
      IsQuasiSeparated B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isSeparated_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L252). The attribute's comment: “separatedness”.

> A modification of `W` outside the complement of `T` is
> separated exactly when its base change to `V` is.

```lean
theorem isSeparated_iff_baseChangeFunctor_obj :
    IsSeparated B S hS g.obj.hom ↔
      IsSeparated B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L279). The attribute's comment: “local finite presentation”.

> A modification of `W` outside the complement of
> `T` is locally of finite presentation exactly when its base change to `V` is.

```lean
theorem isLocallyOfFinitePresentation_iff_baseChangeFunctor_obj :
    IsLocallyOfFinitePresentation B S hS g.obj.hom ↔
      IsLocallyOfFinitePresentation B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L309). The attribute's comment: “local finite type”.

> A modification of `W` outside the complement of `T` is
> locally of finite type exactly when its base change to `V` is.

```lean
theorem isLocallyOfFiniteType_iff_baseChangeFunctor_obj :
    IsLocallyOfFiniteType B S hS g.obj.hom ↔
      IsLocallyOfFiniteType B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isFiniteType_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L341). The attribute's comment: “finite type”.

> A modification of `W` outside the complement of `T` is of
> finite type exactly when its base change to `V` is.

```lean
theorem isFiniteType_iff_baseChangeFunctor_obj :
    IsFiniteType B S hS g.obj.hom ↔
      IsFiniteType B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isFinitePresentation_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L352). The attribute's comment: “finite presentation”.

> A modification of `W` outside the complement of `T`
> is of finite presentation exactly when its base change to `V` is.

```lean
theorem isFinitePresentation_iff_baseChangeFunctor_obj :
    IsFinitePresentation B S hS g.obj.hom ↔
      IsFinitePresentation B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isProper_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L365). The attribute's comment: “properness”.

> A modification of `W` outside the complement of `T` is proper
> exactly when its base change to `V` is.

```lean
theorem isProper_iff_baseChangeFunctor_obj :
    IsProper B S hS g.obj.hom ↔
      IsProper B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isIntegralHom_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L387). The attribute's comment: “integrality”.

> A modification of `W` outside the complement of `T` is
> integral exactly when its base change to `V` is.

```lean
theorem isIntegralHom_iff_baseChangeFunctor_obj :
    IsIntegralHom B S hS g.obj.hom ↔
      IsIntegralHom B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

**`AlgebraicGeometry.Space.isFinite_iff_baseChangeFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionProperties.lean#L405). The attribute's comment: “finiteness”.

> A modification of `W` outside the complement of `T` is finite
> exactly when its base change to `V` is.

```lean
theorem isFinite_iff_baseChangeFunctor_obj :
    IsFinite B S hS g.obj.hom ↔
      IsFinite B S hS
        ((baseChangeFunctor B S hS f (openComplement B S hS T)).1.obj g).obj.hom
```

## Tag 0BH0, a lemma

[Tag 0BH0](https://stacks.math.columbia.edu/tag/0BH0) in the Stacks Project.

**`AlgebraicGeometry.Space.ClosedPointNeighborhood.isEquivalence_henselianBaseChangeFunctor_of_isHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsHenselianLocalRingEquivalence.lean, line 957](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsHenselianLocalRingEquivalence.lean#L957).

> **Stacks 0BH0.** Let `X` be a decent algebraic space over `S` and `x ∈ |X|` a closed point
> such that `U = X ∖ {x} ⟶ X` is quasi-compact; let `(W, w) → (X, x)` be an affine elementary étale
> neighbourhood with `w` the only point above `x` (Stacks 0BBP) and let `R` be a henselization of
> `𝒪_{W, w}`, so that `R = 𝒪^h_{X, x}` (Stacks 0EMY). With `V = Spec(𝒪^h_{X, x}) ∖ {𝔪^h_x}`, the base
> change functor from the morphisms `f : Y ⟶ X` of finite presentation with `f⁻¹(U) ⟶ U` an
> isomorphism to the morphisms `g : Y ⟶ Spec(𝒪^h_{X, x})` of finite presentation with
> `g⁻¹(V) ⟶ V` an isomorphism is an equivalence of categories.

```lean
theorem isEquivalence_henselianBaseChangeFunctor_of_isHenselization :
    (D.henselianBaseChangeFunctor R (D.contains_spec_of_isHenselization R)).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.19, Tag 0BGX](https://stacks.math.columbia.edu/tag/0BGX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
