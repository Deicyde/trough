---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.mpullback_liouvilleForm
statement: formalized
proof: formalized
---

# The Liouville form is tautological

Pulling it back along the smooth section of the
cotangent bundle defined by a smooth one-form `α` gives back `α`.

```lean
TauCeti.CotangentBundle.mpullback_liouvilleForm.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]
  (α : TauCeti.SmoothForm I M ℝ 1) :
  (TauCeti.SmoothForm.mpullback (fun x => ⟨x, (TauCeti.SmoothForm.degreeOneEquiv α) x⟩) ⋯)
      (TauCeti.CotangentBundle.liouvilleForm I M) =
    α
```

## Depends on

- [TauCeti.CotangentBundle](tauceti-cotangentbundle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.mpullback_liouvilleForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.mpullback_liouvilleForm).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.mpullback_liouvilleForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.mpullback_liouvilleForm)
- [Source of `TauCeti.CotangentBundle.mpullback_liouvilleForm` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean#L188)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
