---
declaration: theorem
origin: cited
lean: Erdos275.erdos_275
statement: formalized
---

# Erdős Problem 275

> *References:*
> - [erdosproblems.com/275](https://www.erdosproblems.com/275)
> - [CrVE70] R.B. Crittenden and C.L. Vanden Eynden, *Any n arithmetic progressions covering the first
>   2^n integers cover all integers*, Proc. Amer. Math. Soc. 24 (1970), 475-481.

*Quoted from [FormalConjectures/ErdosProblems/275.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/275.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/275](https://www.erdosproblems.com/275).

The file states 1 research or textbook statement: 1 solved.

## `Erdos275.erdos_275`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos275.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos275.lean).

> If a finite system of $r$ congruences $\{ a_i\pmod{n_i} : 1\leq i\leq r\}$ (the $n_i$ are not
> necessarily distinct) covers $2^r$ consecutive integers then it covers all integers.
>
> This is best possible as the system $2^{i-1}\pmod{2^i}$ shows. This was proved independently by
> Selfridge and Crittenden and Vanden Eynden [CrVE70].
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_275 (r : ℕ) (a : Fin r → ℤ) (n : Fin r → ℕ)
    (H : ∃ k : ℤ, ∀ x ∈ Ico k (k + 2 ^ r), ∃ i, x ≡ a i [ZMOD n i]) (x : ℤ) :
    ∃ i, x ≡ a i [ZMOD n i]
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/275.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/275.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/275.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/275.lean)
- [erdosproblems.com/275](https://www.erdosproblems.com/275)
