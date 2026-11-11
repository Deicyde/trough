---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.cohomologicalDimension_lt_of_le_of_le_jacobson, Stacks.LocalCohomology.cohomologicalDimension_lt_of_isZero_localCohomologyModule, Stacks.LocalCohomology.surjective_smul_top_localCohomologyModule_of_avoidsTopMinimalPrimes, Stacks.LocalCohomology.cohomologicalDimension_lt_of_isZero_homology_localCohomologyDerived, Ideal.exists_symbolicPower_le_pow, Stacks.LocalCohomology.cohomologicalDimension_lt_of_minimalPrimes_adicCompletion, Stacks.LocalCohomology.cohomologicalDimension_lt_of_isExcellent_of_isNormalRing, Stacks.LocalCohomology.isAffineOpen_complZeroLocusOpen_of_isExcellent_of_isNormalRing
statement: formalized
proof: formalized
---

# 51.16 Hartshorne-Lichtenbaum vanishing

Section 51.16 of the Stacks Project, [Tag 0EB0](https://stacks.math.columbia.edu/tag/0EB0). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EB1, a lemma

[Tag 0EB1](https://stacks.math.columbia.edu/tag/0EB1) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_lt_of_le_of_le_jacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/Jacobson.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/Jacobson.lean#L42).

> Let `A` be a Noetherian ring of dimension `d` and let `I ≤ I'` be ideals of `A` with `I'`
> inside the Jacobson radical. If the cohomological dimension of `I'` is less than `d`, then the
> cohomological dimension of `I` is less than `d` as well.

```lean
theorem cohomologicalDimension_lt_of_le_of_le_jacobson
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (d : ℕ) (hd : ringKrullDim A = (d : WithBot ℕ∞))
    (I I' : Ideal A) (hII' : I ≤ I') (hI' : I' ≤ Ring.jacobson A)
    (hcd : cohomologicalDimension A I' (Ideal.fg_of_isNoetherianRing I') < (d : ℤ)) :
    cohomologicalDimension A I (Ideal.fg_of_isNoetherianRing I) < (d : ℤ)
```

## Tag 0EB2, a lemma

[Tag 0EB2](https://stacks.math.columbia.edu/tag/0EB2) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_lt_of_isZero_localCohomologyModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaum.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaum.lean#L363).

> **Stacks Project, Tag 0EB2 (Hartshorne–Lichtenbaum vanishing).** Let `A` be a Noetherian ring
> of dimension `d` and let `I ⊆ A` be an ideal. If `H^d_{V(I)}(M) = 0` for some finite `A`-module
> `M` whose support contains every irreducible component of `Spec A` of dimension `d`, then the
> cohomological dimension of `I` in `A` is strictly less than `d`.

```lean
theorem cohomologicalDimension_lt_of_isZero_localCohomologyModule
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (d : ℕ) (hd : ringKrullDim A = (d : WithBot ℕ∞)) (I : Ideal A)
    (M : ModuleCat.{u} A) [Module.Finite A M]
    (hM : ∀ p : PrimeSpectrum A, IsMinimalPrime p.asIdeal →
      ringKrullDim (A ⧸ p.asIdeal) = (d : WithBot ℕ∞) → p ∈ Module.support A M)
    (hvan : IsZero
      (localCohomologyModule A I (Ideal.fg_of_isNoetherianRing I) M (d : ℤ))) :
    cohomologicalDimension A I (Ideal.fg_of_isNoetherianRing I) < (d : ℤ)
```

## Tag 0EB3, a lemma

[Tag 0EB3](https://stacks.math.columbia.edu/tag/0EB3) in the Stacks Project.

**`Stacks.LocalCohomology.surjective_smul_top_localCohomologyModule_of_avoidsTopMinimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/TopDegreeDivisibility.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/TopDegreeDivisibility.lean#L184).

> **Stacks Project, Tag 0EB3.** Let `A` be a Noetherian ring of Krull dimension `d`, let
> `I ⊆ A` be a finitely generated ideal, let `Y = V(I)` and let `M` be a finite `A`-module. An
> element `f ∈ A` lying outside every minimal prime `p` with `dim A/p = d` acts surjectively on
> `H^d_Y(M)`.
>
> The source assumes `A` local. That is not used: the dimension drop for `M/fM` and the vanishing
> above the dimension of the support both hold over an arbitrary Noetherian ring, so the hypothesis
> is dropped.

```lean
theorem surjective_smul_top_localCohomologyModule_of_avoidsTopMinimalPrimes
    (A : Type u) [CommRing A] [IsNoetherianRing A] (d : ℕ) (hd : ringKrullDim A = d) (f : A)
    (hf : ∀ p : PrimeSpectrum A, IsMinimalPrime p.asIdeal →
      ringKrullDim (A ⧸ p.asIdeal) = d → f ∉ p.asIdeal)
    (I : Ideal A) (hI : I.FG) (M : ModuleCat.{max u v} A) [Module.Finite A M] :
    Function.Surjective fun x : localCohomologyModule A I hI M (d : ℤ) => f • x
```

## Tag 0EB4, a lemma

[Tag 0EB4](https://stacks.math.columbia.edu/tag/0EB4) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_lt_of_isZero_homology_localCohomologyDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/DualizingComplexVanishing.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/DualizingComplexVanishing.lean#L367).

> **Stacks Project, Tag 0EB4.** Let `A` be a Noetherian local ring of dimension `d` with a
> normalized dualizing complex `ω_A^•`, and let `I ⊆ A` be an ideal. If `H^0_{V(I)}(ω_A^•) = 0`,
> then the cohomological dimension of `I` is strictly less than `d`.
>
> Write `ω_A = H^{-d}(ω_A^•)`. Choose `f ∈ A` outside every minimal prime of dimension `d` which
> annihilates `H^i(ω_A^•)` for `i > -d`; then `f` acts as zero on every homology object of
> `U = τ_{≥ -d + 1}ω_A^•`, so `f • 𝟙_U` is nilpotent, and therefore a power of `f` annihilates
> `H^{-1}_{V(I)}(U)`. The truncation triangle `ω_A[d] → ω_A^• → U` gives, after applying
> `RΓ_{V(I)}`, the exact sequence `H^{-1}_{V(I)}(U) → H^0_{V(I)}(ω_A[d]) → H^0_{V(I)}(ω_A^•) = 0`,
> so that same power of `f` annihilates `H^d_{V(I)}(ω_A)`. By Stacks 0EB3 multiplication by `f` is
> surjective on `H^d_{V(I)}(ω_A)`, whence `H^d_{V(I)}(ω_A) = 0`, and `ω_A` is supported at every
> `d`-dimensional minimal prime by Stacks 0A7V, so Stacks 0EB2 applies.

```lean
theorem cohomologicalDimension_lt_of_isZero_homology_localCohomologyDerived
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (d : ℕ) (hd : ringKrullDim A = (d : WithBot ℕ∞))
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : Dualizing.IsNormalizedDualizingComplex.{u, u} K) (I : Ideal A)
    (hvan : IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
      ((localCohomologyDerived A I (Ideal.fg_of_isNoetherianRing I)).obj K))) :
    cohomologicalDimension A I (Ideal.fg_of_isNoetherianRing I) < (d : ℤ)
```

## Tag 0EB5, a lemma

[Tag 0EB5](https://stacks.math.columbia.edu/tag/0EB5) in the Stacks Project.

**`Ideal.exists_symbolicPower_le_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/HartshorneLichtenbaumVanishing/Basic.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/HartshorneLichtenbaumVanishing/Basic.lean#L200).

> **Stacks Project, Tag 0EB5.** Let `p` be a one-dimensional prime ideal in a complete
> Noetherian local domain. For every `n ≥ 1`, some symbolic power `p⁽ᵐ⁾`, with `m ≥ n`, is
> contained in the ordinary power `pⁿ`.

```lean
theorem exists_symbolicPower_le_pow [IsNoetherianRing A] [IsLocalRing A] [IsDomain A]
    [IsAdicComplete (IsLocalRing.maximalIdeal A) A]
    (p : Ideal A) [p.IsPrime] (hp : ringKrullDim (A ⧸ p) = 1)
    (n : ℕ) (hn : 1 ≤ n) :
    ∃ m : ℕ, n ≤ m ∧ Ideal.symbolicPower p m ≤ p ^ n
```

## Tag 0EB6, a proposition

[Tag 0EB6](https://stacks.math.columbia.edu/tag/0EB6) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_lt_of_minimalPrimes_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaumCompletion.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaumCompletion.lean#L501).

> **Hartshorne–Lichtenbaum vanishing.** Let `A` be a Noetherian
> local ring with completion `A^∧` and let `I ⊆ A` be an ideal such that
> `dim V(I A^∧ + 𝔭) ≥ 1` for every minimal prime `𝔭 ⊆ A^∧` of dimension `dim(A)`. Then the
> cohomological dimension of `I` in `A` is strictly less than `dim(A)`.

```lean
theorem cohomologicalDimension_lt_of_minimalPrimes_adicCompletion
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (d : ℕ) (hd : ringKrullDim A = (d : WithBot ℕ∞)) (I : Ideal A)
    (h : ∀ q : PrimeSpectrum (AdicCompletion (IsLocalRing.maximalIdeal A) A),
      IsMinimalPrime q.asIdeal →
      ringKrullDim ((AdicCompletion (IsLocalRing.maximalIdeal A) A) ⧸ q.asIdeal) =
        (d : WithBot ℕ∞) →
      (1 : WithBot ℕ∞) ≤
        ringKrullDim ((AdicCompletion (IsLocalRing.maximalIdeal A) A) ⧸
          (I.map (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A)) +
            q.asIdeal))) :
    cohomologicalDimension A I (Ideal.fg_of_isNoetherianRing I) < (d : ℤ)
```

## Tag 0EB7, a lemma

[Tag 0EB7](https://stacks.math.columbia.edu/tag/0EB7) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_lt_of_isExcellent_of_isNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaumExcellent.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaumExcellent.lean#L123). The attribute's comment: “cd(A, I) < dim(A)”.

> **[Stacks Project, Tag 0EB7].** Let `A` be an excellent normal Noetherian local ring of
> dimension `d` and let `I ⊆ A` be an ideal with `dim V(I) ≥ 1`. Then the cohomological dimension
> of `I` in `A` is strictly less than `d`.

```lean
theorem cohomologicalDimension_lt_of_isExcellent_of_isNormalRing
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : IsExcellent A) (hnormal : IsNormalRing A)
    (d : ℕ) (hd : ringKrullDim A = (d : WithBot ℕ∞)) (I : Ideal A)
    (hI : (1 : WithBot ℕ∞) ≤ ringKrullDim (A ⧸ I)) :
    cohomologicalDimension A I (Ideal.fg_of_isNoetherianRing I) < (d : ℤ)
```

**`Stacks.LocalCohomology.isAffineOpen_complZeroLocusOpen_of_isExcellent_of_isNormalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaumExcellent.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/HartshorneLichtenbaumExcellent.lean#L149). The attribute's comment: “Spec(A) ∖ V(I) is affine when dim(A) = 2”.

> **[Stacks Project, Tag 0EB7].** For an excellent normal Noetherian local ring `A` of
> dimension two and an ideal `I ⊆ A` with `dim V(I) ≥ 1`, the open `Spec A ∖ V(I)` is affine.
>
> The cohomological dimension bound gives `cd(A, I) ≤ 1`, hence the vanishing of the cohomology of
> every quasi-coherent module on the complement in degrees `≥ 1` by Stacks 0DX7; the complement is
> quasi-compact, so Serre's criterion applies. This is the route of Stacks 0DXD.

```lean
theorem isAffineOpen_complZeroLocusOpen_of_isExcellent_of_isNormalRing
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : IsExcellent A) (hnormal : IsNormalRing A)
    (hd : ringKrullDim A = (2 : WithBot ℕ∞)) (I : Ideal A)
    (hI : (1 : WithBot ℕ∞) ≤ ringKrullDim (A ⧸ I)) :
    IsAffineOpen (complZeroLocusOpen A I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.16, Tag 0EB0](https://stacks.math.columbia.edu/tag/0EB0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
