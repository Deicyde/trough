---
declaration: theorem
origin: cited
lean: TauCeti.SacksSplitting.exists_split_low_not_turingReducible, TauCeti.SacksSplitting.exists_split_not_turingReducible
statement: formalized
proof: formalized
---

# Sacks's splitting theorem with low halves [S, VII.3.2]

every c.e. set `B` is the union
of two disjoint low c.e. sets, neither of which computes a prescribed noncomputable c.e. set `C`.
The set `B` may be empty or finite.

```lean
TauCeti.SacksSplitting.exists_split_low_not_turingReducible {B C : Set ℕ}
  (hB : REPred fun x => x ∈ B) (hC : REPred fun x => x ∈ C) (hnc : ¬ComputablePred fun x => x ∈ C) :
  ∃ A₀ A₁,
    (REPred fun x => x ∈ A₀) ∧
      (REPred fun x => x ∈ A₁) ∧
        Disjoint A₀ A₁ ∧
          A₀ ∪ A₁ = B ∧
            A₀.Low ∧
              A₁.Low ∧ ¬TuringReducible C.oracle A₀.oracle ∧ ¬TuringReducible C.oracle A₁.oracle
```

## Depends on

- [Set.Low](../computability-theory-and-finite-injury-construct/set-low.md)

## Proof depends on

- [Adequacy](../computability-theory-and-finite-injury-construct/adequacy.md)
- [Limit Lemma, computing the limit](../computability-theory-and-finite-injury-construct/limit-lemma-computing-the-limit.md)
- [Set.jump](../computability-theory-and-finite-injury-construct/set-jump.md)
- [Soare's Lemma 1](soares-lemma-1.md)
- [TauCeti.Oracle.Single.Code](../computability-theory-and-finite-injury-construct/tauceti-oracle-single-code.md)
- [TauCeti.Priority.injurySet](../computability-theory-and-finite-injury-construct/tauceti-priority-injuryset.md)
- [The use principle](../computability-theory-and-finite-injury-construct/the-use-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SacksSplitting.exists_split_low_not_turingReducible`](https://taucetiproject.org/docs/TauCeti/Computability/SacksSplitting/Low.html#TauCeti.SacksSplitting.exists_split_low_not_turingReducible).

## Other forms

**Sacks's splitting theorem without the lowness clause [S, VII.3.2].** Formalized in Tau Ceti as [`TauCeti.SacksSplitting.exists_split_not_turingReducible`](https://taucetiproject.org/docs/TauCeti/Computability/SacksSplitting/Basic.html#TauCeti.SacksSplitting.exists_split_not_turingReducible).

```lean
TauCeti.SacksSplitting.exists_split_not_turingReducible {B C : Set ℕ} (hB : REPred fun x => x ∈ B)
  (hC : REPred fun x => x ∈ C) (hnc : ¬ComputablePred fun x => x ∈ C) :
  ∃ A₀ A₁,
    (REPred fun x => x ∈ A₀) ∧
      (REPred fun x => x ∈ A₁) ∧
        Disjoint A₀ A₁ ∧
          A₀ ∪ A₁ = B ∧ ¬TuringReducible C.oracle A₀.oracle ∧ ¬TuringReducible C.oracle A₁.oracle
```

## Sources

- [Tau Ceti documentation: `TauCeti.SacksSplitting.exists_split_low_not_turingReducible`](https://taucetiproject.org/docs/TauCeti/Computability/SacksSplitting/Low.html#TauCeti.SacksSplitting.exists_split_low_not_turingReducible)
- [Source of `TauCeti.SacksSplitting.exists_split_low_not_turingReducible` in TauCeti/Computability/SacksSplitting/Low.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/SacksSplitting/Low.lean#L119)
