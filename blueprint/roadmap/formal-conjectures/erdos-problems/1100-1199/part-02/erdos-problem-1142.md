---
declaration: theorem
origin: cited
lean: Erdos1142.erdos_1142, Erdos1142.erdos_1142.variants.mientka_weitzenkamp
statement: formalized
---

# Erdős Problem 1142

> *References:*
> - [erdosproblems.com/1142](https://www.erdosproblems.com/1142)
> - [A039669](https://oeis.org/A039669)
> - [Va99] Various, Some of Paul's favorite problems. Booklet produced for the conference "Paul Erdős
>   and his mathematics", Budapest, July 1999 (1999).
> - [MiWe69] Mientka, W. E. and Weitzenkamp, R. C., On f-plentiful numbers, Journal of
>   Combinatorial Theory, Volume 7, Issue 4, December 1969, pages 374-377.

*Quoted from [FormalConjectures/ErdosProblems/1142.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1142.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1142](https://www.erdosproblems.com/1142).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 8 test statements, counted here but not shown.

## `Erdos1142.erdos_1142`

Open: stated without proof.

> Are there infinitely many $n > 2$ such that $n - 2^k$ is prime for all $k \geq 1$ with $2^k < n$?
>
> The only known such $n$ are $4, 7, 15, 21, 45, 75, 105$ (OEIS [A039669](https://oeis.org/A039669)).

```lean
theorem erdos_1142 :
    Infinite { n | Erdos1142Prop n }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1142.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1142.lean#L55).

## `Erdos1142.erdos_1142.variants.mientka_weitzenkamp`

Solved: stated here without proof.

> Mientka and Weitzenkamp [MiWe69] proved that the only $n \leq 2^{44}$ such that $n > 2$ and
> $n - 2^k$ is prime for all $k \geq 1$ with $2^k < n$ are $4, 7, 15, 21, 45, 75, 105$.

```lean
theorem erdos_1142.variants.mientka_weitzenkamp :
    { n : ℕ | n ≤ 2 ^ 44 ∧ Erdos1142Prop n } = {4, 7, 15, 21, 45, 75, 105}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1142.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1142.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1142.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1142.lean)
- [erdosproblems.com/1142](https://www.erdosproblems.com/1142)
