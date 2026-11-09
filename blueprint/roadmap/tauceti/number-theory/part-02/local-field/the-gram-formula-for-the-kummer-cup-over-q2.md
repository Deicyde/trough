---
declaration: theorem
origin: cited
lean: TauCeti.kummerCup_padicTwo
statement: formalized
proof: formalized
---

# The Gram formula for the Kummer cup over `ℚ₂`

In square-class coordinates along
`-1`, `2`, `5`, the cup is `x₀ y₀ + x₁ y₂ + x₂ y₁` times the nonzero class
`(-1) ∪ (-1)`. The scalar lies in `ZMod 2`.

```lean
TauCeti.kummerCup_padicTwo (x y : TauCeti.SquareClassGroup ℚ_[2]) :
  ((TauCeti.kummerCup ℚ_[2]) x) y =
    ((TauCeti.padicTwoSquareClassBasis.repr x) 0 * (TauCeti.padicTwoSquareClassBasis.repr y) 0 +
          (TauCeti.padicTwoSquareClassBasis.repr x) 1 *
            (TauCeti.padicTwoSquareClassBasis.repr y) 2 +
        (TauCeti.padicTwoSquareClassBasis.repr x) 2 * (TauCeti.padicTwoSquareClassBasis.repr y) 1) •
      ((TauCeti.kummerCup ℚ_[2]) (TauCeti.squareClass (-1))) (TauCeti.squareClass (-1))
```

## Depends on

- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)

## Proof depends on

- [A Kummer cup over a local field is its Hilbert symbol times a fixed nonzero cup](../../part-01/quadratic-forms-and-cohomological-invariants/a-kummer-cup-over-a-local-field-is-its-hilbert-s.md)
- [Serre's formula for the Artin conductor](../../part-01/local-fields-and-ramification/serres-formula-for-the-artin-conductor.md)
- [The splitting criterion for quaternion algebras](../../part-01/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.kummerCup_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/PadicTwo.html#TauCeti.kummerCup_padicTwo).

## Sources

- [Tau Ceti documentation: `TauCeti.kummerCup_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/PadicTwo.html#TauCeti.kummerCup_padicTwo)
- [Source of `TauCeti.kummerCup_padicTwo` in TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/PadicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/PadicTwo.lean#L71)
