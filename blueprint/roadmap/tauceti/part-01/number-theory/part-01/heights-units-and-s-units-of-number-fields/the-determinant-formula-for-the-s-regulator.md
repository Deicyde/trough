---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.SUnit.regulator_eq_abs_det
statement: formalized
proof: formalized
---

# The determinant formula for the `S`-regulator

For a family `ε` of `S`-units that, together
with the torsion subgroup, generates the `S`-units, an infinite place `w'` and any identification
`e` of `ι` with the places of `S` and the infinite places other than `w'`, the `S`-regulator is the
absolute value of the determinant of the matrix whose `i`-th row lists `mult w * log (w (ε i))` at
the infinite places `w ≠ w'` and `log ‖ε i‖_v` at the places `v ∈ S`, in the order given by `e`.
The family `ε` is then a fundamental system, its cardinality being forced by `e`. This is the
`S`-analogue of Mathlib's `NumberField.Units.regulator_eq_det`.

```lean
TauCeti.NumberField.SUnit.regulator_eq_abs_det.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K]
  {S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))} {ι : Type u_2}
  [Fintype ι] [DecidableEq ι] {ε : ι → ↥((↑S).unit K)}
  (hε : Subgroup.closure (Set.range ε) ⊔ CommGroup.torsion ↥((↑S).unit K) = ⊤)
  (w' : NumberField.InfinitePlace K) (e : ι ≃ { w // w ≠ w' } ⊕ ↥S) :
  TauCeti.NumberField.SUnit.regulator S =
    |(Matrix.of fun i k =>
          Sum.elim (fun w => ↑(↑w).mult * Real.log (↑w ↑↑(ε i)))
            (fun v => Real.log ((NumberField.FinitePlace.mk ↑v) ↑↑(ε i))) (e k)).det|
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.NumberField.SUnit.logEmbeddingEquiv](tauceti-numberfield-sunit-logembeddingequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.SUnit.regulator_eq_abs_det`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SUnits/Regulator.html#TauCeti.NumberField.SUnit.regulator_eq_abs_det).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.SUnit.regulator_eq_abs_det`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SUnits/Regulator.html#TauCeti.NumberField.SUnit.regulator_eq_abs_det)
- [Source of `TauCeti.NumberField.SUnit.regulator_eq_abs_det` in TauCeti/NumberTheory/NumberField/SUnits/Regulator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/SUnits/Regulator.lean#L130)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HeightsAndUnits/STATUS.md)
