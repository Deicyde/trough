---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.exists_norm_inclusion_le
statement: formalized
proof: formalized
---

# Ehrling's inequality on the circle

for `r ≤ t < s`, the `H^t` norm is bounded by an
arbitrarily small multiple of the `H^s` norm plus a multiple of the weaker `H^r` norm.

```lean
TauCeti.CircleSobolev.exists_norm_inclusion_le.{u_1} {s t : ℝ} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {r : ℝ} (hrt : r ≤ t) (hts : t < s) {ε : ℝ} (hε : 0 < ε) :
  ∃ C,
    0 ≤ C ∧
      ∀ (a : TauCeti.CircleSobolev s E),
        ‖(TauCeti.CircleSobolev.inclusion ⋯) a‖ ≤
          ε * ‖a‖ + C * ‖(TauCeti.CircleSobolev.inclusion ⋯) a‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.exists_norm_inclusion_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.exists_norm_inclusion_le).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.exists_norm_inclusion_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.exists_norm_inclusion_le)
- [Source of `TauCeti.CircleSobolev.exists_norm_inclusion_le` in TauCeti/Analysis/Sobolev/Circle/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Circle/Basic.lean#L765)
