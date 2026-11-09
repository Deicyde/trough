---
declaration: theorem
origin: cited
lean: Erdos305.erdos_305, Erdos305.erdos_305.variants.bleicher_erdos, Erdos305.erdos_305.variants.prime_lower_bound, Erdos305.erdos_305.variants.yokota, Erdos305.erdos_305.variants.liu_sawhney
statement: formalized
---

# Erdős Problem 305

> *References:*
> - [erdosproblems.com/305](https://www.erdosproblems.com/305)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [BlEr76] Bleicher, M. N. and Erdős, P., *Denominators of unit fractions*. J. Number Th. (1976),
>   157-168.
> - [Yo88] Yokota, H., *On a problem of Bleicher and Erdős*. J. Number Theory (1988), 198-207.
> - [LiSa24] Liu, Y. and Sawhney, M., *On further questions regarding unit fractions*.
>   arXiv:2404.07113 (2024).

*Quoted from [FormalConjectures/ErdosProblems/305.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/305.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/305](https://www.erdosproblems.com/305).

The file states 5 research or textbook statements: 5 solved.

## `Erdos305.erdos_305`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos305.lean#L217](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos305.lean#L217).

> For integers $1\leq a\lt b$ let $D(a,b)$ be the minimal value of $n_k$ such that there exist
> integers $1\leq n_1\lt \cdots \lt n_k$ with
>
> $$\frac{a}{b}=\frac{1}{n_1}+\cdots+\frac{1}{n_k}.$$
>
> Estimate $D(b)=\max_{1\leq a\lt b}D(a,b)$. Is it true that
>
> $$D(b) \ll b(\log b)^{1+o(1)}?$$
>
> Bleicher and Erdős [BlEr76] have shown that $D(b)\ll b(\log b)^2$. If $b=p$ is a prime then
> $D(p) \gg p\log p$.
>
> This was solved by Yokota [Yo88], who proved that
>
> $$D(b)\ll b(\log b)(\log\log b)^4(\log\log\log b)^2.$$
>
> This was improved by Liu and Sawhney [LiSa24] to
>
> $$D(b)\ll b(\log b)(\log\log b)^3(\log\log\log b)^{O(1)}.$$

```lean
theorem erdos_305 : ∃ δ : ℕ → ℝ, Tendsto δ atTop (nhds 0) ∧
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ b : ℕ in atTop,
      (Dmax b : ℝ) ≤ C * b * (log b) ^ (1 + δ b)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/305.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/305.lean#L69).

## `Erdos305.erdos_305.variants.bleicher_erdos`

Solved: stated here without proof.

> Bleicher and Erdős [BlEr76] have shown that $D(b)\ll b(\log b)^2$.

```lean
theorem erdos_305.variants.bleicher_erdos : ∃ C : ℝ, 0 < C ∧
    ∀ᶠ b : ℕ in atTop, (Dmax b : ℝ) ≤ C * b * (log b) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/305.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/305.lean#L76).

## `Erdos305.erdos_305.variants.prime_lower_bound`

Solved: stated here without proof.

> If $b=p$ is a prime then $D(p) \gg p\log p$.

```lean
theorem erdos_305.variants.prime_lower_bound : ∃ c : ℝ, 0 < c ∧
    ∀ᶠ p : ℕ in atTop, p.Prime → c * p * log p ≤ Dmax p
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/305.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/305.lean#L82).

## `Erdos305.erdos_305.variants.yokota`

Solved: stated here without proof.

> Yokota [Yo88] proved that $D(b)\ll b(\log b)(\log\log b)^4(\log\log\log b)^2$.

```lean
theorem erdos_305.variants.yokota : ∃ C : ℝ, 0 < C ∧ ∀ᶠ b : ℕ in atTop,
    (Dmax b : ℝ) ≤ C * b * log b * log (log b) ^ 4 * log (log (log b)) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/305.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/305.lean#L90).

## `Erdos305.erdos_305.variants.liu_sawhney`

Solved: stated here without proof.

> Liu and Sawhney [LiSa24] proved that $D(b)\ll b(\log b)(\log\log b)^3(\log\log\log b)^{O(1)}$.

```lean
theorem erdos_305.variants.liu_sawhney : ∃ C K : ℝ, 0 < C ∧ ∀ᶠ b : ℕ in atTop,
    (Dmax b : ℝ) ≤ C * b * log b * log (log b) ^ 3 * log (log (log b)) ^ K
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/305.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/305.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/305.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/305.lean)
- [erdosproblems.com/305](https://www.erdosproblems.com/305)
