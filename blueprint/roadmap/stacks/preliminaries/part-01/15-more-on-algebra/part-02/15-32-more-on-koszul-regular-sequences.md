---
declaration: section
origin: cited
lean: Cech.cechComplex_homology_isZero_of_isKoszulRegular, Koszul.exists_affineBlowup_algEquiv_mvPolynomial_quotient_of_isH1Regular, KoszulH1.cmp_surjective, Koszul.quasiRegular_and_h1Regular_baseChange_of_quotient_flat, Koszul.flat_quotient_span_of_isQuasiRegular_of_locallyNilpotent, Koszul.smooth_quotient_span_of_isQuasiRegular_of_locallyNilpotent
statement: formalized
proof: formalized
---

# 15.32 More on Koszul regular sequences

Section 15.32 of the Stacks Project, [Tag 0CEN](https://stacks.math.columbia.edu/tag/0CEN). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G6L, a lemma

[Tag 0G6L](https://stacks.math.columbia.edu/tag/0G6L) in the Stacks Project.

**`Cech.cechComplex_homology_isZero_of_isKoszulRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Cech/KoszulResolution.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Cech/KoszulResolution.lean#L233).

> The extended alternating Čech complex of a Koszul-regular sequence has zero cohomology in
> every degree other than the length of the sequence.

```lean
public theorem cechComplex_homology_isZero_of_isKoszulRegular
    {R : Type u} [CommRing R] {r : ℕ} (f : Fin r → R) (hf : Koszul.IsKoszulRegular f)
    (p : ℕ) (hp : p ≠ r) :
    CategoryTheory.Limits.IsZero ((Cech.cechComplex f R).homology p)
```

## Tag 0BIQ, a lemma

[Tag 0BIQ](https://stacks.math.columbia.edu/tag/0BIQ) in the Stacks Project.

**`Koszul.exists_affineBlowup_algEquiv_mvPolynomial_quotient_of_isH1Regular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/Blowup.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/Blowup.lean#L199).

> **Stacks Project, Tag 0BIQ.** The affine blowup algebra associated to an `H₁`-regular
> sequence is the polynomial algebra on the ratios of the remaining terms by the first term,
> modulo the evident linear relations.

```lean
public theorem exists_affineBlowup_algEquiv_mvPolynomial_quotient_of_isH1Regular
    {R : Type u} [CommRing R] {n : ℕ} (f : Fin (n + 1) → R)
    (hf : Koszul.IsH1Regular f) :
    Nonempty
      (affineBlowupAlgebraAway (Ideal.span (Set.range f)) (f 0) ≃ₐ[R]
        MvPolynomial (Fin n) R ⧸
          Ideal.span
            (Set.range fun i : Fin n ↦
              MvPolynomial.C (f 0) * MvPolynomial.X i - MvPolynomial.C (f i.succ)))
```

## Tag 063Q, a lemma

[Tag 063Q](https://stacks.math.columbia.edu/tag/063Q) in the Stacks Project.

**`KoszulH1.cmp_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/H1BaseChange.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/H1BaseChange.lean#L382).

> **Stacks Project, Tag 063Q.**  Let `A → B` be a ring map and `f_1, …, f_r` a
> sequence in `B` such that `B/(f_1, …, f_r)` is flat as an `A`-module.  Let
> `A → A'` be a ring map and set `B' = B ⊗_A A'`, `f'_i = f_i ⊗ 1`.  Then the
> canonical comparison map
>
>   Φ : H\_1(K\_•(B, f\_1, …, f\_r)) ⊗\_A A' ⟶ H\_1(K\_•(B', f'\_1, …, f'\_r))
>
> is surjective.
>
> Here the flatness hypothesis is stated as `Module.Flat A (B ⧸ Ideal.span (Set.range f))`,
> the quotient being viewed as an `A`-module by restriction of scalars along `A → B`.

```lean
theorem cmp_surjective
    {A B A' : Type*} [CommRing A] [CommRing B] [Algebra A B] [CommRing A'] [Algebra A A']
    {r : ℕ} (f : Fin r → B)
    (hflat : Module.Flat A (B ⧸ Ideal.span (Set.range f))) :
    Function.Surjective (cmp (A := A) (A' := A') f)
```

## Tag 0CEP, a lemma

[Tag 0CEP](https://stacks.math.columbia.edu/tag/0CEP) in the Stacks Project.

**`Koszul.quasiRegular_and_h1Regular_baseChange_of_quotient_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/FlatQuotient.lean, line 640](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/FlatQuotient.lean#L640).

> **Stacks Project, Tag 0CEP.** Suppose that `B / (f₁, …, fᵣ)` is flat over `A`. If `f` is
> quasi-regular, then its image in `B ⊗[A] A'` is quasi-regular; if `f` is H₁-regular, then its
> image is H₁-regular.

```lean
public theorem quasiRegular_and_h1Regular_baseChange_of_quotient_flat
    {A B A' : Type*} [CommRing A] [CommRing B] [Algebra A B]
    [CommRing A'] [Algebra A A'] {r : ℕ} (f : Fin r → B)
    (hflat : Module.Flat A (B ⧸ Ideal.span (Set.range f))) :
    (IsQuasiRegular B (List.ofFn f) →
      IsQuasiRegular (B ⊗[A] A')
        (List.ofFn (KoszulH1.fp (A := A) (A' := A') f))) ∧
    (Koszul.IsH1Regular f →
      Koszul.IsH1Regular (KoszulH1.fp (A := A) (A' := A') f))
```

## Tag 0CEQ, a lemma

[Tag 0CEQ](https://stacks.math.columbia.edu/tag/0CEQ) in the Stacks Project.

**`Koszul.flat_quotient_span_of_isQuasiRegular_of_locallyNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/FlatQuotient.lean, line 866](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/FlatQuotient.lean#L866).

> **Stacks Project, Tag 0CEQ.** A flat, finitely presented algebra remains flat after quotienting
> by lifts of a quasi-regular sequence whose reduced quotient is flat.

```lean
public theorem flat_quotient_span_of_isQuasiRegular_of_locallyNilpotent
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Module.Flat R S] [Algebra.FinitePresentation R S]
    (I : Ideal R) (hI : I ≤ nilradical R) {r : ℕ} (f : Fin r → S)
    (hqr : IsQuasiRegular (S ⧸ I.map (algebraMap R S))
      (List.ofFn (fun i ↦ Ideal.Quotient.mk (I.map (algebraMap R S)) (f i))))
    (hflat : Module.Flat (R ⧸ I)
      ((S ⧸ I.map (algebraMap R S)) ⧸
        Ideal.span (Set.range (fun i ↦
          Ideal.Quotient.mk (I.map (algebraMap R S)) (f i))))) :
    Module.Flat R (S ⧸ Ideal.span (Set.range f))
```

## Tag 0CER, a lemma

[Tag 0CER](https://stacks.math.columbia.edu/tag/0CER) in the Stacks Project.

**`Koszul.smooth_quotient_span_of_isQuasiRegular_of_locallyNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/FlatQuotient.lean, line 950](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Koszul/FlatQuotient.lean#L950).

> **Stacks Project, Tag 0CER.** A flat, finitely presented algebra remains smooth after
> quotienting by lifts of a quasi-regular sequence whose reduced quotient is smooth.

```lean
public theorem smooth_quotient_span_of_isQuasiRegular_of_locallyNilpotent
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [Module.Flat R S] [Algebra.FinitePresentation R S]
    (I : Ideal R) (hI : I ≤ nilradical R) {r : ℕ} (f : Fin r → S)
    (hqr : IsQuasiRegular (S ⧸ I.map (algebraMap R S))
      (List.ofFn (fun i ↦ Ideal.Quotient.mk (I.map (algebraMap R S)) (f i))))
    (hsmooth : Algebra.Smooth (R ⧸ I)
      ((S ⧸ I.map (algebraMap R S)) ⧸
        Ideal.span (Set.range (fun i ↦
          Ideal.Quotient.mk (I.map (algebraMap R S)) (f i))))) :
    Algebra.Smooth R (S ⧸ Ideal.span (Set.range f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.32, Tag 0CEN](https://stacks.math.columbia.edu/tag/0CEN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
