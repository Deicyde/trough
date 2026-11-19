---
declaration: theorem
origin: cited
lean: TauCeti.Probability.ergodicSMul_infinitePi_const
statement: formalized
proof: formalized
---

# Hewitt–Savage in ergodic form

The finitely supported permutations of the time index act
ergodically on an i.i.d. product law `P^{⊗ℕ}`.

This is the zero-one law `exchangeableSigma_trivial_of_infinitePi` read through
`exchangeableSigma_trivial_iff_ergodicSMul`.  It is the permutation-action counterpart of the
shift ergodicity recorded by
`MeasureTheory.Measure.ergodic_shift_infinitePi_const`.

```lean
TauCeti.Probability.ergodicSMul_infinitePi_const.{u_1} {α : Type u_1} [MeasurableSpace α]
  (P : MeasureTheory.ProbabilityMeasure α) :
  ErgodicSMul TauCeti.FinitaryPerm (ℕ → α) (MeasureTheory.Measure.infinitePi fun x => ↑P)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.ergodicSMul_infinitePi_const`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/PathSpace/Exchangeable/Ergodic.html#TauCeti.Probability.ergodicSMul_infinitePi_const).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.ergodicSMul_infinitePi_const`](https://taucetiproject.org/docs/TauCeti/Probability/Exchangeability/PathSpace/Exchangeable/Ergodic.html#TauCeti.Probability.ergodicSMul_infinitePi_const)
- [Source of `TauCeti.Probability.ergodicSMul_infinitePi_const` in TauCeti/Probability/Exchangeability/PathSpace/Exchangeable/Ergodic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Exchangeability/PathSpace/Exchangeable/Ergodic.lean#L190)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Exchangeability/STATUS.md)
