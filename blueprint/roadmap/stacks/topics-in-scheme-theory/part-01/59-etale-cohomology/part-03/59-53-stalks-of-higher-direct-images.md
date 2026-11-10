---
declaration: section
origin: cited
lean: AlgebraicGeometry.higherBaseChangeStalkHom_comp_higherDirectImageStalkIso_hom, AlgebraicGeometry.stalkHigherDirectImageIso, AlgebraicGeometry.stalkDerivedPushforwardHomologyIso, AlgebraicGeometry.stalkDerivedPushforwardIso, AlgebraicGeometry.higherDirectImageStalkIso, Stacks.StrictlyHenselian.higherDirectImageEtaleStalkIso, AlgebraicGeometry.strictHenselizationSectionsToFibreSectionsViaBaseChange, AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSectionsViaBaseChange
statement: formalized
proof: formalized
---

# 59.53 Stalks of higher direct images

Section 59.53 of the Stacks Project, [Tag 03Q7](https://stacks.math.columbia.edu/tag/03Q7). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03Q9, a theorem

[Tag 03Q9](https://stacks.math.columbia.edu/tag/03Q9) in the Stacks Project.

**`AlgebraicGeometry.higherBaseChangeStalkHom_comp_higherDirectImageStalkIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StrictHenselizationCriterionCommSq.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StrictHenselizationCriterionCommSq.lean#L571). The attribute's comment: “compatibility of the isomorphisms with the base change map of a commutative square”.

> **Stacks 03Q9, compatibility with base change along a commutative square.** Write
> `θ = AlgebraicGeometry.higherDirectImageStalkIso` for the isomorphisms
> `(R^q g_* F)_{f(x)} ≅ H^q(T ×_S Spec(𝒪^{sh}_{S,f(x)}), F)` and
> `(R^q h_* e⁻¹F)_x ≅ H^q(Y ×_X Spec(𝒪^{sh}_{X,x}), e⁻¹F)`. For a commutative square
> `h ≫ f = e ≫ g` with `g`, `h` quasi-compact and quasi-separated, `θ` at `x` after the stalk `b` at
> `x` of the base change map `f⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` is `θ` at `f(x)` followed by the pull
> back `ρ` along `κ = AlgebraicGeometry.strictHenselizationBaseChangeSquareMap`, the morphism
> `Y ×_X Spec(𝒪^{sh}_{X,x}) ⟶ T ×_S Spec(𝒪^{sh}_{S,f(x)})` given by `e` and by the morphism `m`
> of strict henselizations: `θ ∘ b = ρ ∘ θ`.

```lean
theorem higherBaseChangeStalkHom_comp_higherDirectImageStalkIso_hom (q : ℕ)
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1}) :
    ((higherBaseChangeStalkHom f g h e w x.hom).app q).app F ≫
        (higherDirectImageStalkIso B₁ hX h x q ((smallEtalePullbackAb e).obj F)).hom =
      (higherDirectImageStalkIso B₂ hS g (x.map f) q F).hom ≫
        AddCommGrpCat.ofHom (etaleCohomologyPullback
          (strictHenselizationBaseChangeSquareMap B₁ B₂ hX hS w x m hm)
          ((strictHenselizationBaseChangeSquarePullbackHom B₁ B₂ hX hS w x m hm).app F) q)
```

**`AlgebraicGeometry.stalkHigherDirectImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkHigherDirectImageStrictHenselization.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkHigherDirectImageStrictHenselization.lean#L282). The attribute's comment: “first assertion, for an abelian sheaf `F` on `X_étale`: `(R^n f_* F)_s = H^n_ét(X ×_S Spec(𝒪^{sh}_{S,s}), p^{-1}F)`, with `R^n` Mathlib's right derived functors of direct image and of global sections on the small étale sites; the strict henselization is taken inside a big étale site `B` containing `S`”. References: SGA 4 IX (4.1.1), “more general”.

