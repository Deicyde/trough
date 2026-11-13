---
declaration: theorem
origin: cited
lean: Erdos821.erdos_821, Erdos821.erdos_821.variants.pillai, Erdos821.erdos_821.variants.erdos, Erdos821.erdos_821.variants.lichtman
statement: formalized
---

# Erdős Problem 821

> *References:*
> - [erdosproblems.com/821](https://www.erdosproblems.com/821)
> - [BaHa98] Baker, R. C. and Harman, G., Shifted primes without large prime factors. Acta Arith.
>   (1998), 331--361.
> - [Er35b] Erdős, P., On the normal number of prime factors of $p-1$ and some related problems
>   concerning Euler's $\varphi$-function. Quart. J. Math. (1935), 205-213.
> - [Er74b] Erdős, P., Remarks on some problems in number theory. Math. Balkanica (1974), 197-202.
> - [Li22] J. D. Lichtman, Primes in arithmetic progressions to large moduli and shifted primes
>   without large prime factors. arXiv:2211.09641 (2022).
> - [LuPo11] Luca, Florian and Pollack, Paul, An arithmetic function arising from {C}armichael's
>   conjecture. J. Théor. Nombres Bordeaux (2011), 697--714.
> - [OpenAI26] OpenAI, *Weighted dilation graphs, smooth shifted primes and totient fibers*.
>   OpenAI Math Release preprint (September 2026).
>   [github.com/openai/math](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf)

*Quoted from [FormalConjectures/ErdosProblems/821.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/821.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/821](https://www.erdosproblems.com/821).

The file states 4 research or textbook statements: 4 solved.

## `Erdos821.erdos_821`

Solved: stated here; a Lean proof is at [https://github.com/cadamcat/totient-fibers-lean4/blob/dfce35707a67fce7362cb2bd95af8b80a0b0373e/Erdos821/Theorem.lean#L18](https://github.com/cadamcat/totient-fibers-lean4/blob/dfce35707a67fce7362cb2bd95af8b80a0b0373e/Erdos821/Theorem.lean#L18).

> Is it true that, for every $\epsilon>0$, there exist infinitely many $n$ such that
> $g(n) > n^{1-\epsilon}$?
>
> This was proved in [OpenAI26]; see the linked formal proof for more explanations.

```lean
theorem erdos_821 :
    ∀ ε > (0 : ℝ), { n : ℕ | (g n : ℝ) > (n : ℝ) ^ (1 - ε) }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/821.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/821.lean#L60).

## `Erdos821.erdos_821.variants.pillai`

Solved: stated here without proof.

> Pillai proved that $\limsup g(n)=\infty$.

```lean
theorem erdos_821.variants.pillai :
    atTop.limsup (fun n : ℕ ↦ (g n : EReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/821.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/821.lean#L68).

## `Erdos821.erdos_821.variants.erdos`

Solved: stated here without proof.

> Erdős [Er35b] proved that there exists some constant $c>0$ such that $g(n) > n^c$ for infinitely
> many $n$.

```lean
theorem erdos_821.variants.erdos :
    ∃ c > (0 : ℝ), { n : ℕ | (n : ℝ) ^ c < (g n : ℝ) }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/821.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/821.lean#L77).

## `Erdos821.erdos_821.variants.lichtman`

Solved: stated here without proof.

> The best known bound is that there are infinitely many $n$ such that $g(n) > n^{0.71568\cdots}$,
> obtained by Lichtman [Li22] as a consequence of proving that there are
> $\geq \frac{x}{(\log x)^{O(1)}}$ many primes $p\leq x$ such that all prime factors of $p-1$ are
> $\leq x^{0.2843\cdots}$ (which improves a number of previous exponents, most recently Baker and
> Harman [BaHa98]).

```lean
theorem erdos_821.variants.lichtman :
    ∃ c > (0.71568 : ℝ), { n : ℕ | (n : ℝ) ^ c < (g n : ℝ) }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/821.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/821.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/821.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/821.lean)
- [erdosproblems.com/821](https://www.erdosproblems.com/821)
