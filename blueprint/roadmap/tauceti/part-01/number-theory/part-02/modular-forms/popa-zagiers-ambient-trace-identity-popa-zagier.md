---
declaration: theorem
origin: cited
lean: TauCeti.TraceFormulaMatrixModule.PeriodRelation.trace_periodAction_eq
statement: formalized
proof: formalized
---

# Popa–Zagier's ambient trace identity (Popa–Zagier, §2, Propositions 2 and 3)

for positive
even `w`, `k = w + 2`, `n ≥ 1`, and any `ξ ∈ ℂ[ℳₙ]` satisfying both the period relation (A) and
the exchange relations (B), the trace of `ξ` on the ambient space `V_w` of degree-`w` binary forms
is `2 Tr(Tₙ | S_k(SL(2, ℤ))) + σ_{w+1}(n)`.

```lean
TauCeti.TraceFormulaMatrixModule.PeriodRelation.trace_periodAction_eq {k : ℤ} {w : ℕ}
  (hk : k = ↑w + 2) (hw : Even w) (hw₀ : w ≠ 0) (n : ℕ) [NeZero n]
  {ξ : MonoidAlgebra ℂ (TauCeti.TraceFormulaMatrixModule ↑n)}
  (hP : TauCeti.TraceFormulaMatrixModule.PeriodRelation ℂ (↑n) ξ)
  (hX : TauCeti.TraceFormulaMatrixModule.ExchangeRelations ℂ (↑n) ξ) :
  (LinearMap.trace ℂ ↥(MvPolynomial.homogeneousSubmodule (Fin 2) ℂ w))
      ((TauCeti.TraceFormulaMatrixModule.periodAction hw) ξ) =
    2 *
        (LinearMap.trace ℂ (CuspForm (Matrix.SpecialLinearGroup.mapGL ℝ).range k))
          (TauCeti.heckeTCuspLevelOne k n) +
      ↑((ArithmeticFunction.sigma (w + 1)) n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton in size two](../../../linear-algebra/matrix/cayley-hamilton-in-size-two.md)
- [Classical Sturm bound for finite-index subgroups of `SL(2, ℤ)`](classical-sturm-bound-for-finite-index-subgroups.md)
- [The Main Lemma, per character (Miyake, Lemma 4.6.8; Diamond–Shurman, Theorem 5.7.1)](the-main-lemma-per-character-miyake-lemma-4-6-8.md)
- [Manin's lemma](manins-lemma.md)
- [The Petersson adjoint formula in the second argument](the-petersson-adjoint-formula-in-the-second-argu.md)
- [Popa–Zagier's criterion for `(1 - T)·ℛₙ`](popa-zagiers-criterion-for-1-t-rn.md)
- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)
- [Shimura's decomposition of a double coset into right cosets](../hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)
- [Sturm bound for subgroups of `GL(2, ℝ)` of finite relative index in `SL(2, ℤ)` with discrete strict periods](sturm-bound-for-subgroups-of-gl-2-r-of-finite-re.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TraceFormulaMatrixModule.PeriodRelation.trace_periodAction_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/PeriodPolynomial/EichlerShimura.html#TauCeti.TraceFormulaMatrixModule.PeriodRelation.trace_periodAction_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.TraceFormulaMatrixModule.PeriodRelation.trace_periodAction_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/PeriodPolynomial/EichlerShimura.html#TauCeti.TraceFormulaMatrixModule.PeriodRelation.trace_periodAction_eq)
- [Source of `TauCeti.TraceFormulaMatrixModule.PeriodRelation.trace_periodAction_eq` in TauCeti/NumberTheory/ModularForms/LevelOne/PeriodPolynomial/EichlerShimura.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/LevelOne/PeriodPolynomial/EichlerShimura.lean#L529)
