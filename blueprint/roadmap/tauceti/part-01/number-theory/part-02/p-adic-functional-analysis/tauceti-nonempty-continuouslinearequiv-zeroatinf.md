---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span
statement: formalized
proof: formalized
---

# TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span

An infinite-dimensional ultrametric Banach space of countable type (some sequence has dense
span) over a complete nontrivially normed field is continuously linearly equivalent to
`C₀(ℕ, K)`.

```lean
TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span.{u, v} {K : Type v}
  [NontriviallyNormedField K] [CompleteSpace K] {E : Type u} [NormedAddCommGroup E]
  [NormedSpace K E] [IsUltrametricDist E] [CompleteSpace E] (hE : ¬FiniteDimensional K E)
  {v : ℕ → E} (hv : Dense ↑(Submodule.span K (Set.range v))) :
  Nonempty (E ≃L[K] ZeroAtInftyContinuousMap ℕ K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riesz's lemma, translated form](../../../analysis/part-03/normed/part-02/rieszs-lemma-translated-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/ModelSpace.html#TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/ModelSpace.html#TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span)
- [Source of `TauCeti.nonempty_continuousLinearEquiv_zeroAtInfty_nat_of_dense_span` in TauCeti/Analysis/Normed/Module/Bases/ModelSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Bases/ModelSpace.lean#L167)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
