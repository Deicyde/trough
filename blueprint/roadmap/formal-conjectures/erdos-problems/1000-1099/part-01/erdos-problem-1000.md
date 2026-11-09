---
declaration: theorem
origin: cited
lean: Erdos1000.erdos_1000, Erdos1000.erdos_1000.variants.totient_le, Erdos1000.erdos_1000.variants.liminf_eq_zero, Erdos1000.erdos_1000.variants.not_tendsto_zero, Erdos1000.erdos_1000.variants.limsup_eq_one
statement: formalized
---

# Erdős Problem 1000

> *References:*
> - [erdosproblems.com/1000](https://www.erdosproblems.com/1000)
> - [Ca50b] Cassels, J. W. S., *Some metrical theorems in Diophantine approximation. I*. Proc.
>   Cambridge Philos. Soc. (1950), 209-218.
> - [Er64b] Erdős, P., *Problems and results on diophantine approximations*. Compositio Math. (1964),
>   52-65.
> - [Ha] Haight, J. A., *Metric Diophantine approximation and related topics*. PhD thesis.

*Quoted from [FormalConjectures/ErdosProblems/1000.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1000.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1000](https://www.erdosproblems.com/1000).

The file states 5 research or textbook statements: 5 solved.

## `Erdos1000.erdos_1000`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1000.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1000.lean).

> Let $A=\{n_1\lt n_2\lt \cdots\}$ be an infinite sequence of positive integers, and let $\phi_A(k)$
> count the number of $1\leq m\leq n_k$ such that the fraction $\frac{m}{n_k}$ cannot be written
> as $\frac{b}{n_j}$ for any integer $b$ and any $j\lt k$; equivalently,
>
> $$
> \frac{n_k}{(m,n_k)}\nmid n_j
> $$
>
> for all $1\leq j\lt k$.
>
> Is there a sequence $A$ such that
>
> $$
> \lim_{N\to \infty}\frac{1}{N}\sum_{k\leq N}\frac{\phi_A(k)}{n_k}=0?
> $$
>
> This was solved by Haight [Ha] who proved that such a sequence does exist (contrary to Erdős'
> expectations).

```lean
theorem erdos_1000 :
    ∃ n : ℕ → ℕ, StrictMono n ∧ 0 < n 0 ∧
      Tendsto (phiAvg n) atTop (𝓝 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1000.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1000.lean#L75).

## `Erdos1000.erdos_1000.variants.totient_le`

Proved here.

> It is trivial that $\phi_A(k)\geq \phi(n_k)$, where $\phi$ is the Euler totient function.

```lean
theorem erdos_1000.variants.totient_le (n : ℕ → ℕ) (hn : StrictMono n) (hn0 : 0 < n 0)
    (k : ℕ) :
    (n k).totient ≤ phiSeq n k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1000.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1000.lean#L84).

## `Erdos1000.erdos_1000.variants.liminf_eq_zero`

Solved: stated here without proof.

> The study of $\phi_A$ was introduced by Cassels [Ca50b], who proved that there exist sequences
> such that
>
> $$
> \liminf_{N\to \infty}\frac{1}{N}\sum_{k\leq N}\frac{\phi_A(k)}{n_k}=0.
> $$

```lean
theorem erdos_1000.variants.liminf_eq_zero :
    ∃ n : ℕ → ℕ, StrictMono n ∧ 0 < n 0 ∧
      atTop.liminf (phiAvg n) = 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1000.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1000.lean#L131).

## `Erdos1000.erdos_1000.variants.not_tendsto_zero`

Solved: stated here without proof.

> Erdős [Er64b] proved that the limit of $\frac{\phi_A(k)}{n_k}$ as $k\to \infty$ cannot be $0$.

```lean
theorem erdos_1000.variants.not_tendsto_zero (n : ℕ → ℕ) (hn : StrictMono n) (hn0 : 0 < n 0) :
    ¬ Tendsto (fun k : ℕ => (phiSeq n k : ℝ) / (n k : ℝ)) atTop (𝓝 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1000.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1000.lean#L140).

## `Erdos1000.erdos_1000.variants.limsup_eq_one`

Solved: stated here without proof.

> In fact he proved that if $\liminf \frac{\phi_A(k)}{n_k}=0$ then
> $\limsup \frac{\phi_A(k)}{n_k}=1$.

```lean
theorem erdos_1000.variants.limsup_eq_one (n : ℕ → ℕ) (hn : StrictMono n) (hn0 : 0 < n 0)
    (h : atTop.liminf (fun k : ℕ => (phiSeq n k : ℝ) / (n k : ℝ)) = 0) :
    atTop.limsup (fun k : ℕ => (phiSeq n k : ℝ) / (n k : ℝ)) = 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1000.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1000.lean#L149).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1000.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1000.lean)
- [erdosproblems.com/1000](https://www.erdosproblems.com/1000)
