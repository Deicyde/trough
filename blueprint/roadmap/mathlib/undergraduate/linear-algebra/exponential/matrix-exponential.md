---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: NormedSpace.exp
mathlib_file: Mathlib/Analysis/Normed/Algebra/Exponential.lean
---

# Matrix exponential

`NormedSpace.exp : 𝔸 → 𝔸` is the exponential map. It is defined as the sum of the
`FormalMultilinearSeries` `expSeries ℚ 𝔸`.

If `𝔸` can't be equipped with a `ℚ`-algebra structure, we use the junk value `1`. For details on why
this approach is taken, see the module documentation for
`Mathlib/Analysis/Normed/Algebra/Exponential.lean`.

Note that when `𝔸 = Matrix n n 𝕂`, this is the **Matrix Exponential**; see
`Mathlib/Analysis/Normed/Algebra/MatrixExponential.lean` for lemmas
specific to that case.

```lean
NormedSpace.exp.{u_2} {𝔸 : Type u_2} [Ring 𝔸] [TopologicalSpace 𝔸] [IsTopologicalRing 𝔸] (x : 𝔸) : 𝔸
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Field $\Q$ of rational numbers](../../ring-theory/field-theory/part-01/field-q-of-rational-numbers.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Multilinear map](../../../overview/linear-algebra/fundamentals/multilinear-map.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `NormedSpace.exp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Algebra/Exponential.html#NormedSpace.exp)
- [Source of `NormedSpace.exp` in Mathlib/Analysis/Normed/Algebra/Exponential.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Algebra/Exponential.lean#L118)
- [Mathlib undergraduate list: Linear algebra › Exponential](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L74)
