---
declaration: section
origin: cited
lean: normal_local_domain_sepClosed_fractionField_isStrictlyHenselian, hensel_uniqueness, HenselianLocalRing.TFAE_factorization_etale_quasiFinite, HenselianLocalRing.henselianLocalRing_and_finite_of_finite_of_quasiFiniteAt, exists_algEquiv_prod_of_henselianLocalRing, exists_prod_local_purelyInseparable_not_quasiFiniteAt, CommAlgCat.FiniteEtale.isEquivalence_baseChange_residueField, Algebra.IsUnramifiedIn.exists_algEquiv_prod_quotient
statement: formalized
proof: formalized
---

# 10.153 Henselian local rings

Section 10.153 of the Stacks Project, [Tag 04GE](https://stacks.math.columbia.edu/tag/04GE). 13 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04GF, a definition

[Tag 04GF](https://stacks.math.columbia.edu/tag/04GF) in the Stacks Project.

**`normal_local_domain_sepClosed_fractionField_isStrictlyHenselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Criteria.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Criteria.lean#L326). References: SGA 7 I (0.0.3), “partial”.

> **Stacks Tag 04GF.** Let `R` be a normal local domain (a local integral domain that
> is integrally closed in its fraction field `K`). If `K` is separably algebraically
> closed, then `R` is strictly henselian, i.e. `R` is a henselian local ring and its
> residue field is separably algebraically closed.

```lean
theorem normal_local_domain_sepClosed_fractionField_isStrictlyHenselian
    (R : Type*) [CommRing R] [IsLocalRing R] [IsDomain R] [IsIntegrallyClosed R]
    (K : Type*) [Field K] [Algebra R K] [IsFractionRing R K] [IsSepClosed K] :
    HenselianLocalRing R ∧ IsSepClosed (IsLocalRing.ResidueField R)
```

## Tag 06RR, a lemma

[Tag 06RR](https://stacks.math.columbia.edu/tag/06RR) in the Stacks Project.

**`hensel_uniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Criteria.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Criteria.lean#L368). References: SGA 3 VIIB (1.6), “partial”.

> Hensel uniqueness: in a local ring, two roots of a polynomial that are
> congruent modulo the maximal ideal must be equal, provided the formal
> derivative at one of them is not in the maximal ideal.

```lean
theorem hensel_uniqueness {R : Type*} [CommRing R] [IsLocalRing R]
    (f : Polynomial R) (a b : R)
    (hfa : f.eval a = 0) (hfb : f.eval b = 0)
    (hab : a - b ∈ IsLocalRing.maximalIdeal R)
    (hf' : (Polynomial.derivative f).eval a ∉ IsLocalRing.maximalIdeal R) :
    a = b
```

## Tag 04GG, a lemma

[Tag 04GG](https://stacks.math.columbia.edu/tag/04GG) in the Stacks Project.

**`HenselianLocalRing.TFAE_factorization_etale_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/TFAE/Factorization.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/TFAE/Factorization.lean#L664). The attribute's comment: “The thirteen items are the entries, in the source's order, of one `List.TFAE`. `f̄` is `Polynomial.map (IsLocalRing.residue R) f`, `gcd(g₀, h₀) = 1` is `IsCoprime`, degrees are `Polynomial.degree` and item (6) carries the source's tacit `g₀ ≠ 0`, without which it holds only for fields. A retraction is an element of `S →ₐ[R] R`, `κ = κ(q)` is bijectivity of the canonical `Ideal.ResidueField.mapₐ`. A product of local rings is a `RingEquiv` onto a `Pi` type; the two-factor decompositions of (11)–(13) are `AlgEquiv`s. The source's quasi-finite of Definition 00PM is `Algebra.FiniteType` together with Mathlib's weaker `Algebra.QuasiFinite`. See the module docstring.”. References: EGA IV (18.5.13), “a'') existence half”; EGA IV (18.5.9), “(ii)”; EGA IV (18.5.11), “a), a'), b)”; SGA 4 VIII (4.1), “(i)–(iv)”.

> **Characterisations of henselian local rings** (Stacks 04GG). For a local ring `(R, 𝔪, κ)`
> the following are equivalent: (1) `R` is henselian; (2) every `f ∈ R[T]` and every root `a₀ ∈ κ`
> of `f̄` with `f̄'(a₀) ≠ 0` come from a root `a ∈ R` of `f` with `ā = a₀`; (3) every coprime
> factorisation `f̄ = g₀h₀` of the reduction of a monic `f ∈ R[T]` lifts to `f = gh` in `R[T]`;
> (4) the same with `deg g = deg g₀`; (5), (6) the same two statements for arbitrary `f ∈ R[T]`,
> (6) under the source's tacit `g₀ ≠ 0`;
> (7) every étale `R`-algebra `S` with a prime `q` over `𝔪` such that `κ = κ(q)` admits a
> retraction `S → R`; (8) it admits a unique retraction `τ` with `τ⁻¹(𝔪) = q`; (9) every finite
> `R`-algebra is a product of local rings; (10) a finite product of local rings; (11) every finite
> type `R`-algebra is `A × B` with `A` finite over `R` and `B` quasi-finite over `R` at no prime
> over `𝔪`; (12) the same with each irreducible component of `Spec(κ ⊗_R B)` of dimension `≥ 1`;
> (13) every quasi-finite `R`-algebra is `A × B` with `A` finite over `R` and `κ ⊗_R B = 0`.

```lean
public theorem HenselianLocalRing.TFAE_factorization_etale_quasiFinite
    (R : Type u) [CommRing R] [IsLocalRing R] :
    List.TFAE
      [HenselianLocalRing R,
       ∀ f : R[X], ∀ a₀ : ResidueField R, aeval a₀ f = 0 → aeval a₀ (derivative f) ≠ 0 →
         ∃ a : R, f.IsRoot a ∧ residue R a = a₀,
       ∀ f : R[X], f.Monic → ∀ g₀ h₀ : (ResidueField R)[X], f.map (residue R) = g₀ * h₀ →
         IsCoprime g₀ h₀ →
         ∃ g h : R[X], f = g * h ∧ g.map (residue R) = g₀ ∧ h.map (residue R) = h₀,
       ∀ f : R[X], f.Monic → ∀ g₀ h₀ : (ResidueField R)[X], f.map (residue R) = g₀ * h₀ →
         IsCoprime g₀ h₀ →
         ∃ g h : R[X], f = g * h ∧ g.map (residue R) = g₀ ∧ h.map (residue R) = h₀ ∧
           g.degree = g₀.degree,
       ∀ f : R[X], ∀ g₀ h₀ : (ResidueField R)[X], f.map (residue R) = g₀ * h₀ →
         IsCoprime g₀ h₀ →
         ∃ g h : R[X], f = g * h ∧ g.map (residue R) = g₀ ∧ h.map (residue R) = h₀,
       ∀ f : R[X], ∀ g₀ h₀ : (ResidueField R)[X], g₀ ≠ 0 → f.map (residue R) = g₀ * h₀ →
         IsCoprime g₀ h₀ →
         ∃ g h : R[X], f = g * h ∧ g.map (residue R) = g₀ ∧ h.map (residue R) = h₀ ∧
           g.degree = g₀.degree,
       ∀ (S : Type u) [CommRing S] [Algebra R S], Algebra.Etale R S →
         ∀ q : Ideal S, ∀ [q.IsPrime] [q.LiesOver (maximalIdeal R)],
         Function.Bijective (Ideal.ResidueField.mapₐ (maximalIdeal R) q (Algebra.ofId R S)
           (q.over_def _)) → Nonempty (S →ₐ[R] R),
       ∀ (S : Type u) [CommRing S] [Algebra R S], Algebra.Etale R S →
         ∀ q : Ideal S, ∀ [q.IsPrime] [q.LiesOver (maximalIdeal R)],
         Function.Bijective (Ideal.ResidueField.mapₐ (maximalIdeal R) q (Algebra.ofId R S)
           (q.over_def _)) → ∃! τ : S →ₐ[R] R, (maximalIdeal R).comap (τ : S →+* R) = q,
       ∀ (S : Type u) [CommRing S] [Algebra R S], Module.Finite R S →
         ∃ (ι : Type u) (A : ι → Type u) (_ : ∀ i, CommRing (A i)) (_ : ∀ i, IsLocalRing (A i)),
           Nonempty (S ≃+* ∀ i, A i),
       ∀ (S : Type u) [CommRing S] [Algebra R S], Module.Finite R S →
         ∃ (ι : Type u) (_ : Finite ι) (A : ι → Type u) (_ : ∀ i, CommRing (A i))
           (_ : ∀ i, IsLocalRing (A i)), Nonempty (S ≃+* ∀ i, A i),
       ∀ (S : Type u) [CommRing S] [Algebra R S], Algebra.FiniteType R S →
         ∃ (A B : Type u) (_ : CommRing A) (_ : CommRing B) (_ : Algebra R A) (_ : Algebra R B)
           (_ : S ≃ₐ[R] A × B), Module.Finite R A ∧
           ∀ q : Ideal B, ∀ [q.IsPrime], q.LiesOver (maximalIdeal R) →
             ¬ Algebra.QuasiFiniteAt R q,
       ∀ (S : Type u) [CommRing S] [Algebra R S], Algebra.FiniteType R S →
         ∃ (A B : Type u) (_ : CommRing A) (_ : CommRing B) (_ : Algebra R A) (_ : Algebra R B)
           (_ : S ≃ₐ[R] A × B), Module.Finite R A ∧
           ∀ p ∈ minimalPrimes (ResidueField R ⊗[R] B),
             1 ≤ ringKrullDim ((ResidueField R ⊗[R] B) ⧸ p),
       ∀ (S : Type u) [CommRing S] [Algebra R S], Algebra.FiniteType R S →
         Algebra.QuasiFinite R S →
         ∃ (A B : Type u) (_ : CommRing A) (_ : CommRing B) (_ : Algebra R A) (_ : Algebra R B)
           (_ : S ≃ₐ[R] A × B), Module.Finite R A ∧
           Subsingleton (ResidueField R ⊗[R] B)]
```

## Tag 04GH, a lemma

[Tag 04GH](https://stacks.math.columbia.edu/tag/04GH) in the Stacks Project.

**`HenselianLocalRing.henselianLocalRing_and_finite_of_finite_of_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/QuasiFinite.lean, line 783](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/QuasiFinite.lean#L783). The attribute's comment: “The four items are the four conjuncts, in the source's order. A finite product of local rings is an `AlgEquiv` onto a `Pi` type over a `Finite` index type (04GG (10)'s spelling, upgraded from `RingEquiv` because the factors are required finite over `R`); `S_q` is any `IsLocalization.AtPrime Sq q` in a scalar tower over `R`; the source's quasi-finiteness at `q` is `Algebra.QuasiFiniteAt R q` and its quasi-finite ring map is `Algebra.FiniteType` together with Mathlib's weaker `Algebra.QuasiFinite`. Item (4) is item (3) with `q` quantified. See the module docstring.”. References: EGA IV (18.5.9), “(ii) necessity”; EGA IV (18.5.10), “R henselian local”; SGA 4 VIII (4.1), “partial”.

> **Finite and quasi-finite algebras over a henselian local ring** (Stacks 04GH). Let
> `(R, 𝔪, κ)` be a henselian local ring. (1) A finite `R`-algebra `S` is a finite product of
> henselian local rings each finite over `R`. (2) If moreover `S` is local, then `S` is henselian
> and `R → S` is a local homomorphism. (3) If `S` is of finite type over `R` and `q` is a prime of
> `S` lying over `𝔪` at which `R → S` is quasi-finite, then `S_q` is henselian and finite over `R`.
> (4) If `R → S` is quasi-finite, this holds at every prime `q` of `S` lying over `𝔪`.

```lean
public theorem HenselianLocalRing.henselianLocalRing_and_finite_of_finite_of_quasiFiniteAt
    (R : Type u) [CommRing R] [HenselianLocalRing R] :
    (∀ (S : Type v) [CommRing S] [Algebra R S], Module.Finite R S →
        ∃ (ι : Type (max u v)) (_ : Finite ι) (A : ι → Type (max u v))
          (_ : ∀ i, CommRing (A i))
          (_ : ∀ i, Algebra R (A i)) (_ : ∀ i, HenselianLocalRing (A i)),
          (∀ i, Module.Finite R (A i)) ∧ Nonempty (S ≃ₐ[R] ∀ i, A i)) ∧
      (∀ (S : Type v) [CommRing S] [Algebra R S] [IsLocalRing S], Module.Finite R S →
        HenselianLocalRing S ∧ IsLocalHom (algebraMap R S)) ∧
      (∀ (S : Type v) [CommRing S] [Algebra R S], Algebra.FiniteType R S →
        ∀ q : Ideal S, ∀ [q.IsPrime] [q.LiesOver (maximalIdeal R)], Algebra.QuasiFiniteAt R q →
        ∀ (Sq : Type w) [CommRing Sq] [Algebra R Sq] [Algebra S Sq] [IsScalarTower R S Sq]
          [IsLocalization.AtPrime Sq q], HenselianLocalRing Sq ∧ Module.Finite R Sq) ∧
      (∀ (S : Type v) [CommRing S] [Algebra R S], Algebra.FiniteType R S →
        Algebra.QuasiFinite R S →
        ∀ q : Ideal S, ∀ [q.IsPrime] [q.LiesOver (maximalIdeal R)],
        ∀ (Sq : Type w) [CommRing Sq] [Algebra R Sq] [Algebra S Sq] [IsScalarTower R S Sq]
          [IsLocalization.AtPrime Sq q], HenselianLocalRing Sq ∧ Module.Finite R Sq)
```

## Tag 04GJ, a lemma

[Tag 04GJ](https://stacks.math.columbia.edu/tag/04GJ) in the Stacks Project.

**`exists_algEquiv_prod_of_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/FiniteType/Basic/ProductOfLocalRings.lean, line 611](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/FiniteType/Basic/ProductOfLocalRings.lean#L611). References: EGA IV (18.5.9), “more general”; SGA 4 VIII (4.1), “(ii)”.

> Stacks Tag 04GJ (Lemma 10.153.5). A finite type algebra over a henselian local ring
> decomposes, up to `R`-algebra isomorphism, as a finite product of local algebras finite
> over `R`, times an algebra `B` that is not quasi-finite at any prime lying over the
> maximal ideal of `R`.

```lean
theorem exists_algEquiv_prod_of_henselianLocalRing (R : Type u) [CommRing R] [HenselianLocalRing R]
    (S : Type v) [CommRing S] [Algebra R S] [Algebra.FiniteType R S] :
    ∃ (n : ℕ) (A : Fin n → Type (max u v)) (_ : ∀ i, CommRing (A i))
      (_ : ∀ i, Algebra R (A i)),
      (∀ i, IsLocalRing (A i)) ∧ (∀ i, Module.Finite R (A i)) ∧
      ∃ (B : Type (max u v)) (_ : CommRing B) (_ : Algebra R B),
        (∀ (𝔮 : Ideal B) [𝔮.IsPrime], 𝔮.LiesOver (IsLocalRing.maximalIdeal R) →
          ¬ Algebra.QuasiFiniteAt R 𝔮) ∧
        Nonempty (S ≃ₐ[R] (∀ i, A i) × B)
```

## Tag 06DD, a lemma

[Tag 06DD](https://stacks.math.columbia.edu/tag/06DD) in the Stacks Project.

**`exists_prod_local_purelyInseparable_not_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/FiniteType/StrictlyHenselian/ProductDecomposition.lean, line 765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/FiniteType/StrictlyHenselian/ProductDecomposition.lean#L765).

> Let `(R, m, κ)` be a strictly henselian local ring (a
> henselian local ring whose residue field is separably closed) and let `S` be a
> finite type `R`-algebra. Then `S` decomposes as an `R`-algebra isomorphism
> `S ≃ₐ[R] (∏ i, A i) × B`, where:
> * each `A i` is a local ring, finite over `R`, with `R → A i` a local
>   homomorphism;
> * for each `i`, the induced residue field extension `κ → κ(m_{A i})` is finite
>   and purely inseparable;
> * `R → B` is not quasi-finite at any prime of `B` lying over `m`.

```lean
theorem exists_prod_local_purelyInseparable_not_quasiFiniteAt (R : Type) [CommRing R]
    [HenselianLocalRing R] [IsSepClosed (ResidueField R)]
    (S : Type) [CommRing S] [Algebra R S] [Algebra.FiniteType R S] :
    ∃ (n : ℕ) (A : Fin n → Type) (_ : ∀ i, CommRing (A i)) (_ : ∀ i, Algebra R (A i)) (_ :
      ∀ i, IsLocalRing (A i)) (_ : ∀ i, IsLocalHom (algebraMap R (A i))) (B : Type) (_ :
      CommRing B) (_ : Algebra R B),
      -- the `R`-algebra decomposition `S ≅ (∏ i, A i) × B`
      Nonempty (S ≃ₐ[R] ((Π i, A i) × B)) ∧
        -- (1) each `A i` is finite over `R` (locality and local-hom are recorded
        --     by the instance binders above)
        (∀ i, Module.Finite R (A i)) ∧
          -- (2) each residue extension `κ → κ(m_{A i})` is purely inseparable and
          --     finite, where the `κ`-algebra structure on `κ(m_{A i})` comes from
          --     the residue field map of the local homomorphism `R → A i`
          (∀ i,
              letI : Algebra (ResidueField R) (ResidueField (A i)) :=
                (ResidueField.map (algebraMap R (A i))).toAlgebra
              IsPurelyInseparable (ResidueField R) (ResidueField (A i)) ∧
                Module.Finite (ResidueField R) (ResidueField (A i))) ∧
            -- (3) `R → B` is not quasi-finite at any prime of `B` lying over `m`
            (∀ (q : Ideal B) (hq : q.IsPrime),
              q.LiesOver (maximalIdeal R) → ¬@Algebra.QuasiFiniteAt R B _ _ _ q hq)
```

## Tag 04GK, a lemma

[Tag 04GK](https://stacks.math.columbia.edu/tag/04GK) in the Stacks Project.

**`CommAlgCat.FiniteEtale.isEquivalence_baseChange_residueField`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/FiniteEtale.lean, line 793](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/FiniteEtale.lean#L793). The attribute's comment: “The functor `S ↦ S/𝔪S` of the source is Mathlib's base change functor `CommAlgCat.FiniteEtale.baseChange R (IsLocalRing.ResidueField R)`, `S ↦ κ ⊗[R] S`; the canonical identification of the two is `Algebra.TensorProduct.quotIdealMapEquivQuotTensor`. `Equivalent via the functor` is `CategoryTheory.Functor.IsEquivalence` of that functor, stated as an instance as Mathlib states the sibling `FiniteEtale.fiber Ω Ω`. The object universe is pinned to `R`'s, as in Mathlib's `CommAlgCat.FiniteEtale.equivOfIsSepClosed`. See the module docstring.”. References: EGA IV (18.3.2), “local, I = maximal ideal”; EGA IV (18.5.15), “henselian local ring”; SGA 1 IX (1.8), “more general”; SGA 7 XIII (1.2.1), “the equivalence”; SGA 1 IX (1.8), “more general”; SGA 3 VIIB (1.6.E), “(b), special case”; SGA 7 IX (2.2.4), “more general”.

> **Stacks 04GK.** Let `(R, 𝔪, κ)` be a henselian local ring. Base change along the residue map
> `R → κ`, which on objects is `S ↦ κ ⊗[R] S ≅ S/𝔪S`, is an equivalence from the category of finite
> étale `R`-algebras to the category of finite étale `κ`-algebras.

```lean
public instance CommAlgCat.FiniteEtale.isEquivalence_baseChange_residueField (R : Type u)
    [CommRing R] [HenselianLocalRing R] :
    (CommAlgCat.FiniteEtale.baseChange.{u, u, u} R (ResidueField R)).IsEquivalence
```

## Tag 04GL, a lemma

[Tag 04GL](https://stacks.math.columbia.edu/tag/04GL) in the Stacks Project.

**`Algebra.IsUnramifiedIn.exists_algEquiv_prod_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Unramified.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Unramified.lean#L359). The attribute's comment: “The source's factors `Aᵢ` with `R → Aᵢ` surjective are spelled as the quotients `R ⧸ Iᵢ` with their canonical maps (`Ideal.quotientKerAlgEquivOfSurjective` identifies the two forms), and `Iᵢ ≠ ⊤` records that the factor is nonzero, the source's locality of `Aᵢ` then being automatic. Strictly henselian is `HenselianLocalRing R` with `IsSepClosed (ResidueField R)`. The hypothesis is weakened from `Algebra.Unramified R S` to finite type together with `Algebra.IsUnramifiedIn S 𝔪`, which is what the proof uses; the source's hypothesis implies it by `Algebra.unramified_iff_forall`. See the module docstring.”.

> **Unramified algebras over a strictly henselian local ring** (Stacks 04GL). Let `(R, 𝔪, κ)` be
> a strictly henselian local ring and let `S` be a finite type `R`-algebra which is unramified at
> every prime lying over `𝔪` — for instance an unramified `R`-algebra. Then there are finitely many
> proper ideals `I₁, …, Iₙ` of `R` and an `R`-algebra `B` no prime of which lies over `𝔪`, together
> with an isomorphism of `R`-algebras `S ≅ (R/I₁) × ⋯ × (R/Iₙ) × B`.

```lean
public theorem Algebra.IsUnramifiedIn.exists_algEquiv_prod_quotient
    (R : Type u) [CommRing R] [HenselianLocalRing R] [IsSepClosed (ResidueField R)]
    (S : Type v) [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    (hS : Algebra.IsUnramifiedIn S (maximalIdeal R)) :
    ∃ (n : ℕ) (I : Fin n → Ideal R) (B : Type (max u v)) (_ : CommRing B) (_ : Algebra R B),
      Nonempty (S ≃ₐ[R] (∀ i, R ⧸ I i) × B) ∧ (∀ i, I i ≠ ⊤) ∧
        ∀ q : Ideal B, q.IsPrime → ¬ q.LiesOver (maximalIdeal R)
```

## Tag 04GM, a lemma

[Tag 04GM](https://stacks.math.columbia.edu/tag/04GM) in the Stacks Project.

**`henselianLocalRing_of_isAdicComplete_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Criteria.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Criteria.lean#L342). References: EGA IV (18.5.14), “local case”; EGA IV (18.5.16), “special case”; SGA 3 X (4.0), “partial”.

> A complete local ring is Henselian: `IsAdicComplete.henselianRing` provides
> the lifting property, and we transport the simple-root hypothesis along
> `Ideal.Quotient.mk`.

```lean
theorem henselianLocalRing_of_isAdicComplete_maximalIdeal
    (R : Type*) [CommRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R] :
    HenselianLocalRing R
```

## Tag 06RS, a lemma

[Tag 06RS](https://stacks.math.columbia.edu/tag/06RS) in the Stacks Project.

**`henselianLocalRing_of_krullDimLE_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Criteria.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Criteria.lean#L590).

> **Stacks Tag 06RS / Lemma 10.153.10.** A local ring of Krull dimension `0` is henselian.

```lean
theorem henselianLocalRing_of_krullDimLE_zero (R : Type*) [CommRing R] [IsLocalRing R]
  [Ring.KrullDimLE 0 R] :
    HenselianLocalRing R
```

## Tag 08HQ, a lemma

[Tag 08HQ](https://stacks.math.columbia.edu/tag/08HQ) in the Stacks Project.

**`existsUnique_algHom_henselian_of_residue_datum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/EtaleLifting/HenselianRetraction.lean, line 761](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/EtaleLifting/HenselianRetraction.lean#L761).

> **Stacks Tag 08HQ** (map into henselian). Let `R → S` be a ring map with `S`
> henselian local, `p = R ∩ m_S` the contraction of the maximal ideal. Given an
> etale `R`-algebra `A`, a prime `q` of `A` lying over `p`, and a
> `κ(p)`-algebra map `τ : κ(q) → κ(m_S)`, there is a unique `R`-algebra map
> `f : A → S` with `q = f⁻¹(m_S)` inducing `τ` on residue fields.

```lean
theorem existsUnique_algHom_henselian_of_residue_datum
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [HenselianLocalRing S]
    (A : Type*) [CommRing A] [Algebra R A] [Algebra.Etale R A]
    -- `q` is a prime of `A` lying over `p = R ∩ m_S`.
    (𝔮 : Ideal A) [𝔮.IsPrime]
    (hlo : 𝔮.comap (algebraMap R A) = (maximalIdeal S).comap (algebraMap R S))
    -- `τ : κ(q) → κ(m_S)` is a `κ(p)`-algebra map: the triangle over `κ(p)` commutes.
    (τ : 𝔮.ResidueField →+* (maximalIdeal S).ResidueField)
    (hτ : τ.comp (Ideal.ResidueField.map _ 𝔮 (algebraMap R A) hlo.symm)
        = Ideal.ResidueField.map _ (maximalIdeal S) (algebraMap R S) rfl) :
    -- There is a unique `R`-algebra map `f : A → S` with `q = f⁻¹(m_S)` inducing `τ`.
    ∃! f : A →ₐ[R] S,
      ∃ (h : (maximalIdeal S).comap f.toRingHom = 𝔮),
        Ideal.ResidueField.map 𝔮 (maximalIdeal S) f.toRingHom h.symm = τ
```

## Tag 04GX, a lemma

[Tag 04GX](https://stacks.math.columbia.edu/tag/04GX) in the Stacks Project.

**`bijOn_solutions_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/EtaleLifting/SolutionsBijection.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/EtaleLifting/SolutionsBijection.lean#L478).

> **Stacks Tag 04GX.**
> Let `φ : R → S` be a local homomorphism of strictly henselian local rings and let
> `P_1, …, P_n ∈ R[x_1, …, x_n]` be polynomials such that `R[x_1, …, x_n]/(P_1, …, P_n)` is
> étale over `R`. Then the coordinatewise map `r ↦ (fun i => φ (r i))` induces a bijection
> between the solutions of the `P_i` over `R` and the solutions of their images `P_i^φ` over
> `S`.

```lean
theorem bijOn_solutions_of_etale
    {R S : Type*} [CommRing R] [CommRing S]
    [HenselianLocalRing R] [HenselianLocalRing S]
    [IsSepClosed (IsLocalRing.ResidueField R)] [IsSepClosed (IsLocalRing.ResidueField S)]
    (φ : R →+* S) (hφ : IsLocalHom φ)
    (n : ℕ) (P : Fin n → MvPolynomial (Fin n) R)
    [Algebra.Etale R (MvPolynomial (Fin n) R ⧸ Ideal.span (Set.range P))] :
    Set.BijOn (fun r : Fin n → R => (fun i => φ (r i) : Fin n → S))
      {r : Fin n → R | ∀ i, MvPolynomial.eval r (P i) = 0}
      {s : Fin n → S | ∀ i, MvPolynomial.eval s (MvPolynomial.map φ (P i)) = 0}
```

## Tag 05D6, a lemma

[Tag 05D6](https://stacks.math.columbia.edu/tag/05D6) in the Stacks Project.

**`Module.exists_sSupIndep_finitePresentation_of_countable_span_of_mittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Henselian.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/Henselian.lean#L626). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 059M, 059N, 059P, 059R, 05CQ and 0AS7; countable generation as a countable spanning set, as in 0590; and the direct sum decomposition internally, as an independent set of submodules of `M` with supremum `⊤`, as in 058W. Test data in the universe of `M`, whence `Small.{v} R`. See the module docstring.”.

> **Stacks 05D6.** Let `R` be a henselian local ring and let `M` be an `R`-module which is
> countably generated — it admits a countable spanning set — and Mittag-Leffler, the latter in the
> intrinsic form 059E (1): every map `f : P → M` from a finitely presented module dominates and is
> dominated by a map `g : P → Q` into a finitely presented module, domination meaning
> `Ker(f ⊗ id_T) = Ker(g ⊗ id_T)` for every `R`-module `T`. Then `M` is a direct sum of finitely
> presented `R`-modules, in the internal form: there is an independent set of finitely presented
> submodules of `M` whose supremum is `⊤`.

```lean
public theorem Module.exists_sSupIndep_finitePresentation_of_countable_span_of_mittagLeffler
    (R : Type u) [CommRing R] [HenselianLocalRing R] [Small.{v} R]
    (M : Type v) [AddCommGroup M] [Module R M]
    (hcg : ∃ s : Set M, s.Countable ∧ Submodule.span R s = ⊤)
    (hML : ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module R T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T)) :
    ∃ S : Set (Submodule R M), sSupIndep S ∧ sSup S = ⊤ ∧
      ∀ N ∈ S, Module.FinitePresentation R N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.153, Tag 04GE](https://stacks.math.columbia.edu/tag/04GE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
