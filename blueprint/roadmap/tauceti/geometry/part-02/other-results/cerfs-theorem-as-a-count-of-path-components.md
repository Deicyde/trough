---
declaration: theorem
origin: cited
lean: TauCeti.cerfTheorem_iff_natCard_zerothHomotopy_eq_two
statement: formalized
proof: formalized
---

# Cerf's theorem as a count of path components

Cerf's theorem holds exactly when the
diffeomorphism group of `S³` has two path components.

```lean
TauCeti.cerfTheorem_iff_natCard_zerothHomotopy_eq_two :
  TauCeti.CerfTheorem ↔
    Nat.card
        (ZerothHomotopy
          (TauCeti.Diff (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 3))) ↑(Metric.sphere 0 1)
            ↑⊤)) =
      2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cerfTheorem_iff_natCard_zerothHomotopy_eq_two`](https://taucetiproject.org/docs/TauCeti/Geometry/Diffeomorphism/Cerf.html#TauCeti.cerfTheorem_iff_natCard_zerothHomotopy_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.cerfTheorem_iff_natCard_zerothHomotopy_eq_two`](https://taucetiproject.org/docs/TauCeti/Geometry/Diffeomorphism/Cerf.html#TauCeti.cerfTheorem_iff_natCard_zerothHomotopy_eq_two)
- [Source of `TauCeti.cerfTheorem_iff_natCard_zerothHomotopy_eq_two` in TauCeti/Geometry/Diffeomorphism/Cerf.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Diffeomorphism/Cerf.lean#L99)
