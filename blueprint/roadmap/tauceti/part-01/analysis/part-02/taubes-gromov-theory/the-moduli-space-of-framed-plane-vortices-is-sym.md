---
declaration: def
origin: cited
lean: TauCeti.Vortex.framedVortexModuliEquiv
statement: formalized
---

# The moduli space of framed plane vortices is `Sym ℂ m` (Taubes)

The divisor identifies
the orbits of the smooth framed gauge group on the smooth framed degree-`m` vortices with the
effective divisors of degree `m`.

```lean
TauCeti.Vortex.framedVortexModuliEquiv (m : ℕ) :
  MulAction.orbitRel.Quotient ↥TauCeti.Vortex.framedGaugeGroup
      ↥(TauCeti.Vortex.framedVortexSubMulAction m) ≃
    Sym ℂ m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula with a cutoff](../../part-03/complex/part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)
- [Taubes's existence theorem](taubess-existence-theorem.md)
- [Taubes's uniqueness theorem](taubess-uniqueness-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.framedVortexModuliEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Existence.html#TauCeti.Vortex.framedVortexModuliEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.framedVortexModuliEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Existence.html#TauCeti.Vortex.framedVortexModuliEquiv)
- [Source of `TauCeti.Vortex.framedVortexModuliEquiv` in TauCeti/Analysis/PDE/Vortex/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Vortex/Existence.lean#L317)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
