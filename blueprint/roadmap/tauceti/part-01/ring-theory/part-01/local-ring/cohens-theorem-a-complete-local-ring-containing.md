---
declaration: theorem
origin: cited
lean: TauCeti.exists_residueFieldSection
statement: formalized
proof: formalized
---

# Cohen's theorem: a complete local ring containing a field has a coefficient field

If the
complete local ring `R` is an algebra over some field `k`, then reduction `R → ResidueField R` has
a ring homomorphism section. When `k` is perfect, `TauCeti.residueFieldSection k R` is even a
`k`-algebra section. In general a `k`-linear section need not exist.

```lean
TauCeti.exists_residueFieldSection.{u_1, u_2} (k : Type u_1) (R : Type u_2) [Field k] [CommRing R]
  [IsLocalRing R] [Algebra k R] [IsAdicComplete (IsLocalRing.maximalIdeal R) R] :
  ∃ s, ∀ (a : IsLocalRing.ResidueField R), (IsLocalRing.residue R) (s a) = a
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_residueFieldSection`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/CoefficientField.html#TauCeti.exists_residueFieldSection).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_residueFieldSection`](https://taucetiproject.org/docs/TauCeti/RingTheory/LocalRing/CoefficientField.html#TauCeti.exists_residueFieldSection)
- [Source of `TauCeti.exists_residueFieldSection` in TauCeti/RingTheory/LocalRing/CoefficientField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LocalRing/CoefficientField.lean#L127)
