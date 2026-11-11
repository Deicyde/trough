---
declaration: abbrev
origin: cited
lean: TauCeti.niemeierD24
statement: formalized
---

# TauCeti.niemeierD24

The Niemeier lattice with root system `D₂₄`, glued from the table row
`RootfulNiemeierType.d24`.

```lean
TauCeti.niemeierD24 :
  TauCeti.IntegralLattice
    ((i : Fin TauCeti.RootfulNiemeierType.d24.components.length) →
      Fin (TauCeti.RootfulNiemeierType.d24.componentType i).rank → ℚ)
```

## Depends on

- [The lattice `N_r` of a row of the rootful rank-24 table](the-lattice-n-r-of-a-row-of-the-rootful-rank-24.md)
- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.RootfulNiemeierType](tauceti-rootfulniemeiertype.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.niemeierD24`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.html#TauCeti.niemeierD24).

## Sources

- [Tau Ceti documentation: `TauCeti.niemeierD24`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.html#TauCeti.niemeierD24)
- [Source of `TauCeti.niemeierD24` in TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Rank24/Niemeier.lean#L348)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
