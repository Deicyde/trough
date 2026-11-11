---
declaration: theorem
origin: cited
lean: Matrix.IsHermitian.tendsto_trace_exp_neg_smul_mul_div
statement: formalized
proof: formalized
---

# Zero-temperature limit of the Gibbs state

For a Hermitian matrix `K`, let `P₀` be the
spectral projection of `K` at its least eigenvalue, the orthogonal projection onto the lowest
eigenspace. As `β → +∞`, the Gibbs functionals
`x ↦ Tr (exp (-(β • K)) x) / Tr (exp (-(β • K)))` converge pointwise to
`x ↦ Tr (P₀ x) / Tr P₀`.

This reading assumes `Nonempty m`; for empty `m` there is no eigenvalue or normalized state, and
the statement holds trivially since every trace is zero and both sides are `0 / 0 = 0`.

```lean
Matrix.IsHermitian.tendsto_trace_exp_neg_smul_mul_div.{u_1} {m : Type u_1} [Fintype m]
  [DecidableEq m] {K : Matrix m m ℂ} (hK : K.IsHermitian) (x : Matrix m m ℂ) :
  Filter.Tendsto
    (fun β => (NormedSpace.exp (-(β • K)) * x).trace / (NormedSpace.exp (-(β • K))).trace)
    Filter.atTop
    (nhds
      ((cfc ({sInf (spectrum ℝ K)}.indicator 1) K * x).trace /
        (cfc ({sInf (spectrum ℝ K)}.indicator 1) K).trace))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.IsHermitian.tendsto_trace_exp_neg_smul_mul_div`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Exponential/ZeroTemperature.html#Matrix.IsHermitian.tendsto_trace_exp_neg_smul_mul_div).

## Sources

- [Tau Ceti documentation: `Matrix.IsHermitian.tendsto_trace_exp_neg_smul_mul_div`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Exponential/ZeroTemperature.html#Matrix.IsHermitian.tendsto_trace_exp_neg_smul_mul_div)
- [Source of `Matrix.IsHermitian.tendsto_trace_exp_neg_smul_mul_div` in TauCeti/Analysis/Matrix/Exponential/ZeroTemperature.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/Exponential/ZeroTemperature.lean#L55)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
