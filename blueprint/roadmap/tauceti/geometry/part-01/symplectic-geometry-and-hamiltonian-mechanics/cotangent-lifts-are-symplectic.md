---
declaration: theorem
origin: cited
lean: Diffeomorph.mpullback_cotangent_symplecticForm
statement: formalized
proof: formalized
---

# Cotangent lifts are symplectic

The cotangent lift of a smooth diffeomorphism pulls the
canonical symplectic form of `T*N` back to the canonical symplectic form of `T*M`.

```lean
Diffeomorph.mpullback_cotangent_symplecticForm.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  {H : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] {F : Type u_4}
  {H' : Type u_5} [NormedAddCommGroup F] [NormedSpace ℝ F] [TopologicalSpace H']
  {J : ModelWithCorners ℝ F H'} {N : Type u_6} [TopologicalSpace N] [ChartedSpace H' N]
  [IsManifold I (↑⊤) M] [IsManifold J (↑⊤) N] (h : Diffeomorph I J M N ↑⊤) :
  (TauCeti.SmoothForm.mpullback ⇑h.cotangent ⋯) (TauCeti.CotangentBundle.symplecticForm J N) =
    TauCeti.CotangentBundle.symplecticForm I M
```

## Depends on

- [TauCeti.CotangentBundle](tauceti-cotangentbundle.md)

## Lean

Formalized in Tau Ceti as [`Diffeomorph.mpullback_cotangent_symplecticForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Lift.html#Diffeomorph.mpullback_cotangent_symplecticForm).

## Sources

- [Tau Ceti documentation: `Diffeomorph.mpullback_cotangent_symplecticForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Lift.html#Diffeomorph.mpullback_cotangent_symplecticForm)
- [Source of `Diffeomorph.mpullback_cotangent_symplecticForm` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Lift.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Lift.lean#L85)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
