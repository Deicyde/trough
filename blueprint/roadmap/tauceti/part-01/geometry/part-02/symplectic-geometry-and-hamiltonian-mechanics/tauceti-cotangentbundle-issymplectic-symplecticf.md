---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.isSymplectic_symplecticForm
statement: formalized
proof: formalized
---

# TauCeti.CotangentBundle.isSymplectic_symplecticForm

The canonical symplectic form of the cotangent bundle is closed and nondegenerate.

```lean
TauCeti.CotangentBundle.isSymplectic_symplecticForm.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] :
  (TauCeti.CotangentBundle.symplecticForm I M).IsSymplectic
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.isSymplectic_symplecticForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.isSymplectic_symplecticForm).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.isSymplectic_symplecticForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.isSymplectic_symplecticForm)
- [Source of `TauCeti.CotangentBundle.isSymplectic_symplecticForm` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean#L346)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
