---
declaration: section
origin: cited
lean: Stacks.RelativeAssassin.exists_open_closure_genericPoints_fibre_mem_relativeAssassin, Stacks.RelativeAssassin.exists_open_forall_not_associatedPoints_fibre_subset, Stacks.Divisors.exists_open_associatedPoints_fiber_subset, Stacks.RelativeAssassin.associatedPoints_fiber_subset_preimage_iff_baseChange, Stacks.RelativeAssassin.isLocallyConstructible_fibrewiseContainment
statement: formalized
proof: formalized
---

# 37.25 Relative assassins

Section 37.25 of the Stacks Project, [Tag 05KM](https://stacks.math.columbia.edu/tag/05KM). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05F1, a lemma

[Tag 05F1](https://stacks.math.columbia.edu/tag/05F1) in the Stacks Project.

**`Stacks.RelativeAssassin.exists_open_closure_genericPoints_fibre_mem_relativeAssassin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/GenericFibrePoints.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/GenericFibrePoints.lean#L315).

> **Stacks Project, Tag 05F1.** Let `f : X ⟶ S` be locally of finite type, let `F` be a
> quasi-coherent `𝒪_X`-module of finite type and let `ξ` be a point of `Ass_{X/S}(F)`. There is a
> nonempty open `V` of the closure of `ξ` such that for every `s` in the image of `V` the generic
> points of the fibre `V_s` lie in `Ass_{X/S}(F)`.

```lean
public theorem exists_open_closure_genericPoints_fibre_mem_relativeAssassin
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (ξ : X) (hξ : ξ ∈ Stacks.Divisors.relativeAssassin f F) :
    ∃ V : Set (closure ({ξ} : Set X)), IsOpen V ∧ V.Nonempty ∧
      ∀ s ∈ f '' (Subtype.val '' V),
        ∀ η : genericPoints ((f.fiberι s) ⁻¹' (Subtype.val '' V) : Set (f.fiber s)),
          f.fiberι s η.1.1 ∈ Stacks.Divisors.relativeAssassin f F
```

## Tag 05KN, a lemma

[Tag 05KN](https://stacks.math.columbia.edu/tag/05KN) in the Stacks Project.

**`Stacks.RelativeAssassin.exists_open_forall_not_associatedPoints_fibre_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/GenericFibrePoints.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/GenericFibrePoints.lean#L425). References: EGA IV (1.8.6), “second assertion”.

> **Stacks Project, Tag 05KN.** Let `f : X ⟶ Y` be a finite type morphism, `F` a
> quasi-coherent `𝒪_X`-module of finite type and `U ⊆ X` open, and let `Y` be irreducible with
> generic point `η`. If the associated points of `F` on the fibre over `η` are not all contained
> in `U`, then the same failure of containment holds on the fibre over every point of some
> nonempty open of `Y`.

```lean
public theorem exists_open_forall_not_associatedPoints_fibre_subset {X Y : Scheme.{u}}
    (f : X ⟶ Y) [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (U : X.Opens)
    [IrreducibleSpace Y] (η : Y) (hη : IsGenericPoint η Set.univ)
    (hηU : ¬ Stacks.Divisors.associatedPoints
        ((Scheme.Modules.pullback (f.fiberι η)).obj F) ⊆ f.fiberι η ⁻¹' (U : Set X)) :
    ∃ V : Y.Opens, (V : Set Y).Nonempty ∧ ∀ y ∈ V,
      ¬ Stacks.Divisors.associatedPoints
        ((Scheme.Modules.pullback (f.fiberι y)).obj F) ⊆ f.fiberι y ⁻¹' (U : Set X)
```

## Tag 05KP, a lemma

[Tag 05KP](https://stacks.math.columbia.edu/tag/05KP) in the Stacks Project.

**`Stacks.Divisors.exists_open_associatedPoints_fiber_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FibrewiseContainment.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FibrewiseContainment.lean#L477).

> **Stacks Project, Tag 05KP.** Let `f : X ⟶ Y` be a finite type morphism of schemes, `F` a
> finite type quasi-coherent module on `X` and `U ⊆ X` open. If `Y` is irreducible with generic
> point `η` and all associated points of `F` restricted to the fibre over `η` lie in `U`, then
> there is a nonempty open `V ⊆ Y` such that the same containment holds in the fibre over every
> point of `V`.
>
> The target is replaced by its reduction, which is integral because the closed immersion of the
> reduction is a homeomorphism, and the containment is transported across that base change by
> Stacks 05KQ.

```lean
theorem exists_open_associatedPoints_fiber_subset {X Y : Scheme.{u}} (f : X ⟶ Y)
    (F : X.Modules) [LocallyOfFiniteType f] [QuasiCompact f] [F.IsQuasicoherent]
    [F.IsFiniteType] [IrreducibleSpace Y] (U : X.Opens) (η : Y)
    (hη : IsGenericPoint η Set.univ)
    (hηU : associatedPoints ((Scheme.Modules.pullback (f.fiberι η)).obj F) ⊆
      (f.fiberι η) ⁻¹' (U : Set X)) :
    ∃ V : Y.Opens, (V : Set Y).Nonempty ∧ ∀ y ∈ V,
      associatedPoints ((Scheme.Modules.pullback (f.fiberι y)).obj F) ⊆
        (f.fiberι y) ⁻¹' (U : Set X)
```

## Tag 05KQ, a lemma

[Tag 05KQ](https://stacks.math.columbia.edu/tag/05KQ) in the Stacks Project.

**`Stacks.RelativeAssassin.associatedPoints_fiber_subset_preimage_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FiberBaseChange.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FiberBaseChange.lean#L70).

> **Stacks Project, Tag 05KQ.** After arbitrary base change, the associated points of the
> pullback module on a fibre lie in the pulled-back open exactly when they did so on the original
> fibre.

```lean
theorem associatedPoints_fiber_subset_preimage_iff_baseChange
    {X S S' : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (U : X.Opens) (g : S' ⟶ S) (s' : S') :
    Stacks.Divisors.associatedPoints
          ((Scheme.Modules.pullback (f.fiberι (g s'))).obj F) ⊆
        (f.fiberι (g s')) ⁻¹' (U : Set X) ↔
      Stacks.Divisors.associatedPoints
            ((Scheme.Modules.pullback ((pullback.snd f g).fiberι s')).obj
              ((Scheme.Modules.pullback (pullback.fst f g)).obj F)) ⊆
          ((pullback.snd f g).fiberι s') ⁻¹'
            ((pullback.fst f g) ⁻¹' (U : Set X))
```

## Tag 05KR, a lemma

[Tag 05KR](https://stacks.math.columbia.edu/tag/05KR) in the Stacks Project.

**`Stacks.RelativeAssassin.isLocallyConstructible_fibrewiseContainment`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ContainmentConstructible.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ContainmentConstructible.lean#L491).

> **Stacks Project, Tag 05KR.** Let `f : X ⟶ Y` be a morphism of finite presentation, let `F`
> be a quasi-coherent `𝒪_X`-module of finite presentation and let `U ⊆ X` be an open subscheme
> with `U ⟶ Y` quasi-compact. Then the set of points `y` of `Y` over which every associated point
> of the fibre `F_y` lies in the fibre `U_y` is locally constructible in `Y`.

```lean
theorem isLocallyConstructible_fibrewiseContainment (f : X ⟶ Y)
    (hf : AlgebraicGeometry.FinitePresentation f) (F : X.Modules) [F.IsQuasicoherent]
    [F.IsFinitePresentation] (U : X.Opens) [QuasiCompact (U.ι ≫ f)] :
    IsLocallyConstructible (fibrewiseContainment f F U)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.25, Tag 05KM](https://stacks.math.columbia.edu/tag/05KM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
