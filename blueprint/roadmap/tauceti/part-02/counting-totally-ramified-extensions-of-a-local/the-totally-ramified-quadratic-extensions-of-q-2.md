---
declaration: theorem
origin: cited
lean: TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo
statement: formalized
proof: formalized
---

# The totally ramified quadratic extensions of `ℚ_2`

If `x₁, …, x₆` are square roots of
`-1, -5, 2, -2, 10, -10` in the separable closure of `ℚ_2`, then
`σ_{ℚ_2}(2) = {ℚ_2(x₁), ℚ_2(x₂), ℚ_2(x₃), ℚ_2(x₄), ℚ_2(x₅), ℚ_2(x₆)}`.

```lean
TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo {x₁ x₂ x₃ x₄ x₅ x₆ : SeparableClosure ℚ_[2]}
  (h₁ : x₁ ^ 2 = -1) (h₂ : x₂ ^ 2 = -5) (h₃ : x₃ ^ 2 = 2) (h₄ : x₄ ^ 2 = -2) (h₅ : x₅ ^ 2 = 10)
  (h₆ : x₆ ^ 2 = -10) :
  TauCeti.totallyRamifiedOfDegree ℚ_[2] 2 =
    {ℚ_[2]⟮x₁⟯, ℚ_[2]⟮x₂⟯, ℚ_[2]⟮x₃⟯, ℚ_[2]⟮x₄⟯, ℚ_[2]⟮x₅⟯, ℚ_[2]⟮x₆⟯}
```

## Depends on

- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [IntermediateField.wildExponent](intermediatefield-wildexponent.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae](../../part-06/quadratic-forms-and-cohomological-invariants/tauceti-quaternionalgebra-nonempty-algequiv-matr.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo).

## Sources

- [Tau Ceti documentation: `TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo)
- [Source of `TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo` in TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean#L242)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
