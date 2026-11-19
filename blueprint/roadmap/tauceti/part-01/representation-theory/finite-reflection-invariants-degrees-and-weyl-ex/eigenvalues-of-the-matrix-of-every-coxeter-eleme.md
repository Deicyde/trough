---
declaration: theorem
origin: cited
lean: TauCeti.Coxeter.eigenvalues_of_hasCartanType_E8
statement: formalized
proof: formalized
---

# Eigenvalues of the matrix of every Coxeter element of type `E₈` on the simple roots

`exp (2πi e / 30)` for the exponents `e = 1, 7, 11, 13, 17, 19, 23, 29`, each once.

```lean
TauCeti.Coxeter.eigenvalues_of_hasCartanType_E8.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2}
  {M : Type u_3} {N : Type u_4} [DecidableEq ι] [CommRing R] [AddCommGroup M] [_root_.Module R M]
  [AddCommGroup N] [_root_.Module R N] {P : RootPairing ι R M N} [P.IsCrystallographic] [IsDomain R]
  [CharZero R] {b : P.Base} (h : TauCeti.HasCartanType P b TauCeti.DynkinType.E8)
  {l : List ↥b.support} (hnd : l.Nodup) (hall : ∀ (i : ↥b.support), i ∈ l)
  {W : Matrix ↥b.support ↥b.support ℤ} (hW : b.ActsBy (TauCeti.wordProd P b l) W) :
  (∀ (ζ : ℂ),
      ζ ∈ (W.map ⇑(Int.castRingHom ℂ)).charpoly.roots ↔
        ∃ e ∈ TauCeti.Coxeter.e8Exponents, Complex.exp (2 * ↑Real.pi * Complex.I * (↑e / 30)) = ζ) ∧
    (W.map ⇑(Int.castRingHom ℂ)).charpoly.roots.Nodup
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Coxeter.eigenvalues_of_hasCartanType_E8`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Eigen.html#TauCeti.Coxeter.eigenvalues_of_hasCartanType_E8).

## Sources

- [Tau Ceti documentation: `TauCeti.Coxeter.eigenvalues_of_hasCartanType_E8`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Eigen.html#TauCeti.Coxeter.eigenvalues_of_hasCartanType_E8)
- [Source of `TauCeti.Coxeter.eigenvalues_of_hasCartanType_E8` in TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Eigen.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Coxeter/Element/Eigen.lean#L111)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
