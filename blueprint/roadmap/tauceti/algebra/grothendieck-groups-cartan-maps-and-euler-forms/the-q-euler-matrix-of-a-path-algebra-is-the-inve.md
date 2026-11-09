---
declaration: theorem
origin: cited
lean: TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv
statement: formalized
proof: formalized
---

# The q-Euler matrix of a path algebra is the inverse of its conjugate-transposed graded Cartan matrix

`χ_q(Sᵢ, Sⱼ)` is the `(i, j)` entry of `((C.map invert)ᵀ)⁻¹`, where `C` is the
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

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](the-graded-cartan-matrix-in-a-projective-basis-b.md)
- [The graded projectives `A eᵢ` form a basis of `K₀^gr(proj A)`](the-graded-projectives-a-ei-form-a-basis-of-k0-g.md)

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The graded first-arrow Euler formula](the-graded-first-arrow-euler-formula.md)
- [Jacobson's lemma](../../category-theory/preadditive/jacobsons-lemma.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [TauCeti.isLocalRing_end_of_indecomposable](../../category-theory/preadditive/tauceti-islocalring-end-of-indecomposable.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.html#TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv).

## Sources

- [Tau Ceti documentation: `TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.html#TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv)
- [Source of `TauCeti.PathAlgebra.gradedExtEulerForm_gradedVertexSimpleClassBasis_eq_inv` in TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/CartanMatrix.lean#L54)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