> For `f : X ⟶ S` quasi-compact and quasi-separated, `s` a geometric point of `S` and
> `p : X ×_S Spec(𝒪^{sh}_{S,s}) ⟶ X` the projection,
> `(R^n f_* F)_s ≅ H^n_ét(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹F)` for every abelian sheaf `F` on `X_étale`
> and every `n`.

```lean
def stalkHigherDirectImageIso (F : Sheaf (smallEtaleTopology X) Ab.{u + 1}) (n : ℕ) :
    (smallEtaleStalkAb s.hom).obj (((smallEtalePushforwardAb f).rightDerived n).obj F) ≅
      ((Sheaf.Γ (smallEtaleTopology (strictHenselizationBaseChange B hS f s))
          Ab.{u + 1}).rightDerived n).obj
        ((smallEtalePullbackAb (strictHenselizationBaseChangeToSource B hS f s)).obj F)
```

**`AlgebraicGeometry.stalkDerivedPushforwardHomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkHigherDirectImageStrictHenselization.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkHigherDirectImageStrictHenselization.lean#L295). The attribute's comment: “second assertion, for `K` in `D^+(X_étale)` and `n` in `ℤ`: `(R^n f_* K)_s = H^n_ét(X ×_S Spec(𝒪^{sh}_{S,s}), p^{-1}K)`, the cohomology objects of the right derived functors on the bounded below derived categories”.

> For `f : X ⟶ S` quasi-compact and quasi-separated, `K` in `D⁺(X_étale)` and `n : ℤ`,
> `(R^n f_* K)_s ≅ H^n(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹K)`.

```lean
def stalkDerivedPushforwardHomologyIso
    (K : DerivedCategory.Plus (Sheaf (smallEtaleTopology X) Ab.{u + 1})) (n : ℤ) :
    (smallEtaleStalkAb s.hom).obj ((DerivedCategory.Plus.homologyFunctor _ n).obj
        ((smallEtalePushforwardAb f).rightDerivedFunctorPlus.obj K)) ≅
      (DerivedCategory.Plus.homologyFunctor Ab.{u + 1} n).obj
        ((Sheaf.Γ (smallEtaleTopology (strictHenselizationBaseChange B hS f s))
          Ab.{u + 1}).rightDerivedFunctorPlus.obj
          ((smallEtalePullbackAb
            (strictHenselizationBaseChangeToSource B hS f s)).mapDerivedCategoryPlus.obj K))
```

**`AlgebraicGeometry.stalkDerivedPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkHigherDirectImageStrictHenselization.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkHigherDirectImageStrictHenselization.lean#L312). The attribute's comment: “third assertion: `(Rf_* K)_s = RΓ_ét(X ×_S Spec(𝒪^{sh}_{S,s}), p^{-1}K)` in `D^+(Ab)`, as an isomorphism of functors on `D^+(X_étale)`, the stalk and `p^{-1}` acting degreewise”.

> For `f : X ⟶ S` quasi-compact and quasi-separated,
> `(Rf_* K)_s ≅ RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹K)` in `D⁺(Ab)`, naturally in `K ∈ D⁺(X_étale)`.

```lean
def stalkDerivedPushforwardIso :
    (smallEtalePullbackAb
        (strictHenselizationBaseChangeToSource B hS f s)).mapDerivedCategoryPlus ⋙
        (Sheaf.Γ (smallEtaleTopology (strictHenselizationBaseChange B hS f s))
          Ab.{u + 1}).rightDerivedFunctorPlus ≅
      (smallEtalePushforwardAb f).rightDerivedFunctorPlus ⋙
        (smallEtaleStalkAb s.hom).mapDerivedCategoryPlus
```

