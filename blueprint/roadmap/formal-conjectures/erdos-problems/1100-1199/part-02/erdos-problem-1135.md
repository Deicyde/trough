---
declaration: theorem
origin: cited
lean: Erdos1135.erdos_1135
statement: formalized
---

# Erdős Problem 1135

> The Collatz conjecture states that for any positive integer $n$, there exists a natural
> number $m$ such that the $m$-th term of the sequence is 1.
>
> *References:*
> - [erdosproblems.com/1135](https://www.erdosproblems.com/1135)
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
> - [La10] Lagarias, Jeffrey C., The {$3x+1$} problem: an overview. (2010), 3--29.
> - [La16] Lagarias, Jeffrey C., Erdős, Klarner, and the {$3x+1$} problem. Amer. Math. Monthly
>   (2016), 753--776.
> - [La85] Lagarias, Jeffrey C., The {$3x+1$} problem and its generalizations. Amer. Math. Monthly
>   (1985), 3--23.
>
> This file points to the canonical formalization in
> `FormalConjectures.Wikipedia.CollatzConjecture`.

*Quoted from [FormalConjectures/ErdosProblems/1135.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1135.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1135](https://www.erdosproblems.com/1135).

The file states 1 research or textbook statement: 1 open.

## `Erdos1135.erdos_1135`

Open: stated without proof.

> The Collatz conjecture states that for any positive integer $n$, there exists a natural
> number $m$ such that the $m$-th term of the sequence is 1.

```lean
theorem erdos_1135 : type_of% CollatzConjecture.collatz_conjecture
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../../../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1135.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1135.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1135.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1135.lean)
- [erdosproblems.com/1135](https://www.erdosproblems.com/1135)
