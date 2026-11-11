---
declaration: def
origin: cited
lean: PowerSeries.colemanDEntire
statement: formalized
---

# PowerSeries.colemanDEntire

The coefficientwise limit of the finite Coleman transforms of the truncations of `B` and
`F`. Its convergence and entire-series interpretation hold when `B` and `F` are entire,
`coeff 0 B = 0`, and `coeff 0 F = 1`.

```lean
PowerSeries.colemanDEntire.{u_1} {R : Type u_1} [NormedCommRing R] (B F : PowerSeries R) :
  PowerSeries R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.colemanDEntire`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Entire.html#PowerSeries.colemanDEntire).

## Sources

- [Tau Ceti documentation: `PowerSeries.colemanDEntire`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/Coleman/Entire.html#PowerSeries.colemanDEntire)
- [Source of `PowerSeries.colemanDEntire` in TauCeti/Analysis/Polynomial/Coleman/Entire.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Polynomial/Coleman/Entire.lean#L56)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CompactOperators/STATUS.md)
