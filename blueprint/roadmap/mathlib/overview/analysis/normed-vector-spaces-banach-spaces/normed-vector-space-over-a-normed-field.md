# Normed vector space over a normed field

A normed space over a normed field is a vector space endowed with a norm which satisfies the
equality `‖c • x‖ = ‖c‖ ‖x‖`. We require only `‖c • x‖ ≤ ‖c‖ ‖x‖` in the definition, then prove
`‖c • x‖ = ‖c‖ ‖x‖` in `norm_smul`.

Note that since this requires `SeminormedAddCommGroup` and not `NormedAddCommGroup`, this
typeclass can be used for "seminormed spaces" too, just as `Module` can be used for
"semimodules".

```lean
NormedSpace.{u_6, u_7} (𝕜 : Type u_6) (E : Type u_7) [NormedField 𝕜] [SeminormedAddCommGroup E] :
  Type (max u_6 u_7)
```

## Depends on

- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Module](../../linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `NormedSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Module/Basic.html#NormedSpace)
- [Source of `NormedSpace` in Mathlib/Analysis/Normed/Module/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Module/Basic.lean#L29)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L279)
