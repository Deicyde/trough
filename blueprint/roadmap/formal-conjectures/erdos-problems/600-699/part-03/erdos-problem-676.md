---
declaration: theorem
origin: cited
lean: Erdos676.erdos_676
statement: formalized
---

# Erdős Problem 676

> *References:*
> - [erdosproblems.com/676](https://www.erdosproblems.com/676)
> - [Er79] Erdős, Paul, *Some unconventional problems in number theory*.
>   Math. Mag. (1979), 67–70.
> - [Er79d] Erdős, P., *Some unconventional problems in number theory*.
>   Acta Math. Acad. Sci. Hungar. (1979), 71–80.
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*.
>   Ann. Discrete Math. (1980), 89–115.

*Quoted from [FormalConjectures/ErdosProblems/676.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/676.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/676](https://www.erdosproblems.com/676).

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `Erdos676.erdos_676`

Open: stated without proof.

> Is every sufficiently large integer of the form $ap^2+b$ for some prime $p$ and integers
> $a \geq 1$ and $0 \leq b < p$?

```lean
theorem erdos_676 : ∀ᶠ n in atTop,
    ∃ a p b : ℕ, p.Prime ∧ 1 ≤ a ∧ b < p ∧ n = a * p ^ 2 + b
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/676.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/676.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/676.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/676.lean)
- [erdosproblems.com/676](https://www.erdosproblems.com/676)
