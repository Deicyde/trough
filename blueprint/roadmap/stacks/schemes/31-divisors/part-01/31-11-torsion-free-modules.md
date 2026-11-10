---
declaration: section
origin: cited
lean: AlgebraicGeometry.torsion_section_tfae, Stacks.AlgebraicGeometry.ReflexiveModules.IsTorsionSection, Stacks.AlgebraicGeometry.ReflexiveModules.IsTorsionFree, AlgebraicGeometry.isTorsionFree_iff_forall_isAffineOpen, Stacks.AlgebraicGeometry.TorsionQuasicoherent.torsionSubmodule_isQuasicoherent, Stacks.AlgebraicGeometry.TorsionQuasicoherent.isTorsionFree_torsionQuotient, AlgebraicGeometry.isTorsionFree_of_isFlat, Stacks.AlgebraicGeometry.ReflexiveModules.isTorsionFree_modulePullback
statement: formalized
proof: formalized
---

# 31.11 Torsion free modules

Section 31.11 of the Stacks Project, [Tag 0AVQ](https://stacks.math.columbia.edu/tag/0AVQ). 13 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AXR, a lemma

[Tag 0AXR](https://stacks.math.columbia.edu/tag/0AXR) in the Stacks Project.

**`AlgebraicGeometry.torsion_section_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionSections.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionSections.lean#L224).

> A section of a quasi-coherent module on an integral scheme is torsion at some stalk if
> and only if it is torsion at every stalk; equivalently, its germ at the generic point and
> its image in the pushforward from the generic point vanish.

```lean
theorem torsion_section_tfae
    (X : Scheme.{u}) [IsIntegral X] (F : X.Modules) [F.IsQuasicoherent]
    (U : X.Opens) [Nonempty U] (s : Γ(F, U)) :
    let η := genericPoint X
    let hη : η ∈ U :=
      ((genericPoint_spec X).mem_open_set_iff U.isOpen).mpr
        (by simpa using (inferInstance : Nonempty U))
    letI : ∀ V : X.Opens, Decidable (η ∈ V) := fun V ↦ Classical.propDecidable _
    let isTorsionAt (x : X) (hx : x ∈ U) : Prop :=
      letI : Module (X.presheaf.stalk x) ↑(F.presheaf.stalk x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) F.val x
      IsTorsionElement (R := X.presheaf.stalk x)
        (M := ↑(F.presheaf.stalk x)) (F.presheaf.germ U x hx s)
    List.TFAE [
      ∃ (x : X) (hx : x ∈ U), isTorsionAt x hx,
      ∀ (x : X) (hx : x ∈ U), isTorsionAt x hx,
      F.presheaf.germ U η hη s = 0,
      ((skyscraperPresheafStalkAdjunction (C := AddCommGrpCat.{u}) η).unit.app
        F.presheaf).app (op U) s = 0]
```

## Tag 0AVR, a definition

[Tag 0AVR](https://stacks.math.columbia.edu/tag/0AVR) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.IsTorsionSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Reflexive/Basic.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Reflexive/Basic.lean#L138). The attribute's comment: “part (1)”. References: EGA I (7.4.1), “torsion section”.

> A local section of a module on a scheme is *torsion* if its germ at every point of its
> domain is a torsion element of the stalk, i.e. is annihilated by a nonzero element of the
> local ring.

```lean
public def IsTorsionSection (F : X.Modules) {U : X.Opens} (s : Γ(F, U)) : Prop
```

**`Stacks.AlgebraicGeometry.ReflexiveModules.IsTorsionFree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Reflexive/Basic.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Reflexive/Basic.lean#L144). The attribute's comment: “part (2)”. References: EGA I (7.4.1), “torsion free”; EGA IV (20.1.5), “quasi-coherent case”.

> A module on a scheme is *torsion free* if every torsion local section vanishes.

```lean
public def IsTorsionFree (F : X.Modules) : Prop
```

## Tag 0AXS, a lemma

[Tag 0AXS](https://stacks.math.columbia.edu/tag/0AXS) in the Stacks Project.

**`AlgebraicGeometry.isTorsionFree_iff_forall_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean#L170).

> A quasi-coherent module on an integral scheme is torsion free if and only if its
> sections on every affine open are torsion free over the ring of functions there.

```lean
theorem isTorsionFree_iff_forall_isAffineOpen
    {X : Scheme.{u}} [IsIntegral X] (F : X.Modules) [F.IsQuasicoherent] :
    IsTorsionFree F ↔
      ∀ U : X.Opens, IsAffineOpen U → Module.IsTorsionFree Γ(X, U) Γ(F, U)
```

## Tag 0AXT, a lemma

[Tag 0AXT](https://stacks.math.columbia.edu/tag/0AXT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.TorsionQuasicoherent.torsionSubmodule_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TorsionQuasicoherent/Basic.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TorsionQuasicoherent/Basic.lean#L316). The attribute's comment: “torsion_subsheaf_quasi_coherent”. References: EGA I (7.4.1), “quasi-coherence of T”.

> **The first assertion of [Stacks, Tag 0AXT].** The torsion submodule sheaf of a
> quasi-coherent module on an integral scheme is quasi-coherent.

```lean
instance torsionSubmodule_isQuasicoherent :
    (torsionSubmodule F).toSheafOfModules.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.TorsionQuasicoherent.isTorsionFree_torsionQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TorsionQuasicoherent/Quotient.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TorsionQuasicoherent/Quotient.lean#L165). The attribute's comment: “the quotient F/F_tors is torsion free”. References: EGA I (7.4.1), “special case”.

> **The second assertion of [Stacks, Tag 0AXT].** The quotient of a quasi-coherent module on
> an integral scheme by its torsion subsheaf is torsion free.

```lean
theorem isTorsionFree_torsionQuotient :
    ReflexiveModules.IsTorsionFree (torsionQuotient F)
```

## Tag 0AXU, a lemma

[Tag 0AXU](https://stacks.math.columbia.edu/tag/0AXU) in the Stacks Project.

**`AlgebraicGeometry.isTorsionFree_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean#L222).

> A flat quasi-coherent module on an integral scheme is torsion free.

```lean
theorem isTorsionFree_of_isFlat {X : Scheme.{u}} [IsIntegral X]
    (F : X.Modules) [F.IsQuasicoherent]
    (hF : SheafOfModules.IsFlat.{u, u, u, u} (O := X.sheaf) F) :
    IsTorsionFree F
```

## Tag 0AXV, a lemma

[Tag 0AXV](https://stacks.math.columbia.edu/tag/0AXV) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.isTorsionFree_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/TorsionFree/FlatPullback.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/TorsionFree/FlatPullback.lean#L89). References: EGA IV (9.4.9), “partial”.

> **Stacks Project, Tag 0AXV.** The flat pullback of a torsion-free quasi-coherent module on an
> integral scheme is torsion free.

```lean
theorem isTorsionFree_modulePullback {X Y : Scheme.{u}}
    [IsIntegral X] [IsIntegral Y] (f : X ⟶ Y) [Flat f]
    (G : Y.Modules) [G.IsQuasicoherent] (hG : IsTorsionFree G) :
    letI : ((Scheme.Modules.pullback f).obj G).IsQuasicoherent :=
      @AlgebraicGeometry.SheafOfModules.modulePullback_isQuasicoherent X.toRingedSpace
        Y.toRingedSpace f.toLRSHom.toShHom G ‹G.IsQuasicoherent›
    IsTorsionFree ((Scheme.Modules.pullback f).obj G)
```

## Tag 0BCM, a lemma

[Tag 0BCM](https://stacks.math.columbia.edu/tag/0BCM) in the Stacks Project.

**`AlgebraicGeometry.isIntegral_of_flat_of_isIntegral_genericFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/GenericFibre.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/GenericFibre.lean#L78).

> **Stacks Project, Tag 0BCM.** If a flat morphism has integral target and integral generic
> fibre, then its source is integral.

```lean
theorem isIntegral_of_flat_of_isIntegral_genericFiber
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Flat f] [IsIntegral Y]
    [IsIntegral (f.fiber (genericPoint Y))] : IsIntegral X
```

## Tag 0AXW, a lemma

[Tag 0AXW](https://stacks.math.columbia.edu/tag/0AXW) in the Stacks Project.

**`AlgebraicGeometry.isTorsionFree_iff_forall_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean#L106).

> A quasi-coherent module on an integral scheme is torsion free precisely when its
> stalk at every point is torsion free over the local ring at that point.

```lean
theorem isTorsionFree_iff_forall_stalk
    {X : Scheme.{u}} [IsIntegral X] (F : X.Modules) [F.IsQuasicoherent] :
    IsTorsionFree F ↔
      ∀ x : X,
        letI : Module (X.presheaf.stalk x) ↑(F.presheaf.stalk x) :=
          PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
            (R := X.presheaf) F.val x
        Module.IsTorsionFree (X.presheaf.stalk x) ↑(F.presheaf.stalk x)
```

## Tag 0AXX, a lemma

[Tag 0AXX](https://stacks.math.columbia.edu/tag/0AXX) in the Stacks Project.

**`AlgebraicGeometry.isTorsionFree_middle_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/TorsionFree.lean#L201).

> A short exact extension of torsion-free quasi-coherent modules on an integral
> scheme is torsion free.

```lean
lemma isTorsionFree_middle_of_shortExact {X : Scheme.{u}} [IsIntegral X]
    (S : ShortComplex X.Modules) (hS : S.ShortExact)
    [S.X₁.IsQuasicoherent] [S.X₂.IsQuasicoherent] [S.X₃.IsQuasicoherent]
    (h₁ : IsTorsionFree S.X₁)
    (h₃ : IsTorsionFree S.X₃) :
    IsTorsionFree S.X₂
```

## Tag 0AXY, a lemma

[Tag 0AXY](https://stacks.math.columbia.edu/tag/0AXY) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ReflexiveModules.isTorsionFree_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/TorsionFree/IntegralNoetherian.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/TorsionFree/IntegralNoetherian.lean#L269). References: EGA IV (5.10.14), “integral case, (i)”.

> **Stacks Project, Tag 0AXY.** The characterizations of a nonzero torsion-free coherent
> module on a locally Noetherian integral scheme: torsion freeness, uniqueness of the generic
> point as associated point, Serre's condition `(S₁)` with support at the generic point, and
> absence of embedded associated points with support at the generic point.

```lean
theorem isTorsionFree_tfae
    (X : Scheme.{u}) [IsLocallyNoetherian X] [IsIntegral X]
    (F : X.Modules) [F.IsCoherent] (hF : (SheafOfModules.supp F).Nonempty) :
    letI : F.IsQuasicoherent := isQuasicoherent_of_isCoherent F
    List.TFAE [
      IsTorsionFree F,
      Stacks.Divisors.associatedPoints F = {genericPoint X},
      genericPoint X ∈ SheafOfModules.supp F ∧ AlgebraicGeometry.SheafHasPropertySk X F 1,
      genericPoint X ∈ SheafOfModules.supp F ∧
        AlgebraicGeometry.HasNoEmbeddedAssociatedPoints F]
```

## Tag 0CC4, a lemma

[Tag 0CC4](https://stacks.math.columbia.edu/tag/0CC4) in the Stacks Project.

**`AlgebraicGeometry.isTorsionFree_iff_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/TorsionFreeDimensionOne.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/TorsionFreeDimensionOne.lean#L68).

> On an integral regular scheme of dimension at most one a coherent module is torsion free if
> and only if it is finite locally free.

```lean
theorem isTorsionFree_iff_isFiniteLocallyFree {X : Scheme.{u}} [IsIntegral X]
    (hregular : IsRegular X) (hdim : topologicalKrullDim X ≤ 1)
    (F : X.Modules) [_root_.SheafOfModules.IsCoherent F] :
    (let : F.IsQuasicoherent := _root_.isQuasicoherent_of_isCoherent F
     IsTorsionFree F) ↔ SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) F
```

## Tag 0AXZ, a lemma

[Tag 0AXZ](https://stacks.math.columbia.edu/tag/0AXZ) in the Stacks Project.

**`AlgebraicGeometry.isTorsionFree_sheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/TorsionFree/SheafHom.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/TorsionFree/SheafHom.lean#L64). The attribute's comment: “torsion freeness”.

> **The torsion freeness clause of [Stacks, Tag 0AXZ].** On an integral scheme, the sheaf-hom
> `SheafHom(F, G)` from a module of finite presentation into a quasi-coherent torsion free module
> is torsion free.
>
> The proof is the one of the source: torsion freeness of a quasi-coherent module on an integral
> scheme is a condition on the stalks, the stalk of `SheafHom(F, G)` at `x` is
> `Hom_{𝒪_{X,x}}(F_x, G_x)` by [Stacks, Tag 01CP], and a module of linear maps into a torsion free
> module is torsion free.

```lean
theorem isTorsionFree_sheafHom {X : Scheme.{u}} [IsIntegral X] (F G : X.Modules)
    [F.IsFinitePresentation] [G.IsQuasicoherent] (hG : IsTorsionFree G) :
    IsTorsionFree (sheafInternalHom (spaceRingedSite X.sheaf) F G)
```

**`AlgebraicGeometry.sheafHom_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomCoherent/Quasicoherent.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InternalHomCoherent/Quasicoherent.lean#L135). The attribute's comment: “quasi-coherence”.

> **The quasi-coherence clause of [Stacks, Tag 0AXZ].** On a scheme, the sheaf-hom
> `SheafHom(F, G)` from a module of finite presentation into a quasi-coherent module is
> quasi-coherent.
>
> This is the assertion of Schemes, [Stacks, Tag 01LA] which makes the statement of Tag 0AXZ
> meaningful: torsion freeness is a notion for quasi-coherent modules. It is deduced from the
> first clause of [Stacks, Tag 01CQ],
> `Stacks.SheafOfModules.InternalHom.exists_locally_isoKernel_sheafInternalHom`.

```lean
theorem sheafHom_isQuasicoherent (F G : X.Modules)
    [F.IsFinitePresentation] [G.IsQuasicoherent] :
    SheafOfModules.IsQuasicoherent (R := X.ringCatSheaf)
      (sheafInternalHom (spaceRingedSite X.sheaf) F G)
```

## Tag 0AVS, a lemma

[Tag 0AVS](https://stacks.math.columbia.edu/tag/0AVS) in the Stacks Project.

**`AlgebraicGeometry.isIso_of_stalk_isIso_or_depth_two_and_not_associated_of_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Reflexive.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/Reflexive.lean#L180). The attribute's comment: “alternative (2) in the form Tag 0AV8 gives it, namely depth at least two at a point not associated to the target, which is the form the source's proof of this statement reduces to through Tag 0AV9, and asked for only at the generic point, the one point of an integral base at which a torsion-free target can have an associated point”.

> **Stacks Project, Tag 0AVS.** Let `X` be an integral locally Noetherian scheme and
> `f : F ⟶ G` a map of quasi-coherent modules with `F` coherent and `G` torsion free. If at every
> point the map on stalks is an isomorphism, or the stalk of `F` has depth at least two and, at
> the generic point, that point is not associated to `G`, then `f` is an isomorphism.
>
> Alternative (2) is the one of Tag 0AV8, the lemma the source's proof of this statement reduces
> to: Tag 0AVS is proved there as a translation of Tag 0AV9 into the language of schemes, Tag 0AV9
> as a special case of Tag 0AV8, and the alternative (2) of Tag 0AV8 reads `depth(M_p) ≥ 2`
> together with `p ∉ Ass(N)`. Over an integral base with `G` torsion free the clause on associated
> points holds of itself at every point other than the generic one, by
> `eq_genericPoint_of_isAssociatedPoint_of_isTorsionFree`, which is why it is asked for here only
> at the generic point; that single point is where it does its work, by
> `exists_counterexample_to_displayed_statement_of_tag_0AVS`, which exhibits a map satisfying
> alternative (2) of Tag 0AVS as displayed at every point and failing to be an isomorphism.

```lean
theorem isIso_of_stalk_isIso_or_depth_two_and_not_associated_of_isTorsionFree
    {X : Scheme.{u}} [IsIntegral X] [IsLocallyNoetherian X]
    {F G : X.Modules} [F.IsQuasicoherent] [G.IsQuasicoherent] [F.IsCoherent]
    (f : F ⟶ G) (hG : Stacks.AlgebraicGeometry.ReflexiveModules.IsTorsionFree G)
    (hf : ∀ x : X,
      let : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) F.val x
      IsIso ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
        ((PresheafOfModules.toPresheaf X.ringCatSheaf.obj).map f.val)) ∨
      ((2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
          (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x) ∧
        (x = genericPoint X → x ∉ Stacks.Divisors.associatedPoints G))) :
    IsIso f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.11, Tag 0AVQ](https://stacks.math.columbia.edu/tag/0AVQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
