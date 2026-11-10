---
declaration: section
origin: cited
lean: Stacks.RingHomGluing.exists_ringHom_inducing_at_maximal_ideal, Stacks.PrepareNonZeroDivisors.exists_finiteExtension_factorization_of_ringKrullDim_eq_one, AlgebraicGeometry.exists_bound_factorization_exponent_of_finite_extension, AlgebraicGeometry.exists_tameSymbolPreparation_of_ringKrullDim_eq_one
statement: formalized
proof: formalized
---

# 42.4 Preparation for tame symbols

Section 42.4 of the Stacks Project, [Tag 0EAD](https://stacks.math.columbia.edu/tag/0EAD). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EAE, a lemma

[Tag 0EAE](https://stacks.math.columbia.edu/tag/0EAE) in the Stacks Project.

**`Stacks.RingHomGluing.exists_ringHom_inducing_at_maximal_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/RingHomGluing/MaximalIdealGluing.lean, line 593](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/RingHomGluing/MaximalIdealGluing.lean#L593).

> Ring maps over the localizations at finitely many pairwise distinct maximal ideals glue to
> one global ring map. The map has kernel and cokernel killed by powers of the
> intersection, and it inherits finiteness, injectivity, or surjectivity when all the local maps
> have the corresponding property.

```lean
theorem exists_ringHom_inducing_at_maximal_ideal
    (hm : Pairwise fun i j ↦ m i ≠ m j)
    (f : ∀ i, Localization.AtPrime (m i) →+* B i)
    (hker : ∀ i, KernelIsKilledByIdealPower (f i)
      ((m i).map (algebraMap A (Localization.AtPrime (m i)))))
    (hcoker : ∀ i, CokernelIsKilledByIdealPower (f i)
      ((m i).map (algebraMap A (Localization.AtPrime (m i))))) :
    ∃ (B' : Type (max u v w)) (_ : CommRing B') (g : A →+* B'),
      (∀ i, ∃ gᵢ : B' →+* B i,
        gᵢ.comp g = (f i).comp (algebraMap A (Localization.AtPrime (m i))) ∧
        (Submonoid.map g (m i).primeCompl).IsLocalizationMap gᵢ) ∧
      KernelIsKilledByIdealPower g (⨅ i, m i) ∧
      CokernelIsKilledByIdealPower g (⨅ i, m i) ∧
      ((∀ i, (f i).Finite) → g.Finite) ∧
      ((∀ i, Function.Injective (f i)) → Function.Injective g) ∧
      ((∀ i, Function.Surjective (f i)) → Function.Surjective g)
```

## Tag 02Q7, a lemma

[Tag 02Q7](https://stacks.math.columbia.edu/tag/02Q7) in the Stacks Project.

**`Stacks.PrepareNonZeroDivisors.exists_finiteExtension_factorization_of_ringKrullDim_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/PrepareTwoNonZeroDivisors.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalRing/PrepareTwoNonZeroDivisors.lean#L47).

> **Stacks Project, Tag 02Q7.** Let `R` be a one-dimensional Noetherian local ring and let `a`
> and `b` be nonzerodivisors. There is a finite ring extension in which they have a common
> nonzerodivisor factor and their residual factors generate the unit ideal; moreover, a power of the
> maximal ideal annihilates the quotient by `R`.

```lean
theorem exists_finiteExtension_factorization_of_ringKrullDim_eq_one
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (hdim : ringKrullDim R = 1) (a b : R)
    (ha : a ∈ nonZeroDivisors R) (hb : b ∈ nonZeroDivisors R) :
    ∃ (S : Type u) (_ : CommRing S) (_ : Algebra R S),
      Module.Finite R S ∧
      Function.Injective (algebraMap R S) ∧
      (∃ n : ℕ, maximalIdeal R ^ n ≤
        Module.annihilator R (S ⧸ (Algebra.linearMap R S).range)) ∧
      ∃ t a' b' : S,
        t ∈ nonZeroDivisors S ∧
        a' ∈ nonZeroDivisors S ∧
        b' ∈ nonZeroDivisors S ∧
        algebraMap R S a = t * a' ∧
        algebraMap R S b = t * b' ∧
        Ideal.span ({a', b'} : Set S) = ⊤
```

## Tag 0EAF, a lemma

[Tag 0EAF](https://stacks.math.columbia.edu/tag/0EAF) in the Stacks Project.

**`AlgebraicGeometry.exists_bound_factorization_exponent_of_finite_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PreparationTameSymbols/Basic.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/PreparationTameSymbols/Basic.lean#L221).

> **Stacks Project, Tag 0EAF.** Let `R` be a one-dimensional Noetherian local ring and let
> `a` and `b` be nonzerodivisors, with `a` in the maximal ideal. There is a uniform bound on an
> exponent `m` for which the image of `b` in a finite ring extension is a multiple of `a ^ m`.

```lean
public theorem exists_bound_factorization_exponent_of_finite_extension
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (_hdim : ringKrullDim R = 1) {a b : R} (ha : IsSMulRegular R a)
    (hb : IsSMulRegular R b) (ha_mem : a ∈ IsLocalRing.maximalIdeal R) :
    ∃ n : ℕ, ∀ (S : Type v) [CommRing S] [Algebra R S],
      (algebraMap R S).Finite → Function.Injective (algebraMap R S) → ∀ m : ℕ,
        (∃ c : S, algebraMap R S b = (algebraMap R S a) ^ m * c) → m ≤ n
```

## Tag 0EAG, a lemma

[Tag 0EAG](https://stacks.math.columbia.edu/tag/0EAG) in the Stacks Project.

**`AlgebraicGeometry.exists_tameSymbolPreparation_of_ringKrullDim_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PreparationTameSymbols/Existence.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/PreparationTameSymbols/Existence.lean#L36).

> **Stacks Project, Tag 0EAG.** Nonzerodivisors in a one-dimensional Noetherian local ring, not
> all of which are units, admit a simultaneous tame-symbol preparation after a finite extension
> whose quotient is supported at the maximal ideal.

```lean
theorem exists_tameSymbolPreparation_of_ringKrullDim_eq_one {A : Type u} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] {r : ℕ} (hr : 2 ≤ r)
    (a : Fin r → A) (ha : ∀ i, IsRegular (a i))
    (hunit : ¬ ∀ i, IsUnit (a i)) (hdim : ringKrullDim A = 1) :
    ∃ (B : Type u) (_ : CommRing B) (_ : Algebra A B),
      Nonempty (TameSymbolPreparation a B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.4, Tag 0EAD](https://stacks.math.columbia.edu/tag/0EAD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
