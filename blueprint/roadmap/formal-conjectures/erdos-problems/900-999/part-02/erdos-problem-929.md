---
declaration: theorem
origin: cited
lean: Erdos929.erdos_929.parts.i, Erdos929.erdos_929.parts.ii, Erdos929.erdos_929.variants.rosser, Erdos929.erdos_929.variants.trivial_upper
statement: formalized
---

# Erdős Problem 929

> *References:*
> - [erdosproblems.com/929](https://www.erdosproblems.com/929)
> - [Er76d] Erdős, P., *Problems and results on number theoretic properties of consecutive integers
>   and related questions*. Proceedings of the Fifth Manitoba Conference on Numerical Mathematics
>   (Univ. Manitoba, Winnipeg, Man., 1975) (1976), 25-44.
>   [PDF](https://www.renyi.hu/~p_erdos/1976-39.pdf)

*Quoted from [FormalConjectures/ErdosProblems/929.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/929.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/929](https://www.erdosproblems.com/929).

The file states 4 research or textbook statements: 2 open, 1 solved and 1 textbook result. It also has 1 API statement, counted here but not shown.

## `Erdos929.erdos_929.parts.i`

Open: stated without proof.

> Let $k\geq 2$ be large and let $S(k)$ be the minimal $x$ such that there is a positive density set
> of $n$ where
>
> $$n+1,n+2,\ldots,n+k$$
>
> are all divisible by primes $\leq x$.
>
> Estimate $S(k)$ - in particular, is it true that $S(k)\geq k^{1-o(1)}$?
>
> A problem of Erdős [Er76d, p. 26]. This is the first part. We read "estimate" as
> $S(k) = \Theta(\text{answer})$ as $k \to \infty$.

```lean
theorem erdos_929.parts.i : (fun k ↦ (S k : ℝ)) =Θ[atTop] erdos_929.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/929.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/929.lean#L74).

## `Erdos929.erdos_929.parts.ii`

Open: stated without proof.

> Let $k\geq 2$ be large and let $S(k)$ be the minimal $x$ such that there is a positive density set
> of $n$ where
>
> $$n+1,n+2,\ldots,n+k$$
>
> are all divisible by primes $\leq x$.
>
> Estimate $S(k)$ - in particular, is it true that $S(k)\geq k^{1-o(1)}$?
>
> This is the second part. We read $o(1)$ as an arbitrary $\varepsilon > 0$ for all large $k$.

```lean
theorem erdos_929.parts.ii :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ k : ℕ in atTop, (k : ℝ) ^ (1 - ε) ≤ (S k : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/929.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/929.lean#L88).

## `Erdos929.erdos_929.variants.rosser`

Solved: stated here without proof.

> It follows from Rosser's sieve that $S(k)> k^{1/2-o(1)}$.
>
> Erdős [Er76d, p. 26] states this for the index $\ell$ with $p_\ell = S(k)$. Since
> $S(k) = p_\ell \geq \ell$, the bound transfers to $S(k)$. The $o(1)$ is stated with an arbitrary
> $\varepsilon > 0$.

```lean
theorem erdos_929.variants.rosser :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ k : ℕ in atTop, (k : ℝ) ^ ((1 : ℝ) / 2 - ε) ≤ (S k : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/929.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/929.lean#L100).

## `Erdos929.erdos_929.variants.trivial_upper`

Textbook result, stated without proof.

> It is trivial that $S(k)\leq k+1$ since, for example, one can take $n\equiv 1\pmod{(k+1)!}$.

```lean
theorem erdos_929.variants.trivial_upper (k : ℕ) : S k ≤ k + 1
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/929.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/929.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/929.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/929.lean)
- [erdosproblems.com/929](https://www.erdosproblems.com/929)
