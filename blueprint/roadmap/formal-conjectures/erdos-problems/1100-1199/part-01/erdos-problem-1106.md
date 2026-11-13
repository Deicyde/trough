---
declaration: theorem
origin: cited
lean: Erdos1106.erdos_1106.parts.i, Erdos1106.erdos_1106.parts.ii
statement: formalized
---

# Erdős Problem 1106

> *References:*
> - [erdosproblems.com/1106](https://www.erdosproblems.com/1106)
> - [ScWi87] Schinzel, A. and Wirsing, E., Multiplicative properties of the partition function.
>   Proc. Indian Acad. Sci. Math. Sci. (1987), 297--303.

*Quoted from [FormalConjectures/ErdosProblems/1106.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1106.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1106](https://www.erdosproblems.com/1106).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1106.erdos_1106.parts.i`

Solved: stated here without proof.

> Let $p(n)$ be the partition number of $n$ and $F(n)$ be the number of distinct prime factors of
> $\prod_{i= 1} ^ {n} p(n)$, then $F(n)$ tends to infinity when $n$ tends to infinity.
>
> The answer is yes: Schinzel and Wirsing [ScWi87] proved $F(n) \gg \log n$.

```lean
theorem erdos_1106.parts.i :
    Tendsto (fun n ↦ #(∏ i ∈ Icc 1 n, partitionNumber i).primeFactors) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1106.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1106.lean#L42).

## `Erdos1106.erdos_1106.parts.ii`

Open: stated without proof.

> Let $p(n)$ be the partition number of $n$ and $F(n)$ be the number of distinct prime factors of
> $\prod_{i= 1} ^ {n} p(n)$, $F(n)>n$ for sufficiently large $n$.

```lean
theorem erdos_1106.parts.ii :
    ∀ᶠ n in atTop, #(∏ i ∈ Icc 1 n, partitionNumber i).primeFactors > n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1106.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1106.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1106.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1106.lean)
- [erdosproblems.com/1106](https://www.erdosproblems.com/1106)
