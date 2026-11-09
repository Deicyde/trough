---
declaration: theorem
origin: cited
lean: Erdos763.erdos_763, Erdos763.erdos_763.variants.erdos_fuchs, Erdos763.erdos_763.variants.montgomery_vaughan
statement: formalized
---

# Erdős Problem 763

> *References:*
> - [erdosproblems.com/763](https://www.erdosproblems.com/763)
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Er70c] Erdős, P., *Some problems in additive number theory*. Amer. Math. Monthly (1970),
>   619-621.
> - [ErFu56] Erdős, P. and Fuchs, W. H. J., *On a problem of additive number theory*. J. London
>   Math. Soc. (1956), 67-73.
> - [MoVa90] Montgomery, H. L. and Vaughan, R. C., *On the Erdős-Fuchs theorems*. (1990), 331-338.

*Quoted from [FormalConjectures/ErdosProblems/763.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/763.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/763](https://www.erdosproblems.com/763).

The file states 3 research or textbook statements: 3 solved.

## `Erdos763.erdos_763`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos763.lean#L1464](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos763.lean#L1464).

> Let $A\subseteq \mathbb{N}$. Can there exist some constant $c>0$ such that
>
> $$\sum_{n\leq N} 1_A\ast 1_A(n) = cN+O(1)?$$
>
> A conjecture of Erdős and Turán. Erdős and Fuchs [ErFu56] proved that the answer is no in a
> strong form: in fact even
>
> $$\sum_{n\leq N} 1_A\ast 1_A(n) = cN+o\left(\frac{N^{1/4}}{(\log N)^{1/2}}\right)$$
>
> is impossible. The error term here was improved to $o(N^{1/4})$ by Jurkat (unpublished) and
> Montgomery and Vaughan [MoVa90].
>
> See also [764](https://www.erdosproblems.com/764) for a generalisation to more summands.

```lean
theorem erdos_763 : ¬ ∃ (A : Set ℕ) (c : ℝ), 0 < c ∧
    (fun N : ℕ ↦ (∑ n ∈ Finset.range (N + 1), sumRep A n : ℝ) - c * N) =O[atTop]
      fun _ ↦ (1 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/763.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/763.lean#L55).

## `Erdos763.erdos_763.variants.erdos_fuchs`

Solved: stated here without proof.

> Erdős and Fuchs [ErFu56] proved that
> $\sum_{n\leq N} 1_A\ast 1_A(n) = cN+o\left(\frac{N^{1/4}}{(\log N)^{1/2}}\right)$ is impossible.

```lean
theorem erdos_763.variants.erdos_fuchs : ¬ ∃ (A : Set ℕ) (c : ℝ), 0 < c ∧
    (fun N : ℕ ↦ (∑ n ∈ Finset.range (N + 1), sumRep A n : ℝ) - c * N) =o[atTop]
      fun N ↦ (N : ℝ) ^ (1 / 4 : ℝ) / √(Real.log N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/763.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/763.lean#L65).

## `Erdos763.erdos_763.variants.montgomery_vaughan`

Solved: stated here without proof.

> Jurkat (unpublished) and Montgomery and Vaughan [MoVa90] proved that even
> $\sum_{n\leq N} 1_A\ast 1_A(n) = cN+o(N^{1/4})$ is impossible.

```lean
theorem erdos_763.variants.montgomery_vaughan : ¬ ∃ (A : Set ℕ) (c : ℝ), 0 < c ∧
    (fun N : ℕ ↦ (∑ n ∈ Finset.range (N + 1), sumRep A n : ℝ) - c * N) =o[atTop]
      fun N ↦ (N : ℝ) ^ (1 / 4 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/763.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/763.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/763.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/763.lean)
- [erdosproblems.com/763](https://www.erdosproblems.com/763)
