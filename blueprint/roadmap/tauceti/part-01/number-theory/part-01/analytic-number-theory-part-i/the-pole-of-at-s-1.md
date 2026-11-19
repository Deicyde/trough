---
declaration: theorem
origin: cited
lean: TauCeti.exists_norm_neg_logDeriv_riemannZeta_one_add_sub_inv_le
statement: formalized
proof: formalized
---

# The pole of `-ζ′/ζ` at `s = 1`

One absolute constant `C` satisfies
`‖-ζ′/ζ(1 + η) - η⁻¹‖ ≤ C` for every `0 < η ≤ 1`.

```lean
TauCeti.exists_norm_neg_logDeriv_riemannZeta_one_add_sub_inv_le :
  ∃ C, ∀ (η : ℝ), 0 < η → η ≤ 1 → ‖-logDeriv riemannZeta (1 + ↑η) - (↑η)⁻¹‖ ≤ C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_norm_neg_logDeriv_riemannZeta_one_add_sub_inv_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/RiemannZeta/LogDerivNearOne.html#TauCeti.exists_norm_neg_logDeriv_riemannZeta_one_add_sub_inv_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_norm_neg_logDeriv_riemannZeta_one_add_sub_inv_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/RiemannZeta/LogDerivNearOne.html#TauCeti.exists_norm_neg_logDeriv_riemannZeta_one_add_sub_inv_le)
- [Source of `TauCeti.exists_norm_neg_logDeriv_riemannZeta_one_add_sub_inv_le` in TauCeti/NumberTheory/LSeries/RiemannZeta/LogDerivNearOne.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/RiemannZeta/LogDerivNearOne.lean#L60)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
