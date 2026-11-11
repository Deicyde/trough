---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.FlatFppf.hasLeftDerivedFunctor_abelianLowerShriek, AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekAdjunction, AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekRestrictionIso, AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriek_hasLeftDerivedFunctor, AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekFunctorAdjunction, AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekFunctorRestrictionIso, AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriek_hasLeftDerivedFunctor, AlgebraicGeometry.Stack.LisseEtale.derivedAbelianLowerShriekAdjunction
statement: formalized
proof: formalized
---

# 104.3 The lisse-étale and the flat-fppf sites

Section 104.3 of the Stacks Project, [Tag 08MZ](https://stacks.math.columbia.edu/tag/08MZ). 3 tags here are carried by 35 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07AS, a lemma

[Tag 07AS](https://stacks.math.columbia.edu/tag/07AS) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.hasLeftDerivedFunctor_abelianLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriek.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriek.lean#L275). The attribute's comment: “part (3), existence; conditional on the acyclicity statement of 07AC”.

> **Stacks 07AS (3), existence**, in the form that asserts nothing about how `Lg_!` is
> computed: degreewise lower shriek of abelian sheaves, followed by the localization of the
> homotopy category of `Ab(𝒳_{fppf})`, has a left derived functor along the localization of the
> homotopy category of `Ab(𝒳_{flat,fppf})`. This is the weakening of
> `AlgebraicGeometry.Stack.FlatFppf.hasPointwiseLeftDerivedFunctor_abelianLowerShriek` that
> forgets pointwise-ness.

```lean
theorem hasLeftDerivedFunctor_abelianLowerShriek
    (hFP : AbelianLowerShriekAcyclic B S hS 𝒳) :
    haveI := isContinuous_inclusion B S hS 𝒳 flatClosure
    haveI := isCocontinuous_inclusion B S hS 𝒳 flatClosure
    haveI := abelianLowerShriek_additive B S hS 𝒳
    ((abelianLowerShriek B S hS 𝒳 flatClosure).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).HasLeftDerivedFunctor
      (HomotopyCategory.quasiIso
        (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1}) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriek.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriek.lean#L320). The attribute's comment: “part (3), adjointness; conditional on the acyclicity statement of 07AC”.

> **Stacks 07AS (3), adjointness**: the derived lower-shriek functor on abelian sheaves is
> left adjoint to derived restriction, conditional on the closure property and on the acyclicity
> statement. This is Stacks 09T5 on the unbounded derived category of the Grothendieck abelian
> category `Ab(𝒳_{fppf})`, whose two inputs — existence of `Lg_!` and its absoluteness — both come
> from the acyclicity statement.

```lean
def derivedAbelianLowerShriekAdjunction (hFP : AbelianLowerShriekAcyclic B S hS 𝒳) :
    derivedAbelianLowerShriek B S hS 𝒳 hFP ⊣
      derivedAbelianRestriction B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriek.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriek.lean#L349). The attribute's comment: “part (3), g^\{-1} Lg\_! = id; conditional on the acyclicity statement of 07AC”.

> **Stacks 07AS (3), the last assertion `g⁻¹ Lg_! = id`**: restriction after derived lower
> shriek is canonically the identity of `D(𝒳_{flat,fppf})`, conditional on the closure property and
> on the acyclicity statement.
>
> The ordinary unit `F ⟶ g⁻¹ g_! F` is an isomorphism, the inclusion of the flat objects being
> continuous, cocontinuous and fully faithful — that is Stacks 077I, proved as
> `AlgebraicGeometry.Stack.FlatFppf.isIso_abelianLowerShriek_unit` — and uniqueness of left
> derived functors carries that to the unit of the derived adjunction.

```lean
def derivedAbelianLowerShriekRestrictionIso (hFP : AbelianLowerShriekAcyclic B S hS 𝒳) :
    derivedAbelianLowerShriek B S hS 𝒳 hFP ⋙
        derivedAbelianRestriction B S hS 𝒳 ≅
      𝟭 (DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1}))
```

**`AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriek_hasLeftDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriekUnconditional.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriekUnconditional.lean#L98). The attribute's comment: “part (3), existence of the unbounded left derived functor `Lg_!` on abelian sheaves for the flat-fppf site, with NO hypothesis. The acyclicity statement of Tag 07AC that `AlgebraicGeometry.Stack.FlatFppf.hasLeftDerivedFunctor_abelianLowerShriek` carries as the argument `hFP` is discharged here by `AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriekAcyclic`, which is proved for every algebraic stack out of the object-level vanishing of Tag 0D6X; that theorem lives downstream of the file carrying the conditional form, which is why the conditional form could not cite it. The closure condition of Tag 07AK (1) is likewise a theorem here, not a hypothesis. Only part (3) is covered: parts (1), (2) and (4) are elsewhere”.

> **Stacks 07AS (3), existence of `Lg_!`, for every algebraic stack.** Degreewise lower shriek
> of abelian sheaves, followed by the localization of the homotopy category of `Ab(𝒳_{fppf})`, has
> a left derived functor along the localization of the homotopy category of `Ab(𝒳_{flat,fppf})`.

```lean
theorem abelianLowerShriek_hasLeftDerivedFunctor :
    haveI := isContinuous_inclusion B S hS 𝒳 flatClosure
    haveI := isCocontinuous_inclusion B S hS 𝒳 flatClosure
    haveI := abelianLowerShriek_additive B S hS 𝒳
    ((abelianLowerShriek B S hS 𝒳 flatClosure).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).HasLeftDerivedFunctor
      (HomotopyCategory.quasiIso
        (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1}) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekFunctorAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriekUnconditional.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriekUnconditional.lean#L121). The attribute's comment: “part (3), the adjunction `Lg_! ⊣ g⁻¹` on abelian sheaves for the flat-fppf site, with NO hypothesis: the acyclicity statement of Tag 07AC that `AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekAdjunction` carries as `hFP` is discharged by `AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriekAcyclic`. Only part (3)”.

> **Stacks 07AS (3), adjointness, for every algebraic stack.** The unbounded derived
> lower-shriek functor on abelian sheaves is left adjoint to derived restriction.

```lean
def derivedAbelianLowerShriekFunctorAdjunction :
    derivedAbelianLowerShriekFunctor B S hS 𝒳 ⊣ derivedAbelianRestriction B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekFunctorRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriekUnconditional.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedLowerShriekUnconditional.lean#L131). The attribute's comment: “part (3), `g⁻¹ ∘ Lg_! = id` on abelian sheaves for the flat-fppf site, with NO hypothesis: the acyclicity statement of Tag 07AC that `AlgebraicGeometry.Stack.FlatFppf.derivedAbelianLowerShriekRestrictionIso` carries as `hFP` is discharged by `AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriekAcyclic`. Only part (3)”.

> **Stacks 07AS (3), `g⁻¹ Lg_! = id`, for every algebraic stack.** Restriction after derived
> lower shriek is canonically the identity of `D(𝒳_{flat,fppf})`.

```lean
def derivedAbelianLowerShriekFunctorRestrictionIso :
    derivedAbelianLowerShriekFunctor B S hS 𝒳 ⋙ derivedAbelianRestriction B S hS 𝒳 ≅
      𝟭 (DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1}))
```

**`AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriek_hasLeftDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedLowerShriek.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedLowerShriek.lean#L306). The attribute's comment: “part (1), existence of the unbounded left derived functor `Lg_!` on abelian sheaves for the lisse-étale site, with NO hypothesis. The acyclicity statement of Tag 07AC is discharged by `AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriekAcyclic`, which is proved for every algebraic stack out of the object-level vanishing of Tag 0D6X, `AlgebraicGeometry.Stack.LisseEtale.objectAcyclic`. The closure condition of Tag 07AK (1) for the smooth objects is likewise a theorem here, not a hypothesis, namely `AlgebraicGeometry.Stack.LisseEtale.closedUnderSmoothMorphisms`. Only the abelian-sheaf statement for the lisse-étale site is covered: parts (2) and (4) are the module-level statements, which the source does not know to agree with the abelian one, and part (3) is the flat-fppf site”.

> **Stacks 07AS (1), existence of `Lg_!`, for every algebraic stack.** Degreewise lower shriek
> of abelian sheaves, followed by the localization of the homotopy category of `Ab(𝒳_{étale})`,
> has a left derived functor along the localization of the homotopy category of
> `Ab(𝒳_{lisse,étale})`. This is the weakening of
> `AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriek_hasPointwiseLeftDerivedFunctor` that
> forgets pointwise-ness.

```lean
theorem abelianLowerShriek_hasLeftDerivedFunctor :
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := isCocontinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := abelianLowerShriek_additive.{u, w} B S hS 𝒳
    ((abelianLowerShriek.{u, w} B S hS 𝒳
      (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasLeftDerivedFunctor
      (HomotopyCategory.quasiIso
        (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AbCat.{u, u + 1}) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedAbelianLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedLowerShriek.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedLowerShriek.lean#L391). The attribute's comment: “part (1), the adjunction `Lg_! ⊣ g⁻¹` on abelian sheaves for the lisse-étale site, with NO hypothesis: the acyclicity statement of Tag 07AC that supplies both the existence of `Lg_!` and its absoluteness is discharged by `AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriekAcyclic`, itself proved out of the object-level vanishing of Tag 0D6X, `AlgebraicGeometry.Stack.LisseEtale.objectAcyclic`, and the closure condition of Tag 07AK (1) by `AlgebraicGeometry.Stack.LisseEtale.closedUnderSmoothMorphisms`. Only the abelian-sheaf statement for the lisse-étale site: parts (2) and (4) are the module-level statements and part (3) is the flat-fppf site”.

> **Stacks 07AS (1), adjointness, for every algebraic stack.** The unbounded derived
> lower-shriek functor on abelian sheaves is left adjoint to derived restriction. This is Stacks
> 09T5 on the unbounded derived category of the Grothendieck abelian category `Ab(𝒳_{étale})`,
> whose two inputs — existence of `Lg_!` and its absoluteness — both come from the acyclicity
> statement.

```lean
def derivedAbelianLowerShriekAdjunction :
    derivedAbelianLowerShriek.{u, w} B S hS 𝒳 ⊣ derivedAbelianRestriction.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedAbelianLowerShriekRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedLowerShriek.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedLowerShriek.lean#L419). The attribute's comment: “part (1), `g⁻¹ ∘ Lg_! = id` on abelian sheaves for the lisse-étale site, with NO hypothesis: the acyclicity statement of Tag 07AC is discharged by `AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriekAcyclic`, out of the object-level vanishing of Tag 0D6X, `AlgebraicGeometry.Stack.LisseEtale.objectAcyclic`; the closure condition of Tag 07AK (1) by `AlgebraicGeometry.Stack.LisseEtale.closedUnderSmoothMorphisms`; and the invertibility of the ordinary unit is Tag 077I, `AlgebraicGeometry.Stack.LisseEtale.isIso_abelianLowerShriek_unit`. Only the abelian-sheaf statement for the lisse-étale site: parts (2) and (4) are the module-level statements and part (3) is the flat-fppf site”.

