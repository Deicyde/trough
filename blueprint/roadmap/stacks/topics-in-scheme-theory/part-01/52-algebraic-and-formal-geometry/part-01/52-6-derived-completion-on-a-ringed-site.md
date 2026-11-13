---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.derivedSheafHom_awayCoextendScalars_idempotent, AlgebraicGeometry.RingedSite.derivedSheafHom_awayMulCurryIso, AlgebraicGeometry.RingedSite.derivedSheafHom_coextendScalarsIso, AlgebraicGeometry.RingedSite.coextHomComplexIso_hom_apply, AlgebraicGeometry.RingedSite.derivedSheafHom_awayRestrictScalarsIso, AlgebraicGeometry.RingedSite.derivedSheafHom_awayRestrictScalarsIso_canonical, AlgebraicGeometry.RingedSite.sheafHomComplex_awayLocalizedAction_agree, AlgebraicGeometry.RingedSite.isZero_derivedSheafHom_derivedAwayModule_of_forall
statement: formalized
proof: formalized
---

# 52.6 Derived completion on a ringed site

Section 52.6 of the Stacks Project, [Tag 0995](https://stacks.math.columbia.edu/tag/0995). 21 tags here are carried by 82 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0996, a lemma

[Tag 0996](https://stacks.math.columbia.edu/tag/0996) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedSheafHom_awayCoextendScalars_idempotent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayCoextensionIdempotent.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayCoextensionIdempotent.lean#L62). The attribute's comment: “part (2)”.

> Let `(𝒞, 𝒪)` be a ringed site, let `f` be a global section of `𝒪` and let `K ∈ D(𝒪)`. Then
>
> `R𝑆heafHom_𝒪(𝒪_f, R𝑆heafHom_𝒪(𝒪_f, K)) = R𝑆heafHom_𝒪(𝒪_f, K)`,
>
> with `K` computed by a K-injective complex `I` of sheaves of `𝒪`-modules and
> `R𝑆heafHom_𝒪(𝒪_f, K)` by the coextension of scalars of `I` along `𝒪 ⟶ 𝒪_f`.

```lean
def derivedSheafHom_awayCoextendScalars_idempotent (X : RingedSite.{u, u, u})
    (h : Presheaf.globalSections (X.O.obj ⋙ forget CommRingCat.{u}))
    (I : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    [I.IsKInjective] :
    DerivedCategory.Q.obj ((coeffCoextendComplex X (awaySheaf h) (toAwaySheaf h)).obj I) ≅
      DerivedCategory.Q.obj ((coeffCoextendComplex X (awaySheaf h) (toAwaySheaf h)).obj
        ((coeffRestrictComplex X (awaySheaf h) (toAwaySheaf h)).obj
          ((coeffCoextendComplex X (awaySheaf h) (toAwaySheaf h)).obj I)))
```

**`AlgebraicGeometry.RingedSite.derivedSheafHom_awayMulCurryIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayInternalHomMulDerived.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayInternalHomMulDerived.lean#L108). The attribute's comment: “part (3)”.

> **Stacks Tag 0996(3).** Let `(𝒞, 𝒪)` be a ringed site, let `f` and `g` be global sections of
> `𝒪` and let `K ∈ D(𝒪)`. Then
>
> `R𝑆heafHom_𝒪(𝒪_f, R𝑆heafHom_𝒪(𝒪_g, K)) = R𝑆heafHom_𝒪(𝒪_{g f}, K)`.
>
> Computing `K` by a K-injective complex `I` of sheaves of `𝒪`-modules, `SheafHom•_𝒪(𝒪_g, I)`
> represents `R𝑆heafHom_𝒪(𝒪_g, K)` and is itself K-injective as a complex of sheaves of
> `𝒪`-modules — `AlgebraicGeometry.RingedSite.isKInjective_sheafHomComplex_awayComplex` — so
> `SheafHom•_𝒪(𝒪_f, SheafHom•_𝒪(𝒪_g, I))` represents the left-hand side; and
> `SheafHom•_𝒪(𝒪_{g f}, I)` represents the right-hand side. Nothing is assumed of `f` or `g`.

```lean
def derivedSheafHom_awayMulCurryIso
    (I : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    [I.IsKInjective] :
    DerivedCategory.Q.obj (sheafHomComplex X (awayComplex X f)
        (sheafHomComplex X (awayComplex X g) I).obj).obj ≅
      DerivedCategory.Q.obj (sheafHomComplex X (awayComplex X (mulGlobalSection X f g)) I).obj
```

**`AlgebraicGeometry.RingedSite.derivedSheafHom_coextendScalarsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/HomIntoCoextension.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/HomIntoCoextension.lean#L489). The attribute's comment: “part (2)”.

> **Stacks Tag 0996(2).** Let `(𝒞, 𝒪)` be a ringed site, let `φ₀ : 𝒪 ⟶ 𝒪'` be a morphism of
> sheaves of commutative rings — for instance the localization `𝒪 ⟶ 𝒪_f` at a global section —
> let `K ∈ D(𝒪)` and `L ∈ D(𝒪')`. Then
>
> `R SheafHom_𝒪(L, K) = R SheafHom_{𝒪'}(L, R SheafHom_𝒪(𝒪', K))`.
>
> Computing `K` by a K-injective complex `I` of sheaves of `𝒪`-modules, the right-hand side is
> the internal Hom complex over `𝒪'` of `L` and of `SheafHom_𝒪(𝒪', I)` = `coeffCoextendComplex`
> applied to `I`, the latter representing `R SheafHom_𝒪(𝒪', K)`; the left-hand side is the
> internal Hom complex over `𝒪` of the restriction of scalars of `L` and of `I`. The
> identification is of complexes of sheaves of `𝒪`-modules.

```lean
def derivedSheafHom_coextendScalarsIso [I.IsKInjective] :
    DerivedCategory.Q.obj (sheafHomComplex X ((coeffRestrictComplex X O' φ₀).obj L) I).obj ≅
      DerivedCategory.Q.obj ((coeffRestrictComplex X O' φ₀).obj
        (sheafHomComplex (coeffSite X O') L ((coeffCoextendComplex X O' φ₀).obj I)).obj)
```

**`AlgebraicGeometry.RingedSite.coextHomComplexIso_hom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/HomIntoCoextension.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/HomIntoCoextension.lean#L505). The attribute's comment: “part (2)”.

> **The comparison of Tag 0996(2) is the canonical one.** On a local section it evaluates each
> local component of a cochain — a local morphism `𝒪'|_W ⟶ I|_W` — at the unit section, so it is
> not merely some isomorphism between the two complexes.

```lean
theorem coextHomComplexIso_hom_apply (U : X.C) (n p q : ℤ) (hpq : p + n = q)
    (t : ((coextSource X O' φ₀ L I).X n).val.obj (op U))
    {W : X.C} (g : W ⟶ U) (x : (L.X p).val.obj (op W)) :
    (((AddCommGrpCat.Hom.hom
        (((sheafHomComplex X ((coeffRestrictComplex X O' φ₀).obj L) I).sectionsIso U).hom.f n)
        ((((coextHomComplexIso X O' φ₀ L I).hom.f n).val.app (op U)).hom t)).v
          p q hpq).val.app (op (Over.mk g))) x =
      invSecVal (coeffHom X O' φ₀).hom (I.X q).val (op W)
        ((((AddCommGrpCat.Hom.hom
          (((sheafHomComplex (coeffSite X O') L
            ((coeffCoextendComplex X O' φ₀).obj I)).sectionsIso U).hom.f n) t).v
            p q hpq).val.app (op (Over.mk g))) x)
```

**`AlgebraicGeometry.RingedSite.derivedSheafHom_awayRestrictScalarsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationAtGlobalSection.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationAtGlobalSection.lean#L181). The attribute's comment: “part (1)”.

> Let `(𝒞, 𝒪)` be a ringed site and let `f` be a global section of `𝒪`. For
> `L, N ∈ D(𝒪_f)` we have `R SheafHom_𝒪(L, N) = R SheafHom_{𝒪_f}(L, N)`: computing `N` by a
> K-injective complex `I` of sheaves of `𝒪_f`-modules, the internal Hom complex over `𝒪` of the
> restrictions of `L` and `I` is, as a complex of sheaves of `𝒪`-modules, the restriction of the
> internal Hom complex over `𝒪_f` of `L` and `I`.

```lean
def derivedSheafHom_awayRestrictScalarsIso (X : RingedSite.{u, u, u})
    (h : Presheaf.globalSections (X.O.obj ⋙ forget CommRingCat.{u}))
    (L I : CochainComplex (SheafOfModules.{u}
      ((sheafCompose X.J (forget₂ CommRingCat RingCat)).obj (awaySheaf h))) ℤ)
    [I.IsKInjective] :
    let Xh : RingedSite.{u, u, u} := { C := X.C, J := X.J, O := awaySheaf h }
    let R := SheafOfModules.restrictScalars.{u}
      ((sheafCompose X.J (forget₂ CommRingCat RingCat)).map (toAwaySheaf h))
    let LR := (R.mapHomologicalComplex (.up ℤ)).obj L
    let IR := (R.mapHomologicalComplex (.up ℤ)).obj I
    DerivedCategory.Q.obj (sheafHomComplex X LR IR).obj ≅
      DerivedCategory.Q.obj
        ((R.mapHomologicalComplex (.up ℤ)).obj (sheafHomComplex Xh L I).obj)
```

**`AlgebraicGeometry.RingedSite.derivedSheafHom_awayRestrictScalarsIso_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationAtGlobalSection.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationAtGlobalSection.lean#L201). The attribute's comment: “part (1)”.

> The comparison `derivedSheafHom_awayRestrictScalarsIso` is induced by the isomorphism of
> internal Hom complexes that leaves every local module homomorphism unchanged.

```lean
theorem derivedSheafHom_awayRestrictScalarsIso_canonical (X : RingedSite.{u, u, u})
    (h : Presheaf.globalSections (X.O.obj ⋙ forget CommRingCat.{u}))
    (L I : CochainComplex (SheafOfModules.{u}
      ((sheafCompose X.J (forget₂ CommRingCat RingCat)).obj (awaySheaf h))) ℤ)
    [I.IsKInjective] :
    let Xh : RingedSite.{u, u, u} := { C := X.C, J := X.J, O := awaySheaf h }
    let R := SheafOfModules.restrictScalars.{u}
      ((sheafCompose X.J (forget₂ CommRingCat RingCat)).map (toAwaySheaf h))
    let LR := (R.mapHomologicalComplex (.up ℤ)).obj L
    let IR := (R.mapHomologicalComplex (.up ℤ)).obj I
    ∃ c : (sheafHomComplex X LR IR).obj ≅
        (R.mapHomologicalComplex (.up ℤ)).obj (sheafHomComplex Xh L I).obj,
      (DerivedCategory.Q.mapIso c = derivedSheafHom_awayRestrictScalarsIso X h L I) ∧
      (∀ (U : X.C) (n p q : ℤ) (hpq : p + n = q)
          (s : ((sheafHomComplex X LR IR).obj.X n).val.obj (op U))
          {W : X.C} (g : W ⟶ U) (x : (L.X p).val.obj (op W)),
        (((AddCommGrpCat.Hom.hom
            (((sheafHomComplex Xh L I).sectionsIso U).hom.f n)
            ((c.hom.f n).val.app (op U) s)).v p q hpq).val.app
              (op (Over.mk g))) x =
          (((AddCommGrpCat.Hom.hom
            (((sheafHomComplex X LR IR).sectionsIso U).hom.f n) s).v p q hpq).val.app
              (op (Over.mk g))) x)
```

**`AlgebraicGeometry.RingedSite.sheafHomComplex_awayLocalizedAction_agree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationAtGlobalSection.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationAtGlobalSection.lean#L232). The attribute's comment: “part (1)”.

> The two `𝒪_f`-structures on `R SheafHom_𝒪(L, N)` agree: acting by a local section of `𝒪_f`
> on the source of a local Hom and acting by it on the target give the same section of the
> internal Hom complex.

```lean
theorem sheafHomComplex_awayLocalizedAction_agree (X : RingedSite.{u, u, u})
    (h : Presheaf.globalSections (X.O.obj ⋙ forget CommRingCat.{u}))
    (L I : CochainComplex (SheafOfModules.{u}
      ((sheafCompose X.J (forget₂ CommRingCat RingCat)).obj (awaySheaf h))) ℤ) :
    let _Xh : RingedSite.{u, u, u} := { C := X.C, J := X.J, O := awaySheaf h }
    let R := SheafOfModules.restrictScalars.{u}
      ((sheafCompose X.J (forget₂ CommRingCat RingCat)).map (toAwaySheaf h))
    let LR := (R.mapHomologicalComplex (.up ℤ)).obj L
    let IR := (R.mapHomologicalComplex (.up ℤ)).obj I
    ∀ (U : X.C)
      (r : ((sheafCompose X.J (forget₂ CommRingCat RingCat)).obj
        (awaySheaf h)).obj.obj (op U))
      (n p q : ℤ) (hpq : p + n = q)
      (s : ((sheafHomComplex X LR IR).obj.X n).val.obj (op U))
      {W : X.C} (g : W ⟶ U) (x : (L.X p).val.obj (op W)),
      (((AddCommGrpCat.Hom.hom
        (((sheafHomComplex X LR IR).sectionsIso U).hom.f n) s).v p q hpq).val.app
          (op (Over.mk g)))
            (((L.X p).val.obj (op W)).isModule.smul
              (((sheafCompose X.J (forget₂ CommRingCat RingCat)).obj
                (awaySheaf h)).obj.map g.op r) x) =
        ((I.X q).val.obj (op W)).isModule.smul
          (((sheafCompose X.J (forget₂ CommRingCat RingCat)).obj
            (awaySheaf h)).obj.map g.op r)
          (show (I.X q).val.obj (op W) from (((AddCommGrpCat.Hom.hom
            (((sheafHomComplex X LR IR).sectionsIso U).hom.f n) s).v p q hpq).val.app
              (op (Over.mk g))) x)
```

## Tag 0997, a lemma

[Tag 0997](https://stacks.math.columbia.edu/tag/0997) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isZero_derivedSheafHom_derivedAwayModule_of_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingCriterion.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingCriterion.lean#L143). The attribute's comment: “(2) ⇒ (1)”.

> If `R𝑆heafHom_𝒪(L, K)` vanishes for every object `L` of `D(𝒪_f)`, viewed as an object of
> `D(𝒪)` by restriction of scalars, then `R𝑆heafHom_𝒪(𝒪_f, K)` vanishes.

```lean
theorem isZero_derivedSheafHom_derivedAwayModule_of_forall
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (H : ∀ L : DerivedCategory
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (awayRingedSite X h).O)),
      IsZero (((derivedSheafHomBifunctor X).obj
        (op ((awayRestrictScalarsDerived X h).obj L))).obj K)) :
    IsZero (((derivedSheafHomBifunctor X).obj (op (derivedAwayModule X h))).obj K)
```

**`AlgebraicGeometry.RingedSite.isZero_derivedSheafHom_awayRestrictScalars_of_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingCriterionCoextension.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingCriterionCoextension.lean#L137). The attribute's comment: “(1) ⇒ (2)”.

> Let `(𝒞, 𝒪)` be a ringed site, let `f` be a global section of `𝒪` and let `K ∈ D(𝒪)`. If
> `R𝑆heafHom_𝒪(𝒪_f, K)` vanishes, then `R𝑆heafHom_𝒪(L, K)` vanishes for every object `L` of
> `D(𝒪_f)`, viewed as an object of `D(𝒪)` by restriction of scalars.

```lean
theorem isZero_derivedSheafHom_awayRestrictScalars_of_isZero
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : IsZero (((derivedSheafHomBifunctor X).obj (op (derivedAwayModule X h))).obj K))
    (L : DerivedCategory
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (awayRingedSite X h).O))) :
    IsZero (((derivedSheafHomBifunctor X).obj
      (op ((awayRestrictScalarsDerived X h).obj L))).obj K)
```

**`AlgebraicGeometry.RingedSite.isZero_derivedSheafHom_derivedAwayModule_iff_isDerivedCompleteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingCriterionTelescope.lean, line 608](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingCriterionTelescope.lean#L608). The attribute's comment: “(1) ⇔ (3)”.

> **[Stacks, Tag 0997], the equivalence of (1) and (3)**: the derived internal Hom
> `R𝑆heafHom_𝒪(𝒪_f, K)` vanishes if and only if `T(K, f) = 0`.
>
> Derived internal Hom into `K` carries the triangle of the telescope resolution of `𝒪_f` to a
> distinguished triangle whose first vertex is `R𝑆heafHom_𝒪(𝒪_f, K)`, so that vertex vanishes
> exactly when the second morphism of the triangle is invertible; under the identification
> `R𝑆heafHom_𝒪(∐ₙ 𝒪, K) ≅ ∏ₙ K` that morphism is the Milnor difference map `1 - f·shift`, whose
> invertibility is `T(K, f) = 0` by definition.

```lean
theorem isZero_derivedSheafHom_derivedAwayModule_iff_isDerivedCompleteAt :
    IsZero (((derivedSheafHomBifunctor X).obj (op (derivedAwayModule X h))).obj K) ↔
      IsDerivedCompleteAt K (awaySmul X h)
```

**`AlgebraicGeometry.RingedSite.memVanishingIdeal_iff_isDerivedCompleteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingFromComplete.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingFromComplete.lean#L320). The attribute's comment: “(1) ⇔ (3)”.

> **[Stacks, Tag 0997], the equivalence of conditions (1) and (3).** For a global section `f`
> of `𝒪` and `K ∈ D(𝒪)`, the derived internal Hom `R𝑆heafHom_𝒪(𝒪_f, K)` vanishes exactly when
> `T(K, f) = 0`, that is exactly when the Milnor difference map `1 - f·shift` is invertible on
> `∏ₙ K`.
>
> The proof is the source's: `𝒪_f` is the colimit of `𝒪 --f--> 𝒪 --f--> ⋯`
> (`AlgebraicGeometry.RingedSite.isColimitAwayModuleCocone`), so the mapping telescope resolves it
> by countable direct sums of copies of `𝒪`
> (`Stacks.MappingTelescope.telescope_shortExact_general`); derived internal Hom into `K` turns
> that short exact sequence into a distinguished triangle
> (`AlgebraicGeometry.RingedSite.exists_distinguished_derivedSheafHom`, the contravariant half of
> [Stacks, Tag 08JC]) whose second and third vertices are `∏ₙ K` and whose first vertex is
> `R𝑆heafHom_𝒪(𝒪_f, K)`; and the map between them is `1 - f·shift`, because derived internal Hom
> is `𝒪`-linear in its contravariant variable. The first vertex of a distinguished triangle
> vanishes exactly when the opposite map is invertible.

```lean
theorem memVanishingIdeal_iff_isDerivedCompleteAt :
    MemVanishingIdeal X K h ↔
      IsDerivedCompleteAt K
        (Stacks.SheafOfModules.globalSectionToEnd (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
            (awayFamily X h))
```

## Tag 0998, a lemma

[Tag 0998](https://stacks.math.columbia.edu/tag/0998) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.memVanishingIdeal_mulGlobalSection_of_memVanishingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayAddShortExact.lean, line 574](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayAddShortExact.lean#L574). The attribute's comment: “closure under multiplication, at the membership condition”.

> **The vanishing locus is closed under multiplication, at the tag's own membership
> condition.** If `f` lies in the vanishing locus of `K` then so does `gf`, for every global
> section `g` of `𝒪`.
>
> This is `AlgebraicGeometry.RingedSite.isRightOrthogonalAway_mulGlobalSection` read through the
> implication (1) ⇒ (2) of [Stacks, Tag 0997],
> `AlgebraicGeometry.RingedSite.isZero_derivedSheafHom_awayRestrictScalars_of_isZero`, which turns
> membership into right orthogonality; the converse direction is
> `AlgebraicGeometry.RingedSite.MemVanishingIdeal.of_isRightOrthogonalAway`.
>
> It is stated here rather than beside `isRightOrthogonalAway_mulGlobalSection` in
> `VanishingIdeal.lean` because it is the one declaration of that file needing
> `VanishingCriterionCoextension.lean`, and that import reaches `Completion.lean`, whose consumer
> `AlgebraicGeometry.RingedSite.completionFunctor_obj_eq_derivedSheafHom_flip` of
> `KoszulLimitFormula.lean` then fails to discharge its `omit` clause.

```lean
theorem memVanishingIdeal_mulGlobalSection_of_memVanishingIdeal
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (g h : Presheaf.globalSections (X.O.obj ⋙ forget CommRingCat.{u}))
    (H : MemVanishingIdeal X K h) :
    MemVanishingIdeal X K (mulGlobalSection X g h)
```

**`AlgebraicGeometry.RingedSite.memVanishingIdeal_addGlobalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayAddShortExact.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AwayAddShortExact.lean#L595). The attribute's comment: “closure under addition”.

> **The vanishing locus is closed under addition.** If `R𝑆heafHom_𝒪(𝒪_a, K)` and
> `R𝑆heafHom_𝒪(𝒪_b, K)` vanish then so does `R𝑆heafHom_𝒪(𝒪_{a + b}, K)`.
>
> Write `h = a + b`. Multiplicativity — `isRightOrthogonalAway_mulGlobalSection` together with the
> implication (1) ⇒ (2) of [Stacks, Tag 0997], `isZero_derivedSheafHom_awayRestrictScalars_of_isZero`
> — puts the three products `ha`, `hb` and `hab` in the locus, and the short exact sequence
> `0 → 𝒪_h → 𝒪_{ha} ⊕ 𝒪_{hb} → 𝒪_{hab} → 0` of
> `AlgebraicGeometry.RingedSite.shortExact_awayModuleAddComplex` then puts `h` there by the
> dévissage `AlgebraicGeometry.RingedSite.isZero_derivedSheafHom_of_shortExact`, the middle term
> being handled by `AlgebraicGeometry.RingedSite.isZero_derivedSheafHom_biprod`.
>
> Nothing is assumed of `K`, of `a` or of `b`.

```lean
theorem memVanishingIdeal_addGlobalSection
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (a b : Presheaf.globalSections (X.O.obj ⋙ forget CommRingCat.{u}))
    (Ha : MemVanishingIdeal X K a) (Hb : MemVanishingIdeal X K b) :
    MemVanishingIdeal X K (addGlobalSection X a b)
```

**`AlgebraicGeometry.RingedSite.memVanishingIdeal_over_of_memVanishingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/SliceRestrictionDescent.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/SliceRestrictionDescent.lean#L256). The attribute's comment: “the vanishing locus is stable under restriction to a slice site”.

> **[Stacks, Tag 0998], restriction stability of the vanishing locus.** If the global section
> `f` of `𝒪` lies in the vanishing locus of `K`, then its restriction `f|_U` lies in the vanishing
> locus of `K|_U` over the slice site `𝒞/U`.
>
> Membership of `f|_U` in the locus of `K|_U` is the vanishing of `R𝑆heafHom_{𝒪_U}((𝒪_f)|_U, K|_U)`
> by `AlgebraicGeometry.RingedSite.memVanishingIdeal_over_iff_isZero_derivedSheafHom_overFunctor`,
> whose input is the base change `(𝒪_f)|_U ≅ (𝒪_U)_{f|_U}`; and that object is the restriction of
> `R𝑆heafHom_𝒪(𝒪_f, K)` by [Stacks, Tag 08JB]. Restriction is additive, so it carries the
> vanishing upstairs to the vanishing downstairs.

```lean
theorem memVanishingIdeal_over_of_memVanishingIdeal
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : MemVanishingIdeal X K h) :
    MemVanishingIdeal (X.over U)
      ((SheafOfModules.overFunctor.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.obj K)
      (globalSectionOver X U h)
```

**`AlgebraicGeometry.RingedSite.isRightOrthogonalAway_mulGlobalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingIdeal.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingIdeal.lean#L453). The attribute's comment: “closure under multiplication, for the right-orthogonality condition of 0997”.

> **The vanishing locus is closed under multiplication.** If `K` is right orthogonal to
> `D(𝒪_f)` and `g` is any global section of `𝒪`, then `K` is right orthogonal to `D(𝒪_{gf})`.
> This is the first half of the proof of [Stacks, Tag 0998]: the source observes that `𝒪_{gf}` is
> an `𝒪_f`-module, which here is the factorization of `𝒪 ⟶ 𝒪_{gf}` through `𝒪_f`.

```lean
theorem isRightOrthogonalAway_mulGlobalSection
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (g h : Presheaf.globalSections (X.O.obj ⋙ forget CommRingCat.{u}))
    (H : IsRightOrthogonalAway X K h) :
    IsRightOrthogonalAway X K (mulGlobalSection X g h)
```

**`AlgebraicGeometry.RingedSite.memVanishingIdeal_of_coversTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingIdealLocal.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingIdealLocal.lean#L163). The attribute's comment: “the sheaf condition: membership in the vanishing locus is local on a family of objects covering the final object of the site”.

> **[Stacks, Tag 0998], the sheaf condition for the vanishing locus.** Let `V : ι → 𝒞` be a
> family of objects covering the final object of the site. If the restriction `f|_{V i}` lies in
> the vanishing locus of `K|_{V i}` for every `i`, then `f` lies in the vanishing locus of `K`.
>
> This is the verification the source omits. Membership of `f|_{V i}` in the locus of `K|_{V i}` is
> the vanishing of `R𝑆heafHom_{𝒪_{V i}}((𝒪_f)|_{V i}, K|_{V i})` by
> `AlgebraicGeometry.RingedSite.memVanishingIdeal_over_iff_isZero_derivedSheafHom_overFunctor`, and
> that object is the restriction of `R𝑆heafHom_𝒪(𝒪_f, K)` by [Stacks, Tag 08JB]. So the hypothesis
> says that `R𝑆heafHom_𝒪(𝒪_f, K)` vanishes on each member of the covering family, and
> `isZero_of_coversTop_overFunctor_mapDerivedCategory` concludes that it vanishes.
>
> Nothing is assumed of `K`, of `f` or of the site. The converse implication, at a single object
> and with no covering, is
> `AlgebraicGeometry.RingedSite.memVanishingIdeal_over_of_memVanishingIdeal`.

```lean
theorem memVanishingIdeal_of_coversTop
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {ι : Type*} {V : ι → X.C} (hV : X.J.CoversTop V)
    (hK : ∀ i, MemVanishingIdeal (X.over (V i))
      ((SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        (V i)).mapDerivedCategory.obj K)
      (globalSectionOver X (V i) h)) :
    MemVanishingIdeal X K h
```

**`AlgebraicGeometry.RingedSite.derivedCompleteIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingIdealSheafCondition.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/VanishingIdealSheafCondition.lean#L345).

> **[Stacks, Tag 0998]: the sections `f` of `𝒪` with `T(K|_U, f) = 0` form a sheaf of ideals
> in `𝒪`.** For a ringed site `(𝒞, 𝒪)` and `K ∈ D(𝒪)`, the rule sending an object `U` of `𝒞` to
> `{f ∈ 𝒪(U) | T(K|_U, f) = 0}` is a sheaf of ideals: the value at each object is an ideal
> (`AlgebraicGeometry.RingedSite.derivedCompleteIdealAt`), the values are stable under
> restriction (`AlgebraicGeometry.RingedSite.IsDerivedCompleteAtSection.restrict`), and
> membership is local (`AlgebraicGeometry.RingedSite.IsDerivedCompleteAtSection.of_sieve`).

```lean
def derivedCompleteIdealSheaf :
    SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
```

## Tag 0999, a definition

[Tag 0999](https://stacks.math.columbia.edu/tag/0999) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.IsDerivedComplete`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/Basic.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/Basic.lean#L118).

> Derived completeness of a complex of sheaves of modules along an ideal sheaf.

```lean
def IsDerivedComplete (X : RingedSite.{u, v, r})
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (K : DerivedCategory
      (SheafOfModules.{max u v w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) : Prop
```

## Tag 099A, a lemma

[Tag 099A](https://stacks.math.columbia.edu/tag/099A) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isDerivedComplete_derivedSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/DerivedHomComplete.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/DerivedHomComplete.lean#L158).

> **Stacks 099A.** Let `(𝒞, 𝒪)` be a ringed site and `ℐ ⊂ 𝒪` a sheaf of ideals. For every
> `K ∈ D(𝒪)` — arbitrary, with no finiteness or boundedness assumed — and every derived-complete
> `L ∈ D(𝒪)`, the object `R𝑆heafHom_𝒪(K, L)` is derived complete along the same `ℐ`.
>
> Derived completeness is tested slice by slice. On the slice site over `U`, restriction commutes
> with derived internal Hom by [Stacks, Tag 08JB], so the object to be tested is
> `R𝑆heafHom_{𝒪_U}(K|_U, L|_U)`; and `L|_U` passes the test by hypothesis. That functor is
> additive and takes multiplication by `f` to multiplication by `f`, both proved in
> `StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomAdditive.lean`, and it
> preserves the countable power of `L|_U` by
> `AlgebraicGeometry.RingedSite.preservesLimit_derivedSheafHom`. Together these let it carry the
> Milnor difference map, hence the test, from `L|_U` to its value.

```lean
theorem isDerivedComplete_derivedSheafHom
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (K L : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (hL : IsDerivedComplete.{u, u, u, u} X I L) :
    IsDerivedComplete.{u, u, u, u} X I
      (((derivedSheafHomBifunctor X).obj (op K)).obj L)
```

## Tag 099C, a lemma

[Tag 099C](https://stacks.math.columbia.edu/tag/099C) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedRestrictScalars.isDerivedComplete_restrictScalars_of_extendIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/RestrictScalars.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/RestrictScalars.lean#L463). The attribute's comment: “the inclusion D\_comp(𝒪', ℐ𝒪') ⊆ the inverse image of D\_comp(𝒪, ℐ)”.

> **[Stacks, Tag 099C], the inclusion `D_comp(𝒪', ℐ𝒪') ⊆` the inverse image of
> `D_comp(𝒪, ℐ)`.** A complex of `𝒪'`-modules which is derived complete along the extension
> `ℐ𝒪'` of a sheaf of ideals `ℐ ⊂ 𝒪` restricts to a complex of `𝒪`-modules which is derived
> complete along `ℐ`.
>
> A local section `f` of `ℐ` has its image in `ℐ𝒪'` by `extendIdeal`, so the hypothesis gives
> `T(E|_U, f) = 0` computed over `𝒪'`. Restriction of scalars commutes with restriction to the
> slice site over `U`, and it carries multiplication by the image of `f` to multiplication by `f`,
> so the two difference maps `1 - f·shift` correspond; since restriction of scalars commutes with
> the countable products of the derived categories, invertibility transfers.

```lean
theorem isDerivedComplete_restrictScalars_of_extendIdeal (α : O ⟶ O')
    (I : _root_.SheafOfModules.Submodule
      (_root_.SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf (ringedSite J O).O))))
    (E : DerivedCategory
      (_root_.SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (ringedSite J O').O))))
    (h : RingedSite.IsDerivedComplete.{u, u, u, u} (ringedSite J O')
      (RingedSite.extendIdeal (ringSheafHom (O := O) (O' := O') α) I) E) :
    RingedSite.IsDerivedComplete.{u, u, u, u} (ringedSite J O) I
      ((_root_.SheafOfModules.restrictScalars.{u}
        (ringSheafHom (O := O) (O' := O') α)).mapDerivedCategory.obj E)
```

**`Stacks.SheafOfModules.DerivedRestrictScalars.isDerivedComplete_restrictScalars_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/RestrictScalarsConverse.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/RestrictScalarsConverse.lean#L232).

> **[Stacks, Tag 099C].** For a homomorphism `𝒪 ⟶ 𝒪'` of sheaves of commutative rings on a
> site and a sheaf of ideals `ℐ ⊂ 𝒪`, a complex of `𝒪'`-modules restricts to a complex of
> `𝒪`-modules derived complete along `ℐ` if and only if it is derived complete along `ℐ𝒪'`. That
> is, the inverse image of `D_comp(𝒪, ℐ)` under the restriction functor `D(𝒪') ⟶ D(𝒪)` is
> `D_comp(𝒪', ℐ𝒪')`.

```lean
theorem isDerivedComplete_restrictScalars_iff (α : O ⟶ O')
    (I : _root_.SheafOfModules.Submodule
      (_root_.SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf (ringedSite J O).O))))
    (E : DerivedCategory
      (_root_.SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (ringedSite J O').O)))) :
    RingedSite.IsDerivedComplete.{u, u, u, u} (ringedSite J O) I
        ((_root_.SheafOfModules.restrictScalars.{u}
          (ringSheafHom (O := O) (O' := O') α)).mapDerivedCategory.obj E) ↔
      RingedSite.IsDerivedComplete.{u, u, u, u} (ringedSite J O')
        (RingedSite.extendIdeal (ringSheafHom (O := O) (O' := O') α) I) E
```

## Tag 099J, a lemma

[Tag 099J](https://stacks.math.columbia.edu/tag/099J) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.derivedPushforward_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardTopoi.lean, line 503](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardTopoi.lean#L503).

> **[Stacks, Tag 099J].** Let `f : (Sh(𝒞), 𝒪_X) ⟶ (Sh(𝒟), 𝒪_Y)` be a morphism of ringed topoi
> and let `ℐ' ⊂ 𝒪_X` and `ℐ ⊂ 𝒪_Y` be sheaves of ideals such that `f^♯` sends `f⁻¹ℐ` into `ℐ'`, that
> is, such that the composite `f⁻¹ℐ ⟶ f⁻¹𝒪_Y ⟶ 𝒪_X` of the inverse image of the inclusion with the
> structure map factors through `ℐ' ⊂ 𝒪_X`. Then `Rf_*` sends `D_comp(𝒪_X, ℐ')` into
> `D_comp(𝒪_Y, ℐ)`.
>
> The proof reduces to morphisms of ringed sites by [Stacks, Tag 03CR]; see the module
> docstring.

```lean
theorem derivedPushforward_isDerivedComplete (f : RingedToposHom.{u, u, u, u, u, u} X Y)
    (I : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf Y.toRingedSite.O))))
    (I' : SheafOfModules.Submodule
      (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.toRingedSite.O))))
    (hI : ∃ φ : f.toToposHom.inverseImage.obj
        ((Sheaf.moduleSheafFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf Y.toRingedSite.O))).obj
          I.toSheafOfModules) ⟶
        (Sheaf.moduleSheafFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.toRingedSite.O))).obj
          I'.toSheafOfModules,
      f.toToposHom.inverseImage.map
          ((Sheaf.moduleSheafFunctor
            ((Stacks.SheafOfModules.Tensor.ringSheaf Y.toRingedSite.O))).map I.ι) ≫
        X.forgetRing.map f.fSharpInverseImage =
      φ ≫ (Sheaf.moduleSheafFunctor
        ((Stacks.SheafOfModules.Tensor.ringSheaf X.toRingedSite.O))).map I'.ι)
    (K : DerivedCategory
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := X.J)) X.O)))
    (hK : RingedSite.IsDerivedComplete.{u, u, u, u} X.toRingedSite I' K) :
    RingedSite.IsDerivedComplete.{u, u, u, u} Y.toRingedSite I
      ((Stacks.Cohomology.DerivedPushforward.derivedPushforward.{u, u, u, u, u, u} f).obj K)
```

## Tag 099B, a lemma

[Tag 099B](https://stacks.math.columbia.edu/tag/099B) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_idealOfGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletionIdempotent.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletionIdempotent.lean#L494). The attribute's comment: “the conclusion — for `ℐ` the ideal sheaf generated by the global sections `f_1, …, f_r`, the inclusion `D_comp(𝒪) ⥤ D(𝒪)` has a left adjoint. The tag's formula for that adjoint is `bijective_precomp_completionUnit_idealOfGlobalSections`”.

> **[Stacks, Tag 099F] for the ideal sheaf generated by finitely many global sections, with no
> hypothesis left.** For a ringed site `(𝒞, 𝒪)` and global sections `f_1, …, f_r` of `𝒪`, the
> inclusion of the objects of `D(𝒪)` derived complete along `ℐ = (f_1, …, f_r)` into `D(𝒪)` has a
> left adjoint; the adjoint is the Čech completion functor `Φ K = R𝑆heafHom_𝒪(Č(f), K)` of
> `Completion.lean`, and all three clauses its universal property was reduced to are now
> discharged — clause 1 by `isDerivedComplete_completionFunctor`, clause 2 by
> `isIso_completionUnit_app_of_isDerivedComplete` of `CompletionUnitIso.lean`, clause 3 by
> `completionFunctor_map_completionUnit_app`.
>
> The `@[stacks 099F]` attribute is *not* attached. The source states that proposition for an
> arbitrary **finite type** sheaf of ideals, that is one which is only *locally* generated by
> finitely many sections; an ideal sheaf generated by finitely many *global* sections is a special
> case of that, and the general case is
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete` of `FiniteTypeReflector.lean`.
> What
> *is* at the source's generality here is [Stacks, Tag 099B], whose hypothesis is exactly that
> `ℐ` be generated by finitely many global sections; the attribute for that tag is attached, to
> this statement and to `bijective_precomp_completionUnit_idealOfGlobalSections` below, which
> carry its two halves.

```lean
theorem isRightAdjoint_ι_isDerivedComplete_idealOfGlobalSections :
    (ObjectProperty.ι
      (IsDerivedComplete.{u, u, u, u} X (idealOfGlobalSections X f))).IsRightAdjoint
```

**`AlgebraicGeometry.RingedSite.bijective_precomp_completionUnit_idealOfGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletionIdempotent.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletionIdempotent.lean#L516). The attribute's comment: “the tag's formula for the left adjoint: `K^∧ = R𝑆heafHom_𝒪(Č(f), K)`, with precomposition by `K ⟶ K^∧` bijective on morphisms into a derived-complete object”.

> **The Čech complex computes the left adjoint of [Stacks, Tag 099B]**, which is the formula
> the tag gives alongside the existence statement: for `ℐ = (f_1, …, f_r)`, every `K` and every
> derived-complete `Z`, precomposition with the completion map `η_K : K ⟶ K^∧` is a bijection
> `Hom_{D(𝒪)}(K^∧, Z) ⟶ Hom_{D(𝒪)}(K, Z)`, where
> `K^∧ = R𝑆heafHom_𝒪(Č(f), K)` is `AlgebraicGeometry.RingedSite.completionFunctor` and `η` is
> `AlgebraicGeometry.RingedSite.completionUnit`, both of `Completion.lean`.
>
> This is `Stacks.Algebraization.bijective_precomp_completionUnit` with its two hypotheses
> discharged: `η_Z` is invertible on a derived-complete `Z` by clause 2
> (`isIso_completionUnit_app_of_isDerivedComplete_idealOfGlobalSections`), and `Φ η_K` is
> invertible with no hypothesis by `isIso_completionFunctor_map_completionUnit_app`. Clause 1 is
> not used, so the bijection does not depend on `isDerivedComplete_completionFunctor`; what
> clause 1 supplies is that `K^∧` is itself an object of `D_comp(𝒪)`, which is what turns the
> bijection into an adjunction.

```lean
theorem bijective_precomp_completionUnit_idealOfGlobalSections
    {Z : DerivedCategory
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O))}
    (hZ : IsDerivedComplete.{u, u, u, u} X (idealOfGlobalSections X f) Z) :
    Function.Bijective
      (fun g : (completionFunctor X f).obj L ⟶ Z ↦ (completionUnit X f).app L ≫ g)
```

**`AlgebraicGeometry.RingedSite.bijective_precomp_completionUnit_generatedIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealAdjoint.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealAdjoint.lean#L153). The attribute's comment: “the universal property of the Čech completion: precomposition with `K ⟶ K^∧` is bijective onto the morphisms into a derived-complete object”.

> **The universal property of the Čech completion**: for every `K` in `D(𝒪)` and every `E`
> derived complete along `ℐ = (f_1, …, f_r)`, precomposition with the completion map `K ⟶ K^∧` is a
> bijection
>
> `Hom_{D(𝒪)}(K^∧, E) ⟶ Hom_{D(𝒪)}(K, E)`,
>
> where `K^∧ = R𝑆heafHom_𝒪(Č(f), K)` is the Čech completion and the map `K ⟶ K^∧` is
> `completionUnit`.

```lean
theorem bijective_precomp_completionUnit_generatedIdealSheaf
    (K E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hE : IsDerivedComplete.{u, u, u, u} X (generatedIdealSheaf f) E) :
    Function.Bijective
      (fun g : (completionFunctor X f).obj K ⟶ E ↦ (completionUnit X f).app K ≫ g)
```

**`AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealAdjoint.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealAdjoint.lean#L182). The attribute's comment: “the existence of the left adjoint of the inclusion `D_comp(𝒪) ⥤ D(𝒪)`, at the ideal sheaf generated by the given global sections”.

> Let `(𝒞, 𝒪)` be a ringed site and let `f_1, …, f_r` be global sections of `𝒪`. The inclusion
> of the objects of `D(𝒪)` derived complete along `ℐ = (f_1, …, f_r)` into `D(𝒪)` has a left
> adjoint, namely the Čech completion `K ↦ R𝑆heafHom_𝒪(Č(f), K)`.

```lean
theorem isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf :
    (ObjectProperty.ι
      (IsDerivedComplete.{u, u, u, u} X (generatedIdealSheaf f))).IsRightAdjoint
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_generatedIdealSheaf_completionFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealComplete.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealComplete.lean#L441). The attribute's comment: “that the Čech completion `K^∧ = R𝑆heafHom_𝒪(Č(f), K)` lies in `D_comp(𝒪)`, at the ideal sheaf generated by the sections”.

> **The `hΦ` hypothesis of [Stacks, Tag 099F], discharged**: every Čech completion
> `K^∧ = R𝑆heafHom_𝒪(Č(f), K)` is derived complete along the ideal sheaf
> `ℐ = (f_1, …, f_r)` generated by the sections the Čech complex is built from.
>
> It is `memVanishingIdeal_completionFunctor_obj` — the vanishing at the generators — followed by
> `isDerivedComplete_generatedIdealSheaf_of_forall_memVanishingIdeal`, which raises the vanishing
> at the finitely many generators to the condition of [Stacks, Tag 0999] at every local section of
> `ℐ`. Nothing is assumed of `K`, of the sections or of the site.
>
> It is also the clause of [Stacks, Tag 099B] which asserts that the object `K^∧` the tag
> constructs lies in `D_comp(𝒪)`; the universal property that makes it the left adjoint is
> `AlgebraicGeometry.RingedSite.bijective_precomp_completionUnit_generatedIdealSheaf` of
> `GeneratedIdealAdjoint.lean`.

```lean
theorem isDerivedComplete_generatedIdealSheaf_completionFunctor_obj
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    IsDerivedComplete.{u, u, u, u} X (generatedIdealSheaf f) ((completionFunctor X f).obj K)
```

**`AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_of_forall_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/NilpotentIdeal.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/NilpotentIdeal.lean#L149). The attribute's comment: “the conclusion — the inclusion `D_comp(𝒪) ⥤ D(𝒪)` has a left adjoint — for a sheaf of ideals all of whose local sections are nilpotent, where that left adjoint is the identity. The source's hypothesis that `ℐ` be generated by finitely many global sections is not assumed; with that hypothesis the tag, including its Čech formula for the left adjoint, is carried by `CompletionIdempotent.lean`”.

> **The inclusion `D_comp(𝒪) ⥤ D(𝒪)` has a left adjoint when the local sections of `ℐ` are
> nilpotent.** Every object is then derived complete, so the identity functor together with the
> identity natural transformation is a derived completion functor.
>
> This is the conclusion of [Stacks, Tag 099B], under a hypothesis that is not the source's. The
> source asks that `ℐ` be the ideal sheaf generated by finitely many global sections
> `f_1, …, f_r`; that generation relation is *not* assumed here, so in that direction the
> statement is more general than the tag, and it is restricted in the other direction by the
> nilpotence of the sections. The explicit formula the tag also gives for the left adjoint,
> `K^∧ = R𝑆heafHom_𝒪(Č(f), K)`, is constructed as
> `AlgebraicGeometry.RingedSite.completionFunctor` and
> `AlgebraicGeometry.RingedSite.completionUnit` in
> `StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/Completion.lean` and is
> proved to be that left adjoint — *under* the tag's generation hypothesis — in
> `CompletionIdempotent.lean`. Under the nilpotence hypothesis of this statement the left adjoint
> is the identity, which is not that formula.

```lean
theorem isRightAdjoint_ι_isDerivedComplete_of_forall_isNilpotent
    (hI : ∀ (U : X.C) (f : ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj.obj (op U)),
      f ∈ I.toSubmodule.obj (op U) → IsNilpotent f) :
    (ObjectProperty.ι (IsDerivedComplete.{u, v, max u v, max u v} X I)).IsRightAdjoint
```

## Tag 0A0E, a lemma

[Tag 0A0E](https://stacks.math.columbia.edu/tag/0A0E) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_derivedCompletion_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/FiniteTypeKoszulFormula.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/FiniteTypeKoszulFormula.lean#L183). The attribute's comment: “the stated formula `K^∧ = R lim (K ⊗^𝐋_𝒪 K_n)` for the derived completion of `K ∈ D(𝒪)` along a sheaf of ideals `ℐ ⊂ 𝒪` **of finite type**, with `K^∧` the derived completion functor of [Stacks, Tag 099F] and `K_n` the Koszul complex on the powers of generators of `ℐ` in the cochain grading of the source's proof, that is the `𝒪`-dual of `AlgebraicGeometry.RingedSite.koszulPowerComplex`. The tower of the formula is built from a finite family of sections generating `ℐ`, which a finite-type ideal sheaf carries over the objects of a covering family, so the formula is stated over each object `U` carrying such a family `g_1, …, g_s`, where it reads `K^∧|_U = R lim (K|_U ⊗^𝐋_{𝒪_U} K_n(g))`; that those objects cover the site is `AlgebraicGeometry.RingedSite.exists_coversTop_eq_idealOfGlobalSections_overIdeal_of_isFiniteType`. `R lim` is a predicate rather than a functor, so the source's equality is read as the restriction being a derived limit of the tower. The finite-type hypothesis is the source's own, and the only one: the countable products and coproducts a derived limit needs in order to be written down are supplied here rather than assumed. The source's display at an ideal sheaf generated by finitely many global sections of `𝒪` is the companion registration `AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_completion`.”.

> **[Stacks, Tag 0A0E] at a sheaf of ideals of finite type.** Let `(𝒞, 𝒪)` be a ringed site, let
> `ℐ ⊂ 𝒪` be a sheaf of ideals of finite type and let `E ∈ D(𝒪)`. Let `U` be an object of `𝒞` and
> `g_1, …, g_s` sections of `𝒪` over `U` generating `ℐ|_U`. Then the derived completion `E^∧` of
> [Stacks, Tag 099F] satisfies
>
> `E^∧|_U = R lim (E|_U ⊗^𝐋_{𝒪_U} K_n)`,  `K_n = Hom_{𝒪_U}(K(𝒪_U, g_1^{n+1}, …, g_s^{n+1}), 𝒪_U)`,
>
> the derived tensor products of `E|_U` with the duals of the Koszul complexes on the positive
> powers of `g_1, …, g_s`.
>
> The Koszul complexes of the formula are formed from a finite family of sections generating the
> ideal sheaf, and a finite-type `ℐ` carries one only locally; the objects `U` that carry one cover
> the site, by
> `AlgebraicGeometry.RingedSite.exists_coversTop_eq_idealOfGlobalSections_overIdeal_of_isFiniteType`,
> and `exists_coversTop_isDerivedLimit_koszulPowerSystem_derivedCompletion`
> below states this formula over such a covering family. When `ℐ` is generated by finitely many
> global sections of `𝒪` the formula holds on `𝒞` itself; that is the source's own display,
> `AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_completion`.
>
> Three inputs, each proved: the identification of the reflector of [Stacks, Tag 099F] with
> `R𝑆heafHom_𝒪(K, -)` for the complex of [Stacks, Tag 099E]; the restriction of that to the slice
> over `U` as the Čech completion of [Stacks, Tag 099B] at `g`, which is
> `derivedCompletionOverIsoCompletionFunctor`; and the source's display on the ringed site
> `(𝒞/U, 𝒪_U)`, where `g_1, …, g_s` are global sections.

```lean
theorem isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_derivedCompletion_over
    (U : X.C) {s : ℕ}
    (g : Fin s → Presheaf.globalSections ((X.over U).O.obj ⋙ forget CommRingCat.{u}))
    (hg : idealOfGlobalSections (X.over U) g = overIdeal I U)
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    IsDerivedLimit
      (tensorDerivedDualSystem (X.over U)
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct (X.over U))
        (koszulPowerSystem (X.over U) g ⋙ DerivedCategory.Q)
        ((SheafOfModules.overFunctor.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U).mapDerivedCategory.obj E))
      ((SheafOfModules.overFunctor.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U).mapDerivedCategory.obj
        ((derivedCompletion X I).obj E))
```

**`AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/KoszulCechHomotopyColimit.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/KoszulCechHomotopyColimit.lean#L231). The attribute's comment: “the formula `K^∧ = R lim (K ⊗^L_O K_n)` for the derived completion along the ideal sheaf generated by global sections `f_1, …, f_r`, at the canonical derived tensor product, with the Koszul tower spelled as the duals `K_n^∨` of the Koszul complexes in degrees `0, …, r`, which is the spelling of Stacks 0A0A and the source's own `K_n`; the tower is indexed by `n : ℕ` carrying the exponent `n + 1`, the source's positive powers”.

> **[Stacks, Tag 0A0E].** Let `(𝒞, 𝒪)` be a ringed site, let `f_1, …, f_r` be global sections
> of `𝒪` and let `K` be an object of `D(𝒪)`. Then the derived completion
> `K^∧ = R𝑆heafHom_𝒪(Č(f), K)` of [Stacks, Tag 099B] along the ideal sheaf generated by
> `f_1, …, f_r` is a derived limit of the tower
>
> `n ↦ K ⊗^𝐋_𝒪 K_n^∨`, `K_n = K(𝒪, f_1^{n+1}, …, f_r^{n+1})`,
>
> the derived tensor product being the canonical one of [Stacks, Tag 06YU].
>
> The three inputs of
> `AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDualSystem_completionFunctor` are all
> discharged. The derived-colimit presentation of the Čech complex by the Koszul complexes is
> `AlgebraicGeometry.RingedSite.isHomotopyColimit_koszulPowerSystem`, which is [Stacks, Tag 0913]
> followed by [Stacks, Tag 0949]; the direct-sum comparison is
> `AlgebraicGeometry.RingedSite.isIso_derivedSheafHomSigmaComparison`; and clause 3 of
> [Stacks, Tag 08JJ] — the hypothesis `hdual` of that statement — is not needed at all. The proof
> of [Stacks, Tag 0A0A] uses that clause for one purpose only, an isomorphism of the tower
> `n ↦ K ⊗^𝐋_𝒪 K_n^∨` with the tower `n ↦ R𝑆heafHom_𝒪(K_n, K)`, and
> `AlgebraicGeometry.RingedSite.tensorDerivedDualSystemIsoOfPerfect` builds that isomorphism from
> the perfectness of the `K_n` alone, which is
> `AlgebraicGeometry.RingedSite.isPerfect_koszulPowerComplex`. The canonical map of
> [Stacks, Tag 08JD] therefore never enters.
>
> The tower is the one of `AlgebraicGeometry.RingedSite.tensorDerivedDualSystem`,
> `n ↦ K ⊗^𝐋_𝒪 K_n^∨` with `K_n` the Koszul complex in degrees `0, …, r`; that is the spelling
> in which [Stacks, Tag 0A0A] is stated, and it is the source's `K ⊗^𝐋_𝒪 K_n` for the source's
> `K_n`, which is the `𝒪`-dual of the complex in degrees `0, …, r` and so sits in degrees
> `-r, …, 0`, as the proof of the tag records.

```lean
theorem isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_canonical
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct ((koszulPowerSystem X f ⋙ DerivedCategory.Q).obj)]
    [HasProduct fun n : ℕ ↦
      (derivedSheafHomSystem X (koszulPowerSystem X f ⋙ DerivedCategory.Q) K).obj (op n)]
    [HasProduct fun n : ℕ ↦
      (tensorDerivedDualSystem X (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u} X)
        (koszulPowerSystem X f ⋙ DerivedCategory.Q) K).obj (op n)] :
    IsDerivedLimit (tensorDerivedDualSystem X
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct.{u} X)
        (koszulPowerSystem X f ⋙ DerivedCategory.Q) K)
      ((completionFunctor X f).obj K)
```

**`AlgebraicGeometry.RingedSite.isDerivedLimit_tensorKoszulComplex_completionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/KoszulCompletionFormula.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/KoszulCompletionFormula.lean#L102).

> Let `(𝒞, 𝒪)` be a ringed site, let `f_1, …, f_r` be global sections of `𝒪` and let `K ∈ D(𝒪)`.
> The derived completion `K^∧` of [Stacks, Tag 099B] along the ideal sheaf generated by `f_1, …, f_r`
> is `R lim (K ⊗^𝐋_𝒪 K_n)`, where `K_n` is the Koszul complex on `f_1^n, …, f_r^n` over `𝒪`, in
> degrees `-r, …, 0`.
>
> Here `K^∧` is `AlgebraicGeometry.RingedSite.completionFunctor X f`, the tower is indexed by the
> positive exponents `n + 1`, `K_{n+1}` is
> `AlgebraicGeometry.RingedSite.koszulNaiveDualComplex X f n` (the `n`-th member of
> `AlgebraicGeometry.RingedSite.koszulNaiveDualSystem X f`), `⊗^𝐋_𝒪` is the canonical derived tensor
> product, and `R lim` is read as the predicate `CategoryTheory.Pretriangulated.IsDerivedLimit`.

```lean
theorem isDerivedLimit_tensorKoszulComplex_completionFunctor
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    IsDerivedLimit
      (koszulNaiveDualSystem X f ⋙ DerivedCategory.Q ⋙
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct X).tensor.obj K)
      ((completionFunctor X f).obj K)
```

**`AlgebraicGeometry.RingedSite.isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/KoszulPerfectDual.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/KoszulPerfectDual.lean#L476). The attribute's comment: “the stated formula `K^∧ = R lim (K ⊗^𝐋_𝒪 K_n)` for the derived completion of `K ∈ D(𝒪)` along the ideal sheaf generated by global sections `f_1, …, f_r` of `𝒪`, with `K_n` the Koszul complex on `f_1^n, …, f_r^n` in the cochain grading of the source's proof, that is the `𝒪`-dual of `AlgebraicGeometry.RingedSite.koszulPowerComplex`. `R lim` is a predicate rather than a functor, so the source's equality is read as `K^∧` being a derived limit of the tower; the `HasProduct`/`HasCoproduct` arguments are what lets a derived limit be written down at all and always hold, by `AlgebraicGeometry.RingedSite.exists_isDerivedLimit_tensorDerivedDualSystem`. Nothing is assumed: both inputs of the source's proof are proved here.”.

> **[Stacks, Tag 0A0E].** Let `(𝒞, 𝒪)` be a ringed site, let `f_1, …, f_r` be global sections
> of `𝒪` and let `K ∈ D(𝒪)`. The derived completion
> `K^∧ = R𝑆heafHom_𝒪(Č(f), K)` of [Stacks, Tag 099B] along the ideal sheaf generated by
> `f_1, …, f_r` is a derived limit of the tower
>
> `n ↦ K ⊗^𝐋_𝒪 K_n`, `K_n = Hom_𝒪(K(𝒪, f_1^{n+1}, …, f_r^{n+1}), 𝒪)`,
>
> the derived tensor products of `K` with the duals of the Koszul complexes on the positive powers
> of `f_1, …, f_r`.
>
> The two inputs the source's proof uses are discharged, not assumed: the derived-colimit
> presentation of the Čech complex by the Koszul complexes is
> `AlgebraicGeometry.RingedSite.isHomotopyColimit_koszulPowerSystem` ([Stacks, Tag 0913] followed
> by [Stacks, Tag 0949]), and the identification of the tower with
> `n ↦ R𝑆heafHom_𝒪(K^n, K)` is `AlgebraicGeometry.RingedSite.koszulTensorDualSystemIso`, which
> goes through the interchange morphism of [Stacks, Tag 0BYU] rather than through clause 3 of
> [Stacks, Tag 08JJ] — see the implementation notes of this file.

```lean
theorem isDerivedLimit_tensorDerivedDualSystem_koszulPowerSystem_completion
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct ((koszulPowerSystem X f ⋙ DerivedCategory.Q).obj)]
    [HasProduct fun n : ℕ ↦ (derivedSheafHomSystem X
      (koszulPowerSystem X f ⋙ DerivedCategory.Q) K).obj (op n)]
    [HasProduct fun n : ℕ ↦ (tensorDerivedDualSystem X
      (Stacks.SheafOfModules.canonicalDerivedTensorProduct X)
      (koszulPowerSystem X f ⋙ DerivedCategory.Q) K).obj (op n)] :
    IsDerivedLimit (tensorDerivedDualSystem X
        (Stacks.SheafOfModules.canonicalDerivedTensorProduct X)
        (koszulPowerSystem X f ⋙ DerivedCategory.Q) K)
      ((completionFunctor X f).obj K)
```

## Tag 099D, a lemma

[Tag 099D](https://stacks.math.columbia.edu/tag/099D) in the Stacks Project.

**`Stacks.FunctorialCechFamily.exists_extendedCechObject_iso_over_augmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/FunctorialCechConditionD.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/FunctorialCechConditionD.lean#L70). The attribute's comment: “condition (d) for a pair with a chosen finite generating family”.

> **Condition (d) of tag 099D, for the extended Čech complex of a chosen generating family.**
> If `g₁, …, g_s` and `f₁, …, f_r` both generate the finitely generated ideal `I ⊆ A`, there is an
> isomorphism in `D(A)` from the extended alternating Čech complex on `f₁, …, f_r` to the one on
> `g₁, …, g_s`, carrying the augmentation of the former onto the augmentation of the latter.
>
> This is the field `Stacks.LocalCohomology.FunctorialCechData.exists_cech_iso`, read at
> `complex A I hI = extendedCechComplex g (ModuleCat.of A A)`. The isomorphism is
> `Stacks.IdealCechComplex.canonicalIso`, which lives in `D(A)`; condition (d), being itself a
> condition in `D(A)`, asks for nothing more.

```lean
theorem exists_extendedCechObject_iso_over_augmentation {A : Type u} [CommRing A] {r s : ℕ}
    (f : Fin r → A) (g : Fin s → A) (I : Ideal A)
    (hf : Ideal.span (Set.range f) = I) (hg : Ideal.span (Set.range g) = I) :
    ∃ e : extendedCechObject f (ModuleCat.of A A) ≅
        DerivedCategory.Q.obj (extendedCechComplex g (ModuleCat.of A A)),
      e.hom ≫ DerivedCategory.Q.map (extendedCechAugmentation g (ModuleCat.of A A)) ≫
          ((DerivedCategory.singleFunctorIsoCompQ (ModuleCat.{u} A) 0).app
            (ModuleCat.of A A)).inv =
        extendedCechAugmentationHom f (ModuleCat.of A A)
```

**`Stacks.LocalCohomology.nonempty_functorialCechData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/FunctorialCechDatumExists.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/FunctorialCechDatumExists.lean#L92). The attribute's comment: “for every ring A and finitely generated ideal I ⊆ A the complex K(A, I) of A-modules, its augmentation K(A, I) → A, and for every ring map A → B the map K(A, I) → K(B, IB), compatible with the augmentations and composing on the nose, with K(A, I) ⊗^𝐋\_A B → K(B, IB) an isomorphism in D(B) and with K(A, I) identified in D(A) over A with the extended alternating Čech complex on any finite generating family of I”.

> **[Stacks, Tag 099D].** There is a way to construct, for every commutative ring `A` and
> every finitely generated ideal `I ⊆ A`, a complex `K(A, I)` of `A`-modules, a map of complexes
> of `A`-modules `K(A, I) → A`, and for every ring map `φ : A → B` a map of complexes of
> `A`-modules `K(A, I) → K(B, IB)`, such that
>
> * (a) for `A → B` and `I ⊆ A` finitely generated the square formed by the two augmentations,
>   the map `K(A, I) → K(B, IB)` and `A → B` commutes;
> * (b) for `A → B → C` and `I ⊆ A` finitely generated the composition of
>   `K(A, I) → K(B, IB)` and `K(B, IB) → K(C, IC)` is the map `K(A, I) → K(C, IC)`;
> * (c) for `A → B` and `I ⊆ A` finitely generated the induced map
>   `K(A, I) ⊗^𝐋_A B → K(B, IB)` is an isomorphism in `D(B)`;
> * (d) if `I = (f₁, …, f_r) ⊆ A` then the extended alternating Čech complex on `f₁, …, f_r` is
>   isomorphic to `K(A, I)` in `D(A)` by an isomorphism commuting with the augmentations onto `A`.
>
> These are exactly the data `complex`, `augmentation`, `map` and the conditions
> `map_augmentation`, `map_map`, `isIso_derivedBaseChange`, `exists_cech_iso` of
> `Stacks.LocalCohomology.FunctorialCechData`.

```lean
theorem nonempty_functorialCechData : Nonempty FunctorialCechData.{u}
```

**`Stacks.LocalCohomology.exists_pairCechComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/FunctorialCechDatumExists.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/FunctorialCechDatumExists.lean#L129). The attribute's comment: “the complex K(A, I) of A-modules attached to the pair (A, I) alone, its augmentation K(A, I) → A, and for every ring map φ : A → B the map of complexes of A-modules K(A, I) → K(B, IB), with (a) the augmentation square commuting, (b) the maps composing on the nose, (c) K(A, I) ⊗^𝐋\_A B → K(B, IB) an isomorphism in D(B), and (d) for every finite generating family f₁, …, f\_r of I an isomorphism in D(A) over A from the extended alternating Čech complex on f₁, …, f\_r to K(A, I); the data and the conditions written out in the statement”.

> **[Stacks, Tag 099D], with the three data and the four conditions written out.** This is
> `Stacks.LocalCohomology.nonempty_functorialCechData` with the fields of
> `Stacks.LocalCohomology.FunctorialCechData` unfolded into the statement, so that nothing about
> the tag is hidden behind a structure.
>
> The three quantified data are the tag's items (1), (2), (3):
>
> * `K A I hI` is the complex of `A`-modules of item (1). It is a function of the pair `(A, I)`
>   alone: no generating family of `I` occurs among its arguments, and `hI : I.FG` is a proof, so
>   by proof irrelevance `K A I` is determined by `A` and `I`.
> * `aug A I hI : K A I hI ⟶ A[0]` is the map of complexes of item (2).
> * `mp A B φ I hI J hJ hφ : K A I hI ⟶ (K B J hJ)|_A` is the map of complexes of `A`-modules of
>   item (3), for `J = IB`. The ideal `IB` is passed as a separate `J` with the equation
>   `hφ : J = Ideal.map φ I`, which is the same data and lets (b) be stated without transporting
>   along `Ideal.map_map`.
>
> The four conjuncts are the tag's conditions (a), (b), (c), (d), in order:
>
> * (a) the square formed by `mp`, the two augmentations and `A → B` commutes;
> * (b) `mp` for `A → C` is `mp` for `A → B` followed by `mp` for `B → C`;
> * (c) the induced map `K(A, I) ⊗^𝐋_A B → K(B, IB)` is an isomorphism in `D(B)`;
> * (d) for **every** finite family `f₁, …, f_r` generating `I` there is an isomorphism in `D(A)`
>   from the extended alternating Čech complex on `f₁, …, f_r` to `K(A, I)` carrying its
>   augmentation onto the augmentation of `K(A, I)`.
>
> Conditions (a) and (b) are equalities of maps of complexes, not merely of their images in the
> derived category, which is what makes `K` a functor on the category of pairs.

```lean
theorem exists_pairCechComplex :
    ∃ (K : (A : Type u) → [CommRing A] → (I : Ideal A) → I.FG →
            CochainComplex (ModuleCat.{u} A) ℤ)
      (aug : (A : Type u) → [CommRing A] → (I : Ideal A) → (hI : I.FG) →
            (K A I hI ⟶
              (CochainComplex.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A A)))
      (mp : (A B : Type u) → [CommRing A] → [CommRing B] → (φ : A →+* B) → (I : Ideal A) →
            (hI : I.FG) → (J : Ideal B) → (hJ : J.FG) → J = I.map φ →
            (K A I hI ⟶ (CochainComplex.restrictScalars φ).obj (K B J hJ))),
      (∀ (A B : Type u) [CommRing A] [CommRing B] (φ : A →+* B) (I : Ideal A) (hI : I.FG)
          (J : Ideal B) (hJ : J.FG) (hφ : J = I.map φ),
          mp A B φ I hI J hJ hφ ≫ (CochainComplex.restrictScalars φ).map (aug B J hJ) =
            aug A I hI ≫ singleRingHom φ) ∧
      (∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C] (φ : A →+* B) (ψ : B →+* C)
          (I : Ideal A) (hI : I.FG) (J : Ideal B) (hJ : J.FG) (L : Ideal C) (hL : L.FG)
          (hφ : J = I.map φ) (hψ : L = J.map ψ),
          mp A C (ψ.comp φ) I hI L hL (by rw [hψ, hφ, Ideal.map_map]) =
            mp A B φ I hI J hJ hφ ≫
              (CochainComplex.restrictScalars φ).map (mp B C ψ J hJ L hL hψ) ≫
                (restrictScalarsCompComplexIso φ ψ).hom.app (K C L hL)) ∧
      (∀ (A B : Type u) [CommRing A] [CommRing B] (φ : A →+* B) (I : Ideal A) (hI : I.FG)
          (J : Ideal B) (hJ : J.FG) (hφ : J = I.map φ),
          IsIso (derivedBaseChange φ (mp A B φ I hI J hJ hφ))) ∧
      (∀ (A : Type u) [CommRing A] (r : ℕ) (f : Fin r → A) (I : Ideal A) (hI : I.FG),
          Ideal.span (Set.range f) = I →
          ∃ e : extendedCechObject f (ModuleCat.of A A) ≅ DerivedCategory.Q.obj (K A I hI),
            e.hom ≫ DerivedCategory.Q.map (aug A I hI) ≫
                ((DerivedCategory.singleFunctorIsoCompQ (ModuleCat.{u} A) 0).app
                  (ModuleCat.of A A)).inv =
              extendedCechAugmentationHom f (ModuleCat.of A A))
```

**`Stacks.CechRingBaseChange.cechModEmptyEquiv_modMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/RingBaseChange.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/RingBaseChange.lean#L233). The attribute's comment: “condition (a) for a pair with a chosen finite generating family”.

> **The augmentation square of tag 099D, condition (a).** In degree zero the change-of-rings
> map is `φ` itself: the degree-zero localization inverts nothing, and the identification of it
> with the ring carries the map onto `φ`.  The augmentations of the two Čech complexes are their
> degree-zero identifications with the rings, so this is the commutativity of the square they form
> with `φ`.

```lean
theorem cechModEmptyEquiv_modMap (φ : A →+* B) (f : Fin r → A)
    (x : Cech.cechMod f A (∅ : Finset (Fin r))) :
    Stacks.CechBaseChange.cechModEmptyEquiv (mapFamily φ f) B (modMap φ f ∅ x) =
      φ (Stacks.CechBaseChange.cechModEmptyEquiv f A x)
```

**`Stacks.CechRingBaseChange.termMap_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/RingBaseChange.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/RingBaseChange.lean#L284). The attribute's comment: “condition (a) for a pair with a chosen finite generating family”.

> **Condition (a) on the degree-zero term of the complex.**  The empty set is the only index
> of cardinality zero, so the degree-zero term of the Čech complex is the summand it indexes, and
> there the change-of-rings map is `φ`.

```lean
theorem termMap_zero (φ : A →+* B) (f : Fin r → A) (a : A) :
    termMap φ f 0 (DirectSum.lof A {t : Finset (Fin r) // t.card = 0}
        (fun t => Cech.cechMod f A t.1) ⟨∅, Finset.card_empty⟩
        (LocalizedModule.mkLinearMap (Cech.cechSub f (∅ : Finset (Fin r))) A a)) =
      DirectSum.lof B {t : Finset (Fin r) // t.card = 0}
        (fun t => Cech.cechMod (mapFamily φ f) B t.1) ⟨∅, Finset.card_empty⟩
        (LocalizedModule.mkLinearMap
          (Cech.cechSub (mapFamily φ f) (∅ : Finset (Fin r))) B (φ a))
```

**`Stacks.CechRingBaseChange.complexMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/RingBaseChange.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/RingBaseChange.lean#L317). The attribute's comment: “item (3) for a pair with a chosen finite generating family”.

> **Change of rings for the extended alternating Čech complex, tag 099D items (1)–(3) for a
> pair with a chosen finite generating family.** The complex is `C^•(f₁, …, f_r; A)`, the
> augmentation onto `A` is its degree-zero projection, and this is the map of complexes of
> `A`-modules onto `C^•(g₁, …, g_r; B)` for `g_i = φ(f_i)`.

```lean
def complexMap (φ : A →+* B) (f : Fin r → A) :
    Cech.cechComplex f A ⟶
      ((ModuleCat.restrictScalars φ).mapHomologicalComplex (ComplexShape.up ℕ)).obj
        (Cech.cechComplex (mapFamily φ f) B)
```

**`Stacks.CechRingBaseChange.complexMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/RingBaseChange.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/RingBaseChange.lean#L347). The attribute's comment: “condition (b) for a pair with a chosen finite generating family”.

> **Tag 099D, condition (b).** For `A → B → C` the composite of the change-of-rings maps for
> `φ : A → B` and `ψ : B → C` is the change-of-rings map for `ψ ∘ φ`.

```lean
theorem complexMap_comp (φ : A →+* B) (ψ : B →+* C) (f : Fin r → A) :
    complexMap φ f ≫
        ((ModuleCat.restrictScalars φ).mapHomologicalComplex (ComplexShape.up ℕ)).map
          (complexMap ψ (mapFamily φ f)) =
      complexMap (ψ.comp φ) f
```

**`Stacks.CechRingBaseChange.isIso_derivedBaseChange_extendedComplexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/RingBaseChangeDerived.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/RingBaseChangeDerived.lean#L473). The attribute's comment: “condition (c) for a pair with a chosen finite generating family”.

> **The derived base change of the Čech complex is an isomorphism.** The map
> `C^•(f₁, …, f_r; A) ⊗^L_A B → C^•(g₁, …, g_r; B)` induced by the change-of-rings map of item (3)
> is an isomorphism in `D(B)`: the Čech complex of a ring is K-flat, so the derived base change is
> computed by the degreewise one, which is an isomorphism because each
> `B ⊗_A A_{f_{i_0} \cdots f_{i_{p-1}}} → B_{g_{i_0} \cdots g_{i_{p-1}}}` is.

```lean
theorem isIso_derivedBaseChange_extendedComplexMap (φ : A →+* B) (f : Fin r → A) :
    IsIso (Stacks.LocalCohomology.derivedBaseChange φ (extendedComplexMap φ f))
```

**`Stacks.LocalCohomology.extendedCechComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechModel.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CechModel.lean#L109). The attribute's comment: “item (1) for a pair with a chosen finite generating family”.

> The extended alternating Čech complex `C^•(f₁, …, f_r; M)`, regarded as a cochain complex in
> integer degrees.
>
> Read at `M = A`, this is **item (1) of tag 099D** for a pair carrying a chosen finite generating
> family: the complex of `A`-modules attached to the pair.

```lean
abbrev extendedCechComplex : CochainComplex (ModuleCat.{max u v} R) ℤ
```

**`Stacks.LocalCohomology.extendedCechAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CechModel.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CechModel.lean#L219). The attribute's comment: “item (2) for a pair with a chosen finite generating family”.

> **The augmentation of the Čech complex.** It is the identity on `M` in degree zero and zero
> elsewhere; the Stacks map `C^•(f₁, …, f_r; M) → M`.
>
> Read at `M = A`, this is **item (2) of tag 099D** for a pair carrying a chosen finite generating
> family: the map from the complex onto the ring.

```lean
def extendedCechAugmentation :
    extendedCechComplex f M ⟶
      (CochainComplex.singleFunctor (ModuleCat.{max u v} R) 0).obj M
```

## Tag 099E, a lemma

[Tag 099E](https://stacks.math.columbia.edu/tag/099E) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_isGlobalExtendedCech`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/FiniteTypeExtendedCech.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/FiniteTypeExtendedCech.lean#L304).

> **[Stacks, Tag 099E]**: for a sheaf of ideals `ℐ ⊆ 𝒪` on a ringed site there is a map
> `K ⟶ 𝒪` such that for every object `U` and every finite family of sections over `U` generating
> `ℐ|_U`, the extended alternating Čech complex of the family is isomorphic to `K|_U` in `D(𝒪_U)`,
> compatibly with the maps to `𝒪_U`.
>
> The source assumes `ℐ` of finite type; the construction does not use it — over an object on which
> `ℐ` is not finitely generated the condition is empty — so it is not assumed here. The map is a map
> of complexes, `AlgebraicGeometry.RingedSite.finiteTypeCechAugmentation`, whose image in `D(𝒪)` is
> the map of the tag.

```lean
theorem exists_isGlobalExtendedCech :
    ∃ (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
      (a : K ⟶ structureSheafComplex X),
      IsGlobalExtendedCech X ℐ K a
```

## Tag 099F, a proposition

[Tag 099F](https://stacks.math.columbia.edu/tag/099F) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/FiniteTypeReflector.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/FiniteTypeReflector.lean#L112).

> **[Stacks, Tag 099F].** Let `(𝒞, 𝒪)` be a ringed site and `ℐ ⊂ 𝒪` a sheaf of ideals of
> finite type. Then the inclusion `D_comp(𝒪, ℐ) ⥤ D(𝒪)` of the objects derived complete along `ℐ`
> has a left adjoint.
>
> As in the source, the left adjoint is `E ↦ R𝑆heafHom_𝒪(K, E)` for the map `K ⟶ 𝒪` of
> [Stacks, Tag 099E], `AlgebraicGeometry.RingedSite.finiteTypeCechAugmentation`: the three clauses
> of the universal property are checked on the slices of a covering family over which `ℐ` is
> generated by finitely many sections, in
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_of_isGlobalExtendedCech`; and
> `derivedCompletionIsoFiniteTypeCech` below identifies the derived completion functor with that
> formula.

```lean
instance isRightAdjoint_ι_isDerivedComplete :
    (ObjectProperty.ι (IsDerivedComplete.{u, u, u, u} X I)).IsRightAdjoint
```

**`AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealAdjoint.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GeneratedIdealAdjoint.lean#L182). The attribute's comment: “for the sheaf of ideals generated by finitely many global sections of the structure sheaf, with the Čech completion of 099B as the left adjoint”.

> Let `(𝒞, 𝒪)` be a ringed site and let `f_1, …, f_r` be global sections of `𝒪`. The inclusion
> of the objects of `D(𝒪)` derived complete along `ℐ = (f_1, …, f_r)` into `D(𝒪)` has a left
> adjoint, namely the Čech completion `K ↦ R𝑆heafHom_𝒪(Č(f), K)`.

```lean
theorem isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf :
    (ObjectProperty.ι
      (IsDerivedComplete.{u, u, u, u} X (generatedIdealSheaf f))).IsRightAdjoint
```

## Tag 0CQH, a remark

[Tag 0CQH](https://stacks.math.columbia.edu/tag/0CQH) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isDerivedComplete_derivedTensor_adicQuotient_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientCompletionComparison.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientCompletionComparison.lean#L76). The attribute's comment: “first assertion: `K ⊗^𝐋_𝒪 𝒪/ℐⁿ` is derived complete for `n ≥ 1`”.

> **[Stacks, Tag 0CQH], the derived completeness of the reductions.** For `ℐ` of finite type,
> `K ⊗^𝐋_𝒪 𝒪/ℐⁿ` is derived complete along `ℐ`: multiplication by `fⁿ`, for a local section `f`
> of `ℐ` over `U`, is zero on its restriction to `U`. The source states this for `n ≥ 1`; it holds
> for every `n`, `𝒪/ℐ⁰` being zero.

```lean
theorem isDerivedComplete_derivedTensor_adicQuotient_of_isFiniteType
    [I.toSheafOfModules.IsFiniteType]
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (n : ℕ) :
    IsDerivedComplete.{u, u, u, u} X I
      (((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj
        (adicQuotientObj X I n))
```

**`AlgebraicGeometry.RingedSite.exists_not_isIso_derivedCompletionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientCompletionComparison.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientCompletionComparison.lean#L94). The attribute's comment: “fifth assertion: in general the comparison map is not an isomorphism”.

> **[Stacks, Tag 0CQH], the comparison map is not an isomorphism in general.** There are a
> ringed site `(𝒞, 𝒪)`, a sheaf of ideals `ℐ` of finite type and `K ∈ D(𝒪)` such that no
> comparison map `K^∧ ⟶ R lim (K ⊗^𝐋_𝒪 𝒪/ℐⁿ)` — no map `c` into a derived limit `L` of the
> reduction tower whose composites with the projections are the factorizations — is an
> isomorphism. The witness is the one-point ringed site of `k[X] ⋉ k[X, X⁻¹]/k[X]` for `k = ℤ`,
> with `ℐ = (X)` and `K = (𝒪/ℐ)[0]`.

```lean
theorem exists_not_isIso_derivedCompletionComparison :
    ∃ (X : RingedSite.{u, u, u})
      (I : SheafOfModules.Submodule
        (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
      (_ : I.toSheafOfModules.IsFiniteType)
      (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))),
      ∀ (L : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
        (p : L ⟶ ∏ᶜ fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩)
        (δ : (∏ᶜ fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧)
        (c : (derivedCompletion X I).obj K ⟶ L),
        Triangle.mk p (Pi.lift fun n : ℕ =>
            Pi.π (fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) (n + 1) ≫
              (adicReductionTower X I K).map (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang
            (DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) →
        (∀ n : ℕ, c ≫ p ≫ Pi.π (fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) n =
          derivedCompletionAdicFactor X I K (n + 1)) →
        ¬ IsIso c
```

**`AlgebraicGeometry.RingedSite.existsUnique_derivedCompletion_factorization_adicQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientFactorization.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientFactorization.lean#L192). The attribute's comment: “second assertion: the canonical factorization `K → K^∧ → K ⊗^L O/I^n` of the canonical map, for the derived completion functor of Tag 099F”.

> **The canonical factorization.** The derived reduction `K ⟶ K ⊗^𝐋_𝒪 𝒪/ℐⁿ` factors uniquely
> as `K ⟶ K^∧ ⟶ K ⊗^𝐋_𝒪 𝒪/ℐⁿ` through the derived completion, for an arbitrary sheaf of ideals
> and an arbitrary reflector.

```lean
theorem existsUnique_derivedCompletion_factorization_adicQuotient
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    (n : ℕ) :
    ∃! g : (derivedCompletion X I).obj K ⟶
        ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).obj
          (adicQuotientObj X I n),
      (derivedCompletionUnit X I).app K ≫ g = adicQuotientReduction X I K n
```

**`AlgebraicGeometry.RingedSite.derivedCompletionAdicFactor_comp_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientFactorization.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientFactorization.lean#L209). The attribute's comment: “third assertion: the factorizations are compatible for varying `n`”.

> **The factorizations are compatible for varying `n`.** The factorization through `K^∧` of
> the reduction modulo `ℐⁿ`, followed by the transition map `𝒪/ℐⁿ ⟶ 𝒪/ℐᵐ`, is the factorization
> of the reduction modulo `ℐᵐ`.

```lean
theorem derivedCompletionAdicFactor_comp_map
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
    {m n : ℕ} (h : m ≤ n) :
    derivedCompletionAdicFactor X I K n ≫
        ((Stacks.SheafOfModules.derivedTensorProductFunctor X).obj K).map
          ((DerivedCategory.singleFunctor
              (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) 0).map
            (Stacks.Sites.adicQuotientModuleMap (X := X) I h)) =
      derivedCompletionAdicFactor X I K m
```

**`AlgebraicGeometry.RingedSite.exists_derivedCompletionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientFactorization.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/AdicQuotientFactorization.lean#L238). The attribute's comment: “fourth assertion: the comparison map `K^∧ → R lim (K ⊗^L O/I^n)` induced by the compatible factorizations; `R lim` is presented by its Milnor triangle”.

> **The comparison map `K^∧ ⟶ R lim (K ⊗^𝐋_𝒪 𝒪/ℐⁿ)`.** The compatible factorizations
> `K^∧ ⟶ K ⊗^𝐋_𝒪 𝒪/ℐⁿ⁺¹` lift through the Milnor triangle of the reduction tower to a map into its
> derived limit, whose composite with each projection is the corresponding factorization.

```lean
theorem exists_derivedCompletionComparison
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    ∃ (L : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
      (p : L ⟶ ∏ᶜ fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩)
      (δ : (∏ᶜ fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧)
      (c : (derivedCompletion X I).obj K ⟶ L),
      Triangle.mk p (Pi.lift fun n : ℕ =>
            Pi.π (fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) n -
            Pi.π (fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) (n + 1) ≫
              (adicReductionTower X I K).map (homOfLE (Nat.le_succ n)).op) δ ∈
          distTriang
            (DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) ∧
        ∀ n : ℕ, c ≫ p ≫ Pi.π (fun n : ℕ => (adicReductionTower X I K).obj ⟨n⟩) n =
          derivedCompletionAdicFactor X I K (n + 1)
```

## Tag 0A0F, a remark

[Tag 0A0F](https://stacks.math.columbia.edu/tag/0A0F) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedCompletion_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationCompletionFiniteType.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationCompletionFiniteType.lean#L175).

> **[Stacks, Tag 0A0F]: derived completion commutes with localization.** Let `(𝒞, 𝒪)` be a
> ringed site, `ℐ ⊂ 𝒪` a sheaf of ideals of finite type, `K ↦ K^∧` the derived completion functor
> of [Stacks, Tag 099F] and `U` an object of `𝒞`. Then `K^∧|_U` is the derived completion of `K|_U`
> along `ℐ|_U`:
>
> * `K^∧|_U` is derived complete along `ℐ|_U`, for every `K`;
> * hence there is a canonical map `a : (K|_U)^∧ ⟶ K^∧|_U`, natural in `K`, compatible with the
>   completion maps — its composite with `K|_U ⟶ (K|_U)^∧` is the restriction of `K ⟶ K^∧` — and
>   it is the only such map (`eq_derivedCompletionRestrictComparison_of_derivedCompletionUnit_comp`);
> * `a` is an isomorphism, for every `K`.
>
> The completion functor on `𝒞/U` is that of [Stacks, Tag 099F] for the ringed site
> `(𝒞/U, 𝒪_U)` and the restricted sheaf of ideals `ℐ|_U`, which is of finite type
> (`isFiniteType_overIdeal`); `a` is `derivedCompletionRestrictComparison`, and the resulting
> natural isomorphism is `derivedCompletionRestrictIso`. The source proves the invertibility of `a`
> "from the construction in the proof of the proposition"; so does this library: both completion
> functors are `R𝑆heafHom(K₀, -)` for the map `K₀ ⟶ 𝒪` of [Stacks, Tag 099E] on the respective site,
> the one on `𝒞/U` may be taken to be the restriction of the one on `𝒞`
> (`isGlobalExtendedCech_restrict`), and `R𝑆heafHom` commutes with restriction by
> [Stacks, Tag 08JB]. The Remark's second argument — the map `b : K^∧ ⟶ Rj_*((K|_U)^∧)` and the
> verification that its adjoint inverts `a` — is the companion registration
> `derivedCompletion_restrict_secondMap` of `LocalizationCompletionPushforward.lean`.

```lean
theorem derivedCompletion_restrict :
    (∀ K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
      IsDerivedComplete.{u, u, u, u} (X.over U) (overIdeal I U)
        ((SheafOfModules.overFunctor.{u}
            ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.obj
          ((derivedCompletion X I).obj K))) ∧
    (∀ K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
      (derivedCompletionUnit (X.over U) (overIdeal I U)).app
          ((SheafOfModules.overFunctor.{u}
            ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.obj K) ≫
        (derivedCompletionRestrictComparison X I U (overIdeal I U) (fun _ _ hg ↦ hg)).app K =
      (SheafOfModules.overFunctor.{u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.map
        ((derivedCompletionUnit X I).app K)) ∧
    (∀ K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
      IsIso ((derivedCompletionRestrictComparison X I U (overIdeal I U)
        (fun _ _ hg ↦ hg)).app K))
```

**`AlgebraicGeometry.RingedSite.derivedCompletion_restrict_secondMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationCompletionPushforward.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalizationCompletionPushforward.lean#L121). The attribute's comment: “the Remark's second argument: `Rj_*` carries objects derived complete along `ℐ|_U` to objects derived complete along `ℐ`, so there is a unique map `b : K^∧ ⟶ Rj_*((K|_U)^∧)` compatible with the completion maps, and the adjoint of `b` under `(-)|_U ⊣ Rj_*` is the inverse of the map `a` of `derivedCompletion_restrict`”.

> **The second half of [Stacks, Tag 0A0F]: the map `b` and its adjoint.** Let `ℐ ⊂ 𝒪` be a
> sheaf of ideals of finite type, `U` an object of `𝒞` and `j` the localization morphism.
>
> * `Rj_*` carries objects derived complete along `ℐ|_U` to objects derived complete along `ℐ`
>   ([Stacks, Tag 099J] for `j`);
> * hence for every `K` there is a unique `b : K^∧ ⟶ Rj_*((K|_U)^∧)` whose composite with the
>   completion map `K ⟶ K^∧` is the adjunct `K ⟶ Rj_*((K|_U)^∧)` of the completion map of `K|_U`,
>   under the adjunction `(-)|_U ⊣ Rj_*` (`overFunctorDerivedAdjunction`);
> * the adjoint `K^∧|_U ⟶ (K|_U)^∧` of `b` is the inverse of the canonical map
>   `a = derivedCompletionRestrictComparison` of `derivedCompletion_restrict`.

```lean
theorem derivedCompletion_restrict_secondMap :
    (∀ E : DerivedCategory
        (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (X.over U).O))),
      IsDerivedComplete.{u, u, u, u} (X.over U) (overIdeal I U) E →
        IsDerivedComplete.{u, u, u, u} X I ((localizationDerivedPushforward X U).obj E)) ∧
    (∀ K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
      ∃! b : (derivedCompletion X I).obj K ⟶ (localizationDerivedPushforward X U).obj
          ((derivedCompletion (X.over U) (overIdeal I U)).obj
            ((SheafOfModules.overFunctor.{u}
              ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.obj K)),
        (derivedCompletionUnit X I).app K ≫ b =
          (overFunctorDerivedAdjunction X U).unit.app K ≫
            (localizationDerivedPushforward X U).map
              ((derivedCompletionUnit (X.over U) (overIdeal I U)).app
                ((SheafOfModules.overFunctor.{u}
                  ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.obj K))) ∧
    (∀ (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))))
      (b : (derivedCompletion X I).obj K ⟶ (localizationDerivedPushforward X U).obj
          ((derivedCompletion (X.over U) (overIdeal I U)).obj
            ((SheafOfModules.overFunctor.{u}
              ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.obj K))),
      (derivedCompletionUnit X I).app K ≫ b =
          (overFunctorDerivedAdjunction X U).unit.app K ≫
            (localizationDerivedPushforward X U).map
              ((derivedCompletionUnit (X.over U) (overIdeal I U)).app
                ((SheafOfModules.overFunctor.{u}
                  ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)) U).mapDerivedCategory.obj K)) →
        ((overFunctorDerivedAdjunction X U).homEquiv _ _).symm b ≫
            (derivedCompletionRestrictComparison X I U (overIdeal I U) (fun _ _ hg ↦ hg)).app K =
          𝟙 _ ∧
        (derivedCompletionRestrictComparison X I U (overIdeal I U) (fun _ _ hg ↦ hg)).app K ≫
            ((overFunctorDerivedAdjunction X U).homEquiv _ _).symm b = 𝟙 _)
```

## Tag 099G, a remark

[Tag 099G](https://stacks.math.columbia.edu/tag/099G) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.completeDerivedSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean#L103). The attribute's comment: “the assertion `R𝑆heafHom_𝒪(L, M) ∈ D_comp(𝒪)` for `L, M ∈ D_comp(𝒪)`, which the tag records at the end and attributes to [Stacks, Tag 099A], as the induced bifunctor on the derived-complete objects; it holds for every sheaf of ideals”.

> **The derived internal Hom of derived-complete objects is derived complete**, so it is a
> bifunctor `D_comp(𝒪)ᵒᵖ × D_comp(𝒪) ⥤ D_comp(𝒪)`. This is the last assertion of
> [Stacks, Tag 099G], and it is [Stacks, Tag 099A] — which asks nothing of the source — applied
> to a derived-complete target.

```lean
def completeDerivedSheafHom :
    (ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I))ᵒᵖ ⥤
      ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I) ⥤
        ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I)
```

**`AlgebraicGeometry.RingedSite.completedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean#L193). The attribute's comment: “the completed tensor product `K ⊗^∧_𝒪 L = (K ⊗^𝐋_𝒪 L)^∧` and its functoriality in each variable, as a bifunctor on `D_comp(𝒪)`”.

> **The completed tensor product of [Stacks, Tag 099G].** For `ℐ` of finite type and
> derived-complete `K` and `L`, `K ⊗^∧_𝒪 L = (K ⊗^𝐋_𝒪 L)^∧`, where `(-)^∧` is the derived
> completion functor of [Stacks, Tag 099F]; the completion of any object is derived complete, so
> this is a bifunctor on the derived-complete objects.

```lean
def completedTensorProduct :
    ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I) ⥤
      ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I) ⥤
        ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I)
```

**`AlgebraicGeometry.RingedSite.completedTensorProductProd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean#L202). The attribute's comment: “the completed tensor product as a functor `D_comp(𝒪) × D_comp(𝒪) → D_comp(𝒪)`”.

> **The completed tensor product as a functor `D_comp(𝒪) × D_comp(𝒪) ⥤ D_comp(𝒪)`**, the
> shape in which [Stacks, Tag 099G] states it, for `ℐ` of finite type.

```lean
def completedTensorProductProd :
    ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I) ×
        ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I) ⥤
      ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I)
