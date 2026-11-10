---
declaration: section
origin: cited
lean: Stacks.Cohomology.CompareTopologies.isWeakSerreClass_imageOfLE_of_vanishing, Stacks.Cohomology.CompareTopologies.derivedPullbackEquivalenceImageOfLE, Stacks.Cohomology.CompareTopologies.derivedPullbackEquivalenceImageOfLE_functor_comp_ι, Stacks.Cohomology.CompareTopologies.derivedPullbackEquivalenceImageOfLE_inverse_comp_ι, Stacks.Cohomology.CompareTopologies.derivedEquivalenceImageOfLE_spec, Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE, Stacks.Cohomology.CompareTopologies.isWeakSerreClass_imageOfLE, Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE_of_univLE
statement: formalized
proof: formalized
---

# 21.29 Comparing two topologies, II

Section 21.29 of the Stacks Project, [Tag 0F17](https://stacks.math.columbia.edu/tag/0F17). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07A8, a lemma

[Tag 07A8](https://stacks.math.columbia.edu/tag/07A8) in the Stacks Project.

**`Stacks.Cohomology.CompareTopologies.isWeakSerreClass_imageOfLE_of_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean#L286). The attribute's comment: “the weak Serre subcategory for the coarser topology, with the dévissage step discharged”.

> **[Stacks, Tag 07A8], first conclusion, with no hypothesis beyond the source's.** The image
> `A'` of `A` under `ε_*` is a weak Serre subcategory of `Mod(R_τ')`. This is
> `Stacks.Cohomology.CompareTopologies.isWeakSerreClass_imageOfLE` with its dévissage hypothesis
> `hdev` discharged by `exact_map_pushforward_of_vanishing`.

```lean
theorem isWeakSerreClass_imageOfLE_of_vanishing [A.IsWeakSerreClass] :
    (imageOfLE.{u, v, r, m} h R A).IsWeakSerreClass
```

**`Stacks.Cohomology.CompareTopologies.derivedPullbackEquivalenceImageOfLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean#L369). The attribute's comment: “the equivalence of derived categories given by ε^* and Rε_*”.

> **[Stacks, Tag 07A8], second conclusion.** Let `J' ≤ S.J` be two topologies on the category
> of a ringed site `S`, so that the identity functor of that category is the comparison morphism
> of ringed sites `ε : (C_τ, 𝒪_τ) ⟶ (C_τ', 𝒪_τ')`. Let `A` be a weak Serre subcategory of
> `Mod(𝒪_τ)` and let `B` be a set of objects such that every object has a `τ'`-covering by members
> of `B` and `H^p_τ(U, F)` vanishes for `U` in `B`, `p > 0` and `F` in `A`. Then derived pullback
> and derived pushforward are quasi-inverse equivalences of the unbounded derived categories
>
> `D_{A'}(𝒪_τ') ≌ D_A(𝒪_τ)`,
>
> where `A'` is the image class of the first conclusion,
> `Stacks.Cohomology.CompareTopologies.imageOfLE`.
>
> The five assumptions of [Stacks, Tag 0D7W] are discharged as described in the module docstring.
> Nothing is carried: the hypotheses above are exactly the source's own, the dévissage hypothesis
> `hdev` of `Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE` being proved rather than
> assumed, as `exact_map_pushforward_of_vanishing`.

```lean
def derivedPullbackEquivalenceImageOfLE
    [HasSheafify J' AddCommGrpCat.{u}] [J'.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [EnoughInjectives (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))]
    [EnoughInjectives (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf S.O).ofLE h))]
    [J'.HasSheafCompose (CategoryTheory.forget AddCommGrpCat.{u})]
    [A.IsWeakSerreClass] (B : Set S.C)
    (hB : ∀ U : S.C, ∃ 𝒰 : PreZeroHypercover.{u} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, B (𝒰.X i))
    (hvan : ∀ U : S.C, B U → ∀ p : ℕ, 0 < p →
      ∀ F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.O), A F →
      IsZero (Stacks.Cohomology.moduleCohomology
        (Stacks.SheafOfModules.Tensor.ringSheaf S.O) U p F)) :
    (DerivedCategoryB.derivedCategoryB
      (imageOfLE h (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A)).FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryB A).FullSubcategory
```

**`Stacks.Cohomology.CompareTopologies.derivedPullbackEquivalenceImageOfLE_functor_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean#L423). The attribute's comment: “the forward functor of the equivalence is the derived pullback”.

> **The equivalence of [Stacks, Tag 07A8] is given by `ε^*`**: its forward functor, followed by
> the inclusion of `D_A(𝒪_τ)` into `D(𝒪_τ)`, is the inclusion of `D_{A'}(𝒪_τ')` followed by the
> derived pullback `Lε^* = ε^*`.

```lean
theorem derivedPullbackEquivalenceImageOfLE_functor_comp_ι :
    letI : (pullbackOnHomotopy (S.coarseningHom h).toRingedToposSiteHom).HasLeftDerivedFunctor
        (HomotopyCategory.quasiIso
          (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (S.ofLe h).ringedTopos.O))
          (ComplexShape.up ℤ)) :=
      S.hasLeftDerivedFunctor_pullbackOnHomotopy_coarseningHom h
    (derivedPullbackEquivalenceImageOfLE S h A B hB hvan).functor ⋙
        (DerivedCategoryB.derivedCategoryB A).ι =
      (DerivedCategoryB.derivedCategoryB
        (imageOfLE h (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A)).ι ⋙
        derivedPullback (S.coarseningHom h).toRingedToposSiteHom
```

**`Stacks.Cohomology.CompareTopologies.derivedPullbackEquivalenceImageOfLE_inverse_comp_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CoarseningDerivedEquivalence.lean#L440). The attribute's comment: “the quasi-inverse of the equivalence is the derived pushforward”.

> **The quasi-inverse of the equivalence of [Stacks, Tag 07A8] is `Rε_*`**: it, followed by the
> inclusion of `D_{A'}(𝒪_τ')` into `D(𝒪_τ')`, is the inclusion of `D_A(𝒪_τ)` followed by the
> derived pushforward `Rε_*`.

```lean
theorem derivedPullbackEquivalenceImageOfLE_inverse_comp_ι :
    (derivedPullbackEquivalenceImageOfLE S h A B hB hvan).inverse ⋙
        (DerivedCategoryB.derivedCategoryB
          (imageOfLE h (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A)).ι =
      (DerivedCategoryB.derivedCategoryB A).ι ⋙
        derivedPushforward (S.coarseningHom h).toRingedToposSiteHom
```

**`Stacks.Cohomology.CompareTopologies.derivedEquivalenceImageOfLE_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedWeakSerreAcrossTopologies.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedWeakSerreAcrossTopologies.lean#L442). The attribute's comment: “second conclusion: the equivalence of triangulated categories `D_A(𝒪_τ) ≌ D_{A'}(𝒪_τ')` given by `ε^*` and `Rε_*`”.

> **Stacks 07A8, second conclusion.**  Under the hypotheses of
> `Stacks.Cohomology.CompareTopologies.derivedEquivalenceImageOfLE`, that equivalence
> `D_A(𝒪_τ) ≌ D_{A'}(𝒪_τ')`, where `A' = ε_*A`, is an equivalence of triangulated categories, and it
> is given by `ε^*` and `Rε_*`:
>
> * it is a triangulated equivalence, for the shift structure of `Lε^*` on its quasi-inverse and the
>   compatible one on its functor;
> * its functor, read in `D(𝒪_τ')`, is the derived pushforward `Rε_*`;
> * its quasi-inverse, read in `D(𝒪_τ)`, is the derived pullback `Lε^*`, compatibly with the shift;
> * since `ε^*` is exact, that quasi-inverse is `ε^*` applied termwise to complexes.
>
> That `A'` is a weak Serre subcategory of `Mod(𝒪_τ')`, which is what makes `D_{A'}(𝒪_τ')` a
> triangulated subcategory of `D(𝒪_τ')`, is the first conclusion,
> `Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE_of_univLE`.

```lean
theorem derivedEquivalenceImageOfLE_spec :
    haveI : (DerivedCategoryB.derivedCategoryB
        (imageOfLE.{u, u, u, u} h (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A)).IsTriangulated :=
      DerivedCategoryB.derivedCategoryB_isTriangulated _ (isWeakSerre_imageOfLE_of_univLE h
        (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A (WeakSerre.isWeakSerre_of_isWeakSerreClass A)
        B hB hvan)
    letI := (S.coarseningHom h).toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
      (S.coarseningHom h).isMorphismOfSites_toRingedToposSiteHom
      (S.isFlatMapULift_fSharp_auxHomH_coarseningHom h)
    letI := (S.coarseningHom h).toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
    letI := Functor.additive_of_preserves_binary_products
      (S.coarseningHom h).toRingedToposSiteHom.pullbackTopos
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact
      (S.coarseningHom h).toRingedToposSiteHom
    letI := derivedPullbackRestrictionCommShift S h A B hB hvan
    letI := derivedEquivalenceImageOfLEInverseCommShift S h A B hB hvan
    letI := (derivedEquivalenceImageOfLE S h A B hB hvan).commShiftFunctor ℤ
    haveI := (derivedEquivalenceImageOfLE S h A B hB hvan).commShift_of_inverse ℤ
    (derivedEquivalenceImageOfLE S h A B hB hvan).IsTriangulated ∧
      (derivedEquivalenceImageOfLE S h A B hB hvan).functor ⋙
          (DerivedCategoryB.derivedCategoryB
            (imageOfLE.{u, u, u, u} h (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A)).ι =
        (DerivedCategoryB.derivedCategoryB A).ι ⋙
          derivedPushforward.{u} (S.coarseningHom h).toRingedToposSiteHom ∧
      ∃ e : (derivedEquivalenceImageOfLE S h A B hB hvan).inverse ⋙
          (DerivedCategoryB.derivedCategoryB A).ι =
        (DerivedCategoryB.derivedCategoryB
            (imageOfLE.{u, u, u, u} h (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A)).ι ⋙
          derivedPullback.{u} (S.coarseningHom h).toRingedToposSiteHom,
        NatTrans.CommShift (eqToIso e).hom ℤ ∧
      Nonempty ((derivedEquivalenceImageOfLE S h A B hB hvan).inverse ⋙
          (DerivedCategoryB.derivedCategoryB A).ι ≅
        (DerivedCategoryB.derivedCategoryB
            (imageOfLE.{u, u, u, u} h (Stacks.SheafOfModules.Tensor.ringSheaf S.O) A)).ι ⋙
          (S.coarseningHom h).toRingedToposSiteHom.pullbackTopos.mapDerivedCategory)
```

**`Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologies.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologies.lean#L284). The attribute's comment: “the weak Serre subcategory for the coarser topology”.

> Let `J' ≤ J` be two topologies on `C` and let `R` be a sheaf of rings for the finer topology
> `J`, so that the identity functor of `C` is the comparison morphism of ringed sites
> `ε : (C_τ, R_τ) ⟶ (C_τ', R_τ')`. Let `A` be a class of sheaves of `R`-modules for `J` — the
> source's assumption (1), that every object of `A` is a sheaf for the finer topology, is this — and
> let `B` be a set of objects of `C`. Assume
>
> 1. `A` is a weak Serre subcategory of `Mod(R_τ)`,
> 2. every object of `C` has a `J'`-covering whose members lie in `B`,
> 3. for every `U` in `B` the cohomology `H^p_τ(U, F)` vanishes for `p > 0` and `F` in `A`.
>
> Then the image `A'` of `A` under `ε_*` is a weak Serre subcategory of `Mod(R_τ')`.
>
> The hypothesis `hdev` is the step of the source's proof that assumptions (2) and (3) above force
> `ε_*` to carry an exact short complex with terms in `A` to an exact short complex. In the source
> that step is Stacks 072W, identifying `R^pε_*` with the sheafification of `U ↦ H^p_τ(U, F)`,
> followed by a dévissage.

```lean
theorem isWeakSerre_imageOfLE [HasSheafify J' AddCommGrpCat.{m}]
    [J'.WEqualsLocallyBijective AddCommGrpCat.{m}]
    [EnoughInjectives (_root_.SheafOfModules.{m} R)]
    (hA : WeakSerre.IsWeakSerre A) (B : Set C)
    (hB : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, B (𝒰.X i))
    (hvan : ∀ U : C, B U → ∀ p : ℕ, 0 < p → ∀ F : _root_.SheafOfModules.{m} R, A F →
      IsZero (Stacks.Cohomology.moduleCohomology R U p F))
    (hdev : (∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, B (𝒰.X i)) →
      (∀ U : C, B U → ∀ p : ℕ, 0 < p → ∀ F : _root_.SheafOfModules.{m} R, A F →
        IsZero (Stacks.Cohomology.moduleCohomology R U p F)) →
      ∀ S : ShortComplex (_root_.SheafOfModules.{m} R), S.Exact →
        A S.X₁ → A S.X₂ → A S.X₃ → (S.map (pushforward.{u, v, r, m} h R)).Exact) :
    WeakSerre.IsWeakSerre (imageOfLE.{u, v, r, m} h R A)
```

**`Stacks.Cohomology.CompareTopologies.isWeakSerreClass_imageOfLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologies.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologies.lean#L373). The attribute's comment: “the same conclusion in the closure form of Stacks 0754”.

> The same statement as `Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE`, with the
> conclusion phrased in the closure form `CategoryTheory.ObjectProperty.IsWeakSerreClass` of
> Stacks 0754.

```lean
theorem isWeakSerreClass_imageOfLE [HasSheafify J' AddCommGrpCat.{m}]
    [J'.WEqualsLocallyBijective AddCommGrpCat.{m}]
    [EnoughInjectives (_root_.SheafOfModules.{m} R)]
    (hA : WeakSerre.IsWeakSerre A) (B : Set C)
    (hB : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, B (𝒰.X i))
    (hvan : ∀ U : C, B U → ∀ p : ℕ, 0 < p → ∀ F : _root_.SheafOfModules.{m} R, A F →
      IsZero (Stacks.Cohomology.moduleCohomology R U p F))
    (hdev : (∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, B (𝒰.X i)) →
      (∀ U : C, B U → ∀ p : ℕ, 0 < p → ∀ F : _root_.SheafOfModules.{m} R, A F →
        IsZero (Stacks.Cohomology.moduleCohomology R U p F)) →
      ∀ S : ShortComplex (_root_.SheafOfModules.{m} R), S.Exact →
        A S.X₁ → A S.X₂ → A S.X₃ → (S.map (pushforward.{u, v, r, m} h R)).Exact) :
    (imageOfLE.{u, v, r, m} h R A).IsWeakSerreClass
```

**`Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE_of_univLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologiesOfVanishing.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologiesOfVanishing.lean#L191). The attribute's comment: “first conclusion: the image of `A` is a weak Serre subcategory of `Mod(𝒪_τ')`”.

> **Stacks 07A8, first conclusion.**  Let `J' ≤ J` be two topologies on `C` and let `R` be a
> sheaf of rings for the finer topology `J`, so that the identity functor of `C` is the comparison
> morphism of ringed sites `ε : (C_τ, R_τ) ⟶ (C_τ', R_τ')`.  Let `A` be a class of sheaves of
> `R`-modules for `J` — the source's assumption (1), that every object of `A` is a sheaf for the
> finer topology, is this — and let `B` be a set of objects of `C`.  Assume
>
> 1. `A` is a weak Serre subcategory of `Mod(R_τ)`,
> 2. every object of `C` has a `J'`-covering whose members lie in `B`,
> 3. for every `U` in `B` the cohomology `H^p_τ(U, F)` vanishes for `p > 0` and `F` in `A`.
>
> Then the image `A'` of `A` under `ε_*` is a weak Serre subcategory of `Mod(R_τ')`.
>
> The modules live in a universe containing those of the objects and morphisms of `C` and of the
> rings; in it sheafification exists for both topologies, inverts exactly the locally bijective
> morphisms, and sheaves of `R`-modules have enough injectives, so that `H^p_τ(U, -)` is defined.
> Assumptions 2 and 3 enter through
> `Stacks.Cohomology.CompareTopologies.exact_map_pushforward_of_prop`, which proves from them that
> `ε_*` carries an exact short complex with terms in `A` to an exact short complex.

```lean
theorem isWeakSerre_imageOfLE_of_univLE (hA : WeakSerre.IsWeakSerre A) (B : Set C)
    (hB : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, B (𝒰.X i))
    (hvan : ∀ U : C, B U → ∀ p : ℕ, 0 < p → ∀ F : _root_.SheafOfModules.{m} R, A F →
      IsZero (Stacks.Cohomology.moduleCohomology R U p F)) :
    WeakSerre.IsWeakSerre (imageOfLE.{u, v, r, m} h R A)
```

**`Stacks.Cohomology.CompareTopologies.isWeakSerreClass_imageOfLE_of_univLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologiesOfVanishing.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/WeakSerreAcrossTopologiesOfVanishing.lean#L204). The attribute's comment: “first conclusion, in the closure form of Stacks 0754”.

> **Stacks 07A8, first conclusion, in the closure form of Stacks 0754.**  The same statement as
> `Stacks.Cohomology.CompareTopologies.isWeakSerre_imageOfLE_of_univLE`, with the conclusion
> phrased as `CategoryTheory.ObjectProperty.IsWeakSerreClass`, the form in which the derived
> category results consume it.

```lean
theorem isWeakSerreClass_imageOfLE_of_univLE (hA : WeakSerre.IsWeakSerre A) (B : Set C)
    (hB : ∀ U : C, ∃ 𝒰 : PreZeroHypercover.{max u v} U, 𝒰.sieve₀ ∈ J' U ∧ ∀ i, B (𝒰.X i))
    (hvan : ∀ U : C, B U → ∀ p : ℕ, 0 < p → ∀ F : _root_.SheafOfModules.{m} R, A F →
      IsZero (Stacks.Cohomology.moduleCohomology R U p F)) :
    (imageOfLE.{u, v, r, m} h R A).IsWeakSerreClass
```

## Tag 0F18, a lemma

[Tag 0F18](https://stacks.math.columbia.edu/tag/0F18) in the Stacks Project.

**`Stacks.Cohomology.MayerVietoris.essImage_iff_forall_isCSquareIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DescentForAFamilyOfSquares.lean, line 1171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DescentForAFamilyOfSquares.lean#L1171).

> **Stacks 0F18.** Let `C` carry two Grothendieck topologies `J' ≤ J` and let `𝒪` be a sheaf of
> rings for `J`, so that the identity of `C` is a comparison of ringed sites
> `ε : (C_J, 𝒪_J) ⟶ (C_{J'}, 𝒪_{J'})`. Let `A` be a type and for each `α : A` let
>
> ```
> E α ⟶ Y α
>   ↓      ↓
> Z α ⟶ X α
> ```
>
> be a commutative square in `C`. Assume
>
> 1. a `J'`-sheaf of sets `F'` is a `J`-sheaf whenever
>    `F'(X α) = F'(Z α) ×_{F'(E α)} F'(Y α)` for all `α`, and
> 2. for every `K'` in `D(𝒪_{J'})` in the essential image of `Rε_*` the canonical comparison maps
>    `c^{K'}_{X α, Z α, Y α, E α}` of [Stacks, Tag 0F16] are isomorphisms for all `α`.
>
> Then an object `K'` of `D⁺(𝒪_{J'})` lies in the essential image of `Rε_*` if and only if the
> maps `c^{K'}_{X α, Z α, Y α, E α}` are isomorphisms for all `α`.
>
> `Rε_*` is any right derived functor of `ε_*` together with its unit; the hypothesis that it is a
> right derived functor is what makes the essential image independent of the choice.

```lean
theorem essImage_iff_forall_isCSquareIso {A : Type*} (sq : A → Square S.C)
    (hdetect : ∀ F : Sheaf J' (Type max u w),
      (∀ a, ((sq a).op.map F.obj).IsPullback) → Presheaf.IsSheaf S.J F.obj)
    (Rε : DerivedCategory (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) ⥤
      DerivedCategory (SheafOfModules.{v} (ringSheafOfLe h
          (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (η : letI := modulePushforward_additive.{u, v, w, r} h
            (Stacks.SheafOfModules.Tensor.ringSheaf S.O);
      (modulePushforward.{u, v, w, r} h
          (Stacks.SheafOfModules.Tensor.ringSheaf S.O)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rε)
    [Rε.IsRightDerivedFunctor η
      (HomotopyCategory.quasiIso (SheafOfModules.{v}
          (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) (ComplexShape.up ℤ))]
    (hcomparison : ∀ K' : DerivedCategory (SheafOfModules.{v} (ringSheafOfLe h
        (Stacks.SheafOfModules.Tensor.ringSheaf S.O))),
      Rε.essImage K' → ∀ a, (CanonicalMapOfComplexes.derivedCSquareData.{u, v}
        (R := (Stacks.SheafOfModules.Tensor.ringSheaf (S.ofLe h).O)) (sq a)).IsCSquareIso K')
    (K' : DerivedCategory (SheafOfModules.{v} (ringSheafOfLe h
        (Stacks.SheafOfModules.Tensor.ringSheaf S.O))))
    (hplus : (DerivedCategory.TStructure.t
      (C := SheafOfModules.{v} (ringSheafOfLe h
          (Stacks.SheafOfModules.Tensor.ringSheaf S.O)))).plus K') :
    Rε.essImage K' ↔ ∀ a, (CanonicalMapOfComplexes.derivedCSquareData.{u, v}
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (S.ofLe h).O)) (sq a)).IsCSquareIso K'
```

## Tag 0F19, a lemma

[Tag 0F19](https://stacks.math.columbia.edu/tag/0F19) in the Stacks Project.

**`Stacks.Cohomology.MayerVietoris.isCSquareIso_ofLe_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DescentForACoarserTopology.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietoris/DescentForACoarserTopology.lean#L151).

> **Stacks 0F19.** Let `J' ≤ J` be two topologies on `C` and let `𝒪` be a sheaf of rings for
> `J`, so that the identity of `C` is a comparison `ε : (C_J, 𝒪_J) ⟶ (C_{J'}, 𝒪_{J'})`. Let a
> commutative square in `C` be given whose `J`-sheafified representables form a pushout square and
> whose map `h_E^# ⟶ h_Y^#` is a monomorphism. Then for every object `K'` of `D(𝒪_{J'})` in the
> essential image of the derived direct image `Rε_*`, the canonical map `c^{K'}_{X,Z,Y,E}` of
> Stacks 0F16 for the coarser topology is an isomorphism.

```lean
theorem isCSquareIso_ofLe_of_isPushout (sq : Square S.C)
    (hpushout : (sq.map (Sheaf.sheafifiedYoneda S.J)).IsPushout)
    (hmono : Mono ((Sheaf.sheafifiedYoneda S.J).map sq.f₁₂))
    (Rε : DerivedCategory (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O)) ⥤
      DerivedCategory (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf (S.ofLe h).O)))
    (η : letI := (modulePushforward_additive.{u, v, w, r} h
        (Stacks.SheafOfModules.Tensor.ringSheaf S.O));
      (modulePushforward.{u, v, w, r} h
        (Stacks.SheafOfModules.Tensor.ringSheaf S.O)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rε)
    [Rε.IsRightDerivedFunctor η
      (HomotopyCategory.quasiIso (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf S.O))
        (ComplexShape.up ℤ))]
    (K' : DerivedCategory
      (SheafOfModules.{v} (Stacks.SheafOfModules.Tensor.ringSheaf (S.ofLe h).O)))
    (hK' : Rε.essImage K') :
    (CanonicalMapOfComplexes.derivedCSquareData.{u, v}
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf (S.ofLe h).O)) sq).IsCSquareIso K'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.29, Tag 0F17](https://stacks.math.columbia.edu/tag/0F17)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
