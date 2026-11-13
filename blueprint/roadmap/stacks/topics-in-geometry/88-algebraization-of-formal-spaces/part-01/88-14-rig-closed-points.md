---
declaration: section
origin: cited
lean: Rig.rigPoint_tfae, Rig.Ideal.IsRigPointLocalCondition, Rig.Ideal.IsRigClosed, Rig.exists_residueFieldMap_finiteType_of_rigPoint, Rig.rigPoint_relative_tfae, Rig.isRigPointLocalCondition_comap_of_isJacobsonRing_quotient, Rig.rigPoint_lifts_iff_maximalIdeal_mem_specialFibre_image, Rig.rigPoint_residueFieldMap_finite_of_lift
statement: formalized
proof: formalized
---

# 88.14 Rig-closed points

Section 88.14 of the Stacks Project, [Tag 0GG7](https://stacks.math.columbia.edu/tag/0GG7). 12 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GG8, a lemma

[Tag 0GG8](https://stacks.math.columbia.edu/tag/0GG8) in the Stacks Project.

**`Rig.rigPoint_tfae`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/RigPointCriterion.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/RigPointCriterion.lean#L514).

> The eight equivalent characterizations of a rig point in a Noetherian adic
> topological ring.

```lean
public lemma rigPoint_tfae {A : Type*} [CommRing A] [TopologicalSpace A]
    [IsTopologicalRing A] [IsNoetherianRing A]
    [@CompleteSpace A (IsTopologicalAddGroup.rightUniformSpace A)] [T2Space A]
    (_hadic : ∃ I : Ideal A, IsAdic I) (q : Ideal A) [q.IsPrime] :
    List.TFAE
      [ ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧
          Ideal.IsMaximalAmongPrimesAvoiding I q,
        ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧
          Ideal.IsClosedPointAwayFrom I q,
        ∀ I : Ideal A, TopologicalRing.IsIdealOfDefinition I →
          Ideal.IsMaximalAmongPrimesAvoiding I q,
        ∀ I : Ideal A, TopologicalRing.IsIdealOfDefinition I →
          Ideal.IsClosedPointAwayFrom I q,
        ringKrullDim (A ⧸ q) = 1 ∧
          ∃ I : Ideal A, TopologicalRing.IsIdealOfDefinition I ∧ ¬ I ≤ q,
        ringKrullDim (A ⧸ q) = 1 ∧
          ∀ I : Ideal A, TopologicalRing.IsIdealOfDefinition I → ¬ I ≤ q,
        ringKrullDim (A ⧸ q) = 1 ∧ ¬ DiscreteTopology (A ⧸ q),
          Ideal.IsRigPointLocalCondition q ]
```

## Tag 0GG9, a definition

[Tag 0GG9](https://stacks.math.columbia.edu/tag/0GG9) in the Stacks Project.

**`Rig.Ideal.IsRigPointLocalCondition`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/RigPointCriterion.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/RigPointCriterion.lean#L115). The attribute's comment: “rig-closed, via condition (8) of the rig-point criterion”.

> The local description in condition (8) of the rig-point criterion.  The
> topology and completeness on the quotient are the ones induced from `A`.

```lean
public abbrev Ideal.IsRigPointLocalCondition {A : Type*} [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A] (q : Ideal A) [q.IsPrime] : Prop
```

**`Rig.Ideal.IsRigClosed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/RigClosedPoint.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/RigClosedPoint.lean#L47).

> A prime `q` of a topological ring is *rig-closed* if some ideal of definition is not
> contained in `q` and `q` is maximal among the primes not containing it.

```lean
public def Ideal.IsRigClosed {A : Type u} [CommRing A] [TopologicalSpace A]
    (q : Ideal A) : Prop
```

## Tag 0GGA, a lemma

[Tag 0GGA](https://stacks.math.columbia.edu/tag/0GGA) in the Stacks Project.

**`Rig.exists_residueFieldMap_finiteType_of_rigPoint`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/RelativeCriterion.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/RelativeCriterion.lean#L99).

> The residue field at a rig-closed point is of finite type over the quotient
> of the source by its ideal of topologically nilpotent elements.

```lean
public lemma exists_residueFieldMap_finiteType_of_rigPoint
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    (q : Ideal B) [q.IsPrime]
    (hq : Ideal.IsRigPointLocalCondition q)
    (φ : A →+* B) (hφ : Continuous φ)
    (hfiniteType : (Ideal.quotientMap (I := topologicalNilradical A)
      (topologicalNilradical B) φ
      (by
        intro x hx
        exact IsTopologicallyNilpotent.map hφ
          (IsTopologicallyNilpotent.mem_topologicalNilradical_iff.mp hx))).FiniteType) :
    let _ : IsLocalRing (B ⧸ q) := hq.choose
    ∃ ψ : (A ⧸ topologicalNilradical A) →+* IsLocalRing.ResidueField (B ⧸ q),
      ψ.comp (Ideal.Quotient.mk (topologicalNilradical A)) =
        (IsLocalRing.residue (B ⧸ q)).comp ((Ideal.Quotient.mk q).comp φ) ∧
      ψ.FiniteType
```

## Tag 0GGB, a lemma

[Tag 0GGB](https://stacks.math.columbia.edu/tag/0GGB) in the Stacks Project.

**`Rig.rigPoint_relative_tfae`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/RelativeCriterion.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/RelativeCriterion.lean#L218).

> For an adic, topologically finite type morphism of Noetherian weakly
> admissible rings, a rig-closed prime upstairs satisfies the relative
> rig-closed point criterion.

```lean
public lemma rigPoint_relative_tfae {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hadic : RingHom.IsAdic φ)
    (hft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (q : Ideal B) [q.IsPrime]
    (hq : Ideal.IsClosedPointAwayFrom
      (topologicalNilradical B) q) :
    let a := topologicalNilradical A
    let p := q.comap φ
    List.TFAE
      [ ∃ hlocal : IsLocalRing (B ⧸ q),
          letI : IsLocalRing (B ⧸ q) := hlocal
          ∃ ψ : (A ⧸ a) →+* IsLocalRing.ResidueField (B ⧸ q),
            ψ.comp (Ideal.Quotient.mk a) =
                (IsLocalRing.residue (B ⧸ q)).comp
                  ((Ideal.Quotient.mk q).comp φ) ∧
              ψ.Finite,
        Ideal.IsClosedPointAwayFrom a p,
        (Ideal.quotientMap (I := p) q φ le_rfl).Finite ]
```

## Tag 0GGC, a lemma

[Tag 0GGC](https://stacks.math.columbia.edu/tag/0GGC) in the Stacks Project.

**`Rig.isRigPointLocalCondition_comap_of_isJacobsonRing_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/RelativeCriterion.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/RelativeCriterion.lean#L605).

> Under a Jacobson reduction of the source, the inverse image of a rig-closed
> prime along an adic topologically finite type morphism is rig-closed.

```lean
public theorem isRigPointLocalCondition_comap_of_isJacobsonRing_quotient
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hadic : RingHom.IsAdic φ)
    (hft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (q : Ideal B) [q.IsPrime]
    (hq : Ideal.IsRigPointLocalCondition q)
    (hJacobson : ∃ I : Ideal A,
      TopologicalRing.IsIdealOfDefinition I ∧ IsJacobsonRing (A ⧸ I)) :
    Ideal.IsRigPointLocalCondition (q.comap φ)
```

## Tag 0GGD, a lemma

[Tag 0GGD](https://stacks.math.columbia.edu/tag/0GGD) in the Stacks Project.

**`Rig.rigPoint_lifts_iff_maximalIdeal_mem_specialFibre_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L94). The attribute's comment: “lifting criterion”.

> A rig-closed prime lifts along a flat adic map of topologically finite type
> if and only if the closed point of its quotient is in the image on special
> fibres.

```lean
public theorem rigPoint_lifts_iff_maximalIdeal_mem_specialFibre_image
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hadic : RingHom.IsAdic φ)
    (hflat : φ.Flat)
    (p : Ideal A) [p.IsPrime]
    (hp : Ideal.IsClosedPointAwayFrom
      (topologicalNilradical A) p) :
    ( (∃ hlocal : IsLocalRing (A ⧸ p),
          letI : IsLocalRing (A ⧸ p) := hlocal
          ∃ r : Ideal B, r.IsPrime ∧
            topologicalNilradical B ≤ r ∧
            r.comap φ = (IsLocalRing.maximalIdeal (A ⧸ p)).comap
              (Ideal.Quotient.mk p)) ↔
      (∃ q : Ideal B, ∃ hqprime : q.IsPrime,
        letI : q.IsPrime := hqprime
        Ideal.IsClosedPointAwayFrom
          (topologicalNilradical B) q ∧ q.comap φ = p) )
```

**`Rig.rigPoint_residueFieldMap_finite_of_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L310). The attribute's comment: “relative residue-field finiteness”.

> At a rig-closed lift, the induced map from the reduction of `A` to the
> residue field of `B / q` is finite.

```lean
public theorem rigPoint_residueFieldMap_finite_of_lift
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hadic : RingHom.IsAdic φ)
    (hft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (p : Ideal A) [p.IsPrime]
    (hp : Ideal.IsClosedPointAwayFrom
      (topologicalNilradical A) p)
    (q : Ideal B) [q.IsPrime]
    (hq : Ideal.IsClosedPointAwayFrom
      (topologicalNilradical B) q)
    (hqp : q.comap φ = p) :
    ∃ hlocal : IsLocalRing (B ⧸ q),
      letI : IsLocalRing (B ⧸ q) := hlocal
      ∃ ψ : (A ⧸ topologicalNilradical A) →+*
          IsLocalRing.ResidueField (B ⧸ q),
        ψ.comp (Ideal.Quotient.mk (topologicalNilradical A)) =
            (IsLocalRing.residue (B ⧸ q)).comp
              ((Ideal.Quotient.mk q).comp φ) ∧ ψ.Finite
```

**`Rig.rigPoint_quotientMap_finite_of_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L340). The attribute's comment: “relative quotient finiteness”.

> At a rig-closed lift, the induced map on the quotients by the two primes
> is finite.

```lean
public theorem rigPoint_quotientMap_finite_of_lift
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hadic : RingHom.IsAdic φ)
    (hft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (p : Ideal A) [p.IsPrime]
    (hp : Ideal.IsClosedPointAwayFrom
      (topologicalNilradical A) p)
    (q : Ideal B) [q.IsPrime]
    (hq : Ideal.IsClosedPointAwayFrom
      (topologicalNilradical B) q)
    (hqp : q.comap φ = p) :
    (Ideal.quotientMap (I := p) q φ (by simpa only [← hqp] using le_rfl)).Finite
```

## Tag 0GGE, a definition

[Tag 0GGE](https://stacks.math.columbia.edu/tag/0GGE) in the Stacks Project.

**`Rig.exists_completedAway_algEquiv_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/CompletedPrincipalLocalization.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/CompletedPrincipalLocalization.lean#L74). The attribute's comment: “independence of the ideal of definition”.

> The completed principal localization is independent of the ideal of definition used to
> form it: for ideals of definition `I` and `J` the `I`-adic and `J`-adic completions of `A[1/f]`
> are isomorphic as `A`-algebras, compatibly with the maps from `A[1/f]`.

```lean
public theorem exists_completedAway_algEquiv_of {I J : Ideal A}
    (hI : TopologicalRing.IsIdealOfDefinition I)
    (hJ : TopologicalRing.IsIdealOfDefinition J) (f : A) :
    ∃ e : CompletedAway I f ≃ₐ[A] CompletedAway J f, ∀ x : Localization.Away f,
      e (AdicCompletion.of _ (Localization.Away f) x) =
        AdicCompletion.of _ (Localization.Away f) x
```

Declarations registered for the tag:

- [`CompletedAway`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CompletedAway#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Rig/CompletedPrincipalLocalization.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/CompletedPrincipalLocalization.lean#L39) (StacksFrontier): “the completed principal localization, along a chosen ideal”.

## Tag 0GGF, a lemma

[Tag 0GGF](https://stacks.math.columbia.edu/tag/0GGF) in the Stacks Project.

**`Rig.tensorProduct_equiv_extendedIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L652). The attribute's comment: “tensor-product description”.

> Extension of scalars of `p` to the completed principal localization is canonically its
> extended ideal.

```lean
public theorem tensorProduct_equiv_extendedIdeal
    (I p : Ideal A) (f : A) [IsNoetherianRing A] :
    ∃ e : (CompletedAway I f ⊗[A] p) ≃ₗ[CompletedAway I f] extendedIdeal I p f,
      ∀ (x : p) (c : CompletedAway I f),
        ((e (c ⊗ₜ[A] x) : extendedIdeal I p f) : CompletedAway I f) =
          algebraMap A (CompletedAway I f) (x : A) * c
```

**`Rig.adicCompletion_localizedIdeal_equiv_extendedIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 666](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L666). The attribute's comment: “completion description”.

> Completing the localized ideal `p A[1/f]` gives its extension to the completed principal
> localization, compatibly with the canonical maps.

```lean
public theorem adicCompletion_localizedIdeal_equiv_extendedIdeal
    (I p : Ideal A) (f : A) [IsNoetherianRing A] :
    let A_f := Localization.Away f
    let J := I.map (algebraMap A A_f)
    let p_f := p.map (algebraMap A A_f)
    ∃ e : AdicCompletion J p_f ≃ₗ[A_f] extendedIdeal I p f,
      ∀ x : p_f,
        ((e (AdicCompletion.of J p_f x) : extendedIdeal I p f) : CompletedAway I f) =
          algebraMap A_f (CompletedAway I f) (x : A_f)
```

**`Rig.extendedIdeal_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 706](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L706). The attribute's comment: “primality”.

> The extension of `p` to the completed principal localization is prime.

```lean
public theorem extendedIdeal_isPrime
    (I p : Ideal A) (f : A) [IsNoetherianRing A] [IsAdicComplete I A]
    (hp : p.IsPrime)
    (hf : IsUnit (Ideal.Quotient.mk p f)) :
    (extendedIdeal I p f).IsPrime
```

**`Rig.quotient_extendedIdeal_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 720](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L720). The attribute's comment: “quotient”.

> Quotienting the completed principal localization by the extended prime canonically recovers
> `A / p`.

```lean
public theorem quotient_extendedIdeal_equiv
    (I p : Ideal A) (f : A) [IsNoetherianRing A] [IsAdicComplete I A]
    (hf : IsUnit (Ideal.Quotient.mk p f)) :
    ∃ e : (A ⧸ p) ≃+* (CompletedAway I f ⧸ extendedIdeal I p f),
      ∀ a : A,
        e (Ideal.Quotient.mk p a) =
          Ideal.Quotient.mk (extendedIdeal I p f)
            (algebraMap A (CompletedAway I f) a)
```

Declarations registered for the tag:

- [`Ideal.quotMapEquivTensorQuot`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.quotMapEquivTensorQuot#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 747](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L747) (StacksFrontier): “tensor-product description of the quotient”.
- [`Ideal.map_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.map_map#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean, line 752](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/LiftingAndCompletedAway.lean#L752) (StacksFrontier): “transitivity of ideal extension”.

## Tag 0GGG, a lemma

[Tag 0GGG](https://stacks.math.columbia.edu/tag/0GGG) in the Stacks Project.

**`Rig.exists_isClosedPointAwayFrom_completedAway_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean, line 1388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean#L1388).

> After a suitable completed principal localization, the prime below a
> rig-closed point is rig-closed as well.

```lean
public theorem exists_isClosedPointAwayFrom_completedAway_comap
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hadic : RingHom.IsAdic φ)
    (hft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (q : Ideal B) [q.IsPrime]
    (hq : Ideal.IsClosedPointAwayFrom
      (topologicalNilradical B) q) :
    let I := hadic.choose
    let J := I.map φ
    ∃ f : A,
      IsUnit (Ideal.Quotient.mk q (φ f)) ∧
        (let A_f := CompletedAway I f
         let B_f := CompletedAway J (φ f)
         let ψ : A_f →+* B_f := RingHom.completedAwayMap φ I f
         let I_f := I.map (algebraMap A (Localization.Away f))
         let J_f := J.map (algebraMap B (Localization.Away (φ f)))
         let I_hat := I_f.map (algebraMap (Localization.Away f) A_f)
         let J_hat := J_f.map (algebraMap (Localization.Away (φ f)) B_f)
         let q' := extendedIdeal J q (φ f)
         let p' := q'.comap ψ
         ψ.comp (algebraMap A A_f) = (algebraMap B B_f).comp φ ∧
           (∃ hqprime : q'.IsPrime,
             letI : q'.IsPrime := hqprime
             ∃ hpprime : p'.IsPrime,
               letI : p'.IsPrime := hpprime
               Ideal.IsClosedPointAwayFrom J_hat q' ∧
                 Ideal.IsClosedPointAwayFrom I_hat p'))
```

## Tag 0GGH, a lemma

[Tag 0GGH](https://stacks.math.columbia.edu/tag/0GGH) in the Stacks Project.

**`Rig.adicCompletionMap_localRingHom_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/RestrictedPowerSeries.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/RestrictedPowerSeries.lean#L453).

> Let `A` be a Noetherian adic topological ring, complete for an ideal of definition `I`, and
> let `q` be a prime of the restricted power series ring `A{x_σ}` in finitely many variables.  If
> `q` is rig-closed and so is its contraction to `A`, then the canonical map from the local ring of
> the polynomial ring at `q ∩ A[x_σ]` to the local ring of `A{x_σ}` at `q` induces a bijection on
> the completions at the maximal ideals.

```lean
public theorem adicCompletionMap_localRingHom_bijective
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsNoetherianRing A] (I : Ideal A) (hI : IsAdic I) [IsAdicComplete I A]
    (σ : Type*) [Finite σ]
    (q : Ideal (RestrictedPowerSeries I σ)) [q.IsPrime]
    (hq : Ideal.IsClosedPointAwayFrom (I.map (coefficientRingHom I σ)) q)
    (hp : Ideal.IsClosedPointAwayFrom I (q.comap (coefficientRingHom I σ))) :
    let f := polynomialRingHom I σ
    let q' := q.comap f
    let l := Localization.localRingHom q' q f rfl
    Function.Bijective
      (adicCompletionMap l
        (IsLocalRing.maximalIdeal (Localization.AtPrime q'))
        (IsLocalRing.maximalIdeal (Localization.AtPrime q))
        (IsLocalRing.map_maximalIdeal_le l))
```

## Tag 0GGI, a lemma

[Tag 0GGI](https://stacks.math.columbia.edu/tag/0GGI) in the Stacks Project.

**`Rig.map_comap_eq_map_of_rigPoint_of_etale_quotient`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/EtaleReduction.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/EtaleReduction.lean#L105).

> **Stacks 0GGI.** Let `φ : A → B` be an adic morphism of Noetherian weakly admissible
> topological rings which is topologically of finite type and flat and whose reduction modulo an
> ideal of definition `I ⊆ A` is étale.  If `q ⊆ B` is a rig-closed prime whose contraction to `A`
> is rig-closed as well, then the extension of that contraction to the local ring of `B` at `q` is
> the extension of `q` itself.

```lean
public lemma map_comap_eq_map_of_rigPoint_of_etale_quotient
    {A B : Type*} [CommRing A] [CommRing B]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace B] [IsTopologicalRing B] [IsLinearTopology B B]
    [IsNoetherianRing A] [IsNoetherianRing B]
    (_hA : TopologicalRing.IsWeaklyAdmissible A)
    (hB : TopologicalRing.IsWeaklyAdmissible B)
    (φ : A →+* B) (hφ : Continuous φ)
    (hadic : RingHom.IsAdic φ)
    (_hft : TopologicalRing.IsTopologicallyOfFiniteType φ)
    (hflat : φ.Flat)
    (I : Ideal A) (hI : TopologicalRing.IsIdealOfDefinition I)
    (hetale : (Ideal.quotientMap (I.map φ) φ Ideal.le_comap_map).Etale)
    (q : Ideal B) [q.IsPrime]
    (_hq : Ideal.IsRigPointLocalCondition q)
    (hp : Ideal.IsRigPointLocalCondition (q.comap φ)) :
    (q.comap φ).map ((algebraMap B (Localization.AtPrime q)).comp φ) =
      q.map (algebraMap B (Localization.AtPrime q))
```

## Tag 0GGJ, a lemma

[Tag 0GGJ](https://stacks.math.columbia.edu/tag/0GGJ) in the Stacks Project.

**`Rig.restrictedPowerSeriesBaseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean#L400). The attribute's comment: “regular\_map”.

> Base change of a restricted power series ring by a rig-closed quotient is
> canonically the restricted power series ring over that quotient.

```lean
public noncomputable def restrictedPowerSeriesBaseChangeEquiv
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsNoetherianRing A]
    (_hA : TopologicalRing.IsAdic A)
    (I : Ideal A) (_hI : TopologicalRing.IsIdealOfDefinition I)
    (p : Ideal A) [p.IsPrime]
    (_hp : Ideal.IsRigPointLocalCondition p)
    (n : ℕ) (_hn : 1 ≤ n) :
    letI : Algebra (A ⧸ p)
      (RestrictedPowerSeries I (Fin n) ⊗[A] (A ⧸ p)) :=
      Algebra.TensorProduct.rightAlgebra
    (RestrictedPowerSeries I (Fin n) ⊗[A] (A ⧸ p)) ≃ₐ[A ⧸ p]
      RestrictedPowerSeries (I.map (Ideal.Quotient.mk p)) (Fin n)
```

**`Rig.restrictedPowerSeriesBaseChangeEquiv_coefficientProjection`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean#L428). The attribute's comment: “regular\_map”.

> At every finite level, the base-change identification reduces a series
> coefficientwise modulo `p`. The polynomial `g` is any lift of that level's
> coefficient polynomial, so the equation also asserts independence of lifts.

```lean
public lemma restrictedPowerSeriesBaseChangeEquiv_coefficientProjection
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsNoetherianRing A]
    (hA : TopologicalRing.IsAdic A)
    (I : Ideal A) (hI : TopologicalRing.IsIdealOfDefinition I)
    (p : Ideal A) [p.IsPrime]
    (hp : Ideal.IsRigPointLocalCondition p)
    (n : ℕ) (hn : 1 ≤ n) (k : ℕ)
    (f : RestrictedPowerSeries I (Fin n))
    (g : MvPolynomial (Fin n) A)
    (hg : RestrictedPowerSeries.coefficientProjection I (Fin n) k f =
      MvPolynomial.map (Ideal.Quotient.mk (I ^ k)) g) :
    letI : Algebra (A ⧸ p)
      (RestrictedPowerSeries I (Fin n) ⊗[A] (A ⧸ p)) :=
      Algebra.TensorProduct.rightAlgebra
    RestrictedPowerSeries.coefficientProjection
      (I.map (Ideal.Quotient.mk p)) (Fin n) k
      (restrictedPowerSeriesBaseChangeEquiv hA I hI p hp n hn
        ((Algebra.TensorProduct.includeLeftRingHom :
            RestrictedPowerSeries I (Fin n) →+*
              (RestrictedPowerSeries I (Fin n) ⊗[A] (A ⧸ p))) f)) =
      MvPolynomial.map (Ideal.Quotient.mk
        ((I.map (Ideal.Quotient.mk p)) ^ k))
        (MvPolynomial.map (Ideal.Quotient.mk p) g)
```

**`Rig.isRegularRingHom_baseChange_of_rigPoint`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean, line 510](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean#L510). The attribute's comment: “regular\_map”.

> The canonical map from the rig-closed quotient to the base-changed
> restricted power series ring is regular.

```lean
public lemma isRegularRingHom_baseChange_of_rigPoint
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsNoetherianRing A]
    (_hA : TopologicalRing.IsAdic A)
    (I : Ideal A) (_hI : TopologicalRing.IsIdealOfDefinition I)
    (p : Ideal A) [p.IsPrime]
    (_hp : Ideal.IsRigPointLocalCondition p)
    (n : ℕ) (_hn : 1 ≤ n) :
    letI : Algebra (A ⧸ p)
      (RestrictedPowerSeries I (Fin n) ⊗[A] (A ⧸ p)) :=
      Algebra.TensorProduct.rightAlgebra
    IsRegularRingHom (algebraMap (A ⧸ p)
      (RestrictedPowerSeries I (Fin n) ⊗[A] (A ⧸ p)))
```

**`Rig.isGeometricallyRegular_fibre`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Rig/ClosedPoint/Regular.lean#L592). The attribute's comment: “geometrically\_regular\_fibre”.

> The fibre of a restricted power series algebra at a rig-closed prime is
> geometrically regular over the residue field.

```lean
public lemma isGeometricallyRegular_fibre
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsNoetherianRing A]
    (_hA : TopologicalRing.IsAdic A)
    (I : Ideal A) (_hI : IsAdic I)
    (p : Ideal A) [p.IsPrime]
    (_hp : Ideal.IsRigPointLocalCondition p)
    (n : ℕ) (_hn : 0 < n) :
    letI : Algebra p.ResidueField
      (RestrictedPowerSeries I (Fin n) ⊗[A]
        p.ResidueField) := Algebra.TensorProduct.rightAlgebra
    Algebra.IsGeometricallyRegular p.ResidueField
      (RestrictedPowerSeries I (Fin n) ⊗[A]
        p.ResidueField)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.14, Tag 0GG7](https://stacks.math.columbia.edu/tag/0GG7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
