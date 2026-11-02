---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ContDiff
mathlib_file: Mathlib/Analysis/Calculus/ContDiff/Defs.lean
---

# $C^k$ function

A function is continuously differentiable up to `n` if it admits derivatives up to
order `n`, which are continuous. Contrary to the case of definitions in domains (where derivatives
might not be unique) we do not need to localize the definition in space or time.
The parameter `n` belongs to `ℕ∞ω` (accessible in the `ContDiff` scope), i.e. it can be a natural
number, `∞`, or `ω`.

For `n = ω`, we require the function to be analytic. The precise
definition we give (all the derivatives should be analytic) is more involved to work around issues
when the space is not complete, but it is equivalent when the space is complete.

```lean
ContDiff.{u, uE, uF} (𝕜 : Type u) [NontriviallyNormedField 𝕜] {E : Type uE} [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] {F : Type uF} [NormedAddCommGroup F] [NormedSpace 𝕜 F] (n : WithTop ℕ∞)
  (f : E → F) : Prop
```

## Depends on

- [Analytic function](analytic-function.md)
- [Differentiable function between normed vector spaces](differentiable-function-between-normed-vector-sp.md)
- [Norm of a continuous linear map](../normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Sources

- [Mathlib documentation: `ContDiff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ContDiff/Defs.html#ContDiff)
- [Source of `ContDiff` in Mathlib/Analysis/Calculus/ContDiff/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/ContDiff/Defs.lean#L1056)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L313)
- [Mathlib undergraduate list: Single Variable Real Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L321)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L465)