**`AlgebraicGeometry.higherDirectImageStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkOfHigherDirectImage.lean, line 809](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkOfHigherDirectImage.lean#L809). The attribute's comment: “the first assertion: abelian sheaves”. References: SGA 4 IX (4.1.1), “more general”.

> **Stacks 03Q9: the stalks of the higher direct images.** Let `g : T ⟶ S` be a
> quasi-compact and quasi-separated morphism of schemes, `F` an abelian sheaf on `T_étale` and `s`
> a geometric point of `S`. Then `(R^n g_* F)_s = H^n_étale(T ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹F)`,
> where `p : T ×_S Spec(𝒪^{sh}_{S,s}) ⟶ T` is the projection. The isomorphism is natural in `F`,
> compatible with the connecting morphisms (it is the component of
> `AlgebraicGeometry.higherDirectImageStalkComparison`), and in degree zero it is the canonical map
> `AlgebraicGeometry.pushforwardStalkToStrictHenselizationSectionsAb`.

```lean
def higherDirectImageStalkIso (n : ℕ) (F : Sheaf (smallEtaleTopology T) Ab.{u + 1}) :
    (smallEtaleStalkAb s.hom).obj (((smallEtalePushforwardAb g).rightDerived n).obj F) ≅
      AddCommGrpCat.of (Sheaf.H.{u + 1}
        ((smallEtalePullbackAb (strictHenselizationBaseChangeToSource B hS g s)).obj F) n)
```

**`Stacks.StrictlyHenselian.higherDirectImageEtaleStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianDirectImageStalk.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictlyHenselianDirectImageStalk.lean#L105). The attribute's comment: “conditional on the base being `Spec R` for a strictly henselian local ring `R` and the geometric point lying over its closed point, so that the strict henselization is `R` and the base change of the source is `X` itself”.

> **Stacks 03Q9 over a strictly henselian base.** The stalk at `s` of the `n`-th higher direct
> image of `F` along `f : X ⟶ Spec R` is the `n`-th étale cohomology group of `X` with
> coefficients in `F`.

```lean
public def higherDirectImageEtaleStalkIso
    (hs : s.LiesOver (IsLocalRing.closedPoint R)) (n : ℕ)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}) :
    etaleStalk B (Spec (.of R)) hS s ((higherDirectImage B R hS f n).obj F).obj ≅
      ((smallEtaleGlobalSections B X).rightDerived n).obj F
```

## Tag 0GIX, a remark

[Tag 0GIX](https://stacks.math.columbia.edu/tag/0GIX) in the Stacks Project.

**`AlgebraicGeometry.strictHenselizationSectionsToFibreSectionsViaBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedStalkFibreBaseChangeMaps.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedStalkFibreBaseChangeMaps.lean#L448). The attribute's comment: “the second map: global sections of the base change map for the left square”.

> **Stacks 0GIX, the second map.** The canonical map
> `RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹K) ⟶ RΓ(X_s, K|_{X_s})`, natural in `K ∈ D(X_étale)`, defined as
> the source defines it: from the derived base change map `i⁻¹Rf'_*(p⁻¹K) ⟶ Rf_{s,*}(K|_{X_s})` of
> the left square
>
> ```
> X_s ----> X ×_S Spec(𝒪^{sh}_{S,s})
> |f_s             |f'
> v                v
> s  ---i--> Spec(𝒪^{sh}_{S,s})
> ```
>
> by taking global sections: it is the identification
> `RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), -) ≅ RΓ(Spec(𝒪^{sh}_{S,s}), Rf'_* -)`, restriction of derived
> global sections along `i` (an isomorphism over the strictly henselian base), derived global
> sections on `s` of the base change map, the identification `RΓ(s, Rf_{s,*} -) ≅ RΓ(X_s, -)`, and
> the identification of the restriction of `p⁻¹K` to `X_s` with `K|_{X_s}`.
>
> Every derived functor here is the total right derived functor on the whole unbounded homotopy
> category; their existence is not assumed but supplied by the instances
> `Stacks.EtaleCohomology.smallEtaleGlobalSectionsAb_hasRightDerivedFunctor` and
> `Stacks.EtaleCohomology.hasRightDerivedFunctor_smallEtalePushforwardAb` (abelian sheaves on a
> small étale site have K-injective resolutions).

