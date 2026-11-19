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
- [Source of `TauCeti.exists_incomparable_ce_turingDegrees_mem_Ioo` in TauCeti/Computability/FriedbergMuchnik/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/FriedbergMuchnik/Basic.lean#L404)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
