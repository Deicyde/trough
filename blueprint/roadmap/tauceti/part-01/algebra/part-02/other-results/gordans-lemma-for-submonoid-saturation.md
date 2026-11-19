---
declaration: theorem
origin: cited
lean: AddSubmonoid.FG.nsmulSaturation
statement: formalized
proof: formalized
---

# Gordan's lemma for submonoid saturation

In a free abelian group `L`, the saturation of any
finitely generated additive submonoid `S` is finitely generated.

```lean
AddSubmonoid.FG.nsmulSaturation.{u_1} {L : Type u_1} [AddCommGroup L] [Module.Free ℤ L]
  {S : AddSubmonoid L} (hS : S.FG) : S.nsmulSaturation.FG
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddSubmonoid.FG.nsmulSaturation`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Submonoid/Finiteness.html#AddSubmonoid.FG.nsmulSaturation).

## Sources

- [Tau Ceti documentation: `AddSubmonoid.FG.nsmulSaturation`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Submonoid/Finiteness.html#AddSubmonoid.FG.nsmulSaturation)
- [Source of `AddSubmonoid.FG.nsmulSaturation` in TauCeti/Algebra/Group/Submonoid/Finiteness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Group/Submonoid/Finiteness.lean#L160)
