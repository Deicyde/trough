---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.derivedLocallyQuasicoherentFlatBaseChange_derivedFppfModulePullback, AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback, AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback_comp_ι, AlgebraicGeometry.Stack.isLeftDerivable_toDerivedCategoryQuasicoherent_comp_pullback, AlgebraicGeometry.Stack.FlatFppf.isLeftDerivable_of_parasiticFreePart, AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc, AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc_comp_ι, AlgebraicGeometry.Stack.FlatFppf.isLeftDerivable_derivedSheafFlatBaseChangePullbackSucc
statement: formalized
proof: formalized
---

# 104.7 Derived pullback of quasi-coherent modules

Section 104.7 of the Stacks Project, [Tag 07BD](https://stacks.math.columbia.edu/tag/07BD). 1 tag here is carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07BE, a proposition

[Tag 07BE](https://stacks.math.columbia.edu/tag/07BE) in the Stacks Project.

**`AlgebraicGeometry.Stack.derivedLocallyQuasicoherentFlatBaseChange_derivedFppfModulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L213). The attribute's comment: “the first assertion, that f^* carries D\_LQCoh^fbc(𝒪\_𝒴) into D\_LQCoh^fbc(𝒪\_𝒳), on objects; conditional on the module-level statement that f^* maps LQCoh^fbc(𝒪\_𝒴) into LQCoh^fbc(𝒪\_𝒳) (Stacks 0771 part (3), the source's Cohomology of Stacks, Proposition 103.8.1), carried as the hypothesis hpres”.

> **Stacks 07BE, the first assertion, on objects.**  Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of
> algebraic stacks and let `K` be an object of `D_{LQCoh^fbc}(𝒪_𝒴)`.  Then `f^*K` is an object of
> `D_{LQCoh^fbc}(𝒪_𝒳)`.
>
> Since `f^*` is exact its cohomology modules are the inverse images of those of `K`, so the
> statement reduces degree by degree to the module-level **Stacks 0771** part (3) — that `f^*`
> maps `LQCoh^fbc(𝒪_𝒴)` into `LQCoh^fbc(𝒪_𝒳)` — which is the hypothesis `hpres`.

```lean
theorem derivedLocallyQuasicoherentFlatBaseChange_derivedFppfModulePullback
    (hpres : ∀ F : fppfModules B S hS 𝒴,
      locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒴 F →
        locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒳
          ((fppfModulesPullback B S hS f).obj F))
    (K : DerivedCategory (fppfModules B S hS 𝒴))
    (hK : derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴 K) :
    derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒳
      ((derivedFppfModulePullback B S hS f).obj K)
```

**`AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L234). The attribute's comment: “the first assertion, the induced functor D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_LQCoh^fbc(𝒪\_𝒳); conditional on the module-level Stacks 0771 part (3), carried as the hypothesis hpres”.

> **Stacks 07BE, the first assertion.**  The induced functor
> `f^* : D_{LQCoh^fbc}(𝒪_𝒴) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)`, the left vertical arrow of the square of the
> source.  Its composite with the inclusion of `D_{LQCoh^fbc}(𝒪_𝒳)` into `D(𝒪_𝒳)` is the
> composite of the inclusion of `D_{LQCoh^fbc}(𝒪_𝒴)` with `f^* : D(𝒪_𝒴) ⥤ D(𝒪_𝒳)`, which is the
> commutativity of the square; see
> `AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback_comp_ι`.

```lean
def derivedLocallyQuasicoherentPullback
    (hpres : ∀ F : fppfModules B S hS 𝒴,
      locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒴 F →
        locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒳
          ((fppfModulesPullback B S hS f).obj F)) :
    (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴).FullSubcategory ⥤
      (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒳).FullSubcategory
```

**`AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L253). The attribute's comment: “the commutativity of the square: the induced functor on D\_LQCoh^fbc, followed by the inclusion into D(𝒪\_𝒳), is the inclusion into D(𝒪\_𝒴) followed by f^*; conditional on the module-level Stacks 0771 part (3), carried as the hypothesis hpres”.

> **Stacks 07BE, the commutativity of the square.**  Restricting `f^*` to the subcategories of
> complexes with locally quasi-coherent cohomology and flat base change and then including into
> `D(𝒪_𝒳)` is the same as including into `D(𝒪_𝒴)` and applying `f^*`.

```lean
theorem derivedLocallyQuasicoherentPullback_comp_ι
    (hpres : ∀ F : fppfModules B S hS 𝒴,
      locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒴 F →
        locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒳
          ((fppfModulesPullback B S hS f).obj F)) :
    derivedLocallyQuasicoherentPullback B E hE S hS f hpres ⋙
        (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒳).ι =
      (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴).ι ⋙
        derivedFppfModulePullback B S hS f
```

**`AlgebraicGeometry.Stack.isLeftDerivable_toDerivedCategoryQuasicoherent_comp_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L324). The attribute's comment: “the second assertion, that q\_𝒳 ∘ f^* is left derivable with respect to the localization D\_LQCoh^fbc(𝒪\_𝒴) → D\_QCoh(𝒪\_𝒴) of 07B6, i.e. that LF is defined at every object; conditional on the Bousfield colocalization of 07BA, carried as the hypothesis hres, and on 0771 and 0774, carried as the triangulated-subcategory instances. The adjointness of Lf^*\_QCoh with Rf\_QCoh,* is NOT proved”.

