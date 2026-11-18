---
declaration: theorem
origin: cited
lean: DirichletCharacter.exists_differentiableOn_exp_eq_LFunction
statement: formalized
proof: formalized
---

# The logarithm of a Dirichlet `L`-function continues across `re s = 1`

For a nontrivial
Dirichlet character `χ`, some open neighbourhood `Ω` of the closed half-plane `1 ≤ re s` carries a
holomorphic `F` with `exp (F s) = L(χ, s)` on `Ω` and with `F s` the sum of the absolutely
convergent `L`-series of `DirichletCharacter.eulerLogCoeff χ` for `1 < re s`.

`Ω` need not contain a strip `1 - δ < re s` of uniform width.

```lean
DirichletCharacter.exists_differentiableOn_exp_eq_LFunction {N : ℕ} (χ : DirichletCharacter ℂ N)
  [NeZero N] (hχ : χ ≠ 1) :
  ∃ Ω,
    IsOpen Ω ∧
      {s | 1 ≤ s.re} ⊆ Ω ∧
        ∃ F,
          DifferentiableOn ℂ F Ω ∧
            (∀ s ∈ Ω, Complex.exp (F s) = DirichletCharacter.LFunction χ s) ∧
              ∀ (s : ℂ), 1 < s.re → LSeriesHasSum χ.eulerLogCoeff s (F s)
```

## Depends on

- [DirichletCharacter.eulerLogCoeff](dirichletcharacter-eulerlogcoeff.md)

## Proof depends on

- [A logarithm on an open half-plane extends across its boundary line](a-logarithm-on-an-open-half-plane-extends-across.md)

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.exists_differentiableOn_exp_eq_LFunction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/DirichletEulerLog.html#DirichletCharacter.exists_differentiableOn_exp_eq_LFunction).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.exists_differentiableOn_exp_eq_LFunction`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/DirichletEulerLog.html#DirichletCharacter.exists_differentiableOn_exp_eq_LFunction)
- [Source of `DirichletCharacter.exists_differentiableOn_exp_eq_LFunction` in TauCeti/NumberTheory/LSeries/DirichletEulerLog.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/DirichletEulerLog.lean#L126)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
