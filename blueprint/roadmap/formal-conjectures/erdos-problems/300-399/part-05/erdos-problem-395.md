---
declaration: theorem
origin: cited
lean: Erdos395.erdos_395, Erdos395.erdos_395.variants.one, Erdos395.erdos_395.variants.sharp
statement: formalized
---

# Erdős Problem 395

> *References:*
> - [erdosproblems.com/395](https://www.erdosproblems.com/395)
> - [Er45] Erdős, P., *On a lemma of Littlewood and Offord*. Bull. Amer. Math. Soc. (1945),
>   898--902.
> - [CaCa11] Carnielli, Walter and Carolino, Pietro K., *Adjusting a conjecture of Erdős*. Contrib.
>   Discrete Math. (2011), 154--159.
> - [HJNS24] X. He, T. Juškevičius, B. Narayanan, and S. Spiro, *The Reverse Littlewood-Offord
>   problem of Erdős*. arXiv:2408.11034 (2024).

*Quoted from [FormalConjectures/ErdosProblems/395.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/395.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/395](https://www.erdosproblems.com/395).

The file states 3 research or textbook statements: 3 solved.

## `Erdos395.erdos_395`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos395.lean#L4058](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos395.lean#L4058).

> If $z_1,\ldots,z_n\in \mathbb{C}$ with $\lvert z_i\rvert=1$ then is it true that the probability
> that
> $$\lvert \epsilon_1z_1+\cdots+\epsilon_nz_n\rvert \leq \sqrt{2},$$
> where $\epsilon_i\in \{-1,1\}$ uniformly at random, is $\gg 1/n$?
>
> A reverse Littlewood-Offord problem. Erdős originally asked this with $\sqrt{2}$ replaced by $1$,
> but Carnielli and Carolino [CaCa11] observed that this is false, choosing $z_1=1$ and $z_k=i$
> for $2\leq k\leq n$, where $n$ is even, since then the sum is at least $\sqrt{2}$ always.
>
> Solved in the affirmative by He, Juškevičius, Narayanan, and Spiro [HJNS24]. The bound of $1/n$
> is the best possible, as shown by taking $z_k=1$ for $1\leq k\leq n/2$ and $z_k=i$ otherwise.
>
> See also [498](https://www.erdosproblems.com/498).

```lean
theorem erdos_395 : ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 0 < n → ∀ z : Fin n → ℂ,
    (∀ i, ‖z i‖ = 1) → c / n ≤ (signedSumCount z √2 : ℝ) / 2 ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/395.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/395.lean#L60).

## `Erdos395.erdos_395.variants.one`

Solved: stated here without proof.

> Erdős originally asked [erdős_395](https://www.erdosproblems.com/395) with $\sqrt{2}$ replaced by
> $1$, but Carnielli and Carolino [CaCa11] observed that this is false, choosing $z_1=1$ and $z_k=i$
> for $2\leq k\leq n$, where $n$ is even, since then the sum is at least $\sqrt{2}$ always.

```lean
theorem erdos_395.variants.one : ¬ ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 0 < n →
    ∀ z : Fin n → ℂ, (∀ i, ‖z i‖ = 1) → c / n ≤ (signedSumCount z 1 : ℝ) / 2 ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/395.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/395.lean#L70).

## `Erdos395.erdos_395.variants.sharp`

Solved: stated here without proof.

> The bound of $1/n$ in [erdős_395](https://www.erdosproblems.com/395) is the best possible, as
> shown by taking $z_k=1$ for $1\leq k\leq n/2$ and $z_k=i$ otherwise.

```lean
theorem erdos_395.variants.sharp : ∃ C : ℝ, ∀ n : ℕ, 0 < n → ∃ z : Fin n → ℂ,
    (∀ i, ‖z i‖ = 1) ∧ (signedSumCount z √2 : ℝ) / 2 ^ n ≤ C / n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/395.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/395.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/395.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/395.lean)
- [erdosproblems.com/395](https://www.erdosproblems.com/395)
