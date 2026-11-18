---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.LatticeQuotient.isLagrangianTorusFibration_proj
statement: formalized
proof: formalized
---

# `T*B/Λ → B` is a regular Lagrangian torus fibration for the descended symplectic form

a
proper submersion with connected Lagrangian fibres. It is the model torus bundle of the period
lattice spanned by a closed coframe.

```lean
TauCeti.CotangentBundle.LatticeQuotient.isLagrangianTorusFibration_proj.{u_1, u_2, u_3, u_4}
  {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {B : Type u_3} [TopologicalSpace B] [ChartedSpace H B]
  [IsManifold I (↑⊤) B] {ι : Type u_4} [Fintype ι] {α : ι → TauCeti.SmoothForm I B ℝ 1}
  (hα :
    IsLocalFrameOn I (E →L[ℝ] ℝ) (↑⊤) (fun i x => (TauCeti.SmoothForm.degreeOneEquiv (α i)) x)
      Set.univ)
  [FiniteDimensional ℝ E] [T2Space B] (hclosed : ∀ (i : ι), (α i).IsClosed) :
  TauCeti.SmoothTwoForm.IsNondegenerate.IsLagrangianTorusFibration I ⋯
    (TauCeti.CotangentBundle.LatticeQuotient.proj hα)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.CotangentBundle.isSymplectic_symplecticForm](tauceti-cotangentbundle-issymplectic-symplecticf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.LatticeQuotient.isLagrangianTorusFibration_proj`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/LatticeQuotient.html#TauCeti.CotangentBundle.LatticeQuotient.isLagrangianTorusFibration_proj).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.LatticeQuotient.isLagrangianTorusFibration_proj`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/LatticeQuotient.html#TauCeti.CotangentBundle.LatticeQuotient.isLagrangianTorusFibration_proj)
- [Source of `TauCeti.CotangentBundle.LatticeQuotient.isLagrangianTorusFibration_proj` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/LatticeQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Cotangent/Bundle/LatticeQuotient.lean#L583)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
