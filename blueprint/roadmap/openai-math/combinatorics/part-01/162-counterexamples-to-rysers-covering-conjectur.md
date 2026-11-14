---
declaration: section
origin: cited
lean: OAI.Balanced.main_result, OAI.RyserCoveringCounterexample.exists_prime_eventually_counterexampleRank, OAI.RyserOdd.eventualOddFailures_and_infinite
statement: formalized
---

# 162. Counterexamples to Ryser’s covering conjecture

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves Ryser's covering conjecture by constructing intersecting $(q+1)$-partite, $(q+1)$-uniform hypergraphs with covering number $q+1$, rather than the predicted bound *q*, for every sufficiently large prime *q*. A separate construction over extension fields also disproves Gyárfás's monochromatic tree-cover conjecture.

## Balanced counterexamples to Ryser's conjecture at prime orders

For every sufficiently large prime *q*, we construct a finite intersecting $(q+1)$-partite $(q+1)$-uniform hypergraph with covering number $q+1$ and exactly $q+1$ nonisolated vertices in each part. This disproves Ryser's covering conjecture, even for intersecting hypergraphs with equally sized parts.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Balanced-Counterexamples-to-Rysers-Conjecture-at-Prime-Orders-September-27-2026/paper.pdf); the Lean below formalizes results from it.

## A counterexample to Ryser's covering conjecture

For every sufficiently large prime $s\equiv2\pmod3$ and every sufficiently large odd integer *n*, with the threshold depending on *s*, we construct an intersecting $(s^n+1)$-partite $(s^n+1)$-uniform hypergraph with covering number $s^n+1$. This disproves Ryser's covering conjecture in its intersecting case.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Counterexample-to-Rysers-Covering-Conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Ryser's covering conjecture predicts that an intersecting $r$-partite hypergraph has a vertex cover of size at most $r-1$. The formalization proves that every sufficiently large prime $q$ has a finite intersecting $(q+1)$-partite, $(q+1)$-uniform hypergraph with covering number $q+1$ and exactly $q+1$ nonisolated vertices in each part. Thus the conjecture fails even with equal part sizes. The prime threshold is existential.

Ryser's covering conjecture predicts $\tau\le(r-1)\nu$ for an $r$-partite hypergraph, where $\tau$ and $\nu$ are its covering and matching numbers. The formalized constructions give finite intersecting $r$-partite $r$-uniform hypergraphs with $\nu=1$ and $\tau=r$, contradicting the bound. The ranks have the form $r=p^n+1$: one fixed prime $p\equiv2\pmod3$ works for all sufficiently large prime degrees $n$, and a second result covers every sufficiently large such prime $p$ and every sufficiently large odd $n$, with the degree threshold allowed to depend on $p$. Infinitely many ranks occur. Equal part sizes and numerical thresholds are not asserted.

## Lean: Balanced Ryser counterexamples at prime orders

```lean
theorem main_result : MainResult
```

Stated in [BalancedRyser.lean, line 39](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BalancedRyser.lean#L39). Its proof is in [lean/OAI/Combinatorics/BalancedRyser/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/BalancedRyser/Main.lean) or a file it imports further down, which this chapter does not read.

## Lean: Fixed-prime Ryser counterexamples

```lean
theorem exists_prime_eventually_counterexampleRank :
    ∃ p : ℕ, p.Prime ∧ 5 < p ∧ p % 3 = 2 ∧
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n → n.Prime → 2 < n →
        CounterexampleRank (p ^ n + 1)
```

Stated in [RyserCovering.lean, line 49](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RyserCovering.lean#L49). Proved in [lean/OAI/Combinatorics/Ryser/Construction/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Ryser/Construction/Main.lean#L14). formalization.yaml lists it as one of the repository's main results.

## Lean: Counterexamples in odd extension degrees

```lean
theorem eventualOddFailures_and_infinite :
    (∃ primeThreshold : ℕ, ∀ prime : ℕ, primeThreshold ≤ prime →
      prime.Prime → prime % 3 = 2 →
      ∃ degreeThreshold : ℕ, 3 ≤ degreeThreshold ∧
        ∀ degree : ℕ, degreeThreshold ≤ degree → Odd degree →
          Specification.ExplicitFailureAt (prime ^ degree + 1)) ∧
    Set.Infinite {rank : ℕ | Specification.ExplicitFailureAt rank}
```

Stated in [RyserOddExtensions.lean, line 61](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RyserOddExtensions.lean#L61). Proved in [lean/OAI/Combinatorics/Ryser/OddExtensions.lean, line 132](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Ryser/OddExtensions.lean#L132). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/162.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/162.md)
