---
declaration: theorem
origin: cited
lean: PowerSeries.henselianLocalRing
statement: formalized
proof: formalized
---

# Hensel's lemma for `K⟦t⟧`

Over a field `K`, the power series ring `K⟦t⟧` is a Henselian
local ring: it is complete for its maximal ideal `(t)`, so this is Mathlib's
`IsAdicComplete.henselianRing` at the maximal ideal, read through
`TauCeti.IsAdicComplete.henselianLocalRing`.

```lean
PowerSeries.henselianLocalRing.{u_1} {K : Type u_1} [Field K] : HenselianLocalRing (PowerSeries K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Hensel.html#PowerSeries.henselianLocalRing).

## Sources

- [Tau Ceti documentation: `PowerSeries.henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Hensel.html#PowerSeries.henselianLocalRing)
- [Source of `PowerSeries.henselianLocalRing` in TauCeti/RingTheory/PowerSeries/Hensel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/PowerSeries/Hensel.lean#L396)
