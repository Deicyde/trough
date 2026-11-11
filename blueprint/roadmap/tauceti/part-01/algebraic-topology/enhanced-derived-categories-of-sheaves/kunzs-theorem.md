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

## Proof depends on

- [A regular local ring is Cohen–Macaulay](../../ring-theory/part-01/finite-etale-covers-of-punctured-spectra-and-loc/a-regular-local-ring-is-cohen-macaulay.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRegularRing.flat_frobenius`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Frobenius.html#TauCeti.IsRegularRing.flat_frobenius).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRegularRing.flat_frobenius`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Frobenius.html#TauCeti.IsRegularRing.flat_frobenius)
- [Source of `TauCeti.IsRegularRing.flat_frobenius` in TauCeti/RingTheory/RegularLocalRing/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/RegularLocalRing/Frobenius.lean#L82)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
