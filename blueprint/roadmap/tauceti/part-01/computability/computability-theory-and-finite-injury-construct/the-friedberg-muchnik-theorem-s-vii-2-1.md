---
declaration: theorem
origin: cited
lean: TauCeti.friedberg_muchnik
statement: formalized
proof: formalized
---

# The Friedberg–Muchnik theorem [S, VII.2.1]

```lean
TauCeti.friedberg_muchnik :
  ∃ A B,
    (REPred fun x => x ∈ A) ∧
      (REPred fun x => x ∈ B) ∧
        ¬TuringReducible A.oracle B.oracle ∧ ¬TuringReducible B.oracle A.oracle
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Adequacy](adequacy.md)
- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)
- [The use principle](the-use-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.friedberg_muchnik`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.friedberg_muchnik).

## Sources

- [Tau Ceti documentation: `TauCeti.friedberg_muchnik`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.friedberg_muchnik)
- [Source of `TauCeti.friedberg_muchnik` in TauCeti/Computability/FriedbergMuchnik/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/FriedbergMuchnik/Basic.lean#L363)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
