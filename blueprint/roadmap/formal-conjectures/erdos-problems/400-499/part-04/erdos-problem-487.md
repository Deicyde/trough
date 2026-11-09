---
declaration: theorem
origin: cited
lean: Erdos487.erdos_487
statement: formalized
---

# Erdős Problem 487

> *References:*
> - [erdosproblems.com/487](https://www.erdosproblems.com/487)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [DaEr36] Davenport, H. and Erdős, P., *On sequences of positive integers*. Acta Arithmetica
>   (1936), 147-151.
> - [Kl71] Kleitman, Daniel, *Collections of subsets containing no two sets and their union*.
>   Proceedings of the LA Meeting AMS (1971), 153-155.

*Quoted from [FormalConjectures/ErdosProblems/487.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/487.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/487](https://www.erdosproblems.com/487).

The file states 1 research or textbook statement: 1 solved.

## `Erdos487.erdos_487`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos487.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos487.lean).

> Let $A\subseteq \mathbb{N}$ have positive density. Must there exist distinct $a,b,c\in A$ such
> that $[a,b]=c$ (where $[a,b]$ is the least common multiple of $a$ and $b$)?
>
> This is true, a consequence of the positive solution to [447] by Kleitman [Kl71].
>
> Davenport and Erdős [DaEr36] showed that there must exist an infinite sequence $a_1\lt a_2\cdots$
> in $A$ such that $a_i\mid a_j$ for all $i\leq j$, under the assumption that the upper logarithmic
> density of $A$ is positive.

```lean
theorem erdos_487 :
    ∀ A : Set ℕ, A.HasPosDensity →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A, a ≠ b ∧ b ≠ c ∧ a ≠ c ∧ Nat.lcm a b = c
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/487.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/487.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/487.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/487.lean)
- [erdosproblems.com/487](https://www.erdosproblems.com/487)