> **Stacks 07BE, the second assertion.**  Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks.
> If every object of `D_{LQCoh^fbc}(𝒪_𝒴)` receives a morphism of the inverted class from an object
> left orthogonal to `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒴)` — the Bousfield colocalization of
> **Stacks 07BA** — then every functor out of `D_{LQCoh^fbc}(𝒪_𝒴)`, in particular the composite
>
> `D_{LQCoh^fbc}(𝒪_𝒴) --f^*--> D_{LQCoh^fbc}(𝒪_𝒳) --q_𝒳--> D_QCoh(𝒪_𝒳)`
>
> the source names, is left derivable with respect to the class of morphisms that the Verdier
> quotient `D_{LQCoh^fbc}(𝒪_𝒴) ⟶ D_QCoh(𝒪_𝒴)` of **Stacks 07B6** inverts, in the sense of
> **Stacks 05SV**: the left derived functor is defined at every object.
>
> The resolution is an initial object of the index category `S/E` of **Stacks 05S9**, which is the
> source's assertion that `E' ⟶ E` is cofinal in `S/E`; see
> `CategoryTheory.ObjectProperty.isLeftDerivable_trW_of_leftOrthogonal_resolutions`.

```lean
theorem isLeftDerivable_toDerivedCategoryQuasicoherent_comp_pullback
    [HasDerivedCategory.{t} (fppfModules B S hS 𝒳)]
    [PreservesFiniteColimits (fppfModulesPullback B S hS f)]
    [(locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒳).IsClosedUnderIsomorphisms]
    (hpres : ∀ F : fppfModules B S hS 𝒴,
      locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒴 F →
        locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒳
          ((fppfModulesPullback B S hS f).obj F))
    (hres : ∀ K : (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴).FullSubcategory,
      ∃ (K' : (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴).FullSubcategory)
        (s : K' ⟶ K), derivedQuasicoherentW B E hE S hS 𝒴 s ∧
          (derivedParasiticInLocallyQuasicoherent B E hE S hS (𝒴 := 𝒴)).leftOrthogonal K') :
    (derivedLocallyQuasicoherentPullback B E hE S hS f hpres ⋙
        toDerivedCategoryQuasicoherent B E hE S hS 𝒳).IsLeftDerivable
      (derivedQuasicoherentW B E hE S hS 𝒴)
```

**`AlgebraicGeometry.Stack.FlatFppf.isLeftDerivable_of_parasiticFreePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L374). The attribute's comment: “the second assertion, that q\_𝒳 ∘ f^* is left derivable with respect to the localization D\_LQCoh^fbc(𝒪\_𝒴) → D\_QCoh(𝒪\_𝒴) of 07B6, with the colocalization input supplied by 07BA; conditional on the derived module-level Lg\_! of 07AS (4) and on 07B9 (2)(a), (2)(c), carried as Lsh, adj, hunit and hK', on the module-level 0771 (3), carried as hpres, and on 0771 and 0774, carried as the triangulated-subcategory instances. The adjointness of Lf^*\_QCoh with Rf\_QCoh,* is NOT proved”.

> **Stacks 07BE, the second assertion, over Stacks 07BA.**  Let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks and let `g : Sh(𝒴_{flat,fppf}) ⟶ Sh(𝒴_{fppf})` be the morphism of
> ringed topoi of **Stacks 0788** (2).  Given the derived lower shriek `Lg_!` of **Stacks 07AS**
> part (4) — carried, as in **Stacks 07BA**, as a functor `Lsh`, an adjunction `Lsh ⊣ g^*` and the
> invertibility of its unit — and given that the parasitic-free part `Lg_! g^* K` of an object `K`
> of `D_{LQCoh^fbc}(𝒪_𝒴)` is again in `D_{LQCoh^fbc}(𝒪_𝒴)` (**Stacks 07B9** (2)(a), (2)(c),
> carried as `hK'`), the composite
>
> `D_{LQCoh^fbc}(𝒪_𝒴) --f^*--> D_{LQCoh^fbc}(𝒪_𝒳) --q_𝒳--> D_QCoh(𝒪_𝒳)`
>
> is left derivable with respect to the localization of **Stacks 07B6**.
>
> The resolution hypothesis of
> `AlgebraicGeometry.Stack.isLeftDerivable_toDerivedCategoryQuasicoherent_comp_pullback` is
> discharged from **Stacks 07BA**,
> `AlgebraicGeometry.Stack.FlatFppf.extensionProduct_parasiticFreePart`, through
> `AlgebraicGeometry.Stack.exists_derivedQuasicoherentW_leftOrthogonal_of_extensionProduct`.

```lean
theorem isLeftDerivable_of_parasiticFreePart
    [HasDerivedCategory.{t} (fppfModules B S hS 𝒳)]
    [HasDerivedCategory.{t'} (flatFppfModules B S hS 𝒴)]
    [PreservesFiniteColimits (fppfModulesPullback B S hS f)]
    [(locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒳).IsClosedUnderIsomorphisms]
    [(derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴).IsClosedUnderIsomorphisms]
    (Lsh : DerivedCategory (flatFppfModules B S hS 𝒴) ⥤ DerivedCategory (fppfModules B S hS 𝒴))
    (adj : Lsh ⊣ derivedModuleRestriction B S hS 𝒴) (hunit : IsIso adj.unit)
    (hpres : ∀ F : fppfModules B S hS 𝒴,
      locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒴 F →
        locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒳
          ((fppfModulesPullback B S hS f).obj F))
    (hK' : ∀ K : DerivedCategory (fppfModules B S hS 𝒴),
      derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴 K →
        derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴
          (parasiticFreePart B S hS 𝒴 Lsh K)) :
    (derivedLocallyQuasicoherentPullback B E hE S hS f hpres ⋙
        toDerivedCategoryQuasicoherent B E hE S hS 𝒳).IsLeftDerivable
      (derivedQuasicoherentW B E hE S hS 𝒴)
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L134). The attribute's comment: “the first assertion: the exact functor f^* induces D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_LQCoh^fbc(𝒪\_𝒳), with LQCoh^fbc the class of Stacks 0762 (flat base change for the pullback of sheaves), at module universe u + 1, for any models of the derived categories”.

> The functor `D_{LQCoh^fbc}(𝒪_𝒴) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)` induced by the exact functor
> `f^* : D(𝒪_𝒴) ⥤ D(𝒪_𝒳)`.

```lean
def derivedSheafFlatBaseChangePullbackSucc :
    (DerivedCategoryB.derivedCategoryB
        (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).FullSubcategory
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L147). The attribute's comment: “the commutative square of the first assertion, at module universe u + 1, for the class of Stacks 0762 read with the pullback of sheaves, for any models of the derived categories”.

> The induced functor followed by the inclusion `D_{LQCoh^fbc}(𝒪_𝒳) ⊆ D(𝒪_𝒳)` is the inclusion
> `D_{LQCoh^fbc}(𝒪_𝒴) ⊆ D(𝒪_𝒴)` followed by `f^* : D(𝒪_𝒴) ⥤ D(𝒪_𝒳)`.

```lean
theorem derivedSheafFlatBaseChangePullbackSucc_comp_ι :
    derivedSheafFlatBaseChangePullbackSucc B E h S hS f ⋙
        (DerivedCategoryB.derivedCategoryB (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).ι =
      (DerivedCategoryB.derivedCategoryB (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).ι ⋙
        (modulePullbackSucc B S hS f).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.FlatFppf.isLeftDerivable_derivedSheafFlatBaseChangePullbackSucc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L207). The attribute's comment: “the second assertion: q\_𝒳 ∘ f^* : D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_QCoh(𝒪\_𝒳) is left derivable with respect to D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_QCoh(𝒪\_𝒴) (Stacks 05SV), at module universe u + 1, for the class of Stacks 0762 read with the pullback of sheaves, at the standard models of the derived categories”.

> The composite
> `D_{LQCoh^fbc}(𝒪_𝒴) --f^*--> D_{LQCoh^fbc}(𝒪_𝒳) --q_𝒳--> D_QCoh(𝒪_𝒳)` is left derivable with
> respect to the localization `D_{LQCoh^fbc}(𝒪_𝒴) ⥤ D_QCoh(𝒪_𝒴)` of **Stacks 07B6**, in the sense
> of **Stacks 05SV**.

```lean
theorem isLeftDerivable_derivedSheafFlatBaseChangePullbackSucc :
    (derivedSheafFlatBaseChangePullbackSucc B E h S hS f ⋙
        (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
          (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).Q).IsLeftDerivable
      (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴))
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSucc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L220). The attribute's comment: “Lf^*\_QCoh : D\_QCoh(𝒪\_𝒴) ⥤ D\_QCoh(𝒪\_𝒳), the left derived functor of q\_𝒳 ∘ f^*, at module universe u + 1, at the standard models of the derived categories”.

