---
declaration: theorem
origin: cited
lean: Erdos309.erdos_309, Erdos309.erdos_309.variants.asymptotic
statement: formalized
---

# Erdős Problem 309

> *References:*
> - [erdosproblems.com/309](https://www.erdosproblems.com/309)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Yo97] Yokota, Hisashi, *On number of integers representable as a sum of unit fractions. II*.
>   J. Number Theory (1997), 162--169.
> - [Cr99] Croot, III, Ernest S., *On some questions of Erdős and Graham about Egyptian fractions*.
>   Mathematika (1999), 359-372.
> - [Yo02] Yokota, Hisashi, *On the number of integers representable as sums of unit fractions.
>   III*. J. Number Theory (2002), 351--372.

*Quoted from [FormalConjectures/ErdosProblems/309.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/309.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/309](https://www.erdosproblems.com/309).

The file states 2 research or textbook statements: 2 solved.

## `Erdos309.erdos_309`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos309.lean#L374](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos309.lean#L374).

> Let $N\geq 1$. How many integers can be written as the sum of distinct unit fractions with
> denominators from $\{1,\ldots,N\}$? Are there $o(\log N)$ such integers?
>
> If the number of such integers is $N(n)$ then it is trivial that $N(n)\leq \log n+O(1)$. Yokota
> [Yo97] proved that $N(n)\geq \log n-O(\log\log n)$.
>
> Croot [Cr99] proved that every integer at most
> $$\leq \sum_{n\leq N}\frac{1}{n}-(\tfrac{9}{2}+o(1))\frac{(\log\log N)^2}{\log N}$$
> can be so represented.
>
> If $F(N)$ counts the number of integers which can be represented in this fashion, then the
> current best lower bound known is
> $$F(N) \geq \log N+\gamma -\left(\frac{\pi^2}{3}+o(1)\right)\frac{(\log\log N)^2}{\log N}$$
> due to Yokota [Yo02].
>
> The answer to the question is no: $F(N) \sim \log N$. Here $0$ (the empty sum) is counted.

```lean
theorem erdos_309 :
    ¬ (fun N : ℕ => (F N : ℝ)) =o[atTop] fun N : ℕ => Real.log N
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/309.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/309.lean#L67).

## `Erdos309.erdos_309.variants.asymptotic`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos309.lean#L374](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos309.lean#L374).

> The number of representable integers satisfies $F(N) \sim \log N$.

```lean
theorem erdos_309.variants.asymptotic :
    Tendsto (fun N : ℕ => (F N : ℝ) / Real.log N) atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/309.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/309.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/309.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/309.lean)
- [erdosproblems.com/309](https://www.erdosproblems.com/309)
