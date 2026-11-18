---
declaration: section
origin: cited
lean: OAI.Ostmann.inverseGoldbach, OAI.Ostmann.twoInfiniteSummandsImpossible, OAI.Ostmann.main
statement: formalized
---

# 013. Ostmann’s inverse Goldbach conjecture

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that no finite modification of the primes can be written as $A+B$ with $A,B\subseteq\mathbb Z_{\ge0}$ each containing at least two elements. This resolves Ostmann's inverse Goldbach conjecture on additive indecomposability.

## The additive indecomposability of the primes

We prove Ostmann's inverse Goldbach conjecture: no set differing from the primes by finitely many elements can be written as $A+B$, where *A* and *B* are sets of nonnegative integers with at least two elements each.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/the-additive-indecomposability-of-the-primes-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves Ostmann's inverse Goldbach conjecture. For any two sets $A,B$ of nonnegative integers, each containing at least two elements, the symmetric difference between their sumset $A+B$ and the set of primes is infinite. Thus no set differing from the primes by only finitely many elements can be decomposed as such a sumset. The linked statements include the full result and its two-infinite-summands case.

## Lean: Ostmann's inverse Goldbach theorem and the infinite-summands case

```lean
theorem inverseGoldbach : InverseGoldbach
```

Stated in [OstmannComplete.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OstmannComplete.lean#L30). Proved in [lean/OAI/NumberTheory/Ostmann/Complete.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/Ostmann/Complete.lean#L21).

```lean
theorem twoInfiniteSummandsImpossible : TwoInfiniteSummandsImpossible
```

Stated in [OstmannComplete.lean, line 33](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OstmannComplete.lean#L33). Proved in [lean/OAI/NumberTheory/Ostmann/Complete.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/Ostmann/Complete.lean#L16).

## Lean: Additive indecomposability of the primes up to finite changes

```lean
theorem main : ∀ A B : Set ℕ, A.Nontrivial → B.Nontrivial →
    Set.Infinite ((A + B) ∆ {n : ℕ | Nat.Prime n})
```

Stated in [OstmannPrimes.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OstmannPrimes.lean#L9). Its proof is in [lean/OAI/NumberTheory/Ostmann/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/Ostmann/Main.lean) or a file it imports further down, which this chapter does not read.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/013.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/013.md)
