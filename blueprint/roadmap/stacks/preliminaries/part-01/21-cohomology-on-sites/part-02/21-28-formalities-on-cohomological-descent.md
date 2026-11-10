---
declaration: section
origin: cited
lean: CategoryTheory.Adjunction.unitIsIso, CategoryTheory.Adjunction.isClosedUnderIsomorphisms_unitIsIso, CategoryTheory.Adjunction.unitIsIso_isSaturated, CategoryTheory.Adjunction.fullyFaithfulιCompLeftAdjoint, CategoryTheory.Adjunction.unitIsIso_isTriangulated, Stacks.Cohomology.CohomologicalDescent.unitIsIso_saturated_triangulated_fullyFaithful, CategoryTheory.Adjunction.counitIsIso, CategoryTheory.Adjunction.isClosedUnderIsomorphisms_counitIsIso
statement: formalized
proof: formalized
---

# 21.28 Formalities on cohomological descent

Section 21.28 of the Stacks Project, [Tag 0D7N](https://stacks.math.columbia.edu/tag/0D7N). 7 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D7Q, a lemma

[Tag 0D7Q](https://stacks.math.columbia.edu/tag/0D7Q) in the Stacks Project.

**`CategoryTheory.Adjunction.unitIsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L89). The attribute's comment: “variant: the subcategory of objects at which the unit is invertible, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.unitIsIso_saturated_triangulated_fullyFaithful”.

> The objects `K` of the source of the left adjoint of an adjunction `F ⊣ G` at which the
> unit `K ⟶ G (F K)` is invertible.

```lean
def unitIsIso : ObjectProperty C
```

**`CategoryTheory.Adjunction.isClosedUnderIsomorphisms_unitIsIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L133). The attribute's comment: “variant: the unit subcategory is strictly full, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.unitIsIso_saturated_triangulated_fullyFaithful”.

> **The unit subcategory is strictly full**: it is closed under isomorphisms, by naturality
> of the unit.

```lean
lemma isClosedUnderIsomorphisms_unitIsIso : adj.unitIsIso.IsClosedUnderIsomorphisms
```

**`CategoryTheory.Adjunction.unitIsIso_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L149). The attribute's comment: “variant: the unit subcategory is saturated, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.unitIsIso_saturated_triangulated_fullyFaithful”.

> **The unit subcategory is saturated**: a direct summand of an object at which the unit is
> invertible is again such an object.

```lean
instance unitIsIso_isSaturated [HasZeroMorphisms C] : adj.unitIsIso.IsSaturated
```

**`CategoryTheory.Adjunction.fullyFaithfulιCompLeftAdjoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L166). The attribute's comment: “variant: the left adjoint is fully faithful on the unit subcategory, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.unitIsIso_saturated_triangulated_fullyFaithful”.

> **The left adjoint is fully faithful on the unit subcategory.** The preimage of
> `g : F K ⟶ F L` is the morphism `K ⟶ G (F L)` adjoint to `g`, followed by the inverse of the
> unit at `L`.

```lean
noncomputable def fullyFaithfulιCompLeftAdjoint : (adj.unitIsIso.ι ⋙ F).FullyFaithful
```

**`CategoryTheory.Adjunction.unitIsIso_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L256). The attribute's comment: “variant: the unit subcategory is triangulated, for a triangulated adjunction, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.unitIsIso_saturated_triangulated_fullyFaithful”.

> **The unit subcategory is triangulated**: it contains the zero object, is stable under the
> shift because the unit commutes with it, and passes from two vertices of a distinguished
> triangle to the third by the five lemma for triangles.

```lean
instance unitIsIso_isTriangulated : adj.unitIsIso.IsTriangulated
```

**`Stacks.Cohomology.CohomologicalDescent.unitIsIso_saturated_triangulated_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphismsOfToposHom.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphismsOfToposHom.lean#L105).

> **The subcategory of `D(O_D)` on which the unit of `Lf^* ⊣ Rf_*` is invertible.** For a
> morphism of ringed topoi `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)`, the full subcategory `D'` of
> `D(O_D)` of the objects `K` such that the unit `K ⟶ Rf_* Lf^* K` is an isomorphism is strictly
> full (closed under isomorphisms), saturated and triangulated, and `Lf^* : D' ⥤ D(O_C)` is full
> and faithful.

