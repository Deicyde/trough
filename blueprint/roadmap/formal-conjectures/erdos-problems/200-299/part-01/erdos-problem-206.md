---
declaration: theorem
origin: cited
lean: Erdos206.erdos_206
statement: formalized
---

# Erdős Problem 206

> *References:*
> - [erdosproblems.com/206](https://www.erdosproblems.com/206)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>   number theory*. Monographies de L'Enseignement Mathématique (1980).
> - [Cu22] Curtiss, D. R., *On Kellogg's Diophantine Problem*. Amer. Math. Monthly (1922),
>   380-387.
> - [Er50b] Erdős, Pál, *On a Diophantine equation*. Mat. Lapok (1950), 192-210.
> - [Na23] Nathanson, M., *Underapproximation by Egyptian fractions*. J. Number Theory (2023),
>   208-234.
> - [Ch23b] Chu, H. V., *A threshold for the best two-term underapproximation by Egyptian
>   fractions*. arXiv:2306.12564 (2023).
> - [Ko24b] Kovač, V., *On eventually greedy best underapproximations by Egyptian fractions*.
>   arXiv:2406.07218 (2024).

*Quoted from [FormalConjectures/ErdosProblems/206.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/206.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/206](https://www.erdosproblems.com/206).

The file states 1 research or textbook statement: 1 solved.

## `Erdos206.erdos_206`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos206.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos206.lean).

> Let $x>0$ be a real number. For any $n\geq 1$ let
> $$R_n(x) = \sum_{i=1}^n\frac{1}{m_i}\lt x$$
> be the maximal sum of $n$ distinct unit fractions which is $\lt x$.
>
> Is it true that, for almost all $x$, for sufficiently large $n$, we have
> $$R_{n+1}(x)=R_n(x)+\frac{1}{m},$$
> where $m$ is minimal such that $m$ does not appear in $R_n(x)$ and the right-hand side is
> $\lt x$? (That is, are the best underapproximations eventually always constructed in a 'greedy'
> fashion?)
>
> Kovač [Ko24b] has proved that this is false - in fact as false as possible: the set of
> $x\in (0,\infty)$ for which the best underapproximations are eventually 'greedy' has Lebesgue
> measure zero.

```lean
theorem erdos_206 :
    ¬ ∀ᵐ x ∂(volume.restrict (Set.Ioi (0 : ℝ))), EventuallyGreedy x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/206.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/206.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/206.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/206.lean)
- [erdosproblems.com/206](https://www.erdosproblems.com/206)
