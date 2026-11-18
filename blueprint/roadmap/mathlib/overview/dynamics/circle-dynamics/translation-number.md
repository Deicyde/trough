# Translation number

The translation number of a `CircleDeg1Lift`, $τ(f)=\lim_{n→∞}\frac{f^n(x)-x}{n}$. We use
an auxiliary sequence `\frac{f^{2^n}(0)}{2^n}` to define `τ(f)` because some proofs are simpler
this way.

```lean
CircleDeg1Lift.translationNumber (f : CircleDeg1Lift) : ℝ
```

## Depends on

- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Sources

- [Mathlib documentation: `CircleDeg1Lift.translationNumber`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.html#CircleDeg1Lift.translationNumber)
- [Source of `CircleDeg1Lift.translationNumber` in Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.lean#L547)
- [Mathlib overview: Dynamics › Circle dynamics](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L557)
