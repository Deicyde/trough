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

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Serre's formula for the Artin conductor](../local-fields-and-ramification/serres-formula-for-the-artin-conductor.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo).

## Sources

- [Tau Ceti documentation: `TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo)
- [Source of `TauCeti.totallyRamifiedOfDegree_two_eq_padicTwo` in TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean#L234)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
