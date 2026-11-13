---
declaration: theorem
origin: cited
lean: Erdos1058.erdos_1058, Erdos1058.erdos_1058.variants.luca
statement: formalized
---

# Erdős Problem 1058

> *References:*
> - [erdosproblems.com/1058](https://www.erdosproblems.com/1058)
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
> - [Lu01] Luca, Florian, *On a conjecture of Erdős and Stewart*. Math. Comp. (2001), 893-896.

*Quoted from [FormalConjectures/ErdosProblems/1058.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1058.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1058](https://www.erdosproblems.com/1058).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1058.erdos_1058`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1058.lean#L47](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1058.lean#L47).

> Let $2=p_1\lt p_2\lt \cdots$ be the sequence of prime numbers. Are there only finitely many $n$ such
> that $n\in [p_{k-1},p_k)$ and the only primes dividing $n!+1$ are $p_{k}$ and $p_{k+1}$?
>
> A conjecture of Erdős and Stewart, as reported in problem A2 of Guy's collection [Gu04]. The only
> known cases are $n=1,2,3,4,5$. Luca [Lu01] proved that indeed these are the only solutions.

```lean
theorem erdos_1058 : {n | IsSolution n}.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1058.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1058.lean#L55).

## `Erdos1058.erdos_1058.variants.luca`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1058.lean#L47](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1058.lean#L47).

> Luca [Lu01] proved that $n = 1, 2, 3, 4, 5$ are the only solutions.

```lean
theorem erdos_1058.variants.luca : {n | IsSolution n} = {1, 2, 3, 4, 5}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1058.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1058.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1058.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1058.lean)
- [erdosproblems.com/1058](https://www.erdosproblems.com/1058)
