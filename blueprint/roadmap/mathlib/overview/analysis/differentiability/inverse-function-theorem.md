# Inverse function theorem (Differentiability)

If `f` has an invertible derivative `f'` at `a` in the sense of strict differentiability `(hf)`,
then the inverse function `hf.localInverse f` has derivative `f'.symm` at `f a`.

```lean
HasStrictFDerivAt.to_localInverse.{u_1, u_2, u_3} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {f : E → F} {f' : E ≃L[𝕜] F} {a : E} [CompleteSpace E]
  (hf : HasStrictFDerivAt f (↑f') a) :
  HasStrictFDerivAt (HasStrictFDerivAt.localInverse f f' a hf) (↑f'.symm) (f a)
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `HasStrictFDerivAt.to_localInverse`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.html#HasStrictFDerivAt.to_localInverse)
- [Source of `HasStrictFDerivAt.to_localInverse` in Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.lean#L185)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L316)
- [1000+ theorems list: Q931001](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1108)
- [1000+ theorems project: Q931001](https://1000-plus.github.io/all.html?length=-1#Q931001)
- [Wikipedia: Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem)
- [Wikidata: Q931001](https://www.wikidata.org/wiki/Q931001)
