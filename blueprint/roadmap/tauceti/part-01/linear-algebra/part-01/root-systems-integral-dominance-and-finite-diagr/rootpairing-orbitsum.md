---
declaration: def
origin: cited
lean: RootPairing.orbitSum
statement: formalized
---

# RootPairing.orbitSum

The **orbit sum** of the root `αᵢ` under the automorphism `σ`: the sum of the roots indexed
by the distinct members of the root orbit of `i`, each counted once.

```lean
RootPairing.orbitSum.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2} {M : Type u_3}
  {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] (P : RootPairing ι R M N) [Finite ι] (σ : P.Aut) (i : ι) : M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`RootPairing.orbitSum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.orbitSum).

## Sources

- [Tau Ceti documentation: `RootPairing.orbitSum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.orbitSum)
- [Source of `RootPairing.orbitSum` in TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean#L153)
- [Tau Ceti roadmap status: Root systems, integral dominance and finite diagram folding, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RootSystemsPartII/STATUS.md)
