---
declaration: theorem
origin: cited
lean: OnePoint.instContMDiffConstSMul
statement: formalized
proof: formalized
---

# Möbius transformations of the projective line are analytic

For `𝕜 = ℂ`, every
transformation `z ↦ (a * z + b) / (c * z + d)` of the Riemann sphere is holomorphic, and hence a
biholomorphism `Diffeomorph.constSmul 𝓘(ℂ) ω g` with inverse the transformation of `g⁻¹`.

```lean
OnePoint.instContMDiffConstSMul.{u_1} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] [DecidableEq 𝕜]
  [ProperSpace 𝕜] : ContMDiffConstSMul (modelWithCornersSelf 𝕜 𝕜) ⊤ (GL (Fin 2) 𝕜) (OnePoint 𝕜)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`OnePoint.instContMDiffConstSMul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/OnePoint/Moebius.html#OnePoint.instContMDiffConstSMul).

## Sources

- [Tau Ceti documentation: `OnePoint.instContMDiffConstSMul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Instances/OnePoint/Moebius.html#OnePoint.instContMDiffConstSMul)
- [Source of `OnePoint.instContMDiffConstSMul` in TauCeti/Geometry/Manifold/Instances/OnePoint/Moebius.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Instances/OnePoint/Moebius.lean#L162)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
