---
declaration: theorem
origin: cited
lean: Irrational.badlyApproximable_of_aeval_eq_zero, TauCeti.badlyApproximable_of_natDegree_minpoly_eq_two
statement: formalized
proof: formalized
---

# Liouville's theorem in degree two

An irrational root of a nonzero integer polynomial of
degree at most `2` is badly approximable.

```lean
Irrational.badlyApproximable_of_aeval_eq_zero {ξ : ℝ} (hξ : Irrational ξ) {f : Polynomial ℤ}
  (hf : f ≠ 0) (hdeg : f.natDegree ≤ 2) (hroot : (Polynomial.aeval ξ) f = 0) :
  TauCeti.BadlyApproximable ξ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Irrational.badlyApproximable_of_aeval_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/BadlyApproximable.html#Irrational.badlyApproximable_of_aeval_eq_zero).

## Other forms

**Liouville's theorem in degree two.** Formalized in Tau Ceti as [`TauCeti.badlyApproximable_of_natDegree_minpoly_eq_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/BadlyApproximable.html#TauCeti.badlyApproximable_of_natDegree_minpoly_eq_two).

```lean
TauCeti.badlyApproximable_of_natDegree_minpoly_eq_two {ξ : ℝ} (h : (minpoly ℚ ξ).natDegree = 2) :
  TauCeti.BadlyApproximable ξ
```

## Sources

- [Tau Ceti documentation: `Irrational.badlyApproximable_of_aeval_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/BadlyApproximable.html#Irrational.badlyApproximable_of_aeval_eq_zero)
- [Source of `Irrational.badlyApproximable_of_aeval_eq_zero` in TauCeti/NumberTheory/DiophantineApproximation/BadlyApproximable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/BadlyApproximable.lean#L207)
