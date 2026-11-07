---
declaration: theorem
origin: cited
lean: TauCeti.gradedCartanMatrix_dualNumber
statement: formalized
proof: formalized
---

# TauCeti.gradedCartanMatrix\_dualNumber

**The graded Cartan matrix of the dual numbers is `1 + q²`**, with `ε` in degree two, in the
bases `[A]` and `[S]`: the regular module has the graded composition factors `S` and `S{2}`. At
`q = 1` this is the ungraded Cartan matrix `2` of `TauCeti.cartanMatrix_dualNumber`.

```lean
TauCeti.gradedCartanMatrix_dualNumber.{u} (k : Type u) [Field k] :
  TauCeti.gradedCartanMatrix (TauCeti.dualNumberIntegerGrade k)
      (TauCeti.dualNumberGradedProjectiveBasis k) (TauCeti.dualNumberGradedResidueBasis k) =
    Matrix.of fun x x_1 => 1 + LaurentPolynomial.T 2
```

## Depends on

- [TauCeti.gradedCartanMatrix](tauceti-gradedcartanmatrix.md)
- [TauCeti.gradedIdempotentProjectiveBasis](tauceti-gradedidempotentprojectivebasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanMatrix_dualNumber`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GradedDualNumbers.html#TauCeti.gradedCartanMatrix_dualNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanMatrix_dualNumber`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/GrothendieckGroup/GradedDualNumbers.html#TauCeti.gradedCartanMatrix_dualNumber)
- [Source of `TauCeti.gradedCartanMatrix_dualNumber` in TauCeti/RepresentationTheory/GrothendieckGroup/GradedDualNumbers.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/GrothendieckGroup/GradedDualNumbers.lean#L163)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
