---
declaration: theorem
origin: cited
lean: Erdos363.erdos_363
statement: formalized
---

# Erdős Problem 363

> *References:*
> - [erdosproblems.com/363](https://www.erdosproblems.com/363)
> - [BaBe07] Bauer, Mark and Bennett, Michael A., *On a question of Erd\H{o}s
>   and Graham*. Enseign. Math. (2) (2007), 259--264.
> - [BeVL12] Bennett, Michael A. and Van Luijk, Ronald, *Squares from blocks of
>   consecutive integers: a problem of Erd\H{o}s and Graham*. Indag. Math. (N.S.)
>   (2012), 123--127.
> - [Ul05] Ulas, Maciej, *On products of disjoint blocks of consecutive integers*.
>   Enseign. Math. (2) (2005), 331--334.

*Quoted from [FormalConjectures/ErdosProblems/363.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/363.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/363](https://www.erdosproblems.com/363).

The file states 1 research or textbook statement: 1 solved.

## `Erdos363.erdos_363`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos363.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos363.lean).

> Is it true that, for each fixed $n$ and fixed sizes $k_1,\ldots,k_n \geq 4$, there are only finitely
> many collections of disjoint intervals $I_1,\ldots,I_n$ of size $\lvert I_i\rvert = k_i$ for
> $1\leq i\leq n$ such that
>
> $$\prod_{1\leq i\leq n}\prod_{m\in I_i}m$$
>
> is a square?
>
> The number of intervals and their sizes are fixed: the list `ks` of sizes determines both. Without
> this restriction finiteness fails, by a result of Skałba (see [Ul05]).
>
> This is false: Ulas [Ul05] constructed infinitely many such collections with $n = 4$ and
> $k_1 = \cdots = k_4 = 4$.

```lean
theorem erdos_363 : ¬ ∀ ks : List ℕ,
    {S : List (Finset ℕ) | IsValidCollection S ∧ S.map Finset.card = ks}.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/363.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/363.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/363.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/363.lean)
- [erdosproblems.com/363](https://www.erdosproblems.com/363)
