---
declaration: theorem
origin: cited
lean: Erdos764.erdos_764, Erdos764.erdos_764.variants.vaughan
statement: formalized
---

# Erdős Problem 764

> *References:*
> - [erdosproblems.com/764](https://www.erdosproblems.com/764)
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Er70c] Erdős, P., *Some problems in additive number theory*. Amer. Math. Monthly (1970),
>   619-621.
> - [Va72] Vaughan, R. C., *On the addition of sequences of integers*. J. Number Theory (1972),
>   1-16.

*Quoted from [FormalConjectures/ErdosProblems/764.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/764.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/764](https://www.erdosproblems.com/764).

The file states 2 research or textbook statements: 2 solved.

## `Erdos764.erdos_764`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos764.lean#L3760](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos764.lean#L3760).

> Let $A\subseteq \mathbb{N}$. Can there exist some constant $c>0$ such that
> $$\sum_{n\leq N} 1_A\ast 1_A\ast 1_A(n) = cN+O(1)?$$
>
> The case of $1_A\ast 1_A(n)$ is the subject of [763](https://www.erdosproblems.com/763).
>
> The answer is no, proved in a strong form by Vaughan [Va72], who showed that in fact
> $$\sum_{n\leq N} 1_A\ast 1_A\ast 1_A(n) = cN+o\left(\frac{N^{1/4}}{(\log N)^{1/2}}\right)$$
> is impossible. Vaughan proves a more general result that applies to any $h$-fold convolution,
> with different main terms permitted.

```lean
theorem erdos_764 : ¬ ∃ (A : Set ℕ) (c : ℝ), 0 < c ∧
    (fun N : ℕ ↦ (∑ n ∈ Finset.range (N + 1), tripleRep A n : ℝ) - c * N) =O[atTop]
      fun _ ↦ (1 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/764.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/764.lean#L57).

## `Erdos764.erdos_764.variants.vaughan`

Solved: stated here without proof.

> Vaughan [Va72] showed that
> $\sum_{n\leq N} 1_A\ast 1_A\ast 1_A(n) = cN+o\left(\frac{N^{1/4}}{(\log N)^{1/2}}\right)$ is
> impossible.

```lean
theorem erdos_764.variants.vaughan : ¬ ∃ (A : Set ℕ) (c : ℝ), 0 < c ∧
    (fun N : ℕ ↦ (∑ n ∈ Finset.range (N + 1), tripleRep A n : ℝ) - c * N) =o[atTop]
      fun N ↦ (N : ℝ) ^ (1 / 4 : ℝ) / √(Real.log N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/764.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/764.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/764.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/764.lean)
- [erdosproblems.com/764](https://www.erdosproblems.com/764)
