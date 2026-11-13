---
declaration: theorem
origin: cited
lean: Erdos903.erdos_903
statement: formalized
---

# Erdős Problem 903

> *References:*
> - [erdosproblems.com/903](https://www.erdosproblems.com/903)
> - [EFSW85] Erdős, P. and Fowler, Joel C. and S\'os, Vera T. and Wilson, Richard M., On {$2$}-designs.
>   J. Combin. Theory Ser. A (1985), 131--142.
> - [dBEr48] de Bruijn, N. G. and Erdős, P., On a combinatorial problem. Nederl. Akad. Wetensch.,
>   Proc. (1948), 1277--1279 = Indagationes Math. 10, 421--423.

*Quoted from [FormalConjectures/ErdosProblems/903.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/903.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/903](https://www.erdosproblems.com/903).

The file states 1 research or textbook statement: 1 solved.

## `Erdos903.erdos_903`

Solved: stated here without proof.

> Let $n=p^2+p+1$ for some prime power $p$, and let $A_1,\ldots,A_t\subseteq \{1,\ldots,n\}$ be a
> block design (so that every pair $x,y\in \{1,\ldots,n\}$ is contained in exactly one $A_i$). Is it
> true that if $t>n$ then $t\geq n+p$?
>
> This is true, and was proved by Erdős, Fowler, Sós, and Wilson [EFSW85].

```lean
theorem erdos_903 :
    ∀ p : ℕ, IsPrimePow p →
    ∀ H : Finset (Finset (Fin (p ^ 2 + p + 1))),
      H.IsPairwiseBalancedDesign → p ^ 2 + p + 1 < H.card →
        p ^ 2 + p + 1 + p ≤ H.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/903.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/903.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/903.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/903.lean)
- [erdosproblems.com/903](https://www.erdosproblems.com/903)
