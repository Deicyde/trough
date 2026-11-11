---
declaration: section
origin: cited
lean: AlgebraicGeometry.vanishingCyclesMap, AlgebraicGeometry.vanishingCyclesMap_fac_app, AlgebraicGeometry.vanishingCyclesFibreMap, AlgebraicGeometry.smallEtaleDerivedStalkToSections, AlgebraicGeometry.smallEtaleDerivedStalkToSections_fac_app, AlgebraicGeometry.stalkToVanishingCyclesFibreSections, AlgebraicGeometry.smallEtaleDerivedStalkIsoStrictHenselizationSections, AlgebraicGeometry.stalkToVanishingCyclesFibreSections_eq_restriction
statement: formalized
proof: formalized
---

# 59.93 Local acyclicity

Section 59.93 of the Stacks Project, [Tag 0GJM](https://stacks.math.columbia.edu/tag/0GJM). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GJN, an equation

[Tag 0GJN](https://stacks.math.columbia.edu/tag/0GJN) in the Stacks Project.

**`AlgebraicGeometry.vanishingCyclesMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SpecializationMap.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SpecializationMap.lean#L461). The attribute's comment: “for an arbitrary scheme over the strict henselization”.

> **Stacks 0GJN.** The canonical map `α_{K,x,t} : K_x ⟶ RΓ(T, K)` from the stalk at a geometric
> point `x` of `X` of an object `K` of the unbounded derived category of abelian sheaves on the
> small étale site of `X`, to the unbounded derived global sections of `K` on a scheme `T` over the
> strict henselization `Spec 𝒪^{sh}_{X,x}`, natural in `K`.
>
> For a morphism of schemes `f : X ⟶ S` and a geometric point `t` of `Spec 𝒪^{sh}_{S,f(x)}` the
> variety of vanishing cycles of `f` at `x` is the fibre product
> `F_{x,t} = t ×_{Spec 𝒪^{sh}_{S,f(x)}} Spec 𝒪^{sh}_{X,x}` over `Spec 𝒪^{sh}_{X,x}`, and the
> displayed map of the source is this one for that `T` and the second projection; the construction
> uses nothing about `T` beyond its morphism to the strict henselization.
>
> Since the strict henselization is the initial étale neighbourhood of `x`, pulling back germs
> along `T ⟶ Spec 𝒪^{sh}_{X,x}` gives the map `etaleStalkToSectionsAb` on abelian sheaves. The
> stalk functor is exact, so its action on unbounded derived categories is a right derived functor
> of itself, and the map on sheaves extends uniquely to one of derived categories.

```lean
def vanishingCyclesMap :
    smallEtaleDerivedStalkAb x.hom ⟶
      smallEtaleDerivedPullbackAb
          (q ≫ strictHenselizationToBase B X hX x) ⋙
        smallEtaleDerivedGlobalSections T
```

**`AlgebraicGeometry.vanishingCyclesMap_fac_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SpecializationMap.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SpecializationMap.lean#L481). The attribute's comment: “the derived map factors the map on abelian sheaves”.

> **Stacks 0GJN.** On every complex of abelian sheaves on the small étale site of `X`, the
> canonical map to the derived global sections over `T` factors the degreewise map on sheaves
> through the unit of the derivation of global sections, read through the identifications of the
> degreewise actions of the stalk and of inverse image with their actions on derived categories.
>
> Since the degreewise action of the stalk functor is a right derived functor of itself, this
> property determines the map.

```lean
theorem vanishingCyclesMap_fac_app
    (J : HomotopyCategory (Sheaf (smallEtaleTopology X) Ab.{u + 1}) (.up ℤ)) :
    (smallEtaleStalkAb x.hom).mapDerivedCategoryFactorsh.inv.app J ≫
        (vanishingCyclesMap B X hX x q).app (DerivedCategory.Qh.obj J) =
      DerivedCategory.Qh.map ((Stacks.DerivedFunctor.mapHomotopyCategoryOfComp
          (smallEtaleStalkAb x.hom)
          (smallEtalePullbackAb
            (q ≫ strictHenselizationToBase B X hX x))
          (Sheaf.Γ (smallEtaleTopology T) Ab.{u + 1})
          (etaleStalkToSectionsAb B X hX x q)).app J) ≫
        (smallEtaleDerivedGlobalSectionsUnit T).app
            (((smallEtalePullbackAb
              (q ≫ strictHenselizationToBase B X hX x)).mapHomotopyCategory (.up ℤ)).obj J) ≫
          (smallEtaleDerivedGlobalSections T).map
            ((smallEtalePullbackAb
              (q ≫ strictHenselizationToBase B X hX x)).mapDerivedCategoryFactorsh.inv.app J)
```

**`AlgebraicGeometry.vanishingCyclesFibreMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SpecializationMap.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/SpecializationMap.lean#L537).

> **Stacks 0GJN.** The canonical map
>
> `α_{K,x,t} : K_x ⟶ RΓ(F_{x,t}, K)`
>
> from the stalk at a geometric point `x` of `X` of an object `K` of the unbounded derived category
> of abelian sheaves on the small étale site of `X`, to the unbounded derived sections of `K` on the
> variety of vanishing cycles `F_{x,t}` of a morphism `f : X ⟶ S` at `x` and a geometric point `t`
> of `Spec 𝒪^{sh}_{S,f(x)}`, natural in `K`.
>
> The stalk of `K` at `x` is the derived sections of `K` over the strictly henselian
> `Spec 𝒪^{sh}_{X,x}`, and the map is pullback of cohomology along the projection
> `F_{x,t} ⟶ Spec 𝒪^{sh}_{X,x}`.

```lean
def vanishingCyclesFibreMap :
    smallEtaleDerivedStalkAb x.hom ⟶
      smallEtaleDerivedPullbackAb (vanishingCyclesFibreToSource B hX hS f x t) ⋙
        smallEtaleDerivedGlobalSections (vanishingCyclesFibre B hX hS f x t)
```

**`AlgebraicGeometry.smallEtaleDerivedStalkToSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean#L98). The attribute's comment: “for an arbitrary scheme over the strict henselization”.

> **Stacks 0GJN.** The canonical map `α_{K,x} : K_x ⟶ RΓ(T, K)` from the stalk at a geometric
> point `x` of `X` of an object `K` of the unbounded derived category `D(X_étale)` of abelian
> sheaves on the small étale site of `X`, to the unbounded derived global sections
> `RΓ(T, K) = RΓ(T_étale, g⁻¹K)` of `K` on a scheme `T` over the strict henselization
> `Spec 𝒪^{sh}_{X,x}`, with `g : T ⟶ Spec 𝒪^{sh}_{X,x} ⟶ X` the structure morphism, natural in `K`.
>
> The derived global sections on `T` are the total right derived functor of global sections on the
> whole unbounded homotopy category, which exists by
> `Stacks.EtaleCohomology.smallEtaleGlobalSectionsAb_hasRightDerivedFunctor`. Since the strict
> henselization is the initial étale neighbourhood of `x`, pulling back germs along
> `T ⟶ Spec 𝒪^{sh}_{X,x}` gives the map `etaleStalkToSectionsAb` on abelian sheaves; the stalk
> functor is exact, so the map on sheaves extends uniquely to one of derived categories.
> `AlgebraicGeometry.smallEtaleDerivedStalkToSections_eq_restriction` identifies it with the
> identification `K_x = RΓ(Spec 𝒪^{sh}_{X,x}, K)` followed by pulling back cohomology along
> `T ⟶ Spec 𝒪^{sh}_{X,x}`.

```lean
def smallEtaleDerivedStalkToSections :
    smallEtaleDerivedStalkAb x.hom ⟶
      smallEtaleDerivedPullbackAb (q ≫ strictHenselizationToBase B X hX x) ⋙
        smallEtaleDerivedGlobalSections T
```

**`AlgebraicGeometry.smallEtaleDerivedStalkToSections_fac_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean#L112). The attribute's comment: “the derived map factors the map on abelian sheaves”.

> **Stacks 0GJN.** On every complex of abelian sheaves on the small étale site of `X`, the
> canonical map to the derived global sections over `T` factors the degreewise map on sheaves
> through the unit of the derivation of global sections, read through the identifications of the
> degreewise actions of the stalk and of inverse image with their actions on derived categories.
>
> Since the degreewise action of the stalk functor is a right derived functor of itself, this
> property determines the map.

```lean
theorem smallEtaleDerivedStalkToSections_fac_app
    (J : HomotopyCategory (Sheaf (smallEtaleTopology X) Ab.{u + 1}) (.up ℤ)) :
    (smallEtaleStalkAb x.hom).mapDerivedCategoryFactorsh.inv.app J ≫
        (smallEtaleDerivedStalkToSections B X hX x q).app (DerivedCategory.Qh.obj J) =
      DerivedCategory.Qh.map ((Stacks.DerivedFunctor.mapHomotopyCategoryOfComp
          (smallEtaleStalkAb x.hom)
          (smallEtalePullbackAb
            (q ≫ strictHenselizationToBase B X hX x))
          (Sheaf.Γ (smallEtaleTopology T) Ab.{u + 1})
          (etaleStalkToSectionsAb B X hX x q)).app J) ≫
        (smallEtaleDerivedGlobalSectionsUnit T).app
            (((smallEtalePullbackAb
              (q ≫ strictHenselizationToBase B X hX x)).mapHomotopyCategory (.up ℤ)).obj J) ≫
          (smallEtaleDerivedGlobalSections T).map
            ((smallEtalePullbackAb
              (q ≫ strictHenselizationToBase B X hX x)).mapDerivedCategoryFactorsh.inv.app J)
```

**`AlgebraicGeometry.stalkToVanishingCyclesFibreSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean#L156).

> **Stacks 0GJN.** The canonical map
>
> `α_{K,x,t} : K_x ⟶ RΓ(F_{x,t}, K)`
>
> from the stalk at a geometric point `x` of `X` of an object `K` of the unbounded derived category
> `D(X_étale)` of abelian sheaves on the small étale site of `X`, to the unbounded derived sections
> `RΓ(F_{x,t}, K) = RΓ((F_{x,t})_étale, g⁻¹K)` of `K` on the variety of vanishing cycles
> `F_{x,t} = t ×_{Spec 𝒪^{sh}_{S,f(x)}} Spec 𝒪^{sh}_{X,x}` of a morphism `f : X ⟶ S` at `x` and a
> geometric point `t` of `Spec 𝒪^{sh}_{S,f(x)}`, with `g : F_{x,t} ⟶ X` the canonical morphism,
> natural in `K`.
>
> The derived global sections on `F_{x,t}` exist by
> `Stacks.EtaleCohomology.smallEtaleGlobalSectionsAb_hasRightDerivedFunctor`. The stalk of `K` at
> `x` is the derived sections of `K` over the strictly henselian `Spec 𝒪^{sh}_{X,x}`
> (`AlgebraicGeometry.smallEtaleDerivedStalkIsoStrictHenselizationSections`), and the map is
> pullback of cohomology along the projection `F_{x,t} ⟶ Spec 𝒪^{sh}_{X,x}`
> (`AlgebraicGeometry.stalkToVanishingCyclesFibreSections_eq_restriction`).

```lean
def stalkToVanishingCyclesFibreSections :
    smallEtaleDerivedStalkAb x.hom ⟶
      smallEtaleDerivedPullbackAb (vanishingCyclesFibreToSource B hX hS f x t) ⋙
        smallEtaleDerivedGlobalSections (vanishingCyclesFibre B hX hS f x t)
```

**`AlgebraicGeometry.smallEtaleDerivedStalkIsoStrictHenselizationSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean#L183). The attribute's comment: “`K_x = RΓ(Spec 𝒪^{sh}_{X,x}, K)`, since `𝒪^{sh}_{X,x}` is strictly henselian”.

> **The stalk is the derived sections over the strict henselization.** For every object `K` of
> the unbounded derived category of abelian sheaves on the small étale site of `X`, the canonical
> map `K_x ⟶ RΓ(Spec 𝒪^{sh}_{X,x}, p⁻¹K)` is an isomorphism, natural in `K`: on sheaves it is
> `F_x = Γ(Spec 𝒪^{sh}_{X,x}, p⁻¹F)`, and global sections over the strictly henselian
> `Spec 𝒪^{sh}_{X,x}` are exact, so no boundedness of `K` is needed.

```lean
def smallEtaleDerivedStalkIsoStrictHenselizationSections :
    smallEtaleDerivedStalkAb x.hom ≅
      smallEtaleDerivedPullbackAb (strictHenselizationToBase B X hX x) ⋙
        smallEtaleDerivedGlobalSections (strictHenselization B X hX x)
```

**`AlgebraicGeometry.stalkToVanishingCyclesFibreSections_eq_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StalkToSectionsRestriction.lean#L284). The attribute's comment: “the map is obtained by pulling back cohomology along `F_{x,t} ⟶ Spec 𝒪^{sh}_{X,x}`, using `K_x = RΓ(Spec 𝒪^{sh}_{X,x}, K)`”.

> **Stacks 0GJN: the map `α_{K,x,t}` is pullback of cohomology along
> `F_{x,t} ⟶ Spec 𝒪^{sh}_{X,x}`.** The canonical map `α_{K,x,t} : K_x ⟶ RΓ(F_{x,t}, K)` at the
> variety of vanishing cycles `F_{x,t} = t ×_{Spec 𝒪^{sh}_{S,f(x)}} Spec 𝒪^{sh}_{X,x}` is the
> identification `K_x = RΓ(Spec 𝒪^{sh}_{X,x}, K)` followed by restriction of unbounded derived
> global sections along the second projection `F_{x,t} ⟶ Spec 𝒪^{sh}_{X,x}`, read through the
> composition isomorphism of inverse images.

```lean
theorem stalkToVanishingCyclesFibreSections_eq_restriction :
    stalkToVanishingCyclesFibreSections B hX hS f x t =
      (smallEtaleDerivedStalkIsoStrictHenselizationSections B X hX x).hom ≫
        Functor.whiskerLeft (smallEtaleDerivedPullbackAb (strictHenselizationToBase B X hX x))
          (smallEtaleDerivedGlobalSectionsRestriction
            (vanishingCyclesFibreToStrictHenselization B hX hS f x t)) ≫
        (Functor.associator _ _ _).inv ≫
          Functor.whiskerRight
            (Functor.mapDerivedCategoryCompIsoOfCompIso
              (smallEtalePullbackAbCompIso (vanishingCyclesFibreToStrictHenselization B hX hS f x t)
                (strictHenselizationToBase B X hX x))).hom
            (smallEtaleDerivedGlobalSections (vanishingCyclesFibre B hX hS f x t))
```

## Tag 0GJP, a definition

[Tag 0GJP](https://stacks.math.columbia.edu/tag/0GJP) in the Stacks Project.

**`AlgebraicGeometry.localAcyclicity_iff_isIso_vanishingCyclesFibreMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/Basic.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/Basic.lean#L221).

> Let `f : X ⟶ S` be a morphism of schemes and let `K` be an object of `D(X_étale)`. The five
> notions of the definition are, in terms of the canonical maps `α_{K,x,t} : K_x ⟶ RΓ(F_{x,t}, K)`
> of [Stacks, Tag 0GJN]:
>
> 1. `f` is *locally acyclic at a geometric point `x` of `X` relative to `K`* when `α_{K,x,t}` is
>    an isomorphism for every geometric point `t` of `Spec 𝒪^{sh}_{S,f(x)}`;
> 2. `f` is *locally acyclic relative to `K`* when that holds at every geometric point `x` of `X`;
> 3. `f` is *universally locally acyclic relative to `K`* when for every morphism `g : S' ⟶ S` of
>    schemes the base change `X ×_S S' ⟶ S'` is locally acyclic relative to the inverse image of
>    `K`;
> 4. `f` is *locally acyclic* when for every geometric point `x` of `X` and every positive integer
>    `n` prime to the characteristic of `κ(x)` it is locally acyclic at `x` relative to the
>    constant sheaf `ℤ/nℤ`;
> 5. `f` is *universally locally acyclic* when every base change of `f` is locally acyclic.
>
> The geometric points `t` are not assumed to be algebraic geometric points of
> `Spec 𝒪^{sh}_{S,f(x)}`: `GeometricPoint` asks only for a morphism from the spectrum of an
> algebraically closed field.
>
> The varieties of vanishing cycles are formed inside a big étale site, so clauses (1), (2) and
> (4) carry one; clauses (3) and (5) quantify over all morphisms `g : S' ⟶ S` and over all big
> étale sites containing `X ×_S S'` and `S'`, of which there is always at least one
> (`AlgebraicGeometry.exists_bigEtaleSite_contains_pullback`).

```lean
public theorem localAcyclicity_iff_isIso_vanishingCyclesFibreMap (B : BigEtaleSite.{u})
    {X S : Scheme.{u}} (hX : B.Contains X) (hS : B.Contains S) (f : X ⟶ S)
    (K : smallEtaleDerivedCategory X) :
    (∀ x : GeometricPoint X, IsLocallyAcyclicAt B hX hS f K x ↔
        ∀ t : GeometricPoint (strictHenselization B S hS (x.map f)),
          IsIso ((vanishingCyclesFibreMap B hX hS f x t).app K)) ∧
      (IsLocallyAcyclicRelative B hX hS f K ↔
        ∀ (x : GeometricPoint X)
          (t : GeometricPoint (strictHenselization B S hS (x.map f))),
          IsIso ((vanishingCyclesFibreMap B hX hS f x t).app K)) ∧
      (IsUniversallyLocallyAcyclicRelative f K ↔
        ∀ (S' : Scheme.{u}) (g : S' ⟶ S) (B' : BigEtaleSite.{u})
          (hX' : B'.Contains (pullback f g)) (hS' : B'.Contains S')
          (x' : GeometricPoint (pullback f g))
          (t' : GeometricPoint
            (strictHenselization B' S' hS' (x'.map (pullback.snd f g)))),
          IsIso ((vanishingCyclesFibreMap B' hX' hS'
              (pullback.snd f g) x' t').app
            ((smallEtaleDerivedPullbackAb (pullback.fst f g)).obj K))) ∧
      (IsLocallyAcyclic B hX hS f ↔
        ∀ (x : GeometricPoint X) (n : ℕ), 0 < n →
          (ringChar x.residueField = 0 ∨ n.Coprime (ringChar x.residueField)) →
            ∀ t : GeometricPoint (strictHenselization B S hS (x.map f)),
              IsIso ((vanishingCyclesFibreMap B hX hS f x t).app
                (smallEtaleConstantZModComplex X n))) ∧
      (IsUniversallyLocallyAcyclic f ↔
        ∀ (S' : Scheme.{u}) (g : S' ⟶ S) (B' : BigEtaleSite.{u})
          (hX' : B'.Contains (pullback f g)) (hS' : B'.Contains S')
          (x' : GeometricPoint (pullback f g)) (n : ℕ), 0 < n →
          (ringChar x'.residueField = 0 ∨ n.Coprime (ringChar x'.residueField)) →
            ∀ t' : GeometricPoint
              (strictHenselization B' S' hS' (x'.map (pullback.snd f g))),
              IsIso ((vanishingCyclesFibreMap B' hX' hS'
                  (pullback.snd f g) x' t').app
                (smallEtaleConstantZModComplex (pullback f g) n)))
```

## Tag 0GJQ, a proposition

[Tag 0GJQ](https://stacks.math.columbia.edu/tag/0GJQ) in the Stacks Project.

**`Stacks.EtaleCohomology.SmoothBaseChange.isUniversallyLocallyAcyclic_of_smooth_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/LocalAcyclicity/SmoothMorphismsRegistered.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/LocalAcyclicity/SmoothMorphismsRegistered.lean#L38). References: SGA 4½ Arcata (5.2.1), “more general”; SGA 7 I (2.4), “partial”.

> **Smooth morphisms are universally locally acyclic** ([Stacks, Proposition 0GJQ]). Let
> `f : X ⟶ S` be a smooth morphism of schemes. Then `f` is universally locally acyclic: for every
> morphism `S' ⟶ S` and every big étale site containing `X ×_S S'` and `S'`, the base change
> `X ×_S S' ⟶ S'` of `f` is locally acyclic there.

```lean
theorem isUniversallyLocallyAcyclic_of_smooth_unconditional {X S : Scheme.{u}} (f : X ⟶ S)
    [Smooth f] : IsUniversallyLocallyAcyclic f
```

## Tag 0GJR, a lemma

[Tag 0GJR](https://stacks.math.columbia.edu/tag/0GJR) in the Stacks Project.

**`AlgebraicGeometry.isLocallyAcyclicRelative_of_isLocallyConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/LocallyConstantCoefficients.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/LocallyConstantCoefficients.lean#L382). The attribute's comment: “the dévissage from constant ℤ/nℤ coefficients to a locally constant prime-to-residue-characteristic torsion sheaf: the stalk is the filtered colimit of its finite subgroups and each of those is a finite direct sum of cyclic groups. The two strict-henselization inputs are hypotheses — `hdep`, that the canonical map depends only on the inverse image on Spec O^sh\_\{X,x}, and `hconst`, that a locally constant sheaf is constant there with value its stalk — as are `hcolim`, which is Tag 03Q5 for the affine variety of vanishing cycles, and `hadd`, additivity of RGamma”.

> **Stacks 0GJR.** Let `f : X ⟶ S` be a morphism of schemes and let `F` be a locally constant
> abelian sheaf on `X_étale` whose stalk at every geometric point `x` is torsion with every element
> order prime to the characteristic of the residue field at `x`. If `f` is locally acyclic, then
> `f` is locally acyclic relative to `F`.
>
> What is proved here is the dévissage: the reduction of the locally constant torsion coefficient
> sheaf `F` to the constant sheaves `ℤ/nℤ` that local acyclicity speaks about. The stalk is written
> as the filtered colimit of its finite subgroups, each of those splits as a finite direct sum of
> cyclic groups of prime-to-`p` order, and local acyclicity is applied to each summand.
>
> Four hypotheses are supplied rather than derived.
>
> * `hdep` and `hconst` are the two facts about the strict henselization that the source's proof
>   rests on, each stated in its own right. `hdep` is the consequence of
>   `K_x = RΓ(Spec 𝒪^{sh}_{X,x}, K)` that the canonical map only sees the inverse image of `K` on
>   `Spec 𝒪^{sh}_{X,x}`; `hconst` is that a locally constant sheaf has constant inverse image
>   there, with value its stalk.
> * `hcolim` is Tag 03Q5 for the affine variety of vanishing cycles, in the form the argument
>   consumes it: the iso-locus of the canonical map on constant coefficients is closed under
>   filtered colimits of the coefficient group.
> * `hadd` is additivity of unbounded derived global sections, which is formal but not an
>   available instance.
>
> See the module docstring for why `hcolim` cannot be stated as preservation of filtered
> colimits.

```lean
theorem isLocallyAcyclicRelative_of_isLocallyConstant
    (B : BigEtaleSite.{u}) {X S : Scheme.{u}} (hX : B.Contains X) (hS : B.Contains S)
    (f : X ⟶ S)
    (hadd : ∀ (x : GeometricPoint X)
        (t : GeometricPoint (strictHenselization B S hS (x.map f))),
      (smallEtaleDerivedGlobalSections (vanishingCyclesFibre B hX hS f x t)).Additive)
    (hcolim : ∀ (x : GeometricPoint X)
        (t : GeometricPoint (strictHenselization B S hS (x.map f))),
      ∀ {I : Type (u + 1)} [SmallCategory I] [IsFiltered I] (N : I ⥤ Ab.{u + 1})
        (c : Cocone N), IsColimit c →
        (∀ i, IsIso ((vanishingCyclesFibreMap B hX hS f x t).app
            (smallEtaleConstantComplexAb X (N.obj i)))) →
          IsIso ((vanishingCyclesFibreMap B hX hS f x t).app
            (smallEtaleConstantComplexAb X c.pt)))
    (hdep : ∀ (x : GeometricPoint X)
        (t : GeometricPoint (strictHenselization B S hS (x.map f)))
        (K K' : smallEtaleDerivedCategory X),
      ((smallEtaleDerivedPullbackAb (strictHenselizationToBase B X hX x)).obj K ≅
          (smallEtaleDerivedPullbackAb (strictHenselizationToBase B X hX x)).obj K') →
      (IsIso ((vanishingCyclesFibreMap B hX hS f x t).app K) ↔
        IsIso ((vanishingCyclesFibreMap B hX hS f x t).app K')))
    (hconst : ∀ (G : Sheaf X.smallEtaleTopology Ab.{u + 1}),
        Stacks.ConstantSheaf.IsLocallyConstant X.smallEtaleTopology G →
        ∀ x : GeometricPoint X,
      (smallEtaleDerivedPullbackAb (strictHenselizationToBase B X hX x)).obj
          ((DerivedCategory.singleFunctor (Sheaf X.smallEtaleTopology Ab.{u + 1}) 0).obj G) ≅
        (smallEtaleDerivedPullbackAb (strictHenselizationToBase B X hX x)).obj
          (smallEtaleConstantComplexAb X ((smallEtaleStalkAb x.hom).obj G)))
    (F : Sheaf X.smallEtaleTopology Ab.{u + 1})
    (hFlc : Stacks.ConstantSheaf.IsLocallyConstant X.smallEtaleTopology F)
    (hFtors : ∀ (x : GeometricPoint X) (a : (smallEtaleStalkAb x.hom).obj F),
      ∃ n : ℕ, 0 < n ∧
        (ringChar x.residueField = 0 ∨ Nat.Coprime n (ringChar x.residueField)) ∧ n • a = 0)
    (hf : IsLocallyAcyclic B hX hS f) :
    IsLocallyAcyclicRelative B hX hS f
      ((DerivedCategory.singleFunctor (Sheaf X.smallEtaleTopology Ab.{u + 1}) 0).obj F)
```

**`AlgebraicGeometry.isLocallyAcyclicRelative_of_isLocallyConstant_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/LocallyConstantCoefficientsUnconditional.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/LocallyConstantCoefficientsUnconditional.lean#L401).

> **Stacks 0GJR.** Let `f : X ⟶ S` be a morphism of schemes and let `F` be a locally constant
> abelian sheaf on `X_étale` whose stalk at every geometric point `x` is torsion with every element
> order prime to the characteristic of the residue field at `x`. If `f` is locally acyclic, then
> `f` is locally acyclic relative to `F`.
>
> What is proved here is the dévissage: the reduction of the locally constant torsion coefficient
> sheaf `F` to the constant sheaves `ℤ/nℤ` that local acyclicity speaks about. The stalk is written
> as the filtered colimit of its finite subgroups, each of those splits as a finite direct sum of
> cyclic groups of prime-to-`p` order, and local acyclicity is applied to each summand.
>
> No hypothesis is supplied rather than derived. The two facts about the strict henselization that
> the source's proof rests on are both proved: that the canonical map only sees the inverse image of
> `K` on `Spec 𝒪^{sh}_{X,x}` is
> `AlgebraicGeometry.isIso_vanishingCyclesFibreMap_app_iff_of_derivedPullbackIso`, and that a
> locally constant sheaf has constant inverse image there, with value its stalk, is
> `AlgebraicGeometry.strictHenselizationDerivedPullbackConstantComplexIso`. Nor is the filtered
> colimit step a hypothesis: it is
> `AlgebraicGeometry.isIso_vanishingCyclesFibreMap_app_constantComplex_of_isColimit`, Tag 03Q5 for
> the variety of vanishing cycles, and neither is additivity of `RΓ` there, which is
> `Stacks.EtaleCohomology.smallEtaleDerivedGlobalSections_additive`.
>
> `AlgebraicGeometry.isLocallyAcyclicRelative_of_isLocallyConstant` is the same statement with
> those four facts taken as hypotheses.

```lean
theorem isLocallyAcyclicRelative_of_isLocallyConstant_unconditional
    (B : BigEtaleSite.{u}) {X S : Scheme.{u}} (hX : B.Contains X) (hS : B.Contains S)
    (f : X ⟶ S)
    (F : Sheaf X.smallEtaleTopology Ab.{u + 1})
    (hFlc : Stacks.ConstantSheaf.IsLocallyConstant X.smallEtaleTopology F)
    (hFtors : ∀ (x : GeometricPoint X) (a : (smallEtaleStalkAb x.hom).obj F),
      ∃ n : ℕ, 0 < n ∧
        (ringChar x.residueField = 0 ∨ Nat.Coprime n (ringChar x.residueField)) ∧ n • a = 0)
    (hf : IsLocallyAcyclic B hX hS f) :
    IsLocallyAcyclicRelative B hX hS f
      ((DerivedCategory.singleFunctor (Sheaf X.smallEtaleTopology Ab.{u + 1}) 0).obj F)
```

## Tag 0GJS, a lemma

[Tag 0GJS](https://stacks.math.columbia.edu/tag/0GJS) in the Stacks Project.

**`AlgebraicGeometry.isLocallyAcyclicAt_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/BaseChangeTransfer.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/BaseChangeTransfer.lean#L101). The attribute's comment: “integral base change”.

> For a cartesian square of schemes with `g` integral, an
> object `K` of `D(X_étale)` and a geometric point `x'` of the fibre product with image `x` in `X`,
> local acyclicity of `f` at `x` relative to `K` implies local acyclicity of `f'` at `x'` relative
> to `(g')⁻¹K`.

```lean
public theorem isLocallyAcyclicAt_of_isIntegralHom [IsIntegralHom g]
    (h : IsLocallyAcyclicAt B hX hS f K (x'.map g')) :
    IsLocallyAcyclicAt B hX' hS' f' ((smallEtaleDerivedPullbackAb g').obj K) x'
```

**`AlgebraicGeometry.isLocallyAcyclicAt_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/BaseChangeTransfer.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/BaseChangeTransfer.lean#L113). The attribute's comment: “locally quasi-finite base change”. References: SGA 4½ Arcata (5.1.4), “more general”.

> For a cartesian square of schemes with `g` locally of finite type and locally quasi-finite, an
> object `K` of `D(X_étale)` and a geometric point `x'` of the fibre product with image `x` in `X`,
> local acyclicity of `f` at `x` relative to `K` implies local acyclicity of `f'` at `x'` relative
> to `(g')⁻¹K`.

```lean
public theorem isLocallyAcyclicAt_of_locallyQuasiFinite [LocallyOfFiniteType g]
    [LocallyQuasiFinite g] (h : IsLocallyAcyclicAt B hX hS f K (x'.map g')) :
    IsLocallyAcyclicAt B hX' hS' f' ((smallEtaleDerivedPullbackAb g').obj K) x'
```

**`AlgebraicGeometry.isLocallyAcyclicAt_of_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/BaseChangeTransfer.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/BaseChangeTransfer.lean#L146). The attribute's comment: “directed inverse limit base change”. References: SGA 4½ Arcata (5.1.4), “more general”.

> Let `{ Dᵢ }` be an inverse system of
> schemes indexed by a cofiltered category, with affine transition morphisms, whose stages are
> locally of finite type and locally quasi-finite over `S` compatibly with the transition
> morphisms, let `S' = lim Dᵢ`, and let
>
> ```
> X' --g'--> X
> |f'        |f
> S' --g---> S
> ```
>
> be a cartesian square whose `g` is induced by the morphisms from the stages. For an object `K` of
> `D(X_étale)` and a geometric point `x'` of `X'` with image `x` in `X`, local acyclicity of `f` at
> `x` relative to `K` implies local acyclicity of `f'` at `x'` relative to `(g')⁻¹K`.

```lean
public theorem isLocallyAcyclicAt_of_limit (p : ∀ i : I, D.obj i ⟶ S)
    (hp : ∀ i : I, c.π.app i ≫ p i = g) (hcompat : ∀ {i j : I} (a : i ⟶ j), D.map a ≫ p j = p i)
    [∀ i : I, LocallyOfFiniteType (p i)] [∀ i : I, LocallyQuasiFinite (p i)]
    (h : IsLocallyAcyclicAt B hX hS f K (x'.map g')) :
    IsLocallyAcyclicAt B hX' hS' f' ((smallEtaleDerivedPullbackAb g').obj K) x'
```

**`AlgebraicGeometry.isLocallyAcyclicAt_strictHenselizationBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StrictHenselizationBaseChangeSite.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StrictHenselizationBaseChangeSite.lean#L87). The attribute's comment: “base change along the strict henselization at a geometric point”. References: SGA 4½ Arcata (5.1.4), “special case”; SGA 4½ Arcata (5.1.6), “more general”.

> **Local acyclicity survives base change to the strict henselization.** Let `f : X ⟶ S` be
> a morphism of schemes of a big étale site `B`, let `K` be an object of `D(X_étale)`, let `s` be a
> geometric point of `S` and let `x` be a geometric point of the base change
> `Y = X ×_S Spec 𝒪^{sh}_{S,s}` with image `y` in `X`. If `f` is locally acyclic at `y` relative to
> `K`, then the projection `Y ⟶ Spec 𝒪^{sh}_{S,s}` is locally acyclic at `x` relative to `K|_Y`.

```lean
theorem isLocallyAcyclicAt_strictHenselizationBaseChange
    (x : GeometricPoint (strictHenselizationBaseChange B hS f s))
    (h : IsLocallyAcyclicAt B hX hS f K
      (x.map (strictHenselizationBaseChangeToSource B hS f s))) :
    IsLocallyAcyclicAt B (contains_strictHenselizationBaseChange B hS hX f s)
      (contains_strictHenselization_of_contains B hS s)
      (strictHenselizationBaseChangeToStrictHenselization B hS f s)
      ((smallEtaleDerivedPullbackAb
        (strictHenselizationBaseChangeToSource B hS f s)).obj K) x
```

**`AlgebraicGeometry.isLocallyAcyclicRelative_strictHenselizationBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StrictHenselizationBaseChangeSite.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LocalAcyclicity/StrictHenselizationBaseChangeSite.lean#L111). The attribute's comment: “base change along the strict henselization at a geometric point”. References: SGA 4½ Arcata (5.1.6), “more general”.

> **Local acyclicity survives base change to the strict henselization.** If `f : X ⟶ S` is
> locally acyclic relative to an object `K` of `D(X_étale)`, then the projection
> `X ×_S Spec 𝒪^{sh}_{S,s} ⟶ Spec 𝒪^{sh}_{S,s}` is locally acyclic relative to the restriction of
> `K` to the base change.

```lean
theorem isLocallyAcyclicRelative_strictHenselizationBaseChange
    (hla : IsLocallyAcyclicRelative B hX hS f K) :
    IsLocallyAcyclicRelative B (contains_strictHenselizationBaseChange B hS hX f s)
      (contains_strictHenselization_of_contains B hS s)
      (strictHenselizationBaseChangeToStrictHenselization B hS f s)
      ((smallEtaleDerivedPullbackAb
        (strictHenselizationBaseChangeToSource B hS f s)).obj K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.93, Tag 0GJM](https://stacks.math.columbia.edu/tag/0GJM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
