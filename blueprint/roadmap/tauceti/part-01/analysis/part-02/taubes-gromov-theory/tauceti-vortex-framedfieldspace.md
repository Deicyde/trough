---
declaration: def
origin: cited
lean: TauCeti.Vortex.framedFieldSpace
statement: formalized
---

# TauCeti.Vortex.framedFieldSpace

The affine space `A_m^s = referenceField f m + sobolevFields s` of framed degree-`m` plane
vortex fields, whose direction is `L² ∩ H^s` (all of `H^s` when `s ≥ 0`). It does not depend on
the cutoff `f` (`framedFieldSpace_eq`).

```lean
TauCeti.Vortex.framedFieldSpace (f : ContDiffBump 0) (m : ℕ) (s : ℝ) :
  AffineSubspace ℝ (ℂ → EuclideanSpace ℝ (Fin 4))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.framedFieldSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/FieldSpace.html#TauCeti.Vortex.framedFieldSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.framedFieldSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/FieldSpace.html#TauCeti.Vortex.framedFieldSpace)
- [Source of `TauCeti.Vortex.framedFieldSpace` in TauCeti/Analysis/PDE/Vortex/FieldSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/FieldSpace.lean#L320)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
