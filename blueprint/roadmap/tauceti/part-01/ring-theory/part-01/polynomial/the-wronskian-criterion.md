---
declaration: theorem
origin: cited
lean: Polynomial.linearIndependent_iff_hasseWronskian_ne_zero
statement: formalized
proof: formalized
---

# The Wronskian criterion

Over a field of characteristic zero, a family of polynomials is
linearly independent if and only if its Hasse Wronskian is nonzero.

```lean
Polynomial.linearIndependent_iff_hasseWronskian_ne_zero.{u_3} {m : ℕ} {K : Type u_3} [Field K]
  [CharZero K] {g : Fin m → Polynomial K} : LinearIndependent K g ↔ Polynomial.hasseWronskian g ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.linearIndependent_iff_hasseWronskian_ne_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/HasseWronskian.html#Polynomial.linearIndependent_iff_hasseWronskian_ne_zero).

## Sources

- [Tau Ceti documentation: `Polynomial.linearIndependent_iff_hasseWronskian_ne_zero`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/HasseWronskian.html#Polynomial.linearIndependent_iff_hasseWronskian_ne_zero)
- [Source of `Polynomial.linearIndependent_iff_hasseWronskian_ne_zero` in TauCeti/RingTheory/Polynomial/HasseWronskian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Polynomial/HasseWronskian.lean#L226)
