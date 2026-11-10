---
declaration: theorem
origin: cited
lean: TauCeti.eq_zero_of_two_eq_zero_of_aeval_X_X_eq_zero
statement: formalized
proof: formalized
---

# The symmetric 2-cocycle lemma when `2 = 0`, at powers of two

If `2 = 0` in `R`, a
homogeneous symmetric additive 2-cocycle `f` of degree `2ᵏ` over `R` with zero diagonal
`f(X, X) = 0` is zero.

```lean
TauCeti.eq_zero_of_two_eq_zero_of_aeval_X_X_eq_zero.{u_1} {R : Type u_1} [CommRing R] (h2 : 2 = 0)
  {k : ℕ} {f : MvPolynomial (Fin 2) R} (hh : f.IsHomogeneous (2 ^ k)) (hs : f.IsSymmetric)
  (hf : f.IsAddCocycle₂) (hd : (MvPolynomial.aeval ![Polynomial.X, Polynomial.X]) f = 0) : f = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eq_zero_of_two_eq_zero_of_aeval_X_X_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/CharTwo.html#TauCeti.eq_zero_of_two_eq_zero_of_aeval_X_X_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.eq_zero_of_two_eq_zero_of_aeval_X_X_eq_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/CharTwo.html#TauCeti.eq_zero_of_two_eq_zero_of_aeval_X_X_eq_zero)
- [Source of `TauCeti.eq_zero_of_two_eq_zero_of_aeval_X_X_eq_zero` in TauCeti/RingTheory/FormalGroup/SymmetricCocycle/CharTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/SymmetricCocycle/CharTwo.lean#L111)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
