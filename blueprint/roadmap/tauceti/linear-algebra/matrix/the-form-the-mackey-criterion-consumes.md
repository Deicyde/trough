---
declaration: theorem
origin: cited
lean: TauCeti.GL2Borel.doubleCosetMk_eq_weyl_of_ne_one
statement: formalized
proof: formalized
---

# The form the Mackey criterion consumes

a double coset of the Borel subgroup other than the
identity one is the Weyl one.

```lean
TauCeti.GL2Borel.doubleCosetMk_eq_weyl_of_ne_one.{u} {F : Type u} [Field F]
  {D : DoubleCoset.Quotient ↑(TauCeti.GL2Borel F) ↑(TauCeti.GL2Borel F)}
  (hD : D ≠ DoubleCoset.mk (TauCeti.GL2Borel F) (TauCeti.GL2Borel F) 1) :
  D = DoubleCoset.mk (TauCeti.GL2Borel F) (TauCeti.GL2Borel F) (TauCeti.GL2WeylElement F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GL2Borel.doubleCosetMk_eq_weyl_of_ne_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.html#TauCeti.GL2Borel.doubleCosetMk_eq_weyl_of_ne_one).

## Sources

- [Tau Ceti documentation: `TauCeti.GL2Borel.doubleCosetMk_eq_weyl_of_ne_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.html#TauCeti.GL2Borel.doubleCosetMk_eq_weyl_of_ne_one)
- [Source of `TauCeti.GL2Borel.doubleCosetMk_eq_weyl_of_ne_one` in TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/GeneralLinearGroup/Bruhat.lean#L304)