```lean
def strictHenselizationSectionsToFibreSectionsViaBaseChange :
    smallEtaleDerivedPullbackAb (strictHenselizationBaseChangeToSource B hS f s) ⋙
        smallEtaleDerivedGlobalSections (strictHenselizationBaseChange B hS f s) ⟶
      smallEtaleDerivedPullbackAb (geometricFibreToSource f s) ⋙
        smallEtaleDerivedGlobalSections (geometricFibre f s)
```

**`AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSectionsViaBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedStalkFibreBaseChangeMaps.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedStalkFibreBaseChangeMaps.lean#L709). The attribute's comment: “the first map: global sections of the base change map for the right square”.

> **Stacks 0GIX, the first map.** The canonical map
> `(Rf_*K)_s ⟶ RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹K)`, natural in `K ∈ D(X_étale)`, defined as the
> source defines it: from the derived base change map `j⁻¹Rf_*K ⟶ Rf'_*(p⁻¹K)` of the right square
>
> ```
> X ×_S Spec(𝒪^{sh}_{S,s}) --p--> X
> |f'                           |f
> v                             v
> Spec(𝒪^{sh}_{S,s}) ---j---> S
> ```
>
> by taking global sections over the strict henselization: it is the comparison
> `(Rf_*K)_s ⟶ RΓ(Spec(𝒪^{sh}_{S,s}), j⁻¹Rf_*K)` of the stalk with derived sections over the
> strict henselization (`AlgebraicGeometry.vanishingCyclesMap`, an isomorphism by
> `AlgebraicGeometry.isIso_vanishingCyclesMap_id`), derived global sections over the strict
> henselization of the base change map, and the identification
> `RΓ(Spec(𝒪^{sh}_{S,s}), Rf'_* -) ≅ RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), -)`. The structure morphism `j` is
> written `𝟙 ≫ j`, the form in which the comparison of the stalk with sections presents it.
>
> Every derived functor here is the total right derived functor on the whole unbounded homotopy
> category; their existence is not assumed but supplied by the instances
> `Stacks.EtaleCohomology.smallEtaleGlobalSectionsAb_hasRightDerivedFunctor` and
> `Stacks.EtaleCohomology.hasRightDerivedFunctor_smallEtalePushforwardAb` (abelian sheaves on a
> small étale site have K-injective resolutions).

```lean
def derivedPushforwardStalkToStrictHenselizationSectionsViaBaseChange :
    smallEtaleDerivedPushforwardAb f ⋙ smallEtaleDerivedStalkAb s.hom ⟶
      smallEtaleDerivedPullbackAb (strictHenselizationBaseChangeToSource B hS f s) ⋙
        smallEtaleDerivedGlobalSections (strictHenselizationBaseChange B hS f s)
```

**`AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSectionsViaBaseChange_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedStalkFibreBaseChangeMaps.lean, line 771](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedStalkFibreBaseChangeMaps.lean#L771). The attribute's comment: “the composition is the base change map”.

> **Stacks 0GIX, the composition clause.** For a morphism of schemes `f : X ⟶ S` and a
> geometric point `s` of `S`, the composite of the two canonical maps
>
> `(Rf_*K)_s ⟶ RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹K) ⟶ RΓ(X_s, K|_{X_s})`
>
> obtained by taking global sections of the base change maps of the right and of the left square
> (`AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSectionsViaBaseChange` and
> `AlgebraicGeometry.strictHenselizationSectionsToFibreSectionsViaBaseChange`) is the usual base
> change map `(Rf_*K)_s ⟶ RΓ(X_s, K|_{X_s})`: the identification of the stalk at `s` with global
> sections on `s` of the inverse image, followed by global sections on `s` of the derived base change
> map `s⁻¹Rf_*K ⟶ Rq_*(K|_{X_s})` of Stacks 0A2A for the cartesian square defining the geometric
> fibre (`q : X_s ⟶ s` its structure morphism), and by the identification
> `RΓ(s, Rq_* -) ≅ RΓ(X_s, -)` of Stacks 0D6H. This holds as an equality of natural transformations
> on the whole unbounded derived category `D(X_étale)`; nothing is assumed of `f` or of `s`, and the
> existence of the unbounded derived functors involved is supplied by instances, not assumed.
>
> The two maps agree with the ones this library constructs directly
> (`AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSections_eq_baseChange` and
> `AlgebraicGeometry.strictHenselizationSectionsToFibreSections_eq_baseChange`), whose composite is
> computed by
> `AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSections_comp_fibreSections`.

```lean
theorem derivedPushforwardStalkToStrictHenselizationSectionsViaBaseChange_comp :
    derivedPushforwardStalkToStrictHenselizationSectionsViaBaseChange B hS f s ≫
        strictHenselizationSectionsToFibreSectionsViaBaseChange B hS f s =
      Functor.whiskerLeft (smallEtaleDerivedPushforwardAb f)
          (derivedGeometricStalkToPullbackSections s.hom) ≫
        (Functor.associator _ _ _).inv ≫
        Functor.whiskerRight (geometricFibreDerivedBaseChangeAb f s)
          (smallEtaleDerivedGlobalSections s.source) ≫
        (Functor.associator _ _ _).hom ≫
        Functor.whiskerLeft (smallEtaleDerivedPullbackAb (geometricFibreToSource f s))
          (smallEtaleDerivedGlobalSectionsPushforwardIsoAb (geometricFibreToPoint f s)).hom
