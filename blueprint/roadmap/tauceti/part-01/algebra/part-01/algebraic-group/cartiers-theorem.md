---
declaration: theorem
origin: cited
lean: TauCeti.smoothCommHopfAlgProperty_of_charZero
statement: formalized
proof: formalized
---

# Cartier's theorem

a finite-type commutative Hopf algebra over a field of characteristic
zero is smooth. Equivalently, every affine group scheme of finite type over such a field is
smooth.

```lean
TauCeti.smoothCommHopfAlgProperty_of_charZero.{u, v} (k : Type u) [Field k] [CharZero k]
  (H : CommHopfAlgCat k) [Algebra.FiniteType k ↑H] : TauCeti.smoothCommHopfAlgProperty k H
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.smoothCommHopfAlgProperty_of_charZero`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.html#TauCeti.smoothCommHopfAlgProperty_of_charZero).

## Sources

- [Tau Ceti documentation: `TauCeti.smoothCommHopfAlgProperty_of_charZero`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.html#TauCeti.smoothCommHopfAlgProperty_of_charZero)
- [Source of `TauCeti.smoothCommHopfAlgProperty_of_charZero` in TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Smooth/CharZero.lean#L148)
