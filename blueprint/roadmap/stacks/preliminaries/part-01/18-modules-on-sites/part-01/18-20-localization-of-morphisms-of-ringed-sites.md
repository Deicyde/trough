---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.Hom.localized, AlgebraicGeometry.RingedSite.HomGeneral.localized, AlgebraicGeometry.RingedSite.Hom.localizedRingedToposHom, AlgebraicGeometry.RingedSite.Hom.overPullback_comp_localizedPushforward, AlgebraicGeometry.RingedSite.Hom.localizedRingedSquare, AlgebraicGeometry.RingedSite.MorphismLocalization.localizedStructureMap_comp_comparisonIso_hom, AlgebraicGeometry.RingedSite.MorphismLocalization.eq_localizedStructureMap, AlgebraicGeometry.RingedSite.MorphismLocalization.pushforward_overPullback_comm_modules
statement: formalized
proof: formalized
---

# 18.20 Localization of morphisms of ringed sites

Section 18.20 of the Stacks Project, [Tag 04IZ](https://stacks.math.columbia.edu/tag/04IZ). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04J0, a lemma

[Tag 04J0](https://stacks.math.columbia.edu/tag/04J0) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.Hom.localized`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RingedSiteMorphismLocalization.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RingedSiteMorphismLocalization.lean#L62). The attribute's comment: “(1): the localized morphism of ringed sites, with its canonical structure map `(f')♯ = j_V^{-1}(f♯)`”.

> **Stacks 04J0.** The localization of a morphism of ringed sites at an object `V` of the
> target: the underlying functor is `Over.post u`, a morphism of sites by Stacks 03CF clause (a),
> and the structure map is the restriction `j_V^{-1}(f^♯)` of the structure map of `f`.
>
> That this typechecks is the content of the choice: the target of `j_V^{-1}(f^♯)` is
> `j_V^{-1}f_*O`, which is `f'_*j_U^{-1}O = f'_*O_U` by the strict identity of Stacks 03CF, so no
> comparison isomorphism intervenes.

```lean
noncomputable def localized :
    RingedSite.Hom (X.over (f.u.obj V)) (Y.over V)
```

**`AlgebraicGeometry.RingedSite.HomGeneral.localized`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RingedSiteMorphismLocalizationGeneral.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RingedSiteMorphismLocalizationGeneral.lean#L99). The attribute's comment: “(1): the localized morphism of ringed sites at independent object and morphism universes, with its canonical structure map `(f')♯ = j_V^{-1}(f♯)`. Clause (a) of 03CF is a hypothesis here; the single-universe case is `AlgebraicGeometry.RingedSite.Hom.localized`.”.

> **Stacks 04J0 at independent site universes.** The localization of a morphism of ringed
> sites at an object `V` of the target, with the object and morphism universes of the source
> independent of those of the target: the underlying functor is `Over.post u` and the structure map
> is the restriction `j_V^{-1}(f^♯)` of the structure map of `f`.
>
> That `j_V^{-1}(f^♯)` typechecks as the structure map is the content of the choice, exactly as at
> `AlgebraicGeometry.RingedSite.Hom.localized`: its target is `j_V^{-1}f_*O`, which *is*
> `f'_*j_U^{-1}O = f'_*O_U` by the strict identity `sheafPushforwardContinuous_overPost_eq` of
> Stacks 03CF clause (d), so no comparison isomorphism intervenes.  That identity is proved at
> independent universes, so nothing has to be redone for it here.
>
> Clause (a) of Stacks 03CF, that `Over.post u` again defines a morphism of sites, is the
> hypothesis `hu`.  It is available in this repository only for two sites small in one universe
> (`CategoryTheory.Functor.isMorphismOfSites_overPost_of_isMorphismOfSites`), which is the one case
> in which `AlgebraicGeometry.RingedSite.Hom` already applies; see the module docstring.

```lean
noncomputable def localized
    (hu : IsMorphismOfSites.{w} (Over.post (X := V) f.u) (Y.J.over V) (X.J.over (f.u.obj V))) :
    HomGeneral (X.over (f.u.obj V)) (Y.over V)
```

**`AlgebraicGeometry.RingedSite.Hom.localizedRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean#L131). The attribute's comment: “(1): the localized morphism of ringed topoi”.

> The localized morphism of ringed *topoi* `(f', (f')♯) : (Sh(C/U), O_U) ⟶ (Sh(D/V), O'_V)`,
> with `U = u(V)`.

```lean
noncomputable def Hom.localizedRingedToposHom (V : Y.C) :
    AlgebraicGeometry.RingedToposHom (ringedTopos (X.over (f.u.obj V)))
      (ringedTopos (Y.over V))
```

**`AlgebraicGeometry.RingedSite.Hom.overPullback_comp_localizedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean#L140). The attribute's comment: “(3): the identity `f'_* j_U^{-1} = j_V^{-1} f_*`”.

> The identity `f'_* j_U^{-1} = j_V^{-1} f_*`, as a strict equality of functors
> `Sh(C) ⥤ Sh(D/V)`. This is Stacks 03CF's clause (d) read on the assembled morphisms of ringed
> topoi: the localizations contribute their inverse images and `f`, `f'` their direct images.

```lean
theorem Hom.overPullback_comp_localizedPushforward (V : Y.C) :
    (X.localizationRingedToposHom (f.u.obj V)).toToposHom.inverseImage ⋙
        (f.localizedRingedToposHom V).toToposHom.pushforward =
      f.ringedToposHom.toToposHom.pushforward ⋙
        (Y.localizationRingedToposHom V).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedSite.Hom.localizedRingedSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean#L319). The attribute's comment: “(2): the commutative diagram of ringed topoi”.

> With `U = u(V)`, the square
> ```
>   (Sh(C/U), O_U)   --j_U-->  (Sh(C), O)
>        | f'                     | f
>   (Sh(D/V), O'_V)  --j_V-->  (Sh(D), O')
> ```
> commutes, as a square of ringed topoi.

```lean
noncomputable def Hom.localizedRingedSquare (V : Y.C) :
    AlgebraicGeometry.RingedToposHom.TwoIso
      (A := ringedTopos (X.over (f.u.obj V))) (B := ringedTopos Y)
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over (f.u.obj V)))
        (Y := ringedTopos (Y.over V)) (Z := ringedTopos Y)
        (Y.localizationRingedToposHom V) (f.localizedRingedToposHom V))
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over (f.u.obj V)))
        (Y := ringedTopos X) (Z := ringedTopos Y)
        f.ringedToposHom (X.localizationRingedToposHom (f.u.obj V)))
