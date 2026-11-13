---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.derivedLocallyQuasicoherentFlatBaseChange_derivedFppfModulePullback, AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback, AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback_comp_ι, AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc, AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc_comp_ι, AlgebraicGeometry.Stack.FlatFppf.isLeftDerivable_derivedSheafFlatBaseChangePullbackSucc, AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSucc, AlgebraicGeometry.Stack.FlatFppf.isLeftDerivedFunctor_derivedQuasicoherentPullbackSucc
statement: formalized
proof: formalized
---

# 104.7 Derived pullback of quasi-coherent modules

Section 104.7 of the Stacks Project, [Tag 07BD](https://stacks.math.columbia.edu/tag/07BD). 1 tag here is carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07BE, a proposition

[Tag 07BE](https://stacks.math.columbia.edu/tag/07BE) in the Stacks Project.

**`AlgebraicGeometry.Stack.derivedLocallyQuasicoherentFlatBaseChange_derivedFppfModulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L261). The attribute's comment: “the first assertion, on objects: for a 1-morphism f of algebraic stacks the exact functor f^* : D(𝒪\_𝒴) ⥤ D(𝒪\_𝒳) carries D\_LQCoh^fbc(𝒪\_𝒴) into D\_LQCoh^fbc(𝒪\_𝒳), at module universe u, for any models of the derived categories”.

> **The first assertion of Stacks 07BE, on objects, at module universe `u`.**  Let
> `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks and let `K` be an object of
> `D_{LQCoh^fbc}(𝒪_𝒴)`.  Then `f^*K` is an object of `D_{LQCoh^fbc}(𝒪_𝒳)`.
>
> Since `f^*` is exact its cohomology modules are the inverse images of those of `K`, so the
> statement reduces degree by degree to the module-level **Stacks 0771** part (3) — that `f^*`
> maps `LQCoh^fbc(𝒪_𝒴)` into `LQCoh^fbc(𝒪_𝒳)` —, which is
> `AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_fppfModulesPullback`.

```lean
theorem derivedLocallyQuasicoherentFlatBaseChange_derivedFppfModulePullback
    (K : DerivedCategory (fppfModules B S hS 𝒴))
    (hK : derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴 K) :
    derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒳
      ((derivedFppfModulePullback B S hS f).obj K)
```

**`AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L279). The attribute's comment: “the first assertion: the functor D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_LQCoh^fbc(𝒪\_𝒳) induced by the exact functor f^*, at module universe u, for any models of the derived categories”.

> **The first assertion of Stacks 07BE at module universe `u`.**  The induced functor
> `f^* : D_{LQCoh^fbc}(𝒪_𝒴) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)`, the left vertical arrow of the square of the
> source.  Its composite with the inclusion of `D_{LQCoh^fbc}(𝒪_𝒳)` into `D(𝒪_𝒳)` is the
> composite of the inclusion of `D_{LQCoh^fbc}(𝒪_𝒴)` with `f^* : D(𝒪_𝒴) ⥤ D(𝒪_𝒳)`, which is the
> commutativity of the square; see
> `AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback_comp_ι`.

```lean
def derivedLocallyQuasicoherentPullback :
    (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴).FullSubcategory ⥤
      (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒳).FullSubcategory
```

**`AlgebraicGeometry.Stack.derivedLocallyQuasicoherentPullback_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullback.lean#L294). The attribute's comment: “the commutative square of the first assertion: the induced functor on D\_LQCoh^fbc followed by the inclusion into D(𝒪\_𝒳) is the inclusion into D(𝒪\_𝒴) followed by f^*, at module universe u, for any models of the derived categories”.

> **The square of Stacks 07BE at module universe `u`.**  Restricting `f^*` to the subcategories of
> complexes with locally quasi-coherent cohomology and flat base change and then including into
> `D(𝒪_𝒳)` is the same as including into `D(𝒪_𝒴)` and applying `f^*`.

```lean
theorem derivedLocallyQuasicoherentPullback_comp_ι :
    derivedLocallyQuasicoherentPullback B E hE S hS f ⋙
        (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒳).ι =
      (derivedLocallyQuasicoherentFlatBaseChange B E hE S hS 𝒴).ι ⋙
        derivedFppfModulePullback B S hS f
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L134). The attribute's comment: “the first assertion: the exact functor f^* induces D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_LQCoh^fbc(𝒪\_𝒳), with LQCoh^fbc the class of Stacks 0762 (flat base change for the pullback of sheaves), at module universe u + 1, for any models of the derived categories”.

> The functor `D_{LQCoh^fbc}(𝒪_𝒴) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)` induced by the exact functor
> `f^* : D(𝒪_𝒴) ⥤ D(𝒪_𝒳)`.

```lean
def derivedSheafFlatBaseChangePullbackSucc :
    (DerivedCategoryB.derivedCategoryB
        (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).FullSubcategory
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedSheafFlatBaseChangePullbackSucc_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L147). The attribute's comment: “the commutative square of the first assertion, at module universe u + 1, for the class of Stacks 0762 read with the pullback of sheaves, for any models of the derived categories”.