```lean
theorem unitIsIso_saturated_triangulated_fullyFaithful :
    (derivedAdjunction f).unitIsIso.IsClosedUnderIsomorphisms ∧
      (derivedAdjunction f).unitIsIso.IsSaturated ∧
      (derivedAdjunction f).unitIsIso.IsTriangulated ∧
      ((derivedAdjunction f).unitIsIso.ι ⋙ derivedPullback f).Full ∧
      ((derivedAdjunction f).unitIsIso.ι ⋙ derivedPullback f).Faithful
```

## Tag 0D7R, a lemma

[Tag 0D7R](https://stacks.math.columbia.edu/tag/0D7R) in the Stacks Project.

**`CategoryTheory.Adjunction.counitIsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L96). The attribute's comment: “variant: the subcategory of objects at which the counit is invertible, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.counitIsIso_saturated_triangulated_fullyFaithful”.

> The objects `K` of the source of the right adjoint of an adjunction `F ⊣ G` at which the
> counit `F (G K) ⟶ K` is invertible.

```lean
def counitIsIso : ObjectProperty D
```

**`CategoryTheory.Adjunction.isClosedUnderIsomorphisms_counitIsIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L141). The attribute's comment: “variant: the counit subcategory is strictly full, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.counitIsIso_saturated_triangulated_fullyFaithful”.

> **The counit subcategory is strictly full**: it is closed under isomorphisms, by naturality
> of the counit.

```lean
lemma isClosedUnderIsomorphisms_counitIsIso : adj.counitIsIso.IsClosedUnderIsomorphisms
```

**`CategoryTheory.Adjunction.counitIsIso_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L157). The attribute's comment: “variant: the counit subcategory is saturated, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.counitIsIso_saturated_triangulated_fullyFaithful”.

> **The counit subcategory is saturated**: a direct summand of an object at which the counit
> is invertible is again such an object.

```lean
instance counitIsIso_isSaturated [HasZeroMorphisms D] : adj.counitIsIso.IsSaturated
```

**`CategoryTheory.Adjunction.fullyFaithfulιCompRightAdjoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L191). The attribute's comment: “variant: the right adjoint is fully faithful on the counit subcategory, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.counitIsIso_saturated_triangulated_fullyFaithful”. References: SGA 4 I (6.4), “more general”.

> **The right adjoint is fully faithful on the counit subcategory.** The preimage of
> `g : G A ⟶ G B` is the inverse of the counit at `A`, followed by the morphism `F (G A) ⟶ B`
> adjoint to `g`.

```lean
noncomputable def fullyFaithfulιCompRightAdjoint : (adj.counitIsIso.ι ⋙ G).FullyFaithful
```

**`CategoryTheory.Adjunction.counitIsIso_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphisms.lean#L263). The attribute's comment: “variant: the counit subcategory is triangulated, for a triangulated adjunction, for an arbitrary adjunction F ⊣ G; the tag, for the derived adjunction Lf^* ⊣ Rf_* of a morphism of ringed topoi, is Stacks.Cohomology.CohomologicalDescent.counitIsIso_saturated_triangulated_fullyFaithful”.

> **The counit subcategory is triangulated.**

```lean
instance counitIsIso_isTriangulated : adj.counitIsIso.IsTriangulated
```

**`Stacks.Cohomology.CohomologicalDescent.counitIsIso_saturated_triangulated_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphismsOfToposHom.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnitAndCounitIsomorphismsOfToposHom.lean#L121).

> **The subcategory of `D(O_C)` on which the counit of `Lf^* ⊣ Rf_*` is invertible.** For a
> morphism of ringed topoi `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)`, the full subcategory `D'` of
> `D(O_C)` of the objects `K` such that the counit `Lf^* Rf_* K ⟶ K` is an isomorphism is strictly
> full (closed under isomorphisms), saturated and triangulated, and `Rf_* : D' ⥤ D(O_D)` is full
> and faithful.

