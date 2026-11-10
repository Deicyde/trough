---
declaration: theorem
origin: cited
lean: OeisA113255.conjecture
statement: formalized
---

# Conjectures associated with A113255

> Corresponds to m = 9 in a family of 4th-order linear recurrence sequences
>
> This sequence is defined by the recurrence relation
> $a(n) = -4 a(n-1) + 324 a(n-3) + 6561 a(n-4)$ for n > 3.
> Initial values are $a(0) = -1, a(1) = 4, a(2) = 227, a(3) = 5329$.
>
> *References:*
> - [A113255](https://oeis.org/A113255)

*Quoted from [FormalConjectures/OEIS/113255.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113255.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA113255.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a113249-family-square-terms-lean/blob/9b999db08344184285e8050c2722c845fd5f5309/lean/OeisA113249FamilyFC.lean#L126-L134](https://github.com/KitaKen1/oeis-a113249-family-square-terms-lean/blob/9b999db08344184285e8050c2722c845fd5f5309/lean/OeisA113249FamilyFC.lean#L126-L134).

> Conjecture: $a(m, 2n+1)$ is a perfect square for all $m, n$ (see A113249).
> Specialized for $m=9$, which is A113255.

```lean
theorem conjecture : ∀ n : ℕ, IsSquare (a (2 * n + 1))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113255.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113255.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113255.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113255.lean)
- [A113255](https://oeis.org/A113255)
