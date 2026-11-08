---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.mvfderiv_kineticEnergy_vectorBundleEulerField
statement: formalized
proof: formalized
---

# Euler's identity for the kinetic energy

The kinetic energy is homogeneous of degree two
in the fibres, so the Euler vector field `Z = p ∂_p` satisfies `dK(Z) = 2K = ‖p‖²`.

```lean
TauCeti.CotangentBundle.mvfderiv_kineticEnergy_vectorBundleEulerField.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [FiniteDimensional ℝ E] [IsManifold I 2 M]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] (z : TauCeti.CotangentBundle I M) :
  (d% (TauCeti.CotangentBundle.kineticEnergy I M) z) (TauCeti.vectorBundleEulerField I z) =
    ‖z.snd‖ ^ 2
```

## Depends on

- [TauCeti.CotangentBundle](../symplectic-geometry-and-hamiltonian-mechanics/tauceti-cotangentbundle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.mvfderiv_kineticEnergy_vectorBundleEulerField`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Cogeodesic.html#TauCeti.CotangentBundle.mvfderiv_kineticEnergy_vectorBundleEulerField).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.mvfderiv_kineticEnergy_vectorBundleEulerField`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Cogeodesic.html#TauCeti.CotangentBundle.mvfderiv_kineticEnergy_vectorBundleEulerField)
- [Source of `TauCeti.CotangentBundle.mvfderiv_kineticEnergy_vectorBundleEulerField` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Cogeodesic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Cogeodesic.lean#L122)