> **Stacks 07AS (1), `g⁻¹ Lg_! = id`, for every algebraic stack.** Restriction after derived
> lower shriek is canonically the identity of `D(𝒳_{lisse,étale})`.
>
> The ordinary unit `F ⟶ g⁻¹ g_! F` is an isomorphism, the inclusion of the smooth objects being
> continuous, cocontinuous and fully faithful — that is Stacks 077I, which for this inclusion is
> `AlgebraicGeometry.Stack.LisseEtale.isIso_abelianLowerShriek_unit` — and uniqueness of left
> derived functors carries that to the unit of the derived adjunction.

```lean
def derivedAbelianLowerShriekRestrictionIso :
    derivedAbelianLowerShriek.{u, w} B S hS 𝒳 ⋙ derivedAbelianRestriction.{u, w} B S hS 𝒳 ≅
      𝟭 (DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AbCat.{u, u + 1}))
```

**`AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriek_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean#L67). The attribute's comment: “part (1), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on abelian sheaves for the lisse-étale site, its adjunction `Lg_! ⊣ g⁻¹` (with invertible unit), and `g⁻¹ ∘ Lg_! = id`, for every algebraic stack and with NO hypothesis. The acyclicity statement of Tag 07AC is the theorem `AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriekAcyclic` and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (1)**, all three assertions, for every algebraic stack and with NO hypothesis.
> For `g : Sh(𝒳_{lisse,étale}) ⟶ Sh(𝒳_{étale})` the comparison morphism of topoi of
> **Stacks 0788** (1):
>
> * the functor `g_! : Ab(𝒳_{lisse,étale}) ⥤ Ab(𝒳_{étale})` has a left derived functor
>   `Lg_! : D(𝒳_{lisse,étale}) ⟶ D(𝒳_{étale})` — degreewise `g_!` followed by the localization of
>   the homotopy category of `Ab(𝒳_{étale})` has a pointwise left derived functor along the
>   localization of the homotopy category of `Ab(𝒳_{lisse,étale})`, and `Lg_!` is that total left
>   derived functor;
> * `Lg_!` is left adjoint to `g⁻¹`, by an adjunction whose unit is an isomorphism;
> * `g⁻¹ ∘ Lg_! = id`.

```lean
theorem abelianLowerShriek_derived :
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := isCocontinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := abelianLowerShriek_additive.{u, w} B S hS 𝒳
    ((abelianLowerShriek.{u, w} B S hS 𝒳
        (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
      (HomotopyCategory.quasiIso
        (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AbCat.{u, u + 1}) (ComplexShape.up ℤ)) ∧
    (∃ adj : derivedAbelianLowerShriek.{u, w} B S hS 𝒳 ⊣
        derivedAbelianRestriction.{u, w} B S hS 𝒳, IsIso adj.unit) ∧
    Nonempty (derivedAbelianLowerShriek.{u, w} B S hS 𝒳 ⋙
        derivedAbelianRestriction.{u, w} B S hS 𝒳 ≅
      𝟭 (DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AbCat.{u, u + 1})))
```

**`AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriek_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean#L109). The attribute's comment: “part (3), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on abelian sheaves for the flat-fppf site, its adjunction `Lg_! ⊣ g⁻¹` (with invertible unit), and `g⁻¹ ∘ Lg_! = id`, for every algebraic stack and with NO hypothesis. The acyclicity statement of Tag 07AC is the theorem `AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriekAcyclic` and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (3)**, all three assertions, for every algebraic stack and with NO hypothesis.
> For `g : Sh(𝒳_{flat,fppf}) ⟶ Sh(𝒳_{fppf})` the comparison morphism of topoi of
> **Stacks 0788** (2):
>
> * the functor `g_! : Ab(𝒳_{flat,fppf}) ⥤ Ab(𝒳_{fppf})` has a left derived functor
>   `Lg_! : D(𝒳_{flat,fppf}) ⟶ D(𝒳_{fppf})` — degreewise `g_!` followed by the localization of the
>   homotopy category of `Ab(𝒳_{fppf})` has a pointwise left derived functor along the localization
>   of the homotopy category of `Ab(𝒳_{flat,fppf})`, and `Lg_!` is that total left derived functor;
> * `Lg_!` is left adjoint to `g⁻¹`, by an adjunction whose unit is an isomorphism;
> * `g⁻¹ ∘ Lg_! = id`.

```lean
theorem abelianLowerShriek_derived :
    haveI := isContinuous_inclusion B S hS 𝒳 flatClosure
    haveI := isCocontinuous_inclusion B S hS 𝒳 flatClosure
    haveI := abelianLowerShriek_additive B S hS 𝒳
    ((abelianLowerShriek B S hS 𝒳 flatClosure).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
      (HomotopyCategory.quasiIso
        (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1}) (ComplexShape.up ℤ)) ∧
    (∃ adj : derivedAbelianLowerShriekFunctor B S hS 𝒳 ⊣ derivedAbelianRestriction B S hS 𝒳,
      IsIso adj.unit) ∧
    Nonempty (derivedAbelianLowerShriekFunctor B S hS 𝒳 ⋙ derivedAbelianRestriction B S hS 𝒳 ≅
      𝟭 (DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1})))
```

**`AlgebraicGeometry.Stack.FlatFppf.lowerShriekModules_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean#L443). The attribute's comment: “part (4), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on sheaves of modules for the flat-fppf site, its adjunction `Lg_! ⊣ g^*` (with invertible unit), and `g^* ∘ Lg_! = id`, for every algebraic stack and with NO hypothesis. The structure sheaf is the one of Tag 06TV; the acyclicity statement of Tag 07AC is a theorem here, `AlgebraicGeometry.Stack.subsiteLowerShriekModulesAcyclic`, and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (4)**, all three assertions, for every algebraic stack and with NO
> hypothesis.  For `g : Sh(𝒳_{flat,fppf}) ⟶ Sh(𝒳_τ)` the morphism of ringed topoi of
> **Stacks 0788**:
>
> * the functor `g_! : Mod(𝒪_{𝒳_{flat,fppf}}) ⥤ Mod(𝒪_𝒳)` has a left derived functor
>   `Lg_! : D(𝒪_{𝒳_{flat,fppf}}) ⟶ D(𝒪_𝒳)` — degreewise `g_!` followed by the localization of the
>   homotopy category of `Mod(𝒪_𝒳)` has a pointwise left derived functor along the localization of
>   the homotopy category of `Mod(𝒪_{𝒳_{flat,fppf}})`, and `Lg_!` is that total left derived functor;
> * `Lg_!` is left adjoint to `g^*`, by an adjunction whose unit is an isomorphism;
> * `g^* ∘ Lg_! = id`.
>
> The structure sheaf is the one of **Stacks 06TV**, with sections in `Type u`, and the modules
> have their sections in `Type (u+1)`.

```lean
theorem lowerShriekModules_derived :
    (FreeRingUniverse.lowerShriekOnHomotopy.{u + 1} (inclusionTopology B S hS 𝒳)
        (associatedTopology B S hS 𝒳.val.val.p B.topology) (objectProperty B S hS 𝒳).ι
        (moduleRing B S hS 𝒳) ⋙
      DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
        (FreeRingUniverse.sourceQuasiIso.{u + 1} (inclusionTopology B S hS 𝒳)
        (associatedTopology B S hS 𝒳.val.val.p B.topology) (objectProperty B S hS 𝒳).ι
        (moduleRing B S hS 𝒳)) ∧
    (∃ adj : derivedLowerShriekModules B S hS 𝒳 ⊣ derivedRestrictionModules B S hS 𝒳,
      IsIso adj.unit) ∧
    Nonempty (derivedLowerShriekModules B S hS 𝒳 ⋙ derivedRestrictionModules B S hS 𝒳 ≅
      𝟭 (DerivedCategory (SheafOfModules.{u + 1} (subsiteModuleRingFlat B S hS 𝒳))))
```

**`AlgebraicGeometry.Stack.LisseEtale.lowerShriekModules_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean#L572). The attribute's comment: “part (2), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on sheaves of modules for the lisse-étale site, its adjunction `Lg_! ⊣ g^*` (with invertible unit), and `g^* ∘ Lg_! = id`, for every algebraic stack and with NO hypothesis. The structure sheaf is the one of Tag 06TV; the acyclicity statement of Tag 07AC is a theorem here, `AlgebraicGeometry.Stack.subsiteLowerShriekModulesAcyclic`, and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (2)**, all three assertions, for every algebraic stack and with NO
> hypothesis.  For `g : Sh(𝒳_{lisse,étale}) ⟶ Sh(𝒳_τ)` the morphism of ringed topoi of
> **Stacks 0788**:
>
> * the functor `g_! : Mod(𝒪_{𝒳_{lisse,étale}}) ⥤ Mod(𝒪_𝒳)` has a left derived functor
>   `Lg_! : D(𝒪_{𝒳_{lisse,étale}}) ⟶ D(𝒪_𝒳)` — degreewise `g_!` followed by the localization of the
>   homotopy category of `Mod(𝒪_𝒳)` has a pointwise left derived functor along the localization of
>   the homotopy category of `Mod(𝒪_{𝒳_{lisse,étale}})`, and `Lg_!` is that total left derived
>   functor;
> * `Lg_!` is left adjoint to `g^*`, by an adjunction whose unit is an isomorphism;
> * `g^* ∘ Lg_! = id`.
>
> The structure sheaf is the one of **Stacks 06TV**, with sections in `Type u`, and the modules
> have their sections in `Type (u+1)`.

```lean
theorem lowerShriekModules_derived :
    (FreeRingUniverse.lowerShriekOnHomotopy.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (ambientTopology B S hS 𝒳) (smoothObject.{u, w} B S hS 𝒳).ι
        (moduleRing.{u, w} B S hS 𝒳) ⋙
      DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
        (FreeRingUniverse.sourceQuasiIso.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (ambientTopology B S hS 𝒳) (smoothObject.{u, w} B S hS 𝒳).ι
        (moduleRing.{u, w} B S hS 𝒳)) ∧
    (∃ adj : derivedLowerShriekModules B S hS 𝒳 ⊣ derivedRestrictionModules B S hS 𝒳,
      IsIso adj.unit) ∧
    Nonempty (derivedLowerShriekModules B S hS 𝒳 ⋙ derivedRestrictionModules B S hS 𝒳 ≅
      𝟭 (DerivedCategory (SheafOfModules.{u + 1} (subsiteModuleRingSmooth B S hS 𝒳))))
```

## Tag 07AV, a lemma

[Tag 07AV](https://stacks.math.columbia.edu/tag/07AV) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.derivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean#L112). The attribute's comment: “the flat-fppf case for abelian sheaves, first identity: g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories, as an isomorphism (g')⁻¹ ⋙ Rf'\_* ≅ Rf\_* ⋙ g⁻¹ for any total right derived functors Rf\_*, Rf'\_* of the two direct images, with no further hypothesis. The degree-zero square of Stacks 07AT (2) and the fact that restricted K-injective complexes compute Rf'\_* (Stacks 07AK at the 2-fibre products V ×\_y 𝒳, the content of Stacks 0GR3) are proved, not assumed”.

> **Stacks 07AV, first identity, for abelian sheaves on the flat-fppf sites:
> `g⁻¹ ∘ Rf_* = Rf'_* ∘ (g')⁻¹`.** Let `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic stacks, `Rf_*`
> and `Rf'_*` total right derived functors of the direct images along `f` and along its restriction
> `f'` to the flat-fppf sites, and `g⁻¹`, `(g')⁻¹` restriction of abelian sheaves to the
> flat-fppf sites of `𝒴` and `𝒳`. Then, on the unbounded derived categories,
>
> `(g')⁻¹ ⋙ Rf'_* ≅ Rf_* ⋙ g⁻¹`.
>
> No hypothesis is made beyond the right derived functor properties of `Rf_*` and `Rf'_*` (a right
> derived functor being determined only up to unique isomorphism). The isomorphism is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero
> identification `AlgebraicGeometry.Stack.FlatFppf.isIso_abelianSheafBaseChange` and at
> `AlgebraicGeometry.Stack.FlatFppf.isIso_derivedPushforwardUnit_restriction`.

```lean
def derivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology)
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p B.topology)
        AddCommGrpCat.{u + 1}))
    (Rf' : DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology B S hS 𝒴) AddCommGrpCat.{u + 1}))
    (αf : haveI := (isContinuous_and_isCocontinuous_homFunctor B S hS f).2
      haveI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p B.topology)
          (associatedTopology B S hS 𝒴.val.val.p B.topology)).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p B.topology)
          (associatedTopology B S hS 𝒴.val.val.p B.topology)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : haveI := isCocontinuous_subsiteFunctor B S hS f hf
      haveI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (flatObject B S hS 𝒳.val)
          (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
        (inclusionTopology B S hS 𝒴)).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (flatObject B S hS 𝒳.val)
          (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
        (inclusionTopology B S hS 𝒴)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology) AddCommGrpCat.{u + 1})
      (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))] :
    haveI := isContinuous_inclusion B S hS 𝒳 (closedUnderFlatMorphisms B S hS 𝒳)
    haveI := isContinuous_inclusion B S hS 𝒴 (closedUnderFlatMorphisms B S hS 𝒴)
    haveI := additive_subsiteRestriction B S hS 𝒳
    haveI := additive_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒴
    (subsiteRestriction B S hS 𝒳.val.val.p B.topology
        (flatObject B S hS 𝒳.val)).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p B.topology
        (flatObject B S hS 𝒴.val)).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean#L344). The attribute's comment: “the flat-fppf case for abelian sheaves, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! of the canonical functors, with no hypothesis: the derived lower shrieks are those of Stacks 07AS (3), and the four derived adjunctions are constructed”.

> **Stacks 07AV, second identity, for abelian sheaves on the flat-fppf sites:
> `L(g')_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg_!`.** For a flat 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, with
> `Lg_!` and `L(g')_!` the derived lower shrieks of **Stacks 07AS** (1) for `𝒴` and `𝒳`, and `f⁻¹`,
> `(f')⁻¹` the inverse images along `f` and along its restriction `f'` to the flat-fppf sites,
>
> `Lg_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')_!`
>
> on the unbounded derived categories of abelian sheaves. All four functors are the canonical ones
> and no hypothesis is made. The isomorphism is the conjugate, under the composites of the derived
> adjunctions `Lg_! ⊣ g⁻¹`, `L(g')_! ⊣ (g')⁻¹` of Stacks 07AS (3) and `f⁻¹ ⊣ Rf_*`,
> `(f')⁻¹ ⊣ Rf'_*` (exact left adjoints), of the first identity
> `AlgebraicGeometry.Stack.FlatFppf.derivedRestrictionBaseChangeIso`.

```lean
def derivedLowerShriekBaseChangeIso :
    derivedAbelianLowerShriekFunctor B S hS 𝒴 ⋙ derivedAbelianInverseImage B S hS f ≅
      derivedAbelianSubsiteInverseImage B S hS f hf ⋙ derivedAbelianLowerShriekFunctor B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.moduleDerivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean#L178). The attribute's comment: “the module case for the flat-fppf sites, first identity: g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories of sheaves of modules, as an isomorphism (g')^* ⋙ Rf'\_* ≅ Rf\_* ⋙ g^* for any total right derived functors Rf\_*, Rf'\_* of the two direct images, with no further hypothesis: the degree-zero square of Stacks 07AT (2) on modules and the fact that restricted K-injective complexes of modules compute Rf'\_* (Stacks 0D6J with Stacks 07AK at the 2-fibre products V ×\_y 𝒳) are proved, not assumed”.

> **Stacks 07AV, first identity, for sheaves of modules on the flat-fppf sites:
> `g^* ∘ Rf_* = Rf'_* ∘ (g')^*`.** For a flat 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, total
> right derived functors `Rf_*`, `Rf'_*` of the direct images of sheaves of modules along `f` and
> along its restriction `f'` to the flat-fppf sites, and `g^*`, `(g')^*` the restrictions of
> sheaves of modules to the flat-fppf sites (which are `g⁻¹`, `(g')⁻¹`),
>
> `(g')^* ⋙ Rf'_* ≅ Rf_* ⋙ g^*`
>
> on the unbounded derived categories, with no further hypothesis. It is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero square
> `AlgebraicGeometry.Stack.FlatFppf.isIso_moduleSquareComparison` and at
> `Stacks.SheafOfModules.isIso_derivedPushforwardUnit_inverseImage`, fed with
> `AlgebraicGeometry.Stack.FlatFppf.qh_map_bijective_directImageCorep_restriction`.

```lean
def moduleDerivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒴)))
    (Rf' : DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒴)))
    (αf : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : (moduleSubsitePushforward B S hS f hf).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))] :
    (moduleInverseImage B S hS 𝒳).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (moduleInverseImage B S hS 𝒴).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.FlatFppf.moduleDerivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean#L353). The attribute's comment: “the module case for the flat-fppf sites, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories of sheaves of modules, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! for the actual derived lower shrieks and the exact inverse images, with no hypothesis: the adjunctions Lg\_! ⊣ g⁻¹, f⁻¹ ⊣ Rf\_* and their primed versions are constructed, and the first identity is proved”.

> **Stacks 07AV, the module case for the flat-fppf sites, second identity.** Let
> `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic stacks, `f'` its restriction to the flat-fppf
> sites, and `Lg_!`, `L(g')_!` the derived lower shrieks of sheaves of modules along the inclusions
> of the flat-fppf sites (`AlgebraicGeometry.Stack.FlatFppf.derivedModuleLowerShriekSucc`). Then
>
> `Lg_! ⋙ f^{-1} ≅ (f')^{-1} ⋙ L(g')_!`
>
> on the unbounded derived categories of sheaves of modules, that is,
> `L(g')_! ∘ (f')^{-1} = f^{-1} ∘ Lg_!`. Here `f^{-1}`, `(f')^{-1}` are the exact inverse images
> (Stacks 06WE, and restriction along `f'`), left adjoint to the canonical total right derived
> direct images `Rf_*`, `Rf'_*` (`derivedAdjunctionOfExactLeftAdjoint` on
> `AlgebraicGeometry.Stack.FlatFppf.modulePullbackPushforwardAdjunction` and
> `AlgebraicGeometry.Stack.FlatFppf.moduleSubsiteInverseImageAdjunction`), and the isomorphism
> is the conjugate, across the composed adjunctions, of the first identity
> `AlgebraicGeometry.Stack.FlatFppf.moduleDerivedRestrictionBaseChangeIso`.

```lean
def moduleDerivedLowerShriekBaseChangeIso :
    derivedModuleLowerShriekSucc B S hS 𝒴 ⋙ derivedModulePullback B S hS f ≅
      derivedModuleSubsiteInverseImage B S hS f hf ⋙ derivedModuleLowerShriekSucc B S hS 𝒳
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean#L163). The attribute's comment: “the lisse-étale case for abelian sheaves, first identity: g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories, as an isomorphism (g')⁻¹ ⋙ Rf'\_* ≅ Rf\_* ⋙ g⁻¹ for any total right derived functors Rf\_*, Rf'\_* of the two direct images, with no further hypothesis. The degree-zero square of Stacks 07AT (1) and the fact that restricted K-injective complexes compute Rf'\_* (Stacks 07AK at the 2-fibre products V ×\_y 𝒳, the content of Stacks 0GR3) are proved, not assumed”.

> **Stacks 07AV, first identity, for abelian sheaves on the lisse-étale sites:
> `g⁻¹ ∘ Rf_* = Rf'_* ∘ (g')⁻¹`.** Let `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic stacks, `Rf_*`
> and `Rf'_*` total right derived functors of the direct images along `f` and along its restriction
> `f'` to the lisse-étale sites, and `g⁻¹`, `(g')⁻¹` restriction of abelian sheaves to the
> lisse-étale sites of `𝒴` and `𝒳`. Then, on the unbounded derived categories,
>
> `(g')⁻¹ ⋙ Rf'_* ≅ Rf_* ⋙ g⁻¹`.
>
> No hypothesis is made beyond the right derived functor properties of `Rf_*` and `Rf'_*` (a right
> derived functor being determined only up to unique isomorphism). The isomorphism is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero
> identification `AlgebraicGeometry.Stack.LisseEtale.isIso_abelianSheafBaseChange` and at
> `AlgebraicGeometry.Stack.LisseEtale.isIso_derivedPushforwardUnit_restriction`.

```lean
def derivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}))
    (Rf' : DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒴) AddCommGrpCat.{u + 1}))
    (αf : haveI := (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
        (etaleTopology B)).2
      haveI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : haveI := isCocontinuous_subsiteFunctor.{u, w} B S hS f hf
      haveI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (smoothObject.{u, w} B S hS 𝒳)
          (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (inclusionTopology.{u, w} B S hS 𝒴)).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (smoothObject.{u, w} B S hS 𝒳)
          (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (inclusionTopology.{u, w} B S hS 𝒴)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) AddCommGrpCat.{u + 1})
      (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))] :
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒴 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒴)
    haveI := additive_subsiteRestriction B S hS 𝒳
    haveI := additive_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒴
    (subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
        (smoothObject.{u, w} B S hS 𝒳)).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
        (smoothObject.{u, w} B S hS 𝒴)).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean#L402). The attribute's comment: “the lisse-étale case for abelian sheaves, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! of the canonical functors, with no hypothesis: the derived lower shrieks are those of Stacks 07AS (1), and the four derived adjunctions are constructed”.

> **Stacks 07AV, second identity, for abelian sheaves on the lisse-étale sites:
> `L(g')_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg_!`.** For a smooth 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, with
> `Lg_!` and `L(g')_!` the derived lower shrieks of **Stacks 07AS** (1) for `𝒴` and `𝒳`, and `f⁻¹`,
> `(f')⁻¹` the inverse images along `f` and along its restriction `f'` to the lisse-étale sites,
>
> `Lg_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')_!`
>
> on the unbounded derived categories of abelian sheaves. All four functors are the canonical ones
> and no hypothesis is made. The isomorphism is the conjugate, under the composites of the derived
> adjunctions `Lg_! ⊣ g⁻¹`, `L(g')_! ⊣ (g')⁻¹` of Stacks 07AS (1) and `f⁻¹ ⊣ Rf_*`,
> `(f')⁻¹ ⊣ Rf'_*` (exact left adjoints), of the first identity
> `AlgebraicGeometry.Stack.LisseEtale.derivedRestrictionBaseChangeIso`.

```lean
def derivedLowerShriekBaseChangeIso :
    derivedAbelianLowerShriek.{u, w} B S hS 𝒴 ⋙ derivedAbelianInverseImage B S hS f ≅
      derivedAbelianSubsiteInverseImage B S hS f hf ⋙ derivedAbelianLowerShriek.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.LisseEtale.moduleDerivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean#L331). The attribute's comment: “the module case for the lisse-étale sites, first identity: g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories of sheaves of modules, as an isomorphism (g')^* ⋙ Rf'\_* ≅ Rf\_* ⋙ g^* for any total right derived functors Rf\_*, Rf'\_* of the two direct images, with no further hypothesis: the degree-zero square of Stacks 07AT (1) on modules and the fact that restricted K-injective complexes of modules compute Rf'\_* (Stacks 0D6J with Stacks 07AK at the 2-fibre products V ×\_y 𝒳) are proved, not assumed”.

> **Stacks 07AV, first identity, for sheaves of modules on the lisse-étale sites:
> `g^* ∘ Rf_* = Rf'_* ∘ (g')^*`.** For a smooth 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, total
> right derived functors `Rf_*`, `Rf'_*` of the direct images of sheaves of modules along `f` and
> along its restriction `f'` to the lisse-étale sites, and `g^*`, `(g')^*` the restrictions of
> sheaves of modules to the lisse-étale sites (which are `g⁻¹`, `(g')⁻¹`),
>
> `(g')^* ⋙ Rf'_* ≅ Rf_* ⋙ g^*`
>
> on the unbounded derived categories, with no further hypothesis. It is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero square
> `AlgebraicGeometry.Stack.LisseEtale.isIso_moduleSquareComparison` and at
> `Stacks.SheafOfModules.isIso_derivedPushforwardUnit_inverseImage`, fed with
> `AlgebraicGeometry.Stack.LisseEtale.qh_map_bijective_directImageCorep_restriction`.

```lean
def moduleDerivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒴)))
    (Rf' : DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒴)))
    (αf : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : (moduleSubsitePushforward B S hS f hf).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))] :
    (moduleInverseImage B S hS 𝒳).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (moduleInverseImage B S hS 𝒴).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.LisseEtale.moduleDerivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean#L513). The attribute's comment: “the module case for the lisse-étale sites, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories of sheaves of modules, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! for the actual derived lower shrieks and the exact inverse images, with no hypothesis: the adjunctions Lg\_! ⊣ g⁻¹, f⁻¹ ⊣ Rf\_* and their primed versions are constructed, and the first identity is proved”.

> **Stacks 07AV, the module case for the lisse-étale sites, second identity.** Let
> `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic stacks, `f'` its restriction to the lisse-étale
> sites, and `Lg_!`, `L(g')_!` the derived lower shrieks of sheaves of modules along the inclusions
> of the lisse-étale sites (`AlgebraicGeometry.Stack.LisseEtale.derivedModuleLowerShriekSucc`). Then
>
> `Lg_! ⋙ f^{-1} ≅ (f')^{-1} ⋙ L(g')_!`
>
> on the unbounded derived categories of sheaves of modules, that is,
> `L(g')_! ∘ (f')^{-1} = f^{-1} ∘ Lg_!`. Here `f^{-1}`, `(f')^{-1}` are the exact inverse images
> (Stacks 06WE, and restriction along `f'`), left adjoint to the canonical total right derived
> direct images `Rf_*`, `Rf'_*` (`derivedAdjunctionOfExactLeftAdjoint` on
> `AlgebraicGeometry.Stack.LisseEtale.modulePullbackPushforwardAdjunction` and
> `AlgebraicGeometry.Stack.LisseEtale.moduleSubsiteInverseImageAdjunction`), and the isomorphism
> is the conjugate, across the composed adjunctions, of the first identity
> `AlgebraicGeometry.Stack.LisseEtale.moduleDerivedRestrictionBaseChangeIso`.

```lean
def moduleDerivedLowerShriekBaseChangeIso :
    derivedModuleLowerShriekSucc B S hS 𝒴 ⋙ derivedModulePullback B S hS f ≅
      derivedModuleSubsiteInverseImage B S hS f hf ⋙ derivedModuleLowerShriekSucc B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.nonempty_moduleInverseImage_comp_derivedPushforward_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean#L471). The attribute's comment: “the module case for the flat-fppf site, first identity: `g⁻¹ ∘ Rf_* ≅ Rf'_* ∘ (g')⁻¹` on the unbounded derived categories of sheaves of modules, where `g`, `g'` are the inclusions of the flat-fppf subsites of `𝒴` and of `𝒳` and `f'` is the restriction of `f` given by Stacks 07AT (2). An isomorphism rather than an equality, and asserted through `Nonempty`: a right derived functor is determined only up to a canonical isomorphism, so `Rf_*` and `Rf'_*` are carried as data together with their comparisons `αf`, `αf'` from the degreewise direct images and the `IsRightDerivedFunctor` property. Two hypotheses are granted. `hzero` is the degree-zero square `f'_* ∘ (g')^* ≅ g^* ∘ f_*` on sheaves of modules, which is the second assertion of Stacks 07AT (2) read on modules; the general base-change theorem Stacks 0FN3 would give it from a cofinality condition on the comparison functors of the index categories of Section 00XF, which is not available for this square. `hKinj` is that `(g')^*` preserves K-injectivity of complexes, which is the conclusion of Stacks 08BJ applied to the module-level adjunction `g'_! ⊣ (g')^*` of Stacks 0797, i.e. it follows from left exactness of the module `g'_!` — Stacks 0789 (2) with Stacks 07AS (4) — which this development has only conditionally. The abelian-sheaf case of the tag is not proved here.”.

> **Stacks 07AV for sheaves of modules on the flat-fppf site, first identity.** Let
> `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic stacks, let `g` and `g'` be the inclusions of the
> flat-fppf subsites of `𝒴` and of `𝒳`, and let `f'` be the restriction of `f` to those subsites,
> **Stacks 07AT** (2). Suppose the degree-zero square `f'_* ∘ (g')^* ≅ g^* ∘ f_*` of sheaves of
> modules holds, and that `(g')^*` carries K-injective complexes to K-injective complexes. Then
>
> `Rf'_* ∘ (g')^* ≅ g^* ∘ Rf_*`
>
> on the unbounded derived categories of sheaves of modules.

```lean
theorem nonempty_moduleInverseImage_comp_derivedPushforward_iso
    (hzero : moduleInverseImage B S hS 𝒳 ⋙ restrictedModulePushforward B S hS f hf ≅
      modulePushforward B S hS f ⋙ moduleInverseImage B S hS 𝒴)
    (hKinj : ∀ I : CochainComplex
        (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ℤ,
      I.IsKInjective → CochainComplex.IsKInjective
        (((moduleInverseImage B S hS 𝒳).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    Nonempty ((moduleInverseImage B S hS 𝒳).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (moduleInverseImage B S hS 𝒴).mapDerivedCategory)
```

**`AlgebraicGeometry.Stack.FlatFppf.nonempty_derivedLowerShriek_comp_moduleInverseImage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean#L520). The attribute's comment: “the module case for the flat-fppf site, second identity: `L(g')_! ∘ (f')⁻¹ ≅ f⁻¹ ∘ Lg_!` on the unbounded derived categories of sheaves of modules, where `g`, `g'` are the inclusions of the flat-fppf subsites of `𝒴` and of `𝒳` and `f'` is the restriction of `f` given by Stacks 07AT (2). An isomorphism rather than an equality, and asserted through `Nonempty`: it is the conjugate of the first identity, whose right-hand sides are right derived functors and so determined only up to a canonical isomorphism, with `Rf_*`, `Rf'_*` and their comparisons `αf`, `αf'` carried as data. The hypotheses granted are those of the first identity — `hzero`, the degree-zero square `f'_* ∘ (g')^* ≅ g^* ∘ f_*` of Stacks 07AT (2) read on modules, and `hKinj`, preservation of K-injectivity by `(g')^*`, which is Stacks 08BJ for the module-level adjunction `g'_! ⊣ (g')^*` of Stacks 0797 and so follows from left exactness of the module `g'_!`, Stacks 0789 (2) with Stacks 07AS (4) — together with the four derived adjunctions, which also carry the derived functors they name as data: `adjg` and `adjg'`, `Lg_! ⊣ g^*` and `L(g')_! ⊣ (g')^*`, the derived form of Stacks 0789 (2) and Stacks 07AS (4), and `adjf` and `adjf'`, `f⁻¹ ⊣ Rf_*` and `(f')⁻¹ ⊣ Rf'_*`. The abelian-sheaf case of the tag is not proved here.”.

> **Stacks 07AV for sheaves of modules on the flat-fppf site, second identity.** In the
> situation of
> `AlgebraicGeometry.Stack.FlatFppf.nonempty_moduleInverseImage_comp_derivedPushforward_iso`,
> suppose moreover that `f^*` and `(f')^*` are left adjoint to `Rf_*` and `Rf'_*` and that `Lg_!`
> and `L(g')_!` are left adjoint to `g^*` and `(g')^*` on the derived categories. Then
>
> `f^* ∘ Lg_! ≅ L(g')_! ∘ (f')^*`
>
> on the unbounded derived categories of sheaves of modules.

```lean
theorem nonempty_derivedLowerShriek_comp_moduleInverseImage_iso
    (adjf : fStar ⊣ Rf) (adjf' : f'Star ⊣ Rf')
    (adjg : Lg ⊣ (moduleInverseImage B S hS 𝒴).mapDerivedCategory)
    (adjg' : Lg' ⊣ (moduleInverseImage B S hS 𝒳).mapDerivedCategory)
    (hzero : moduleInverseImage B S hS 𝒳 ⋙ restrictedModulePushforward B S hS f hf ≅
      modulePushforward B S hS f ⋙ moduleInverseImage B S hS 𝒴)
    (hKinj : ∀ I : CochainComplex
        (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ℤ,
      I.IsKInjective → CochainComplex.IsKInjective
        (((moduleInverseImage B S hS 𝒳).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    Nonempty (Lg ⋙ fStar ≅ f'Star ⋙ Lg')
```

**`AlgebraicGeometry.Stack.LisseEtale.nonempty_moduleInverseImage_comp_derivedPushforward_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean#L652). The attribute's comment: “the module case for the lisse-étale site, first identity: `g⁻¹ ∘ Rf_* ≅ Rf'_* ∘ (g')⁻¹` on the unbounded derived categories of sheaves of modules, where `g`, `g'` are the inclusions of the lisse-étale subsites of `𝒴` and of `𝒳` and `f'` is the restriction of `f` given by Stacks 07AT (1). An isomorphism rather than an equality, and asserted through `Nonempty`: a right derived functor is determined only up to a canonical isomorphism, so `Rf_*` and `Rf'_*` are carried as data together with their comparisons `αf`, `αf'` from the degreewise direct images and the `IsRightDerivedFunctor` property. Two hypotheses are granted. `hzero` is the degree-zero square `f'_* ∘ (g')^* ≅ g^* ∘ f_*` on sheaves of modules, which is the second assertion of Stacks 07AT (1) read on modules; the general base-change theorem Stacks 0FN3 would give it from a cofinality condition on the comparison functors of the index categories of Section 00XF, which is not available for this square. `hKinj` is that `(g')^*` preserves K-injectivity of complexes, which is the conclusion of Stacks 08BJ applied to the module-level adjunction `g'_! ⊣ (g')^*` of Stacks 0797, i.e. it follows from left exactness of the module `g'_!` — Stacks 0789 (1) with Stacks 07AS (2) — which this development has only conditionally. The abelian-sheaf case of the tag is not proved here.”.

> **Stacks 07AV for sheaves of modules on the lisse-étale site, first identity.** Let
> `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic stacks, let `g` and `g'` be the inclusions of
> the lisse-étale subsites of `𝒴` and of `𝒳`, and let `f'` be the restriction of `f` to those
> subsites, **Stacks 07AT** (1). Suppose the degree-zero square `f'_* ∘ (g')^* ≅ g^* ∘ f_*` of
> sheaves of modules holds, and that `(g')^*` carries K-injective complexes to K-injective
> complexes. Then
>
> `Rf'_* ∘ (g')^* ≅ g^* ∘ Rf_*`
>
> on the unbounded derived categories of sheaves of modules.

```lean
theorem nonempty_moduleInverseImage_comp_derivedPushforward_iso
    (hzero : moduleInverseImage B S hS 𝒳 ⋙ restrictedModulePushforward B S hS f hf ≅
      modulePushforward B S hS f ⋙ moduleInverseImage B S hS 𝒴)
    (hKinj : ∀ I : CochainComplex
        (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ℤ,
      I.IsKInjective → CochainComplex.IsKInjective
        (((moduleInverseImage B S hS 𝒳).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    Nonempty ((moduleInverseImage B S hS 𝒳).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (moduleInverseImage B S hS 𝒴).mapDerivedCategory)
```

**`AlgebraicGeometry.Stack.LisseEtale.nonempty_derivedLowerShriek_comp_moduleInverseImage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean#L702). The attribute's comment: “the module case for the lisse-étale site, second identity: `L(g')_! ∘ (f')⁻¹ ≅ f⁻¹ ∘ Lg_!` on the unbounded derived categories of sheaves of modules, where `g`, `g'` are the inclusions of the lisse-étale subsites of `𝒴` and of `𝒳` and `f'` is the restriction of `f` given by Stacks 07AT (1). An isomorphism rather than an equality, and asserted through `Nonempty`: it is the conjugate of the first identity, whose right-hand sides are right derived functors and so determined only up to a canonical isomorphism, with `Rf_*`, `Rf'_*` and their comparisons `αf`, `αf'` carried as data. The hypotheses granted are those of the first identity — `hzero`, the degree-zero square `f'_* ∘ (g')^* ≅ g^* ∘ f_*` of Stacks 07AT (1) read on modules, and `hKinj`, preservation of K-injectivity by `(g')^*`, which is Stacks 08BJ for the module-level adjunction `g'_! ⊣ (g')^*` of Stacks 0797 and so follows from left exactness of the module `g'_!`, Stacks 0789 (1) with Stacks 07AS (2) — together with the four derived adjunctions, which also carry the derived functors they name as data: `adjg` and `adjg'`, `Lg_! ⊣ g^*` and `L(g')_! ⊣ (g')^*`, the derived form of Stacks 0789 (1) and Stacks 07AS (2), and `adjf` and `adjf'`, `f⁻¹ ⊣ Rf_*` and `(f')⁻¹ ⊣ Rf'_*`. The abelian-sheaf case of the tag is not proved here.”.

> **Stacks 07AV for sheaves of modules on the lisse-étale site, second identity.** In the
> situation of
> `AlgebraicGeometry.Stack.LisseEtale.nonempty_moduleInverseImage_comp_derivedPushforward_iso`,
> suppose moreover that `f^*` and `(f')^*` are left adjoint to `Rf_*` and `Rf'_*` and that `Lg_!`
> and `L(g')_!` are left adjoint to `g^*` and `(g')^*` on the derived categories. Then
>
> `f^* ∘ Lg_! ≅ L(g')_! ∘ (f')^*`
>
> on the unbounded derived categories of sheaves of modules.

```lean
theorem nonempty_derivedLowerShriek_comp_moduleInverseImage_iso
    (adjf : fStar ⊣ Rf) (adjf' : f'Star ⊣ Rf')
    (adjg : Lg ⊣ (moduleInverseImage B S hS 𝒴).mapDerivedCategory)
    (adjg' : Lg' ⊣ (moduleInverseImage B S hS 𝒳).mapDerivedCategory)
    (hzero : moduleInverseImage B S hS 𝒳 ⋙ restrictedModulePushforward B S hS f hf ≅
      modulePushforward B S hS f ⋙ moduleInverseImage B S hS 𝒴)
    (hKinj : ∀ I : CochainComplex
        (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ℤ,
      I.IsKInjective → CochainComplex.IsKInjective
        (((moduleInverseImage B S hS 𝒳).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)) :
    Nonempty (Lg ⋙ fStar ≅ f'Star ⋙ Lg')
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedPushforwardRestrictionIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean#L436). The attribute's comment: “the lisse-étale case for abelian sheaves, first identity: Rf'\_* ∘ (g')⁻¹ ≅ g⁻¹ ∘ Rf\_* on the *unbounded* derived categories. An isomorphism rather than an equality, a right derived functor being determined only up to a canonical isomorphism; the two total right derived direct images, their comparisons from the degreewise direct images and the two IsRightDerivedFunctor properties are carried as data, as in Stacks 0FN6 and 0FN7. Granted: that restriction to the lisse-étale site carries K-injective cochain complexes to K-injective ones, which is Stacks 08BJ from exactness of g\_! = Stacks 07AS (3); and the degree-zero identification f\_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ f'\_* of Stacks 07AT (1). The module case is not proved here.”.

> **Stacks 07AV, the lisse-étale case for abelian sheaves: `g⁻¹ ∘ Rf_* = Rf'_* ∘ (g')⁻¹`.** Let
> `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic stacks, let `g⁻¹` and `(g')⁻¹` be restriction of
> abelian sheaves to the lisse-étale sites of `𝒴` and of `𝒳`, and let `f_*` and `f'_*` be the direct
> images along `f` and along its restriction `f'` to the lisse-étale sites. Suppose `(g')⁻¹` carries
> K-injective cochain complexes to K-injective ones, and that the degree-zero identification
> `f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ f'_*` of **Stacks 07AT** (1) holds. Then, on the unbounded derived
> categories,
>
> `Rf'_* ∘ (g')⁻¹ ≅ g⁻¹ ∘ Rf_*`.
>
> Both restrictions are exact, so they act degreewise on derived categories, and the abelian sheaves
> on the two sites of `𝒳` are Grothendieck abelian, so both sides are right derived functors of one
> and the same functor out of the homotopy category; the isomorphism is the comparison that the
> universal property produces. This is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIso` at this square of sites.

```lean
theorem derivedPushforwardRestrictionIso :
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (smoothObject.{u, w} B S hS 𝒳)
        (smoothObject_map.{u, w} B S hS f hf)).IsContinuous
          (inclusionTopology.{u, w} B S hS 𝒳) (inclusionTopology.{u, w} B S hS 𝒴) :=
      isContinuous_subsiteFunctor.{u, w} B S hS f hf
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (smoothObject.{u, w} B S hS 𝒳)
        (smoothObject_map.{u, w} B S hS f hf)).IsCocontinuous
          (inclusionTopology.{u, w} B S hS 𝒳) (inclusionTopology.{u, w} B S hS 𝒴) :=
      isCocontinuous_subsiteFunctor.{u, w} B S hS f hf
    letI : f.hom.hom.toFunctor.IsContinuous
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)) :=
      (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
        (etaleTopology B)).1
    letI : f.hom.hom.toFunctor.IsCocontinuous
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)) :=
      (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
        (etaleTopology B)).2
    letI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    letI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (smoothObject.{u, w} B S hS 𝒳)
          (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (inclusionTopology.{u, w} B S hS 𝒴)).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    ∀ (_hKinj : ∀ I : CochainComplex (Sheaf
            (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
            AddCommGrpCat.{u + 1}) ℤ, I.IsKInjective →
          CochainComplex.IsKInjective
            (((subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
              (smoothObject.{u, w} B S hS 𝒳)).mapHomologicalComplex
                (ComplexShape.up ℤ)).obj I))
      (_hzero : f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
              (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
              (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B)) ⋙
            subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
              (smoothObject.{u, w} B S hS 𝒴) ≅
          subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
              (smoothObject.{u, w} B S hS 𝒳) ⋙
            (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
                (smoothObject.{u, w} B S hS 𝒳)
                (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
              AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
              (inclusionTopology.{u, w} B S hS 𝒴))
      (Rf : DerivedCategory (Sheaf
            (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
            AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
            AddCommGrpCat.{u + 1}))
      (Rf' : DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳)
            AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒴) AddCommGrpCat.{u + 1}))
      (αf : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
              (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
              (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
      (αf' : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
                (smoothObject.{u, w} B S hS 𝒳)
                (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
              AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
              (inclusionTopology.{u, w} B S hS 𝒴)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
            DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
      (_hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
          (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
            AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ)))
      (_hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
          (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1})
          (ComplexShape.up ℤ))),
      Nonempty ((subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
            (smoothObject.{u, w} B S hS 𝒳)).mapDerivedCategory ⋙ Rf' ≅
          Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
            (smoothObject.{u, w} B S hS 𝒴)).mapDerivedCategory)
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedShriekInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean#L549). The attribute's comment: “the lisse-étale case for abelian sheaves, second identity: f⁻¹ ∘ Lg\_! ≅ L(g')\_! ∘ (f')⁻¹ on the unbounded derived categories, obtained formally from the first identity as its conjugate under the composed adjunctions. An isomorphism rather than an equality, the derived functors being determined only up to canonical isomorphism and carried as data. Granted: the first identity itself, and the four derived adjunctions Lg\_! ⊣ g⁻¹ and L(g')\_! ⊣ (g')⁻¹ — which are Stacks 07AS (3) — together with f⁻¹ ⊣ Rf\_* and (f')⁻¹ ⊣ Rf'\_*, which are standard. The module case is not proved here.”.

> **Stacks 07AV, the lisse-étale case for abelian sheaves: `L(g')_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg_!`.**
> Let `Rf_*` and `Rf'_*` be the total right derived direct images along a smooth 1-morphism
> `f : 𝒳 ⟶ 𝒴` and along its restriction `f'` to the lisse-étale sites, let `Lg_!` and `L(g')_!` be
> the derived lower shrieks of **Stacks 07AS** (3) over `𝒴` and over `𝒳`, left adjoint to the derived
> restrictions `g⁻¹` and `(g')⁻¹`, and let `f⁻¹` and `(f')⁻¹` be the derived inverse images, left
> adjoint to `Rf_*` and `Rf'_*`. Then the base change isomorphism
> `σ : Rf'_* ∘ (g')⁻¹ ≅ g⁻¹ ∘ Rf_*` of
> `AlgebraicGeometry.Stack.LisseEtale.derivedPushforwardRestrictionIso` gives
>
> `f⁻¹ ∘ Lg_! ≅ L(g')_! ∘ (f')⁻¹`.
>
> This is the source's "the rest of the proof is formal": the two sides are left adjoint to the two
> sides of `σ`, by composing the adjunctions, and `σ` is the conjugate of the asserted isomorphism
> under `CategoryTheory.conjugateIsoEquiv`.

```lean
def derivedShriekInverseImageIso
    (Rf : DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}))
    (Rf' : DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒴) AddCommGrpCat.{u + 1}))
    (Lg : DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒴) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}))
    (Lg' : DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}))
    (finv : DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}))
    (f'inv : DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒴) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}))
    (adjg : Lg ⊣ (subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
      (smoothObject.{u, w} B S hS 𝒴)).mapDerivedCategory)
    (adjg' : Lg' ⊣ (subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
      (smoothObject.{u, w} B S hS 𝒳)).mapDerivedCategory)
    (adjf : finv ⊣ Rf) (adjf' : f'inv ⊣ Rf')
    (σ : (subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
          (smoothObject.{u, w} B S hS 𝒳)).mapDerivedCategory ⋙ Rf' ≅
        Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
          (smoothObject.{u, w} B S hS 𝒴)).mapDerivedCategory) :
    Lg ⋙ finv ≅ f'inv ⋙ Lg'
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedPushforwardRestrictionIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean, line 767](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean#L767). The attribute's comment: “the flat-fppf case for abelian sheaves, first identity: Rf'\_* ∘ (g')⁻¹ ≅ g⁻¹ ∘ Rf\_* on the *unbounded* derived categories. An isomorphism rather than an equality, a right derived functor being determined only up to a canonical isomorphism; the two total right derived direct images, their comparisons from the degreewise direct images and the two IsRightDerivedFunctor properties are carried as data, as in Stacks 0FN6 and 0FN7. Granted: that restriction to the flat-fppf site carries K-injective cochain complexes to K-injective ones, which is Stacks 08BJ from exactness of g\_! = Stacks 07AS (3); and the degree-zero identification f\_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ f'\_* of Stacks 07AT (2). The module case is not proved here.”.

> **Stacks 07AV, the flat-fppf case for abelian sheaves: `g⁻¹ ∘ Rf_* = Rf'_* ∘ (g')⁻¹`.** Let
> `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic stacks, let `g⁻¹` and `(g')⁻¹` be restriction of
> abelian sheaves to the flat-fppf sites of `𝒴` and of `𝒳`, and let `f_*` and `f'_*` be the direct
> images along `f` and along its restriction `f'` to the flat-fppf sites. Suppose `(g')⁻¹` carries
> K-injective cochain complexes to K-injective ones, and that the degree-zero identification
> `f_* ∘ g⁻¹ ≅ (g')⁻¹ ∘ f'_*` of **Stacks 07AT** (2) holds. Then, on the unbounded derived
> categories,
>
> `Rf'_* ∘ (g')⁻¹ ≅ g⁻¹ ∘ Rf_*`.
>
> Both restrictions are exact, so they act degreewise on derived categories, and the abelian sheaves
> on the two sites of `𝒳` are Grothendieck abelian, so both sides are right derived functors of one
> and the same functor out of the homotopy category; the isomorphism is the comparison that the
> universal property produces. This is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIso` at this square of sites.

```lean
theorem derivedPushforwardRestrictionIso :
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (flatObject B S hS 𝒳.val)
        (flatObject_map B S hS f hf)).IsContinuous
          (inclusionTopology B S hS 𝒳) (inclusionTopology B S hS 𝒴) :=
      isContinuous_subsiteFunctor B S hS f hf
    letI : (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
        (flatObject B S hS 𝒳.val)
        (flatObject_map B S hS f hf)).IsCocontinuous
          (inclusionTopology B S hS 𝒳) (inclusionTopology B S hS 𝒴) :=
      isCocontinuous_subsiteFunctor B S hS f hf
    letI : f.hom.hom.toFunctor.IsContinuous
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology) :=
      (isContinuous_and_isCocontinuous_homFunctor B S hS f).1
    letI : f.hom.hom.toFunctor.IsCocontinuous
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology) :=
      (isContinuous_and_isCocontinuous_homFunctor B S hS f).2
    letI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
        (associatedTopology B S hS 𝒳.val.val.p B.topology)
        (associatedTopology B S hS 𝒴.val.val.p B.topology)).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    letI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (flatObject B S hS 𝒳.val)
          (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
        (inclusionTopology B S hS 𝒴)).Additive :=
      Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
    ∀ (_hKinj : ∀ I : CochainComplex (Sheaf
            (associatedTopology B S hS 𝒳.val.val.p B.topology)
            AddCommGrpCat.{u + 1}) ℤ, I.IsKInjective →
          CochainComplex.IsKInjective
            (((subsiteRestriction B S hS 𝒳.val.val.p B.topology
              (flatObject B S hS 𝒳.val)).mapHomologicalComplex
                (ComplexShape.up ℤ)).obj I))
      (_hzero : f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
              (associatedTopology B S hS 𝒳.val.val.p B.topology)
              (associatedTopology B S hS 𝒴.val.val.p B.topology) ⋙
            subsiteRestriction B S hS 𝒴.val.val.p B.topology
              (flatObject B S hS 𝒴.val) ≅
          subsiteRestriction B S hS 𝒳.val.val.p B.topology
              (flatObject B S hS 𝒳.val) ⋙
            (SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
                (flatObject B S hS 𝒳.val)
                (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
              AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
              (inclusionTopology B S hS 𝒴))
      (Rf : DerivedCategory (Sheaf
            (associatedTopology B S hS 𝒳.val.val.p B.topology)
            AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p B.topology)
            AddCommGrpCat.{u + 1}))
      (Rf' : DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳)
            AddCommGrpCat.{u + 1}) ⥤
          DerivedCategory (Sheaf (inclusionTopology B S hS 𝒴) AddCommGrpCat.{u + 1}))
      (αf : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
              (associatedTopology B S hS 𝒳.val.val.p B.topology)
              (associatedTopology B S hS 𝒴.val.val.p B.topology)).mapHomotopyCategory
            (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
      (αf' : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
                (flatObject B S hS 𝒳.val)
                (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
              AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
              (inclusionTopology B S hS 𝒴)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
            DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
      (_hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
          (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology)
            AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ)))
      (_hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
          (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1})
          (ComplexShape.up ℤ))),
      Nonempty ((subsiteRestriction B S hS 𝒳.val.val.p B.topology
            (flatObject B S hS 𝒳.val)).mapDerivedCategory ⋙ Rf' ≅
          Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p B.topology
            (flatObject B S hS 𝒴.val)).mapDerivedCategory)
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedShriekInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean, line 877](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedPushforwardBaseChange.lean#L877). The attribute's comment: “the flat-fppf case for abelian sheaves, second identity: f⁻¹ ∘ Lg\_! ≅ L(g')\_! ∘ (f')⁻¹ on the unbounded derived categories, obtained formally from the first identity as its conjugate under the composed adjunctions. An isomorphism rather than an equality, the derived functors being determined only up to canonical isomorphism and carried as data. Granted: the first identity itself, and the four derived adjunctions Lg\_! ⊣ g⁻¹ and L(g')\_! ⊣ (g')⁻¹ — which are Stacks 07AS (3) — together with f⁻¹ ⊣ Rf\_* and (f')⁻¹ ⊣ Rf'\_*, which are standard. The module case is not proved here.”.

> **Stacks 07AV, the flat-fppf case for abelian sheaves: `L(g')_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg_!`.**
> Let `Rf_*` and `Rf'_*` be the total right derived direct images along a flat 1-morphism
> `f : 𝒳 ⟶ 𝒴` and along its restriction `f'` to the flat-fppf sites, let `Lg_!` and `L(g')_!` be the
> derived lower shrieks of **Stacks 07AS** (3) over `𝒴` and over `𝒳`, left adjoint to the derived
> restrictions `g⁻¹` and `(g')⁻¹`, and let `f⁻¹` and `(f')⁻¹` be the derived inverse images, left
> adjoint to `Rf_*` and `Rf'_*`. Then the base change isomorphism
> `σ : Rf'_* ∘ (g')⁻¹ ≅ g⁻¹ ∘ Rf_*` of
> `AlgebraicGeometry.Stack.FlatFppf.derivedPushforwardRestrictionIso` gives
>
> `f⁻¹ ∘ Lg_! ≅ L(g')_! ∘ (f')⁻¹`.
>
> This is the source's "the rest of the proof is formal": the two sides are left adjoint to the two
> sides of `σ`, by composing the adjunctions, and `σ` is the conjugate of the asserted isomorphism
> under `CategoryTheory.conjugateIsoEquiv`.

```lean
def derivedShriekInverseImageIso
    (Rf : DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology)
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p B.topology)
        AddCommGrpCat.{u + 1}))
    (Rf' : DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology B S hS 𝒴) AddCommGrpCat.{u + 1}))
    (Lg : DerivedCategory (Sheaf (inclusionTopology B S hS 𝒴) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p B.topology)
        AddCommGrpCat.{u + 1}))
    (Lg' : DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology)
        AddCommGrpCat.{u + 1}))
    (finv : DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p B.topology)
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology)
        AddCommGrpCat.{u + 1}))
    (f'inv : DerivedCategory (Sheaf (inclusionTopology B S hS 𝒴) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}))
    (adjg : Lg ⊣ (subsiteRestriction B S hS 𝒴.val.val.p B.topology
      (flatObject B S hS 𝒴.val)).mapDerivedCategory)
    (adjg' : Lg' ⊣ (subsiteRestriction B S hS 𝒳.val.val.p B.topology
      (flatObject B S hS 𝒳.val)).mapDerivedCategory)
    (adjf : finv ⊣ Rf) (adjf' : f'inv ⊣ Rf')
    (σ : (subsiteRestriction B S hS 𝒳.val.val.p B.topology
          (flatObject B S hS 𝒳.val)).mapDerivedCategory ⋙ Rf' ≅
        Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p B.topology
          (flatObject B S hS 𝒴.val)).mapDerivedCategory) :
    Lg ⋙ finv ≅ f'inv ⋙ Lg'
```

## Tag 07B3, a lemma

[Tag 07B3](https://stacks.math.columbia.edu/tag/07B3) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.locallyQuasicoherentSheafFlatBaseChange_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedModuleLowerShriekSheafFlatBaseChange.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedModuleLowerShriekSheafFlatBaseChange.lean#L90). The attribute's comment: “part (2): for a quasi-coherent module `H` (Stacks 03DL) on the flat-fppf site of an arbitrary algebraic stack and every `p`, `H^p(Lg_! H)` is a locally quasi-coherent module with the flat base change property, the class `LQCoh^fbc` of Stacks 0762 read with the pullback of sheaves, for the actual derived lower shriek `Lg_!` of Stacks 07AS (4) at the universe of the rings, with no hypothesis”.

> Let `H` be a quasi-coherent module on the flat-fppf site of an algebraic
> stack `𝒳`. For every `p`, the cohomology sheaf `H^p(Lg_! H)` of the derived lower shriek of
> Stacks 07AS (4) is a locally quasi-coherent module with the flat base change property on `𝒳`, the
> flat base change property of Stacks 0762 being read with the pullback of sheaves.

```lean
theorem locallyQuasicoherentSheafFlatBaseChange_homology_derivedModuleLowerShriek
    (H : flatFppfModules B S hS 𝒳) (hH : H.IsQuasicoherentOnSite) (p : ℤ) :
    letI := (SheafOfModules.instAbelian _ : Abelian (fppfModules B S hS 𝒳))
    letI := abelianFlatFppfModulesSpelling B S hS 𝒳
    letI := HasDerivedCategory.standard (flatFppfModules B S hS 𝒳)
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳
      ((DerivedCategory.homologyFunctor _ p).obj
        ((derivedModuleLowerShriek B S hS 𝒳).obj ((DerivedCategory.singleFunctor _ 0).obj H)))
```

**`AlgebraicGeometry.Stack.LisseEtale.isLocallyQuasicoherentWithSheafFlatBaseChange_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedModuleLowerShriekSheafFlatBaseChange.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedModuleLowerShriekSheafFlatBaseChange.lean#L56). The attribute's comment: “part (1): for a quasi-coherent module `H` (Stacks 03DL) on the lisse-étale site of an arbitrary algebraic stack and every `p`, `H^p(Lg_! H)` is a locally quasi-coherent module with the flat base change property, the class `LQCoh^fbc` of Stacks 0762 read with the pullback of sheaves, for the actual derived lower shriek `Lg_!` of Stacks 07AS (2) at the universe of the rings, with no hypothesis”.

> Let `H` be a quasi-coherent module on the lisse-étale site of an algebraic stack `𝒳`. For
> every `p`, the cohomology sheaf `H^p(Lg_! H)` of the derived lower shriek `Lg_!` is a locally
> quasi-coherent module with the flat base change property on `𝒳`, the flat base change property
> being read with the pullback of sheaves.

```lean
theorem isLocallyQuasicoherentWithSheafFlatBaseChange_homology_derivedModuleLowerShriek
    (H : SheafOfModules.{u} (lisseEtaleModuleRing B S hS 𝒳)) (hH : H.IsQuasicoherentOnSite)
    (p : ℤ) :
    letI := abelianEtaleModules B S hS 𝒳
    letI := abelianLisseEtaleModules B S hS 𝒳
    letI := HasDerivedCategory.standard (SheafOfModules.{u} (lisseEtaleModuleRing B S hS 𝒳))
    letI := HasDerivedCategory.standard (SheafOfModules.{u}
      (SmallModel.targetRing (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedRingedTopos B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids (etaleTopology B)
          (etaleTopology_le_topology B)).O))
    IsLocallyQuasicoherentWithSheafFlatBaseChange.{u, u + 1, u, u} B E h S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      ((DerivedCategory.homologyFunctor _ p).obj
        ((derivedModuleLowerShriek B S hS 𝒳).obj
          ((DerivedCategory.singleFunctor _ 0).obj H))).val
```

**`AlgebraicGeometry.Stack.LisseEtale.isLocallyQuasicoherent_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean#L170). The attribute's comment: “part (1), the local quasi-coherence half: for a quasi-coherent module `H` on the lisse-étale site of an algebraic stack `𝒳` and every `p`, the sheaf `H^p(Lg_! H)` is locally quasi-coherent (Stacks 06WJ) on `𝒳`, read at section universe `u + 1`. Three hypotheses are carried. `Lg` is the functor `Lg_!` itself, carried as data because this library constructs no unbounded total left derived functor of the module-level `g_!` of Stacks 0789 (1); it stands for Stacks 07AS (2) and (4) on sheaves of modules, and is carried in the same shape as in StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean. `hserre` is Stacks 0771 part (2), the half saying that LQCoh^fbc is a weak Serre subcategory of Mod(𝒳\_étale, 𝒪\_𝒳); only part (3) of Stacks 0771 is proved here. `hK` and `e` say that `Lg_! H` is represented by a complex whose TERMS are quasi-coherent (Stacks 03DL), which is the computation of `Lg_! H` from a free resolution that the source performs before citing Stacks 0771, and `hqc` is Stacks 06WK, that a quasi-coherent module lies in LQCoh^fbc, which this library does not have in any form; the reduction of the general case to the affine case with a global presentation, by Stacks 07AQ and Stacks 07AV, is not carried out. The quasi-coherence hypothesis on `H` is the source's and is unweakened”.

> **Stacks 07B3 part (1), local quasi-coherence**: for a quasi-coherent module `H` on the
> lisse-étale site of `𝒳`, every cohomology sheaf of `Lg_! H` is locally quasi-coherent.

```lean
theorem isLocallyQuasicoherent_homology_derivedModuleLowerShriek
    (hH : H.IsQuasicoherentOnSite)
    (hserre : StackEtaleModuleRule.IsWeakSerre.{u, w} B S hS
      (locallyQuasicoherentFlatBaseChangeRule B E h S hS))
    (hqc : ∀ F : _root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳),
      F.IsQuasicoherentOnSite → locallyQuasicoherentFlatBaseChangeRule B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids F.val)
    (hK : ∀ m : ℤ, (K.X m).IsQuasicoherentOnSite)
    (e : Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H) ≅ DerivedCategory.Q.obj K)
    (p : ℤ) :
    IsLocallyQuasicoherent B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      ((DerivedCategory.homologyFunctor _ p).obj
        (Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H))).val
```

**`AlgebraicGeometry.Stack.LisseEtale.hasFlatBaseChange_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean#L201). The attribute's comment: “part (1), the flat base change half: for a quasi-coherent module `H` on the lisse-étale site of an algebraic stack `𝒳` and every `p`, the sheaf `H^p(Lg_! H)` has the flat base change property (Stacks 0762) on `𝒳`, read at section universe `u + 1` through HasFlatBaseChangePropertyUnivLE, the comparison map of Stacks 06WC pinning the other spelling to Type u. The same three hypotheses are carried as for the local quasi-coherence half. `Lg` is `Lg_!` carried as data, standing for Stacks 07AS (2) and (4) on sheaves of modules, no unbounded total left derived functor of the module-level `g_!` of Stacks 0789 (1) being constructed here. `hserre` is Stacks 0771 part (2) for Mod(𝒳\_étale, 𝒪\_𝒳); only part (3) of Stacks 0771 is proved here. `hK` and `e` say that `Lg_! H` is represented by a complex whose TERMS lie in LQCoh^fbc, the source's computation of `Lg_! H` from a free resolution; the reduction of the general case to the affine case with a global presentation, by Stacks 07AQ and Stacks 07AV, is not carried out. The quasi-coherence hypothesis on `H` is the source's and is unweakened”.

> **Stacks 07B3 part (1), the flat base change property**: for a quasi-coherent module `H` on
> the lisse-étale site of `𝒳`, every cohomology sheaf of `Lg_! H` has the flat base change
> property.

```lean
theorem hasFlatBaseChange_homology_derivedModuleLowerShriek
    (hH : H.IsQuasicoherentOnSite)
    (hserre : StackEtaleModuleRule.IsWeakSerre.{u, w} B S hS
      (locallyQuasicoherentFlatBaseChangeRule B E h S hS))
    (hqc : ∀ F : _root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳),
      F.IsQuasicoherentOnSite → locallyQuasicoherentFlatBaseChangeRule B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids F.val)
    (hK : ∀ m : ℤ, (K.X m).IsQuasicoherentOnSite)
    (e : Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H) ≅ DerivedCategory.Q.obj K)
    (p : ℤ) :
    HasFlatBaseChangePropertyUnivLE B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      (etaleTopology B) (etaleTopology_le_topology B)
      ((DerivedCategory.homologyFunctor _ p).obj
        (Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H))).val
```

**`AlgebraicGeometry.Stack.FlatFppf.isLocallyQuasicoherent_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean#L278). The attribute's comment: “part (2), the local quasi-coherence half: for a quasi-coherent module `H` on the flat-fppf site of an algebraic stack `𝒳` and every `p`, the sheaf `H^p(Lg_! H)` is locally quasi-coherent (Stacks 06WJ) on `𝒳`, read at section universe `u + 1`. Three hypotheses are carried. `Lg` is the functor `Lg_!` itself, carried as data because this library constructs no unbounded total left derived functor of the module-level `g_!` of Stacks 0789 (2); it stands for Stacks 07AS (2) and (4) on sheaves of modules, and is carried in the same shape as in StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleBaseChange.lean. `hserre` is Stacks 0771 part (2), the half saying that LQCoh^fbc is a weak Serre subcategory of Mod(𝒪\_𝒳), written out on the fppf site; only part (3) of Stacks 0771 is proved here. `hK` and `e` say that `Lg_! H` is represented by a complex whose TERMS lie in LQCoh^fbc, which is the computation of `Lg_! H` from a free resolution that the source performs before citing Stacks 0771; the reduction of the general case to the affine case with a global presentation, by Stacks 07AQ and Stacks 07AV, is not carried out. The quasi-coherence hypothesis on `H` is the source's and is unweakened”.

> **Stacks 07B3 part (2), local quasi-coherence**: for a quasi-coherent module `H` on the
> flat-fppf site of `𝒳`, every cohomology sheaf of `Lg_! H` is locally quasi-coherent.

```lean
theorem isLocallyQuasicoherent_homology_derivedModuleLowerShriek
    (hH : H.IsQuasicoherentOnSite)
    (hserre : ObjectProperty.IsWeakSerreClass
      (C := _root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳))
      (fun F => locallyQuasicoherentFlatBaseChangeRule B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids F.val))
    (hqc : ∀ F : _root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳),
      F.IsQuasicoherentOnSite → locallyQuasicoherentFlatBaseChangeRule B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids F.val)
    (hK : ∀ m : ℤ, (K.X m).IsQuasicoherentOnSite)
    (e : Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H) ≅ DerivedCategory.Q.obj K)
    (p : ℤ) :
    IsLocallyQuasicoherent B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      ((DerivedCategory.homologyFunctor _ p).obj
        (Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H))).val
```

**`AlgebraicGeometry.Stack.FlatFppf.hasFlatBaseChange_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteDerivedModuleQuasicoherence.lean#L314). The attribute's comment: “part (2), the flat base change half: for a quasi-coherent module `H` on the flat-fppf site of an algebraic stack `𝒳` and every `p`, the sheaf `H^p(Lg_! H)` has the flat base change property (Stacks 0762) on `𝒳`, read at section universe `u + 1` through HasFlatBaseChangePropertyUnivLE, the comparison map of Stacks 06WC pinning the other spelling to Type u. The same three hypotheses are carried as for the local quasi-coherence half. `Lg` is `Lg_!` carried as data, standing for Stacks 07AS (2) and (4) on sheaves of modules, no unbounded total left derived functor of the module-level `g_!` of Stacks 0789 (2) being constructed here. `hserre` is Stacks 0771 part (2) for Mod(𝒪\_𝒳), written out on the fppf site; only part (3) of Stacks 0771 is proved here. `hK` and `e` say that `Lg_! H` is represented by a complex whose TERMS are quasi-coherent (Stacks 03DL), the source's computation of `Lg_! H` from a free resolution, and `hqc` is Stacks 06WK, that a quasi-coherent module lies in LQCoh^fbc, which this library does not have in any form; the reduction of the general case to the affine case with a global presentation, by Stacks 07AQ and Stacks 07AV, is not carried out. The quasi-coherence hypothesis on `H` is the source's and is unweakened”.

> **Stacks 07B3 part (2), the flat base change property**: for a quasi-coherent module `H` on
> the flat-fppf site of `𝒳`, every cohomology sheaf of `Lg_! H` has the flat base change
> property.

```lean
theorem hasFlatBaseChange_homology_derivedModuleLowerShriek
    (hH : H.IsQuasicoherentOnSite)
    (hserre : ObjectProperty.IsWeakSerreClass
      (C := _root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳))
      (fun F => locallyQuasicoherentFlatBaseChangeRule B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids F.val))
    (hqc : ∀ F : _root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳),
      F.IsQuasicoherentOnSite → locallyQuasicoherentFlatBaseChangeRule B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids F.val)
    (hK : ∀ m : ℤ, (K.X m).IsQuasicoherentOnSite)
    (e : Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H) ≅ DerivedCategory.Q.obj K)
    (p : ℤ) :
    HasFlatBaseChangePropertyUnivLE B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      (etaleTopology B) (etaleTopology_le_topology B)
      ((DerivedCategory.homologyFunctor _ p).obj
        (Lg.obj ((DerivedCategory.singleFunctor _ 0).obj H))).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 104.3, Tag 08MZ](https://stacks.math.columbia.edu/tag/08MZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
