---
declaration: theorem
origin: cited
lean: PointedCone.IsFaceOf.isExposed_of_fg
statement: formalized
proof: formalized
---

# PointedCone.IsFaceOf.isExposed_of_fg

Every face of a finitely generated cone in a real normed space is exposed
in Mathlib's continuous-functional sense. Finite generation provides continuity
on the span of the generators, and Hahn–Banach extends the exposing functional.

```lean
PointedCone.IsFaceOf.isExposed_of_fg.{u_1} {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V]
  {C F : PointedCone ℝ V} (hF : F.IsFaceOf C) (hC : Submodule.FG C) : IsExposed ℝ ↑C ↑F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`PointedCone.IsFaceOf.isExposed_of_fg`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Face/Exposed.html#PointedCone.IsFaceOf.isExposed_of_fg).

## Sources

- [Tau Ceti documentation: `PointedCone.IsFaceOf.isExposed_of_fg`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/Face/Exposed.html#PointedCone.IsFaceOf.isExposed_of_fg)
- [Source of `PointedCone.IsFaceOf.isExposed_of_fg` in TauCeti/Geometry/Convex/Cone/Face/Exposed.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Convex/Cone/Face/Exposed.lean#L280)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
