---
declaration: lemma
origin: cited
lean: Erdos499.erdos_499, Erdos499.vanDerWaerden, Erdos499.erdos_499.variants.one_le
statement: formalized
---

# Erdős Problem 499

> *Reference:* [erdosproblems.com/499](https://www.erdosproblems.com/499)

*Quoted from [FormalConjectures/ErdosProblems/499.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/499.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/499](https://www.erdosproblems.com/499).

The file states 3 research or textbook statements: 3 solved.

## `Erdos499.erdos_499`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos499.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos499.lean).

> Let $M$ be a real $n \times n$ doubly stochastic matrix. Does there exist some $σ \in S_n$ such that
>
> $$
> \prod_{1 \leq i \leq n} M_{i, σ(i)} \geq n^{-n}?
> $$
>
> This is true, and was proved by Marcus and Minc [MaMi62]
>
> [MaMi62] Marcus, Marvin and Minc, Henryk, Some results on doubly stochastic matrices. Proc. Amer. Math. Soc. (1962), 571-579.

```lean
lemma erdos_499 :
    (∀ n, ∀ M ∈ doublyStochastic ℝ (Fin n), ∃ σ : Equiv.Perm (Fin n),
      n ^ (- n : ℤ) ≤ ∏ i, M i (σ i))
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/ErdosProblems/499.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/499.lean#L42).

## `Erdos499.vanDerWaerden`

Solved: stated here without proof.

> The conjecture of van der Waerden, which states that the permanent of a doubly stochastic matrix is
> at least $n^{-n} n!$.
>
> Proved by Gyires [Gy80], Egorychev [Eg81], and Falikman [Fa81].
>
> [Gy80] Gyires, B., The common source of several inequalities concerning doubly stochastic matrices. Publ. Math. Debrecen (1980), 291-304.
> [Eg81] Egorychev, G. P., The solution of the van der Waerden problem for permanents. Dokl. Akad. Nauk SSSR (1981), 1041-1044.
> [Fa81] Falikman, D. I., Proof of the van der Waerden conjecture on the permanent of a doubly stochastic matrix. Mat. Zametki (1981), 931-938, 957.

```lean
lemma vanDerWaerden (n : ℕ) (M : Matrix (Fin n) (Fin n) ℝ) (hM : M ∈ doublyStochastic ℝ (Fin n)) :
    n ^ (- n : ℤ) * n ! ≤ M.permanent
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/ErdosProblems/499.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/499.lean#L58).

## `Erdos499.erdos_499.variants.one_le`

Solved: stated here without proof.

> A weaker version of Erdős' problem 499, which asks whether for every doubly stochastic matrix, there
> exists a permutation $σ \in S_n$ with $M_{i, σ(i)} ≠ 0$ and such that
>
> $$
> \sum_{1 \leq i \leq n} M_{i, σ(i)} \geq 1
> $$
>
> Proved by Marcus and Ree [MaRe59].
>
> [MaRe59] Marcus, M. and Ree, R., Diagonals of doubly stochastic matrices. Quart. J. Math. Oxford Ser. (2) (1959), 296-302.

```lean
lemma erdos_499.variants.one_le :
    ∀ n > 0, ∀ M ∈ doublyStochastic ℝ (Fin n), ∃ σ : Equiv.Perm (Fin n),
      (∀ i, M i (σ i) ≠ 0) ∧ 1 ≤ ∑ i, M i (σ i)
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/ErdosProblems/499.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/499.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/499.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/499.lean)
- [erdosproblems.com/499](https://www.erdosproblems.com/499)
