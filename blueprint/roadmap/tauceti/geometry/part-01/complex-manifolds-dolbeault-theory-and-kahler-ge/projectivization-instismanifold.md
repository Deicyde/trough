---
declaration: theorem
origin: cited
lean: Projectivization.instIsManifold
statement: formalized
proof: formalized
---

# Projectivization.instIsManifold

Projective space over a nontrivially normed field, with its standard affine charts, is a
`C^r` manifold for every `r`; for `r = ω` it is an analytic manifold. Over `ℂ` this is the
standard complex manifold structure on `ℂℙⁿ`.

```lean
Projectivization.instIsManifold.{u_1} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {n : ℕ}
  (r : WithTop ℕ∞) :
  IsManifold (modelWithCornersSelf 𝕜 (Fin n → 𝕜)) r (Projectivization 𝕜 (Fin (n + 1) → 𝕜))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Projectivization.instIsManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/Projectivization.html#Projectivization.instIsManifold).

## Sources

- [Tau Ceti documentation: `Projectivization.instIsManifold`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/Projectivization.html#Projectivization.instIsManifold)
- [Source of `Projectivization.instIsManifold` in TauCeti/Geometry/Manifold/Instances/Projectivization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Instances/Projectivization.lean#L87)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory, and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
