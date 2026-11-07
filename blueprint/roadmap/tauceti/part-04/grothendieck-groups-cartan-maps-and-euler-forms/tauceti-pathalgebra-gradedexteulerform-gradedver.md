---
declaration: theorem
origin: cited
lean: TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv
statement: formalized
proof: formalized
---

# TauCeti.PathAlgebra.gradedExtEulerForm\_gradedVertexSimpleClassBasis\_eq\_inv

**The q-Euler matrix of a path algebra is the inverse of its conjugate-transposed graded
Cartan matrix**: `χ_q(Sᵢ, Sⱼ)` is the `(i, j)` entry of `((C.map invert)ᵀ)⁻¹`, where `C` is the
graded Cartan matrix in the bases of graded vertex projectives and graded vertex simples.

```lean
TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv.{u, v, w} (k : Type w)
  (Q : Type u) [Field k] [Quiver Q] [Fintype Q] [DecidableEq Q]
  [Module.Finite k (TauCeti.pathAlgebra k Q)]
  [CategoryTheory.HasExt (TauCeti.GradedModuleCat (TauCeti.PathAlgebra.integerGrade k Q))]
  (i j : Q) :
  ((TauCeti.PathAlgebra.gradedExtEulerForm k Q)
        ((TauCeti.PathAlgebra.gradedVertexSimpleClassBasis k Q) i))
      ((TauCeti.PathAlgebra.gradedVertexSimpleClassBasis k Q) j) =
    ((TauCeti.gradedCartanMatrix (TauCeti.PathAlgebra.integerGrade k Q)
                (TauCeti.PathAlgebra.gradedVertexProjectiveClassBasis k Q)
                (TauCeti.PathAlgebra.gradedVertexSimpleClassBasis k Q)).map
            ⇑LaurentPolynomial.invert).transpose⁻¹
      i j
```

## Depends on

- [The graded Cartan matrix](the-graded-cartan-matrix.md)
- [The graded projectives `A eᵢ` form a basis of `K₀^gr(proj A)`](the-graded-projectives-a-ei-form-a-basis-of-k0-g.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.html#TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv).

## Sources

- [Tau Ceti documentation: `TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.html#TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv)
- [Source of `TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv` in TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.lean#L54)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
