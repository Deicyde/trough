---
declaration: theorem
origin: cited
lean: Erdos645.erdos_645
statement: formalized
---

# Erdős Problem 645

> *References:*
> - [erdosproblems.com/645](https://www.erdosproblems.com/645)
> - [BrLa99] Brown, Tom C. and Landman, Bruce M., Monochromatic arithmetic progressions with large
>   differences. Bull. Austral. Math. Soc. (1999), 21--35.

*Quoted from [FormalConjectures/ErdosProblems/645.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/645.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/645](https://www.erdosproblems.com/645).

The file states 1 research or textbook statement: 1 solved.

## `Erdos645.erdos_645`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos645.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos645.lean).

> If ℕ is $2$-coloured then there must exist a monochromatic three-term arithmetic progression
> $x,x+d,x+2d$ such that $d>x$.
>
> This was first proved by Brown and Landman [BrLa99], who in fact show that this is always possible
> with $d>f(x)$ for any increasing function $f$.
>
> This was formalized in Lean by Alexeev using Aristotle and ChatGPT.

```lean
theorem erdos_645 (c : ℕ → Bool) : ∃ x d, 0 < x ∧ x < d ∧
    (∃ C, c x = C ∧ c (x + d) = C ∧ c (x + 2 * d) = C)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/645.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/645.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/645.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/645.lean)
- [erdosproblems.com/645](https://www.erdosproblems.com/645)
