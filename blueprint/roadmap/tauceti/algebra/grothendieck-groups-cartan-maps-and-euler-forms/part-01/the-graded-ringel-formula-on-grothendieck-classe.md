---
declaration: theorem
origin: cited
lean: TauCeti.PathAlgebra.gradedExtEulerForm_eq_sum, TauCeti.PathAlgebra.gradedExtEuler_eq_sum_smulGradedDimension
statement: formalized
proof: formalized
---

# The graded Ringel formula on Grothendieck classes

The vertex coordinates are the
idempotent graded dimensions, and the source coordinates are conjugated by `q ↦ q⁻¹`.

```lean
TauCeti.PathAlgebra.gradedExtEulerForm_eq_sum.{u, v, w} (k : Type w) (Q : Type u) [Field k]
  [Quiver Q] [Finite Q] [Module.Finite k (TauCeti.pathAlgebra k Q)]
  [CategoryTheory.HasExt (TauCeti.GradedModuleCat (TauCeti.PathAlgebra.integerGrade k Q))]
  [Fintype Q]
  (x y :
    TauCeti.LaurentK0
      (TauCeti.gradedFiniteModulesExactStructure (TauCeti.PathAlgebra.integerGrade k Q))) :
  ((TauCeti.PathAlgebra.gradedExtEulerForm k Q) x) y =
    ∑ i,
        LaurentPolynomial.invert
            (((TauCeti.PathAlgebra.gradedVertexSimpleClassBasis k Q).repr x) i) *
          ((TauCeti.PathAlgebra.gradedVertexSimpleClassBasis k Q).repr y) i -
      LaurentPolynomial.T (-1) *
        ∑ i,
          ∑ j,
            ↑(Nat.card (i ⟶ j)) *
                LaurentPolynomial.invert
                  (((TauCeti.PathAlgebra.gradedVertexSimpleClassBasis k Q).repr x) i) *
              ((TauCeti.PathAlgebra.gradedVertexSimpleClassBasis k Q).repr y) j
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The graded first-arrow Euler formula](the-graded-first-arrow-euler-formula.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PathAlgebra.gradedExtEulerForm_eq_sum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Pairing.html#TauCeti.PathAlgebra.gradedExtEulerForm_eq_sum).

## Other forms

**The graded Ringel formula for finite-dimensional graded modules.** Formalized in Tau Ceti as [`TauCeti.PathAlgebra.gradedExtEuler_eq_sum_smulGradedDimension`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Pairing.html#TauCeti.PathAlgebra.gradedExtEuler_eq_sum_smulGradedDimension).

```lean
TauCeti.PathAlgebra.gradedExtEuler_eq_sum_smulGradedDimension.{u, v, w} (k : Type w) (Q : Type u)
  [Field k] [Quiver Q] [Finite Q] [Module.Finite k (TauCeti.pathAlgebra k Q)]
  [CategoryTheory.HasExt (TauCeti.GradedModuleCat (TauCeti.PathAlgebra.integerGrade k Q))]
  [Fintype Q] (X Y : TauCeti.GradedModuleCat (TauCeti.PathAlgebra.integerGrade k Q))
  [Module.Finite k X.carrier] [Module.Finite k Y.carrier]
  (h :
    TauCeti.IsGradedEulerAdmissible k
      (TauCeti.GradedModuleCat.shift (TauCeti.PathAlgebra.integerGrade k Q)) X Y) :
  TauCeti.gradedExtEuler k (TauCeti.GradedModuleCat.shift (TauCeti.PathAlgebra.integerGrade k Q))
      h =
    ∑ i,
        LaurentPolynomial.invert
            (TauCeti.GradedModuleCat.smulGradedDimension (TauCeti.PathAlgebra.vertexIdempotent k i)
              X) *
          TauCeti.GradedModuleCat.smulGradedDimension (TauCeti.PathAlgebra.vertexIdempotent k i) Y -
      LaurentPolynomial.T (-1) *
        ∑ i,
          ∑ j,
            ↑(Nat.card (i ⟶ j)) *
                LaurentPolynomial.invert
                  (TauCeti.GradedModuleCat.smulGradedDimension
                    (TauCeti.PathAlgebra.vertexIdempotent k i) X) *
              TauCeti.GradedModuleCat.smulGradedDimension (TauCeti.PathAlgebra.vertexIdempotent k j)
                Y
```

## Sources

- [Tau Ceti documentation: `TauCeti.PathAlgebra.gradedExtEulerForm_eq_sum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Pairing.html#TauCeti.PathAlgebra.gradedExtEulerForm_eq_sum)
- [Source of `TauCeti.PathAlgebra.gradedExtEulerForm_eq_sum` in TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Pairing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Pairing.lean#L115)
