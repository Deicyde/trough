---
declaration: theorem
origin: cited
lean: TauCeti.norm_add_rpow_add_norm_sub_rpow_le
statement: formalized
proof: formalized
---

# The pointwise Clarkson inequality

For `2 ≤ q` and vectors `a`, `b` of a normed group
satisfying the parallelogram identity,
`‖a + b‖ ^ q + ‖a - b‖ ^ q ≤ 2 ^ (q - 1) * (‖a‖ ^ q + ‖b‖ ^ q)`.

```lean
TauCeti.norm_add_rpow_add_norm_sub_rpow_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpaceable E] {q : ℝ} (hq : 2 ≤ q) (a b : E) :
  ‖a + b‖ ^ q + ‖a - b‖ ^ q ≤ 2 ^ (q - 1) * (‖a‖ ^ q + ‖b‖ ^ q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_add_rpow_add_norm_sub_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Clarkson.html#TauCeti.norm_add_rpow_add_norm_sub_rpow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_add_rpow_add_norm_sub_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Clarkson.html#TauCeti.norm_add_rpow_add_norm_sub_rpow_le)
- [Source of `TauCeti.norm_add_rpow_add_norm_sub_rpow_le` in TauCeti/Analysis/InnerProductSpace/Clarkson.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Clarkson.lean#L42)
