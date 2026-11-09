---
declaration: theorem
origin: cited
lean: OeisA113250.conjecture
statement: formalized
---

# Expansion of g.f. $-(1 - 48x^2 - 256x^3) / ((1 - 4x)(1 + 4x)(1 + 4x + 16x^2))$

> Corresponds to m = 4 in a family of 4th-order linear recurrence sequences
>
> This sequence is defined by the linear recurrence relation with signature $(-4, 0, 64, 256)$
> and initial values $a(0) = -1, a(1) = 4, a(2) = 32, a(3) = 64$.
> The recurrence is $a(n) = -4 a(n-1) + 64 a(n-3) + 256 a(n-4)$.
>
> *References:*
> - [A113250](https://oeis.org/A113250)

*Quoted from [FormalConjectures/OEIS/113250.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113250.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA113250.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a113249-family-square-terms-lean/blob/9b999db08344184285e8050c2722c845fd5f5309/lean/OeisA113249FamilyFC.lean#L106-L114](https://github.com/KitaKen1/oeis-a113249-family-square-terms-lean/blob/9b999db08344184285e8050c2722c845fd5f5309/lean/OeisA113249FamilyFC.lean#L106-L114).

> Conjecture: $a(m, 2n+1)$ is a perfect square for all $m$ (see A113249).
> Specialized to $m = 4$, which is A113250.

```lean
theorem conjecture : ∀ n : ℕ, IsSquare (a (2 * n + 1))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113250.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113250.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113250.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113250.lean)
- [A113250](https://oeis.org/A113250)
