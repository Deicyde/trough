---
declaration: theorem
origin: cited
lean: Erdos824.erdos_824, Erdos824.erdos_824.variants.pollack_pomerance, Erdos824.erdos_824.variants.squarefree
statement: formalized
---

# Erdős Problem 824

> *References:*
> - [erdosproblems.com/824](https://www.erdosproblems.com/824)
> - [Er59c] Erdős, P., *Remarks on number theory. II. Some problems on the $\sigma$ function*.
>   Acta Arith. (1959), 171--177.
> - [Er74b] Erdős, P., *Remarks on some problems in number theory*. Math. Balkanica (1974),
>   197-202.
> - [PoPo16] Pollack, Paul and Pomerance, Carl, *Some problems of Erdős on the sum-of-divisors
>   function*. Trans. Amer. Math. Soc. Ser. B (2016), 1-26.
> - [LiZh26] Li, Shisheng and Zhuang, Zhong, *Coprime pairs with equal sum of divisors, assuming
>   smooth shifted primes*. Preprint (October 2026).
>   [github.com/daizisheng/erdos-824](https://github.com/daizisheng/erdos-824/blob/b4b7099bb8ab9c1c7fc61dae18a73cdbe503fe5a/paper/erdos824.pdf)
> - [OpenAI26] OpenAI, *Weighted dilation graphs, smooth shifted primes and totient fibers*.
>   OpenAI Math Release preprint (September 2026).
>   [github.com/openai/math](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf)

*Quoted from [FormalConjectures/ErdosProblems/824.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/824.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/824](https://www.erdosproblems.com/824).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos824.erdos_824`

Solved: stated here; a Lean proof is at [https://github.com/cadamcat/equal-divisor-sums-lean4/blob/6280393739de142f3c54160ce7083110ed55f194/Erdos824/Theorem.lean#L17](https://github.com/cadamcat/equal-divisor-sums-lean4/blob/6280393739de142f3c54160ce7083110ed55f194/Erdos824/Theorem.lean#L17).

> Let $h(x)$ count the number of integers $1\leq a\lt b\lt x$ such that $(a,b)=1$ and
> $\sigma(a)=\sigma(b)$, where $\sigma$ is the sum of divisors function. Is it true that
> $h(x)>x^{2-o(1)}$?
>
> That is, is it true that for every $\epsilon > 0$ we have $h(x) > x^{2-\epsilon}$ for all large
> $x$? According to erdosproblems.com, Erdős [Er74b] proved that $\limsup h(x)/x = \infty$ and
> claimed a similar proof for this problem.

```lean
theorem erdos_824 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ x : ℕ in atTop, (x : ℝ) ^ (2 - ε) < (h x : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/824.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/824.lean#L73).

## `Erdos824.erdos_824.variants.pollack_pomerance`

Solved: stated here without proof.

> Pollack and Pomerance [PoPo16, Section 6] proved that $h(x)/x \to \infty$, answering a question
> of Erdős [Er59c].

```lean
theorem erdos_824.variants.pollack_pomerance :
    Tendsto (fun x : ℕ ↦ (h x : ℝ) / (x : ℝ)) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/824.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/824.lean#L82).

## `Erdos824.erdos_824.variants.squarefree`

Open: stated without proof.

> A similar question can be asked if the condition $(a,b)=1$ is replaced by the condition that $a$
> and $b$ are squarefree. Let $h'(x)$ count the number of squarefree integers $1\leq a\lt b\lt x$ with
> $\sigma(a)=\sigma(b)$. Is it true that $h'(x)>x^{2-o(1)}$?

```lean
theorem erdos_824.variants.squarefree :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ x : ℕ in atTop, (x : ℝ) ^ (2 - ε) < (hSquarefree x : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/824.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/824.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/824.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/824.lean)
- [erdosproblems.com/824](https://www.erdosproblems.com/824)
