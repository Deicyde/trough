---
declaration: theorem
origin: cited
lean: TauCeti.IsRegularRing.flat_frobenius
statement: formalized
proof: formalized
---

# Kunz's theorem

The Frobenius endomorphism of a regular ring of exponential characteristic
`p` is flat. Stacks, Lemma 51.17.6 (0EC0), the implication from regularity to flatness.

```lean
TauCeti.IsRegularRing.flat_frobenius.{u_1} {R : Type u_1} [CommRing R] (p : ℕ) [ExpChar R p]
  [IsRegularRing R] : (frobenius R p).Flat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRegularRing.flat_frobenius`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Frobenius.html#TauCeti.IsRegularRing.flat_frobenius).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRegularRing.flat_frobenius`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Frobenius.html#TauCeti.IsRegularRing.flat_frobenius)
- [Source of `TauCeti.IsRegularRing.flat_frobenius` in TauCeti/RingTheory/RegularLocalRing/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/RegularLocalRing/Frobenius.lean#L82)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
