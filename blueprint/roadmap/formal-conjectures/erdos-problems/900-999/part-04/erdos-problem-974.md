---
declaration: theorem
origin: cited
lean: Erdos974.erdos_974, Erdos974.erdos_974.variants.two_tuples
statement: formalized
---

# Erdős Problem 974

> *References:*
> - [erdosproblems.com/974](https://www.erdosproblems.com/974)
> - [Ti66] Tijdeman, R., *On a conjecture of Turán and Erdős*. Indag. Math. (1966), 374-383.

*Quoted from [FormalConjectures/ErdosProblems/974.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/974.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/974](https://www.erdosproblems.com/974).

The file states 2 research or textbook statements: 2 solved.

## `Erdos974.erdos_974`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos974.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos974.lean).

> Let $z_1,\ldots,z_n\in \mathbb{C}$ be a sequence such that $z_1=1$. Suppose that the sequence of
>
> $$s_k=\sum_{1\leq i\leq n}z_i^k$$
>
> contains infinitely many $(n-1)$-tuples of consecutive values of $s_k$ which are all $0$. Then
> (essentially)
>
> $$z_j=e(j/n),$$
>
> where $e(x)=e^{2\pi ix}$.
>
> A conjecture of Turán.
>
> This is true (in the stronger form with only two such tuples) - in fact if $n$ is odd then the
> $z_i$ must be exactly the $n$th roots of unity, and if $n$ is even they must be the vertices of
> two regular $(n/2)$-gons with the same circumscribed circle centred at the origin. This was first
> proved by Tijdeman [Ti66]. An independent proof of this was given in the comments section by Hu,
> Tang, and Zhang.

```lean
theorem erdos_974 {n : ℕ} [NeZero n] (z : Fin n → ℂ) (hz : z 0 = 1)
    (hs : Set.Infinite {k : ℕ | ∀ j < n - 1, ∑ i, z i ^ (k + j) = 0}) :
    IsTuranConfiguration z
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/974.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/974.lean#L61).

## `Erdos974.erdos_974.variants.two_tuples`

Solved: stated here without proof.

> Erdős speculates that this may be true if there are two distinct $(n-1)$-tuples of consecutive
> values of $s_k$ which are $0$. He does not elaborate on what the 'essentially' may mean precisely.
>
> This is true (in the stronger form with only two such tuples) - in fact if $n$ is odd then the
> $z_i$ must be exactly the $n$th roots of unity, and if $n$ is even they must be the vertices of
> two regular $(n/2)$-gons with the same circumscribed circle centred at the origin. This was first
> proved by Tijdeman [Ti66]. An independent proof of this was given in the comments section by Hu,
> Tang, and Zhang.

```lean
theorem erdos_974.variants.two_tuples {n : ℕ} [NeZero n] (z : Fin n → ℂ) (hz : z 0 = 1)
    {a b : ℕ} (hab : a ≠ b) (ha : ∀ j < n - 1, ∑ i, z i ^ (a + j) = 0)
    (hb : ∀ j < n - 1, ∑ i, z i ^ (b + j) = 0) :
    IsTuranConfiguration z
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/974.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/974.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/974.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/974.lean)
- [erdosproblems.com/974](https://www.erdosproblems.com/974)
