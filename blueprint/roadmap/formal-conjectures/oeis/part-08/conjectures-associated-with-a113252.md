---
declaration: theorem
origin: cited
lean: OeisA113252.conjecture
statement: formalized
---

# Conjectures associated with A113252

> Corresponds to m = 6 in a family of 4th order linear recurrence sequences
>
> This sequence is defined by the linear recurrence relation
> a(n) = -4 a(n-1) + 144 a(n-3) + 1296 a(n-4) for n > 3.
> Initial values are a(0) = -1, a(1) = 4, a(2) = 92, a(3) = 784.
>
> *References:*
> - [A113252](https://oeis.org/A113252)

*Quoted from [FormalConjectures/OEIS/113252.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113252.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA113252.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a113249-family-square-terms-lean/blob/9b999db08344184285e8050c2722c845fd5f5309/lean/OeisA113249FamilyFC.lean#L116-L124](https://github.com/KitaKen1/oeis-a113249-family-square-terms-lean/blob/9b999db08344184285e8050c2722c845fd5f5309/lean/OeisA113249FamilyFC.lean#L116-L124).

> Conjecture: $a(m, 2n+1)$ is a perfect square for all $m, n$ (see A113249).
> Specialized for $m=6$, which is A113252.

```lean
theorem conjecture : ∀ n : ℕ, IsSquare (a (2 * n + 1))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113252.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113252.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113252.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113252.lean)
- [A113252](https://oeis.org/A113252)
