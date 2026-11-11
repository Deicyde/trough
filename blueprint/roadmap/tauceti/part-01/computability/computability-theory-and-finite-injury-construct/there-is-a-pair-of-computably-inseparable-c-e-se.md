---
declaration: theorem
origin: cited
lean: TauCeti.exists_computablyInseparable_rePred
statement: formalized
proof: formalized
---

# There is a pair of computably inseparable c.e. sets, for instance the diagonal fibers over `0` and `1`

```lean
TauCeti.exists_computablyInseparable_rePred :
  ∃ A B, (REPred fun x => x ∈ A) ∧ (REPred fun x => x ∈ B) ∧ A.ComputablyInseparable B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_computablyInseparable_rePred`](https://taucetiproject.org/docs/TauCeti/Computability/Inseparable.html#TauCeti.exists_computablyInseparable_rePred).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_computablyInseparable_rePred`](https://taucetiproject.org/docs/TauCeti/Computability/Inseparable.html#TauCeti.exists_computablyInseparable_rePred)
- [Source of `TauCeti.exists_computablyInseparable_rePred` in TauCeti/Computability/Inseparable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/Inseparable.lean#L189)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
