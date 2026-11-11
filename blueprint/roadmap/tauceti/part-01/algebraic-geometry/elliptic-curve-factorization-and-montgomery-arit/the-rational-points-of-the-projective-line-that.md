---
declaration: theorem
origin: cited
lean: TauCeti.Montgomery.toProj_mem_range_projectiveX_iff
statement: formalized
proof: formalized
---

# The rational points of the projective line that lift to the curve

For an elliptic
model, the point `(r : 1)` is the projective `x`-coordinate of a native point exactly when
`(r³ + A r² + r) / B` is a square in `K`; the point `(1 : 0)` is always that of infinity.

```lean
TauCeti.Montgomery.toProj_mem_range_projectiveX_iff.{u_1} {K : Type u_1} [Field K] {A B : K}
  [(TauCeti.Montgomery.model A B).IsElliptic] (hB : B ≠ 0) (r : K) :
  { x := r, z := 1 }.toProj ⋯ ∈ Set.range (TauCeti.Montgomery.projectiveX A hB) ↔
    IsSquare ((r ^ 3 + A * r ^ 2 + r) / B)
```

## Depends on

- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)
- [TauCeti.Montgomery.projectiveX](tauceti-montgomery-projectivex.md)

## Proof depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.toProj_mem_range_projectiveX_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.toProj_mem_range_projectiveX_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.toProj_mem_range_projectiveX_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.toProj_mem_range_projectiveX_iff)
- [Source of `TauCeti.Montgomery.toProj_mem_range_projectiveX_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean#L220)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)
