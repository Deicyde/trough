---
declaration: theorem
origin: cited
lean: Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn
statement: formalized
proof: formalized
---

# Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn

The order of the decomposition group is `e * f`, without a separability hypothesis on the
residue extension and for an arbitrary prime `P`.

```lean
Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn.{u_1, u_2, u_3} {R : Type u_1}
  {S : Type u_2} {G : Type u_3} [CommRing R] [CommRing S] [Algebra R S] [Group G]
  [MulSemiringAction G S] [IsGaloisGroup G R S] [IsDomain R] [IsDomain S] [Module.Finite R S]
  [Module.Flat R S] (p : Ideal R) [p.IsPrime] (P : Ideal S) [P.LiesOver p] [P.IsPrime] :
  Nat.card ↥(MulAction.stabilizer G P) = p.ramificationIdxIn S * p.inertiaDegIn S
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn`](https://taucetiproject.org/docs/TauCeti/NumberTheory/RamificationInertia/Galois.html#Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn).

## Sources

- [Tau Ceti documentation: `Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn`](https://taucetiproject.org/docs/TauCeti/NumberTheory/RamificationInertia/Galois.html#Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn)
- [Source of `Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn` in TauCeti/NumberTheory/RamificationInertia/Galois.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/RamificationInertia/Galois.lean#L182)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/NumberFieldArithmetic/STATUS.md)
