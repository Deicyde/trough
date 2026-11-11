---
declaration: theorem
origin: cited
lean: FreeGroup.geodesicEdges_mul
statement: formalized
proof: formalized
---

# Haagerup's cocycle identity

The geodesic to `g * h` is the symmetric difference of the
geodesic to `g` and the translate by `g` of the geodesic to `h`.

```lean
FreeGroup.geodesicEdges_mul.{u_1} {α : Type u_1} [DecidableEq α] (g h : FreeGroup α) :
  (g * h).geodesicEdges =
    symmDiff g.geodesicEdges (Finset.image (Prod.map (fun x => g * x) id) h.geodesicEdges)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FreeGroup.geodesicEdges_mul`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/GeodesicEdges.html#FreeGroup.geodesicEdges_mul).

## Sources

- [Tau Ceti documentation: `FreeGroup.geodesicEdges_mul`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/GeodesicEdges.html#FreeGroup.geodesicEdges_mul)
- [Source of `FreeGroup.geodesicEdges_mul` in TauCeti/GroupTheory/FreeGroup/GeodesicEdges.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/FreeGroup/GeodesicEdges.lean#L183)
