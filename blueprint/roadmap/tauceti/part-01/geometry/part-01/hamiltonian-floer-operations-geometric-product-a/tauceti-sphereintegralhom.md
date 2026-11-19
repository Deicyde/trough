---
declaration: def
origin: cited
lean: TauCeti.sphereIntegralHom
statement: formalized
---

# TauCeti.sphereIntegralHom

The integral of a closed `C¹` two-form over the second homotopy group, as an additive
homomorphism. For the symplectic form of a symplectic manifold it is the symplectic area of
spheres.

```lean
TauCeti.sphereIntegralHom.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] (x : M) [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M]
  [CompactSpace M] [T2Space M] {φ : TauCeti.RoughForm I M F 2} (hφ : TauCeti.IsSmoothForm I 1 φ)
  (hdφ : TauCeti.mextDeriv φ = 0) : Additive (HomotopyGroup.Pi 2 M x) →+ F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for a converging family](../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)
- [Smooth tubular neighbourhood theorem](../../part-02/manifold/part-04/smooth-tubular-neighbourhood-theorem.md)
- [Stokes' formula for a homotopy of maps of a rectangle](../../part-02/manifold/part-04/stokes-formula-for-a-homotopy-of-maps-of-a-recta.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sphereIntegralHom`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Sphere.html#TauCeti.sphereIntegralHom).

## Sources

- [Tau Ceti documentation: `TauCeti.sphereIntegralHom`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Sphere.html#TauCeti.sphereIntegralHom)
- [Source of `TauCeti.sphereIntegralHom` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Sphere.lean#L773)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
