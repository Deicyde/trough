---
declaration: theorem
origin: cited
lean: FormalGroup.heightIdeal_eq_span
statement: formalized
proof: formalized
---

# Landweber's generators

`I_n(F) = (v₀, …, v_(n-1))`, where `v_i` is the coefficient of
`X^(pⁱ)` in `[p]_F`; in particular `v₀ = p`.

```lean
FormalGroup.heightIdeal_eq_span.{u_1} {R : Type u_1} [CommRing R] {p : ℕ} (F : FormalGroup R)
  [F.IsComm] (hp : Nat.Prime p) (n : ℕ) :
  F.heightIdeal p n =
    Ideal.span ((fun i => (PowerSeries.coeff (p ^ i)) (F.nsmulSeries p)) '' Set.Iio n)
```

## Depends on

- [FormalGroup.heightIdeal](formalgroup-heightideal.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.heightIdeal_eq_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Ideal.html#FormalGroup.heightIdeal_eq_span).

## Sources

- [Tau Ceti documentation: `FormalGroup.heightIdeal_eq_span`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Ideal.html#FormalGroup.heightIdeal_eq_span)
- [Source of `FormalGroup.heightIdeal_eq_span` in TauCeti/RingTheory/FormalGroup/Height/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Height/Ideal.lean#L283)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
