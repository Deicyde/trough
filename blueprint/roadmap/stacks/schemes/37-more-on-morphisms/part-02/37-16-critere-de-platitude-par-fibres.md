---
declaration: section
origin: cited
lean: Stacks.Flatness.isFlatOverBaseAndFiberAt_iff_of_isLocallyNoetherian, Stacks.Flatness.isFlatOverBaseAndFiberAt_iff, Stacks.Flatness.isOpen_isFlatOverBaseAndFiberAt, AlgebraicGeometry.flat_of_flat_fiberHom, AlgebraicGeometry.flat_of_flat_fiberHom_of_surjective, Stacks.Flatness.flat_of_flat_fiberHom, Stacks.Flatness.flat_of_flat_fiberHom_of_surjective, AlgebraicGeometry.isOpen_setOf_isFlatOverAt_of_locallyOfFiniteType
statement: formalized
proof: formalized
---

# 37.16 Critère de platitude par fibres

Section 37.16 of the Stacks Project, [Tag 039A](https://stacks.math.columbia.edu/tag/039A). 8 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 039B, a theorem

[Tag 039B](https://stacks.math.columbia.edu/tag/039B) in the Stacks Project.

**`Stacks.Flatness.isFlatOverBaseAndFiberAt_iff_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseFiber.lean, line 702](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseFiber.lean#L702). The attribute's comment: “Noetherian fibrewise criterion”. References: EGA IV (11.3.10), “1°) a) ⇔ b)”.

> For morphisms `f : X ⟶ Y` and `g : Y ⟶ S` of locally Noetherian schemes and a coherent
> `𝒪_X`-module `F` with nonzero stalk at `x`, flatness over the base together with flatness on the
> fibre is equivalent to flatness of `Y` over the base at `f x` together with flatness of `F` over
> `Y` at `x`.

```lean
public theorem isFlatOverBaseAndFiberAt_iff_of_isLocallyNoetherian {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ S)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [IsLocallyNoetherian S] [IsLocallyNoetherian X] [IsLocallyNoetherian Y]
    [F.IsQuasicoherent] [Stacks.SheafOfModules.IsCoherent F]
    (x : X)
    (hx : ∃ a : TopCat.Presheaf.stalk (C := AddCommGrpCat.{u}) F.val.presheaf x,
      a ≠ 0) :
    IsFlatOverBaseAndFiberAt f g F x ↔ IsFlatOverIntermediateAt f g F x
```

## Tag 039C, a theorem

[Tag 039C](https://stacks.math.columbia.edu/tag/039C) in the Stacks Project.

**`Stacks.Flatness.isFlatOverBaseAndFiberAt_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseFiber.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseFiber.lean#L633). The attribute's comment: “fibrewise criterion”. References: EGA IV (11.3.10), “2°) a) ⇔ b)”.

> At a point where a quasi-coherent module of finite presentation has nonzero stalk, flatness
> over the base together with flatness on the fibre is equivalent to flatness of the intermediate
> scheme over the base together with flatness over the intermediate scheme.

```lean
public theorem isFlatOverBaseAndFiberAt_iff {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ S)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [LocallyOfFinitePresentation (f ≫ g)] [F.IsFinitePresentation]
    [LocallyOfFiniteType g]
    (x : X)
    (hx : ∃ a : TopCat.Presheaf.stalk (C := AddCommGrpCat.{u}) F.val.presheaf x,
      a ≠ 0) :
    IsFlatOverBaseAndFiberAt f g F x ↔ IsFlatOverIntermediateAt f g F x
```

**`Stacks.Flatness.isOpen_isFlatOverBaseAndFiberAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseOpenLocus.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseOpenLocus.lean#L93). The attribute's comment: “openness of the common locus”. References: EGA IV (11.3.10), “2°) open locus”.

> **Stacks Project, Tag 039C.** The set of points of the support of a quasi-coherent module of
> finite presentation at which the two equivalent conditions of the fibrewise criterion for
> flatness hold is open in the support.

```lean
public theorem isOpen_isFlatOverBaseAndFiberAt {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ S)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
    [LocallyOfFinitePresentation (f ≫ g)] [F.IsFinitePresentation] [LocallyOfFiniteType g] :
    IsOpen {x : SheafOfModules.supp F |
      IsFlatOverBaseAndFiberAt f g F x.1 ∧ IsFlatOverIntermediateAt f g F x.1}
```

## Tag 039D, a lemma

[Tag 039D](https://stacks.math.columbia.edu/tag/039D) in the Stacks Project.

**`AlgebraicGeometry.flat_of_flat_fiberHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean#L130). The attribute's comment: “flatness of the morphism”.

> **Stacks Project, Tag 039D.** Let `f : X ⟶ Y` be a morphism of schemes over a base `S`, given
> by `g : Y ⟶ S`. If `S`, `X`, `Y` are locally Noetherian, `X` is flat over `S` and every induced
> morphism of fibres `X_s ⟶ Y_s` is flat, then `f` is flat.

```lean
public theorem flat_of_flat_fiberHom {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [IsLocallyNoetherian S] [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Flat (f ≫ g)]
    (hfib : ∀ s : S, Flat (Stacks.Flatness.fiberHom f g s)) :
    Flat f
```

**`AlgebraicGeometry.flat_of_flat_fiberHom_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean#L141). The attribute's comment: “flatness of the intermediate scheme over the base”.

> **Stacks Project, Tag 039D.** In the situation of
> `AlgebraicGeometry.flat_of_flat_fiberHom`, if `f` is in addition surjective then `Y` is flat over
> the base.

```lean
public theorem flat_of_flat_fiberHom_of_surjective {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [IsLocallyNoetherian S] [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Flat (f ≫ g)]
    [Surjective f] (hfib : ∀ s : S, Flat (Stacks.Flatness.fiberHom f g s)) :
    Flat g
```

## Tag 039E, a lemma

[Tag 039E](https://stacks.math.columbia.edu/tag/039E) in the Stacks Project.

**`Stacks.Flatness.flat_of_flat_fiberHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseMorphism.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseMorphism.lean#L220). The attribute's comment: “flatness of the morphism”. References: EGA IV (20.5.7), “partial”; SGA 1 I (5.9), “partial”.

> **Stacks Project, Tag 039E.** Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes with
> `X` locally of finite presentation and flat over `S`, with `Y` locally of finite type over `S`,
> and with the morphism `X_s ⟶ Y_s` of fibres flat for every point `s` of `S`. Then `f` is
> flat.

```lean
public theorem flat_of_flat_fiberHom {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [LocallyOfFinitePresentation (f ≫ g)] [LocallyOfFiniteType g]
    [AlgebraicGeometry.Flat (f ≫ g)]
    (hfib : ∀ s : S, AlgebraicGeometry.Flat (fiberHom f g s)) :
    AlgebraicGeometry.Flat f
```

**`Stacks.Flatness.flat_of_flat_fiberHom_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseMorphism.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Flat/FibrewiseMorphism.lean#L232). The attribute's comment: “flatness of the target over the base”.

> **Stacks Project, Tag 039E.** In the situation of
> `Stacks.Flatness.flat_of_flat_fiberHom`, if `f` is moreover surjective then `Y` is flat
> over `S`.

```lean
public theorem flat_of_flat_fiberHom_of_surjective {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [LocallyOfFinitePresentation (f ≫ g)] [LocallyOfFiniteType g]
    [AlgebraicGeometry.Flat (f ≫ g)] [AlgebraicGeometry.Surjective f]
    (hfib : ∀ s : S, AlgebraicGeometry.Flat (fiberHom f g s)) :
    AlgebraicGeometry.Flat g
```

## Tag 05VJ, a lemma

[Tag 05VJ](https://stacks.math.columbia.edu/tag/05VJ) in the Stacks Project.

**`AlgebraicGeometry.isOpen_setOf_isFlatOverAt_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean#L318). The attribute's comment: “open locus”.

> **Stacks Project, Tag 05VJ (open locus).** For a morphism `f : X ⟶ Y` of schemes over a base
> with `X` locally of finite presentation over the base and `Y` locally of finite type over it, the
> locus where a finitely presented quasi-coherent `𝒪_X`-module is flat over `Y` is open, because `f`
> is then itself locally of finite presentation.

```lean
public theorem isOpen_setOf_isFlatOverAt_of_locallyOfFiniteType {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (pY : Y ⟶ S)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    [F.IsFinitePresentation] [LocallyOfFinitePresentation (f ≫ pY)] [LocallyOfFiniteType pY] :
    IsOpen {x : X | IsFlatOverAt f.toLRSHom.toShHom F x}
```

**`AlgebraicGeometry.setOf_isFlatOverAt_modulePullback_of_isFlatOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FlatLocusBaseChange.lean#L335). The attribute's comment: “base change”.

> **Stacks Project, Tag 05VJ (base change).** For a morphism `f : X ⟶ Y` of schemes over a base
> `S` with `X` locally of finite presentation over `S` and `Y` locally of finite type over `S`, and
> a finitely presented quasi-coherent `𝒪_X`-module flat over `S`, the locus where the module is flat
> over `Y` commutes with an arbitrary base change `S' ⟶ S`: the corresponding locus upstairs is the
> preimage of the original one.

```lean
public theorem setOf_isFlatOverAt_modulePullback_of_isFlatOver
    {X Y S S' X' Y' : Scheme.{u}} {f : X ⟶ Y} {pY : Y ⟶ S} {g : S' ⟶ S}
    {qY : Y' ⟶ Y} {pY' : Y' ⟶ S'} {qX : X' ⟶ X} {f' : X' ⟶ Y'}
    (hY : IsPullback qY pY' pY g) (hX : IsPullback qX f' f qY)
    (F : SheafOfModules.{u} (structureSheafRing X.toRingedSpace)) [F.IsQuasicoherent]
    [F.IsFinitePresentation] [LocallyOfFinitePresentation (f ≫ pY)] [LocallyOfFiniteType pY]
    (hF : IsFlatOver (f ≫ pY).toLRSHom.toShHom F) :
    {x' : X' | IsFlatOverAt f'.toLRSHom.toShHom
        ((modulePullback qX.toLRSHom.toShHom).obj F) x'} =
      qX ⁻¹' {x : X | IsFlatOverAt f.toLRSHom.toShHom F x}
```

## Tag 05VK, a lemma

[Tag 05VK](https://stacks.math.columbia.edu/tag/05VK) in the Stacks Project.

**`AlgebraicGeometry.isOpen_setOf_isFlatAt_of_locallyOfFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean#L159). The attribute's comment: “open locus”. References: SGA 3 VIB (1.3), “partial”; SGA 3 X (4.4), “partial”; SGA 3 XV (7.2), “partial”.

> **Stacks Project, Tag 05VK (open locus).** For a morphism `f : X ⟶ Y` of schemes over a base
> with `X` locally of finite presentation over the base and `Y` locally of finite type over it, the
> locus of points of `X` at which `f` is flat is open.
>
> Flatness of `X` over the base, which the source assumes, is not needed here: the two finiteness
> hypotheses already make `f` locally of finite presentation, so Tag 0399 applies to `f` itself.

```lean
public theorem isOpen_setOf_isFlatAt_of_locallyOfFinitePresentation_comp {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (pY : Y ⟶ S) [LocallyOfFinitePresentation (f ≫ pY)] [LocallyOfFiniteType pY] :
    IsOpen {x : X | IsFlatAt f.toLRSHom.toShHom x}
```

**`AlgebraicGeometry.setOf_isFlatAt_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FlatMorphisms/FibrewiseCriterion.lean#L173). The attribute's comment: “base change”. References: EGA IV (20.5.7), “more general”; SGA 3 VIB (2.5), “flatness clause”; SGA 3 XV (7.2), “partial”.

> **Stacks Project, Tag 05VK (base change).** For a morphism `f : X ⟶ Y` of schemes over a base
> `S` with `X` locally of finite presentation and flat over `S` and `Y` locally of finite type over
> `S`, the locus of points at which `f` is flat commutes with an arbitrary base change `S' ⟶ S`:
> the corresponding locus upstairs is the preimage of the original one.

```lean
public theorem setOf_isFlatAt_baseChange {X Y S S' X' Y' : Scheme.{u}} {f : X ⟶ Y} {pY : Y ⟶ S}
    {g : S' ⟶ S} {qY : Y' ⟶ Y} {pY' : Y' ⟶ S'} {qX : X' ⟶ X} {f' : X' ⟶ Y'}
    (hY : IsPullback qY pY' pY g) (hX : IsPullback qX f' f qY)
    [LocallyOfFinitePresentation (f ≫ pY)] [LocallyOfFiniteType pY] [Flat (f ≫ pY)] :
    {x' : X' | IsFlatAt f'.toLRSHom.toShHom x'} =
      qX ⁻¹' {x : X | IsFlatAt f.toLRSHom.toShHom x}
```

## Tag 080Q, a lemma

[Tag 080Q](https://stacks.math.columbia.edu/tag/080Q) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.exists_iso_free_over_of_flat_over_at_of_flat_fiber_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiberRank/FlatFibreFiniteFree.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiberRank/FlatFibreFiniteFree.lean#L178).

> **Stacks Project, Tag 080Q.** Let `f : X ⟶ S` be a morphism of finite presentation and let
> `F` be a finitely presented `𝒪_X`-module. If `F` is flat over `S` at `x` and the stalk at `x` of
> the restriction of `F` to the fibre of `f` through `x` is a flat module over the local ring of
> that fibre, then `F` is free of finite rank on an open neighbourhood of `x`.

```lean
theorem exists_iso_free_over_of_flat_over_at_of_flat_fiber_stalk {X S : Scheme.{u}} (f : X ⟶ S)
    (hf : AlgebraicGeometry.FinitePresentation f) (F : X.Modules) [F.IsFinitePresentation]
    (x : X)
    (hflat : AlgebraicGeometry.IsFlatOverAt (Scheme.Hom.toLRSHom f).toShHom F x)
    (hfiber :
      letI := Stacks.Flatness.stalkModule
        ((Scheme.Modules.pullback (f.fiberι (f x))).obj F) (f.asFiber x)
      Module.Flat (ToType ((f.fiber (f x)).presheaf.stalk (f.asFiber x)))
        (ToType (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u})
          ((Scheme.Modules.pullback (f.fiberι (f x))).obj F).val.presheaf (f.asFiber x)))) :
    ∃ U : X.Opens, x ∈ U ∧ ∃ n : ℕ,
      Nonempty (F.over U ≅ SheafOfModules.free (ULift.{u} (Fin n)))
```

## Tag 0CZR, a lemma

[Tag 0CZR](https://stacks.math.columbia.edu/tag/0CZR) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isOpen_freeLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiberRank/FreeLocusBaseChange.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiberRank/FreeLocusBaseChange.lean#L85). The attribute's comment: “openness”.

> **Stacks Project, Tag 0CZR (openness).** The locus of points at which a sheaf of modules on
> a scheme is free of finite rank on a neighbourhood is open: the trivialising neighbourhood of a
> point of the locus is contained in the locus.

```lean
public theorem isOpen_freeLocus {X : Scheme.{u}} (F : X.Modules) :
    IsOpen (freeLocus F)
```

**`AlgebraicGeometry.Scheme.Modules.freeLocus_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiberRank/FreeLocusBaseChange.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiberRank/FreeLocusBaseChange.lean#L197). The attribute's comment: “base change”.

> **Stacks Project, Tag 0CZR (base change).** Let `f : X ⟶ S` be locally of finite presentation
> and let `F` be a finitely presented `𝒪_X`-module flat over `S`. The formation of the locus of
> points at which `F` is free of finite rank on a neighbourhood commutes with an arbitrary base
> change `g : S' ⟶ S`: the locus of the pulled-back module is the preimage of the original locus
> under the projection.

```lean
public theorem freeLocus_pullback {X S S' : Scheme.{u}} (f : X ⟶ S)
    (F : X.Modules) [F.IsFinitePresentation] [LocallyOfFinitePresentation f]
    (hF : AlgebraicGeometry.IsFlatOver f.toLRSHom.toShHom F) (g : S' ⟶ S) :
    freeLocus ((Scheme.Modules.pullback (pullback.fst f g)).obj F) =
      pullback.fst f g ⁻¹' freeLocus F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.16, Tag 039A](https://stacks.math.columbia.edu/tag/039A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
