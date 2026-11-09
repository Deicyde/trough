---
declaration: theorem
origin: cited
lean: TauCeti.DualGraph.sum_arithmeticGenus_cutComponent_add_card
statement: formalized
proof: formalized
---

# Genus of a partial normalization

The sum of the arithmetic genera of its connected
pieces, plus the number of cut nodes plus one, equals the original genus plus the number of
pieces. This includes separating, nonseparating and simultaneous cuts, without subtraction.

```lean
TauCeti.DualGraph.sum_arithmeticGenus_cutComponent_add_card.{u, v} {ι : Type v}
  (G : TauCeti.DualGraph ι) (S : Finset G.Edge) :
  ∑ x, (G.cutComponent S x).arithmeticGenus + S.card + 1 =
    G.arithmeticGenus + Fintype.card (G.smoothing Sᶜ).Vertex
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Smoothing preserves the arithmetic genus](smoothing-preserves-the-arithmetic-genus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DualGraph.sum_arithmeticGenus_cutComponent_add_card`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Cutting.html#TauCeti.DualGraph.sum_arithmeticGenus_cutComponent_add_card).

## Sources

- [Tau Ceti documentation: `TauCeti.DualGraph.sum_arithmeticGenus_cutComponent_add_card`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Cutting.html#TauCeti.DualGraph.sum_arithmeticGenus_cutComponent_add_card)
- [Source of `TauCeti.DualGraph.sum_arithmeticGenus_cutComponent_add_card` in TauCeti/AlgebraicGeometry/Curves/DualGraph/Cutting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/DualGraph/Cutting.lean#L132)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
