---
declaration: theorem
origin: cited
lean: Erdos310.erdos_310, Erdos310.erdos_310.variants.liu_sawhney
statement: formalized
---

# Erdős Problem 310

> *References:*
> - [erdosproblems.com/310](https://www.erdosproblems.com/310)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [LiSa24] Liu, Y. and Sawhney, M., *On further questions regarding unit fractions*.
>   arXiv:2404.07113 (2024).
> - [Bl21] Bloom, T. F., *On a density conjecture about unit fractions*. arXiv:2112.03726 (2021).

*Quoted from [FormalConjectures/ErdosProblems/310.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/310.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/310](https://www.erdosproblems.com/310).

The file states 2 research or textbook statements: 2 solved.

## `Erdos310.erdos_310`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos310.lean#L240](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos310.lean#L240).

> Let $\alpha >0$ and $N\geq 1$. Is it true that for any $A\subseteq \{1,\ldots,N\}$ with
> $\lvert A\rvert \geq \alpha N$ there exists some $S\subseteq A$ such that
> $$\frac{a}{b}=\sum_{n\in S}\frac{1}{n}$$
> with $a\leq b =O_\alpha(1)$?
>
> Liu and Sawhney [LiSa24] observed that the main result of Bloom [Bl21] implies a positive
> solution to this conjecture. They prove a more precise version, that if
> $(\log N)^{-1/7+o(1)}\leq \alpha \leq 1/2$ then there is some $S\subseteq A$ such that
> $\frac{a}{b}=\sum_{n\in S}\frac{1}{n}$ with $a\leq b \leq \exp(O(1/\alpha))$. They also observe
> that the dependence $b\leq \exp(O(1/\alpha))$ is sharp.

```lean
theorem erdos_310 : ∀ α : ℝ, 0 < α → ∃ C : ℕ, ∀ N : ℕ, 1 ≤ N →
    ∀ A ⊆ Finset.Icc 1 N, α * N ≤ A.card →
      ∃ S ⊆ A, ∃ a b : ℕ, 0 < a ∧ a ≤ b ∧ b ≤ C ∧ ∑ n ∈ S, (1 / n : ℚ) = a / b
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/310.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/310.lean#L51).

## `Erdos310.erdos_310.variants.liu_sawhney`

Solved: stated here without proof.

> Liu and Sawhney [LiSa24] proved that if $(\log N)^{-1/7+o(1)}\leq \alpha \leq 1/2$ then there is
> some $S\subseteq A$ such that $\frac{a}{b}=\sum_{n\in S}\frac{1}{n}$ with
> $a\leq b \leq \exp(O(1/\alpha))$.

```lean
theorem erdos_310.variants.liu_sawhney : ∃ C : ℝ, ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in Filter.atTop,
    ∀ α : ℝ, Real.log N ^ (-(1 / 7 : ℝ) + ε) ≤ α → α ≤ 1 / 2 →
      ∀ A ⊆ Finset.Icc 1 N, α * N ≤ A.card →
        ∃ S ⊆ A, ∃ a b : ℕ, 0 < a ∧ a ≤ b ∧ (b : ℝ) ≤ Real.exp (C / α) ∧
          ∑ n ∈ S, (1 / n : ℚ) = a / b
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/310.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/310.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/310.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/310.lean)
- [erdosproblems.com/310](https://www.erdosproblems.com/310)
