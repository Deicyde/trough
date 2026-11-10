---
declaration: section
origin: cited
lean: Crystalline.pAdicCompletedDividedPowerEnvelope, Crystalline.pAdicCompletedDividedPowerDifferentials, Crystalline.pAdicCompletedDividedPowerDifferentialsEquivLimit, Crystalline.pAdicCompletedDividedPowerDifferentialsEquivCompletion, Crystalline.exists_dividedPowerDifferentialsCompletionEquiv, Crystalline.completedDividedPowerDifferential, Crystalline.pAdicCompletedTensorPowerEnvelope, Crystalline.exists_ringEquiv_pAdicCompletedDividedPowerPolynomial
statement: formalized
proof: formalized
---

# 60.17 Crystals in quasi-coherent modules

Section 60.17 of the Stacks Project, [Tag 07J7](https://stacks.math.columbia.edu/tag/07J7). 17 tags here are carried by 24 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07J8, an equation

[Tag 07J8](https://stacks.math.columbia.edu/tag/07J8) in the Stacks Project.

**`Crystalline.pAdicCompletedDividedPowerEnvelope`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Crystal.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Crystal.lean#L85).

> The `p`-adically completed divided power envelope of the kernel of a
> surjective polynomial presentation of `C` over `A`.

```lean
public noncomputable abbrev pAdicCompletedDividedPowerEnvelope
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) (_hf : Function.Surjective f) : Type (max u w)
```

## Tag 07J9, an equation

[Tag 07J9](https://stacks.math.columbia.edu/tag/07J9) in the Stacks Project.

**`Crystalline.pAdicCompletedDividedPowerDifferentials`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean#L307).

> The module `Ω_D`: the `p`-adic completion of the module of divided power differentials of
> the divided power envelope of a polynomial presentation of `C` over `A`.

```lean
public noncomputable abbrev pAdicCompletedDividedPowerDifferentials
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) : Type (max u w)
```

**`Crystalline.pAdicCompletedDividedPowerDifferentialsEquivLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean#L328). The attribute's comment: “the inverse limit over the finite levels”.

> **Stacks 07J9, the first identification.** `Ω_D = lim_e Ω_{D_e/A, γ̄}`: the completed module
> of divided power differentials is the inverse limit of the modules of divided power
> differentials of the finite levels `D_e`.

```lean
public noncomputable def pAdicCompletedDividedPowerDifferentialsEquivLimit
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) :
    pAdicCompletedDividedPowerDifferentials s f ≃+
      ((limit (QuotientDifferentialsSystem.functor (A := s.A)
          (polynomialDividedPowerEnvelopeRing s f).ideal
          (polynomialDividedPowerEnvelopeRing s f).dividedPowers s.p
          (presentationDifferentialsCompletionComparison s f).quotientSystem) :
        AddCommGrpCat) : Type (max u w))
```

**`Crystalline.pAdicCompletedDividedPowerDifferentialsEquivCompletion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean#L343). The attribute's comment: “the p-adic completion of the differentials of the completed envelope”.

> **Stacks 07J9, the second identification.** `Ω_D = lim_e Ω_{D/A, γ̄}/p^eΩ_{D/A, γ̄}`: the
> completed module of divided power differentials is also the `p`-adic completion of the module
> of divided power differentials of the completed envelope `D` itself.

```lean
public noncomputable def pAdicCompletedDividedPowerDifferentialsEquivCompletion
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) :
    pAdicCompletedDividedPowerDifferentials s f ≃+
      AdicCompletion
        (DividedPowers.pAdicIdeal
          (A := AdicCompletion
            (DividedPowers.pAdicIdeal (A := polynomialDividedPowerEnvelopeRing s f) s.p)
            (polynomialDividedPowerEnvelopeRing s f)) s.p)
        (dividedPowerDifferentials (A := s.A)
          (DividedPowers.completedDividedPowers (polynomialDividedPowerEnvelopeRing s f).ideal
            (polynomialDividedPowerEnvelopeRing s f).dividedPowers s.p
            (polynomialDividedPowerEnvelope_prime_nilpotent s f)).1)
```

**`Crystalline.exists_dividedPowerDifferentialsCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Completion.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Completion.lean#L722). The attribute's comment: “the identification of the inverse limits that defines Ω_D, the case B = D”.

> Let `A → B` be a ring map, let `(J, δ)` be a divided power structure on `B`, let `p` be
> prime, let `A` be a `ℤ_(p)`-algebra and let `p` be nilpotent in `B / J`.  Then
> `lim_e Ω_{B_e/A, δ̄} = lim_e Ω_{B/A, δ} / pᵉ Ω_{B/A, δ}
>   = lim_e Ω_{B^∧/A, δ^∧} / pᵉ Ω_{B^∧/A, δ^∧}`.
>
> The conclusion is written out here, with no reference to
> `Crystalline.DifferentialsCompletionComparison`.  Beyond a level `N`, each `pᵉ B` lies in `J` and
> is stable under the divided powers of `δ` (`level`), so `B_e = B / pᵉ B` carries divided powers
> `δ̄` and the modules `Ω_{B_e/A, δ̄} = Crystalline.quotientDifferentials ..` form an inverse system
> whose transition maps are those induced on universal differentials (`transition`, and the first
> conjunct).  The second and third limits are Mathlib's `AdicCompletion`s of `Ω_{B/A, δ}` and of
> `Ω_{B^∧/A, δ^∧}`; `fromOriginal` and `fromCompletion` identify every level of their towers of
> quotients with that system, compatibly with all three families of transition maps, which is the
> first equality in the strong form of an isomorphism of inverse systems.  `limitEquiv` is the
> isomorphism of the second limit with the third that results, and the last conjunct says its
> component at each level `N + e` is `fromOriginal` followed by the inverse of `fromCompletion`.

```lean
public theorem exists_dividedPowerDifferentialsCompletionEquiv
    [Fact p.Prime] [Algebra (DividedPowers.IntegersAtPrime p) A]
    (hp : IsNilpotent (Ideal.Quotient.mk J (p : B))) :
    ∃ (N : ℕ)
      (level : ∀ e, N ≤ e → (DividedPowers.pAdicIdeal (A := B) p ^ e ≤ J) ∧
        delta.IsSubDPIdeal (DividedPowers.pAdicIdeal (A := B) p ^ e))
      (transition : ∀ e e' : ℕ, e ≤ e' →
        quotientDifferentials (A := A) J delta p (N + e')
            (level _ (Nat.le_add_right N e')).1 (level _ (Nat.le_add_right N e')).2 →+
          quotientDifferentials (A := A) J delta p (N + e)
            (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (fromOriginal : ∀ e : ℕ, differentialsModPow (A := A) J delta p (N + e) ≃ₗ[B]
        quotientDifferentials (A := A) J delta p (N + e)
          (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (fromCompletion : ∀ e : ℕ,
        completedDifferentialsModPow (A := A) J delta p hp (N + e) ≃+
          quotientDifferentials (A := A) J delta p (N + e)
            (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (limitEquiv : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p)
            (dividedPowerDifferentials (A := A) delta) ≃+
          AdicCompletion
            (DividedPowers.pAdicIdeal
              (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
            (dividedPowerDifferentials (A := A)
              (DividedPowers.completedDividedPowers J delta p hp).1)),
      (∀ (e e' : ℕ) (h : e ≤ e') (b : B),
          transition e e' h
              (dividedPowerDifferential (A := A)
                (DividedPowers.quotientDividedPowers J delta p (N + e')
                  (level _ (Nat.le_add_right N e')).1 (level _ (Nat.le_add_right N e')).2)
                (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e')) b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e)) b)) ∧
      (∀ (e : ℕ) (b : B),
          fromOriginal e
              (Submodule.Quotient.mk (dividedPowerDifferential (A := A) delta b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e)) b)) ∧
      (∀ (e e' : ℕ) (h : e ≤ e')
          (omega : differentialsModPow (A := A) J delta p (N + e')),
          transition e e' h (fromOriginal e' omega) =
            fromOriginal e
              (AdicCompletion.transitionMap (DividedPowers.pAdicIdeal (A := B) p)
                (dividedPowerDifferentials (A := A) delta)
                (Nat.add_le_add_left h N) omega)) ∧
      (∀ (e : ℕ) (b : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B),
          fromCompletion e
              (Submodule.Quotient.mk
                (dividedPowerDifferential (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1 b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (AdicCompletion.evalₐ (DividedPowers.pAdicIdeal (A := B) p) (N + e) b)) ∧
      (∀ (e : ℕ) (b : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B)
          (omega : completedDifferentialsModPow (A := A) J delta p hp (N + e)),
          fromCompletion e (b • omega) =
            AdicCompletion.evalₐ (DividedPowers.pAdicIdeal (A := B) p) (N + e) b •
              fromCompletion e omega) ∧
      (∀ (e e' : ℕ) (h : e ≤ e')
          (omega : completedDifferentialsModPow (A := A) J delta p hp (N + e')),
          transition e e' h (fromCompletion e' omega) =
            fromCompletion e
              (AdicCompletion.transitionMap
                (DividedPowers.pAdicIdeal
                  (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
                (dividedPowerDifferentials (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1)
                (Nat.add_le_add_left h N) omega)) ∧
      (∀ (e : ℕ) (omega : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p)
            (dividedPowerDifferentials (A := A) delta)),
          fromCompletion e
              (AdicCompletion.eval
                (DividedPowers.pAdicIdeal
                  (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
                (dividedPowerDifferentials (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1)
                (N + e) (limitEquiv omega)) =
            fromOriginal e
              (AdicCompletion.eval (DividedPowers.pAdicIdeal (A := B) p)
                (dividedPowerDifferentials (A := A) delta) (N + e) omega))
```

## Tag 07JA, an equation

[Tag 07JA](https://stacks.math.columbia.edu/tag/07JA) in the Stacks Project.

**`Crystalline.completedDividedPowerDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean#L175).

> The universal divided power derivation of the completed envelope, characterized
> on the dense image of the original envelope.

```lean
public noncomputable def completedDividedPowerDifferential
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) (hf : Function.Surjective f) :
    let env := polynomialDividedPowerEnvelope s f
    let E := env.object
    letI : Algebra s.A E := env.structureMap.toRingHom.toAlgebra
    let P := DividedPowers.pAdicIdeal (A := E) s.p
    let Ω := AdicCompletion P (dividedPowerDifferentials (A := s.A) E.dividedPowers)
    Σ' hp : IsNilpotent (Ideal.Quotient.mk E.ideal (s.p : E)),
      let D := DividedPowerRing.of
        (pAdicCompletedDividedPowerEnvelope s f hf)
        (DividedPowers.completionIdeal E.ideal s.p hp)
        (DividedPowers.completedDividedPowers E.ideal E.dividedPowers s.p hp).1
      letI : Algebra s.A D :=
        ((algebraMap E D).comp env.structureMap.toRingHom).toAlgebra
      { d : DividedPowerDerivation s.A D (algebraMap s.A D) Ω //
        ∀ b : E, d (algebraMap E D b) =
          AdicCompletion.of P (dividedPowerDifferentials (A := s.A) E.dividedPowers)
            (dividedPowerDifferential (A := s.A) E.dividedPowers b) }
```

## Tag 07JF, an equation

[Tag 07JF](https://stacks.math.columbia.edu/tag/07JF) in the Stacks Project.

**`Crystalline.pAdicCompletedTensorPowerEnvelope`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Crystal.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Crystal.lean#L150).

> The ring `D(n)`: the `p`-adically completed divided power envelope of the kernel `J(n)`
> of the surjection `P ⊗_A … ⊗_A P → C` on the `(n + 1)`-fold tensor power of a surjective
> polynomial presentation of `C` over `A`.

```lean
public noncomputable abbrev pAdicCompletedTensorPowerEnvelope
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) (hf : Function.Surjective f) (n : ℕ) :
    Type (max u w)
```

## Tag 07L0, an equation

[Tag 07L0](https://stacks.math.columbia.edu/tag/07L0) in the Stacks Project.

**`Crystalline.exists_dividedPowerDifferentialsCompletionEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Completion.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/ModuleDifferentials/Completion.lean#L722). The attribute's comment: “the same identification of the limits, read at the divided power envelope D(n)”.

> Let `A → B` be a ring map, let `(J, δ)` be a divided power structure on `B`, let `p` be
> prime, let `A` be a `ℤ_(p)`-algebra and let `p` be nilpotent in `B / J`.  Then
> `lim_e Ω_{B_e/A, δ̄} = lim_e Ω_{B/A, δ} / pᵉ Ω_{B/A, δ}
>   = lim_e Ω_{B^∧/A, δ^∧} / pᵉ Ω_{B^∧/A, δ^∧}`.
>
> The conclusion is written out here, with no reference to
> `Crystalline.DifferentialsCompletionComparison`.  Beyond a level `N`, each `pᵉ B` lies in `J` and
> is stable under the divided powers of `δ` (`level`), so `B_e = B / pᵉ B` carries divided powers
> `δ̄` and the modules `Ω_{B_e/A, δ̄} = Crystalline.quotientDifferentials ..` form an inverse system
> whose transition maps are those induced on universal differentials (`transition`, and the first
> conjunct).  The second and third limits are Mathlib's `AdicCompletion`s of `Ω_{B/A, δ}` and of
> `Ω_{B^∧/A, δ^∧}`; `fromOriginal` and `fromCompletion` identify every level of their towers of
> quotients with that system, compatibly with all three families of transition maps, which is the
> first equality in the strong form of an isomorphism of inverse systems.  `limitEquiv` is the
> isomorphism of the second limit with the third that results, and the last conjunct says its
> component at each level `N + e` is `fromOriginal` followed by the inverse of `fromCompletion`.

```lean
public theorem exists_dividedPowerDifferentialsCompletionEquiv
    [Fact p.Prime] [Algebra (DividedPowers.IntegersAtPrime p) A]
    (hp : IsNilpotent (Ideal.Quotient.mk J (p : B))) :
    ∃ (N : ℕ)
      (level : ∀ e, N ≤ e → (DividedPowers.pAdicIdeal (A := B) p ^ e ≤ J) ∧
        delta.IsSubDPIdeal (DividedPowers.pAdicIdeal (A := B) p ^ e))
      (transition : ∀ e e' : ℕ, e ≤ e' →
        quotientDifferentials (A := A) J delta p (N + e')
            (level _ (Nat.le_add_right N e')).1 (level _ (Nat.le_add_right N e')).2 →+
          quotientDifferentials (A := A) J delta p (N + e)
            (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (fromOriginal : ∀ e : ℕ, differentialsModPow (A := A) J delta p (N + e) ≃ₗ[B]
        quotientDifferentials (A := A) J delta p (N + e)
          (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (fromCompletion : ∀ e : ℕ,
        completedDifferentialsModPow (A := A) J delta p hp (N + e) ≃+
          quotientDifferentials (A := A) J delta p (N + e)
            (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
      (limitEquiv : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p)
            (dividedPowerDifferentials (A := A) delta) ≃+
          AdicCompletion
            (DividedPowers.pAdicIdeal
              (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
            (dividedPowerDifferentials (A := A)
              (DividedPowers.completedDividedPowers J delta p hp).1)),
      (∀ (e e' : ℕ) (h : e ≤ e') (b : B),
          transition e e' h
              (dividedPowerDifferential (A := A)
                (DividedPowers.quotientDividedPowers J delta p (N + e')
                  (level _ (Nat.le_add_right N e')).1 (level _ (Nat.le_add_right N e')).2)
                (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e')) b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e)) b)) ∧
      (∀ (e : ℕ) (b : B),
          fromOriginal e
              (Submodule.Quotient.mk (dividedPowerDifferential (A := A) delta b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := B) p ^ (N + e)) b)) ∧
      (∀ (e e' : ℕ) (h : e ≤ e')
          (omega : differentialsModPow (A := A) J delta p (N + e')),
          transition e e' h (fromOriginal e' omega) =
            fromOriginal e
              (AdicCompletion.transitionMap (DividedPowers.pAdicIdeal (A := B) p)
                (dividedPowerDifferentials (A := A) delta)
                (Nat.add_le_add_left h N) omega)) ∧
      (∀ (e : ℕ) (b : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B),
          fromCompletion e
              (Submodule.Quotient.mk
                (dividedPowerDifferential (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1 b)) =
            dividedPowerDifferential (A := A)
              (DividedPowers.quotientDividedPowers J delta p (N + e)
                (level _ (Nat.le_add_right N e)).1 (level _ (Nat.le_add_right N e)).2)
              (AdicCompletion.evalₐ (DividedPowers.pAdicIdeal (A := B) p) (N + e) b)) ∧
      (∀ (e : ℕ) (b : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B)
          (omega : completedDifferentialsModPow (A := A) J delta p hp (N + e)),
          fromCompletion e (b • omega) =
            AdicCompletion.evalₐ (DividedPowers.pAdicIdeal (A := B) p) (N + e) b •
              fromCompletion e omega) ∧
      (∀ (e e' : ℕ) (h : e ≤ e')
          (omega : completedDifferentialsModPow (A := A) J delta p hp (N + e')),
          transition e e' h (fromCompletion e' omega) =
            fromCompletion e
              (AdicCompletion.transitionMap
                (DividedPowers.pAdicIdeal
                  (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
                (dividedPowerDifferentials (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1)
                (Nat.add_le_add_left h N) omega)) ∧
      (∀ (e : ℕ) (omega : AdicCompletion (DividedPowers.pAdicIdeal (A := B) p)
            (dividedPowerDifferentials (A := A) delta)),
          fromCompletion e
              (AdicCompletion.eval
                (DividedPowers.pAdicIdeal
                  (A := AdicCompletion (DividedPowers.pAdicIdeal (A := B) p) B) p)
                (dividedPowerDifferentials (A := A)
                  (DividedPowers.completedDividedPowers J delta p hp).1)
                (N + e) (limitEquiv omega)) =
            fromOriginal e
              (AdicCompletion.eval (DividedPowers.pAdicIdeal (A := B) p)
                (dividedPowerDifferentials (A := A) delta) (N + e) omega))
```

## Tag 07L1, an equation

[Tag 07L1](https://stacks.math.columbia.edu/tag/07L1) in the Stacks Project.

**`Crystalline.completedDividedPowerDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsQuasiCoherent/Basic.lean#L175). The attribute's comment: “the same derivation for the (n+1)-fold tensor-product presentation”.

> The universal divided power derivation of the completed envelope, characterized
> on the dense image of the original envelope.

```lean
public noncomputable def completedDividedPowerDifferential
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) (hf : Function.Surjective f) :
    let env := polynomialDividedPowerEnvelope s f
    let E := env.object
    letI : Algebra s.A E := env.structureMap.toRingHom.toAlgebra
    let P := DividedPowers.pAdicIdeal (A := E) s.p
    let Ω := AdicCompletion P (dividedPowerDifferentials (A := s.A) E.dividedPowers)
    Σ' hp : IsNilpotent (Ideal.Quotient.mk E.ideal (s.p : E)),
      let D := DividedPowerRing.of
        (pAdicCompletedDividedPowerEnvelope s f hf)
        (DividedPowers.completionIdeal E.ideal s.p hp)
        (DividedPowers.completedDividedPowers E.ideal E.dividedPowers s.p hp).1
      letI : Algebra s.A D :=
        ((algebraMap E D).comp env.structureMap.toRingHom).toAlgebra
      { d : DividedPowerDerivation s.A D (algebraMap s.A D) Ω //
        ∀ b : E, d (algebraMap E D b) =
          AdicCompletion.of P (dividedPowerDifferentials (A := s.A) E.dividedPowers)
            (dividedPowerDifferential (A := s.A) E.dividedPowers b) }
```

## Tag 07L2, a lemma

[Tag 07L2](https://stacks.math.columbia.edu/tag/07L2) in the Stacks Project.

**`Crystalline.exists_ringEquiv_pAdicCompletedDividedPowerPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/TensorPowerEnvelope.lean, line 1347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/TensorPowerEnvelope.lean#L1347).

> **Stacks Project, Lemma 60.17.5, Tag 07L2.** Let `D` and `D(n)` be as in (07J8) and
> (07JF).  The coprojection `P → P ⊗_A … ⊗_A P`, `h ↦ h ⊗ 1 ⊗ … ⊗ 1` induces an isomorphism
>
> `D(n) = lim_e D⟨ξ_i(j)⟩/p^e D⟨ξ_i(j)⟩`
>
> of algebras over `D`, with `ξ_i(j) = x_i ⊗ 1 ⊗ … ⊗ 1 - 1 ⊗ … ⊗ 1 ⊗ x_i ⊗ 1 ⊗ … ⊗ 1` for
> `j = 1, …, n`, where the second `x_i` is placed in the `(j + 1)`-st slot.
>
> The map `φ` induced by the coprojection is the algebra structure of `D(n)` over `D`: it
> agrees with the coprojection on the image of `P`.  The isomorphism `e` is an isomorphism
> over `φ`, and it carries the image of `ξ_i(j)` in `D(n)` to the divided power variable
> `ξ_i(j)`.

```lean
public theorem exists_ringEquiv_pAdicCompletedDividedPowerPolynomial (n : ℕ) :
    ∃ (φ : pAdicCompletedDividedPowerEnvelope s f hf →+*
        pAdicCompletedTensorPowerEnvelope s f hf n)
      (e : pAdicCompletedTensorPowerEnvelope s f hf n ≃+*
        pAdicCompletedDividedPowerPolynomialOverEnvelope s f hf n),
      (∀ x : MvPolynomial ι s.A,
          φ (toPAdicCompletedDividedPowerEnvelope s f hf x) =
            toPAdicCompletedDividedPowerEnvelope s (tensorPowerPresentation s f n)
              (tensorPowerPresentation_surjective s f hf n)
              (mvPolynomialCoprojection s.A (0 : Fin (n + 1)) x)) ∧
      (∀ y : pAdicCompletedDividedPowerEnvelope s f hf,
          e (φ y) = toPAdicCompletedDividedPowerPolynomial s f hf n y) ∧
      (∀ q : ι × Fin n,
          e (toPAdicCompletedDividedPowerEnvelope s (tensorPowerPresentation s f n)
            (tensorPowerPresentation_surjective s f hf n) (coprojectionDifference s n q)) =
            coprojectionDifferenceVariable s f hf n q)
```

## Tag 07L3, an equation

[Tag 07L3](https://stacks.math.columbia.edu/tag/07L3) in the Stacks Project.

Declarations registered for the tag:

- [`Crystalline.exists_ringEquiv_pAdicCompletedDividedPowerPolynomial`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/TensorPowerEnvelope.lean#L1347), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/TensorPowerEnvelope.lean, line 1536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/TensorPowerEnvelope.lean#L1536) (StacksFrontier): “equation 60.17.1.1, the display of this lemma: the isomorphism `e` produced here is `D(n) = lim_e D⟨ξ_i(j)⟩/p^e D⟨ξ_i(j)⟩`, over the algebra structure `φ` of `D(n)` over `D` and carrying the image of each `ξ_i(j)` to the divided power variable of the same name”.

## Tag 07L4, a lemma

[Tag 07L4](https://stacks.math.columbia.edu/tag/07L4) in the Stacks Project.

**`Crystalline.completedEnvelopeThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Coproduct.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Coproduct.lean#L140). The attribute's comment: “the completed envelopes are objects of the site”.

> **Stacks Project, Tag 07L4**, first assertion.  The divided power ring `(D, J̄, γ̄)` of a
> surjective polynomial presentation of `C` over `A` is an object of `Cris^∧(C/A)`.  Applied to
> the tensor power presentation this is `(D(n), J̄(n), γ̄(n))`, see
> `Crystalline.tensorPowerEnvelopeThickening`.

```lean
public noncomputable def completedEnvelopeThickening
    (g : MvPolynomial ι s.A →ₐ[s.A] s.C) (hg : Function.Surjective g) :
    CompletedEnvelopeThickening s g hg
```

**`Crystalline.completedEnvelope_isCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Coproduct.lean, line 691](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Coproduct.lean#L691). The attribute's comment: “the canonical coproduct”.

> **Stacks Project, Tag 07L4**, second assertion.  The canonical coprojections exhibit
> `D(n)` as the coproduct `∐_{j = 0, …, n} D` of `n + 1` copies of `D` in `Cris^∧(C/A)`.

```lean
public theorem completedEnvelope_isCoproduct
    (g : MvPolynomial ι s.A →ₐ[s.A] s.C) (hg : Function.Surjective g) (n : ℕ) :
    Nonempty (IsColimit (Cofan.mk (tensorPowerEnvelopeThickening s g hg n).thickening
      (completedEnvelopeCoprojection s g hg n)))
```

## Tag 07JB, an item

[Tag 07JB](https://stacks.math.columbia.edu/tag/07JB) in the Stacks Project.

**`Crystalline.IsPAdicallyComplete`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean#L123).

> A `D`-module is `p`-adically complete when it is complete and separated for the `p`-adic
> filtration, that is for the ideal `p D`.

```lean
public def IsPAdicallyComplete (M : Type w) [AddCommGroup M] [Module D M] : Prop
```

**`Crystalline.instIsAdicCompleteCompletedDividedPowerRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CompletedRingPAdicComplete.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CompletedRingPAdicComplete.lean#L63). The attribute's comment: “item (07JB) for the module `M = D` over the completed divided power ring itself”.

> **The `p`-adic completion `D` of `B` is `p`-adically complete for its own ideal `(p) ⊆ D`.**
>
> This is item (07JB) of [Stacks, Lemma 60.17.3, Tag 07JG] for the module `M = D` over itself, the
> case of the coefficient sheaf `𝒪_{X/S}`.  Mathlib's `AdicCompletion.isAdicComplete_self` proves
> it for the extension along `algebraMap B D` of the ideal `(p) ⊆ B`, and
> `Crystalline.pAdicIdeal_map_ringHom` identifies that extension with the ideal `(p) ⊆ D`; the
> finite generation it asks of `(p) ⊆ B` is `Submodule.fg_span_singleton`.

```lean
public instance instIsAdicCompleteCompletedDividedPowerRing :
    IsAdicComplete (pAdicIdeal (A := completedDividedPowerRing p (B := B)) p)
      (completedDividedPowerRing p (B := B))
```

## Tag 07JC, an item

[Tag 07JC](https://stacks.math.columbia.edu/tag/07JC) in the Stacks Project.

**`Crystalline.CompletedConnection`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean#L131).

> A connection `∇ : M → M ⊗̂_D Ω` relative to a map `d : D → Ω`: an additive map satisfying the
> Leibniz rule `∇ (f m) = f • ∇ m + m ⊗ d f`.

```lean
public structure CompletedConnection (d : D → Omega) (M : Type w) [AddCommGroup M]
    [Module D M]
```

## Tag 07JD, an item

[Tag 07JD](https://stacks.math.columbia.edu/tag/07JD) in the Stacks Project.

**`Crystalline.IsIntegrable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean#L196). The attribute's comment: “integrability in the coordinates x_i: the coordinate operators commute”.

> A completed connection is integrable when its coordinate operators commute.

```lean
public def IsIntegrable (dx : ι → Omega) {d : D → Omega} {M : Type w} [AddCommGroup M]
    [Module D M] (nabla : CompletedConnection p D Omega d M) : Prop
```

## Tag 07JE, an item

[Tag 07JE](https://stacks.math.columbia.edu/tag/07JE) in the Stacks Project.

**`Crystalline.IsTopologicallyQuasiNilpotent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CompletedConnection.lean#L205). The attribute's comment: “corrected to k ≥ 1: admitting k = 0 would force M = p M”.

> A completed connection is topologically quasi-nilpotent when, writing
> `∇ m = ∑ θ_i m ⬝ d x_i`, for every `m` only finitely many pairs `(i, k)` with `k ≥ 1` satisfy
> `θ_i^k m ∉ p M`.

```lean
public def IsTopologicallyQuasiNilpotent (dx : ι → Omega) {d : D → Omega} {M : Type w}
    [AddCommGroup M] [Module D M] (nabla : CompletedConnection p D Omega d M) : Prop
```

## Tag 07JG, a lemma

[Tag 07JG](https://stacks.math.columbia.edu/tag/07JG) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.pairTensorLevel_crystalPairFunctor_nabla`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairConnection07J6.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairConnection07J6.lean#L65). The attribute's comment: “for any surjective polynomial presentation g : A[x_i : i ∈ ι] → C, supplied as the WholeSpacePresentation instance (the default instance is the tautological one): the connection of the pair attached to a crystal is the canonical connection of 07J6 evaluated on the finite thickenings (X, T_e, δ̄): its image at each level e is the 07J6 connection of the crystal over T_e applied to the image of m”.

> **The connection `∇` of the pair attached to a crystal is obtained by evaluating the canonical
> connection of [Stacks, Tag 07J6] on the finite thickenings.**  For a crystal `ℱ` in quasi-coherent
> `𝒪_{X/S}`-modules on `Cris(X/S)`, an element `m` of `M = lim_e Γ((X, T_e, δ̄), ℱ)` and a level
> `e`, the image of `∇(m) ∈ M ⊗̂_D Ω_D` in `Γ(T_e, Ω_{T_e/S,δ̄}) ⊗_{Γ(T_e, 𝒪)} Γ(T_e, ℱ)` is the
> canonical connection of `ℱ` on the sections over `(X, T_e, δ̄)`, applied to the image of `m`.

```lean
theorem pairTensorLevel_crystalPairFunctor_nabla (Fc : QuasiCoherentCrystal S) (e : ℕ)
    (m : wholeSpaceSections hp Fc ⦋0⦌) :
    pairTensorLevel hp Fc e (((crystalPairFunctor hp).obj Fc).nabla m) =
      AffineConnection.connection (bijective_crysExtensionSectionsMap_levelObj hp Fc e)
        (pairComponent hp Fc e m)
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.firstOrderTensorInclusion_crystalConnection_crystalPairFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairConnection07J6.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairConnection07J6.lean#L90). The attribute's comment: “for any surjective polynomial presentation g : A[x_i : i ∈ ι] → C, supplied as the WholeSpacePresentation instance (the default instance is the tautological one): the connection of the pair attached to a crystal is the sheaf-level canonical connection of 07J6 evaluated on the finite thickenings (X, T_e, δ̄), level by level”.

> **The connection `∇` of the pair attached to a crystal is obtained by evaluating the
> sheaf-level canonical connection of [Stacks, Tag 07J6] on the finite thickenings.**  For a crystal
> `ℱ` in quasi-coherent `𝒪_{X/S}`-modules on `Cris(X/S)`, an element `m` of
> `M = lim_e Γ((X, T_e, δ̄), ℱ)` and a level `e`, the canonical connection
> `∇ : ℱ_{T_e} ⟶ ℱ_{T_e} ⊗ Ω_{T_e/S,δ̄}` of `...SmallSite.crystalConnection`, applied to the image
> of `m` over the whole of `T_e` and read in the sections of `ℱ` over the first-order thickening
> `T'_e` through the canonical morphism `ℱ_{T_e} ⊗ Ω ⟶ p₀_* ℱ_{T'_e}`, is the image of `∇(m)` at
> the level `e` read there through the canonical map `ω ⊗ s ↦ ω · p₀^* s`.

```lean
theorem firstOrderTensorInclusion_crystalConnection_crystalPairFunctor
    (Fc : QuasiCoherentCrystal S) (e : ℕ) (m : wholeSpaceSections hp Fc ⦋0⦌) :
    (firstOrderTensorInclusion Fc.obj (levelObj hp 0 e)).val.app (op ⊤)
        ((crystalConnection (levelObj hp 0 e) Fc.property.2).hom.app (op ⊤)
          (crysSiteRestrict Fc.obj ((levelObj hp 0 e).restrictOpenHom ⊤)
            (show Fc.obj.val.obj (op (levelObj hp 0 e)) from pairComponent hp Fc e m))) =
      crysSiteRestrict Fc.obj
        ((firstOrderThickeningCrysObject S (levelObj hp 0 e)).restrictOpenHom ⊤)
        (AffineConnection.diffAction Fc.obj (levelObj hp 0 e)
          (pairTensorLevel hp Fc e (((crystalPairFunctor hp).obj Fc).nabla m)))
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystalPairFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairFunctor07JG.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairFunctor07JG.lean#L697). The attribute's comment: “the functor from the crystals in quasi-coherent O_{X/S}-modules on Cris(X/S) to the pairs (M, ∇) satisfying (07JB), (07JC), (07JD) and (07JE), for any surjective polynomial presentation g : P = A[x_i : i ∈ ι] → C, supplied as the WholeSpacePresentation instance (the default instance is the tautological one): M = lim_e Γ(T_e, F), ∇ read off the Taylor expansion of the crystal over D(1); that ∇ is the 07J6 connection evaluated on the T_e is pairTensorLevel_crystalPairFunctor_nabla”.

> **[Stacks, Lemma 60.17.3, Tag 07JG]: the functor**
>
> `{crystals in quasi-coherent 𝒪_{X/S}-modules on Cris(X/S)} ⟶ {pairs (M, ∇) satisfying (07JB),
> (07JC), (07JD) and (07JE)}`,
>
> in the situation of [Stacks, Section 60.17, Tag 07J7]: `X = Spec(C)`, `S = Spec(A)` affine with
> `p` nilpotent on `C`, `P = A[x_i : i ∈ ι] → C` any surjective polynomial presentation (the
> instance `...SmallSite.WholeSpacePresentation S hp` the system of thickenings is built from; by
> default `A[x_c : c ∈ C] → C`), `D` the `p`-adically completed divided power envelope (07J8),
> `Ω_D` its completed module of divided power differentials (07J9) and `d : D → Ω_D` (07JA).  It
> sends a crystal `ℱ` to `M = lim_e Γ((X, T_e, δ̄), ℱ)` with the connection read off the crystal's
> Taylor expansion over `D(1)`, and a morphism of crystals to the induced map of the limits.  That
> this connection is the canonical connection of [Stacks, Tag 07J6] evaluated on the finite
> thickenings `(X, T_e, δ̄)` is `...SmallSite.pairTensorLevel_crystalPairFunctor_nabla` and
> `...SmallSite.firstOrderTensorInclusion_crystalConnection_crystalPairFunctor`.

```lean
def crystalPairFunctor :
    QuasiCoherentCrystal S ⥤ Pair.{u, u, u, u} S.p (pairRing hp) (pairForms hp) (pairDx hp)
      (derivationFun ((affineSituation S hp).A : Type u) (pairRing hp) _ (pairForms hp)
        (pairDerivation hp))
```

## Tag 07JH, a proposition

[Tag 07JH](https://stacks.math.columbia.edu/tag/07JH) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystalPairFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairEquivalence.lean, line 633](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalPairEquivalence.lean#L633). The attribute's comment: “for any surjective polynomial presentation g : P = A[x_i : i ∈ ι] → C, supplied as the WholeSpacePresentation instance (the default instance is the tautological one): the functor of 07JG, from the crystals in quasi-coherent O_{X/S}-modules on Cris(X/S) to the pairs (M, ∇) over D satisfying (07JB), (07JC), (07JD) and (07JE), with its connection the canonical connection of 07J6 evaluated on the finite thickenings (pairTensorLevel_crystalPairFunctor_nabla), is an equivalence of categories”.

> **[Stacks, Proposition 60.17.4, Tag 07JH]: the functor of [Stacks, Lemma 60.17.3, Tag 07JG]**
>
> `{crystals in quasi-coherent 𝒪_{X/S}-modules on Cris(X/S)} ⟶ {pairs (M, ∇) satisfying (07JB),
> (07JC), (07JD) and (07JE)}`
>
> **is an equivalence of categories.**  This is the functor `...SmallSite.crystalPairFunctor` of
> the tag 07JG, in the situation of [Stacks, Section 60.17, Tag 07J7]: `X = Spec(C)`,
> `S = Spec(A)` affine with `p` nilpotent on `C`, any surjective polynomial presentation
> `P = A[x_i : i ∈ ι] → C` (the instance `...SmallSite.WholeSpacePresentation S hp` the system of
> thickenings is built from; by default the tautological `A[x_c : c ∈ C] → C`), `D`
> the `p`-adically completed divided power envelope and `Ω_D` its completed module of divided power
> differentials.  It sends `ℱ` to `M = lim_e Γ((X, T_e, δ̄), ℱ)` with its specified canonical
> crystalline connection: the canonical connection of [Stacks, Tag 07J6] evaluated on the finite
> thickenings `(X, T_e, δ̄)`, which is
> `...SmallSite.pairTensorLevel_crystalPairFunctor_nabla`.

```lean
theorem crystalPairFunctor_isEquivalence : (crystalPairFunctor hp).IsEquivalence
```

## Tag 07L5, a lemma

[Tag 07L5](https://stacks.math.columbia.edu/tag/07L5) in the Stacks Project.

**`Crystalline.exists_presentation_retract_pairEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/EnvelopeRetractEquivalence.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/EnvelopeRetractEquivalence.lean#L245). The attribute's comment: “both assertions, under exactly the source's hypotheses: for A -> P' smooth and P' -> C surjective, there are a polynomial presentation q : A[x_i] ->> P' with finitely many variables and divided power A-algebra maps a : D -> D', b : D' -> D between the p-adically completed envelopes, compatible with the augmentations to C, with a . b = id; and an equivalence of categories between the pairs (M, nabla) over D satisfying 07JB-07JE (Crystalline.Pair over the completed one-forms of D in the coordinates d x_i) and the pairs (M', nabla') over D' satisfying 07JB-07JE (Crystalline.RetractPair: p-adically complete, a completed connection over the completed forms of D' whose curvature vanishes, and 07JE read on the base change G(M', nabla') along b, as the proof defines it), whose functor is the base change along a and whose inverse is the base change along b; and, for the last sentence, a functor towards the pairs over D is an equivalence exactly when its composite with the base change towards D' is”.

> **[Stacks, Lemma 60.17.5, Tag 07L5].**  In Situation [Stacks, Tag 07MD], let `A → P' → C` be
> ring maps with `A → P'` smooth and `P' → C` surjective with kernel `J'`, and let `D'` be the
> `p`-adic completion of `D_{P', γ}(J')` (`Crystalline.completedEnvelopeOfPresentation`).  Then
>
> * **(first assertion)** there are a choice of the data `A → P → C` — a polynomial algebra
>   `P = A[x_i]` in finitely many variables with a surjection `q : P ↠ P'`, `P → C` being the
>   composite — and homomorphisms of divided power `A`-algebras `a : D → D'`, `b : D' → D`
>   between the `p`-adic completions of the divided power envelopes, compatible with the
>   augmentations `D → C` and `D' → C`, with `a ∘ b = id_{D'}`;
> * **(second assertion)** these maps induce an equivalence of categories between the pairs
>   `(M, ∇)` over `D` satisfying (07JB)–(07JE) — `Crystalline.Pair` for the completed one-forms
>   `Ω_D` with the coordinates `d x_i` — and the pairs `(M', ∇')` over `D'` satisfying them —
>   `Crystalline.RetractPair` for the completed forms `Ω^*_{D'}`: `p`-adically complete, with a
>   completed connection whose curvature vanishes, and topologically quasi-nilpotent in the sense
>   the proof gives that condition over `D'`, on `G(M', ∇')`.  The functor is the base change `F`
>   along `a` and its quasi-inverse the base change `G` along `b`;
> * **(last sentence)** consequently a functor towards the pairs over `D` — in particular the
>   functor of [Stacks, Proposition 60.17.4, Tag 07JH] — is an equivalence exactly when its
>   composite with `F`, towards the pairs over `D'`, is one.  For the functor of
>   [Stacks, Tag 07JG] on crystals this is
>   `...SmallSite.exists_presentation_retract_crystalPairEquivalence`.
>
> The proof of the second assertion is the source's: `F ∘ G ≅ 𝟭` because `a ∘ b = id`, and
> `G ∘ F ≅ 𝟭` by the Taylor comparison `c_{id_D, b ∘ a}`, whose horizontality — which the source
> omits — is `Crystalline.coordOp_taylorRoundTrip`.

```lean
theorem exists_presentation_retract_pairEquivalence :
    ∃ (ι : Type u) (_ : Fintype ι) (_ : DecidableEq ι) (q : MvPolynomial ι s.A →ₐ[s.A] P')
      (hq : Function.Surjective q)
      (a : DPMorphism (envelopeCompletion (presentationEnvelope s (f'.comp q)) s.p
          (presentationEnvelope_prime_nilpotent s (f'.comp q) (hf'.comp hq))).dividedPowers
        (completedEnvelopeOfPresentation s f' hf').dividedPowers)
      (b : DPMorphism (completedEnvelopeOfPresentation s f' hf').dividedPowers
        (envelopeCompletion (presentationEnvelope s (f'.comp q)) s.p
          (presentationEnvelope_prime_nilpotent s (f'.comp q) (hf'.comp hq))).dividedPowers)
      (ha : ∀ c : (s.A : Type u), a (algebraMap (s.A : Type u)
          (envelopeCompletion (presentationEnvelope s (f'.comp q)) s.p
            (presentationEnvelope_prime_nilpotent s (f'.comp q) (hf'.comp hq)) : Type u) c) =
          algebraMap (s.A : Type u) (completedEnvelopeOfPresentation s f' hf' : Type u) c)
      (hb : ∀ c : (s.A : Type u), b (algebraMap (s.A : Type u)
          (completedEnvelopeOfPresentation s f' hf' : Type u) c) =
          algebraMap (s.A : Type u) (envelopeCompletion (presentationEnvelope s (f'.comp q)) s.p
            (presentationEnvelope_prime_nilpotent s (f'.comp q) (hf'.comp hq)) : Type u) c)
      (hab : ∀ x, a (b x) = x)
      (hρ : ∀ y, b (a y) - y ∈ (envelopeCompletion (presentationEnvelope s (f'.comp q)) s.p
          (presentationEnvelope_prime_nilpotent s (f'.comp q) (hf'.comp hq))).ideal),
      a.comp b = DPMorphism.id _ ∧
        (completedEnvelopeAugmentation s f' hf').comp a.toRingHom =
          completedEnvelopeAugmentation s (f'.comp q) (hf'.comp hq) ∧
        (completedEnvelopeAugmentation s (f'.comp q) (hf'.comp hq)).comp b.toRingHom =
          completedEnvelopeAugmentation s f' hf' ∧
        ∃ e : Pair.{u, u, u, u} s.p _
            (polynomialEnvelopeCoordinates s (f'.comp q) (hf'.comp hq)).forms
            (polynomialEnvelopeCoordinates s (f'.comp q) (hf'.comp hq)).dx
            (polynomialEnvelopeCoordinates s (f'.comp q) (hf'.comp hq)).diff ≌
          RetractPair (polynomialEnvelopeCoordinates s (f'.comp q) (hf'.comp hq))
            (envelopeRetractData _ s.p _ (completedEnvelopeOfPresentation s f' hf') a b ha hb
              hab hρ),
          e.functor = retractForwardFunctor _ (envelopeRetractData _ s.p _
            (completedEnvelopeOfPresentation s f' hf') a b ha hb hab hρ) ∧
          e.inverse = retractBackFunctor _ (envelopeRetractData _ s.p _
            (completedEnvelopeOfPresentation s f' hf') a b ha hb hab hρ) ∧
          ∀ {𝒞 : Type w} [Category.{w'} 𝒞] (Φ : 𝒞 ⥤ Pair.{u, u, u, u} s.p _
            (polynomialEnvelopeCoordinates s (f'.comp q) (hf'.comp hq)).forms
            (polynomialEnvelopeCoordinates s (f'.comp q) (hf'.comp hq)).dx
            (polynomialEnvelopeCoordinates s (f'.comp q) (hf'.comp hq)).diff),
            Φ.IsEquivalence ↔ (Φ ⋙ e.functor).IsEquivalence
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.exists_presentation_retract_crystalPairEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalRetractPairs07L5.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalRetractPairs07L5.lean#L208). The attribute's comment: “all three parts in the situation of 07J7 (X = Spec C, S = Spec A affine, p nilpotent on C), for A -> P' smooth and P' -> C surjective: a polynomial presentation q : A[x_i] ->> P' in finitely many variables, the system of 07JN being presented by A[x_(0,i)] -> P' -> C (WholeSpacePresentation S hp), and divided power A-algebra maps a : D -> D', b : D' -> D compatible with the augmentations, with a . b = id; an equivalence between the pairs over D and the pairs over D' satisfying 07JB-07JE whose functor is the base change along a and whose inverse is the base change along b; and the last sentence: the functor of 07JG for that presentation, from the crystals in quasi-coherent O_{X/S}-modules on Cris(X/S), followed by the base change along a towards the pairs over D' (crystalRetractPairFunctor), is an equivalence”.

> **[Stacks, Lemma 60.17.5, Tag 07L5], for the crystals of [Stacks, Tag 07JH].**  In the
> situation of [Stacks, Section 60.17, Tag 07J7], `X = Spec(C)` and `S = Spec(A)` affine with `p`
> nilpotent on `C`, let `A → P' → C` be ring maps with `A → P'` smooth and `P' → C` surjective,
> and let `D'` be the `p`-adic completion of `D_{P', γ}(J')`.  Then
>
> * **(first assertion)** there are a choice of the data `A → P → C` — a polynomial algebra
>   `P = A[x_i]` in finitely many variables with a surjection `q : P ↠ P'`, the presentation of the
>   system of [Stacks, Tag 07JN] being the composite `P → P' → C` — and homomorphisms of divided
>   power `A`-algebras `a : D → D'`, `b : D' → D` compatible with the augmentations to `C`, with
>   `a ∘ b = id_{D'}`;
> * **(second assertion)** these maps induce an equivalence of categories `e` between the pairs over
>   `D` and the pairs over `D'` satisfying (07JB)–(07JE), with functor the base change `F` along `a`
>   and quasi-inverse the base change `G` along `b`;
> * **(last sentence)** the equivalence of [Stacks, Proposition 60.17.4, Tag 07JH] also holds for
>   the corresponding functor towards the pairs over `D'`: the functor
>   `...SmallSite.crystalRetractPairFunctor` from the crystals in quasi-coherent
>   `𝒪_{X/S}`-modules on `Cris(X/S)`, which is the functor of [Stacks, Tag 07JG]
>   (`...SmallSite.crystalPairFunctor`, for the presentation `P → C`) followed by `F`, is an
>   equivalence of categories.

```lean
theorem exists_presentation_retract_crystalPairEquivalence (P' : Type u) [CommRing P']
    [Algebra ((affineSituation S hp).A : Type u) P']
    [Algebra.Smooth ((affineSituation S hp).A : Type u) P']
    (f' : P' →ₐ[(affineSituation S hp).A] (affineSituation S hp).C)
    (hf' : Function.Surjective f') :
    ∃ (ι : Type u) (_ : Fintype ι) (_ : DecidableEq ι)
      (q : MvPolynomial ι (affineSituation S hp).A →ₐ[(affineSituation S hp).A] P')
      (hq : Function.Surjective q),
      letI : WholeSpacePresentation S hp := ⟨ι, f'.comp q, hf'.comp hq⟩
      ∃ (a : DPMorphism (systemEnvelopeCompletion hp).dividedPowers
          (completedEnvelopeOfPresentation (affineSituation S hp) f' hf').dividedPowers)
        (b : DPMorphism
          (completedEnvelopeOfPresentation (affineSituation S hp) f' hf').dividedPowers
          (systemEnvelopeCompletion hp).dividedPowers)
        (ha : ∀ c : ((affineSituation S hp).A : Type u),
          a (algebraMap ((affineSituation S hp).A : Type u) (systemEnvelopeCompletion hp) c) =
            algebraMap ((affineSituation S hp).A : Type u)
              (completedEnvelopeOfPresentation (affineSituation S hp) f' hf' : Type u) c)
        (hb : ∀ c : ((affineSituation S hp).A : Type u),
          b (algebraMap ((affineSituation S hp).A : Type u)
              (completedEnvelopeOfPresentation (affineSituation S hp) f' hf' : Type u) c) =
            algebraMap ((affineSituation S hp).A : Type u) (systemEnvelopeCompletion hp) c)
        (hab : ∀ x, a (b x) = x)
        (hρ : ∀ y, b (a y) - y ∈ (systemEnvelopeCompletion hp).ideal),
        a.comp b = DPMorphism.id _ ∧
        (completedEnvelopeAugmentation (affineSituation S hp) f' hf').comp a.toRingHom =
          completedEnvelopeAugmentation (affineSituation S hp)
            (tensorPowerPresentation (affineSituation S hp) (wholeSpacePresentation S hp) 0)
            (tensorPowerPresentation_surjective (affineSituation S hp)
              (wholeSpacePresentation S hp) (wholeSpacePresentation_surjective S hp) 0) ∧
        (completedEnvelopeAugmentation (affineSituation S hp)
            (tensorPowerPresentation (affineSituation S hp) (wholeSpacePresentation S hp) 0)
            (tensorPowerPresentation_surjective (affineSituation S hp)
              (wholeSpacePresentation S hp) (wholeSpacePresentation_surjective S hp) 0)).comp
            b.toRingHom =
          completedEnvelopeAugmentation (affineSituation S hp) f' hf' ∧
        ∃ e : Pair.{u, u, u, u} (affineSituation S hp).p _ (systemEnvelopeCoordinates hp).forms
            (systemEnvelopeCoordinates hp).dx (systemEnvelopeCoordinates hp).diff ≌
          RetractPair (systemEnvelopeCoordinates hp)
            (envelopeRetractData _ (affineSituation S hp).p _
              (completedEnvelopeOfPresentation (affineSituation S hp) f' hf') a b ha hb hab hρ),
          e.functor = retractForwardFunctor _ (envelopeRetractData _ (affineSituation S hp).p _
            (completedEnvelopeOfPresentation (affineSituation S hp) f' hf') a b ha hb hab hρ) ∧
          e.inverse = retractBackFunctor _ (envelopeRetractData _ (affineSituation S hp).p _
            (completedEnvelopeOfPresentation (affineSituation S hp) f' hf') a b ha hb hab hρ) ∧
          crystalRetractPairFunctor hp _ a b ha hb hab hρ =
            crystalPairFunctor hp ⋙ pairCatToTensorPowerPairs hp ⋙
              (tensorPowerPairFormsEquivalence (affineSituation S hp)
                (wholeSpacePresentation S hp) (wholeSpacePresentation_surjective S hp)).functor ⋙
              e.functor ∧
          (crystalRetractPairFunctor hp _ a b ha hb hab hρ).IsEquivalence
```

## Tag 07L6, a remark

[Tag 07L6](https://stacks.math.columbia.edu/tag/07L6) in the Stacks Project.

**`Crystalline.exists_dpMorphism_envelope_of_hasStrongLiftingProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/StrongLiftingEnvelope.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/StrongLiftingEnvelope.lean#L248). The attribute's comment: “the hypothesis-generalisation of the lifting step in the proof of 07L5: smoothness of P'/A is used only through the strong lifting property of 07K4, which is here a hypothesis. The equivalence of categories asserted by 07L6 is NOT proved: the source defers its own proof of it”.

> **The lifting step of the construction in the proof of [Stacks, Tag 07L5], with smoothness
> replaced by the strong lifting property of [Stacks, Tag 07K4].**
>
> Let `(A, I, γ)` be a divided power ring, let `P'` be an `A`-algebra with the strong lifting
> property, let `π : P' → C` be a ring map whose kernel contains the image of `I`, and let `D` be
> the divided power envelope of `ker π`.  Let `(B, K, δ)` be a divided power ring, `aB : A → B` a
> divided power morphism, and suppose `p` is nilpotent in `B` for a prime `p`.  Given an ideal
> `L ⊆ K` and a ring map `g : P' → B ⧸ L` which restricts to `aB` on `A` and whose further
> reduction to `B ⧸ K` is induced by `π`, there is a divided power morphism `b : D → (B, K, δ)`
> over `A` whose restriction along `P' → D`, read modulo `L`, is `g`, and which is compatible with
> the maps to `C`: its restriction read modulo `K` is induced by `π`.
>
> Taking `B = D_e` and `L = ker(D_e → D'_e)` this is the step of the source's proof which produces
> `β_e : P' → D_e` lifting `P' → D'_e` and then the map `D_{P', γ}(J') → D_e`.

```lean
theorem exists_dpMorphism_envelope_of_hasStrongLiftingProperty {p : ℕ} (hp : p.Prime)
    (A : DividedPowerRing.{u}) {P' : Type u} [CommRing P'] [Algebra A P']
    {C : Type v} [CommRing C] (π : P' →+* C)
    {hJ : A.ideal.map (algebraMap A P') ≤ RingHom.ker π}
    (D : DividedPowerEnvelope A (algebraMap A P') (RingHom.ker π) hJ)
    (hlift : Algebra.HasStrongLiftingProperty A P')
    (B : DividedPowerRing.{u}) (hpB : IsNilpotent (p : B))
    (aB : DividedPowers.DPMorphism A.dividedPowers B.dividedPowers)
    {L : Ideal B} (hL : L ≤ B.ideal) (c : C →+* B ⧸ B.ideal) (g : P' →+* B ⧸ L)
    (hgA : g.comp (algebraMap A P') = (Ideal.Quotient.mk L).comp aB.toRingHom)
    (hgC : (Ideal.Quotient.factor hL).comp g = c.comp π) :
    ∃ b : DividedPowers.DPMorphism D.object.dividedPowers B.dividedPowers,
      b.comp D.structureMap = aB ∧
        (Ideal.Quotient.mk L).comp (b.toRingHom.comp D.algebraMap.toRingHom) = g ∧
        (Ideal.Quotient.mk B.ideal).comp (b.toRingHom.comp D.algebraMap.toRingHom) =
          c.comp π
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.17, Tag 07J7](https://stacks.math.columbia.edu/tag/07J7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
