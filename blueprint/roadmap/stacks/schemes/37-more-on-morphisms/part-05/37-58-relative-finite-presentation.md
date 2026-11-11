---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsFinitelyPresentedRelative, AlgebraicGeometry.isFinitelyPresentedRelative_iff_affine, AlgebraicGeometry.isFinitelyPresentedRelative_resLE, AlgebraicGeometry.isFinitelyPresentedRelative_iff_isFinitePresentation, AlgebraicGeometry.locallyOfFinitePresentation_iff_structureSheaf_finitelyPresentedRelative, AlgebraicGeometry.isFinitelyPresentedRelative_pushforward_iff, AlgebraicGeometry.isFinitelyPresentedRelative_baseChange, AlgebraicGeometry.isFinitelyPresentedRelative_pullback
statement: formalized
proof: formalized
---

# 37.58 Relative finite presentation

Section 37.58 of the Stacks Project, [Tag 05GX](https://stacks.math.columbia.edu/tag/05GX). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05H1, a definition

[Tag 05H1](https://stacks.math.columbia.edu/tag/05H1) in the Stacks Project.

**`AlgebraicGeometry.IsFinitelyPresentedRelative`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Defs.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Defs.lean#L59).

> A sheaf of modules `M` on `X` is finitely presented relative to `S` if there is an affine
> open cover of `S` and, over each member, an affine open cover of its inverse image such that
> the corresponding module of sections of `M` is finitely presented relative to the ring of
> functions on the base open.

```lean
abbrev IsFinitelyPresentedRelative {X S : Scheme.{u}} (f : X ⟶ S) (M : X.Modules) : Prop
```

## Tag 09T7, a lemma

[Tag 09T7](https://stacks.math.columbia.edu/tag/09T7) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_iff_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Affine.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Affine.lean#L389). The attribute's comment: “affine-open characterization”.

> **Stacks Project, Tag 09T7.** A quasi-coherent module on a scheme locally of finite type
> over a base is finitely presented relative to that base if and only if its sections over every
> affine open are finitely presented relative to the sections over every compatible affine open
> of the base.

```lean
theorem isFinitelyPresentedRelative_iff_affine
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (M : X.Modules) [M.IsQuasicoherent] :
    IsFinitelyPresentedRelative f M ↔
      ∀ (U : X.Opens), IsAffineOpen U →
        ∀ (V : S.Opens), IsAffineOpen V →
          ∀ (hUV : U ≤ f ⁻¹ᵁ V),
            letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U hUV).hom.toAlgebra
            Module.FinitePresentationRel Γ(S, V) Γ(X, U) Γ(M, U)
```

**`AlgebraicGeometry.isFinitelyPresentedRelative_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Affine.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Affine.lean#L438). The attribute's comment: “restriction to open subschemes”.

> **Stacks Project, Tag 09T7.** Once a quasi-coherent module is finitely presented relative
> to a base, its restriction to any open subscheme is finitely presented relative to every
> compatible open subscheme of the base.

```lean
theorem isFinitelyPresentedRelative_resLE
    {X S : Scheme.{u}} {f : X ⟶ S} [LocallyOfFiniteType f]
    (M : X.Modules) [M.IsQuasicoherent]
    (hM : IsFinitelyPresentedRelative f M)
    (U : X.Opens) (V : S.Opens) (hUV : U ≤ f ⁻¹ᵁ V) :
    IsFinitelyPresentedRelative (f.resLE V U hUV) (M.restrict U.ι)
```

## Tag 09T8, a lemma

[Tag 09T8](https://stacks.math.columbia.edu/tag/09T8) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_iff_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/FinitePresentation.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/FinitePresentation.lean#L163). The attribute's comment: “relative\_iff\_finite\_presentation”.

> **Stacks Project, Tag 09T8.** For a locally finitely presented morphism of schemes, a
> quasi-coherent sheaf of modules is finitely presented relative to the base if and only if it is
> finitely presented.

```lean
theorem isFinitelyPresentedRelative_iff_isFinitePresentation
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (M : X.Modules) [M.IsQuasicoherent] :
    IsFinitelyPresentedRelative f M ↔ M.IsFinitePresentation
```

**`AlgebraicGeometry.locallyOfFinitePresentation_iff_structureSheaf_finitelyPresentedRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/StructureSheaf.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/StructureSheaf.lean#L79). The attribute's comment: “morphism\_iff\_structure\_sheaf\_relative”.

> **Stacks Project, Tag 09T8.** A locally finite type morphism is locally of finite
> presentation if and only if its structure sheaf is finitely presented relative to the base.

```lean
theorem locallyOfFinitePresentation_iff_structureSheaf_finitelyPresentedRelative
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] :
    LocallyOfFinitePresentation f ↔
      IsFinitelyPresentedRelative f (SheafOfModules.unit X.ringCatSheaf)
```

## Tag 09T9, a lemma

[Tag 09T9](https://stacks.math.columbia.edu/tag/09T9) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_pushforward_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeFinitePresentation/FinitePushforward.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeFinitePresentation/FinitePushforward.lean#L81).

> **Stacks Project, Tag 09T9.** A quasi-coherent module on the source of a finite morphism
> between schemes locally of finite type over a base is finitely presented relative to that base
> if and only if its pushforward is.

```lean
theorem isFinitelyPresentedRelative_pushforward_iff
    {X Y S : Scheme.{u}} (π : X ⟶ Y) (f : X ⟶ S) (g : Y ⟶ S)
    (hπ : π ≫ g = f) [IsFinite π] [LocallyOfFiniteType f]
    [LocallyOfFiniteType g] (M : X.Modules) [M.IsQuasicoherent] :
    IsFinitelyPresentedRelative g ((Scheme.Modules.pushforward π).obj M) ↔
      IsFinitelyPresentedRelative f M
```

## Tag 09TA, a lemma

[Tag 09TA](https://stacks.math.columbia.edu/tag/09TA) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeFinitePresentation/BaseChange.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeFinitePresentation/BaseChange.lean#L215).

> **Stacks Project, Tag 09TA.** Relative finite presentation of a quasi-coherent module is
> stable under arbitrary base change: if `M` on `X` is finitely presented relative to `f : X ⟶ S`,
> then its pullback to `X ×_S S'` is finitely presented relative to `S'`.

```lean
theorem isFinitelyPresentedRelative_baseChange
    {X S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    [LocallyOfFiniteType f] (M : X.Modules) [M.IsQuasicoherent]
    (hM : IsFinitelyPresentedRelative f M) :
    IsFinitelyPresentedRelative (pullback.snd f g)
      ((Scheme.Modules.pullback (pullback.fst f g)).obj M)
```

## Tag 09TB, a lemma

[Tag 09TB](https://stacks.math.columbia.edu/tag/09TB) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeFinitePresentation/Pullback.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeFinitePresentation/Pullback.lean#L150).

> **Stacks Project, Tag 09TB.** Relative finite presentation of a quasi-coherent module is
> preserved by pullback along a morphism locally of finite presentation.

```lean
theorem isFinitelyPresentedRelative_pullback
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [LocallyOfFiniteType g]
    [LocallyOfFinitePresentation f]
    (G : Y.Modules) [G.IsQuasicoherent]
    (hG : IsFinitelyPresentedRelative g G) :
    IsFinitelyPresentedRelative (f ≫ g) ((Scheme.Modules.pullback f).obj G)
```

## Tag 09TC, a lemma

[Tag 09TC](https://stacks.math.columbia.edu/tag/09TC) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean#L67).

> **Stacks Project, Tag 09TC.** Relative finite presentation of a quasi-coherent
> module passes through a locally finitely presented intermediate scheme.

```lean
theorem isFinitelyPresentedRelative_comp {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ S) [LocallyOfFiniteType f]
    [LocallyOfFiniteType g] [LocallyOfFinitePresentation g]
    (M : X.Modules) [M.IsQuasicoherent]
    (hM : IsFinitelyPresentedRelative f M) :
    IsFinitelyPresentedRelative (f ≫ g) M
```

## Tag 09TD, a lemma

[Tag 09TD](https://stacks.math.columbia.edu/tag/09TD) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean#L170). The attribute's comment: “extension”.

> In a short exact sequence of quasi-coherent modules over a locally finite type
> morphism, relative finite presentation of the two end terms implies that of the middle
> term.

```lean
theorem isFinitelyPresentedRelative_of_shortExact
    (s : RelativeFinitePresentationExactSequenceSituation.{u})
    (hleft : IsFinitelyPresentedRelative s.f s.sequence.X₁)
    (hright : IsFinitelyPresentedRelative s.f s.sequence.X₃) :
    IsFinitelyPresentedRelative s.f s.sequence.X₂
```

**`AlgebraicGeometry.isFinitelyPresentedRelative_of_shortExact_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean#L190). The attribute's comment: “quotient”.

> In a short exact sequence of quasi-coherent modules over a locally finite type
> morphism whose left-hand term is of finite type, relative finite presentation of the middle
> term implies that of the right-hand term.

```lean
theorem isFinitelyPresentedRelative_of_shortExact_of_isFiniteType
    (s : RelativeFinitePresentationExactSequenceSituation.{u})
    (hleft : s.sequence.X₁.IsFiniteType)
    (hmid : IsFinitelyPresentedRelative s.f s.sequence.X₂) :
    IsFinitelyPresentedRelative s.f s.sequence.X₃
```

## Tag 09TE, a lemma

[Tag 09TE](https://stacks.math.columbia.edu/tag/09TE) in the Stacks Project.

**`AlgebraicGeometry.isFinitelyPresentedRelative_left_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean#L310). The attribute's comment: “first summand”.

> **Stacks Project, Tag 09TE.** The first summand of a relatively finitely presented direct
> sum is relatively finitely presented.

```lean
theorem isFinitelyPresentedRelative_left_of_biprod
    {X S : Scheme.{u}} (f : X ⟶ S) (M N : X.Modules)
    (h : IsFinitelyPresentedRelative f (M ⊞ N)) :
    IsFinitelyPresentedRelative f M
```

**`AlgebraicGeometry.isFinitelyPresentedRelative_right_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/RelativeFinitePresentation/Operations.lean#L318). The attribute's comment: “second summand”.

> **Stacks Project, Tag 09TE.** The second summand of a relatively finitely presented direct
> sum is relatively finitely presented.

```lean
theorem isFinitelyPresentedRelative_right_of_biprod
    {X S : Scheme.{u}} (f : X ⟶ S) (M N : X.Modules)
    (h : IsFinitelyPresentedRelative f (M ⊞ N)) :
    IsFinitelyPresentedRelative f N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.58, Tag 05GX](https://stacks.math.columbia.edu/tag/05GX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
