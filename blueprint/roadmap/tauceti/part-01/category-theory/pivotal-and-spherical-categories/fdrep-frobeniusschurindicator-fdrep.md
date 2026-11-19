---
declaration: theorem
origin: cited
lean: FDRep.frobeniusSchurIndicator_fdRep
statement: formalized
proof: formalized
---

# FDRep.frobeniusSchurIndicator_fdRep

In `FDRep k G` with its standard spherical structure, the `n`-th Frobenius–Schur indicator of
`V` equals `(Nat.card G : k)⁻¹ * ∑ g : G, V.character (g ^ (n : ℕ))` whenever `|G|` is invertible
in `k`.

```lean
FDRep.frobeniusSchurIndicator_fdRep.{u, v} {k : Type u} {G : Type v} [Field k] [Group G] [Fintype G]
  [Invertible ↑(Nat.card G)] (V : FDRep k G) (n : ℕ+) :
  TauCeti.frobeniusSchurIndicator k V n = (↑(Nat.card G))⁻¹ * ∑ g, V.character (g ^ ↑n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FDRep.frobeniusSchurIndicator_fdRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FDRep/FrobeniusSchur.html#FDRep.frobeniusSchurIndicator_fdRep).

## Sources

- [Tau Ceti documentation: `FDRep.frobeniusSchurIndicator_fdRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FDRep/FrobeniusSchur.html#FDRep.frobeniusSchurIndicator_fdRep)
- [Source of `FDRep.frobeniusSchurIndicator_fdRep` in TauCeti/RepresentationTheory/FDRep/FrobeniusSchur.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/FDRep/FrobeniusSchur.lean#L71)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
