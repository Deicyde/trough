---
declaration: section
origin: cited
lean: Stacks.Smoothing.exists_approximate_solution_of_henselian_isGRing, Stacks.Smoothing.exists_localEtaleSolution_of_isGRing, IsLocalRing.isNoetherianRing_henselization, IsLocalRing.exists_ringEquiv_adicCompletion_henselization, IsLocalRing.injective_henselizationToAdicCompletion, IsLocalRing.isAlgebraic_of_isHenselization, IsLocalRing.finite_setOf_aeval_eq_zero_of_isHenselization, IsLocalRing.range_henselizationToAdicCompletion_eq_setOf_isAlgebraic
statement: formalized
proof: formalized
---

# 16.13 The approximation property for G-rings

Section 16.13 of the Stacks Project, [Tag 07QX](https://stacks.math.columbia.edu/tag/07QX). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07QY, a theorem

[Tag 07QY](https://stacks.math.columbia.edu/tag/07QY) in the Stacks Project.

**`Stacks.Smoothing.exists_approximate_solution_of_henselian_isGRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ApproximationHenselianGRing.lean#L239). The attribute's comment: “the full conclusion for a henselian local G-ring -- general `m`, `n` and every `N`, including `N = 0` -- with `𝔪^N R^∧` as the extension of `𝔪^N` to `AdicCompletion (maximalIdeal R) R`, and with NO carried hypotheses. All three of the source's cited inputs are formalized and used: Popescu's Theorem 07GC, reached from the G-ring hypothesis through Lemma 0AH2; and 07M7 and 04GG, which are consumed inside Lemma 0AH5 applied to the henselian pair `(R, 𝔪)`. Nothing else is assumed.”.

> **Stacks 07QY (the approximation property for G-rings).** Let `(R, 𝔪)` be a henselian local
> G-ring. A system of polynomial equations over `R` with a solution in the `𝔪`-adic completion
> `R^∧` has, for every `N`, a solution in `R` congruent to the given one modulo `𝔪 ^ N R^∧`.

```lean
theorem exists_approximate_solution_of_henselian_isGRing
    {R : Type u} [CommRing R] [HenselianLocalRing R] (hG : IsGRing R)
    {m n : ℕ} (f : Fin m → MvPolynomial (Fin n) R)
    (a : Fin n → AdicCompletion (maximalIdeal R) R)
    (ha : ∀ j, MvPolynomial.aeval a (f j) = 0) (N : ℕ) :
    ∃ b : Fin n → R,
      (∀ i, a i - algebraMap R (AdicCompletion (maximalIdeal R) R) (b i) ∈
        ((maximalIdeal R) ^ N).map (algebraMap R (AdicCompletion (maximalIdeal R) R))) ∧
      ∀ j, MvPolynomial.aeval b (f j) = 0
```

## Tag 07QZ, a theorem

[Tag 07QZ](https://stacks.math.columbia.edu/tag/07QZ) in the Stacks Project.

**`Stacks.Smoothing.exists_localEtaleSolution_of_isGRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ApproximationGRing.lean, line 754](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ApproximationGRing.lean#L754). The attribute's comment: “the conclusion for a Noetherian local G-ring, with NO hypothesis beyond the source's own: the appeal to Popescu's Theorem 07GC that the source makes here runs through Lemma 0AH2 and `indSmooth_of_isRegularRingMap`, which is proved. The instance `IsNoetherianRing R` is redundant, being the first component of `IsGRing` (Tag 07GH); it is present because the statement names the maximal ideal of `R^∧`, which is only known to be local once `R` is known to be Noetherian. Every part of the source's conclusion is here: the étale `R → R'`, the ideal `𝔪'` lying over `𝔪`, its MAXIMALITY, the residue field equality `κ(𝔪) = κ(𝔪')`, the solution `b` in `R'`, and the congruence `a_i - b_i ∈ (𝔪')^N R^∧` read along the embedding `R' ⊂ R^∧` — which is local at `𝔪'`, as in the source's `R ⊂ R'_{𝔪'} ⊂ R^h ⊂ R^∧`. Two further conclusions are added: the same congruence modulo the smaller `𝔪^N R^∧`, and the congruence of Lemma 0CAR in `(R'_{𝔪'})^∧`, which is the `approx` field of `LocalEtaleSolution`. See the module docstring.”.

> **Stacks 07QZ (the approximation property for G-rings).** Let `(R, 𝔪)` be a Noetherian local
> G-ring. A system of polynomial equations over `R` with a solution in the `𝔪`-adic completion
> `R^∧` has, for every `N`, a solution in an étale extension `R → R'` at a maximal ideal `𝔪'` over
> `𝔪` with `κ(𝔪) = κ(𝔪')`, congruent to the given solution modulo `(𝔪')^N R^∧`.
>
> The G-ring hypothesis is the source's, and it enters where the source puts it: through Popescu's
> Theorem 07GC and Lemma 0AH2, which is
> `Stacks.Smoothing.isIndSmoothAdicCompletion_of_isGRing`.

```lean
theorem exists_localEtaleSolution_of_isGRing
    {R : Type u} [CommRing R] [IsLocalRing R] [IsNoetherianRing R] (hG : IsGRing R)
    {m n : ℕ} (f : Fin m → MvPolynomial (Fin n) R) (N : ℕ)
    (a : Fin n → AdicCompletion (maximalIdeal R) R)
    (ha : ∀ j, MvPolynomial.aeval a (f j) = 0) :
    ∃ s : StacksDraft.ArtinApproximation.LocalEtaleSolution R f N a,
      s.prime.IsMaximal ∧
        ∃ ι : s.carrier →ₐ[R] AdicCompletion (maximalIdeal R) R,
          (∀ x : s.carrier,
              x ∈ s.prime ↔ ι x ∈ maximalIdeal (AdicCompletion (maximalIdeal R) R)) ∧
            (∀ i, a i - ι (s.sol i) ∈
              (s.prime ^ N).map (ι : s.carrier →+* AdicCompletion (maximalIdeal R) R)) ∧
            ∀ i, a i - ι (s.sol i) ∈
              (maximalIdeal R ^ N).map (algebraMap R (AdicCompletion (maximalIdeal R) R))
```

## Tag 0A1W, an example

[Tag 0A1W](https://stacks.math.columbia.edu/tag/0A1W) in the Stacks Project.

**`IsLocalRing.isNoetherianRing_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean#L102). The attribute's comment: “the henselization is Noetherian; this is Stacks 06LJ, proved in the library as `isNoetherianRing_of_isHenselization`”. References: EGA IV (18.6.6), “(v)”; SGA 4 VIII (4.1).

> **A henselization of a Noetherian local ring is Noetherian** (Stacks 06LJ, recalled in the
> discussion of Stacks 0A1W).

```lean
theorem isNoetherianRing_henselization (R : Type u) (Rh : Type v) [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh]
    [IsHenselization R (ResidueField R) Rh] : IsNoetherianRing Rh
```

**`IsLocalRing.exists_ringEquiv_adicCompletion_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean#L111). The attribute's comment: “the map on completions `R^∧ → (Rʰ)^∧` is an isomorphism; this is Stacks 06LJ, proved in the library as `exists_ringEquiv_adicCompletion_of_isHenselization`”.

> **The completion of a henselization is the completion of the base** (Stacks 06LJ, recalled in
> the discussion of Stacks 0A1W): `R^∧ → (Rʰ)^∧` is an isomorphism.

```lean
theorem exists_ringEquiv_adicCompletion_henselization (R Rh : Type u) [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh]
    [IsHenselization R (ResidueField R) Rh] :
    ∃ e : AdicCompletion (maximalIdeal R) R ≃+* AdicCompletion (maximalIdeal Rh) Rh,
      ∀ x : R, e (algebraMap R (AdicCompletion (maximalIdeal R) R) x) =
        algebraMap Rh (AdicCompletion (maximalIdeal Rh) Rh) (algebraMap R Rh x)
```

**`IsLocalRing.injective_henselizationToAdicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean#L181). The attribute's comment: “the henselization is a subring of the completion: the canonical map is injective”.

> **A henselization of a Noetherian local ring is a subring of the completion** (Stacks 0A1W).
> The canonical map `Rʰ → R^∧` is faithfully flat, because it is flat — the completion is flat over
> `R` and the henselization is ind-étale over `R` — and local; hence it is injective.

```lean
theorem injective_henselizationToAdicCompletion :
    Function.Injective (henselizationToAdicCompletion R Rh)
```

**`IsLocalRing.isAlgebraic_of_isHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean#L241). The attribute's comment: “every element of the henselization is algebraic over `R`, equivalently over its fraction field”.

> **Every element of a henselization of a local domain is algebraic over it** (Stacks 0A1W).
> A henselization is a filtered colimit of étale algebras, so the element comes from an étale
> stage, where `isAlgebraic_of_etale` applies.

```lean
theorem isAlgebraic_of_isHenselization (R : Type u) [CommRing R] [IsDomain R] [IsLocalRing R]
    (Rh : Type v) [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh]
    [IsHenselization R (ResidueField R) Rh] (g : Rh) : IsAlgebraic R g
```

**`IsLocalRing.finite_setOf_aeval_eq_zero_of_isHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean#L261). The attribute's comment: “`Rʰ ⊆ Rʰ ⊗_R K` and `Rʰ ⊗_R K` is a finite product of field extensions of `K`; hence a nonzero polynomial over `R` has only finitely many roots in `Rʰ`”.

> **A nonzero polynomial has only finitely many roots in a henselization of a Noetherian local
> domain** (Stacks 0A1W). The henselization is flat over the base, so it injects into its fibre
> over the generic point, and that fibre is a finite product of field extensions of the fraction
> field by Stacks 0AH1; a nonzero polynomial has finitely many roots in each factor.

```lean
theorem finite_setOf_aeval_eq_zero_of_isHenselization (R : Type u) [CommRing R] [IsDomain R]
    [IsLocalRing R] [IsNoetherianRing R] (Rh : Type u) [CommRing Rh] [IsLocalRing Rh]
    [Algebra R Rh] [IsHenselization R (ResidueField R) Rh]
    (p : Polynomial R) (hp : p ≠ 0) :
    {g : Rh | Polynomial.aeval g p = 0}.Finite
```

**`IsLocalRing.range_henselizationToAdicCompletion_eq_setOf_isAlgebraic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/Henselization/AlgebraicInCompletion.lean#L420). The attribute's comment: “the conclusion of the example, with NO carried hypotheses: for a Noetherian local domain `R` which is a G-ring, the image of the henselization in `R^∧` is exactly the set of elements of `R^∧` algebraic over `R`. Algebraicity over the fraction field `K` is `IsAlgebraic R`, the source's own form `a_n f^n + ⋯ + a_0 = 0` with `a_i ∈ R` and `a_n ≠ 0`, which over a domain is equivalent to algebraicity over `K`. Both inclusions are proved: `⊆` is `isAlgebraic_of_isHenselization`, and `⊇` uses Theorem 07QZ (`Stacks.Smoothing.exists_localEtaleSolution_of_isGRing`, unconditional), the factorization of its étale solution through `Rʰ` (`exists_algHom_eq_of_etale`, proved here rather than taken from the source's remark that the embedding factors as `R' ⊂ R'_{𝔪'} ⊂ Rʰ ⊂ R^∧`), the finiteness of the root set in `Rʰ` (`finite_setOf_aeval_eq_zero_of_isHenselization`) and Krull's intersection theorem in `R^∧`. The other clauses of this tag -- that `Rʰ` is Noetherian, that `R^∧ → (Rʰ)^∧` is an isomorphism, that `Rʰ → R^∧` is injective, and the two statements about `Rʰ ⊗_R K` -- are registered separately above.”.

> **Stacks 0A1W, the conclusion of the example.** Let `R` be a Noetherian local domain with
> fraction field `K` which is a G-ring. Then the henselization `Rʰ`, viewed as a subring of the
> completion `R^∧`, is exactly the set of elements of `R^∧` that are algebraic over `K`.
>
> The inclusion `⊆` is `isAlgebraic_of_isHenselization`. For `⊇`, Theorem 07QZ produces, for each
> `N`, a root `g` of the same polynomial in an étale extension of `R`; that root is pushed into `Rʰ`
> by `exists_algHom_eq_of_etale` and satisfies `f - g ∈ (𝔪 R^∧)^N`. Since the polynomial has only
> finitely many roots in `Rʰ` and `⋂_N (𝔪 R^∧)^N = 0`, one of them must equal `f`.

```lean
theorem range_henselizationToAdicCompletion_eq_setOf_isAlgebraic [IsDomain R]
    (hG : IsGRing R) :
    Set.range (henselizationToAdicCompletion R Rh) =
      {x : AdicCompletion (maximalIdeal R) R | IsAlgebraic R x}
```

## Tag 0CAR, a lemma

[Tag 0CAR](https://stacks.math.columbia.edu/tag/0CAR) in the Stacks Project.

**`StacksDraft.ArtinApproximation.artinApproximationGRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ApproximationGRingEtale.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/ApproximationGRingEtale.lean#L614). The attribute's comment: “the full conclusion — étaleness of `A → A'`, `𝔭'` lying over `𝔭`, the solution in `A'`, the residue field equality `κ(𝔭) = κ(𝔭')` and the congruence `a_i - b_i ∈ (𝔭')^N (A'_{𝔭'})^∧` for every `i` and every `N` — in the spelling of `StacksDraft.ArtinApproximation.ArtinApproximationGRing`, with NO carried hypotheses. The source's proof has two inputs and both are proved. The second, Algebra Lemma 00U2 (10), is `etaleDescentAlongLocalization`, from the public `AlgebraicGeometry.exists_etale_pushout_of_localization`. The first is Theorem 07QZ, `Stacks.Smoothing.exists_localEtaleSolution_of_isGRing`, itself unconditional because Popescu's Theorem 07GC is (`indSmooth_of_isRegularRingMap`, resting on Lemma 07FJ `canBeResolvedInPositiveCharacteristic`, whose λ-choice repair is due to Brian Nugent); the shape 0CAR's proof consumes it in is `localApproximationProperty`. The reduction of 0CAR to 07QZ — the base change of the system to `A_𝔭`, the descent of the solution and its equations to a principal localization, the identification of `𝔭'` and of `A'_{𝔭'}` with `S_q`, the residue field equality and the transport of the congruence — is `artinApproximationGRing_of_local`.”.

> **Stacks 0CAR (Smoothing Ring Maps, Lemma 16.13.4).** Let `A` be a Noetherian ring, let `𝔭`
> be a prime of `A` such that `A_𝔭` is a G-ring, and let `f₁, …, f_m` be polynomials over `A` in
> `n` variables. If the system `f = 0` has a solution `(a₁, …, a_n)` in the completion of `A_𝔭`,
> then for every `N` there are an étale ring map `A → A'`, a prime `𝔭' ⊂ A'` lying over `𝔭` with
> `κ(𝔭) = κ(𝔭')`, and a solution `(b₁, …, b_n)` of the system in `A'` with
> `a_i - b_i ∈ (𝔭')^N (A'_{𝔭'})^∧`.
>
> Both inputs of the source's proof are proved: Theorem 07QZ is `localApproximationProperty` and
> Algebra, Lemma 00U2 (10) is `etaleDescentAlongLocalization`.

```lean
theorem artinApproximationGRing : ArtinApproximationGRing.{u}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.13, Tag 07QX](https://stacks.math.columbia.edu/tag/07QX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
