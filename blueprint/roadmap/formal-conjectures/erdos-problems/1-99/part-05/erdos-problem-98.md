---
declaration: theorem
origin: cited
lean: Erdos98.erdos_98, Erdos98.erdos_98.variants.upper_bound
statement: formalized
---

# Erdős Problem 98

> *References:*
> - [[Er75f](https://mathscinet.ams.org/mathscinet/relay-station?mr=411984)]
>   Erdős, Paul, On some problems of elementary and combinatorial geometry.
>   Ann. Mat. Pura Appl. (4) (1975), 99-108.
> - [[Er83c](https://mathscinet.ams.org/mathscinet/relay-station?mr=706025)]
>   Erdős, Paul, Combinatorial problems in geometry.
>   Math. Chronicle (1983), 35-54.
> - [[Er87b](https://mathscinet.ams.org/mathscinet/relay-station?mr=910710)]
>   Erdős, P., Some combinatorial and metric problems in geometry.
>   Intuitive geometry (Siófok, 1985) (1987), 167-177.
> - [[Er90](https://mathscinet.ams.org/mathscinet/relay-station?mr=1117038)]
>   Erdős, Paul, Some of my favourite unsolved problems.
>   A tribute to Paul Erdős (1990), 467-478.
> - [[Er92b](https://mathscinet.ams.org/mathscinet/relay-station?mr=1275857)]
>   Erdős, Paul, Some of my favourite problems in various branches of combinatorics.
>   Matematiche (Catania) (1992), 231-240.
> - [[EFPR93](https://mathscinet.ams.org/mathscinet/relay-station?mr=1210096)]
>   Erdős, Paul and Füredi, Zoltán and Pach, János and Ruzsa, Imre Z.,
>   The grid revisited. Discrete Math. (1993), 189-196.
> - [[Er94b](https://mathscinet.ams.org/mathscinet/relay-station?mr=1304854)]
>   Erdős, Paul, Some problems in number theory, combinatorics and combinatorial geometry.
>   Math. Pannon. (1994), 261-269.
> - [[Er97e](https://mathscinet.ams.org/mathscinet/relay-station?mr=1487304)]
>   Erdős, Paul, Some of my favourite unsolved problems.
>   Math. Japon. (1997), 527-537.
> - [erdosproblems.com/98](https://www.erdosproblems.com/98)

*Quoted from [FormalConjectures/ErdosProblems/98.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/98.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/98](https://www.erdosproblems.com/98).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos98.erdos_98`

Open: stated without proof.

> Let $h(n)$ be such that any $n$ points in $\mathbb{R}^2$, with no three on a line
> and no four on a circle, determine at least $h(n)$ distinct distances. Does
> $h(n)/n\to \infty$?

```lean
theorem erdos_98 :
    Tendsto (fun n : ℕ ↦ ((h n : ℝ) / (n : ℝ))) atTop atTop
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/98.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/98.lean#L70).

## `Erdos98.erdos_98.variants.upper_bound`

Solved: stated here without proof.

> Erdős could not even prove $h(n)\geq n$. Pach has shown $h(n) < n^{\log_2 3}$.
> Erdős, Füredi, and Pach [EFPR93] have improved this to
> $h(n) < n\exp(c\sqrt{\log n})$ for some constant $c>0$.

```lean
theorem erdos_98.variants.upper_bound :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (h n : ℝ) < (n : ℝ) * Real.exp (c * Real.sqrt (Real.log (n : ℝ)))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/98.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/98.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/98.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/98.lean)
- [erdosproblems.com/98](https://www.erdosproblems.com/98)