> `Lf^*_QCoh : D_QCoh(𝒪_𝒴) ⥤ D_QCoh(𝒪_𝒳)`, the left derived functor of
> `q_𝒳 ∘ f^*` with respect to the quotient functor of `𝒴` (Stacks 05S9, 05SV).

```lean
def derivedQuasicoherentPullbackSucc :
    (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).Localization ⥤
      (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).Localization
```

**`AlgebraicGeometry.Stack.FlatFppf.isLeftDerivedFunctor_derivedQuasicoherentPullbackSucc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L243). The attribute's comment: “Lf^*\_QCoh is the (total) left derived functor of q\_𝒳 ∘ f^*, with counit derivedQuasicoherentPullbackSuccCounit, at module universe u + 1”.

> `Lf^*_QCoh` is the left derived functor of `q_𝒳 ∘ f^*`.

```lean
instance isLeftDerivedFunctor_derivedQuasicoherentPullbackSucc :
    (derivedQuasicoherentPullbackSucc B E h S hS f).IsLeftDerivedFunctor
      (derivedQuasicoherentPullbackSuccCounit B E h S hS f)
      (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴))
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSuccHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L351). The attribute's comment: “the third assertion: for f quasi-compact and quasi-separated, Hom\_D\_QCoh(𝒪\_𝒳)(Lf^*\_QCoh A, B) = Hom\_D\_QCoh(𝒪\_𝒴)(A, Rf\_QCoh,* B) for A in D\_QCoh(𝒪\_𝒴) and B in D⁺\_QCoh(𝒪\_𝒳), at module universe u + 1, for the class of Stacks 0762 read with the pullback of sheaves, at the standard models of the derived categories”.

