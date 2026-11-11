---
declaration: theorem
origin: cited
lean: TauCeti.PathAlgebra.gradedExtEuler_gradedVertexSimple
statement: formalized
proof: formalized
---

# The graded first-arrow Euler formula

Pairing a vertex simple against a finite-dimensional
graded module subtracts the shifted outgoing-arrow coordinates from its own vertex coordinate.

```lean
TauCeti.PathAlgebra.gradedExtEuler_gradedVertexSimple.{u, v, w, t} (k : Type w) (Q : Type u)
  [Field k] [Quiver Q] [Fintype Q] [(a b : Q) → Fintype (a ⟶ b)]
  [CategoryTheory.HasExt (TauCeti.GradedModuleCat (TauCeti.PathAlgebra.integerGrade k Q))] (i : Q)
  (Y : TauCeti.GradedModuleCat (TauCeti.PathAlgebra.integerGrade k Q)) [Module.Finite k Y.carrier]
  (h :
    TauCeti.IsGradedEulerAdmissible k
      (TauCeti.GradedModuleCat.shift (TauCeti.PathAlgebra.integerGrade k Q))
      (TauCeti.PathAlgebra.gradedVertexSimple k Q i) Y) :
  TauCeti.gradedExtEuler k (TauCeti.GradedModuleCat.shift (TauCeti.PathAlgebra.integerGrade k Q))
      h =
    TauCeti.GradedModuleCat.smulGradedDimension (TauCeti.PathAlgebra.vertexIdempotent k i) Y -
      LaurentPolynomial.T (-1) *
        ∑ a,
          TauCeti.GradedModuleCat.smulGradedDimension (TauCeti.PathAlgebra.vertexIdempotent k a.fst)
            Y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PathAlgebra.gradedExtEuler_gradedVertexSimple`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Value.html#TauCeti.PathAlgebra.gradedExtEuler_gradedVertexSimple).

## Sources

- [Tau Ceti documentation: `TauCeti.PathAlgebra.gradedExtEuler_gradedVertexSimple`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Value.html#TauCeti.PathAlgebra.gradedExtEuler_gradedVertexSimple)
- [Source of `TauCeti.PathAlgebra.gradedExtEuler_gradedVertexSimple` in TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Value.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/PathAlgebra/GradedExtEuler/Value.lean#L101)
