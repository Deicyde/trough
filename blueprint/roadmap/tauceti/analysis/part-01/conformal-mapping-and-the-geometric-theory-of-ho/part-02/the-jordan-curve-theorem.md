---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.natCard_connectedComponents_compl_eq_two, TauCeti.IsJordanCurve.natCard_zerothHomotopy_compl_eq_two_onePoint
statement: formalized
proof: formalized
---

# The Jordan curve theorem

The complement of a Jordan curve in the plane has exactly two
connected components: by `TauCeti.IsJordanCurve.connectedComponentIn_eq_filledHull_sdiff_or_compl`
they are its inside `filledHull C \ C` and its unbounded outside `(filledHull C)ᶜ`.

```lean
TauCeti.IsJordanCurve.natCard_connectedComponents_compl_eq_two {C : Set ℂ}
  (hC : TauCeti.IsJordanCurve C) : Nat.card (ConnectedComponents ↑Cᶜ) = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jordan separation theorem](../part-01/the-jordan-separation-theorem.md)
- [The Jordan–Brouwer separation theorem](../part-01/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.natCard_connectedComponents_compl_eq_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Inside.html#TauCeti.IsJordanCurve.natCard_connectedComponents_compl_eq_two).

## Other forms

**The Jordan curve theorem on the Riemann sphere.** Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.natCard_zerothHomotopy_compl_eq_two_onePoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/RiemannSphere.html#TauCeti.IsJordanCurve.natCard_zerothHomotopy_compl_eq_two_onePoint).

```lean
TauCeti.IsJordanCurve.natCard_zerothHomotopy_compl_eq_two_onePoint {J : Set (OnePoint ℂ)}
  (hJ : TauCeti.IsJordanCurve J) : Nat.card (ZerothHomotopy ↑Jᶜ) = 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.natCard_connectedComponents_compl_eq_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Inside.html#TauCeti.IsJordanCurve.natCard_connectedComponents_compl_eq_two)
- [Source of `TauCeti.IsJordanCurve.natCard_connectedComponents_compl_eq_two` in TauCeti/Analysis/Complex/PlaneSeparation/Inside.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/PlaneSeparation/Inside.lean#L187)
