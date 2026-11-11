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

- [Set.jump](set-jump.md)

## Proof depends on

- [Adequacy](adequacy.md)
- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)
- [The use principle](the-use-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo)
- [Source of `TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo` in TauCeti/Computability/FriedbergMuchnik/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/FriedbergMuchnik/Basic.lean#L404)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
