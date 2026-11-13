---
declaration: theorem
origin: cited
lean: OeisA28859.exists_finset_sequence
statement: formalized
---

# Combinatorial representation of the recurrence $a(n+2) = 2a(n+1) + 2a(n)$

> A028859 (OEIS): $a(n+2) = 2 \cdot a(n+1) + 2 \cdot a(n)$; $a(0) = 1$, $a(1) = 3$.
>
> *References:*
> - [A028859](https://oeis.org/A028859)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/28859.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/28859.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA28859.exists_finset_sequence`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/28859.wip.lean#L402](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/28859.wip.lean#L402).

> Conjecture: The sequence a(n) is also the number of compositions of $n$ into positive integers
> such that adjacent parts and the largest part differ by at most 1. - _Gus Wiseman_, May 19 2020
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem exists_finset_sequence (n : ℕ) :
    let L := n + 1
    let Sequence := Fin L → ℕ
    let S : Set Sequence :=
      {σ : Sequence |
        L > 0 ∧
          (∀ i : Fin L, σ i > 0) ∧
            let max_val := Finset.sup Finset.univ σ
            (∀ k : ℕ, 1 ≤ k ∧ k ≤ max_val → ∃ i : Fin L, σ i = k) ∧
            (∀ i j : Fin L, i < j → j.val ≠ i.val + 1 → σ i ≥ σ j)}
    ∃ (F : Finset Sequence), (F : Set Sequence) = S ∧ F.card = a n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/28859.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/28859.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/28859.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/28859.lean)
- [A028859](https://oeis.org/A028859)