```

**`AlgebraicGeometry.strictHenselizationSectionsToFibreSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkOfDerivedPushforward.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkOfDerivedPushforward.lean#L445). The attribute's comment: “the map to the fibre”.

> **Stacks 0GIX, the map to the fibre.** The canonical map
>
> `RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹K) ⟶ RΓ(X_s, K|_{X_s})`
>
> for an object `K` of the unbounded derived category of abelian sheaves on the small étale site of
> `X`, natural in `K`, where `p : X ×_S Spec(𝒪^{sh}_{S,s}) ⟶ X` is the projection.
>
> It is the derived restriction map along the canonical morphism
> `X_s ⟶ X ×_S Spec(𝒪^{sh}_{S,s})` over `X`, after identifying the inverse image along that
> morphism of `p⁻¹K` with the restriction of `K` to the geometric fibre.

```lean
def strictHenselizationSectionsToFibreSections :
    smallEtaleDerivedPullbackAb (strictHenselizationBaseChangeToSource B hS f s) ⋙
        smallEtaleDerivedGlobalSections (strictHenselizationBaseChange B hS f s) ⟶
      smallEtaleDerivedPullbackAb (geometricFibreToSource f s) ⋙
        smallEtaleDerivedGlobalSections (geometricFibre f s)
```

**`AlgebraicGeometry.derivedPushforwardStalkToStrictHenselizationSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkOfDerivedPushforward.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkOfDerivedPushforward.lean#L551). The attribute's comment: “the map from the stalk”.

> **Stacks 0GIX, the map from the stalk.** The canonical map
>
> `(Rf_*K)_s ⟶ RΓ(X ×_S Spec(𝒪^{sh}_{S,s}), p⁻¹K)`
>
> for an object `K` of the unbounded derived category of abelian sheaves on the small étale site of
> `X`, natural in `K`, where `p : X ×_S Spec(𝒪^{sh}_{S,s}) ⟶ X` is the projection.
>
> The stalk of the derived direct image is a right derived functor of the stalk of the direct
> image, the stalk functor having a right adjoint, so the map on sheaves
> `AlgebraicGeometry.pushforwardStalkToStrictHenselizationSectionsAb` extends uniquely to a map of
> unbounded derived categories factoring it through the units.

```lean
def derivedPushforwardStalkToStrictHenselizationSections :
    smallEtaleDerivedPushforwardAb f ⋙ smallEtaleDerivedStalkAb s.hom ⟶
      smallEtaleDerivedPullbackAb (strictHenselizationBaseChangeToSource B hS f s) ⋙
        smallEtaleDerivedGlobalSections (strictHenselizationBaseChange B hS f s)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.53, Tag 03Q7](https://stacks.math.columbia.edu/tag/03Q7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
