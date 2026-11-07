---
declaration: theorem
origin: cited
lean: TauCeti.PathAlgebra.laurentSpecialize_gradedExtEulerForm_eq_extEulerPairing
statement: formalized
proof: formalized
---

# The graded quiver q-Euler form at `q = 1` is the ungraded Ext-Euler pairing

On
`G₀^gr(mod kQ)` specialized at `q = 1`, the q-Euler form is the Ext-Euler pairing on
`G₀(mod kQ)` of the classes with their grading forgotten.

```lean
TauCeti.PathAlgebra.laurentSpecialize_gradedExtEulerForm_eq_extEulerPairing.{u, v}
  (k : Type (max u v)) (Q : Type u) [Field k] [Quiver Q] [Finite Q]
  [FiniteDimensional k (TauCeti.pathAlgebra k Q)]
  [CategoryTheory.HasExt (TauCeti.GradedModuleCat (TauCeti.PathAlgebra.integerGrade k Q))]
  (x y :
    TauCeti.LaurentSpecialization 1
      (TauCeti.LaurentK0
        (TauCeti.gradedFiniteModulesExactStructure (TauCeti.PathAlgebra.integerGrade k Q)))) :
  (((TauCeti.PathAlgebra.gradedExtEulerForm k Q).laurentSpecialize ⋯) x) y =
    ((TauCeti.extEulerPairing ⋯ ⋯ ⋯)
        ((TauCeti.finiteModulesExactK0Equiv (TauCeti.pathAlgebra k Q))
          ((TauCeti.gradedFiniteModulesForgetK0 (TauCeti.PathAlgebra.integerGrade k Q)) x)))
      ((TauCeti.finiteModulesExactK0Equiv (TauCeti.pathAlgebra k Q))
        ((TauCeti.gradedFiniteModulesForgetK0 (TauCeti.PathAlgebra.integerGrade k Q)) y))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PathAlgebra.laurentSpecialize_gradedExtEulerForm_eq_extEulerPairing`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/ForgetGrading.html#TauCeti.PathAlgebra.laurentSpecialize_gradedExtEulerForm_eq_extEulerPairing).

## Sources

- [Tau Ceti documentation: `TauCeti.PathAlgebra.laurentSpecialize_gradedExtEulerForm_eq_extEulerPairing`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/ForgetGrading.html#TauCeti.PathAlgebra.laurentSpecialize_gradedExtEulerForm_eq_extEulerPairing)
- [Source of `TauCeti.PathAlgebra.laurentSpecialize_gradedExtEulerForm_eq_extEulerPairing` in TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/ForgetGrading.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/ForgetGrading.lean#L94)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
