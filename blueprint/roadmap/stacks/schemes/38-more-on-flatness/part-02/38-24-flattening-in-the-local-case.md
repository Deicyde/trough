---
declaration: section
origin: cited
lean: Module.FlatAtPointSituation.exists_ideal_condition_iff_map_eq_bot_of_henselian, AlgebraicGeometry.exists_closedSubscheme_flatOverAt_iff_factorStalk, AlgebraicGeometry.exists_finitePresentation_closedSubscheme_flatOverAt_iff_factorStalk, AlgebraicGeometry.exists_finitePresentation_closedSubscheme_flatOverAt_iff_factors, AlgebraicGeometry.exists_closedSubscheme_flatOverAt_iff_factors, AlgebraicGeometry.exists_idealSheafData_forall_isFlatOverAt_iff_of_isAdicComplete
statement: formalized
proof: formalized
---

# 38.24 Flattening in the local case

Section 38.24 of the Stacks Project, [Tag 05MZ](https://stacks.math.columbia.edu/tag/05MZ). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05PG, a theorem

[Tag 05PG](https://stacks.math.columbia.edu/tag/05PG) in the Stacks Project.

**`Module.FlatAtPointSituation.exists_ideal_condition_iff_map_eq_bot_of_henselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianFlatteningTheorem.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/HenselianFlatteningTheorem.lean#L88).

> **Stacks Project, Tag 05PG.** Let `A → B` be a local homomorphism of local rings with `A`
> henselian and `B` essentially of finite type over `A`, and let `M` be a finite `B`-module. There
> is an ideal `I ⊆ A` such that `A ⧸ I` corepresents the functor `F_lf` of Stacks Tag 05MK: for
> every local `A`-algebra `A'` with local structure map, the base change of `M` is flat over `A'`
> at every prime of `B ⊗_A A'` containing the extensions of the maximal ideals of `A'` and of `B`
> exactly when `I` dies in `A'`. If `B` is essentially of finite presentation over `A` and `M` is
> of finite presentation over `B`, then `I` is finitely generated.

```lean
theorem exists_ideal_condition_iff_map_eq_bot_of_henselian
    (S : FlatAtPointSituation.{u, v, w}) [HenselianLocalRing S.A]
    [Algebra.EssFiniteType S.A S.B] [Module.Finite S.B S.M] :
    ∃ I : Ideal S.A,
      (∀ R : LocalAlgCat.{u, x} S.A, S.Condition R ↔ Ideal.map (algebraMap S.A R) I = ⊥) ∧
      ((algebraMap S.A S.B).EssentiallyOfFinitePresentation →
        Module.FinitePresentation S.B S.M → I.FG)
```

## Tag 05PH, a remark

[Tag 05PH](https://stacks.math.columbia.edu/tag/05PH) in the Stacks Project.

**`AlgebraicGeometry.exists_closedSubscheme_flatOverAt_iff_factorStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LocalFlatteningSubscheme.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LocalFlatteningSubscheme.lean#L232). The attribute's comment: “the local flattening subscheme”.

> **Stacks Project, Tag 05PH.** A closed subscheme detects flatness of the
> pulled-back module at every point of the distinguished fibre lying above `x`.

```lean
theorem exists_closedSubscheme_flatOverAt_iff_factorStalk
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (x : X) (s : S) (hxs : f x = s)
    [HenselianLocalRing (S.presheaf.stalk s)]
    [IsIso (S.fromSpecStalk s)] :
    ∃ I : S.IdealSheafData,
      ∀ {T : Scheme.{u}} (g : T ⟶ S) (t : T) (_ht : g t = s),
        (∀ y : pullback (C := Scheme.{u}) f g,
            (pullback.snd f g y = t) →
            (pullback.fst f g y = x) →
              AlgebraicGeometry.IsFlatOverAt
                (pullback.snd f g).toLRSHom.toShHom
                ((Scheme.Modules.pullback (pullback.fst f g)).obj F) y) ↔
          ∃ h : Spec (T.presheaf.stalk t) ⟶ I.subscheme,
            h ≫ I.subschemeι = T.fromSpecStalk t ≫ g
```

**`AlgebraicGeometry.exists_finitePresentation_closedSubscheme_flatOverAt_iff_factorStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LocalFlatteningSubscheme.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LocalFlatteningSubscheme.lean#L351). The attribute's comment: “finite-presentation refinement”.

> **Stacks Project, Tag 05PH.** Under pointwise finite-presentation
> hypotheses, the local flattening subscheme can be finitely presented.

```lean
theorem exists_finitePresentation_closedSubscheme_flatOverAt_iff_factorStalk
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (x : X) (s : S) (hxs : f x = s)
    [HenselianLocalRing (S.presheaf.stalk s)]
    [IsIso (S.fromSpecStalk s)]
    (hfp : FinitePresentationAt f x)
    (hFfp :
      letI : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) F.val x
      Module.FinitePresentation (X.presheaf.stalk x)
        (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)) :
    ∃ I : S.IdealSheafData,
      FinitePresentation I.subschemeι ∧
      ∀ {T : Scheme.{u}} (g : T ⟶ S) (t : T) (_ht : g t = s),
        (∀ y : pullback (C := Scheme.{u}) f g,
            (pullback.snd f g y = t) →
            (pullback.fst f g y = x) →
              AlgebraicGeometry.IsFlatOverAt
                (pullback.snd f g).toLRSHom.toShHom
                ((Scheme.Modules.pullback (pullback.fst f g)).obj F) y) ↔
          ∃ h : Spec (T.presheaf.stalk t) ⟶ I.subscheme,
            h ≫ I.subschemeι = T.fromSpecStalk t ≫ g
```

## Tag 05PI, a lemma

[Tag 05PI](https://stacks.math.columbia.edu/tag/05PI) in the Stacks Project.

**`AlgebraicGeometry.exists_finitePresentation_closedSubscheme_flatOverAt_iff_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ClosedFibreFlatteningFinitePresentation.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ClosedFibreFlatteningFinitePresentation.lean#L154). The attribute's comment: “finite-presentation refinement”.

> **Stacks Project, Tag 05PI.** When the morphism and the module are in addition locally of
> finite presentation and the chosen subset of the closed fibre is closed and quasi-compact, the
> closed subscheme of the henselian local base detecting flatness along that subset can be chosen
> of finite presentation.

```lean
theorem exists_finitePresentation_closedSubscheme_flatOverAt_iff_factors
    (A : Type u) [CommRing A] [HenselianLocalRing A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f]
    [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    [F.IsFinitePresentation]
    (E : Set (f.fiber (IsLocalRing.closedPoint A)))
    (_ : IsClosed E) (hEcompact : IsCompact E) :
    ∃ I : (Spec (.of A)).IdealSheafData,
      FinitePresentation I.subschemeι ∧
      ∀ (T : Scheme.{u}) (g : T ⟶ Spec (.of A)) (t : T)
        (_ : g t = IsLocalRing.closedPoint A),
        (∀ y : (pullback f g : Scheme.{u}),
          (pullback.snd f g) y = t →
          (pullback.fst f g) y ∈
            (f.fiberι (IsLocalRing.closedPoint A)) '' E →
          AlgebraicGeometry.IsFlatOverAt (pullback.snd f g).toLRSHom.toShHom
            ((Scheme.Modules.pullback (pullback.fst f g)).obj F) y) ↔
        ∃ h : Spec (T.presheaf.stalk t) ⟶ I.subscheme,
          h ≫ I.subschemeι = T.fromSpecStalk t ≫ g
```

**`AlgebraicGeometry.exists_closedSubscheme_flatOverAt_iff_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ClosedFibreFlatteningSubscheme.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ClosedFibreFlatteningSubscheme.lean#L70). The attribute's comment: “closed flattening subscheme”.

> **Stacks Project, Tag 05PI.** Flatness of a finite type quasi-coherent module along an
> arbitrary subset `E` of the closed fibre, after an arbitrary pointed base change of a henselian
> local base, is detected by a closed subscheme of that base: the flatness condition for a pointed
> scheme `(T, t)` over `(Spec A, closed point)` holds exactly when `Spec O_{T,t} ⟶ Spec A` factors
> through the closed subscheme.

```lean
theorem exists_closedSubscheme_flatOverAt_iff_factors
    (A : Type u) [CommRing A] [HenselianLocalRing A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (E : Set (f.fiber (IsLocalRing.closedPoint A))) :
    ∃ I : (Spec (.of A)).IdealSheafData,
      ∀ (T : Scheme.{u}) (g : T ⟶ Spec (.of A)) (t : T)
        (_ : g t = IsLocalRing.closedPoint A),
        (∀ y : (pullback f g : Scheme.{u}),
          (pullback.snd f g) y = t →
          (pullback.fst f g) y ∈
            (f.fiberι (IsLocalRing.closedPoint A)) '' E →
          AlgebraicGeometry.IsFlatOverAt (pullback.snd f g).toLRSHom.toShHom
            ((Scheme.Modules.pullback (pullback.fst f g)).obj F) y) ↔
        ∃ h : Spec (T.presheaf.stalk t) ⟶ I.subscheme,
          h ≫ I.subschemeι = T.fromSpecStalk t ≫ g
```

## Tag 052G, a remark

[Tag 052G](https://stacks.math.columbia.edu/tag/052G) in the Stacks Project.

**`AlgebraicGeometry.exists_idealSheafData_forall_isFlatOverAt_iff_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/CompleteLocalFlattening.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/CompleteLocalFlattening.lean#L311). The attribute's comment: “the closed subscheme of Lemma 05PI for E = X_s over a Noetherian complete local base, constructed from finite affine charts and Lemma 0528”.

> **Stacks Project, Tag 052G.** Let `S = Spec A` be the spectrum of a Noetherian complete local
> ring with closed point `s`, let `f : X ⟶ S` be of finite type and let `F` be a quasi-coherent
> `𝒪_X`-module of finite type. Then the closed subscheme `Z ⊆ S` of Lemma 05PI for `E = X_s`
> exists: for every morphism of pointed schemes `(T, t) ⟶ (S, s)`, the pulled back module `F_T` is
> flat over `T` at every point of the fibre `X_t` if and only if `Spec(𝒪_{T,t}) ⟶ S` factors
> through `Z`. As the remark explains, the proof is elementary: a finite affine open cover reduces
> to `X` affine, where `Z` is cut out by the least flattening ideal of More on Algebra, Lemma 0526,
> whose universal property is Lemma 0528.

```lean
theorem exists_idealSheafData_forall_isFlatOverAt_iff_of_isAdicComplete
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    [IsAdicComplete (IsLocalRing.maximalIdeal A) A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] :
    ∃ Z : (Spec (.of A)).IdealSheafData,
      ∀ (T : Scheme.{u}) (g : T ⟶ Spec (.of A)) (t : T),
        g t = IsLocalRing.closedPoint A →
        ((∀ y : (pullback f g : Scheme.{u}), pullback.snd f g y = t →
            IsFlatOverAt (pullback.snd f g).toLRSHom.toShHom
              ((Scheme.Modules.pullback (pullback.fst f g)).obj F) y) ↔
          ∃ h : Spec (T.presheaf.stalk t) ⟶ Z.subscheme,
            h ≫ Z.subschemeι = T.fromSpecStalk t ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.24, Tag 05MZ](https://stacks.math.columbia.edu/tag/05MZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
