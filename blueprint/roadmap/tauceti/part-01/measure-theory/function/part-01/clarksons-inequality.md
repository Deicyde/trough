---
declaration: theorem
origin: cited
lean: MeasureTheory.Lp.norm_add_rpow_add_norm_sub_rpow_le
statement: formalized
proof: formalized
---

# Clarkson's inequality

For `2 ≤ p < ∞` and `f g : Lp E p μ`, where the norm of `E`
satisfies the parallelogram identity,
`‖f + g‖ ^ p + ‖f - g‖ ^ p ≤ 2 ^ (p - 1) * (‖f‖ ^ p + ‖g‖ ^ p)`.

```lean
MeasureTheory.Lp.norm_add_rpow_add_norm_sub_rpow_le.{u_1, u_2} {α : Type u_1} {E : Type u_2}
  {m : MeasurableSpace α} {μ : MeasureTheory.Measure α} [NormedAddCommGroup E] {p : ENNReal}
  [InnerProductSpaceable E] (hp : 2 ≤ p) (hp_top : p ≠ ⊤) (f g : ↥(MeasureTheory.Lp E p μ)) :
  ‖f + g‖ ^ p.toReal + ‖f - g‖ ^ p.toReal ≤ 2 ^ (p.toReal - 1) * (‖f‖ ^ p.toReal + ‖g‖ ^ p.toReal)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The pointwise Clarkson inequality](../../../analysis/part-03/inner-product-space/part-02/the-pointwise-clarkson-inequality.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Lp.norm_add_rpow_add_norm_sub_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/UniformConvex.html#MeasureTheory.Lp.norm_add_rpow_add_norm_sub_rpow_le).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Lp.norm_add_rpow_add_norm_sub_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/Lp/UniformConvex.html#MeasureTheory.Lp.norm_add_rpow_add_norm_sub_rpow_le)
- [Source of `MeasureTheory.Lp.norm_add_rpow_add_norm_sub_rpow_le` in TauCeti/MeasureTheory/Function/Lp/UniformConvex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/Lp/UniformConvex.lean#L72)
