---
declaration: theorem
origin: cited
lean: Erdos1140.erdos_1140, Erdos1140.erdos_1140.variants.at_most_one_exception
statement: formalized
---

# Erdős Problem 1140

> *References:*
> - [erdosproblems.com/1140](https://www.erdosproblems.com/1140)
> - [EpGi10] Epure, M. and Gica, A., *Principal quadratic real fields in connection with some
>   additive problems*. Bull. Math. Soc. Sci. Math. Roumanie (N.S.) (2010), 251-259.
> - [MoWi89] Mollin, R. A. and Williams, H. C., *Period four and real quadratic fields of class
>   number one*. Proc. Japan Acad. Ser. A Math. Sci. (1989), 89-93.
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/1140.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1140.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1140](https://www.erdosproblems.com/1140).

The file states 2 research or textbook statements: 2 solved. It also has 2 test statements, counted here but not shown.

## `Erdos1140.erdos_1140`

Solved: stated here without proof.

> Do there exist infinitely many $n$ such that $n-2x^2$ is prime for all $x$ with $2x^2\lt n$?
>
> The answer is no: see `erdos_1140.variants.at_most_one_exception`.

```lean
theorem erdos_1140 : ¬ {n : ℕ | Erdos1140Prop n}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1140.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1140.lean#L67).

## `Erdos1140.erdos_1140.variants.at_most_one_exception`

Solved: stated here without proof.

> The known such $n$ are $2,5,7,13,31,61,181,199$. It is known that these are, with at most one
> exception, all such $n$. An even such $n$ must be prime (take $x = 0$), so $n = 2$. Theorem 4.1
> of Epure and Gica [EpGi10] implies that the only such
> $n\equiv 1\pmod{4}$ are $5,13,61,181$, and their method, coupled with a result of Mollin and
> Williams [MoWi89], implies that the only such $n\equiv 3\pmod{4}$ are $7,31,199$, and at most one
> other exception.

```lean
theorem erdos_1140.variants.at_most_one_exception :
    ({n : ℕ | Erdos1140Prop n} \ {2, 5, 7, 13, 31, 61, 181, 199}).Subsingleton
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1140.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1140.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1140.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1140.lean)
- [erdosproblems.com/1140](https://www.erdosproblems.com/1140)
