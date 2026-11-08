---
declaration: theorem
origin: cited
lean: TauCeti.mul_burkholderPhi_le
statement: formalized
proof: formalized
---

# The scalar Bellman majorization estimate

For `2 ≤ p` and `x, y ≥ 0`,
`((p - 1) ^ (p - 1) / p ^ (p - 2)) Φ_p(x, y) ≤ (p - 1) ^ p x ^ p - y ^ p`.

```lean
TauCeti.mul_burkholderPhi_le {p : ℝ} (hp : 2 ≤ p) {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) :
  (p - 1) ^ (p - 1) / p ^ (p - 2) * TauCeti.burkholderPhi p x y ≤ (p - 1) ^ p * x ^ p - y ^ p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mul_burkholderPhi_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.html#TauCeti.mul_burkholderPhi_le).

## Sources

- [Tau Ceti documentation: `TauCeti.mul_burkholderPhi_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.html#TauCeti.mul_burkholderPhi_le)
- [Source of `TauCeti.mul_burkholderPhi_le` in TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Pow/Burkholder.lean#L202)
