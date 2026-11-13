---
declaration: section
origin: cited
lean: strictTransform, Stacks.Flatness.BlowupFlattening.stacks053I, fittingIdeal_strictTransform_affineBlowup_eq_top, isFiniteLocallyFreeOfRank_strictTransform_affineBlowup, exists_fg_ideal_strictTransform_isFiniteLocallyFreeOfRank
statement: formalized
proof: formalized
---

# 15.27 Blowing up and flatness

Section 15.27 of the Stacks Project, [Tag 0535](https://stacks.math.columbia.edu/tag/0535). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 053H, a definition

[Tag 053H](https://stacks.math.columbia.edu/tag/053H) in the Stacks Project.

**`strictTransform`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Blowup/StrictTransform.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Blowup/StrictTransform.lean#L45).

> The strict transform of an `R`-module `M` along the affine blowup algebra `R → R[I/a]`:
> the scalar extension `R[I/a] ⊗[R] M`, modulo the elements annihilated by some power of the
> image of `a`.

```lean
noncomputable def strictTransform (I : Ideal R) (a : R) [Fact (a ∈ I)]
    (M : Type v) [AddCommGroup M] [Module R M]
```

## Tag 053I, a lemma

[Tag 053I](https://stacks.math.columbia.edu/tag/053I) in the Stacks Project.

**`Stacks.Flatness.BlowupFlattening.stacks053I`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/BlowupFlattenAssembly.lean, line 1039](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/BlowupFlattenAssembly.lean#L1039).

> **Stacks Tag 053I: flattening by blowing up.** Let `(R, 𝔪)` be a local domain with fraction
> field `K` and `𝔪 ≠ 0`, let `S` be a finite type `R`-algebra, let `M` be a finite `S`-module and
> let `A ⊆ K` be a valuation ring dominating `R`.  Then there is an admissible affine blowup chart
> `R[I/a]` — so `I ⊆ 𝔪` is finitely generated, the fibre ring of `R → R[I/a]` at `𝔪` is nonzero and
> `A` has center on `R[I/a]` — on which the strict transform of `S` is flat and of finite
> presentation over `R[I/a]` and the strict transform of `M` is flat over `R[I/a]` and finitely
> presented over the strict transform of `S`.
>
> The polynomial case is `Stacks.Flatness.BlowupFlattening.exists_admissiblePair_mvPolynomial`.  The
>   reduction to it is
> the source's first step: write `S` as a quotient of `P = R[x_1, …, x_n]` and apply the polynomial
> case to the `P`-module `N = S ⊕ M`.  The strict transform of `N` is the product of the strict
> transforms of `S` and of `M` (`Stacks.Flatness.BlowupFlattening.prodLinearEquiv`, the version of
> `strictTransform.prodEquiv` that is linear over the strict transform of `P`), so flatness and
> finite presentation of each summand follow from `Module.Flat.prod_iff` and
> `Module.FinitePresentation.prod_iff`.  Finite presentation of the strict transform of `S` as an
> `R[I/a]`-*algebra* is then
> `Algebra.FinitePresentation.of_surjective_of_module_finitePresentation`, and finite presentation
> of the strict transform of `M` over the strict transform of `S` is Stacks Tag 0561,
> `Module.FinitePresentation.of_restrictScalars_of_finiteType`.
>
> The statement deviates from the source in two ways: the
> hypothesis `𝔪 ≠ 0`, without which the conclusion is unsatisfiable, and clause (4) being read over
> `R[I/a]` rather than over `R`.

```lean
theorem stacks053I (hdom : Dominates R A) (hm : IsLocalRing.maximalIdeal R ≠ ⊥) (S : Type w)
    [CommRing S] [Algebra R S] [Algebra.FiniteType R S] (M : Type uM) [AddCommGroup M]
    [Module S M] [Module R M] [IsScalarTower R S M] [Module.Finite S M] :
    Stacks053IConclusion R A S M
```

## Tag 0CZM, a lemma

[Tag 0CZM](https://stacks.math.columbia.edu/tag/0CZM) in the Stacks Project.

**`fittingIdeal_strictTransform_affineBlowup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Blowup.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Blowup.lean#L182).

> **Stacks Tag 0CZM.** Let `M` be a finite module over a commutative ring `R`, and let `I` be
> its `k`th Fitting ideal.  On the affine blowup chart `R[I/a]` associated to any `a ∈ I`, the
> `k`th Fitting ideal of the strict transform of `M` — the quotient of `R[I/a] ⊗[R] M` by its
> `a`-power torsion — is the unit ideal.

```lean
theorem fittingIdeal_strictTransform_affineBlowup_eq_top
    {R : Type u} [CommRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (k : ℕ) (a : R) (ha : a ∈ fittingIdeal (R := R) (M := M) (k : ℤ))
    (S : Type w) [CommRing S] [Algebra R S] [IsLocalization.Away a S] :
    let I := fittingIdeal (R := R) (M := M) (k : ℤ)
    let R' := affineBlowupAlgebra I a S
    let M' := (R' ⊗[R] M) ⧸
      Ideal.primaryComponent (R' ⊗[R] M)
        (Ideal.span {algebraMap R R' a})
    fittingIdeal (R := R') (M := M') (k : ℤ) = ⊤
```

## Tag 0CZN, a lemma

[Tag 0CZN](https://stacks.math.columbia.edu/tag/0CZN) in the Stacks Project.

**`isFiniteLocallyFreeOfRank_strictTransform_affineBlowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Blowup.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Blowup.lean#L306).

> **Stacks Tag 0CZN.** Let `M` be a finite module over a commutative ring `R`, and let `I` be
> its `k`th Fitting ideal.  Suppose that the localization of `M` at every prime outside `V(I)` is
> free of rank `k`.  Then the strict transform of `M` on the affine blowup chart `R[I/a]`, for any
> `a ∈ I`, is finite locally free of rank `k`.

```lean
theorem isFiniteLocallyFreeOfRank_strictTransform_affineBlowup
    {R : Type u} [CommRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (k : ℕ)
    (hfree : ∀ (p : Ideal R) [p.IsPrime],
      ¬ fittingIdeal (R := R) (M := M) (k : ℤ) ≤ p →
        Nonempty ((Fin k → Localization.AtPrime p) ≃ₗ[Localization.AtPrime p]
          LocalizedModule.AtPrime p M))
    (a : R) (ha : a ∈ fittingIdeal (R := R) (M := M) (k : ℤ))
    (S : Type w) [CommRing S] [Algebra R S] [IsLocalization.Away a S] :
    let I := fittingIdeal (R := R) (M := M) (k : ℤ)
    let R' := affineBlowupAlgebra I a S
    let M' := (R' ⊗[R] M) ⧸
      Ideal.primaryComponent (R' ⊗[R] M)
        (Ideal.span {algebraMap R R' a})
    Module.IsFiniteLocallyFreeOfRank R' M' k
```

## Tag 0BBJ, a lemma

[Tag 0BBJ](https://stacks.math.columbia.edu/tag/0BBJ) in the Stacks Project.

**`exists_fg_ideal_strictTransform_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Blowup.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/Blowup.lean#L616).

> **Stacks Tag 0BBJ.** Let `M` be a finite module over a commutative ring `R`.  If the
> localization of `M` away from `f` is finite locally free of rank `r`, then there is a finitely
> generated ideal `I` with the same vanishing locus as `f` such that, on every affine blowup chart
> `R[I/a]` with `a ∈ I`, the strict transform of `M` is finite locally free of rank `r`.

```lean
theorem exists_fg_ideal_strictTransform_isFiniteLocallyFreeOfRank
    {R : Type u} {M : Type v} [CommRing R] [AddCommGroup M] [Module R M] [Module.Finite R M]
    (f : R) (r : ℕ)
    (hf : Module.IsFiniteLocallyFreeOfRank (Localization.Away f)
      (LocalizedModule.Away f M) r) :
    ∃ I : Ideal R, I.FG ∧
      PrimeSpectrum.zeroLocus ({f} : Set R) = PrimeSpectrum.zeroLocus (I : Set R) ∧
      ∀ a : I,
        let _ : Fact ((a : R) ∈ I) := ⟨a.property⟩
        Module.IsFiniteLocallyFreeOfRank (Blowup I a) (strictTransform I a M) r
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.27, Tag 0535](https://stacks.math.columbia.edu/tag/0535)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
