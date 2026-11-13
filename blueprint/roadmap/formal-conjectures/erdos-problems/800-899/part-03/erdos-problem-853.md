---
declaration: theorem
origin: cited
lean: Erdos853.erdos_853.parts.i, Erdos853.erdos_853.parts.ii
statement: formalized
---

# Erdős Problem 853

> *Reference:* [erdosproblems.com/853](https://www.erdosproblems.com/853)

*Quoted from [FormalConjectures/ErdosProblems/853.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/853.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/853](https://www.erdosproblems.com/853).

The file states 2 research or textbook statements: 2 open.

## `Erdos853.erdos_853.parts.i`

Open: stated without proof.

> Let $d_n = p_{n+1} - p_n$, where $p_n$ is the $n$th prime. Let $r(x)$ be the smallest even
> integer $t$ such that $d_n = t$ has no solutions for $n \le x$.
>
> Is it true that $r(x) \to \infty$?

```lean
theorem erdos_853.parts.i : atTop.Tendsto r atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/853.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/853.lean#L46).

## `Erdos853.erdos_853.parts.ii`

Open: stated without proof.

> Let $d_n = p_{n+1} - p_n$, where $p_n$ is the $n$th prime. Let $r(x)$ be the smallest even
> integer $t$ such that $d_n = t$ has no solutions for $n \le x$.
>
> Is it true that $r(x) / \log x \to \infty$?

```lean
theorem erdos_853.parts.ii :
    atTop.Tendsto (fun n ↦ r n / Real.log n) atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/853.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/853.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/853.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/853.lean)
- [erdosproblems.com/853](https://www.erdosproblems.com/853)