```lean
theorem counitIsIso_saturated_triangulated_fullyFaithful :
    (derivedAdjunction f).counitIsIso.IsClosedUnderIsomorphisms ∧
      (derivedAdjunction f).counitIsIso.IsSaturated ∧
      (derivedAdjunction f).counitIsIso.IsTriangulated ∧
      ((derivedAdjunction f).counitIsIso.ι ⋙ derivedPushforward (X := X) (Y := Y) f).Full ∧
      ((derivedAdjunction f).counitIsIso.ι ⋙ derivedPushforward (X := X) (Y := Y) f).Faithful
```

## Tag 0D7S, a lemma

[Tag 0D7S](https://stacks.math.columbia.edu/tag/0D7S) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.isIso_derivedCounit_app_of_isIso_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowDescent.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowDescent.lean#L242).

> **Stacks 0D7S.** Let `f` be a flat morphism of ringed topoi and let `K` be a bounded below
> object of `D(O_X)`. If the counit `Lf^*Rf_*H^q(K) ⟶ H^q(K)` of the derived adjunction is an
> isomorphism for every `q`, with each cohomology object placed in degree zero, then the counit
> `Lf^*Rf_*K ⟶ K` is an isomorphism.
>
> This is the previous statement with the pair of functors reversed: here it is
> `(Rf_* ⋙ Lf^*, 𝟭)`, and the theorem applied at the counit.

```lean
theorem isIso_derivedCounit_app_of_isIso_homology :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    ∀ (K : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
      DerivedCategory.TStructure.t.plus K →
      (∀ q : ℤ, IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).counit.app
        ((DerivedCategory.singleFunctor
            (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
          ((DerivedCategory.homologyFunctor
            (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) q).obj K)))) →
      IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).counit.app K)
```

## Tag 0D7T, a lemma

[Tag 0D7T](https://stacks.math.columbia.edu/tag/0D7T) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.isIso_derivedUnit_app_of_isIso_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowDescent.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowDescent.lean#L212).

> **Stacks 0D7T.** Let `f` be a flat morphism of ringed topoi and let `K` be a bounded below
> object of `D(O_Y)`. If the unit `H^q(K) ⟶ Rf_*Lf^*H^q(K)` of the derived adjunction is an
> isomorphism for every `q`, with each cohomology object placed in degree zero, then the unit
> `K ⟶ Rf_*Lf^*K` is an isomorphism.
>
> The pair of functors is `(𝟭, Lf^* ⋙ Rf_*)`: both are exact, both commute with the shift, and
> both carry `D^{≥m}` into `D^{≥m}`, so this is
> `CategoryTheory.NatTrans.isIso_app_of_isGE` at the unit.

```lean
theorem isIso_derivedUnit_app_of_isIso_homology :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    ∀ (K : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))),
      DerivedCategory.TStructure.t.plus K →
      (∀ q : ℤ, IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
        ((DerivedCategory.singleFunctor
            (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj
          ((DerivedCategory.homologyFunctor
            (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) q).obj K)))) →
      IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app K)
```

## Tag 0D7U, a lemma

[Tag 0D7U](https://stacks.math.columbia.edu/tag/0D7U) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.derivedCategoryBPlus_derivedPullback_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean#L307). The attribute's comment: “derived pullback”.

> **Stacks 0D7U**, the assertion that derived pullback restricts. Let `f` be a flat morphism of
> ringed topoi and let `𝒜 ⊂ Mod(𝒪)`, `𝒜' ⊂ Mod(𝒪')` be weak Serre subcategories with
> `f^*𝒜' ⊂ 𝒜`. Then `Lf^*` carries `D⁺_{𝒜'}(𝒪')` into `D⁺_𝒜(𝒪)`.

```lean
theorem derivedCategoryBPlus_derivedPullback_obj :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    ∀ (K : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))),
      DerivedCategoryB.derivedCategoryBPlus A' K →
        DerivedCategoryB.derivedCategoryBPlus A ((derivedPullback f).obj K)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedCategoryBPlus_derivedPushforward_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean#L328). The attribute's comment: “derived pushforward”.

> **Stacks 0D7U**, the assertion that derived pushforward restricts. Under the hypotheses of the
> source — `f` flat, `f^*` inducing an equivalence `𝒜' ⟶ 𝒜`, and the unit `ℱ' ⟶ Rf_*f^*ℱ'`
> invertible on `𝒜'` — the pushforward `Rf_*` carries `D⁺_𝒜(𝒪)` into `D⁺_{𝒜'}(𝒪')`.

```lean
theorem derivedCategoryBPlus_derivedPushforward_obj :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    (∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) →
      ∀ (K : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
        DerivedCategoryB.derivedCategoryBPlus A K →
          DerivedCategoryB.derivedCategoryBPlus A' ((derivedPushforward f).obj K)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean#L351). The attribute's comment: “equivalence”.

> **Stacks 0D7U.** For a flat morphism of ringed topoi `f` and weak Serre subcategories
> `𝒜 ⊂ Mod(𝒪)`, `𝒜' ⊂ Mod(𝒪')` such that `f^*` induces an equivalence `𝒜' ⟶ 𝒜` and the unit
> `ℱ' ⟶ Rf_*f^*ℱ'` is invertible for every `ℱ'` of `𝒜'`, the derived pullback is an **equivalence**
> `D⁺_{𝒜'}(𝒪') ≌ D⁺_𝒜(𝒪)`.
>
> The hypothesis on the unit propagates from `𝒜'` to all of `D⁺_{𝒜'}(𝒪')` by Tag 0D7T, and the
> corresponding statement for the counit from `𝒜` to all of `D⁺_𝒜(𝒪)` by Tag 0D7S.

```lean
noncomputable def derivedPullbackEquivalence
    (hUnit :
      letI := f.pullbackTopos_preservesFiniteLimits hmos hf
      letI := f.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
      ∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    (DerivedCategoryB.derivedCategoryBPlus A').FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryBPlus A).FullSubcategory
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalence_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean#L374). The attribute's comment: “forward functor”.

> **Stacks 0D7U**, the identification of the forward functor of the equivalence with the
> restriction of the derived pullback.

```lean
theorem derivedPullbackEquivalence_functor
    (hUnit :
      letI := f.pullbackTopos_preservesFiniteLimits hmos hf
      letI := f.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
      ∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    (derivedPullbackEquivalence f A A' hmos hf hA hEquiv hUnit).functor =
      (DerivedCategoryB.derivedCategoryBPlus A).lift
        ((DerivedCategoryB.derivedCategoryBPlus A').ι ⋙ derivedPullback f)
        (fun K ↦ derivedCategoryBPlus_derivedPullback_obj f A A' hmos hf hA K.obj K.property)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalence_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/BoundedBelowEquivalence.lean#L394). The attribute's comment: “quasi-inverse”.

> **Stacks 0D7U**, the identification of the quasi-inverse of the equivalence with the
> restriction of the derived pushforward.

```lean
theorem derivedPullbackEquivalence_inverse
    (hUnit :
      letI := f.pullbackTopos_preservesFiniteLimits hmos hf
      letI := f.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
      ∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    (derivedPullbackEquivalence f A A' hmos hf hA hEquiv hUnit).inverse =
      (DerivedCategoryB.derivedCategoryBPlus A').lift
        ((DerivedCategoryB.derivedCategoryBPlus A).ι ⋙ derivedPushforward f)
        (fun K ↦ derivedCategoryBPlus_derivedPushforward_obj f A A' hmos hf hA hEquiv hUnit
          K.obj K.property)
```

## Tag 0D7V, a lemma

[Tag 0D7V](https://stacks.math.columbia.edu/tag/0D7V) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.derivedCategoryB_derivedPullback_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean#L512). The attribute's comment: “derived pullback”.

> **Stacks 0D7V**, the assertion that derived pullback restricts. Let `f` be a flat morphism of
> ringed topoi and let `𝒜 ⊂ Mod(𝒪)`, `𝒜' ⊂ Mod(𝒪')` be weak Serre subcategories with
> `f^*𝒜' ⊂ 𝒜`. Then `Lf^*` carries `D_{𝒜'}(𝒪')` into `D_𝒜(𝒪)`.

```lean
theorem derivedCategoryB_derivedPullback_obj :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    ∀ (K : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))),
      DerivedCategoryB.derivedCategoryB A' K →
        DerivedCategoryB.derivedCategoryB A ((derivedPullback f).obj K)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedCategoryB_derivedPushforward_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean#L530). The attribute's comment: “derived pushforward”.

> **Stacks 0D7V**, the assertion that derived pushforward restricts. Under the hypotheses of the
> source — `f` flat, `f^*` inducing an equivalence `𝒜' ⟶ 𝒜`, the unit `ℱ' ⟶ Rf_*f^*ℱ'` invertible
> on `𝒜'`, and both sites satisfying the Olsson--Laszlo hypothesis of Tag 0D6R — the pushforward
> `Rf_*` carries `D_𝒜(𝒪)` into `D_{𝒜'}(𝒪')`.

```lean
theorem derivedCategoryB_derivedPushforward_obj :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    (∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
      ((DerivedCategory.singleFunctor (SheafOfModules.{w}
          (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) →
      ∀ (K : DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
        DerivedCategoryB.derivedCategoryB A K →
          DerivedCategoryB.derivedCategoryB A' ((derivedPushforward f).obj K)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalenceUnbounded`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean#L564). The attribute's comment: “equivalence”.

> **Stacks 0D7V.** Let `f : (Sh(C), 𝒪) ⟶ (Sh(C'), 𝒪')` be a flat morphism of ringed topoi and
> let `𝒜 ⊂ Mod(𝒪)`, `𝒜' ⊂ Mod(𝒪')` be weak Serre subcategories such that `f^*` induces an
> equivalence `𝒜' ⟶ 𝒜` and the unit `ℱ' ⟶ Rf_*f^*ℱ'` is invertible for every `ℱ'` of `𝒜'`, and
> assume that `C, 𝒪, 𝒜` and `C', 𝒪', 𝒜'` both satisfy the standing hypothesis of Tag 0D6R. Then
> the derived pullback is an **equivalence** `D_{𝒜'}(𝒪') ≌ D_𝒜(𝒪)`.
>
> The hypothesis on the unit propagates from `𝒜'` to all of `D⁺_{𝒜'}(𝒪')` by Tag 0D7T and the
> corresponding statement for the counit from `𝒜` to all of `D⁺_𝒜(𝒪)` by Tag 0D7S; the
> Olsson--Laszlo hypotheses then carry both from the bounded below subcategories to the whole
> derived categories, through Tag 0D6U.

```lean
def derivedPullbackEquivalenceUnbounded
    (hUnit :
      letI := f.pullbackTopos_preservesFiniteLimits hmos hf
      letI := f.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
      ∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
        ((DerivedCategory.singleFunctor (SheafOfModules.{w}
            (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    (DerivedCategoryB.derivedCategoryB A').FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryB A).FullSubcategory
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalenceUnbounded_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean#L587). The attribute's comment: “forward functor”.

> **Stacks 0D7V**, the identification of the forward functor of the equivalence with the
> restriction of the derived pullback.

```lean
theorem derivedPullbackEquivalenceUnbounded_functor
    (hUnit :
      letI := f.pullbackTopos_preservesFiniteLimits hmos hf
      letI := f.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
      ∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
        ((DerivedCategory.singleFunctor (SheafOfModules.{w}
            (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    (derivedPullbackEquivalenceUnbounded f A A' hmos hf hA hEquiv
      B basisCover degreeBound coverings vanishing
      B' basisCover' degreeBound' coverings' vanishing' hUnit).functor =
      (DerivedCategoryB.derivedCategoryB A).lift
        ((DerivedCategoryB.derivedCategoryB A').ι ⋙ derivedPullback f)
        (fun K ↦ derivedCategoryB_derivedPullback_obj f A A' hmos hf hA K.obj K.property)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalenceUnbounded_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean, line 609](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalence.lean#L609). The attribute's comment: “quasi-inverse”.

> **Stacks 0D7V**, the identification of the quasi-inverse of the equivalence with the
> restriction of the derived pushforward.

```lean
theorem derivedPullbackEquivalenceUnbounded_inverse
    (hUnit :
      letI := f.pullbackTopos_preservesFiniteLimits hmos hf
      letI := f.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
      ∀ M, A' M → IsIso ((derivedPullbackPushforwardAdjunctionOfExact f).unit.app
        ((DerivedCategory.singleFunctor (SheafOfModules.{w}
            (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    letI := f.pullbackTopos_preservesFiniteLimits hmos hf
    letI := f.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f
    (derivedPullbackEquivalenceUnbounded f A A' hmos hf hA hEquiv
      B basisCover degreeBound coverings vanishing
      B' basisCover' degreeBound' coverings' vanishing' hUnit).inverse =
      (DerivedCategoryB.derivedCategoryB A').lift
        ((DerivedCategoryB.derivedCategoryB A).ι ⋙ derivedPushforward f)
        (fun K ↦ derivedCategoryB_derivedPushforward_obj f A A' hmos hf hA hEquiv
          B basisCover degreeBound coverings vanishing
          B' basisCover' degreeBound' coverings' vanishing' hUnit K.obj K.property)
```

## Tag 0D7W, a lemma

[Tag 0D7W](https://stacks.math.columbia.edu/tag/0D7W) in the Stacks Project.

**`Stacks.Cohomology.CohomologicalDescent.derivedCategoryB_derivedPullback_obj_relative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean#L429). The attribute's comment: “derived pullback”.

> **Stacks 0D7W**, the assertion that derived pullback restricts. Let `f` be a flat morphism of
> ringed sites and let `𝒜 ⊂ Mod(𝒪)`, `𝒜' ⊂ Mod(𝒪')` be weak Serre subcategories with
> `f^*𝒜' ⊂ 𝒜`. Then `Lf^*` carries `D_{𝒜'}(𝒪')` into `D_𝒜(𝒪)`. Neither standing hypothesis is
> needed: derived pullback is degreewise pullback, which is exact, so `Hʲ(Lf^*K)` is `f^*Hʲ(K)`,
> and `f^*` carries `𝒜'` into `𝒜`.

```lean
theorem derivedCategoryB_derivedPullback_obj_relative :
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
      f.isMorphismOfSites_toRingedToposSiteHom hf
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
    ∀ (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))),
      DerivedCategoryB.derivedCategoryB A' K →
        DerivedCategoryB.derivedCategoryB A
          ((derivedPullback f.toRingedToposSiteHom).obj K)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedCategoryB_derivedPushforward_obj_relative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean#L495). The attribute's comment: “derived pushforward”.

> **Stacks 0D7W**, the assertion that derived pushforward restricts. Under the hypotheses of
> the source — `f` flat, `f^*` inducing an equivalence `𝒜' ⟶ 𝒜`, the unit `ℱ' ⟶ Rf_*f^*ℱ'`
> invertible on `𝒜'`, the source satisfying the Olsson--Laszlo hypothesis of Tag 0D6R and `f`
> together with `𝒜` satisfying the relative hypothesis of Tag 0D6V — the pushforward `Rf_*`
> carries `D_𝒜(𝒪)` into `D_{𝒜'}(𝒪')`.

```lean
theorem derivedCategoryB_derivedPushforward_obj_relative
    (hUnit :
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
        f.isMorphismOfSites_toRingedToposSiteHom hf
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
      ∀ M, A' M → IsIso
        ((derivedPullbackPushforwardAdjunctionOfExact f.toRingedToposSiteHom).unit.app
          ((DerivedCategory.singleFunctor (SheafOfModules.{u}
              (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
      f.isMorphismOfSites_toRingedToposSiteHom hf
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
    ∀ (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))),
      DerivedCategoryB.derivedCategoryB A K →
        DerivedCategoryB.derivedCategoryB A'
          ((derivedPushforward f.toRingedToposSiteHom).obj K)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalenceUnboundedRelative`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean#L534). The attribute's comment: “equivalence”.

> **Stacks 0D7W.** Let `f : (C, 𝒪) ⟶ (C', 𝒪')` be a flat morphism of ringed sites and let
> `𝒜 ⊂ Mod(𝒪)`, `𝒜' ⊂ Mod(𝒪')` be weak Serre subcategories such that `f^*` induces an equivalence
> `𝒜' ⟶ 𝒜` and the unit `ℱ' ⟶ Rf_*f^*ℱ'` is invertible for every `ℱ'` of `𝒜'`, and assume that
> `C, 𝒪, 𝒜` satisfy the standing hypothesis of Tag 0D6R and that `f` together with `𝒜` satisfies
> the relative standing hypothesis of Tag 0D6V. Then the derived pullback is an **equivalence**
> `D_{𝒜'}(𝒪') ≌ D_𝒜(𝒪)`.
>
> The hypothesis on the unit propagates from `𝒜` to all of `D⁺_𝒜(𝒪)` by Tag 0D7S; the two standing
> hypotheses then carry the counit from the bounded below subcategory to the whole derived
> category, through Tag 0D6W. This is Tag 0D7V with its appeal to Tag 0D6U replaced by one to Tag
> 0D6W, which is the source's own description of the proof.

```lean
def derivedPullbackEquivalenceUnboundedRelative
    (hUnit :
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
        f.isMorphismOfSites_toRingedToposSiteHom hf
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
      ∀ M, A' M → IsIso
        ((derivedPullbackPushforwardAdjunctionOfExact f.toRingedToposSiteHom).unit.app
          ((DerivedCategory.singleFunctor (SheafOfModules.{u}
              (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    (DerivedCategoryB.derivedCategoryB A').FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryB A).FullSubcategory
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalenceUnboundedRelative_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean#L563). The attribute's comment: “forward functor”.

> **Stacks 0D7W**, the identification of the forward functor of the equivalence with the
> restriction of the derived pullback.

```lean
theorem derivedPullbackEquivalenceUnboundedRelative_functor
    (hUnit :
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
        f.isMorphismOfSites_toRingedToposSiteHom hf
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
      ∀ M, A' M → IsIso
        ((derivedPullbackPushforwardAdjunctionOfExact f.toRingedToposSiteHom).unit.app
          ((DerivedCategory.singleFunctor (SheafOfModules.{u}
              (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
      f.isMorphismOfSites_toRingedToposSiteHom hf
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
    (derivedPullbackEquivalenceUnboundedRelative f hf A A' hA hEquiv
      B basisCover degreeBound coverings vanishing
      B' basisCover' degreeBound' coverings' vanishing' hUnit).functor =
      (DerivedCategoryB.derivedCategoryB A).lift
        ((DerivedCategoryB.derivedCategoryB A').ι ⋙
          derivedPullback.{u} f.toRingedToposSiteHom)
        (fun K ↦ derivedCategoryB_derivedPullback_obj_relative f hf A A' hA K.obj
          K.property)
```

**`Stacks.Cohomology.CohomologicalDescent.derivedPullbackEquivalenceUnboundedRelative_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CohomologicalDescent/UnboundedEquivalenceRelativeSituation.lean#L590). The attribute's comment: “quasi-inverse”.

> **Stacks 0D7W**, the identification of the quasi-inverse of the equivalence with the
> restriction of the derived pushforward.

```lean
theorem derivedPullbackEquivalenceUnboundedRelative_inverse
    (hUnit :
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
        f.isMorphismOfSites_toRingedToposSiteHom hf
      letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
      letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
      ∀ M, A' M → IsIso
        ((derivedPullbackPushforwardAdjunctionOfExact f.toRingedToposSiteHom).unit.app
          ((DerivedCategory.singleFunctor (SheafOfModules.{u}
              (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj M))) :
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteLimits
      f.isMorphismOfSites_toRingedToposSiteHom hf
    letI := f.toRingedToposSiteHom.pullbackTopos_preservesFiniteColimits
    letI := pullbackOnHomotopy_hasLeftDerivedFunctor_of_exact f.toRingedToposSiteHom
    (derivedPullbackEquivalenceUnboundedRelative f hf A A' hA hEquiv
      B basisCover degreeBound coverings vanishing
      B' basisCover' degreeBound' coverings' vanishing' hUnit).inverse =
      (DerivedCategoryB.derivedCategoryB A').lift
        ((DerivedCategoryB.derivedCategoryB A).ι ⋙
          derivedPushforward.{u} f.toRingedToposSiteHom)
        (fun K ↦ derivedCategoryB_derivedPushforward_obj_relative f hf A A' hA hEquiv
          B basisCover degreeBound coverings vanishing
          B' basisCover' degreeBound' coverings' vanishing' hUnit K.obj K.property)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.28, Tag 0D7N](https://stacks.math.columbia.edu/tag/0D7N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
