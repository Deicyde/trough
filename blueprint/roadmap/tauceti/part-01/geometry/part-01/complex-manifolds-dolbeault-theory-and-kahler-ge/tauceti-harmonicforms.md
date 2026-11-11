---
declaration: def
origin: cited
lean: TauCeti.harmonicForms
statement: formalized
---

# TauCeti.harmonicForms

The harmonic `k`-forms on an oriented Riemannian manifold of dimension `m = k + l`: the
kernel of the Hodge Laplacian `Δ = d*d + dd*`.

```lean
TauCeti.harmonicForms.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] {m k l : ℕ}
  (o : TauCeti.Manifold.Orientation I M (Fin m)) (hkl : k + l = m) :
  Submodule ℝ (TauCeti.SmoothForm I M ℝ k)
```

## Depends on

- [TauCeti.SmoothForm.hodgeLaplacian](tauceti-smoothform-hodgelaplacian.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.harmonicForms`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Harmonic.html#TauCeti.harmonicForms).

## Sources

- [Tau Ceti documentation: `TauCeti.harmonicForms`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Harmonic.html#TauCeti.harmonicForms)
- [Source of `TauCeti.harmonicForms` in TauCeti/Geometry/Manifold/DeRham/Harmonic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DeRham/Harmonic.lean#L80)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
