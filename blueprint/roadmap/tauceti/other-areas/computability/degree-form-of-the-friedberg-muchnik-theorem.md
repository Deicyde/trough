---
declaration: theorem
origin: cited
lean: TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo
statement: formalized
proof: formalized
---

# Degree form of the Friedberg–Muchnik theorem

```lean
TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo :
  ∃ A B,
    (REPred fun x => x ∈ A) ∧
      (REPred fun x => x ∈ B) ∧
        toAntisymmetrization TuringReducible A.oracle ∈
            Set.Ioo (toAntisymmetrization TuringReducible ∅.oracle)
              (toAntisymmetrization TuringReducible ∅.jump.oracle) ∧
          toAntisymmetrization TuringReducible B.oracle ∈
              Set.Ioo (toAntisymmetrization TuringReducible ∅.oracle)
                (toAntisymmetrization TuringReducible ∅.jump.oracle) ∧
            ¬toAntisymmetrization TuringReducible A.oracle ≤
                  toAntisymmetrization TuringReducible B.oracle ∧
              ¬toAntisymmetrization TuringReducible B.oracle ≤
                  toAntisymmetrization TuringReducible A.oracle
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo)
- [Source of `TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo` in TauCeti/Computability/FriedbergMuchnik/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Computability/FriedbergMuchnik/Basic.lean#L404)
