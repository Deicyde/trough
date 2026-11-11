---
declaration: theorem
origin: cited
lean: TauCeti.moebius_sub_moebius
statement: formalized
proof: formalized
---

# The Möbius difference formula

if both denominators are nonzero, then
`(a * t + b) / (c * t + d) - (a * w + b) / (c * w + d) =
(a * d - b * c) * (t - w) / ((c * t + d) * (c * w + d))`.

```lean
TauCeti.moebius_sub_moebius.{u_1} {𝕜 : Type u_1} [Field 𝕜] {a b c d w t : 𝕜} (hj : c * w + d ≠ 0)
  (hjt : c * t + d ≠ 0) :
  (a * t + b) / (c * t + d) - (a * w + b) / (c * w + d) =
    (a * d - b * c) * (t - w) / ((c * t + d) * (c * w + d))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.moebius_sub_moebius`](https://taucetiproject.org/docs/TauCeti/Algebra/Field/LinearFractional.html#TauCeti.moebius_sub_moebius).

## Sources

- [Tau Ceti documentation: `TauCeti.moebius_sub_moebius`](https://taucetiproject.org/docs/TauCeti/Algebra/Field/LinearFractional.html#TauCeti.moebius_sub_moebius)
- [Source of `TauCeti.moebius_sub_moebius` in TauCeti/Algebra/Field/LinearFractional.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Field/LinearFractional.lean#L50)
