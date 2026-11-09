---
declaration: theorem
origin: cited
lean: Erdos817.erdos_817, Erdos817.erdos_817.variants.bdd_power
statement: formalized
---

# Erdős Problem 817

> *References:*
> - [erdosproblems.com/817](https://www.erdosproblems.com/817)
> - [Co26] Costa, S., *A negative answer to the Erdős–Sárközy question*.
>   [arXiv:2609.06303](https://arxiv.org/abs/2609.06303) (2026).

*Quoted from [FormalConjectures/ErdosProblems/817.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/817.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/817](https://www.erdosproblems.com/817).

The file states 2 research or textbook statements: 2 solved.

## `Erdos817.erdos_817`

Solved: stated here; a Lean proof is at [https://zenodo.org/records/22638810](https://zenodo.org/records/22638810).

> Let $k \geq 3$. Define $g_k(n)$ to be the minimal $N$ such that
> $\{1, ..., N\}$ contains some $A$ of size $|A| = n$ such that
>
> $$
>   \langle A\rangle = \left\{\sum_{a \in A} \epsilon_a a : \epsilon_a \in\{0, 1\}\right\}
> $$
>
> contains no non-trivial $k$-term arithmetic progression. Estimate $g_k(n)$. In
> particular, is it true that
>
> $$
>   g_3(n) \gg 3^n
> $$
>
> The answer is no: Costa [Co26, Corollary 1.2] proved that $\liminf_{n \to \infty} g_3(n)/3^n = 0$.

```lean
theorem erdos_817 :
    ¬ (fun n => (3 ^ n : ℝ)) =O[atTop] fun n => (g 3 n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/817.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/817.lean#L62).

## `Erdos817.erdos_817.variants.bdd_power`

Solved: stated here without proof.

> A problem of Erdős and Sárközy who proved
>
> $$
>   g_3(n) \gg \frac{3^n}{n^{O(1)}}.
> $$

```lean
theorem erdos_817.variants.bdd_power : ∃ O > (0 : ℝ),
    (fun (n : ℕ) => (3 ^ n : ℝ) / n ^ O) =O[atTop] fun n => (g 3 n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/817.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/817.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/817.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/817.lean)
- [erdosproblems.com/817](https://www.erdosproblems.com/817)
