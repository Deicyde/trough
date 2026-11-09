---
declaration: theorem
origin: cited
lean: Erdos823.erdos_823, Erdos823.erdos_823.variants.totient
statement: formalized
---

# Erdős Problem 823

> *References:*
> - [erdosproblems.com/823](https://www.erdosproblems.com/823)
> - [Er59c] Erdős, P., *Remarks on number theory. II. Some problems on the $\sigma$ function*.
>   Acta Arith. (1959), 171--177.
> - [Er74b] Erdős, P., *Remarks on some problems in number theory*. Math. Balkanica (1974),
>   197-202.
> - [Po15b] Pollack, Paul, *Remarks on fibers of the sum-of-divisors function*. Analytic number
>   theory, Springer, Cham (2015), 305-320.

*Quoted from [FormalConjectures/ErdosProblems/823.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/823.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/823](https://www.erdosproblems.com/823).

The file states 2 research or textbook statements: 2 solved.

## `Erdos823.erdos_823`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos823.lean#L72](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos823.lean#L72).

> Let $\alpha\geq 1$. Is there a sequence of integers $n_k,m_k$ such that $n_k/m_k\to \alpha$ and
> $\sigma(n_k)=\sigma(m_k)$ for all $k\geq 1$, where $\sigma$ is the sum of divisors function?
>
> The answer is yes, proved by Pollack [Po15b].
>
> We take $n_k$ and $m_k$ to be positive integers.

```lean
theorem erdos_823 : ∀ α : ℝ, 1 ≤ α →
    ∃ n m : ℕ → ℕ, (∀ k, 0 < n k) ∧ (∀ k, 0 < m k) ∧ (∀ k, σ 1 (n k) = σ 1 (m k)) ∧
      Tendsto (fun k ↦ (n k : ℝ) / m k) atTop (𝓝 α)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/823.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/823.lean#L51).

## `Erdos823.erdos_823.variants.totient`

Solved: stated here without proof.

> For every $\alpha\geq 1$ there are sequences of integers $n_k,m_k$ such that $n_k/m_k\to \alpha$
> and $\phi(n_k)=\phi(m_k)$ for all $k\geq 1$. Erdős [Er74b] writes it is 'easy to prove the
> analogous result for $\phi(n)$'.

```lean
theorem erdos_823.variants.totient : ∀ α : ℝ, 1 ≤ α →
    ∃ n m : ℕ → ℕ, (∀ k, 0 < n k) ∧ (∀ k, 0 < m k) ∧ (∀ k, φ (n k) = φ (m k)) ∧
      Tendsto (fun k ↦ (n k : ℝ) / m k) atTop (𝓝 α)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/823.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/823.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/823.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/823.lean)
- [erdosproblems.com/823](https://www.erdosproblems.com/823)
