---
declaration: theorem
origin: cited
lean: Chvatal.exists_maximal_star
statement: formalized
---

# Chvátal's Conjecture

> *References:*
>
> * [A Conjecture in Extremal Combinatorics](https://users.encs.concordia.ca/~chvatal/conjecture.html)
> * [Chvátal's Conjecture and Correlation Inequalities](https://arxiv.org/abs/1608.08954)
> * [A proof of Chvátal's conjecture via a sharp correlation inequality](https://arxiv.org/abs/2609.19123)

*Quoted from [FormalConjectures/Paper/Chvatal.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Chvatal.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Chvatal.exists_maximal_star`

Solved: stated here; a Lean proof is at [https://github.com/boonsuan/chvatal/blob/c19ed3aaac9e42d446f963a862d39d8a09eddbf9/Solution.lean#L22-L33](https://github.com/boonsuan/chvatal/blob/c19ed3aaac9e42d446f963a862d39d8a09eddbf9/Solution.lean#L22-L33).

> If F is a decreasing family of sets of some finite type α, then there is some element
> x of α such that the family consisting of all members of F containing x is an intersecting
> subfamily of F with maximal cardinality.

```lean
theorem exists_maximal_star :
    ∀ F : Finset (Finset α), Decreasing F →
        ∃ x : α, ∀ G, G ⊆ F → Intersecting G → G.card ≤ { A ∈ F | x ∈ A }.card
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/Chvatal.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Chvatal.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/Chvatal.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Chvatal.lean)
- [A Conjecture in Extremal Combinatorics](https://users.encs.concordia.ca/~chvatal/conjecture.html)
