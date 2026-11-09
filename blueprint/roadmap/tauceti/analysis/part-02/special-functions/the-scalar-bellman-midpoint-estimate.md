---
declaration: theorem
origin: cited
lean: TauCeti.two_mul_burkholderPhi_abs_le
statement: formalized
proof: formalized
---

# The scalar Bellman midpoint estimate

For `2 ≤ p`, real `x`, `y`, `a` and `ε` with
`|ε| = 1`, `2 Φ_p(|x|, |y|) ≤ Φ_p(|x + a|, |y + ε a|) + Φ_p(|x - a|, |y - ε a|)`.

```lean
TauCeti.two_mul_burkholderPhi_abs_le {p : ℝ} (hp : 2 ≤ p) (x y a : ℝ) {ε : ℝ} (hε : |ε| = 1) :
  2 * TauCeti.burkholderPhi p |x| |y| ≤
    TauCeti.burkholderPhi p |x + a| |y + ε * a| + TauCeti.burkholderPhi p |x - a| |y - ε * a|
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.two_mul_burkholderPhi_abs_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.html#TauCeti.two_mul_burkholderPhi_abs_le).

## Sources

- [Tau Ceti documentation: `TauCeti.two_mul_burkholderPhi_abs_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.html#TauCeti.two_mul_burkholderPhi_abs_le)
- [Source of `TauCeti.two_mul_burkholderPhi_abs_le` in TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.lean#L382)
