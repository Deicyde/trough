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
- [Source of `Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn` in TauCeti/NumberTheory/RamificationInertia/Galois.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/RamificationInertia/Galois.lean#L182)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/NumberFieldArithmetic/STATUS.md)
