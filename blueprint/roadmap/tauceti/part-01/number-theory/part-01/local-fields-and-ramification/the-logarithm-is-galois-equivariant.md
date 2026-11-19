---
declaration: theorem
origin: cited
lean: AlgEquiv.map_log
statement: formalized
proof: formalized
---

# The logarithm is Galois-equivariant

Every `K`-automorphism of an extension `L/K` of
nonarchimedean local fields (necessarily finite) commutes with the logarithm:
`σ (log u) = log (σ u)`. This is `RingEquiv.map_log_of_continuous` for the homeomorphism `σ`.

```lean
AlgEquiv.map_log.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L]
  [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L]
  (σ : Gal(L/K)) (u : L) : σ (NormedSpace.log u) = NormedSpace.log (σ u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`AlgEquiv.map_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Logarithm.html#AlgEquiv.map_log).

## Sources

- [Tau Ceti documentation: `AlgEquiv.map_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Logarithm.html#AlgEquiv.map_log)
- [Source of `AlgEquiv.map_log` in TauCeti/NumberTheory/LocalField/Logarithm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/Logarithm.lean#L305)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalFieldsRamification/STATUS.md)
