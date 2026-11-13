---
declaration: theorem
origin: cited
lean: Erdos26.erdos_26, Erdos26.erdos_26.variants.rusza, Erdos26.erdos_26.variants.tenenbaum
statement: formalized
---

# Erdős Problem 26

> *References:*
> - [erdosproblems.com/26](https://www.erdosproblems.com/26)
> - [Te19](https://arxiv.org/pdf/1908.00488) G. Tenenbaum,
>   _Some of Erdős' unconventional problems in number theory, thirty-four years later_,
>   arXiv:1908.00488 [math.NT] (2019)

*Quoted from [FormalConjectures/ErdosProblems/26.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/26.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/26](https://www.erdosproblems.com/26).

The file states 3 research or textbook statements: 3 solved. It also has 7 test statements, counted here but not shown.

## `Erdos26.erdos_26`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos26.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos26.lean).

> Let $A\subset\mathbb{N}$ be infinite such that $\sum_{a \in A} \frac{1}{a} = \infty$. Must
> there exist some $k\geq 1$ such that almost all integers have a divisor of the form $a+k$
> for some $a\in A$?
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_26 : ¬ ∀ A : ℕ → ℕ, StrictMono A → IsThick A →
    ∃ k, IsBehrend (A · + k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/26.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/26.lean#L99).

## `Erdos26.erdos_26.variants.rusza`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos26.lean#L752](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos26.lean#L752).

> If we allow for $\sum_{a\in A} \frac{1}{a} < \infty$ then Rusza has found a counter-example.

```lean
theorem erdos_26.variants.rusza : ∃ A : ℕ → ℕ,
    StrictMono A ∧ ¬IsThick A ∧ ∀ k, ¬IsBehrend (A · + k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/26.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/26.lean#L109).

## `Erdos26.erdos_26.variants.tenenbaum`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/09c54540aa51cb40dff73660c94a82e2631386f8/FormalConjectures/ErdosProblems/26.lean#L625](https://github.com/mo271/formal-conjectures/blob/09c54540aa51cb40dff73660c94a82e2631386f8/FormalConjectures/ErdosProblems/26.lean#L625).

> Tenenbaum asked the weaker variant where for every $\epsilon>0$ there is
> some $k=k(\epsilon)$ such that at least $1-\epsilon$ density of all integers have a
> divisor of the form $a+k$ for some $a\in A$.
>
> The DeepMind prover agent has found a formal disproof of this statement.

```lean
theorem erdos_26.variants.tenenbaum : ¬ ∀ᵉ (A : ℕ → ℕ), StrictMono A → IsThick A →
    (∀ ε > (0 : ℝ), ∃ k, IsWeaklyBehrend (A · + k) ε)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/26.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/26.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/26.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/26.lean)
- [erdosproblems.com/26](https://www.erdosproblems.com/26)
