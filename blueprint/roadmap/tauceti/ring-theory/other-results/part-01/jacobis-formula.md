---
declaration: theorem
origin: cited
lean: Derivation.leibniz_det
statement: formalized
proof: formalized
---

# Jacobi's formula

a derivation `D` differentiates the determinant of `M` as the trace of
the adjugate of `M` times the entrywise derivative of `M`.

```lean
Derivation.leibniz_det.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2} [CommSemiring R] [CommRing A]
  [Algebra R A] (D : Derivation R A A) {n : Type u_3} [Fintype n] [DecidableEq n]
  (M : Matrix n n A) : D M.det = (M.adjugate * M.map ⇑D).trace
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Derivation.leibniz_det`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/Determinant.html#Derivation.leibniz_det).

## Sources

- [Tau Ceti documentation: `Derivation.leibniz_det`](https://taucetiproject.org/docs/TauCeti/RingTheory/Derivation/Determinant.html#Derivation.leibniz_det)
- [Source of `Derivation.leibniz_det` in TauCeti/RingTheory/Derivation/Determinant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Derivation/Determinant.lean#L49)
