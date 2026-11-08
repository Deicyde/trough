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

## Lean

Formalized in Tau Ceti as [`TauCeti.friedberg_muchnik`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.friedberg_muchnik).

## Sources

- [Tau Ceti documentation: `TauCeti.friedberg_muchnik`](https://taucetiproject.org/docs/TauCeti/Computability/FriedbergMuchnik/Basic.html#TauCeti.friedberg_muchnik)
- [Source of `TauCeti.friedberg_muchnik` in TauCeti/Computability/FriedbergMuchnik/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Computability/FriedbergMuchnik/Basic.lean#L363)
