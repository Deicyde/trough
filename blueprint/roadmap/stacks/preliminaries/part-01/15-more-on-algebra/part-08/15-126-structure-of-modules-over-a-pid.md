---
declaration: section
origin: cited
lean: summand_sum_cyclic_iff_lifting, generalizedValuationRing_tfae, finitePresentation_equiv_directSum_quotient_span_singleton, finitePresentation_summand_fin_directSum_quotient_span_singleton, IsElementaryDivisorDomain, IsBezout, isBezout_of_isElementaryDivisorDomain, isBezout_localization_and_valuationRing_atPrime_and_iff
statement: formalized
proof: formalized
---

# 15.126 Structure of modules over a PID

Section 15.126 of the Stacks Project, [Tag 0ASL](https://stacks.math.columbia.edu/tag/0ASL). 10 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ASM, a lemma

[Tag 0ASM](https://stacks.math.columbia.edu/tag/0ASM) in the Stacks Project.

**`summand_sum_cyclic_iff_lifting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Warfield.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Warfield.lean#L163).

> For a commutative ring `R` and an `R`-module `P`, `P` is a direct summand of a direct sum of
> modules `R / f R` if and only if every linear map from `P` lifts along every short exact sequence
> `0 → A → B → C → 0` satisfying `f A = A ∩ f B` for all `f ∈ R`.

```lean
theorem summand_sum_cyclic_iff_lifting
    (R : Type u) [CommRing R] (P : Type v) [AddCommGroup P] [Module R P] :
    IsSummandOfSumCyclic R P ↔ LiftingProperty R P
```

## Tag 0ASN, a lemma

[Tag 0ASN](https://stacks.math.columbia.edu/tag/0ASN) in the Stacks Project.

**`generalizedValuationRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Generalized.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Generalized.lean#L107).

> For a nonzero commutative ring, total divisibility, being a local Bézout ring, and total
> inclusion of ideals are equivalent. In particular, all three properties hold for a valuation
> ring.

```lean
theorem generalizedValuationRing_tfae (R : Type u) [CommRing R] [Nontrivial R] :
    List.TFAE
        [@Std.Total R (· ∣ ·),
          IsBezout R ∧ IsLocalRing R,
          @Std.Total (Ideal R) (· ≤ ·)] ∧
      (∀ [IsDomain R] [ValuationRing R],
        @Std.Total R (· ∣ ·) ∧
          (IsBezout R ∧ IsLocalRing R) ∧
          @Std.Total (Ideal R) (· ≤ ·))
```

## Tag 0ASP, a lemma

[Tag 0ASP](https://stacks.math.columbia.edu/tag/0ASP) in the Stacks Project.

**`finitePresentation_equiv_directSum_quotient_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Generalized.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Generalized.lean#L407).

> Every finitely presented module over a local Bézout ring is isomorphic to a finite direct
> sum of quotients by principal ideals.

```lean
theorem finitePresentation_equiv_directSum_quotient_span_singleton
    (R : Type u) [CommRing R] [IsBezout R] [IsLocalRing R]
    (M : Type v) [AddCommGroup M] [Module R M] [Module.FinitePresentation R M] :
    ∃ (n : ℕ) (f : Fin n → R),
      Nonempty (M ≃ₗ[R] ⨁ i : Fin n, R ⧸ Ideal.span {f i})
```

## Tag 0ASQ, a lemma

[Tag 0ASQ](https://stacks.math.columbia.edu/tag/0ASQ) in the Stacks Project.

**`finitePresentation_summand_fin_directSum_quotient_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Generalized.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Generalized.lean#L652).

> Every finitely presented module over a commutative ring whose localizations at maximal ideals
> are Bézout rings is a direct summand of a finite direct sum of quotients by principal ideals.

```lean
theorem finitePresentation_summand_fin_directSum_quotient_span_singleton
    (R : Type u) [CommRing R]
    (hR : ∀ (m : Ideal R) [m.IsMaximal], IsBezout (Localization.AtPrime m))
    (M : Type v) [AddCommGroup M] [Module R M] [Module.FinitePresentation R M] :
    ∃ (n : ℕ) (f : Fin n → R)
      (i : M →ₗ[R] ⨁ j, R ⧸ Ideal.span {f j})
      (p : (⨁ j, R ⧸ Ideal.span {f j}) →ₗ[R] M),
      p.comp i = LinearMap.id
```

## Tag 0ASR, a definition

[Tag 0ASR](https://stacks.math.columbia.edu/tag/0ASR) in the Stacks Project.

**`IsElementaryDivisorDomain`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ElementaryDivisorDomain.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain.lean#L90). The tag is given by the `attribute` command at [StacksFrontier/RingTheory/ElementaryDivisorDomain.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain.lean#L101). The attribute's comment: “(2) An elementary divisor domain: every rectangular matrix with at least one row and one column can be brought into Smith normal form by invertible row and column operations.”.

> `R` is an *elementary divisor domain* if for all `n, m ≥ 1` and every
> `n × m` matrix `A` there exist invertible matrices `U` (size `n`) and `V`
> (size `m`) such that `U * A * V` is in Smith normal form.

```lean
class IsElementaryDivisorDomain (R : Type*) [CommRing R] : Prop
```

Declarations registered for the tag:

- [`IsBezout`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsBezout#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/ElementaryDivisorDomain.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain.lean#L97) (StacksFrontier): “(1) A Bézout domain: every finitely generated ideal is principal.”.

## Tag 0ASS, a lemma

[Tag 0ASS](https://stacks.math.columbia.edu/tag/0ASS) in the Stacks Project.

**`isBezout_of_isElementaryDivisorDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ElementaryDivisorDomain.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain.lean#L164).

> **Stacks 0ASS**.
> Every elementary divisor domain is a Bézout ring: if `R` is an elementary divisor
> domain, then every finitely generated ideal of `R` is principal (`IsBezout R`).

```lean
theorem isBezout_of_isElementaryDivisorDomain {R : Type*} [CommRing R]
    [IsElementaryDivisorDomain R] : IsBezout R
```

## Tag 0AST, a lemma

[Tag 0AST](https://stacks.math.columbia.edu/tag/0AST) in the Stacks Project.

**`isBezout_localization_and_valuationRing_atPrime_and_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ElementaryDivisorDomain/Bezout.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain/Bezout.lean#L70).

> Localizations of a Bézout domain are Bézout, its local rings are valuation rings, and an
> arbitrary local domain is Bézout if and only if it is a valuation ring.

```lean
theorem isBezout_localization_and_valuationRing_atPrime_and_iff
    {R Rₘ A : Type*} [CommRing R] [IsDomain R] [IsBezout R]
    (M : Submonoid R) [CommRing Rₘ] [Algebra R Rₘ] [IsLocalization M Rₘ]
    (p : Ideal R) [p.IsPrime]
    [CommRing A] [IsDomain A] [IsLocalRing A] :
    IsBezout Rₘ ∧
      ValuationRing (Localization.AtPrime p) ∧
      (IsBezout A ↔ ValuationRing A)
```

## Tag 0ASU, a lemma

[Tag 0ASU](https://stacks.math.columbia.edu/tag/0ASU) in the Stacks Project.

**`finite_submodule_free_and_finitePresentation_split_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ElementaryDivisorDomain/Bezout.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain/Bezout.lean#L455).

> Over a Bézout domain, finite submodules of free modules are free. Every finitely presented
> module splits as the direct sum of its finite free torsion quotient and its torsion submodule,
> which is itself a summand of a finite direct sum of quotients by nonzero principal ideals.

```lean
theorem finite_submodule_free_and_finitePresentation_split_torsion
    (R : Type u) [CommRing R] [IsDomain R] [IsBezout R] :
    (∀ (F : Type v) [AddCommGroup F] [Module R F] [Module.Free R F]
      (N : Submodule R F) [Module.Finite R N], Module.Free R N) ∧
    (∀ (M : Type w) [AddCommGroup M] [Module R M] [Module.FinitePresentation R M],
      Module.Finite R (M ⧸ Submodule.torsion R M) ∧
      Module.Free R (M ⧸ Submodule.torsion R M) ∧
      Nonempty (M ≃ₗ[R] (M ⧸ Submodule.torsion R M) × Submodule.torsion R M) ∧
      ∃ (n : ℕ) (f : Fin n → R),
        (∀ j, f j ≠ 0) ∧
        ∃ (i : Submodule.torsion R M →ₗ[R] ⨁ j, R ⧸ Ideal.span {f j})
          (p : (⨁ j, R ⧸ Ideal.span {f j}) →ₗ[R] Submodule.torsion R M),
          p.comp i = LinearMap.id)
```

## Tag 0ASV, a lemma

[Tag 0ASV](https://stacks.math.columbia.edu/tag/0ASV) in the Stacks Project.

**`finite_equiv_free_prod_directSum_quotient_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ElementaryDivisorDomain/PID.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain/PID.lean#L41).

> **Stacks 0ASV**.
> Every finite module over a principal ideal domain is isomorphic to the direct sum of a
> finite-rank free module and finitely many cyclic modules defined by nonzero elements.

```lean
theorem finite_equiv_free_prod_directSum_quotient_span_singleton
    (R : Type u) [CommRing R] [IsDomain R] [IsPrincipalIdealRing R]
    (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    ∃ (r n : ℕ) (f : Fin n → R),
      (∀ i, f i ≠ 0) ∧
        Nonempty (M ≃ₗ[R] (Fin r →₀ R) × ⨁ i : Fin n, R ⧸ Ideal.span {f i})
```

## Tag 0ASW, a lemma

[Tag 0ASW](https://stacks.math.columbia.edu/tag/0ASW) in the Stacks Project.

**`bezout_unimodular_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ElementaryDivisorDomain.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ElementaryDivisorDomain.lean#L313).

> **Stacks 0ASW**.
> Over a Bézout domain `R`, any row `f : Fin n → R` whose entries generate the unit ideal is the
> first row of some invertible `n × n` matrix over `R`.

```lean
theorem bezout_unimodular_completion {R : Type*} [CommRing R] [IsBezout R] [IsDomain R]
    {n : ℕ} [NeZero n] (f : Fin n → R)
    (hf : Ideal.span (Set.range f) = ⊤) :
    ∃ M : Matrix (Fin n) (Fin n) R, IsUnit M.det ∧ ∀ j : Fin n, M 0 j = f j
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.126, Tag 0ASL](https://stacks.math.columbia.edu/tag/0ASL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
