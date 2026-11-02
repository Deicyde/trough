---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ImplicitFunctionData.implicitFunction
mathlib_file: Mathlib/Analysis/Calculus/Implicit.lean
---

# Implicit function theorem

Implicit function theorem. If `f : E → F` and `g : E → G` are two maps strictly differentiable
at `a`, their derivatives `f'`, `g'` are surjective, and the kernels of these derivatives are
complementary subspaces of `E`, then `implicitFunction` is the unique (germ of a) map
`φ : F → G → E` such that `f (φ y z) = y` and `g (φ y z) = z`.

```lean
ImplicitFunctionData.implicitFunction.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [CompleteSpace E] {F : Type u_3} [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F]
  {G : Type u_4} [NormedAddCommGroup G] [NormedSpace 𝕜 G] [CompleteSpace G]
  (φ : ImplicitFunctionData 𝕜 E F G) : F → G → E
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `ImplicitFunctionData.implicitFunction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Implicit.html#ImplicitFunctionData.implicitFunction)
- [Source of `ImplicitFunctionData.implicitFunction` in Mathlib/Analysis/Calculus/Implicit.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Implicit.lean#L155)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L317)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L474)
- [1000+ theorems list: Q848375](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L960)
- [1000+ theorems project: Q848375](https://1000-plus.github.io/all.html?length=-1#Q848375)
- [Wikipedia: Implicit function theorem](https://en.wikipedia.org/wiki/Implicit_function_theorem)
- [Wikidata: Q848375](https://www.wikidata.org/wiki/Q848375)
