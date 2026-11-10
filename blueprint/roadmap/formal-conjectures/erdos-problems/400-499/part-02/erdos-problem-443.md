---
declaration: theorem
origin: cited
lean: Erdos443.erdos_443.parts.i, Erdos443.erdos_443.parts.ii
statement: formalized
---

# Erdős Problem 443

> *References:*
> - [erdosproblems.com/443](https://www.erdosproblems.com/443)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [He25] Hegyvári, Norbert, *An elementary question of Erdős and Graham*.
>   arXiv:2503.24201 (2025).

*Quoted from [FormalConjectures/ErdosProblems/443.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/443.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/443](https://www.erdosproblems.com/443).

The file states 2 research or textbook statements: 2 solved.

## `Erdos443.erdos_443.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos443.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos443.lean).

> Let $m,n\geq 1$. What is
>
> $$\# \{ k(m-k) : 1\leq k\leq m/2\} \cap \{ l(n-l) : 1\leq l\leq n/2\}?$$
>
> Can it be arbitrarily large?
>
> This was solved independently by Hegyvári [He25] and Cambie (unpublished), who show that if
> $m>n$ then the set in question has size
>
> $$\leq m^{O(1/\log\log m)},$$
>
> and that for any integer $s$ there exist infinitely many pairs $(m,n)$ such that the set in
> question has size $s$.

```lean
theorem erdos_443.parts.i :
    ∀ s : ℕ, ∃ m n : ℕ, n < m ∧ s ≤ (A n ∩ A m).card
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/443.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/443.lean#L53).

## `Erdos443.erdos_443.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos443.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos443.lean).

> Let $m,n\geq 1$. What is
>
> $$\# \{ k(m-k) : 1\leq k\leq m/2\} \cap \{ l(n-l) : 1\leq l\leq n/2\}?$$
>
> Is it $\leq (mn)^{o(1)}$ for all sufficiently large $m,n$?
>
> This was solved independently by Hegyvári [He25] and Cambie (unpublished), who show that if
> $m>n$ then the set in question has size
>
> $$\leq m^{O(1/\log\log m)},$$
>
> and that for any integer $s$ there exist infinitely many pairs $(m,n)$ such that the set in
> question has size $s$.

```lean
theorem erdos_443.parts.ii :
    ∀ ε : ℝ, 0 < ε → ∃ n₀ : ℕ, ∀ m n : ℕ, n₀ < n → n < m →
      ((A n ∩ A m).card : ℝ) < ((m : ℝ) * n) ^ ε
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/443.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/443.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/443.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/443.lean)
- [erdosproblems.com/443](https://www.erdosproblems.com/443)
