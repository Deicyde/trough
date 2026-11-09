---
declaration: theorem
origin: cited
lean: Erdos289.erdos_289
statement: formalized
---

# Erdős Problem 289

> *References:*
> - [erdosproblems.com/289](https://www.erdosproblems.com/289)
> - [Ku+26] Kung, P.-N., Song, L., Hwang, D., Yoon, J., Li, C.-L., Severini, S., Olšák, M.,
>   Lockhart, E., Le, Q. V., Gokturk, B., Luong, T., Pfister, T., & Peng, N. (2026). _LEAP:
>   Supercharging LLMs for Formal Mathematics with Agentic Frameworks_.
>   [arXiv:2606.03303](https://arxiv.org/abs/2606.03303).

*Quoted from [FormalConjectures/ErdosProblems/289.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/289.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/289](https://www.erdosproblems.com/289).

The file states 1 research or textbook statement: 1 solved.

## `Erdos289.erdos_289`

Solved: stated here; a Lean proof is at [https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/289.lean#L9514](https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/289.lean#L9514).

> Is it true that, for all sufficiently large $k$, there exist finite intervals
> $I_1, \dotsc, I_k \subset \mathbb{N}$, distinct, not overlapping or adjacent, with
> $|I_i| \geq 2$ for $1 \leq i \leq k$ such that
>
> $$
> 1 = \sum_{i=1}^k \sum_{n \in I_i} \frac{1}{n}?
> $$
>
> Here two intervals are adjacent if their union is again an interval, so any two of the
> $I_i$ must be separated by at least one integer.
>
> This is true: a formal proof in Lean 4 was produced by the LEAP prover agent [Ku+26]
> (see the linked `formal_proof`). We note that other recent solutions were also posted ahead of
> this one (see [erdosproblems.com/forum/thread/289/proof-claims](https://www.erdosproblems.com/forum/thread/289/proof-claims));
> this formalization follows an independent, different proof path.

```lean
theorem erdos_289 :
    (∀ᶠ k : ℕ in atTop, ∃ I : Fin k → ℕ × ℕ,
    (∀ i, (I i).1 < (I i).2) ∧
    (∀ i j, i ≠ j → (I i).2 + 1 < (I j).1 ∨ (I j).2 + 1 < (I i).1) ∧
    ∑ i, ∑ n ∈ .Icc (I i).1 (I i).2, (n⁻¹ : ℚ) = 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/289.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/289.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/289.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/289.lean)
- [erdosproblems.com/289](https://www.erdosproblems.com/289)
