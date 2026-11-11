---
declaration: theorem
origin: cited
lean: Polynomial.finite_setOf_natDegree_le_supNorm_le
statement: formalized
proof: formalized
---

# Northcott's theorem for integer polynomials

Only finitely many integer polynomials
have degree at most `n` and coefficient sup norm (naive height) at most `B`.

```lean
Polynomial.finite_setOf_natDegree_le_supNorm_le (n : ℕ) (B : ℝ) :
  {P | P.natDegree ≤ n ∧ P.supNorm ≤ B}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.finite_setOf_natDegree_le_supNorm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/SupNorm/Northcott.html#Polynomial.finite_setOf_natDegree_le_supNorm_le).

## Sources

- [Tau Ceti documentation: `Polynomial.finite_setOf_natDegree_le_supNorm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/SupNorm/Northcott.html#Polynomial.finite_setOf_natDegree_le_supNorm_le)
- [Source of `Polynomial.finite_setOf_natDegree_le_supNorm_le` in TauCeti/Analysis/Polynomial/SupNorm/Northcott.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Polynomial/SupNorm/Northcott.lean#L60)
