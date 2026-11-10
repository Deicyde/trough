---
declaration: theorem
origin: cited
lean: TauCeti.DualGraph.arithmeticGenus_smoothing
statement: formalized
proof: formalized
---

# Smoothing preserves the arithmetic genus

The first Betti number lost by smoothing the
nodes in `S` reappears in the genera of the smoothed components.

```lean
TauCeti.DualGraph.arithmeticGenus_smoothing.{u, v} {ι : Type v} (G : TauCeti.DualGraph ι)
  (S : Finset G.Edge) : (G.smoothing S).arithmeticGenus = G.arithmeticGenus
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DualGraph.arithmeticGenus_smoothing`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Smoothing.html#TauCeti.DualGraph.arithmeticGenus_smoothing).

## Sources

- [Tau Ceti documentation: `TauCeti.DualGraph.arithmeticGenus_smoothing`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Smoothing.html#TauCeti.DualGraph.arithmeticGenus_smoothing)
- [Source of `TauCeti.DualGraph.arithmeticGenus_smoothing` in TauCeti/AlgebraicGeometry/Curves/DualGraph/Smoothing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/DualGraph/Smoothing.lean#L266)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