> The induced functor followed by the inclusion `D_{LQCoh^fbc}(𝒪_𝒳) ⊆ D(𝒪_𝒳)` is the inclusion
> `D_{LQCoh^fbc}(𝒪_𝒴) ⊆ D(𝒪_𝒴)` followed by `f^* : D(𝒪_𝒴) ⥤ D(𝒪_𝒳)`.

```lean
theorem derivedSheafFlatBaseChangePullbackSucc_comp_ι :
    derivedSheafFlatBaseChangePullbackSucc B E h S hS f ⋙
        (DerivedCategoryB.derivedCategoryB (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).ι =
      (DerivedCategoryB.derivedCategoryB (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).ι ⋙
        (modulePullbackSucc B S hS f).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.FlatFppf.isLeftDerivable_derivedSheafFlatBaseChangePullbackSucc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L207). The attribute's comment: “the second assertion: q\_𝒳 ∘ f^* : D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_QCoh(𝒪\_𝒳) is left derivable with respect to D\_LQCoh^fbc(𝒪\_𝒴) ⥤ D\_QCoh(𝒪\_𝒴) (Stacks 05SV), at module universe u + 1, for the class of Stacks 0762 read with the pullback of sheaves, at the standard models of the derived categories”.

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

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSucc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L220). The attribute's comment: “Lf^*\_QCoh : D\_QCoh(𝒪\_𝒴) ⥤ D\_QCoh(𝒪\_𝒳), the left derived functor of q\_𝒳 ∘ f^*, at module universe u + 1, at the standard models of the derived categories”.

> `Lf^*_QCoh : D_QCoh(𝒪_𝒴) ⥤ D_QCoh(𝒪_𝒳)`, the left derived functor of
> `q_𝒳 ∘ f^*` with respect to the quotient functor of `𝒴` (Stacks 05S9, 05SV).

```lean
def derivedQuasicoherentPullbackSucc :
    (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴)).Localization ⥤
      (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒳)).Localization
```

**`AlgebraicGeometry.Stack.FlatFppf.isLeftDerivedFunctor_derivedQuasicoherentPullbackSucc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L243). The attribute's comment: “Lf^*\_QCoh is the (total) left derived functor of q\_𝒳 ∘ f^*, with counit derivedQuasicoherentPullbackSuccCounit, at module universe u + 1”.

> `Lf^*_QCoh` is the left derived functor of `q_𝒳 ∘ f^*`.

```lean
instance isLeftDerivedFunctor_derivedQuasicoherentPullbackSucc :
    (derivedQuasicoherentPullbackSucc B E h S hS f).IsLeftDerivedFunctor
      (derivedQuasicoherentPullbackSuccCounit B E h S hS f)
      (DerivedCategoryB.serreQuotientW (sheafFlatBaseChangeModulesSucc B E h S hS 𝒴)
        (parasiticSheafFlatBaseChangeModulesSucc B E h S hS 𝒴))
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSuccHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L351). The attribute's comment: “the third assertion: for f quasi-compact and quasi-separated, Hom\_D\_QCoh(𝒪\_𝒳)(Lf^*\_QCoh A, B) = Hom\_D\_QCoh(𝒪\_𝒴)(A, Rf\_QCoh,* B) for A in D\_QCoh(𝒪\_𝒴) and B in D⁺\_QCoh(𝒪\_𝒳), at module universe u + 1, for the class of Stacks 0762 read with the pullback of sheaves, at the standard models of the derived categories”.

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

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSuccHomEquiv_naturality_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L381). The attribute's comment: “the third assertion: naturality of the adjointness in A”.

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

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentPullbackSuccHomEquiv_naturality_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentPullbackSheafFlatBaseChange.lean#L397). The attribute's comment: “the third assertion: naturality of the adjointness in B”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
