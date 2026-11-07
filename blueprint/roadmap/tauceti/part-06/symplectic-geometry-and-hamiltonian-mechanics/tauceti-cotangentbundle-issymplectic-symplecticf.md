---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.isSymplectic_symplecticForm
statement: formalized
proof: formalized
---

# TauCeti.CotangentBundle.isSymplectic\_symplecticForm

The canonical symplectic form of the cotangent bundle is closed and nondegenerate.

```lean
TauCeti.CotangentBundle.isSymplectic_symplecticForm.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] :
  (TauCeti.CotangentBundle.symplecticForm I M).IsSymplectic
```

## Depends on

- [TauCeti.CotangentBundle](tauceti-cotangentbundle.md)

## Proof depends on

- [Chart formula for the canonical symplectic form](chart-formula-for-the-canonical-symplectic-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.isSymplectic_symplecticForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.isSymplectic_symplecticForm).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.isSymplectic_symplecticForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.isSymplectic_symplecticForm)
- [Source of `TauCeti.CotangentBundle.isSymplectic_symplecticForm` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean#L333)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
