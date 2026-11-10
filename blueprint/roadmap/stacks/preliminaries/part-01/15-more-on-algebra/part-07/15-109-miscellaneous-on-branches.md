---
declaration: section
origin: cited
lean: comap_ne_bot_of_localization_or_discrete_fibers, exists_etale_away_of_isGeometricallyUnibranch_of_isUnramifiedAt, exists_etale_isLocalization_of_isGeometricallyUnibranch, minimalPrimes_strictHenselization_tensorProduct_bijOn
statement: formalized
proof: formalized
---

# 15.109 Miscellaneous on branches

Section 15.109 of the Stacks Project, [Tag 0GS4](https://stacks.math.columbia.edu/tag/0GS4). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GS5, a lemma

[Tag 0GS5](https://stacks.math.columbia.edu/tag/0GS5) in the Stacks Project.

**`comap_ne_bot_of_localization_or_discrete_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/UnibranchEtale.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/UnibranchEtale.lean#L153).

> Let `A → B` be a map of domains. Suppose that it is a localization of an étale
> map; or that it is flat and a localization of an unramified, quasi-finite, or integral
> map; or that it is flat and its fibers have no nontrivial specializations; or that it
> maps the generic point to the generic point and its fibers have no nontrivial
> specializations; or that exactly one point of `Spec(B)` maps to the generic point of
> `Spec(A)`. Then every nonzero ideal of `B` has nonzero contraction to `A`.

```lean
theorem comap_ne_bot_of_localization_or_discrete_fibers
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [Algebra A B]
    (h :
      (∃ (T : Type (max u v)) (_ : CommRing T) (_ : Algebra A T) (_ : Algebra T B)
          (_ : IsScalarTower A T B), Algebra.Etale A T ∧
            ∃ M : Submonoid T, IsLocalization M B) ∨
      (Module.Flat A B ∧
        ∃ (T : Type (max u v)) (_ : CommRing T) (_ : Algebra A T) (_ : Algebra T B)
          (_ : IsScalarTower A T B), Algebra.Unramified A T ∧
            ∃ M : Submonoid T, IsLocalization M B) ∨
      (Module.Flat A B ∧
        ∃ (T : Type (max u v)) (_ : CommRing T) (_ : Algebra A T) (_ : Algebra T B)
          (_ : IsScalarTower A T B), Algebra.QuasiFinite A T ∧
            ∃ M : Submonoid T, IsLocalization M B) ∨
      (Module.Flat A B ∧
        ∃ (T : Type (max u v)) (_ : CommRing T) (_ : Algebra A T) (_ : Algebra T B)
          (_ : IsScalarTower A T B), Algebra.IsIntegral A T ∧
            ∃ M : Submonoid T, IsLocalization M B) ∨
      (Module.Flat A B ∧ NoNontrivialSpecializationsInFibers A B) ∨
      ((⊥ : Ideal B).comap (algebraMap A B) = ⊥ ∧
        NoNontrivialSpecializationsInFibers A B) ∨
      (∃! q : Ideal B, q.IsPrime ∧ q.comap (algebraMap A B) = ⊥)) :
    ∀ J : Ideal B, J ≠ ⊥ → J.comap (algebraMap A B) ≠ ⊥
```

## Tag 0GSC, a lemma

[Tag 0GSC](https://stacks.math.columbia.edu/tag/0GSC) in the Stacks Project.

**`exists_etale_away_of_isGeometricallyUnibranch_of_isUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Miscellaneous/UnramifiedNeighborhood.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Miscellaneous/UnramifiedNeighborhood.lean#L251). References: EGA IV (18.10.1), “(i)+(ii) ⇒ étale”.

> Let `A → B` be a ring map from a domain, and let `q` be a prime of `B` lying over a prime
> `p` of `A`. If `Aₚ` is geometrically unibranch, the map is unramified at `q`, and the canonical
> map `Aₚ → B_q` is injective, then some principal localization `B_g`, with `g ∉ q`, is étale
> over `A`.

```lean
theorem exists_etale_away_of_isGeometricallyUnibranch_of_isUnramifiedAt
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B] [IsDomain A]
    (p : Ideal A) [p.IsPrime] (q : Ideal B) [q.IsPrime] [q.LiesOver p]
    (hgeom : IsGeometricallyUnibranch (Localization.AtPrime p))
    (hunram : ∃ f : B, f ∉ q ∧ Algebra.Unramified A (Localization.Away f))
    (hinj : letI := Localization.AtPrime.algebraOfLiesOver p q
      Function.Injective
        (algebraMap (Localization.AtPrime p) (Localization.AtPrime q))) :
    ∃ g : B, g ∉ q ∧ Algebra.Etale A (Localization.Away g)
```

## Tag 0GS6, a lemma

[Tag 0GS6](https://stacks.math.columbia.edu/tag/0GS6) in the Stacks Project.

**`exists_etale_isLocalization_of_isGeometricallyUnibranch`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/UnibranchEtale.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/UnibranchEtale.lean#L336). References: EGA IV (18.10.1), “(i)+(ii) ⇒ étale”; SGA 1 I (9.5), “(ii)”.

> **Stacks 0GS6.** An injective, essentially finite type local map from a geometrically
> unibranch local domain is a localization of an étale map when its target maximal ideal is
> extended from the source and its residue-field extension is separable.

```lean
theorem exists_etale_isLocalization_of_isGeometricallyUnibranch
    (A : Type u) (B : Type v)
    [CommRing A] [IsLocalRing A] [IsDomain A]
    [CommRing B] [IsLocalRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)] [Algebra.EssFiniteType A B]
    (hinjective : Function.Injective (algebraMap A B))
    (hunibranch : IsGeometricallyUnibranch A)
    (hmaximal : Ideal.map (algebraMap A B) (IsLocalRing.maximalIdeal A) =
      IsLocalRing.maximalIdeal B)
    (hseparable : Algebra.IsSeparable (IsLocalRing.ResidueField A)
      (IsLocalRing.ResidueField B)) :
    ∃ (C : Type (max u v)) (_ : CommRing C) (_ : Algebra A C)
      (_ : Algebra C B) (_ : IsScalarTower A C B) (M : Submonoid C),
        Algebra.Etale A C ∧ IsLocalization M B
```

## Tag 06DU, a lemma

[Tag 06DU](https://stacks.math.columbia.edu/tag/06DU) in the Stacks Project.

**`minimalPrimes_strictHenselization_tensorProduct_bijOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Branches/Miscellaneous/StrictHenselizationTensorProduct.lean, line 905](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Branches/Miscellaneous/StrictHenselizationTensorProduct.lean#L905).

> The minimal primes of the strict henselization of the localization of `A ⊗[k] B` at the
> maximal ideal induced by the residue maps correspond bijectively, by contraction, to pairs of
> minimal primes of `A` and `B`.

```lean
theorem minimalPrimes_strictHenselization_tensorProduct_bijOn
    (k A B : Type u) [Field k] [IsAlgClosed k]
    [CommRing A] [Algebra k A] [HenselianLocalRing A] [IsSepClosed (ResidueField A)]
    [CommRing B] [Algebra k B] [HenselianLocalRing B] [IsSepClosed (ResidueField B)]
    (resA : A →ₐ[k] k) (resB : B →ₐ[k] k)
    (hresA : RingHom.ker resA.toRingHom = maximalIdeal A)
    (hresB : RingHom.ker resB.toRingHom = maximalIdeal B)
    (R C : Type u) [CommRing R] [IsLocalRing R] [CommRing C] [IsLocalRing C]
    [Algebra (A ⊗[k] B) R]
    [IsLocalization
      (Submonoid.comap
        (Algebra.TensorProduct.lift resA resB (fun _ _ ↦ Commute.all _ _)).toRingHom
        (nonZeroDivisors k)) R]
    [Algebra R C]
    (ksep : Type v) [Field ksep] [Algebra (ResidueField R) ksep]
    [IsSepClosure (ResidueField R) ksep]
    [IsLocalRing.IsHenselization R ksep C] :
    Set.BijOn
      (fun q : Ideal C ↦
        (q.comap ((algebraMap R C).comp
          ((algebraMap (A ⊗[k] B) R).comp
            (Algebra.TensorProduct.includeLeft : A →ₐ[k] A ⊗[k] B).toRingHom)),
         q.comap ((algebraMap R C).comp
          ((algebraMap (A ⊗[k] B) R).comp
            (Algebra.TensorProduct.includeRight : B →ₐ[k] A ⊗[k] B).toRingHom))))
      (minimalPrimes C) ((minimalPrimes A) ×ˢ (minimalPrimes B))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.109, Tag 0GS4](https://stacks.math.columbia.edu/tag/0GS4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
