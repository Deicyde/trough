---
declaration: theorem
origin: cited
lean: TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq
statement: formalized
proof: formalized
---

# TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq

Two symmetric gauges that induce the same operator-ideal family over a
`RCLike` scalar field have equal extensions on every antitone `ℝ≥0∞`-valued sequence.

```lean
TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq {𝕜 : Type} [RCLike 𝕜]
  {Φ Ψ : TauCeti.SymmetricGauge}
  (h :
    TauCeti.SymmetricGauge.operatorIdealFamily 𝕜 Φ = TauCeti.SymmetricGauge.operatorIdealFamily 𝕜 Ψ)
  {a : ℕ → ENNReal} (ha : Antitone a) : Φ.extend a = Ψ.extend a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ky Fan triangle inequality](../../part-03/operator-ideal/ky-fan-triangle-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/SymmetricGauge/Faithfulness.html#TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/Family/SymmetricGauge/Faithfulness.html#TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq)
- [Source of `TauCeti.SymmetricGauge.extend_eq_of_operatorIdealFamily_eq` in TauCeti/Analysis/OperatorIdeal/Family/SymmetricGauge/Faithfulness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/OperatorIdeal/Family/SymmetricGauge/Faithfulness.lean#L44)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorTheory/STATUS.md)
