---
declaration: theorem
origin: cited
lean: PFun.turingJoin_turingReducible_iff
statement: formalized
proof: formalized
---

# The Turing join is the least upper bound for Turing reducibility

it is reducible to `h`
exactly when both of its sides are.

```lean
PFun.turingJoin_turingReducible_iff {f g h : ℕ →. ℕ} :
  TuringReducible (f.turingJoin g) h ↔ TuringReducible f h ∧ TuringReducible g h
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PFun.turingJoin_turingReducible_iff`](https://taucetiproject.org/docs/TauCeti/Computability/TuringDegree.html#PFun.turingJoin_turingReducible_iff).

## Sources

- [Tau Ceti documentation: `PFun.turingJoin_turingReducible_iff`](https://taucetiproject.org/docs/TauCeti/Computability/TuringDegree.html#PFun.turingJoin_turingReducible_iff)
- [Source of `PFun.turingJoin_turingReducible_iff` in TauCeti/Computability/TuringDegree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Computability/TuringDegree.lean#L213)
