---
declaration: theorem
origin: cited
lean: TauCeti.signedCheckedR_braid
statement: formalized
proof: formalized
---

# TauCeti.signedCheckedR_braid

The braid relation for signed checked R-matrices on two pairs of strands sharing the strand
`k`, the Yang-Baxter equation for the signed checked R-matrix.

```lean
TauCeti.signedCheckedR_braid.{u_1, u_2} {R : Type u_1} [CommRing R] {ι : Type u_2} [LinearOrder ι]
  (pos : ι → Prop) [DecidablePred pos] {n : ℕ} (s : R) {j k l : Fin n} (hjk : j ≠ k) (hkl : k ≠ l)
  (hjl : j ≠ l) :
  TauCeti.signedCheckedR pos s j k * TauCeti.signedCheckedR pos s k l *
      TauCeti.signedCheckedR pos s j k =
    TauCeti.signedCheckedR pos s k l * TauCeti.signedCheckedR pos s j k *
      TauCeti.signedCheckedR pos s k l
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.signedCheckedR_braid`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.html#TauCeti.signedCheckedR_braid).

## Sources

- [Tau Ceti documentation: `TauCeti.signedCheckedR_braid`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.html#TauCeti.signedCheckedR_braid)
- [Source of `TauCeti.signedCheckedR_braid` in TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/TypeAHeckeAlgebra/SignedCheckedR.lean#L179)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
