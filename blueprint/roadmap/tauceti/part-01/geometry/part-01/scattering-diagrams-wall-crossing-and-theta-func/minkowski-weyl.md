---
declaration: theorem
origin: cited
lean: PointedCone.fg_iff_dualFG
statement: formalized
proof: formalized
---

# Minkowski–Weyl

a pointed cone is finitely generated exactly when it is
cut out by finitely many linear halfspaces, including when it has lineality.

```lean
PointedCone.fg_iff_dualFG.{u_1, u_2} {K : Type u_1} {V : Type u_2} [Field K] [LinearOrder K]
  [IsStrictOrderedRing K] [AddCommGroup V] [_root_.Module K V] [Module.Finite K V]
  {C : PointedCone K V} : Submodule.FG C ↔ PointedCone.DualFG LinearMap.id C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's key lemma](../../part-02/convex/tuckers-key-lemma.md)

## Lean

Formalized in Tau Ceti as [`PointedCone.fg_iff_dualFG`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/MinkowskiWeyl.html#PointedCone.fg_iff_dualFG).

## Sources

- [Tau Ceti documentation: `PointedCone.fg_iff_dualFG`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/MinkowskiWeyl.html#PointedCone.fg_iff_dualFG)
- [Source of `PointedCone.fg_iff_dualFG` in TauCeti/Geometry/Convex/Cone/MinkowskiWeyl.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Convex/Cone/MinkowskiWeyl.lean#L51)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
