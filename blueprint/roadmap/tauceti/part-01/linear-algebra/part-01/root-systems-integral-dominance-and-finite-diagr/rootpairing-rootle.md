---
declaration: def
origin: cited
lean: RootPairing.rootLE
statement: formalized
---

# RootPairing.rootLE

Integral root dominance: the difference is a natural sum of simple roots.
No saturation of the positive root monoid is taken.

```lean
RootPairing.rootLE.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2} {M : Type u_3} {N : Type u_4}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N] [_root_.Module R N]
  (P : RootPairing ι R M N) (b : P.Base) (x y : M) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.rootLE`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Dominance.html#RootPairing.rootLE).

## Sources

- [Tau Ceti documentation: `RootPairing.rootLE`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Dominance.html#RootPairing.rootLE)
- [Source of `RootPairing.rootLE` in TauCeti/LinearAlgebra/RootSystem/Dominance.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/Dominance.lean#L41)
- [Tau Ceti roadmap status: Root systems, integral dominance and finite diagram folding, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RootSystemsPartII/STATUS.md)