```

**`AlgebraicGeometry.RingedSite.completedTensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/CompletedTensorProduct.lean#L236). The attribute's comment: “the bijection `Hom_{D_comp(𝒪)}(K, R𝑆heafHom_𝒪(L, M)) = Hom_{D_comp(𝒪)}(K ⊗^∧_𝒪 L, M)` for `K, L, M ∈ D_comp(𝒪)`”.

> **The adjunction of [Stacks, Tag 099G].** For `ℐ` of finite type and derived-complete `K`,
> `L` and `M`,
>
> `Hom_{D_comp(𝒪)}(K, R𝑆heafHom_𝒪(L, M)) = Hom_{D_comp(𝒪)}(K ⊗^∧_𝒪 L, M)`.
>
> It is `completedTensorHomEquivOfIsRightAdjoint` at the derived completion functor of
> [Stacks, Tag 099F]: in order, the full faithfulness of `D_comp(𝒪) ⥤ D(𝒪)`, the bijection of
> [Stacks, Tag 08J8], and the inverse of the hom-set bijection of the adjunction of
> [Stacks, Tag 099F] at the derived-complete `M`.

```lean
def completedTensorHomEquiv
    (K L M : ObjectProperty.FullSubcategory (IsDerivedComplete.{u, u, u, u} X I)) :
    (K ⟶ ((completeDerivedSheafHom X I).obj (op L)).obj M) ≃
      (((completedTensorProduct X I).obj K).obj L ⟶ M)
```

