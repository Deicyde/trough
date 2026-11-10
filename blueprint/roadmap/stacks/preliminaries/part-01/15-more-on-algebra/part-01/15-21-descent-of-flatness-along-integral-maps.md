---
declaration: section
origin: cited
lean: exists_monic_eq_X_sub_C_mul_of_isRoot, exists_finite_free_algebra_factor, exists_finite_free_extension_quotient_split_polynomials, Stacks.Spectrum.PolynomialQuotientImage.range_comap_eq_zeroLocus_iInf_imageIdeal, Module.Flat.of_finite_injective_baseChange, Module.Flat.of_integral_injective_baseChange, Module.Projective.of_finite_injective_baseChange
statement: formalized
proof: formalized
---

# 15.21 Descent of flatness along integral maps

Section 15.21 of the Stacks Project, [Tag 052Y](https://stacks.math.columbia.edu/tag/052Y). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 052Z, a lemma

[Tag 052Z](https://stacks.math.columbia.edu/tag/052Z) in the Stacks Project.

**`exists_monic_eq_X_sub_C_mul_of_isRoot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Polynomial/MonicSplitting.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Polynomial/MonicSplitting.lean#L36).

> If `a` is a root of a monic polynomial `P`, then `P = (X - C a) * Q` for some monic
> polynomial `Q`.

```lean
theorem exists_monic_eq_X_sub_C_mul_of_isRoot {R : Type*} [CommRing R]
    {P : Polynomial R} (hP : P.Monic) {a : R} (ha : P.IsRoot a) :
    ∃ Q : Polynomial R, Q.Monic ∧ P = (Polynomial.X - Polynomial.C a) * Q
```

## Tag 0530, a lemma

[Tag 0530](https://stacks.math.columbia.edu/tag/0530) in the Stacks Project.

**`exists_finite_free_algebra_factor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Polynomial/MonicSplitting.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Polynomial/MonicSplitting.lean#L66).

> For a monic polynomial `P` over `R` there is a finite free `R`-algebra `R'` over which the
> image of `P` factors as `(X - C α) * Q`, with `Q` monic.

```lean
theorem exists_finite_free_algebra_factor {R : Type u} [CommRing R]
    {P : Polynomial R} (hP : P.Monic) :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R')
      (_ : Module.Finite R R') (_ : Module.Free R R'),
      ∃ (α : R') (Q : Polynomial R'),
        Q.Monic ∧ P.map (algebraMap R R') = (Polynomial.X - Polynomial.C α) * Q
```

## Tag 0531, a lemma

[Tag 0531](https://stacks.math.columbia.edu/tag/0531) in the Stacks Project.

**`exists_finite_free_extension_quotient_split_polynomials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Polynomial/MonicSplitting.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Polynomial/MonicSplitting.lean#L121).

> A finite algebra becomes a quotient by split univariate polynomials after an injective
> finite free extension of its base ring.

```lean
theorem exists_finite_free_extension_quotient_split_polynomials
    {R : Type u} [CommRing R] {S : Type v} [CommRing S]
    [Algebra R S] [Module.Finite R S] :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R')
      (_ : Module.Finite R R') (_ : Module.Free R R'),
      Function.Injective (algebraMap R R') ∧
        letI : Algebra R' (S ⊗[R] R') := Algebra.TensorProduct.rightAlgebra
        ∃ (n : ℕ) (d : Fin n → ℕ) (α : ∀ i, Fin (d i) → R')
          (f : (MvPolynomial (Fin n) R' ⧸
            Ideal.span (Set.range fun i : Fin n ↦
              ∏ j : Fin (d i), (MvPolynomial.X i - MvPolynomial.C (α i j))))
              →ₐ[R'] S ⊗[R] R'),
          Function.Surjective f
```

## Tag 0532, a lemma

[Tag 0532](https://stacks.math.columbia.edu/tag/0532) in the Stacks Project.

**`Stacks.Spectrum.PolynomialQuotientImage.range_comap_eq_zeroLocus_iInf_imageIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Image.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Image.lean#L217).

> **Stacks Tag 0532.** The image of the map `Spec(S) → Spec(R)` induced by the
> structure map `R → S = R[T_1, …, T_n] / J` equals the closed set `V(⋂_{k ∈ K} J_k)`
> cut out by the intersection of the image ideals.

```lean
theorem range_comap_eq_zeroLocus_iInf_imageIdeal
    (J : Ideal (MvPolynomial (Fin n) R))
    (hJ : ∀ i, factoredPoly d α i ∈ J) :
    Set.range (PrimeSpectrum.comap (structMap J)) =
      PrimeSpectrum.zeroLocus (R := R)
        ((⨅ k : (i : Fin n) → Fin (d i), imageIdeal d α k J) : Ideal R)
```

## Tag 0533, a lemma

[Tag 0533](https://stacks.math.columbia.edu/tag/0533) in the Stacks Project.

**`Module.Flat.of_finite_injective_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/IntegralDescent.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/IntegralDescent.lean#L196). References: EGA IV (11.5.5), “finite injective case”.

> Let `R → S` be a finite injective homomorphism of rings with `R` Noetherian and let `M` be an
> `R`-module. If the scalar extension `S ⊗[R] M` is flat over `S`, then `M` is flat over `R`.

```lean
theorem Module.Flat.of_finite_injective_baseChange {R : Type u} [CommRing R] [IsNoetherianRing R]
    {S : Type v} [CommRing S] [Algebra R S] [Module.Finite R S]
    {M : Type w} [AddCommGroup M] [Module R M]
    (hRS : Function.Injective (algebraMap R S))
    (hM : Module.Flat S (S ⊗[R] M)) : Module.Flat R M
```

## Tag 0534, a lemma

[Tag 0534](https://stacks.math.columbia.edu/tag/0534) in the Stacks Project.

**`Module.Flat.of_integral_injective_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/IntegralDescent.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/IntegralDescent.lean#L722).

> Let `R → S` be an injective integral ring map and let `M` be a module over `R[x₁, …, xₙ]` that
> is finitely presented there and carries the restricted `R`-action. If the scalar extension
> `S ⊗[R] M` is flat over `S`, then `M` is flat over `R`.

```lean
theorem Module.Flat.of_integral_injective_baseChange
    {R : Type u} [CommRing R] {S : Type v} [CommRing S] [Algebra R S] [Algebra.IsIntegral R S]
    {n : ℕ} {M : Type w} [AddCommGroup M]
    [Module (MvPolynomial (Fin n) R) M] [Module R M]
    [IsScalarTower R (MvPolynomial (Fin n) R) M]
    [Module.FinitePresentation (MvPolynomial (Fin n) R) M]
    (hRS : Function.Injective (algebraMap R S))
    (hM : Module.Flat S (S ⊗[R] M)) : Module.Flat R M
```

## Tag 0H7R, a lemma

[Tag 0H7R](https://stacks.math.columbia.edu/tag/0H7R) in the Stacks Project.

**`Module.Projective.of_finite_injective_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/IntegralDescent.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/IntegralDescent.lean#L345).

> Let `R → S` be a finite injective homomorphism of rings with `R` Noetherian and let `P` be an
> `R`-module. If the scalar extension `S ⊗[R] P` is projective over `S`, then `P` is projective
> over `R`.

```lean
theorem Module.Projective.of_finite_injective_baseChange {R : Type u} [CommRing R]
    [IsNoetherianRing R] {S : Type v} [CommRing S] [Algebra R S] [Module.Finite R S]
    {P : Type w} [AddCommGroup P] [Module R P]
    (hRS : Function.Injective (algebraMap R S))
    [Module.Projective S (S ⊗[R] P)] : Module.Projective R P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.21, Tag 052Y](https://stacks.math.columbia.edu/tag/052Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
