---
declaration: section
origin: cited
lean: Stacks.Examples.flat_perfectClosure_polynomial, Stacks.Examples.formallyUnramified_perfectClosure_polynomial, Stacks.Examples.not_formallyEtale_perfectClosure_polynomial, Stacks.Examples.flat_formallyUnramified_adicCompletion_and_not_formallyEtale, Stacks.Examples.formallyEtale_adicCompletion_of_isExcellent, Stacks.Examples.isExcellent_iff_formallyEtale_adicCompletion_maximalIdeal
statement: formalized
proof: formalized
---

# 110.44 Flat and formally unramified is not formally étale

Section 110.44 of the Stacks Project, [Tag 0G64](https://stacks.math.columbia.edu/tag/0G64). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G65, a lemma

[Tag 0G65](https://stacks.math.columbia.edu/tag/0G65) in the Stacks Project.

**`Stacks.Examples.flat_perfectClosure_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/PerfectClosureNotFormallyEtale.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/PerfectClosureNotFormallyEtale.lean#L295). The attribute's comment: “flatness of the example F_p[T] into its perfect closure”.

> **Flat and formally unramified is not formally étale**, flatness: the perfect closure of
> `𝔽ₚ[T]` is flat over `𝔽ₚ[T]`.

```lean
public theorem flat_perfectClosure_polynomial (p : ℕ) [Fact p.Prime] :
    Module.Flat (Polynomial (ZMod p)) (PerfectClosure (Polynomial (ZMod p)) p)
```

**`Stacks.Examples.formallyUnramified_perfectClosure_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/PerfectClosureNotFormallyEtale.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/PerfectClosureNotFormallyEtale.lean#L302). The attribute's comment: “formal unramifiedness of the example F_p[T] into its perfect closure”.

> **Flat and formally unramified is not formally étale**, formal unramifiedness: the perfect
> closure of `𝔽ₚ[T]` is formally unramified over `𝔽ₚ[T]`.

```lean
public theorem formallyUnramified_perfectClosure_polynomial (p : ℕ) [Fact p.Prime] :
    Algebra.FormallyUnramified (Polynomial (ZMod p)) (PerfectClosure (Polynomial (ZMod p)) p)
```

**`Stacks.Examples.not_formallyEtale_perfectClosure_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/PerfectClosureNotFormallyEtale.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/PerfectClosureNotFormallyEtale.lean#L309). The attribute's comment: “the example F_p[T] into its perfect closure is not formally etale”.

> **Flat and formally unramified is not formally étale**, the negative conjunct: the perfect
> closure of `𝔽ₚ[T]` is not formally étale over `𝔽ₚ[T]`.

```lean
public theorem not_formallyEtale_perfectClosure_polynomial (p : ℕ) [Fact p.Prime] :
    ¬ Algebra.FormallyEtale (Polynomial (ZMod p)) (PerfectClosure (Polynomial (ZMod p)) p)
```

## Tag 0G66, a lemma

[Tag 0G66](https://stacks.math.columbia.edu/tag/0G66) in the Stacks Project.

**`Stacks.Examples.flat_formallyUnramified_adicCompletion_and_not_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/ExcellentCompletionFormallyEtale.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/ExcellentCompletionFormallyEtale.lean#L325).

> Let `(A, 𝔪, κ)` be a Noetherian local ring of prime characteristic `p` with
> `[κ : κᵖ] < ∞`. Then the canonical map `A → A^∧` to the `𝔪`-adic completion is flat and
> formally unramified; if moreover `A` is regular but not excellent, it is not formally étale.

```lean
public theorem flat_formallyUnramified_adicCompletion_and_not_formallyEtale
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (p : ℕ) [Fact p.Prime]
    [CharP A p]
    [Module.Finite (frobenius (ResidueField A) (ringExpChar (ResidueField A))).fieldRange
      (ResidueField A)] :
    Module.Flat A (AdicCompletion (maximalIdeal A) A) ∧
      Algebra.FormallyUnramified A (AdicCompletion (maximalIdeal A) A) ∧
      (IsRegularLocalRing A → ¬ IsExcellent A →
        ¬ Algebra.FormallyEtale A (AdicCompletion (maximalIdeal A) A))
```

## Tag 0G68, a lemma

[Tag 0G68](https://stacks.math.columbia.edu/tag/0G68) in the Stacks Project.

**`Stacks.Examples.formallyEtale_adicCompletion_of_isExcellent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/ExcellentCompletionFormallyEtale.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/ExcellentCompletionFormallyEtale.lean#L346). The attribute's comment: “the forward implication, with no carried hypotheses; see the module docstring”.

> The forward implication of Stacks `0G68`: for a regular local ring of characteristic
> `p > 0` whose residue field has finite imperfection degree, excellence makes the canonical map
> to the maximal-ideal-adic completion formally étale.
>
> This needs none of Lemma `0G66`: excellence makes the map regular, Néron–Popescu writes the
> completion as a filtered colimit of smooth algebras, and formal unramifiedness upgrades that to
> formal smoothness.

```lean
public theorem formallyEtale_adicCompletion_of_isExcellent
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (p : ℕ) [Fact p.Prime] [CharP A p]
    [Module.Finite (frobenius (ResidueField A) (ringExpChar (ResidueField A))).fieldRange
      (ResidueField A)] (excellent : IsExcellent A) :
    Algebra.FormallyEtale A (AdicCompletion (maximalIdeal A) A)
```

**`Stacks.Examples.isExcellent_iff_formallyEtale_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/ExcellentCompletionFormallyEtale.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/ExcellentCompletionFormallyEtale.lean#L363). The attribute's comment: “both directions, with no carried hypotheses”.

> A regular local ring of characteristic `p > 0` whose residue field has finite imperfection
> degree is excellent if and only if the canonical map to its maximal-ideal-adic completion is
> formally étale.

```lean
public theorem isExcellent_iff_formallyEtale_adicCompletion_maximalIdeal
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (p : ℕ) [Fact p.Prime] [CharP A p]
    [Module.Finite (frobenius (ResidueField A) (ringExpChar (ResidueField A))).fieldRange
      (ResidueField A)] :
    IsExcellent A ↔ Algebra.FormallyEtale A (AdicCompletion (maximalIdeal A) A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.44, Tag 0G64](https://stacks.math.columbia.edu/tag/0G64)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
