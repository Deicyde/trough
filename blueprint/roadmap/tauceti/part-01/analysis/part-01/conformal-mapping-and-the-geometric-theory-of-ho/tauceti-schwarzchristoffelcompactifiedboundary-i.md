---
declaration: theorem
origin: cited
lean: TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections
statement: formalized
proof: formalized
---

# TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections

A side-intersection criterion for simplicity of the compactified
Schwarz--Christoffel boundary. The finite prevertices are strictly ordered, their exponents
are integrable, and the total exponent is `-2`. Bounded sides may make reentrant turns.
The three intersection hypotheses say that nonadjacent bounded sides are disjoint,
adjacent ones meet only at their common vertex, and the bounded arc meets either closing
side only at its finite endpoint.

```lean
TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections {n : ℕ}
  (a e : Fin (n + 2) → ℝ) (z₀ : UpperHalfPlane) (ha : StrictMono a)
  (hfinite : ∀ (k : Fin (n + 2)), -1 < ∑ l with a l = a k, e l) (hsum : ∑ k, e k = -2)
  (hinter :
    ∀ (i j : Fin (n + 1)),
      i < j →
        ∀ z ∈ Polygon.edgeSet ℝ (TauCeti.schwarzChristoffelPolygon a e z₀) i.castSucc.castSucc,
          z ∈ Polygon.edgeSet ℝ (TauCeti.schwarzChristoffelPolygon a e z₀) j.castSucc.castSucc →
            ↑j = ↑i + 1 ∧ z = TauCeti.schwarzChristoffelVertex a e z₀ i.succ)
  (hleft :
    ∀ (i : Fin (n + 1)),
      ∀ z ∈ Polygon.edgeSet ℝ (TauCeti.schwarzChristoffelPolygon a e z₀) i.castSucc.castSucc,
        z ∈ Polygon.edgeSet ℝ (TauCeti.schwarzChristoffelPolygon a e z₀) (Fin.last (n + 2)) →
          z = TauCeti.schwarzChristoffelVertex a e z₀ 0)
  (hright :
    ∀ (i : Fin (n + 1)),
      ∀ z ∈ Polygon.edgeSet ℝ (TauCeti.schwarzChristoffelPolygon a e z₀) i.castSucc.castSucc,
        z ∈
            Polygon.edgeSet ℝ (TauCeti.schwarzChristoffelPolygon a e z₀)
              (Fin.last (n + 1)).castSucc →
          z = TauCeti.schwarzChristoffelVertex a e z₀ (Fin.last (n + 1))) :
  Function.Injective (TauCeti.schwarzChristoffelCompactifiedBoundary a e z₀)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Polygon/EdgeIntersection/Criterion.html#TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections).

## Sources

- [Tau Ceti documentation: `TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Polygon/EdgeIntersection/Criterion.html#TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections)
- [Source of `TauCeti.schwarzChristoffelCompactifiedBoundary_injective_of_edge_intersections` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Polygon/EdgeIntersection/Criterion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Polygon/EdgeIntersection/Criterion.lean#L156)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ConformalMapping/STATUS.md)