## Tag 099H, a lemma

[Tag 099H](https://stacks.math.columbia.edu/tag/099H) in the Stacks Project.

**`Stacks.Sheaves.CechFlatNeighbourhood.quasiIso_complexMap_cechSystemBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatNeighbourhoodCechNatural.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatNeighbourhoodCechNatural.lean#L417).

> **Stacks Project, Tag 099H.**  Let `C` be a site, let `φ : O ⟶ O'` be a flat homomorphism
> of sheaves of commutative rings on `C`, and let `f₁, …, f_r` be global sections of `O` such that
> the canonical map `O/(f₁, …, f_r) ⟶ O'/(f₁, …, f_r)O'` of sheaves of `O`-modules
> (`Stacks.SheafOfModules.DerivedRestrictScalars.quotientMap`) is an isomorphism; here
> `(f₁, …, f_r)` is the ideal sheaf generated by the `f_k`
> (`AlgebraicGeometry.RingedSite.idealOfGlobalSections`) and `(f₁, …, f_r)O'` is the ideal sheaf of
> `O'` it generates (`AlgebraicGeometry.RingedSite.extendIdeal`), which is the ideal sheaf generated
> by the images of the `f_k`
> (`Stacks.Sheaves.CechFlatNeighbourhood.extendedIdeal_idealOfGlobalSections`). Then the map of
> extended alternating Čech complexes
>
> `O → ∏_{i₀} O_{f_{i₀}} → ∏_{i₀ < i₁} O_{f_{i₀}f_{i₁}} → ⋯ → O_{f₁⋯f_r}`
> `  ⟶ O' → ∏_{i₀} O'_{f_{i₀}} → ∏_{i₀ < i₁} O'_{f_{i₀}f_{i₁}} → ⋯ → O'_{f₁⋯f_r}`
>
> is a quasi-isomorphism.  The map is the one induced by the canonical maps
> `O_{f_S} ⟶ O'_{f_S}` of sheaves of `O`-modules, `cechSystemBaseChangeMap`: they are compatible
> with `O ⟶ O_{f_S}` and `O ⟶ O' ⟶ O'_{f_S}`
> (`unitToAwayModule_comp_cechSystemBaseChangeMap_app`), and they are the only such family
> (`eq_cechSystemBaseChangeMap`).  The lower complex is the extended alternating Čech complex of
> the system `S ↦ O'_{f_S}` of sheaves of `O`-modules.
>
> The proof is the source's: `quasiIso_extendedAlternatingCechBaseChangeMap`.

```lean
theorem quasiIso_complexMap_cechSystemBaseChangeMap (hφ : IsFlatMap φ)
    (hiso : IsIso (Stacks.SheafOfModules.DerivedRestrictScalars.quotientMap φ
      (idealOfGlobalSections (ringedSite O) f))) :
    QuasiIso (AlternatingCech.complexMap (cechSystemBaseChangeMap O f φ))
```

## Tag 099I, a lemma

[Tag 099I](https://stacks.math.columbia.edu/tag/099I) in the Stacks Project.

**`Stacks.SheafOfModules.DerivedRestrictScalars.isEquivalence_derivedCompleteRestrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/RestrictScalarsFlatEquivalence.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/RestrictScalarsFlatEquivalence.lean#L233).

> **[Stacks, Tag 099I].** Let `𝒞` be a site, `α : 𝒪 ⟶ 𝒪'` a homomorphism of sheaves of
> commutative rings and `ℐ ⊂ 𝒪` a sheaf of ideals of finite type. If `α` is flat and
> `𝒪/ℐ ≅ 𝒪'/ℐ𝒪'`, then restriction of scalars `D(𝒪') ⥤ D(𝒪)` induces an equivalence
> `D_comp(𝒪', ℐ𝒪') ⥤ D_comp(𝒪, ℐ)`: the functor `derivedCompleteRestrictScalars α ℐ` is an
> equivalence.
>
> Flatness is `AlgebraicGeometry.SheafOfModules.IsFlatMap α` ([Stacks, Tag 03ER]): `𝒪'` is a flat
> `𝒪`-module. The isomorphism `𝒪/ℐ ≅ 𝒪'/ℐ𝒪'` is the canonical map
> `quotientMap α ℐ : 𝒪/ℐ ⟶ 𝒪'/ℐ𝒪'` induced by `α` being invertible, with `ℐ𝒪'` the ideal sheaf
> `AlgebraicGeometry.RingedSite.extendIdeal` of `D_comp(𝒪', ℐ𝒪')`. Finite type is Mathlib's
> `SheafOfModules.IsFiniteType`.

```lean
theorem isEquivalence_derivedCompleteRestrictScalars
    (hflat : AlgebraicGeometry.SheafOfModules.IsFlatMap α)
    (I : _root_.SheafOfModules.Submodule
      (_root_.SheafOfModules.unit
        (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} (ringedSite J O).O)))
    [I.toSheafOfModules.IsFiniteType]
    (hquot : IsIso (quotientMap α I)) :
    (derivedCompleteRestrictScalars α I).IsEquivalence
```

## Tag 099K, a lemma

[Tag 099K](https://stacks.math.columbia.edu/tag/099K) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.isDerivedComplete_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionTopos.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionTopos.lean#L176). The attribute's comment: “first statement: `Rf_*` sends `D_comp(𝒪', ℐ')` into `D_comp(𝒪, ℐ)`; the finite-type hypotheses on `ℐ` and `ℐ'` are not needed”.

> **[Stacks, Tag 099K], first statement.** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism
> of ringed topoi and let `ℐ ⊆ 𝒪`, `ℐ' ⊆ 𝒪'` be sheaves of ideals such that `f^♯` sends `f^{-1}ℐ`
> into `ℐ'`. Then `Rf_*` sends `D_comp(𝒪', ℐ')` into `D_comp(𝒪, ℐ)`: if `K` is derived complete
> along `ℐ'`, then `Rf_*K` is derived complete along `ℐ`.
>
> The source asks `ℐ` and `ℐ'` to be of finite type; neither hypothesis is needed. This is
> [Stacks, Tag 099J], `AlgebraicGeometry.RingedToposHom.derivedPushforward_isDerivedComplete`,
> read in the variables of Tag 099K, as the source's proof says.

```lean
theorem isDerivedComplete_derivedPushforward (hI : IdealCompatible f I I')
    (K : DerivedCategory
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.toRingedSite.O))))
    (hK : RingedSite.IsDerivedComplete.{u, u, u, u} X.toRingedSite I' K) :
    RingedSite.IsDerivedComplete.{u, u, u, u} Y.toRingedSite I
      ((DerivedPushforward.derivedPushforward (X := X) (Y := Y) f).obj K)
```

**`AlgebraicGeometry.RingedToposHom.derivedCompletePullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionTopos.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCompletionTopos.lean#L212). The attribute's comment: “second statement: the left adjoint `Lf^*_comp` of `Rf_*` on the derived-complete objects, `Lf^*` followed by derived completion; the finite-type hypothesis on `ℐ` is not needed”.

> **[Stacks, Tag 099K], second statement.** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a
> morphism of ringed topoi and let `ℐ ⊆ 𝒪`, `ℐ' ⊆ 𝒪'` be sheaves of ideals such that `f^♯` sends
> `f^{-1}ℐ` into `ℐ'`, with `ℐ'` of finite type. Then `Rf_*` sends `D_comp(𝒪', ℐ')` into
> `D_comp(𝒪, ℐ)` (`isDerivedComplete_derivedPushforward`, read as the functor
> `derivedCompletePushforward`), and this functor has a left adjoint `Lf^*_comp`, which is `Lf^*`
> followed by derived completion along `ℐ'` (`derivedCompletePullback`, and
> `derivedCompletePullback_comp_ι`).
>
> The derived completion functor is the left adjoint of the inclusion `D_comp(𝒪', ℐ') ⥤ D(𝒪')`
> that [Stacks, Tag 099F] provides for `ℐ'` of finite type, the instance
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete`. The source also asks `ℐ` to be
> of finite type; that is not needed, since [Stacks, Tag 099J] holds for an arbitrary `ℐ`. The two
> ringed topoi are presented by sites small in the universe of the sections of their structure
> sheaves, as in [Stacks, Tag 03CR], through which Tag 099J is proved.

```lean
def derivedCompletePullbackPushforwardAdjunction [I'.toSheafOfModules.IsFiniteType]
    (hI : IdealCompatible f I I') :
    derivedCompletePullback f I I' ⊣ derivedCompletePushforward f I I' hI
```

## Tag 0A0G, a lemma

[Tag 0A0G](https://stacks.math.columbia.edu/tag/0A0G) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedCompletionPushforwardComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean#L367). The attribute's comment: “the canonical map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` whose invertibility the tag asserts, constructed as a mate and hence natural in `K`, at an arbitrary pair of sheaves of ideals subject only to the relation of [Stacks, Tag 099J] between them. Its invertibility at every object of `D(𝒪')`, which is the tag's assertion, is `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType` of `PushforwardCommutesCompletionLocalToGlobal.lean`, at the tag's own data: `ℐ` of finite type and `ℐ' = f^{-1}ℐ · 𝒪_X`”.

> **The canonical map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` of [Stacks, Tag 0A0G].** It exists because
> `Rf_*(K^∧)` is derived complete, by [Stacks, Tag 099J], so the universal property of derived
> completion applies to `Rf_*K ⟶ Rf_*(K^∧)`. Built as a mate, so that it is natural in `K`.
>
> This is the map the tag asserts to be invertible, and it is invertible at every object of
> `D(𝒪')` at the tag's own data — `ℐ` of **finite type** and `ℐ' = f^{-1}ℐ · 𝒪_X` — by
> `RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`
> of `PushforwardCommutesCompletionLocalToGlobal.lean`; that statement localizes the globally
> generated case,
> `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf`
> of `PushforwardCommutesCompletionCanonical.lean`. Here `ℐ` and `ℐ'` are an arbitrary pair of
> sheaves of ideals subject only to `hI`, which is where the construction already makes sense.

```lean
def derivedCompletionPushforwardComparison :
    derivedPushforward.{u} f.toRingedToposSiteHom ⋙ derivedCompletion Y I ⟶
      derivedCompletion X I' ⋙ derivedPushforward.{u} f.toRingedToposSiteHom
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_of_isIso_map_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean#L398). The attribute's comment: “the criterion: `Rf_*` commutes with derived completion at every `K` for which `Rf_*(K ⟶ K^∧)` is invertible; the source proves it for every `K`”.

> **A criterion for `Rf_*` to commute with derived completion at `K`.** If `Rf_*` applied to
> the unit `K ⟶ K^∧` is invertible, then so is the comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`.
>
> Indeed `Rf_*(K^∧)` is derived complete, so an invertible `Rf_*(K ⟶ K^∧)` makes `Rf_*K` derived
> complete too, whence its unit `Rf_*K ⟶ (Rf_*K)^∧` is invertible; and the comparison map is the
> second factor of that unit followed by itself in
> `derivedCompletionUnit_comp_derivedCompletionPushforwardComparison`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_of_isIso_map_unit
    {K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (hK : IsIso ((derivedPushforward.{u} f.toRingedToposSiteHom).map
      ((derivedCompletionUnit X I').app K))) :
    IsIso ((derivedCompletionPushforwardComparison f I I' hI).app K)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletion.lean#L440). The attribute's comment: “for `K` in `D_comp(𝒪', ℐ')`, where the unit `K ⟶ K^∧` is invertible, at an arbitrary pair of sheaves of ideals subject only to the relation of [Stacks, Tag 099J]. The tag's assertion for an arbitrary `K` is `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf` of `PushforwardCommutesCompletionCanonical.lean`, at the tag's own pair of sheaves of ideals”.

> **[Stacks, Tag 0A0G] at a derived-complete object.** For `K` in `D_comp(𝒪', ℐ')` the
> canonical map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible, so `Rf_*(K^∧) = Rf_*K = (Rf_*K)^∧`: the
> unit `K ⟶ K^∧` is invertible on a derived-complete `K`.
>
> The general case of Tag 0A0G, for an arbitrary `K`, is proved at the tag's own data — a sheaf
> of ideals `ℐ ⊂ 𝒪` of finite type and `ℐ' = f^{-1}ℐ · 𝒪_X` — by
> `isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType` of
> `PushforwardCommutesCompletionLocalToGlobal.lean`. Equation 52.7.0.1 of [Stacks, Tag 0A0I], in
> its own setting of a morphism of schemes and a quasi-coherent sheaf of ideals of finite type, is
> `AlgebraicGeometry.Scheme`
> `.isIso_derivedCompletionPushforwardComparison_idealSheafData_inverseImageIdealSheaf` of
> `PushforwardCommutesCompletionFiniteType.lean`. The statement here is the case of an independent
> pair of sheaves of ideals subject only to the relation of [Stacks, Tag 099J], at a
> derived-complete object. It also carries part (3) of
> [Stacks, Tag 099N], with the restrictions named on `derivedCompletePushforward`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_of_isDerivedComplete
    {K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (hK : IsDerivedComplete.{u, u, u, u} X I' K) :
    IsIso ((derivedCompletionPushforwardComparison f I I' hI).app K)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionCanonical.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionCanonical.lean#L422). The attribute's comment: “the tag's conclusion for the **canonical** comparison map and an **arbitrary** object: `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible for every `K` of `D(𝒪')`, at a morphism of ringed sites and at `ℐ = (t_1, …, t_r) ⊂ 𝒪` and `ℐ' = (f^♯t_1, …, f^♯t_r) ⊂ 𝒪'` generated by finitely many global sections of the two structure sheaves — the regime the source's own proof reduces to, and the regime in which [Stacks, Tag 099F] is available here, so that both derived completion functors are produced from those generators and no conclusion of that tag is an input. The relation between the two sheaves of ideals is proved from `g_i = f^♯(t_i)` rather than received, and no countable coproduct in a derived category is assumed. The restriction is on the data alone: the source's `ℐ` is quasi-coherent of finite type, hence only *locally* generated by finitely many sections, and [Stacks, Tag 099F] at such an `ℐ` rests on [Stacks, Tags 099D and 099E]”.

> **[Stacks, Tag 0A0G] for the canonical comparison map and an arbitrary object, at two
> sheaves of ideals generated by finitely many global sections.** Let
> `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism of ringed sites, let `t_1, …, t_r` be global
> sections of `𝒪` generating `ℐ ⊂ 𝒪`, let `g_i = f^♯(t_i)` generate `ℐ' ⊂ 𝒪'`, and let
> `K ∈ D(𝒪')` be **arbitrary**. Then the canonical map
>
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`
>
> of `AlgebraicGeometry.RingedSite.derivedCompletionPushforwardComparisonGeneratedIdealSheaf` is
> invertible: `Rf_*` commutes with derived completion, through the map the tag says it does.
>
> Both derived completion functors are the reflector of [Stacks, Tag 099F], produced from the
> generators by
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`, so no
> conclusion of that tag is an input; and the relation `PushforwardIdealCompatible` between the two
> sheaves of ideals that the comparison map needs is proved from `hg`, by
> `AlgebraicGeometry.RingedSite.pushforwardIdealCompatible_of_pushGlobalSectionsCompatible`.
>
> The proof is `isIso_derivedCompletionPushforwardComparison_of_nonempty_iso` fed with
> `AlgebraicGeometry.RingedSite.derivedPushforwardDerivedCompletionGeneratedIdealSheafIso` of
> `PushforwardCommutesCompletionCech.lean`, which runs the source's own computation through the
> Čech presentation of the two completions and gives the display at every object. The Koszul
> Hom-tower form of the display,
> `RingedSite.nonempty_iso_derivedPushforward_derivedCompletion_generatedIdealSheaf`,
> would serve equally except that it carries `Limits.HasCoproduct` on the two Koszul towers as
> instance binders — countable coproducts of a derived category, which K-injective resolutions do
> not produce — and the Čech form needs no coproduct in a derived category at all, so this
> statement carries no such binder.
>
> The source's `ℐ` is of finite type, hence only *locally* generated by finitely many sections;
> [Stacks, Tag 099F] at such an `ℐ` rests on [Stacks, Tags 099D and 099E], and the module
> documentation of `PushforwardCommutesCompletionGenerated.lean` records what stands in the way of
> the local-to-global descent.

```lean
theorem isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    IsIso ((derivedCompletionPushforwardComparisonGeneratedIdealSheaf f g t
      (pushforwardIdealCompatible_of_pushGlobalSectionsCompatible f t g hg)).app K)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionCanonical.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionCanonical.lean#L502). The attribute's comment: “**the ringed-sites case** for the **canonical** comparison map, at the tag's own pair of sheaves of ideals and for an **arbitrary** object. The tag states a morphism of ringed *topoi*; this is a morphism of ringed *sites*, which is how the sibling [Stacks, Tag 099J] is recorded in this directory (its full sites case is deliberately untagged and the attribute sits on the topos-level theorem). Concretely: `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible for every `K` of `D(𝒪')`, where `ℐ = (t_1, …, t_r) ⊂ 𝒪` is generated by finitely many global sections and `ℐ' = f^{-1}ℐ · 𝒪_X ⊂ 𝒪'` is constructed from `f` and `t` as the ideal sheaf generated by `f^♯t_1, …, f^♯t_r` and characterised as the least one receiving `f^♯(f^{-1}ℐ)`. The morphism of ringed sites carries a terminal object of the target site to a terminal object, as at ringed spaces and at schemes; both derived completion functors are produced from the generators of `ℐ`, so no conclusion of [Stacks, Tag 099F] is an input. The restriction is on the data alone: the source's `ℐ` is of finite type, hence only *locally* generated by finitely many sections”.

> **[Stacks, Tag 0A0G] for the canonical comparison map and an arbitrary object, at the
> source's own ideal sheaf `ℐ' = f^{-1}ℐ · 𝒪_X`.** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a
> morphism of ringed sites carrying a terminal object `T` of the target site to a terminal object,
> let `ℐ = (t_1, …, t_r) ⊂ 𝒪` be generated by finitely many global sections, and let `K ∈ D(𝒪')`
> be **arbitrary**. Then the canonical map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible, the completion
> on the source being taken along `ℐ' = f^{-1}ℐ · 𝒪_X`.
>
> That ideal sheaf is built here from `f` and `t`, as the one generated by `f^♯t_1, …, f^♯t_r`,
> and is the source's own: it receives `f^♯(f^{-1}ℐ)` and is least among those that do, by
> `AlgebraicGeometry.RingedSite.eq_generatedIdealSheaf_pushGlobalSections`. The terminal objects
> are what make a global section of `𝒪` transportable along a general morphism of sites; they are
> present at ringed spaces and at schemes, where `f.u` is `Opens.map` and carries `⊤` to `⊤`.
>
> This is `isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf` at
> `g = pushGlobalSections f hT' t`, whose relation to `t` is
> `AlgebraicGeometry.RingedSite.pushGlobalSectionsCompatible_pushGlobalSections`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    IsIso ((derivedCompletionPushforwardComparisonInverseImageIdealSheaf f hT hT' t).app K)
```

**`AlgebraicGeometry.RingedSite.derivedPushforwardDerivedCompletionGeneratedIdealSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionCech.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionCech.lean#L223). The attribute's comment: “`Rf_*` commutes with derived completion, `Rf_*(K^∧) = (Rf_*K)^∧`, for an **arbitrary** object `K` of `D(𝒪')`, at `ℐ = (t_1, …, t_r) ⊂ 𝒪` and `ℐ' = (f^♯t_1, …, f^♯t_r) ⊂ 𝒪'` generated by finitely many global sections of the two structure sheaves — the regime the source's own proof reduces to, and the regime in which [Stacks, Tag 099F] is available here, so that both derived completion functors are built from those generators and no part of that tag is an input. The display is produced as an explicit isomorphism from three identifications: derived completion along a globally generated ideal sheaf is the Čech completion of [Stacks, Tag 099B]; `Lf^*Č(𝒪, t) ≅ Č(𝒪', g)`; and the adjoint formula `Rf_* R𝓗om_{𝒪'}(Lf^*A, M) ≅ R𝓗om_𝒪(A, Rf_*M)` at arbitrary `A` and `M`. Restrictions on the data only: the object is arbitrary, and no countable coproduct in a derived category is assumed”.

> **[Stacks, Tags 0A0G and 0A0I] for an arbitrary object, at two sheaves of ideals generated by
> finitely many global sections.** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism of ringed
> sites, let `t_1, …, t_r` be global sections of `𝒪` generating `ℐ ⊂ 𝒪`, let `g_i = f^♯(t_i)`
> generate `ℐ' ⊂ 𝒪'`, and let `K ∈ D(𝒪')` be **arbitrary**. Then
>
> `Rf_*(K^∧) ≅ (Rf_*K)^∧`:
>
> `Rf_*` commutes with derived completion. Both derived completion functors are the reflector of
> [Stacks, Tag 099F], produced from the generators by
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`, so no part
> of that tag is an input.
>
> The reflector at a globally generated ideal sheaf **is** the Čech completion
> `R𝓗om(Č(-), -)` of [Stacks, Tag 099B]
> (`AlgebraicGeometry.RingedSite.reflectorIsoCompletionFunctor`), the source's Čech complex is the
> derived inverse image of the target's, and the adjoint formula moves `Rf_*` across the internal
> Hom. No countable coproduct in a derived category is assumed, and the isomorphism is produced
> rather than shown to exist; see the module documentation for the comparison with the
> derived-limit form.

```lean
def derivedPushforwardDerivedCompletionGeneratedIdealSheafIso
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedPushforward.{u} f.toRingedToposSiteHom).obj
        ((derivedCompletion X (generatedIdealSheaf g)).obj K) ≅
      (derivedCompletion Y (generatedIdealSheaf t)).obj
        ((derivedPushforward.{u} f.toRingedToposSiteHom).obj K)
```

**`AlgebraicGeometry.RingedSite.derivedCompletionPushforwardComparisonInverseImageIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionConstructedIdeal.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionConstructedIdeal.lean#L353). The attribute's comment: “the canonical comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` that the tag asserts to be invertible, at a morphism of ringed sites sending a terminal object of the target site to a terminal object of the source site, with `ℐ` generated by finitely many global sections of `𝒪` and the completion on the source taken along `f^{-1}ℐ · 𝒪_X` — the ideal sheaf Section 52.7 builds out of `ℐ`, which here is constructed from `f` and the generators of `ℐ` and identified as that ideal sheaf by `AlgebraicGeometry.RingedSite.eq_generatedIdealSheaf_pushGlobalSections`. Both derived completion functors are produced from the generators, by `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`. This map is invertible at every object of `D(𝒪')`, which is the tag's assertion, by `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf` of `PushforwardCommutesCompletionCanonical.lean`. At the tag's own `ℐ`, which is of finite type and hence only *locally* generated by finitely many sections, the derived completion functors come instead from [Stacks, Tag 099F] at a sheaf of ideals of finite type, `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete`”.

> **The canonical comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` of [Stacks, Tag 0A0G] at the source's
> own ideal sheaves.** It exists because `Rf_*(K^∧)` is derived complete, by [Stacks, Tag 099J];
> it is built as a mate and is therefore natural in `K`.
>
> This is `AlgebraicGeometry.RingedSite.derivedCompletionPushforwardComparisonGeneratedIdealSheaf`
> at `ℐ = (t_1, …, t_s)` and `ℐ' = f^{-1}ℐ · 𝒪_X`. It is invertible at every object of `D(𝒪')`,
> which is the tag's assertion:
> `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf`
> of `PushforwardCommutesCompletionCanonical.lean`, and
> `isIso_natTrans_derivedCompletionPushforwardComparison_inverseImageIdealSheaf` there for the
> whole natural transformation.

```lean
def derivedCompletionPushforwardComparisonInverseImageIdealSheaf :
    derivedPushforward.{u} f.toRingedToposSiteHom ⋙
        derivedCompletion Y (generatedIdealSheaf t) ⟶
      derivedCompletion X (generatedIdealSheaf (pushGlobalSections f hT' t)) ⋙
        derivedPushforward.{u} f.toRingedToposSiteHom
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isIso_map_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionConstructedIdeal.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionConstructedIdeal.lean#L385). The attribute's comment: “the criterion that the comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible as soon as `Rf_*(K ⟶ K^∧)` is, at a morphism of ringed sites sending a terminal object of the target site to a terminal object of the source site, with `ℐ` generated by finitely many global sections of `𝒪` and the completion on the source taken along the ideal sheaf `f^{-1}ℐ · 𝒪_X` of Section 52.7, built here out of `f` and the generators of `ℐ`. This is the reduction the source's own proof makes before its local computation, and by `AlgebraicGeometry.RingedSite.isIso_map_derivedCompletionUnit_iff` it covers exactly the objects with `Rf_*K` already derived complete. For an arbitrary object the source's computation is run in `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf` of `PushforwardCommutesCompletionCanonical.lean`, which gives the tag's assertion at this very pair of sheaves of ideals”.

> **A criterion for `Rf_*` to commute with derived completion at `K`, at the source's own ideal
> sheaves.** The comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible as soon as `Rf_*` applied to
> the completion map `K ⟶ K^∧` is.
>
> This is
> `RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isIso_map_unit` at
> `ℐ' = f^{-1}ℐ · 𝒪_X`. By `AlgebraicGeometry.RingedSite.isIso_map_derivedCompletionUnit_iff` its
> hypothesis `hK` holds exactly when `Rf_*K` is already derived complete, so this is the criterion at
> those objects; for an arbitrary `K` the invertibility comes from the source's computation, run in
> `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf`
> of `PushforwardCommutesCompletionCanonical.lean`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isIso_map_unit
    {K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))}
    (hK : IsIso ((derivedPushforward.{u} f.toRingedToposSiteHom).map
      ((derivedCompletionUnit X
        (generatedIdealSheaf (pushGlobalSections f hT' t))).app K))) :
    IsIso ((derivedCompletionPushforwardComparisonInverseImageIdealSheaf f hT hT' t).app K)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionConstructedIdeal.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionConstructedIdeal.lean#L417). The attribute's comment: “the display `Rf_*(K^∧) = (Rf_*K)^∧` for a **derived-complete** `K`, at a morphism of ringed sites sending a terminal object of the target site to a terminal object of the source site, with `ℐ` generated by finitely many global sections of `𝒪` and the completion on the source taken along the ideal sheaf `f^{-1}ℐ · 𝒪_X` of Section 52.7 — built here out of `f` and the generators of `ℐ`, and identified as that ideal sheaf by `AlgebraicGeometry.RingedSite.eq_generatedIdealSheaf_pushGlobalSections`. Both derived completion functors are produced from those generators. The tag's assertion is this display for an arbitrary `K`, and at this very pair of sheaves of ideals it is `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf` of `PushforwardCommutesCompletionCanonical.lean`; what the statement here adds is that at a derived-complete object the display needs none of that computation”.

> **[Stacks, Tags 0A0G and 0A0I] at a derived-complete object, at the source's own ideal
> sheaves.** The comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible for every `K ∈ D(𝒪')`
> derived complete along `ℐ' = f^{-1}ℐ · 𝒪_X`, so that `Rf_*(K^∧) = Rf_*K = (Rf_*K)^∧` there.
>
> This is
> `RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isDerivedComplete`
> at `ℐ' = f^{-1}ℐ · 𝒪_X`. The same invertibility holds for an **arbitrary** `K` at this very pair of
> sheaves of ideals, by
> `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf`
> of `PushforwardCommutesCompletionCanonical.lean`; the point of the statement below is that at a
> derived-complete `K` it needs none of that computation.

```lean
theorem isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isDerivedComplete
    {K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))}
    (hK : IsDerivedComplete.{u, u, u, u} X
      (generatedIdealSheaf (pushGlobalSections f hT' t)) K) :
    IsIso ((derivedCompletionPushforwardComparisonInverseImageIdealSheaf f hT hT' t).app K)
```

**`AlgebraicGeometry.RingedSite.isIso_natTrans_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionDisplay.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionDisplay.lean#L141). The attribute's comment: “`Rf_*` commutes with derived completion, as the tag phrases it: the canonical natural transformation `Rf_* ⋙ (-)^∧ ⟶ (-)^∧ ⋙ Rf_*` is invertible **as a morphism of functors**, for a morphism of ringed sites, a sheaf of ideals `ℐ ⊂ 𝒪` of **finite type** and `ℐ' = f^{-1}ℐ · 𝒪_X` the ideal sheaf Section 52.7 constructs out of `ℐ`. The finite type of `ℐ'` and the relation of [Stacks, Tag 099J] between the two sheaves of ideals are proved, not assumed. No hypothesis is placed on the object, none on the generating family, and the identification is the canonical comparison map characterised by its compatibility with the two completion units, so the two functors are identified by the map the tag names”.

> **[Stacks, Tag 0A0G]: `Rf_*` commutes with derived completion.** For a morphism of ringed
> sites `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)`, a sheaf of ideals `ℐ ⊂ 𝒪` of **finite type** and
> `ℐ' = f^{-1}ℐ · 𝒪_X` the ideal sheaf Section 52.7 builds out of `ℐ`, the canonical natural
> transformation
>
> `Rf_* ⋙ (-)^∧_ℐ ⟶ (-)^∧_{ℐ'} ⋙ Rf_*`
>
> of [Stacks, Tag 0A0G] is **invertible as a morphism of functors**. This is the tag's own
> phrasing: the two functors are identified, not merely their values at one object.
>
> It is `isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType` —
> the invertibility at each object, for an arbitrary object and the tag's finite-type ideal sheaf
> — assembled over all objects by `CategoryTheory.NatIso.isIso_of_isIso_app`, which applies
> because the comparison map is a natural transformation by construction.

```lean
theorem
    isIso_natTrans_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType :
    IsIso (derivedCompletionPushforwardComparison f I (inverseImageIdealSheaf f I)
      (pushforwardIdealCompatible_inverseImageIdealSheaf f I))
```

**`AlgebraicGeometry.RingedSite.derivedCompletionPushforwardComparisonGeneratedIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean#L200). The attribute's comment: “the canonical comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` that the tag asserts to be invertible, constructed with nothing assumed, for two **independent** families of global sections of the two structure sheaves generating `ℐ` and `ℐ'` and related only by the hypothesis of [Stacks, Tag 099J] — the regime in which [Stacks, Tag 099F] is proved in this library, by `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`, so that both derived completion functors are produced from the data. Its invertibility at every object of `D(𝒪')`, which is the tag's assertion, holds as soon as the two families correspond, `g_i = f^♯(t_i)`, as the tag's own `ℐ'` does: `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf` of `PushforwardCommutesCompletionCanonical.lean`. At the tag's own `ℐ`, which is of finite type and hence only *locally* generated by finitely many sections, the derived completion functors come instead from [Stacks, Tag 099F] at a sheaf of ideals of finite type, `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete`”.

> **The canonical comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` of [Stacks, Tag 0A0G], at ideal
> sheaves generated by global sections.** It exists because `Rf_*(K^∧)` is derived complete, by
> [Stacks, Tag 099J], so the universal property of derived completion applies to the natural map
> `Rf_*K ⟶ Rf_*(K^∧)`; it is built as a mate and is therefore natural in `K`.
>
> This is `AlgebraicGeometry.RingedSite.derivedCompletionPushforwardComparison` with both of its
> instance hypotheses discharged from the generators, by
> `isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf` on either site. The comparison map is
> what [Stacks, Tag 0A0G] asserts to be invertible and what the display of [Stacks, Tag 0A0I]
> compares its two sides by.
>
> It is invertible at every object of `D(𝒪')` as soon as the two generating families correspond,
> `g_i = f^♯(t_i)`:
> `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf`
> of `PushforwardCommutesCompletionCanonical.lean`, and
> `isIso_natTrans_derivedCompletionPushforwardComparison_generatedIdealSheaf` there for the whole
> natural transformation. Here the two families are independent and related only by `hI`, which is
> all the construction needs.

```lean
def derivedCompletionPushforwardComparisonGeneratedIdealSheaf :
    derivedPushforward.{u} f.toRingedToposSiteHom ⋙
        derivedCompletion Y (generatedIdealSheaf t) ⟶
      derivedCompletion X (generatedIdealSheaf g) ⋙
        derivedPushforward.{u} f.toRingedToposSiteHom
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isIso_map_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean#L232). The attribute's comment: “the criterion that the comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible as soon as `Rf_*(K ⟶ K^∧)` is, proved with nothing assumed at two independent families of global sections of the two structure sheaves generating `ℐ` and `ℐ'`. This is the reduction the source's own proof makes before its local computation, and by `AlgebraicGeometry.RingedSite.isIso_map_derivedCompletionUnit_iff` it covers exactly the objects with `Rf_*K` already derived complete. The tag's assertion for an arbitrary object is `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf` of `PushforwardCommutesCompletionCanonical.lean`, which runs the source's computation at two corresponding families `g_i = f^♯(t_i)`”.

> **A criterion for `Rf_*` to commute with derived completion at `K`, with nothing assumed.**
> At ideal sheaves generated by finitely many global sections, the comparison map
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible as soon as `Rf_*` applied to the completion map
> `K ⟶ K^∧` is.
>
> Indeed `Rf_*(K^∧)` is derived complete, so an invertible `Rf_*(K ⟶ K^∧)` makes `Rf_*K` derived
> complete too, whence its own completion map is invertible; and the comparison is the remaining
> factor.
>
> This is `isIso_derivedCompletionPushforwardComparison_of_isIso_map_unit` with both instance
> hypotheses discharged from the generators. By
> `AlgebraicGeometry.RingedSite.isIso_map_derivedCompletionUnit_iff` its hypothesis `hK` holds
> exactly when `Rf_*K` is already derived complete, so this is the criterion at those objects. For
> an arbitrary `K`, with no condition on `Rf_*K`, the invertibility is
> `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf`
> of `PushforwardCommutesCompletionCanonical.lean`, once the two generating families correspond.

```lean
theorem isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isIso_map_unit
    {K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))}
    (hK : IsIso ((derivedPushforward.{u} f.toRingedToposSiteHom).map
      ((derivedCompletionUnit X (generatedIdealSheaf g)).app K))) :
    IsIso ((derivedCompletionPushforwardComparison f (generatedIdealSheaf t)
      (generatedIdealSheaf g) hI).app K)
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isDerivedComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionGenerated.lean#L259). The attribute's comment: “the display `Rf_*(K^∧) = (Rf_*K)^∧` for a **derived-complete** `K`, proved with nothing assumed at two **independent** families of global sections of the two structure sheaves generating `ℐ` and `ℐ'` and related only by the hypothesis of [Stacks, Tag 099J] — the regime in which [Stacks, Tag 099F] is proved here, so that both derived completion functors are produced from those generators. For an **arbitrary** `K` the display holds once the two families correspond, `g_i = f^♯(t_i)`, as the source's own `ℐ'` does: `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf` of `PushforwardCommutesCompletionCanonical.lean`”.

> **[Stacks, Tags 0A0G and 0A0I] at a derived-complete object, with nothing assumed.** At
> ideal sheaves generated by finitely many global sections, the comparison map
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible for every `K ∈ D(𝒪')` that is derived complete along
> `ℐ'`, so that `Rf_*(K^∧) = Rf_*K = (Rf_*K)^∧` there.
>
> This is `isIso_derivedCompletionPushforwardComparison_of_isDerivedComplete` with both instance
> hypotheses discharged from the generators. What it asks of the object it does not ask of the
> data: the two generating families are independent, related only by `hI`. For an arbitrary object
> the two families have to correspond, `g_i = f^♯(t_i)`, and then the display holds by
> `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf`
> of `PushforwardCommutesCompletionCanonical.lean`.

```lean
theorem isIso_derivedCompletionPushforwardComparison_generatedIdealSheaf_of_isDerivedComplete
    {K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))}
    (hK : IsDerivedComplete.{u, u, u, u} X (generatedIdealSheaf g) K) :
    IsIso ((derivedCompletionPushforwardComparison f (generatedIdealSheaf t)
      (generatedIdealSheaf g) hI).app K)
```

**`AlgebraicGeometry.RingedSite.nonempty_iso_derivedPushforward_derivedCompletion_generatedIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionHomTower.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionHomTower.lean#L233). The attribute's comment: “`Rf_*` commutes with derived completion, `Rf_*(K^∧) = (Rf_*K)^∧`, for an **arbitrary** object `K` of `D(𝒪')`, at **any** morphism of ringed sites and at `ℐ = (t_1, …, t_r) ⊂ 𝒪` and `ℐ' = (f^♯t_1, …, f^♯t_r) ⊂ 𝒪'` generated by finitely many global sections of the two structure sheaves — the regime the source's own proof reduces to, and the regime in which [Stacks, Tag 099F] is available here, so that both derived completion functors are built from those generators and no part of that tag is an input. The argument is the source's: the two completions are the derived limits of the Koszul Hom towers ([Stacks, Tag 0A0E]), `Rf_*` exchanges with `R lim` ([Stacks, Tag 0A07]), and the two towers are identified by `Rf_* R𝓗om_{𝒪'}(Lf^*A, M) ≅ R𝓗om_𝒪(A, Rf_*M)` naturally in both variables together with `Lf^*K(𝒪, t^n) ≅ K(𝒪', g^n)`. Restrictions on the data only: the object is arbitrary”.

> **[Stacks, Tags 0A0G and 0A0I] for an arbitrary object, at two sheaves of ideals generated by
> finitely many global sections.** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism of ringed
> sites, let `t_1, …, t_r` be global sections
> of `𝒪` generating `ℐ ⊂ 𝒪`, let `g_1, …, g_r` be global sections of `𝒪'` with `g_i = f^♯(t_i)`
> generating `ℐ' ⊂ 𝒪'`, and let `K ∈ D(𝒪')` be **arbitrary**. Then
>
> `Rf_*(K^∧) ≅ (Rf_*K)^∧`:
>
> `Rf_*` commutes with derived completion. Both derived completion functors are the reflector of
> [Stacks, Tag 099F], produced from the generators by
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`, so no
> part of that tag is an input here.
>
> The proof is the source's own. `K^∧` is the derived limit of the Koszul Hom tower
> `n ↦ R𝓗om_{𝒪'}(K(𝒪', g^{n+1}), K)` by
> `isDerivedLimit_derivedSheafHomSystem_derivedCompletion` ([Stacks, Tag 0A0E]); `Rf_*` carries
> that derived limit to one of the pushed-forward tower by
> `Stacks.Cohomology.DerivedPushforwardOnRingedTopoi.isDerivedLimit_map_derivedPushforward`
> ([Stacks, Tag 0A07]); `derivedPushforwardKoszulSheafHomSystemIso` identifies the pushed-forward
> tower with `n ↦ R𝓗om_𝒪(K(𝒪, t^{n+1}), Rf_*K)`, whose derived limit is `(Rf_*K)^∧` by the same
> presentation on the target; and two derived limits of isomorphic towers are isomorphic, by
> `Rlim.Pro.nonempty_iso_of_isDerivedLimit_of_natIso` ([Stacks, Tag 0H9L]).
>
> The conclusion is the display as the source writes it, an isomorphism of the two objects, rather
> than invertibility of the canonical comparison map
> `AlgebraicGeometry.RingedSite.derivedCompletionPushforwardComparison`: the uniqueness of derived
> limits produces a non-canonical isomorphism. The source's `ℐ` is of finite type, hence only
> locally generated by finitely many sections; [Stacks, Tag 099F] at such an `ℐ` rests on
> [Stacks, Tags 099D and 099E].

```lean
theorem nonempty_iso_derivedPushforward_derivedCompletion_generatedIdealSheaf
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct ((koszulPowerSystem X g ⋙ DerivedCategory.Q).obj)]
    [HasCoproduct ((koszulPowerSystem Y t ⋙ DerivedCategory.Q).obj)] :
    Nonempty ((derivedPushforward.{u} f.toRingedToposSiteHom).obj
        ((derivedCompletion X (generatedIdealSheaf g)).obj K) ≅
      (derivedCompletion Y (generatedIdealSheaf t)).obj
        ((derivedPushforward.{u} f.toRingedToposSiteHom).obj K))
```

**`AlgebraicGeometry.RingedSite.nonempty_iso_derivedPushforward_derivedCompletion_pushGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionHomTower.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionHomTower.lean#L364). The attribute's comment: “`Rf_*` commutes with derived completion, `Rf_*(K^∧) = (Rf_*K)^∧`, for an **arbitrary** object `K` of `D(𝒪')`, with the source's own ideal sheaf `ℐ' = f^{-1}ℐ · 𝒪_X` built from `ℐ` rather than given: at a morphism of ringed sites carrying a terminal object of the target site to a terminal object — as happens at ringed spaces and at schemes — `ℐ'` is the ideal sheaf generated by `f^♯t_1, …, f^♯t_r`, which receives `f^♯(f^{-1}ℐ)` and is least among those that do, and the display holds at that pair for every object of `D(𝒪')`. `ℐ = (t_1, …, t_r)` is generated by finitely many global sections, which is the regime the source's own proof reduces to and the regime in which [Stacks, Tag 099F] is available here, so both derived completion functors are built from the generators”.

> **[Stacks, Tags 0A0G and 0A0I] for an arbitrary object, at the source's own ideal sheaf
> `ℐ' = f^{-1}ℐ · 𝒪_X`.** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism of ringed sites
> carrying a terminal object `T` of the target site to a terminal object, let
> `ℐ = (t_1, …, t_r) ⊂ 𝒪` be generated by finitely many
> global sections, and let `K ∈ D(𝒪')` be **arbitrary**. Then
>
> `Rf_*(K^∧) ≅ (Rf_*K)^∧`,
>
> the completion on the source being taken along the ideal sheaf generated by `f^♯t_1, …, f^♯t_r`.
>
> That ideal sheaf **is** the source's `ℐ' = f^{-1}ℐ · 𝒪_X`: it receives `f^♯(f^{-1}ℐ)`, by
> `AlgebraicGeometry.RingedSite.pushforwardIdealCompatible_pushGlobalSections`, and is least among
> those that do, by `AlgebraicGeometry.RingedSite.generatedIdealSheaf_pushGlobalSections_le`,
> which together pin it down —
> `AlgebraicGeometry.RingedSite.eq_generatedIdealSheaf_pushGlobalSections`. So the relation
> between the two sheaves of ideals is built from `f` and `t` here rather than given, and the
> statement depends only on `f`, on the two terminal objects and on `t`.
>
> The terminal objects are what makes a global section of `𝒪` transportable along a general
> morphism of sites: `f^♯` produces sections only over objects in the image of `f.u`, and a
> section over a terminal object is a global section. They are present at ringed spaces and at
> schemes, where `f.u` is `Opens.map` and carries `⊤` to `⊤`.
>
> This is `nonempty_iso_derivedPushforward_derivedCompletion_generatedIdealSheaf` at
> `g = pushGlobalSections f hT' t`, whose relation to `t` is
> `pushGlobalSectionsCompatible_pushGlobalSections`.

```lean
theorem nonempty_iso_derivedPushforward_derivedCompletion_pushGlobalSections
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct ((koszulPowerSystem X (pushGlobalSections f hT' t) ⋙
      DerivedCategory.Q).obj)]
    [HasCoproduct ((koszulPowerSystem Y t ⋙ DerivedCategory.Q).obj)] :
    Nonempty ((derivedPushforward.{u} f.toRingedToposSiteHom).obj
        ((derivedCompletion X (generatedIdealSheaf (pushGlobalSections f hT' t))).obj K) ≅
      (derivedCompletion Y (generatedIdealSheaf t)).obj
        ((derivedPushforward.{u} f.toRingedToposSiteHom).obj K))
```

**`AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionLocalToGlobal.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionLocalToGlobal.lean#L261). The attribute's comment: “**the ringed-sites case**, in full for that case: the **canonical** comparison map, at the tag's own data and for an **arbitrary** object. The tag states a morphism of ringed *topoi*; this is the statement for a morphism of ringed *sites*. That is how the sibling [Stacks, Tag 099J] is handled in this directory — `AlgebraicGeometry.RingedSite.derivedPushforward_isDerivedComplete` is its full sites case and is deliberately untagged, the attribute sitting instead on the topos-level theorem reached by [Stacks, Tag 03CR] transport. The topos-level comparison map and its universal property are in `PushforwardCommutesCompletionTopoi.lean`, and the invertibility criterion in `PushforwardCommutesCompletionToposCriterion.lean`; what the transport still owes is a topos-level `f^♯(f^{-1}ℐ)·𝒪`, submodule transport along the dense-subsite replacement, and derived completion across that equivalence. Concretely here: for a morphism of ringed sites, a sheaf of ideals `ℐ ⊂ 𝒪` of finite type and `ℐ' = f^{-1}ℐ · 𝒪_X` the ideal sheaf Section 52.7 constructs out of `ℐ`, the canonical map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible for every `K` of `D(𝒪')`. Both derived completion functors come from [Stacks, Tag 099F] at a sheaf of ideals of finite type — `ℐ'` is of finite type because `ℐ` is, by `AlgebraicGeometry.RingedSite.isFiniteType_inverseImageIdealSheaf` — and the relation of [Stacks, Tag 099J] between the two sheaves of ideals is proved from the construction rather than assumed. The hypotheses are the source's: no object is excluded and no generating family is assumed global; the source's own reduction to the globally generated case by localization on the target site is the proof”.

> **[Stacks, Tag 0A0G] at a sheaf of ideals of finite type, for an arbitrary object.** Let
> `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism of ringed sites, let `ℐ ⊂ 𝒪` be a sheaf of ideals
> **of finite type** and let `ℐ' = f^{-1}ℐ · 𝒪_X` be the ideal sheaf Section 52.7 builds out of
> `ℐ`. Then the canonical comparison map
>
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`
>
> is invertible for **every** object `K` of `D(𝒪')`, the completion on the target being taken
> along `ℐ` and the one on the source along `ℐ'`.
>
> The proof is the source's own localization. `ℐ` of finite type is generated by finitely many
> sections above a covering family `{V_i}` of the final object of the target site
> (`exists_coversTop_eq_generatedIdealSheaf_of_isFiniteType`); on each `𝒟/V_i` the comparison map
> of the localized morphism of [Stacks, Tag 04J0] at `(ℐ|_{V_i}, ℐ'|_{u(V_i)})` is invertible,
> because both of those sheaves of ideals are globally generated there
> (`isIso_derivedCompletionPushforwardComparison_localized_overIdeal`); the restriction coherence
> `derivedCompletionPushforwardComparison_localized` identifies the restriction of the comparison
> map of `f` with it up to three isomorphisms — the two comparison maps of [Stacks, Tag 0A0F],
> invertible because `ℐ` and `ℐ'` are of finite type, and [Stacks, Tag 0D6G]; and invertibility in
> the derived category of sheaves of modules is local on the site
> (`Stacks.SheafOfModules.isIso_of_coversTop_mapDerivedCategory`).
>
> Finite type of `ℐ'` is not a hypothesis: it is
> `AlgebraicGeometry.RingedSite.isFiniteType_inverseImageIdealSheaf`, and it is what makes the
> derived completion functor along `ℐ'` exist at all, by [Stacks, Tag 099F].

```lean
theorem isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    IsIso ((derivedCompletionPushforwardComparison f I (inverseImageIdealSheaf f I)
      (pushforwardIdealCompatible_inverseImageIdealSheaf f I)).app K)
```

**`AlgebraicGeometry.RingedToposHom.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionToposGlobal.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/PushforwardCommutesCompletionToposGlobal.lean#L232). The attribute's comment: “**the tag's own statement, for a morphism of ringed topoi.** For a morphism of ringed topoi `f`, a sheaf of ideals `ℐ ⊂ 𝒪` of finite type and `ℐ' = f^{-1}ℐ · 𝒪_X` the sheaf of ideals generated by `f^♯(f^{-1}ℐ)` that Section 52.7 builds out of `ℐ`, the canonical comparison map `(Rf_*K)^∧ ⟶ Rf_*(K^∧)` is invertible for every object `K` of `D(𝒪')`. The hypotheses are exactly the source's: the relation of [Stacks, Tag 099J] between the two sheaves of ideals is a theorem about the construction, `AlgebraicGeometry.RingedToposHom.idealCompatible_inverseImageIdealSheaf`, and so is finite type of `ℐ'`, `AlgebraicGeometry.RingedToposHom.isFiniteType_inverseImageIdealSheaf`; no object is excluded and no generating family is assumed global. The proof is the source's reduction to a morphism of ringed sites by [Stacks, Tag 03CR], whose ringed-sites case is `AlgebraicGeometry.RingedSite.isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType`. Two results make that reduction go through: the sheaves of ideals that the square's arrows build agree where the applications meet, by `AlgebraicGeometry.RingedToposHom.inverseImageIdealSheaf_denseSquare`, and the square's 2-isomorphism costs no coherence because `AlgebraicGeometry.RingedToposHom.isIso_derivedCompletionPushforwardComparison_of_nonempty_iso` reduces invertibility of the canonical map to a display of objects quantified over all objects”.

> **[Stacks, Tag 0A0G].** Let `f : (Sh(𝒟), 𝒪') ⟶ (Sh(𝒞), 𝒪)` be a morphism of ringed topoi, let
> `ℐ ⊂ 𝒪` be a sheaf of ideals **of finite type** and let `ℐ' = f^{-1}ℐ · 𝒪_X` be the sheaf of
> ideals generated by `f^♯(f^{-1}ℐ)` that Section 52.7 builds out of `ℐ`. Then the canonical
> comparison map
>
> `(Rf_*K)^∧ ⟶ Rf_*(K^∧)`
>
> is invertible for **every** object `K` of `D(𝒪')`, the completion on the target being taken along
> `ℐ` and the one on the source along `ℐ'`.
>
> Both of the properties `ℐ'` has to have are theorems about the construction rather than
> hypotheses: the relation of [Stacks, Tag 099J] between `ℐ` and `ℐ'`, which the comparison map
> needs in order to exist, is
> `AlgebraicGeometry.RingedToposHom.idealCompatible_inverseImageIdealSheaf`, and finite type of
> `ℐ'` — which is what makes the derived completion functor along it exist at all, by
> [Stacks, Tag 099F] — is
> `AlgebraicGeometry.RingedToposHom.isFiniteType_inverseImageIdealSheaf`.
>
> The proof is the source's reduction to a morphism of ringed *sites* by [Stacks, Tag 03CR]; see the
> module documentation.

```lean
theorem isIso_derivedCompletionPushforwardComparison_inverseImageIdealSheaf_of_isFiniteType
    (K : DerivedCategory
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.toRingedSite.O)))) :
    IsIso ((derivedCompletionPushforwardComparison f I (inverseImageIdealSheaf.{u} f I)
      (idealCompatible_inverseImageIdealSheaf.{u} f I)).app K)
```

## Tag 0BLX, a lemma

[Tag 0BLX](https://stacks.math.columbia.edu/tag/0BLX) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_iso_and_pages_derivedCompletion_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GlobalSectionsCompletionWhole.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/GlobalSectionsCompletionWhole.lean#L336). The attribute's comment: “the whole lemma, at the source's own hypotheses — `A` a ring, `I ⊂ A` a finitely generated ideal, `𝒞` a site, `𝒪` a sheaf of `A`-algebras, `ℱ` a sheaf of `𝒪`-modules and `I𝒪` the ideal sheaf `I` generates: the identity `RΓ(𝒞,ℱ)^∧ = RΓ(𝒞,ℱ^∧)` in `D(A)` together with both spectral sequences, `E₂^{i,j} = H^i(H^j(𝒞,ℱ)^∧)` and `E₂^{p,q} = H^p(𝒞, H^q(ℱ^∧))`, converging to `H^*(RΓ(𝒞,ℱ)^∧) = H^*(𝒞,ℱ^∧)`. The derived completion along `I𝒪` ([Stacks, Tag 099F]) and the derived completion along `I` ([Stacks, Tag 0920]) are both produced, each with its reflector adjunction, and a bounded below representative of `ℱ^∧` is produced as well”.

> **[Stacks, Tag 0BLX].** Let `A` be a ring, `I ⊂ A` a finitely generated ideal, `𝒞` a site,
> `𝒪` a sheaf of `A`-algebras — a ring map `ρ : A ⟶ Γ(𝒞, 𝒪)` — `𝓘 = I𝒪` the ideal sheaf `I`
> generates and `ℱ` a sheaf of `𝒪`-modules. Write `ℱ^∧` for the derived completion of `ℱ` along
> `I𝒪` and `(-)^∧` for the derived completion along `I` on `D(A)`. Then
>
> 1. `RΓ(𝒞, ℱ)^∧ = RΓ(𝒞, ℱ^∧)` in `D(A)`;
> 2. there is a bounded cohomological spectral sequence with
>    `E₂^{i,j} = H^i(H^j(𝒞, ℱ)^∧)` converging to `H^{i+j}(RΓ(𝒞, ℱ)^∧)`, every term of which is a
>    derived complete `A`-module;
> 3. `ℱ^∧` has a bounded below representative, and the second spectral sequence of
>    [Stacks, Tag 015J] for `Γ(𝒞, -)` at it has `E₂^{p,q} = H^p(𝒞, H^q(ℱ^∧))` and abuts to
>    `H^{p+q}(RΓ(𝒞, ℱ^∧))`.
>
> By (1) the two abutments are the cohomology of the two sides of one object of `D(A)`, which is
> the source's `H^*(RΓ(𝒞, ℱ)^∧) = H^*(𝒞, ℱ^∧)`: all three parts are read with one and the same
> derived global sections functor
> `AlgebraicGeometry.RingedSite.derivedGlobalSectionsOverUnbounded` on the unbounded `D(𝒪)`.
>
> Both derived completion functors are conclusions rather than hypotheses. On the sheaf side the
> reflector of [Stacks, Tag 099F] onto the objects of `D(𝒪)` derived complete along `I𝒪` is
> produced from the generators of `I` by
> `AlgebraicGeometry.RingedSite.isRightAdjoint_ι_isDerivedComplete_generatedIdealSheaf`; on the
> module side the reflector of [Stacks, Tag 0920] onto the objects of `D(A)` derived complete along
> `I` comes with the package of [Stacks, Tag 0BKE]. Each is existentially quantified, together with
> its adjunction, because the library fixes no choice of either.
>
> The hypotheses are the source's: `I` finitely generated, and `𝓘 = I𝒪`, which is
> `AlgebraicGeometry.RingedSite.IsIdealSheafGeneratedBy` and determines `𝓘` uniquely. No
> nilpotence, boundedness or finiteness enters: `I` being finitely generated, `I = (a_1, …, a_r)`
> and `I𝒪` **is** the ideal sheaf generated by the global sections `ρ a_1, …, ρ a_r` of `𝒪`, by
> `AlgebraicGeometry.RingedSite.exists_eq_generatedIdealSheaf_of_isIdealSheafGeneratedBy`, so the
> statement is proved at the source's own `I𝒪`.
>
> The three parts come from
> `AlgebraicGeometry.RingedSite.nonempty_iso_derivedCompletion_derivedGlobalSections`,
> `AdicFilteredCompletion.exists_spectralSequence_derivedCompletion_homology` and
> `AlgebraicGeometry.RingedSite.exists_pages_derivedCompletion_globalSections`; the module
> documentation says how they are matched up, the two reflections of `D(A)` being identified by
> `CategoryTheory.ObjectProperty.isoOfReflection` and the two derived global sections functors by
> `AlgebraicGeometry.RingedSite.nonempty_iso_derivedGlobalSectionsOverUnbounded_of_plus`.
>
> The Cartan-Eilenberg resolution of part (3) is universally quantified, as it is in
> [Stacks, Tag 015J] itself, and its existence is [Stacks, Tag 015I].

```lean
theorem exists_iso_and_pages_derivedCompletion_globalSections
    (hI : I.FG) (h𝓘 : IsIdealSheafGeneratedBy A I X ρ 𝓘) :
    let Pm : ObjectProperty (DerivedCategory (ModuleCat.{u} A)) :=
      fun L ↦ _root_.IsDerivedComplete I L
    let Ps : ObjectProperty
        (DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :=
      IsDerivedComplete.{u, u, u, u} X 𝓘
    let RG := derivedGlobalSectionsOverUnbounded X A ρ
    let F0 := (DerivedCategory.singleFunctor
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) 0).obj F
    ∃ (completionSheaf :
        DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) ⥤
          Ps.FullSubcategory)
      (completion : DerivedCategory (ModuleCat.{u} A) ⥤ Pm.FullSubcategory)
      (M : CochainComplex.Filtered (ModuleCat.{u} A))
      (E : E₂CohomologicalSpectralSequence (ModuleCat.{u} A))
      (hF : ∀ n : ℤ, Antitone (M.inducedFiltrationStep n))
      (Kc : CochainComplex (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) ℤ)
      (_ : CochainComplex.plus
        (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) Kc),
      Nonempty (completionSheaf ⊣ Ps.ι) ∧
      Nonempty (completion ⊣ Pm.ι) ∧
      Nonempty ((completion ⋙ Pm.ι).obj (RG.obj F0) ≅
        RG.obj ((completionSheaf ⋙ Ps.ι).obj F0)) ∧
      Nonempty (DerivedCategory.Q.obj M.X ≅ (completion ⋙ Pm.ι).obj (RG.obj F0)) ∧
      (∀ n : ℤ, Nonempty (M.X.homology n ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj
          ((completion ⋙ Pm.ι).obj (RG.obj F0)))) ∧
      (∀ i j : ℤ, Nonempty ((E.page 2).X (i, j) ≅
        (DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
          ((completion ⋙ Pm.ι).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              ((siteCohomologyOver X A ρ j).obj F))))) ∧
      (∀ (r i j : ℤ) (hr : 2 ≤ r), IsDerivedCompleteModule I ((E.page r hr).X (i, j))) ∧
      (∀ n : ℤ, {i : ℤ | ¬ IsZero ((E.page 2).X (i, n - i))}.Finite) ∧
      (∀ n : ℤ, ∃ p q : ℤ, p ≤ q ∧ M.inducedFiltrationStep n p = ⊤ ∧
        M.inducedFiltrationStep n q = ⊥) ∧
      (∀ i j : ℤ, ∃ (r₀ : ℤ) (hr₀ : 2 ≤ r₀), ∀ (r : ℤ) (hr : r₀ ≤ r),
        (E.page r (by omega)).d (i, j) (i + r, j - r + 1) = 0 ∧
        (E.page r (by omega)).d (i - r, j + r - 1) (i, j) = 0 ∧
        Nonempty ((E.page r (by omega)).X (i, j) ≅
          cokernel (Subobject.ofLE (M.inducedFiltrationStep (i + j) (-j + 1))
            (M.inducedFiltrationStep (i + j) (-j)) (hF (i + j) (by omega))))) ∧
      Nonempty (DerivedCategory.Q.obj Kc ≅ (completionSheaf ⋙ Ps.ι).obj F0) ∧
      ∀ (Ires : Kc.CartanEilenbergResolution)
        [HomologicalComplex₂.HasTotal
          ((((moduleGlobalSectionsOver X A ρ).mapHomologicalComplex
            (ComplexShape.up ℤ)).mapHomologicalComplex (ComplexShape.up ℤ)).obj Ires.bicomplex)
          (ComplexShape.up ℤ)],
        (∀ p q : ℤ, Nonempty
          ((((((moduleGlobalSectionsOver X A ρ).mapHomologicalComplex
              (ComplexShape.up ℤ)).mapHomologicalComplex
              (ComplexShape.up ℤ)).obj Ires.bicomplex).homology q).homology p ≅
            (siteCohomologyOver X A ρ p).obj
              ((DerivedCategory.homologyFunctor
                  (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) q).obj
                ((completionSheaf ⋙ Ps.ι).obj F0)))) ∧
        ∀ n : ℤ, Nonempty ((HomologicalComplex₂.total
            ((((moduleGlobalSectionsOver X A ρ).mapHomologicalComplex
              (ComplexShape.up ℤ)).mapHomologicalComplex
              (ComplexShape.up ℤ)).obj Ires.bicomplex) (ComplexShape.up ℤ)).homology n ≅
          (DerivedCategory.homologyFunctor (ModuleCat.{u} A) n).obj
            (RG.obj ((completionSheaf ⋙ Ps.ι).obj F0)))
```

## Tag 0CQI, a remark

[Tag 0CQI](https://stacks.math.columbia.edu/tag/0CQI) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isIso_map_derivedCompletionUnit_derivedSectionsOverObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculation.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculation.lean#L261). The attribute's comment: “the left hand side: the canonical map `RΓ(U, K) ⟶ RΓ(U, K^∧)` is invertible, for a sheaf of ideals of finite type all of whose local sections are nilpotent — the hypothesis under which this library has the derived completion functor of [Stacks, Tag 099F]. The equality with `RΓ(U, K)^∧` is this together with `isDerivedComplete_derivedSectionsOverObject`. The general case needs [Stacks, Tags 0A0F, 0BLX]; the first is `derivedCompletion_restrict`, the second is not available as an identity here”.

> **[Stacks, Tag 0CQI], the left hand side, for a sheaf of ideals with nilpotent sections.**
> The canonical map `RΓ(U, K) ⟶ RΓ(U, K^∧)` is invertible.
>
> Together with `isDerivedComplete_derivedSectionsOverObject`, whose content is that the right hand
> side `RΓ(U, K)^∧` is `RΓ(U, K)` as well, this is the equality `RΓ(U, K^∧) = RΓ(U, K)^∧` of the
> source in this regime, compatibly with the canonical maps on both sides.

```lean
theorem isIso_map_derivedCompletionUnit_derivedSectionsOverObject
    [𝓘.toSheafOfModules.IsFiniteType]
    [(ObjectProperty.ι (IsDerivedComplete.{u, u, u, u} X 𝓘)).IsRightAdjoint]
    (hgen : IsGeneratedAsIdealSheafBySectionsOver X 𝓘 U f)
    (hnil : ∀ (V : X.C) (g : ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj.obj (op V)),
      g ∈ 𝓘.toSubmodule.obj (op V) → IsNilpotent g)
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    IsIso ((derivedSectionsOverObject X U).map ((derivedCompletionUnit X 𝓘).app K))
```

**`AlgebraicGeometry.RingedSite.isIso_map_derivedCompletionUnit_derivedSectionsOverObject_of_forall_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculation.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculation.lean#L289). The attribute's comment: “the left hand side: the canonical map `RΓ(U, K) ⟶ RΓ(U, K^∧)` is invertible, for a sheaf of ideals of finite type all of whose local sections are nilpotent — the hypothesis under which this library has the derived completion functor of [Stacks, Tag 099F]. That functor is *produced* from the nilpotence hypothesis rather than assumed: the `IsRightAdjoint` instance is discharged inside the statement. The equality with `RΓ(U, K)^∧` is this together with `isDerivedComplete_derivedSectionsOverObject`. The general case needs [Stacks, Tags 0A0F, 0BLX]; the first is `derivedCompletion_restrict`, the second is not available as an identity here”.

> **[Stacks, Tag 0CQI], the left hand side, for a sheaf of ideals with nilpotent sections, with
> the derived completion functor produced rather than assumed.** This is
> `isIso_map_derivedCompletionUnit_derivedSectionsOverObject` without its `IsRightAdjoint` instance
> argument: the left adjoint of the inclusion of derived complete objects is discharged inside the
> statement from the nilpotence hypothesis, by
> `isRightAdjoint_ι_isDerivedComplete_of_isFiniteType_of_forall_isNilpotent`.

```lean
theorem isIso_map_derivedCompletionUnit_derivedSectionsOverObject_of_forall_isNilpotent
    [𝓘.toSheafOfModules.IsFiniteType]
    (hgen : IsGeneratedAsIdealSheafBySectionsOver X 𝓘 U f)
    (hnil : ∀ (V : X.C) (g : ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj.obj (op V)),
      g ∈ 𝓘.toSubmodule.obj (op V) → IsNilpotent g)
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    letI : (ObjectProperty.ι (IsDerivedComplete.{u, u, u, u} X 𝓘)).IsRightAdjoint :=
      isRightAdjoint_ι_isDerivedComplete_of_isFiniteType_of_forall_isNilpotent X 𝓘 hnil
    IsIso ((derivedSectionsOverObject X U).map ((derivedCompletionUnit X 𝓘).app K))
```

**`AlgebraicGeometry.RingedSite.isDerivedComplete_derivedSectionsOverObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculation.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculation.lean#L313). The attribute's comment: “the right hand side `RΓ(U, K)^∧`, identified with `RΓ(U, K)` by its being already derived complete along `I = (f_1, …, f_r) ⊂ 𝒪(U)`, for a sheaf of ideals all of whose local sections are nilpotent. The completion is along the ideal the chosen sections generate and not along `𝓘(U)`, which the source warns need not be the same ideal”.

> **[Stacks, Tag 0CQI], the right hand side, for a sheaf of ideals with nilpotent sections.**
> `RΓ(U, K)` is derived complete along `I = (f_1, …, f_r) ⊂ A = 𝒪(U)`, so its derived completion is
> itself.
>
> Together with `isIso_map_derivedCompletionUnit_derivedSectionsOverObject` this is the equality
> `RΓ(U, K^∧) = RΓ(U, K)^∧` of the source in this regime. The completion is along the ideal
> generated by the chosen sections, not along `𝓘(U)`.

```lean
theorem isDerivedComplete_derivedSectionsOverObject
    (hgen : IsGeneratedAsIdealSheafBySectionsOver X 𝓘 U f)
    (hnil : ∀ (V : X.C) (g : ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj.obj (op V)),
      g ∈ 𝓘.toSubmodule.obj (op V) → IsNilpotent g)
    (K : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O)))) :
    _root_.IsDerivedComplete (localIdeal X U f)
      ((derivedSectionsOverObject X U).obj K)
```

**`AlgebraicGeometry.RingedSite.nonempty_iso_derivedSectionsOverObject_derivedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculationFiniteType.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/LocalCalculationFiniteType.lean#L171). The attribute's comment: “the whole remark, at the source's own hypotheses — `(𝒞, 𝒪)` a ringed site, `ℐ ⊂ 𝒪` a sheaf of ideals of finite type, `K ↦ K^∧` the derived completion of [Stacks, Tag 099F], `U` an object over which `ℐ` is generated as an ideal sheaf by `f_1, …, f_r ∈ ℐ(U)`, `A = 𝒪(U)` and `I = (f_1, …, f_r) ⊂ A`: the displayed identity `RΓ(U, K^∧) = RΓ(U, K)^∧` in `D(A)` for every `K` of `D(𝒪)`, the right hand side being the derived completion of `RΓ(U, K)` along `I`. Both completion functors are produced: the one on `D(𝒪)` is the reflector of [Stacks, Tag 099F] at a finite-type ideal sheaf and the one on `D(A)` is the reflector of [Stacks, Tag 0G3E] along `I`. The proof is the source's, by [Stacks, Tag 0A0F] and [Stacks, Tag 0BLX], and `I` is the ideal the chosen sections generate rather than `ℐ(U)`, which the source warns need not be the same ideal”.

> **[Stacks, Tag 0CQI].** Let `(𝒞, 𝒪)` be a ringed site, let `ℐ ⊂ 𝒪` be a sheaf of ideals of
> finite type and let `K ↦ K^∧` be the derived completion of [Stacks, Tag 099F]. Let `U` be an
> object of `𝒞` such that `ℐ` is generated as an ideal sheaf by `f_1, …, f_r ∈ ℐ(U)`, and set
> `A = 𝒪(U)` and `I = (f_1, …, f_r) ⊂ A`. Then, for every `K ∈ D(𝒪)`,
> ```
> RΓ(U, K^∧) = RΓ(U, K)^∧   in D(A),
> ```
> the right hand side being the derived completion of `RΓ(U, K)` along `I`.
>
> `I` is the ideal of `A` generated by the chosen sections and is not `ℐ(U)`: the source warns
> that the two may differ, and neither side of the statement mentions `ℐ(U)`.
>
> Derived completion commutes with localization
> ([Stacks, Tag 0A0F], `derivedCompletionRestrictIso`), so `K^∧|_U` is the derived completion of
> `K|_U` along `ℐ|_U`; on the localized ringed site `(𝒞/U, 𝒪_U)` the sections `f_i` are global
> sections generating `ℐ|_U`, so [Stacks, Tag 0BLX] gives
> `RΓ(𝒞/U, (K|_U)^∧) = RΓ(𝒞/U, K|_U)^∧`; and `RΓ(U, -)` is `RΓ(𝒞/U, (-)|_U)` by
> [Stacks, Tag 0D6F] in its `A`-linear functor-level form,
> `derivedSectionsOverObjectIsoSliceModule`.

```lean
theorem nonempty_iso_derivedSectionsOverObject_derivedCompletion
    (_hf : ∀ i, f i ∈ 𝓘.toSubmodule.obj (op U))
    (hgen : idealOfGlobalSections (X.over U)
      (fun i => globalSectionOfTerminalSection (X := X.over U) Over.mkIdTerminal (f i)) =
        overIdeal 𝓘 U)
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    Nonempty ((derivedSectionsOverObject X U).obj ((derivedCompletion X 𝓘).obj K) ≅
      (DerivedCompletion.derivedCompletionFunctor (sectionRing X U) f).obj
        ((derivedSectionsOverObject X U).obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.6, Tag 0995](https://stacks.math.columbia.edu/tag/0995)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
