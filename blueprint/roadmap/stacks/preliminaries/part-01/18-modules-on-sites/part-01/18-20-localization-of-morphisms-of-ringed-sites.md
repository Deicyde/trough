---
declaration: section
origin: cited
lean: Stacks.Cohomology.Localization.pushforwardTopos_comp_overFunctor, AlgebraicGeometry.RingedSite.Hom.localized, AlgebraicGeometry.RingedSite.Hom.localizedRingedToposHom, AlgebraicGeometry.RingedSite.Hom.overPullback_comp_localizedPushforward, AlgebraicGeometry.RingedSite.Hom.localizedRingedSquare, AlgebraicGeometry.RingedSite.Hom.relocalized, AlgebraicGeometry.RingedSite.Hom.relocalizedLocalizationSquare, AlgebraicGeometry.RingedSite.Hom.relocalizedNaturalitySquare
statement: formalized
proof: formalized
---

# 18.20 Localization of morphisms of ringed sites

Section 18.20 of the Stacks Project, [Tag 04IZ](https://stacks.math.columbia.edu/tag/04IZ). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04J0, a lemma

[Tag 04J0](https://stacks.math.columbia.edu/tag/04J0) in the Stacks Project.

**`Stacks.Cohomology.Localization.pushforwardTopos_comp_overFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedDirectImageAndRestriction.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedDirectImageAndRestriction.lean#L217). The attribute's comment: “(3): the identity `f'_* j_U^* = j_V^* f_*` on sheaves of modules”.

> **Stacks 04J0, the identity `f'_* j_U^* = j_V^* f_*` on sheaves of modules**, which is also
> the underived identity behind Stacks 0D6G: the direct image of a sheaf of modules along a morphism
> of ringed sites, restricted to the site localized at an object `V` of the target, is the direct
> image along the localized morphism `f.localized V` of the restriction to the localization at
> `U = u(V)`. As in the source this is an equality of functors, not merely an isomorphism: the
> functor identity `u' ∘ j_V = j_U ∘ u` of Stacks 03CF is strict.

```lean
theorem pushforwardTopos_comp_overFunctor :
    f.toRingedToposSiteHom.pushforwardTopos ⋙
        SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) V =
      SheafOfModules.overFunctor.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (f.u.obj V) ⋙
        localizedPushforward f V
```

**`AlgebraicGeometry.RingedSite.Hom.localized`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RingedSiteMorphismLocalization.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/RingedSiteMorphismLocalization.lean#L62). The attribute's comment: “(1): the localized morphism of ringed sites, with its canonical structure map `(f')♯ = j_V^{-1}(f♯)`”.

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

**`AlgebraicGeometry.RingedSite.Hom.localizedRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean#L133). The attribute's comment: “(1): the localized morphism of ringed topoi”.

> The localized morphism of ringed *topoi* `(f', (f')♯) : (Sh(C/U), O_U) ⟶ (Sh(D/V), O'_V)`,
> with `U = u(V)`.

```lean
noncomputable def Hom.localizedRingedToposHom (V : Y.C) :
    AlgebraicGeometry.RingedToposHom (ringedTopos (X.over (f.u.obj V)))
      (ringedTopos (Y.over V))
```

**`AlgebraicGeometry.RingedSite.Hom.overPullback_comp_localizedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean#L142). The attribute's comment: “(3): the identity `f'_* j_U^{-1} = j_V^{-1} f_*`”.

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

**`AlgebraicGeometry.RingedSite.Hom.localizedRingedSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/LocalizedMorphism.lean#L327). The attribute's comment: “(2): the commutative diagram of ringed topoi `(f, f♯) ∘ (j_U, j_U♯) ≅ (j_V, j_V♯) ∘ (f', (f')♯)`, as a 2-isomorphism of ringed topoi”.

> With `U = u(V)`, the square
> ```
>   (Sh(C/U), O_U)   --j_U-->  (Sh(C), O)
>        | f'                     | f
>   (Sh(D/V), O'_V)  --j_V-->  (Sh(D), O')
> ```
> commutes, as a square of ringed topoi: the two composites `j_V ∘ f'` and `f ∘ j_U` are
> 2-isomorphic in the sense of Stacks 04IC, which is what Stacks means by a commutative diagram of
> ringed topoi. The 2-isomorphism is an isomorphism of the two direct images (from Stacks 03CF's
> clause (b)) carrying the structure map of `j_V ∘ f'` to that of `f ∘ j_U`, where `j_U♯` and `j_V♯`
> are the units of `j^{-1} ⊣ j_*` at the structure sheaves and `(f')♯` is the structure map of
> `localizedRingedToposHom`. No hypothesis beyond `f` being a morphism of ringed sites is used.

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

## Tag 04J1, a lemma

[Tag 04J1](https://stacks.math.columbia.edu/tag/04J1) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.Hom.relocalized`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean#L131). The attribute's comment: “the morphism `f_c` and its factorization as the morphism of 04J0 after the relocalization morphism of 04IY”.

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

**`AlgebraicGeometry.RingedSite.Hom.relocalizedLocalizationSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedMorphism.lean#L152). The attribute's comment: “commutativity of the localization square, pasted from 04IY's triangle and the square of 04J0”.

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

**`AlgebraicGeometry.RingedSite.Hom.relocalizedNaturalitySquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedNaturality.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/RelocalizedNaturality.lean#L151). The attribute's comment: “the final assertion: for `b : V' ⟶ V`, `a : U' ⟶ U` and `c'` with `a ≫ c = c' ≫ u(b)`, the induced square of ringed topoi on the slices commutes”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
