---
declaration: theorem
origin: cited
lean: Erdos430.erdos_430
statement: formalized
---

# Erdős Problem 430

> *References:*
> - [erdosproblems.com/430](https://www.erdosproblems.com/430)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
>
> The question is equivalent to the first part of
> [Erdős Problem 385](https://www.erdosproblems.com/385) (an observation of Sarosh Adenwalla
> recorded on both problem pages).

*Quoted from [FormalConjectures/ErdosProblems/430.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/430.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/430](https://www.erdosproblems.com/430).

The file states 1 research or textbook statement: 1 open. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos430.erdos_430`

Open: stated without proof.

> Fix some integer $n$ and define a decreasing sequence in $[1,n)$ by $a_1=n-1$ and, for
> $k\geq 2$, letting $a_k$ be the greatest integer in $[1,a_{k-1})$ such that all of the prime
> factors of $a_k$ are $>n-a_k$.
>
> Is it true that, for sufficiently large $n$, not all of this sequence can be prime?

```lean
theorem erdos_430 : ∀ᶠ n in atTop, ¬ ∀ m ∈ terms n, m.Prime
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/430.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/430.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/430.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/430.lean)
- [erdosproblems.com/430](https://www.erdosproblems.com/430)
