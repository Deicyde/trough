---
declaration: section
origin: cited
lean: Stacks.Cohomology.ModuleSections.globalSectionsKInjectiveIso_naturality, Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedAdjunction, Stacks.Cohomology.DerivedPullbackOfToposHom.derivedAdjunction, Stacks.Cohomology.DerivedPushforward.derivedPullbackPushforwardAdjunctionOfToposHom, Stacks.Cohomology.DerivedPushforwardCompositionOfToposHom.isIso_derivedPushforwardComparison_unconditional, Stacks.Cohomology.DerivedPushforwardCompositionOnTopoi.isIso_derivedPushforwardComparison_unconditional, Stacks.Cohomology.DerivedPushforwardCompositionOnTopoi.derivedPushforwardCompIsoUnconditional, Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMap
statement: formalized
proof: formalized
---

# 21.19 Cohomology of unbounded complexes

Section 21.19 of the Stacks Project, [Tag 07A5](https://stacks.math.columbia.edu/tag/07A5). 9 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07A5, the section

[Tag 07A5](https://stacks.math.columbia.edu/tag/07A5) in the Stacks Project.

**`Stacks.Cohomology.ModuleSections.globalSectionsKInjectiveIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/KInjectiveSectionsNaturality.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedSections/KInjectiveSectionsNaturality.lean#L60). The attribute's comment: “global sections of modules on a ringed site, naturality of the comparison”.

> **The comparison of global sections with derived global sections on a K-injective complex
> is natural.** For a morphism `t : I ⟶ J` of K-injective complexes of `O`-modules, the class of
> the induced morphism of global section complexes corresponds to the morphism
> `RΓ(C, I) ⟶ RΓ(C, J)` induced by the class of `t`.

```lean
theorem globalSectionsKInjectiveIso_naturality
    {I J : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    [I.IsKInjective] [J.IsKInjective]
    (t : I ⟶ J) :
    DerivedCategory.Q.map
          (((moduleGlobalSections X).mapHomologicalComplex (ComplexShape.up ℤ)).map t) ≫
        (globalSectionsKInjectiveIso X J).hom =
      (globalSectionsKInjectiveIso X I).hom ≫
        (derivedModuleGlobalSections X).map (DerivedCategory.Q.map t)
```

## Tag 07A6, a lemma

[Tag 07A6](https://stacks.math.columbia.edu/tag/07A6) in the Stacks Project.

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean#L164). The attribute's comment: “for a morphism of ringed topoi presented by a morphism of the underlying sites, at RingedTopos.{u, u, u}”.

> **Stacks 07A6 along an arbitrary morphism of ringed topoi.**  The unbounded derived
> pullback `Lf^*` is left adjoint to the unbounded derived pushforward `Rf_*`.
>
> This is `derivedPullbackPushforwardAdjunctionOfKFlat` with its one deferred input supplied by
> `pullbackInvertsQuasiIso_isKFlat`.  An `Adjunction` is exactly the bifunctorial bijection
> `Hom_{D(𝒪_C)}(Lf^*G, F) = Hom_{D(𝒪_D)}(G, Rf_*F)` that the source states: its `homEquiv` is
> the bijection and `Adjunction.homEquiv_naturality_left`, `homEquiv_naturality_right` are its
> naturality in the two arguments.
>
> The only input is `hmos`, and it is not an assumption beyond the source's.  `RingedToposSiteHom`
> records continuity of `f.u` and nothing else, so `f` alone is a morphism of ringed *sites*;
> `hmos : f.u.IsMorphismOfSites Y.J X.J` adds the exactness of `f^{-1}` that Stacks 00X1 demands,
> which is what makes `f` a morphism of ringed *topoi* (Stacks 00XC,
> `CategoryTheory.Functor.IsMorphismOfSites.morphismOfTopoi`).  Everything else the construction
> needed has been discharged: the deferred exactness input is `pullbackInvertsQuasiIso_isKFlat`,
> which holds along every morphism of ringed topoi, and the `HasLeftDerivedFunctor` binder is a
> `Prop` class discharged by `hasLeftDerivedFunctor_pullbackOnHomotopy`.

```lean
noncomputable def derivedAdjunction : derivedPullback f ⊣ derivedPushforward f
```

**`Stacks.Cohomology.DerivedPullbackOfToposHom.derivedAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/DerivedAdjunctionOfToposHom.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/DerivedAdjunctionOfToposHom.lean#L195). The attribute's comment: “for a morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) -- a morphism of the underlying topoi together with the structure map, with no continuous functor between the underlying sites -- and with no hypothesis beyond those making the two categories of modules exist”.

> **Stacks 07A6 for a morphism of ringed topoi.**  The total left derived pullback `Lf^*` is
> left adjoint to the total right derived direct image `Rf_*`,
> `Hom_{D(𝒪)}(Lf^*𝒢, ℱ) = Hom_{D(𝒪')}(𝒢, Rf_*ℱ)`, bifunctorially in the unbounded derived
> categories.
>
> This is `Stacks.Cohomology.DerivedPushforward.derivedPullbackPushforwardAdjunction`, Stacks 07A6
> relative to the Stacks 06YY datum, at the datum `kFlatLeftDerivedPullback`; the hypothesis for
> whose sake the attribute is withheld there is discharged, so there is none left.

```lean
def derivedAdjunction (f : RingedToposHom X Y) :
    derivedPullback f ⊣ derivedPushforward (X := X) (Y := Y) f
```

**`Stacks.Cohomology.DerivedPushforward.derivedPullbackPushforwardAdjunctionOfToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/PullbackAdjunctionOfToposHom.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/PullbackAdjunctionOfToposHom.lean#L76). The attribute's comment: “for a morphism of ringed topoi whose two sites are small in the universe of the sections of their structure sheaves”.

> For a morphism of ringed topoi `f`, the derived pullback `Lf^*` is left adjoint to the
> derived direct image `Rf_*` on the unbounded derived categories,
> `Hom_{D(𝒪)}(Lf^*G, F) = Hom_{D(𝒪')}(G, Rf_*F)`.

```lean
def derivedPullbackPushforwardAdjunctionOfToposHom :
    DerivedPullbackOfToposHom.derivedPullback f ⊣ derivedPushforward (X := X) (Y := Y) f
```

## Tag 0D6E, a lemma

[Tag 0D6E](https://stacks.math.columbia.edu/tag/0D6E) in the Stacks Project.

**`Stacks.Cohomology.DerivedPushforwardCompositionOfToposHom.isIso_derivedPushforwardComparison_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CompositionOfToposHomUnconditional.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CompositionOfToposHomUnconditional.lean#L560). The attribute's comment: “for a morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) -- a morphism of the underlying topoi together with the structure map, with no continuous functor between the underlying sites -- and with no hypothesis on either morphism; the three universes of each of the three ringed topoi are free and unrelated”.

> **Stacks 0D6E for a morphism of ringed topoi.**  For composable morphisms of ringed topoi
> `f : (Sh(𝒞), 𝒪_𝒞) ⟶ (Sh(𝒟), 𝒪_𝒟)` and `g : (Sh(𝒟), 𝒪_𝒟) ⟶ (Sh(ℰ), 𝒪_ℰ)`, the canonical
> comparison from a derived direct image along `g ∘ f` to the composite of the derived direct
> images along `f` and `g` is an isomorphism, so `Rg_* ∘ Rf_* = R(g ∘ f)_*` as functors
> `D(𝒪_𝒞) ⟶ D(𝒪_ℰ)`.
>
> There is **no hypothesis on either morphism**: the geometric datum is the two-field morphism of
> ringed topoi of Stacks 01D3, part (2), with no continuous functor between the underlying sites,
> and the condition that
> `AlgebraicGeometry.RingedToposHom.derivedPushforwardComparison_isIso` carries — Stacks 093Y for
> `f`, which at module coefficients Stacks 075L records as false in general — is discharged by
> `isIso_app_pushforwardMapHomotopy_of_isKInjective`.

```lean
theorem isIso_derivedPushforwardComparison_unconditional
    [Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg (HomotopyCategory.quasiIso Y.Modules (ComplexShape.up ℤ))]
    [Rh.IsRightDerivedFunctor αh (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))] :
    IsIso (derivedPushforwardComparison f g Rf Rg Rh αf αg αh)
```

**`Stacks.Cohomology.DerivedPushforwardCompositionOnTopoi.isIso_derivedPushforwardComparison_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CompositionOnRingedTopoiUnconditional.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CompositionOnRingedTopoiUnconditional.lean#L535).

> **Stacks 0D6E.**  For composable morphisms of ringed topoi `f : (Sh(𝒞), 𝒪_𝒞) ⟶ (Sh(𝒟), 𝒪_𝒟)`
> and `g : (Sh(𝒟), 𝒪_𝒟) ⟶ (Sh(ℰ), 𝒪_ℰ)`, the canonical comparison from a derived pushforward along
> `g ∘ f` to the composite of derived pushforwards along `f` and `g` is an isomorphism, so
> `Rg_* ∘ Rf_* = R(g ∘ f)_*` as functors `D(𝒪_𝒞) ⟶ D(𝒪_ℰ)`.
>
> No hypothesis beyond the two morphisms and the three presentations of the derived pushforwards:
> the condition `PushforwardComputesDerived`, which `isIso_derivedPushforwardComparison_iff` shows
> to be equivalent to this statement, is discharged by `pushforwardComputesDerived`.

```lean
theorem isIso_derivedPushforwardComparison_unconditional
    [Rf.IsRightDerivedFunctor αf
      (HomotopyCategory.quasiIso (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
          (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg
      (HomotopyCategory.quasiIso (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
          (ComplexShape.up ℤ))]
    [Rh.IsRightDerivedFunctor αh
      (HomotopyCategory.quasiIso (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
          (ComplexShape.up ℤ))] :
    IsIso (derivedPushforwardComparison f g Rf Rg Rh αf αg αh)
```

**`Stacks.Cohomology.DerivedPushforwardCompositionOnTopoi.derivedPushforwardCompIsoUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CompositionOnRingedTopoiUnconditional.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/CompositionOnRingedTopoiUnconditional.lean#L555). The attribute's comment: “as a natural isomorphism”.

> **Stacks 0D6E as a natural isomorphism** `Rf_* ⋙ Rg_* ≅ R(g ∘ f)_*`, obtained by inverting
> the canonical comparison.  This is the source's equality of composite functors, in the only form
> in which it can hold: the two functors are total derived functors of different functors on the
> homotopy category, so they agree up to the canonical isomorphism and not on the nose.

```lean
noncomputable def derivedPushforwardCompIsoUnconditional
    [Rf.IsRightDerivedFunctor αf
      (HomotopyCategory.quasiIso (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
          (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg
      (HomotopyCategory.quasiIso (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
          (ComplexShape.up ℤ))]
    [Rh.IsRightDerivedFunctor αh
      (HomotopyCategory.quasiIso (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
          (ComplexShape.up ℤ))] :
    Rf ⋙ Rg ≅ Rh
```

## Tag 07A7, a remark

[Tag 07A7](https://stacks.math.columbia.edu/tag/07A7) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangeOfToposHom.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangeOfToposHom.lean#L176). The attribute's comment: “the canonical derived base change map `Lg^* Rf_* K ⟶ Rf'_* L(g')^* K` of a commutative square of morphisms of ringed topoi in the two-field sense of Tag 01D3, part (2) -- a morphism of the underlying topoi together with the map of structure sheaves, with no continuous functor between the underlying sites -- at the twelve free universes of the four ringed topoi”. References: SGA 6 IV (3.1.0).

> For a commutative square of morphisms of ringed topoi
>
> ```
>                 g'
>   (Sh(C'), 𝒪_{C'}) --→ (Sh(C), 𝒪_C)
>         |  f'                |  f
>         v                    v
>   (Sh(D'), 𝒪_{D'}) --→ (Sh(D), 𝒪_D)
>                 g
> ```
>
> and an object `K` of the unbounded derived category `D(𝒪_C)`, the canonical base change map
>
> `Lg^* Rf_* K ⟶ Rf'_* L(g')^* K`
>
> in `D(𝒪_{D'})`.

```lean
def derivedBaseChangeMap (h : g.comp f' = f.comp g')
    (K : DerivedCategory
      (SheafOfModules.{wC} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := X.J)) X.O))) :
    (derivedPullback g).obj ((derivedPushforward f).obj K) ⟶
      (derivedPushforward f').obj ((derivedPullback g').obj K)
```

**`Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMap_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangeOfToposHom.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangeOfToposHom.lean#L192). The attribute's comment: “the adjoint characterization which the source gives of the base change map of a commutative square of morphisms of ringed topoi in the two-field sense of Tag 01D3, part (2), and which pins the map down: its adjunct under `L(f')^* ⊣ Rf'_*` is `L(g')^*` of the derived counit, across the two composition isomorphisms of Tag 0D6D”.

> **The adjoint characterization of the base change map.** Under the derived adjunction
> `L(f')^* ⊣ Rf'_*`, the base change map of a commutative square of morphisms of ringed topoi is
> `L(g')^*` of the derived counit `Lf^* Rf_* K ⟶ K`, transported across the two composition
> isomorphisms.

```lean
theorem derivedBaseChangeMap_adjoint (h : g.comp f' = f.comp g')
    (K : DerivedCategory
      (SheafOfModules.{wC} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := X.J)) X.O))) :
    ((derivedAdjunction f').homEquiv
        ((derivedPullback g).obj ((derivedPushforward f).obj K))
        ((derivedPullback g').obj K)).symm
        (derivedBaseChangeMap f g' f' g h K) =
      (derivedPullbackCompIsoLeft f' g).hom.app ((derivedPushforward f).obj K) ≫
        (derivedPullbackCompIsoRight f g' f' g h).inv.app ((derivedPushforward f).obj K) ≫
        (derivedPullback g').map ((derivedAdjunction f).counit.app K)
```

## Tag 0E46, a remark

[Tag 0E46](https://stacks.math.columbia.edu/tag/0E46) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChangePasting.derivedBaseChangeMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangePastingOnRingedTopoi.lean, line 1068](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangePastingOnRingedTopoi.lean#L1068). The attribute's comment: “variant: the special case of squares of morphisms of ringed topoi presented by morphisms of sites; the tag for arbitrary morphisms of ringed topoi is Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMapOfTwoIso_vertical”.

> **The vertical pasting law, for ringed topoi presented by morphisms of sites.**  For two
> vertically composable commutative squares of ringed topoi whose arrows come from morphisms of the
> underlying sites, the composite of the derived base change maps of the two squares, read through
> the composition isomorphisms for the derived pushforward along the two composite vertical legs, is
> the derived base change map of the outer rectangle.
>
> Stacks 0E46 for arbitrary morphisms of ringed topoi is
> `Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMapOfTwoIso_vertical`.

```lean
theorem derivedBaseChangeMap_comp (htop : l.comp f' = f.comp k) (hbot : m.comp g' = g.comp l)
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf B.O))) :
    (derivedPullback m).map ((derivedPushforwardCompIso f g hmosf hmosg).inv.app K) ≫
        derivedBaseChangeMap g l g' m hmosg hmosl hmosg' hmosm hbot
          ((derivedPushforward f).obj K) ≫
        (derivedPushforward g').map
          (derivedBaseChangeMap f k f' l hmosf hmosk hmosf' hmosl htop K) ≫
        (derivedPushforwardCompIso f' g' hmosf' hmosg').hom.app ((derivedPullback k).obj K) =
      derivedBaseChangeMap (g.comp f) k (g'.comp f') m
        (RingedToposSiteHom.isMorphismOfSites_comp_u f g hmosf hmosg) hmosk
        (RingedToposSiteHom.isMorphismOfSites_comp_u f' g' hmosf' hmosg') hmosm
        (comp_stack f g f' g' k l m htop hbot) K
```

**`Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMapOfTwoIso_vertical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangeVerticalPastingOfToposHom.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangeVerticalPastingOfToposHom.lean#L456).

> **Stacks 0E46.**  Consider a commutative diagram of ringed topoi
>
> ```
>                  k
>   (Sh(B'), 𝒪) ———→ (Sh(B), 𝒪)
>        │ f'              │ f
>        v        l        v
>   (Sh(C'), 𝒪) ———→ (Sh(C), 𝒪)
>        │ g'              │ g
>        v                 v
>   (Sh(D'), 𝒪) ———→ (Sh(D), 𝒪)
>                  m
> ```
>
> in which each square commutes up to the given 2-isomorphism (Stacks 04IC):
> `st : l ∘ f' ≅ f ∘ k` and `sb : m ∘ g' ≅ g ∘ l`, the outer rectangle commuting up to their
> pasting `AlgebraicGeometry.RingedToposHom.TwoIso.pasteVertical st sb`.  Then the base change
> maps of Remark 07A7 for the two squares compose to the base change map of the rectangle: for
> `K` in `D(𝒪_B)`, the composite
>
> `Lm^* R(g ∘ f)_* K = Lm^* Rg_* Rf_* K ⟶ Rg'_* Ll^* Rf_* K ⟶ Rg'_* Rf'_* Lk^* K
>   = R(g' ∘ f')_* Lk^* K`
>
> is the base change map of the rectangle.  The two identifications `=` are the composition
> isomorphisms of Stacks 0D6E, `derivedPushforwardCompIsoOfAdjoints`.
>
> The seven morphisms are arbitrary morphisms of ringed topoi in the sense of Stacks 01D3,
> part (2), the two 2-isomorphisms are arbitrary, and the eighteen universes of the six ringed topoi
> are free.  As for the base change map of Remark 07A7 itself (`derivedBaseChangeMapOfTwoIso`), the
> module categories of the ringed topoi at the sources of the vertical arrows carry the instance
> `CategoryTheory.IsGrothendieckAbelian` at their section universes, which is what makes the
> unbounded derived pushforwards exist at free universes (see the implementation notes of
> `StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/Existence.lean`).

```lean
theorem derivedBaseChangeMapOfTwoIso_vertical
    (st : RingedToposHom.TwoIso (l.comp f') (f.comp k))
    (sb : RingedToposHom.TwoIso (m.comp g') (g.comp l)) (K :
      DerivedCategory (SheafOfModules.{wB} (SheafOfModules.Tensor.ringSheaf B.O))) :
    (derivedPullback m).map ((derivedPushforwardCompIsoOfAdjoints f g).inv.app K) ≫
        derivedBaseChangeMapOfTwoIso g l g' m sb ((derivedPushforward f).obj K) ≫
        (derivedPushforward g').map (derivedBaseChangeMapOfTwoIso f k f' l st K) ≫
        (derivedPushforwardCompIsoOfAdjoints f' g').hom.app ((derivedPullback k).obj K) =
      derivedBaseChangeMapOfTwoIso (g.comp f) k (g'.comp f') m
        (RingedToposHom.TwoIso.pasteVertical st sb) K
```

## Tag 0E47, a remark

[Tag 0E47](https://stacks.math.columbia.edu/tag/0E47) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChangeOfToposHom.derivedBaseChangeMapOfTwoIso_horizontal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangePastingOfToposHom.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangePastingOfToposHom.lean#L388).

> **Stacks 0E47.**  Consider a commutative diagram of ringed topoi
>
> ```
>             g'              g
>   (Sh(C''), 𝒪) ———→ (Sh(C'), 𝒪) ———→ (Sh(C), 𝒪)
>        │ f''              │ f'              │ f
>        v                  v                 v
>   (Sh(D''), 𝒪) ———→ (Sh(D'), 𝒪) ———→ (Sh(D), 𝒪)
>             h'              h
> ```
>
> in which each square commutes up to the given 2-isomorphism (Stacks 04IC):
> `s : h ∘ f' ≅ f ∘ g` and `s' : h' ∘ f'' ≅ f' ∘ g'`, the outer rectangle commuting up to their
> pasting `AlgebraicGeometry.RingedToposHom.TwoIso.pasteHorizontal s s'`.  Then the base change
> maps of Remark 07A7 for the two squares compose to the base change map of the rectangle: for
> `K` in `D(𝒪_C)`, the composite
>
> `L(h ∘ h')^* Rf_* K = L(h')^* Lh^* Rf_* K ⟶ L(h')^* Rf'_* Lg^* K ⟶ Rf''_* L(g')^* Lg^* K
>   = Rf''_* L(g ∘ g')^* K`
>
> is the base change map of the rectangle.  The two identifications `=` are the composition
> isomorphisms of Stacks 0D6D.
>
> The six morphisms are arbitrary morphisms of ringed topoi in the sense of Stacks 01D3,
> part (2), the two 2-isomorphisms are arbitrary, and the eighteen universes of the six ringed topoi
> are free.  As for the base change map of Remark 07A7 itself (`derivedBaseChangeMapOfTwoIso`), the
> module categories of the three upper ringed topoi carry the instance
> `CategoryTheory.IsGrothendieckAbelian` at their section universes, which is what makes the
> unbounded `Rf_*` exist at free universes (see the implementation notes of
> `StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/Existence.lean`).

```lean
theorem derivedBaseChangeMapOfTwoIso_horizontal
    (s : RingedToposHom.TwoIso (h.comp f') (f.comp g))
    (s' : RingedToposHom.TwoIso (h'.comp f'') (f'.comp g')) (K :
      DerivedCategory (SheafOfModules.{wC} (SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedPullbackCompIso h' h).inv.app ((derivedPushforward f).obj K) ≫
        (derivedPullback h').map (derivedBaseChangeMapOfTwoIso f g f' h s K) ≫
        derivedBaseChangeMapOfTwoIso f' g' f'' h' s' ((derivedPullback g).obj K) ≫
        (derivedPushforward f'').map ((derivedPullbackCompIso g' g).hom.app K) =
      derivedBaseChangeMapOfTwoIso f (g.comp g') f'' (h.comp h')
        (RingedToposHom.TwoIso.pasteHorizontal s s') K
```

**`Stacks.Cohomology.DerivedBaseChangePasting.derivedBaseChangeMap_horizontal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangePastingOnRingedTopoi.lean, line 796](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/BaseChangePastingOnRingedTopoi.lean#L796).

> **Stacks 0E47.**  For two horizontally composable commutative squares of ringed topoi, the
> composite of the derived base change maps of the two squares, read through the composition
> isomorphisms of Stacks 0D6D for the two composite horizontal legs, is the derived base change map
> of the outer rectangle.

```lean
theorem derivedBaseChangeMap_horizontal (hmosf : f.u.IsMorphismOfSites Y.J X.J)
    (hmosf' : f'.u.IsMorphismOfSites Y'.J X'.J) (hmosf'' : f''.u.IsMorphismOfSites Y''.J X''.J)
    (hmosg' : g'.u.IsMorphismOfSites X.J X'.J) (hmosg'' : g''.u.IsMorphismOfSites X'.J X''.J)
    (hmosg : g.u.IsMorphismOfSites Y.J Y'.J) (hmosh : h.u.IsMorphismOfSites Y'.J Y''.J)
    (sq : g.comp f' = f.comp g') (sq' : h.comp f'' = f'.comp g'')
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    (derivedPullbackCompIso h g hmosh hmosg).inv.app ((derivedPushforward f).obj K) ≫
        (derivedPullback h).map
          (derivedBaseChangeMap f g' f' g hmosf hmosg' hmosf' hmosg sq K) ≫
        derivedBaseChangeMap f' g'' f'' h hmosf' hmosg'' hmosf'' hmosh sq'
          ((derivedPullback g').obj K) ≫
        (derivedPushforward f'').map
          ((derivedPullbackCompIso g'' g' hmosg'' hmosg').hom.app K) =
      derivedBaseChangeMap f (g'.comp g'') f'' (g.comp h) hmosf
        (RingedToposSiteHom.isMorphismOfSites_comp_u g'' g' hmosg'' hmosg') hmosf''
        (RingedToposSiteHom.isMorphismOfSites_comp_u h g hmosh hmosg)
        (comp_rectangle f f' f'' g' g'' g h sq sq') K
```

## Tag 0FPI, a lemma

[Tag 0FPI](https://stacks.math.columbia.edu/tag/0FPI) in the Stacks Project.

**`Stacks.Cohomology.DerivedPullbackOfToposHom.derivedAdjunction_counit_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/DerivedAdjunctionOfToposHom.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/DerivedAdjunctionOfToposHom.lean#L225). The attribute's comment: “for a morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) -- a morphism of the underlying topoi together with the structure map, with no continuous functor between the underlying sites -- and with no hypothesis beyond those making the two categories of modules exist; stated at an object of the unbounded homotopy category, which a complex gives through `HomotopyCategory.quotient`”.

> **Stacks 0FPI for a morphism of ringed topoi.**  For a complex `𝒦` of `𝒪`-modules the square
>
> ```
> Lf^* f_* 𝒦 ⟶ f^* f_* 𝒦
>     ↓               ↓
> Lf^* Rf_* 𝒦 ⟶       𝒦
> ```
>
> commutes in `D(𝒪)`: its upper edge is the comparison `Lf^* ⟶ f^*` of Stacks 06YY at `f_*𝒦`, its
> left edge is `Lf^*` applied to the comparison `f_* ⟶ Rf_*`, its lower edge is the counit of the
> derived adjunction `Lf^* ⊣ Rf_*` of Stacks 07A6 at `Rf_*𝒦`, and its right edge is the ordinary
> counit `f^*f_*𝒦 ⟶ 𝒦` of Stacks 03D7.
>
> The derived counit is by construction the one induced by the ordinary one, which is exactly this
> commutativity, so the proof is
> `Stacks.Cohomology.DerivedPushforward.derivedPullbackPushforwardAdjunction_counit_fac` at the
> datum `kFlatLeftDerivedPullback`.
>
> The square is stated for an object of the unbounded homotopy category rather than for a cochain
> complex, which is the form the comparison maps of the two derived functors take and is more
> general: a complex gives such an object through `HomotopyCategory.quotient`.

```lean
theorem derivedAdjunction_counit_fac (f : RingedToposHom X Y)
    (K : HomotopyCategory (SheafOfModules.{w} (SheafOfModules.Tensor.ringSheaf X.O))
      (ComplexShape.up ℤ)) :
    (derivedPullback f).map
        (((pushforwardOnHomotopy (X := X) (Y := Y) f).totalRightDerivedUnit DerivedCategory.Qh
          (sourceQuasiIso X)).app K) ≫
        (derivedAdjunction f).counit.app (DerivedCategory.Qh.obj K) =
      (derivedPullbackComparison f).app ((pushforwardMapHomotopy f).obj K) ≫
        DerivedCategory.Qh.map ((pullbackAdjPushforwardMapHomotopy f).counit.app K)
```

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedAdjunction_counit_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/OrdinaryAndDerivedCounit.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/OrdinaryAndDerivedCounit.lean#L117).

> **Stacks 0FPI.**  For a complex `K` of `𝒪_C`-modules the square
>
> ```
> Lf^* f_* K ⟶ f^* f_* K
>     ↓              ↓
> Lf^* Rf_* K ⟶      K
> ```
>
> commutes in `D(𝒪_C)`: its upper edge is the comparison `Lf^* ⟶ f^*`, its left edge is `Lf^*`
> applied to the comparison `f_* ⟶ Rf_*`, its lower edge is the counit of the derived adjunction
> `Lf^* ⊣ Rf_*`, and its right edge is the ordinary counit `f^* f_* ⟶ id`.
>
> The derived counit is the one induced by the ordinary counit, which is exactly this
> commutativity, so the proof is `derivedPullbackPushforwardAdjunctionOfKFlat_counit_fac`.
>
> The source's hypothesis is just that `f` be a morphism of ringed topoi, and `hmos` is how that is
> spelled here, not an extra condition: `AlgebraicGeometry.RingedToposSiteHom` records only the
> continuity of `f.u`, while `CategoryTheory.Functor.IsMorphismOfSites` is the library's encoding
> of Stacks 00X1 — continuity together with exactness of `f^{-1}` — and by Stacks 00XC
> (`CategoryTheory.Functor.IsMorphismOfSites.morphismOfTopoi`) it is exactly `hmos` that makes the
> geometric datum of `f` a morphism of topoi.  See the implementation notes above for the
> presentation restriction, which is the repository's convention for ringed topoi and is separate
> from `hmos`.

```lean
theorem derivedAdjunction_counit_fac
    (K : HomotopyCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
      (ComplexShape.up ℤ)) :
    (derivedPullback f).map ((derivedPushforwardUnit f).app K) ≫
        (derivedAdjunction f hmos).counit.app (DerivedCategory.Qh.obj K) =
      (derivedPullbackComparison f).app
          ((f.pushforwardTopos.mapHomotopyCategory (ComplexShape.up ℤ)).obj K) ≫
        DerivedCategory.Qh.map
          ((homotopyPullbackPushforwardAdjunction f).counit.app K)
```

## Tag 0B6C, a remark

[Tag 0B6C](https://stacks.math.columbia.edu/tag/0B6C) in the Stacks Project.

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProduct.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProduct.lean#L250). The attribute's comment: “the relative cup product”.

> **[Stacks, Tag 0B6C].**  For a morphism of ringed topoi
> `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and objects `K`, `L` of `D(O_C)`, the canonical relative cup
> product
>
> `Rf_*K ⊗^L_{O_D} Rf_*L ⟶ Rf_*(K ⊗^L_{O_C} L)`,
>
> with no further hypothesis.  It is the map adjoint, for the adjunction `Lf^* ⊣ Rf_*` of
> [Stacks, Tag 07A6], to the bifunctorial identification
> `Lf^*(Rf_*K ⊗^L Rf_*L) ≅ Lf^*Rf_*K ⊗^L Lf^*Rf_*L` of [Stacks, Tag 07A4] followed by the counit
> `Lf^*Rf_* ⟶ id` in each of the two factors.

```lean
def relativeCupProduct
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((derivedTensorProductFunctor Y.O).obj ((derivedPushforward f).obj K)).obj
        ((derivedPushforward f).obj L) ⟶
      (derivedPushforward f).obj (((derivedTensorProductFunctor X.O).obj K).obj L)
```

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProduct.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProduct.lean#L278). The attribute's comment: “naturality in the first object”.

> **Naturality of the relative cup product of [Stacks, Tag 0B6C] in the first object.**

```lean
theorem relativeCupProduct_naturality_left
    {K K' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (k : K ⟶ K')
    (L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((derivedTensorProductFunctor Y.O).map ((derivedPushforward f).map k)).app
          ((derivedPushforward f).obj L) ≫
        relativeCupProduct f hmos K' L =
      relativeCupProduct f hmos K L ≫
        (derivedPushforward f).map (((derivedTensorProductFunctor X.O).map k).app L)
```

**`Stacks.Cohomology.RelativeCupProductOnRingedTopoi.relativeCupProduct_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProduct.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProduct.lean#L293). The attribute's comment: “naturality in the second object”.

> **Naturality of the relative cup product of [Stacks, Tag 0B6C] in the second object.**

```lean
theorem relativeCupProduct_naturality_right
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    {L L' : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
    (l : L ⟶ L') :
    ((derivedTensorProductFunctor Y.O).obj ((derivedPushforward f).obj K)).map
          ((derivedPushforward f).map l) ≫
        relativeCupProduct f hmos K L' =
      relativeCupProduct f hmos K L ≫
        (derivedPushforward f).map (((derivedTensorProductFunctor X.O).obj K).map l)
```

**`Stacks.Cohomology.RelativeCupProductOfToposHom.relativeCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductOfToposHom.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/RelativeCupProductOfToposHom.lean#L116). The attribute's comment: “the relative cup product, for a morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) -- a morphism of the underlying topoi together with the structure map, with no continuous functor between the underlying sites and no morphism-of-sites hypothesis”.

> For a morphism of ringed topoi
> `f : (Sh(C), 𝒪_C) ⟶ (Sh(D), 𝒪_D)` — a morphism of the underlying topoi together with the
> structure map, with no functor between the underlying sites — and objects `K`, `L` of `D(𝒪_C)`,
> the relative cup product
>
> `Rf_*K ⊗^L_{𝒪_D} Rf_*L ⟶ Rf_*(K ⊗^L_{𝒪_C} L)`.
>
> It is the map adjoint, for the adjunction `Lf^* ⊣ Rf_*` of [Stacks, Tag 07A6], to the
> identification `Lf^*(Rf_*K ⊗^L Rf_*L) ≅ Lf^*Rf_*K ⊗^L Lf^*Rf_*L` of [Stacks, Tag 07A4] followed
> by the counit `Lf^*Rf_* ⟶ id` in each of the two factors.

```lean
def relativeCupProduct
    (K L : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ((derivedTensorProductFunctor Y.O).obj ((derivedPushforward f).obj K)).obj
        ((derivedPushforward f).obj L) ⟶
      (derivedPushforward f).obj (((derivedTensorProductFunctor X.O).obj K).obj L)
```

## Tag 0DD7, a lemma

[Tag 0DD7](https://stacks.math.columbia.edu/tag/0DD7) in the Stacks Project.

**`Stacks.Torsion.torsionSheafProperty_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsion/DerivedCategoryOfTorsionSheaves.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsion/DerivedCategoryOfTorsionSheaves.lean#L566). The attribute's comment: “Serre subcategory”.

> Torsion abelian sheaves form a Serre subcategory.

```lean
public instance torsionSheafProperty_isSerreClass :
    (torsionSheafProperty J).IsSerreClass
```

**`Stacks.Torsion.exists_torsionDerivedEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Torsion/DerivedCategoryOfTorsionSheaves.lean, line 1118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Torsion/DerivedCategoryOfTorsionSheaves.lean#L1118). The attribute's comment: “derived equivalence”.

> **Stacks 0DD7.** The derived category of torsion abelian sheaves is equivalent to the full
> subcategory of the derived category of all abelian sheaves consisting of objects with torsion
> cohomology.  Under this equivalence, the inclusion is the derived functor of the inclusion of
> torsion sheaves.

```lean
public theorem exists_torsionDerivedEquivalence :
    ∃ e : DerivedCategory (TorsionSheaf J) ≌ TorsionDerivedCategory J,
      Nonempty (e.functor ⋙ (torsionCohomologyProperty J).ι ≅
        (torsionSheafProperty J).ι.mapDerivedCategory)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.19, Tag 07A5](https://stacks.math.columbia.edu/tag/07A5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
