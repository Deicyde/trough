---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Units.UnitCandidateEliminationCertificate.sound
statement: formalized
proof: formalized
---

# Soundness of unit-candidate elimination

A unit expanding at a real place generates
modulo torsion if every candidate below its absolute value has been eliminated.

```lean
TauCeti.NumberField.Units.UnitCandidateEliminationCertificate.sound.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {u : (NumberField.RingOfIntegers K)ˣ} {w : NumberField.InfinitePlace K}
  (h :
    TauCeti.NumberField.Units.UnitCandidateEliminationCertificate K
      (w ((algebraMap (NumberField.RingOfIntegers K) K) ↑u)))
  (hr : NumberField.Units.rank K = 1) (hp : Nat.Prime (Module.finrank ℚ K)) (hw : w.IsReal)
  (hu : 1 < w ((algebraMap (NumberField.RingOfIntegers K) K) ↑u)) :
  Subgroup.closure {u} ⊔ NumberField.Units.torsion K = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.UnitCandidateEliminationCertificate.sound`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Elimination/Basic.html#TauCeti.NumberField.Units.UnitCandidateEliminationCertificate.sound).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.UnitCandidateEliminationCertificate.sound`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Elimination/Basic.html#TauCeti.NumberField.Units.UnitCandidateEliminationCertificate.sound)
- [Source of `TauCeti.NumberField.Units.UnitCandidateEliminationCertificate.sound` in TauCeti/NumberTheory/NumberField/Units/Elimination/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Units/Elimination/Basic.lean#L97)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/NumberFieldArithmetic/STATUS.md)
