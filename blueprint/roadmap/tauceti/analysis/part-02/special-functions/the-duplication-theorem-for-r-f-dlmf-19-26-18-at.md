---
declaration: theorem
origin: cited
lean: Complex.carlsonRF_ofReal_duplication
statement: formalized
proof: formalized
---

# The duplication theorem for `R_F` (DLMF 19.26.18) at nonnegative real arguments

for real
`x, y, z ≥ 0`, with `λ = √x √y + √y √z + √z √x`,
`R_F(x, y, z) = R_F((x + λ)/4, (y + λ)/4, (z + λ)/4)`.

No hypothesis beyond nonnegativity is needed. When two of `x, y, z` vanish, the defining integrals
on both sides diverge and the identity is between the totalized values `0`.

```lean
Complex.carlsonRF_ofReal_duplication {x y z : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) :
  have l := √x * √y + √y * √z + √z * √x;
  (↑x).carlsonRF ↑y ↑z = (↑((x + l) / 4)).carlsonRF ↑((y + l) / 4) ↑((z + l) / 4)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.carlsonRF_ofReal_duplication`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Basic.html#Complex.carlsonRF_ofReal_duplication).

## Sources

- [Tau Ceti documentation: `Complex.carlsonRF_ofReal_duplication`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Basic.html#Complex.carlsonRF_ofReal_duplication)
- [Source of `Complex.carlsonRF_ofReal_duplication` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Duplication/Basic.lean#L152)
