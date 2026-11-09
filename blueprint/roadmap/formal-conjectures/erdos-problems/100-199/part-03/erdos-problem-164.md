---
declaration: theorem
origin: cited
lean: Erdos164.erdos_164
statement: formalized
---

# Erdős Problem 164

> *References:*
> - [erdosproblems.com/164](https://www.erdosproblems.com/164)
> - [Er76g] Erdős, P., *Problems and results on combinatorial number theory. II*. J. Indian Math. Soc.
>   (N.S.) (1976), 285-298.
> - [Er86] Erdős, P., *Problémes et résultats en théorie des nombres*. (1986).
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference "Paul
>   Erdős and his mathematics", Budapest, July 1999 (1999).
> - [ABLLPSTT26] B. Alexeev, K. Barreto, Y. Li, J. D. Lichtman, L. Price, J. I. Shah, Q. Tang, and
>   T. Tao, *Primitive sets and Von Mangoldt Chains: Erdős problem #1196 and beyond*.
>   arXiv:2605.00301 (2026).
> - [Er35] Erdős, Paul, *Note on Sequences of Integers No One of Which is Divisible By Any Other*.
>   J. London Math. Soc. (1935), 126-128.
> - [Li23] Lichtman, J. D., *A proof of the Erdős primitive set conjecture*. arXiv:2202.02384 (2023).

*Quoted from [FormalConjectures/ErdosProblems/164.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/164.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/164](https://www.erdosproblems.com/164).

The file states 1 research or textbook statement: 1 solved.

## `Erdos164.erdos_164`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos164.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos164.lean).

> A set $A\subset \mathbb{N}$ is primitive if no member of $A$ divides another. Is the sum
>
> $$\sum_{n\in A}\frac{1}{n\log n}$$
>
> maximised over all primitive sets when $A$ is the set of primes?
>
> Erdős [Er35] proved that this sum always converges for a primitive set. Lichtman [Li23] proved
> that the answer is yes. An alternative, simpler, proof is given by Alexeev, Barreto, Li, Lichtman,
> Price, Shah, Tang, and Tao [ABLLPSTT26].

```lean
theorem erdos_164 :
    ∀ A : Set ℕ, (∀ a ∈ A, 2 ≤ a) → Erdos1196.IsPrimitive A →
      (∑' a : A, 1 / ((a : ℕ) * Real.log (a : ℕ))) ≤
        ∑' p : {p : ℕ | p.Prime}, 1 / ((p : ℕ) * Real.log (p : ℕ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/164.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/164.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/164.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/164.lean)
- [erdosproblems.com/164](https://www.erdosproblems.com/164)
