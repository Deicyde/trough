---
declaration: theorem
origin: cited
lean: TauCeti.Probability.integerWalk_isRecurrent_iff
statement: formalized
proof: formalized
---

# TauCeti.Probability.integerWalk_isRecurrent_iff

An integer walk returns almost surely exactly for the symmetric step law.
This includes the deterministic parameters zero and one.

```lean
TauCeti.Probability.integerWalk_isRecurrent_iff (p : ↑unitInterval) (x : ℤ) :
  (TauCeti.Probability.integerWalk p).IsRecurrent x ↔ ↑p = 1 / 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The recurrence criterion](the-recurrence-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.integerWalk_isRecurrent_iff`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Examples/IntegerWalk/Recurrence.html#TauCeti.Probability.integerWalk_isRecurrent_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.integerWalk_isRecurrent_iff`](https://taucetiproject.org/docs/TauCeti/Probability/MarkovChain/Examples/IntegerWalk/Recurrence.html#TauCeti.Probability.integerWalk_isRecurrent_iff)
- [Source of `TauCeti.Probability.integerWalk_isRecurrent_iff` in TauCeti/Probability/MarkovChain/Examples/IntegerWalk/Recurrence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/MarkovChain/Examples/IntegerWalk/Recurrence.lean#L54)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)