> For a quasi-compact quasi-separated
> 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, `A ∈ D_QCoh(𝒪_𝒴)` and `B ∈ D⁺_QCoh(𝒪_𝒳)`,
>
> `Hom_{D_QCoh(𝒪_𝒳)}(Lf^*_QCoh A, B) ≃ Hom_{D_QCoh(𝒪_𝒴)}(A, Rf_{QCoh,*} B)`,
>
> `D⁺_QCoh` being read inside `D_QCoh` through the functor induced by the inclusion.

```lean
def derivedQuasicoherentPullbackSuccHomEquiv
    (A : (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
      (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).Localization)
    (Bq : (DerivedCategoryB.serreQuotientWPlus (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
      (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).Localization) :
    ((derivedQuasicoherentPullbackSucc B E h S hS f).obj A ⟶
        (DerivedCategoryB.serreQuotientPlusToSerreQuotient
          (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
          (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).obj Bq) ≃
      (A ⟶ (DerivedCategoryB.serreQuotientPlusToSerreQuotient
          (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
          (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).obj
        ((derivedPushforwardQuasicoherentPlusSucc B E h S hS f hqc hqs).obj Bq))
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSuccHomEquiv_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L381). The attribute's comment: “the third assertion: naturality of the adjointness in A”.

> Naturality of the adjointness of Stacks 07BE in `A`.

```lean
theorem derivedQuasicoherentPullbackSuccHomEquiv_naturality_left
    {A A' : (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
      (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).Localization} (e : A' ⟶ A)
    (Bq : (DerivedCategoryB.serreQuotientWPlus (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
      (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).Localization)
    (g : (derivedQuasicoherentPullbackSucc B E h S hS f).obj A ⟶
      (DerivedCategoryB.serreQuotientPlusToSerreQuotient
        (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).obj Bq) :
    derivedQuasicoherentPullbackSuccHomEquiv B E h S hS f hqc hqs A' Bq
        ((derivedQuasicoherentPullbackSucc B E h S hS f).map e ≫ g) =
      e ≫ derivedQuasicoherentPullbackSuccHomEquiv B E h S hS f hqc hqs A Bq g
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSuccHomEquiv_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L397). The attribute's comment: “the third assertion: naturality of the adjointness in B”.

> Naturality of the adjointness of Stacks 07BE in `B`.

```lean
theorem derivedQuasicoherentPullbackSuccHomEquiv_naturality_right
    (A : (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
      (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).Localization)
    {Bq Bq' : (DerivedCategoryB.serreQuotientWPlus (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
      (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).Localization} (k : Bq ⟶ Bq')
    (g : (derivedQuasicoherentPullbackSucc B E h S hS f).obj A ⟶
      (DerivedCategoryB.serreQuotientPlusToSerreQuotient
        (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).obj Bq) :
    derivedQuasicoherentPullbackSuccHomEquiv B E h S hS f hqc hqs A Bq'
        (g ≫ (DerivedCategoryB.serreQuotientPlusToSerreQuotient
          (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
          (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).map k) =
      derivedQuasicoherentPullbackSuccHomEquiv B E h S hS f hqc hqs A Bq g ≫
        (DerivedCategoryB.serreQuotientPlusToSerreQuotient
          (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
          (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).map
          ((derivedPushforwardQuasicoherentPlusSucc B E h S hS f hqc hqs).map k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 104.7, Tag 07BD](https://stacks.math.columbia.edu/tag/07BD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
