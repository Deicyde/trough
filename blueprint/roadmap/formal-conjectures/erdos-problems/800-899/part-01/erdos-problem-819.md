---
declaration: theorem
origin: cited
lean: Erdos819.erdos_819, Erdos819.erdos_819.variants.erdos_freud_lower, Erdos819.erdos_819.variants.erdos_freud_upper
statement: formalized
---

# Erdős Problem 819

> *References:*
> - [erdosproblems.com/819](https://www.erdosproblems.com/819)
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [ErFr91] Erdős, P. and Freud, R., *On sums of a Sidon-sequence*. J. Number Theory 38 (1991),
>   196-205.

*Quoted from [FormalConjectures/ErdosProblems/819.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/819.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/819](https://www.erdosproblems.com/819).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 3 API statements, counted here but not shown.

## `Erdos819.erdos_819`

Open: stated without proof.

> Let $f(N)$ be maximal such that there exists $A\subseteq \{1,\ldots,N\}$ with
> $\lvert A\rvert=\lfloor N^{1/2}\rfloor$ such that $\lvert (A+A)\cap [1,N]\rvert=f(N)$.
> Estimate $f(N)$.

```lean
theorem erdos_819 : (fun N ↦ (f N : ℝ)) ~[atTop] erdos_819.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/819.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/819.lean#L89).

## `Erdos819.erdos_819.variants.erdos_freud_lower`

Solved: stated here without proof.

> Erdős and Freud [ErFr91] proved
>
> $$\left(\frac{3}{8}-o(1)\right)N \leq f(N) \leq \left(\frac{1}{2}+o(1)\right)N.$$
>
> This is the lower bound.

```lean
theorem erdos_819.variants.erdos_freud_lower :
    ∀ ε > (0 : ℝ), ∀ᶠ N : ℕ in atTop, (3 / 8 - ε) * N ≤ (f N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/819.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/819.lean#L99).

## `Erdos819.erdos_819.variants.erdos_freud_upper`

Proved here.

> Erdős and Freud [ErFr91] proved
>
> $$\left(\frac{3}{8}-o(1)\right)N \leq f(N) \leq \left(\frac{1}{2}+o(1)\right)N.$$
>
> This is the upper bound.

```lean
theorem erdos_819.variants.erdos_freud_upper :
    ∀ ε > (0 : ℝ), ∀ᶠ N : ℕ in atTop, (f N : ℝ) ≤ (1 / 2 + ε) * N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/819.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/819.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/819.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/819.lean)
- [erdosproblems.com/819](https://www.erdosproblems.com/819)
