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
- [Source of `TauCeti.Probability.ergodicSMul_infinitePi_const` in TauCeti/Probability/Exchangeability/PathSpace/Exchangeable/Ergodic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Exchangeability/PathSpace/Exchangeable/Ergodic.lean#L192)
- [Tau Ceti roadmap status: Exchangeability and de Finetti](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Exchangeability/STATUS.md)
