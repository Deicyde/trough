---
declaration: def
origin: cited
lean: RootPairing.foldedIndices
statement: formalized
---

# RootPairing.foldedIndices

The set of all orbit sums of `σ`. Distinct orbits may have the same sum, so this set, rather
than the set of orbits, indexes the folded roots.

```lean
RootPairing.foldedIndices.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2} {M : Type u_3}
  {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] (P : RootPairing ι R M N) [Finite ι] (σ : P.Aut) : Set M
```

## Depends on

- [RootPairing.orbitSum](rootpairing-orbitsum.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.foldedIndices`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.foldedIndices).

## Sources

- [Tau Ceti documentation: `RootPairing.foldedIndices`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.foldedIndices)
- [Source of `RootPairing.foldedIndices` in TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean#L316)
- [Tau Ceti roadmap status: Root systems, integral dominance and finite diagram folding, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RootSystemsPartII/STATUS.md)
