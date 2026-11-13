---
declaration: theorem
origin: cited
lean: Erdos689.erdos_689
statement: formalized
---

# Erdős Problem 689

> *References:*
> - [erdosproblems.com/689](https://www.erdosproblems.com/689)
> - [Ben Green's Open Problem 45](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.45)
> - [Ch26] Chojecki, P., *A greedy matching proof of Erdős's two-fold residue-class problem*.
>   [ulam.ai/research/erdos689.pdf](https://www.ulam.ai/research/erdos689.pdf) (April 2026).
> - [PALOMAR-2026-09-20-000002](https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-20-000002&version=1)

*Quoted from [FormalConjectures/ErdosProblems/689.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/689.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/689](https://www.erdosproblems.com/689).

The file states 1 research or textbook statement: 1 solved.

## `Erdos689.erdos_689`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/54f272582dd71321ab9d458663d675edd3d0a463/erdos-689/Solution.lean#L18](https://github.com/linrock/math-proofs/blob/54f272582dd71321ab9d458663d675edd3d0a463/erdos-689/Solution.lean#L18).

> Let `n` be sufficiently large. Is there some choice of congruence class `a_p` for all primes
> `2 ≤ p ≤ n` such that every integer in `[1,n]` satisfies at least two of the congruences
> `≡ a_p (mod p)`?
>
> Yes: this follows from the greedy-matching reduction of Chojecki [Ch26] combined with an
> unconditional Fourier-analytic proof of the required three-prime counting estimate.

```lean
theorem erdos_689 :
    ∀ᶠ n in .atTop, ∃ a : ℕ → ℕ, ∀ m ∈ Finset.Icc 1 n,
      2 ≤ (Finset.Icc 1 n |>.filter fun p => p.Prime ∧ a p ≡ m [MOD p]).card
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/689.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/689.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/689.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/689.lean)
- [erdosproblems.com/689](https://www.erdosproblems.com/689)