```

**`AlgebraicGeometry.RingedSite.MorphismLocalization.localizedStructureMap_comp_comparisonIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean#L161). The attribute's comment: “(1)”.

> **Part (1): the defining characterisation of `(f')^#`.** The canonical structure map
> `(f')^# = localizedStructureMap`, transported across the Tag 03CF comparison isomorphism,
> equals `j_V^{-1}` applied to the structure map `f^# = α`.  This is the formal content of
> the composite formula of part (1): up to the localization identifications
> `O'_V = j_V^{-1} O'`, `O_U = j_U^{-1} O` and the identity `f'_* j_U^{-1} = j_V^{-1} f_*`,
> the map `(f')^#` is `j_U^{-1}(f^#)`.

```lean
theorem localizedStructureMap_comp_comparisonIso_hom :
    localizedStructureMap u JC JD V OC OD α ≫
        (localizationComparisonIso u JC JD V RingCat).hom.app OC
      = (JD.overPullback RingCat V).map α
```

**`AlgebraicGeometry.RingedSite.MorphismLocalization.eq_localizedStructureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean#L176). The attribute's comment: “(2)”.

> **Part (2): commutativity of the square of ringed topoi.** With `(f')^#` chosen as in
> `localizedStructureMap`, the square of ringed topoi formed by `(f, f^#)`, `(f', (f')^#)`,
> `(j_U, j_U^#)`, `(j_V, j_V^#)` commutes.  The underlying square of topoi commutes by Stacks
> Lemma 7.28.1 (encoded by `localizationComparisonIso`); the new content is the
> compatibility of the structure-sheaf maps, namely that `(f')^#` is the *unique* map of
> sheaves of rings `g : O'_V ⟶ f'_* O_U` intertwining `f^#` with the localization
> identifications, i.e. satisfying `g ≫ cmp = j_V^{-1}(f^#)` (both `j_U^#`, `j_V^#` being
> identities).  Uniqueness expresses that the commuting choice of structure map is canonical.

```lean
theorem eq_localizedStructureMap
    (g : (JD.overPullback RingCat V).obj OD ⟶
          ((Over.post u).sheafPushforwardContinuous RingCat (JD.over V)
              (JC.over (u.obj V))).obj ((JC.overPullback RingCat (u.obj V)).obj OC))
    (hg : g ≫ (localizationComparisonIso u JC JD V RingCat).hom.app OC
        = (JD.overPullback RingCat V).map α) :
    g = localizedStructureMap u JC JD V OC OD α
```

**`AlgebraicGeometry.RingedSite.MorphismLocalization.pushforward_overPullback_comm_modules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean#L195). The attribute's comment: “(3)”.

> **Part (3), module form: `f'_* j_U^* = j_V^* f_*`.** Equality of functors
> `SheafOfModules OC ⥤ SheafOfModules O'_V`.  On the left we first apply the module
> restriction `j_U^* = j_U^{-1}` (the localization pushforward along `Over.forget U` with the
> identity structure map, since `O_U = j_U^{-1} O`) and then push forward along `f'` (using
> `(f')^# = localizedStructureMap`); on the right we first push forward along `f` (using
> `f^# = α`) and then restrict along `j_V`.  Because `j^# = id` for a localization morphism,
> `j_U^* = j_U^{-1}` and `j_V^* = j_V^{-1}` on modules, so this single equality realizes both
> functor identities of part (3) at the level of sheaves of modules.

```lean
theorem pushforward_overPullback_comm_modules :
    SheafOfModules.pushforward (F := Over.forget (u.obj V))
        (𝟙 ((JC.overPullback RingCat (u.obj V)).obj OC))
      ⋙ SheafOfModules.pushforward (localizedStructureMap u JC JD V OC OD α)
    = SheafOfModules.pushforward α
      ⋙ SheafOfModules.pushforward (F := Over.forget V)
          (𝟙 ((JD.overPullback RingCat V).obj OD))
```

**`AlgebraicGeometry.RingedSite.MorphismLocalization.nonempty_overPullback_pushforward_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/MorphismLocalization.lean#L213). The attribute's comment: “(3)”.

> **Part (3), abelian / value-category form: `f'_* j_U^{-1} = j_V^{-1} f_*`.** At the
> level of sheaves valued in an arbitrary category `A` (in particular abelian sheaves,
> `A := AddCommGrp`), the functors `f'_* ∘ j_U^{-1}` and `j_V^{-1} ∘ f_*` are canonically
> isomorphic, by `localizationComparisonIso`, the identification of functors of Stacks
> Lemma 7.28.1.

```lean
theorem nonempty_overPullback_pushforward_iso (A : Type*) [Category A] :
    Nonempty
      ((JC.overPullback A (u.obj V) ⋙
          (Over.post u).sheafPushforwardContinuous A (JD.over V) (JC.over (u.obj V)))
        ≅ (u.sheafPushforwardContinuous A JD JC ⋙ JD.overPullback A V))
```

## Tag 04J1, a lemma

[Tag 04J1](https://stacks.math.columbia.edu/tag/04J1) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.Hom.relocalized`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean#L131). The attribute's comment: “the morphism `f_c` and its factorization as the morphism of 04J0 after the relocalization morphism of 04IY”.

> **Stacks 04J1.** The morphism of ringed topoi
> `(f_c, f_c♯) : (Sh(C/U), O_U) ⟶ (Sh(D/V), O'_V)` attached to a morphism of ringed sites
> `(f, f♯)` and a morphism `c : U ⟶ u(V)` of the source site: the composition of the localized
> morphism of Stacks 04J0, from the localization at `u(V)`, with the relocalization morphism of
> Stacks 04IY along `c`.
>
> The factorization that Stacks 04J1 asserts is this definition.

```lean
noncomputable def Hom.relocalized :
    AlgebraicGeometry.RingedToposHom (ringedTopos (X.over U)) (ringedTopos (Y.over V))
```

**`AlgebraicGeometry.RingedSite.Hom.relocalizedLocalizationSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean#L152). The attribute's comment: “commutativity of the localization square, pasted from 04IY's triangle and the square of 04J0”.

> **Stacks 04J1**, the localization square: the square
>
> ```
>   (Sh(C/U), O_U)   --j_U-->  (Sh(C), O)
>        | f_c                     | f
>   (Sh(D/V), O'_V)  --j_V-->  (Sh(D), O')
> ```
>
> commutes, as a square of ringed topoi.
>
> This is the square of Stacks 04J0 for the localized morphism `f'`
> (`AlgebraicGeometry.RingedSite.Hom.localizedRingedSquare`), pasted with the relocalization
> triangle of Stacks 04IY for `c : U ⟶ u(V)`.

```lean
noncomputable def Hom.relocalizedLocalizationSquare :
    TwoIso (A := ringedTopos (X.over U)) (B := ringedTopos Y)
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over U))
        (Y := ringedTopos (Y.over V)) (Z := ringedTopos Y)
        (Y.localizationRingedToposHom V) (f.relocalized c))
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over U))
        (Y := ringedTopos X) (Z := ringedTopos Y)
        f.ringedToposHom (X.localizationRingedToposHom U))
```

**`AlgebraicGeometry.RingedSite.Hom.relocalizedNaturalitySquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedNaturality.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedNaturality.lean#L151). The attribute's comment: “the final assertion: for `b : V' ⟶ V`, `a : U' ⟶ U` and `c'` with `a ≫ c = c' ≫ u(b)`, the induced square of ringed topoi on the slices commutes”.

> **Stacks 04J1**, the last assertion: for `a ≫ c = c' ≫ u(b)` the square
>
> ```
>   (Sh(C/U'), O_{U'})  --j_{U'/U}-->  (Sh(C/U), O_U)
>         | f_{c'}                          | f_c
>   (Sh(D/V'), O'_{V'}) --j_{V'/V}-->  (Sh(D/V), O'_V)
> ```
>
> commutes, as a square of ringed topoi.
>
> Both `f_c` and `f_{c'}` are, by definition, the localized morphism of Stacks 04J0 after a
> relocalization of Stacks 04IY. Reassociating, the two relocalizations of the source site compose
> by `AlgebraicGeometry.RingedSite.relocalizationComp`, and the hypothesis says that the two
> composites are the relocalization along one and the same morphism `a ≫ c = c' ≫ u(b)`; what is
> left is `Hom.localizedNaturalitySquare`.

```lean
noncomputable def Hom.relocalizedNaturalitySquare (h : a ≫ c = c' ≫ f.u.map b) :
    TwoIso (A := (X.over U').ringedTopos) (B := (Y.over V).ringedTopos)
      (AlgebraicGeometry.RingedToposHom.comp
        (X := (X.over U').ringedTopos) (Y := (Y.over V').ringedTopos)
        (Z := (Y.over V).ringedTopos)
        (Y.relocalizationRingedToposHom b) (f.relocalized c'))
      (AlgebraicGeometry.RingedToposHom.comp
        (X := (X.over U').ringedTopos) (Y := (X.over U).ringedTopos)
        (Z := (Y.over V).ringedTopos)
        (f.relocalized c) (X.relocalizationRingedToposHom a))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.20, Tag 04IZ](https://stacks.math.columbia.edu/tag/04IZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
