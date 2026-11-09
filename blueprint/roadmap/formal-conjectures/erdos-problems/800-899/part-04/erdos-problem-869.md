---
declaration: theorem
origin: cited
lean: Erdos869.erdos_869
statement: formalized
---

# Erdős Problem 869

> *References:*
> - [erdosproblems.com/869](https://www.erdosproblems.com/869)
> - [ErNa88] Erdős, Paul and Nathanson, Melvyn B., *Partitions of bases into disjoint unions of
>   bases*. J. Number Theory (1988), 1-9.
> - [Er92c] Erdős, P., *Some of my forgotten problems in number theory*. Hardy-Ramanujan J. (1992),
>   34-50.
> - [La26] Larsen, D., *Three questions of Erdős–Nathanson on asymptotic bases of order 2*.
>   [arXiv:2603.03472](https://arxiv.org/abs/2603.03472) (2026).

*Quoted from [FormalConjectures/ErdosProblems/869.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/869.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/869](https://www.erdosproblems.com/869).

The file states 1 research or textbook statement: 1 solved.

## `Erdos869.erdos_869`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos869.lean#L3490](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos869.lean#L3490).

> If $A_1, A_2$ are disjoint additive bases of order $2$ (i.e. $A_i + A_i$ contains all large
> integers) then must $A = A_1 \cup A_2$ contain a minimal additive basis of order $2$ (one such that
> deleting any element creates infinitely many $n \notin A + A$)?
>
> A question of Erdős and Nathanson [ErNa88, Er92c]. The answer is no: Larsen [La26] constructed
> disjoint bases $A_1, A_2$ of order $2$ such that $A_1 \cup A_2$ contains no minimal basis of
> order $2$.

```lean
theorem erdos_869 :
    ¬ ∀ (A₁ A₂ : Set ℕ), Disjoint A₁ A₂ →
      A₁.IsAsymptoticAddBasisOfOrder 2 → A₂.IsAsymptoticAddBasisOfOrder 2 →
      ∃ D ⊆ A₁ ∪ A₂, D.IsAsymptoticAddBasisOfOrder 2 ∧
        ∀ d ∈ D, ¬ (D \ {d}).IsAsymptoticAddBasisOfOrder 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/869.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/869.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/869.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/869.lean)
- [erdosproblems.com/869](https://www.erdosproblems.com/869)
