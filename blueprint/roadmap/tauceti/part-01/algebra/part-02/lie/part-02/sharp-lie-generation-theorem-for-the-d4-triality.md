---
declaration: theorem
origin: cited
lean: TauCeti.D4Triality.lieSpan_foldedGenerators_eq_top_iff
statement: formalized
proof: formalized
---

# Sharp Lie-generation theorem for the `D₄` triality fixed Lie subalgebra

Over any commutative ring `A`, the four folded `G₂` simple root vectors generate the entire
`14`-rank triality-fixed Lie subalgebra if and only if both `2` and `3` are units in `A`.

```lean
TauCeti.D4Triality.lieSpan_foldedGenerators_eq_top_iff.{u_1} (A : Type u_1) [CommRing A] :
  LieSubalgebra.lieSpan A
        (↥(LieEquiv.baseChange A TauCeti.D4Triality.trialityLieEquiv).fixedSubalgebra)
        (TauCeti.D4Triality.foldedGenerators A) =
      ⊤ ↔
    IsUnit 2 ∧ IsUnit 3
```

## Depends on

- [The Leibniz form of the Jacobi identity, for a positive definite `B` with even diagonal](../part-01/the-leibniz-form-of-the-jacobi-identity-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.D4Triality.lieSpan_foldedGenerators_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/TrialityD4/Generation.html#TauCeti.D4Triality.lieSpan_foldedGenerators_eq_top_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.D4Triality.lieSpan_foldedGenerators_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/NormTwoShell/TrialityD4/Generation.html#TauCeti.D4Triality.lieSpan_foldedGenerators_eq_top_iff)
- [Source of `TauCeti.D4Triality.lieSpan_foldedGenerators_eq_top_iff` in TauCeti/Algebra/Lie/NormTwoShell/TrialityD4/Generation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/NormTwoShell/TrialityD4/Generation.lean#L473)
