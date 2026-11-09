---
declaration: def
origin: cited
lean: TauCeti.SpinPolarizationData.evenCliffordEquivEnd, TauCeti.SpinPolarizationData.cliffordEquivEndProd
statement: formalized
---

# The odd structure theorem in operator form

for a polarized quadratic space of odd
dimension over a field of characteristic not two, the Fock action is an isomorphism of
`F`-algebras from the even Clifford subalgebra onto the endomorphism algebra of the spinor module
`S = ⋀·W`.

This is the odd-dimensional companion of
`TauCeti.SpinPolarizationData.cliffordEquivEnd`, one grade down: there the *whole* algebra is
`Module.End F S`, here only its even half is, the whole algebra being two copies of it.

```lean
TauCeti.SpinPolarizationData.evenCliffordEquivEnd.{u, v} {F : Type u} [Field F] [NeZero 2]
  {V : Type v} [AddCommGroup V] [_root_.Module F V] [FiniteDimensional F V] {Q : QuadraticForm F V}
  (P : TauCeti.SpinPolarizationData Q) (hodd : Odd (Module.finrank F V)) :
  ↥(CliffordAlgebra.even Q) ≃ₐ[F] Module.End F (ExteriorAlgebra F ↥P.W)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.evenCliffordEquivEnd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/OddStructure.html#TauCeti.SpinPolarizationData.evenCliffordEquivEnd).

## Other forms

**The odd structure theorem, labelled by the two signs of the line coordinate.** Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.cliffordEquivEndProd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/LineSign.html#TauCeti.SpinPolarizationData.cliffordEquivEndProd).

```lean
TauCeti.SpinPolarizationData.cliffordEquivEndProd.{u, v} {F : Type u} [Field F] {V : Type v}
  [AddCommGroup V] [_root_.Module F V] [FiniteDimensional F V] {Q : QuadraticForm F V}
  (P : TauCeti.SpinPolarizationData Q) [NeZero 2] (hodd : Odd (Module.finrank F V)) :
  CliffordAlgebra Q ≃ₐ[F]
    Module.End F (ExteriorAlgebra F ↥P.W) × Module.End F (ExteriorAlgebra F ↥P.W)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.evenCliffordEquivEnd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/OddStructure.html#TauCeti.SpinPolarizationData.evenCliffordEquivEnd)
- [Source of `TauCeti.SpinPolarizationData.evenCliffordEquivEnd` in TauCeti/RepresentationTheory/Spin/OddStructure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Spin/OddStructure.lean#L286)
