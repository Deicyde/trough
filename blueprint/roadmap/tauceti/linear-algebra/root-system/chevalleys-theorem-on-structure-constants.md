---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.structureConstant_eq_natCast_or_eq_neg_natCast
statement: formalized
proof: formalized
---

# Chevalley's theorem on structure constants

If `α + β` is a root, then
`N_{α,β} = ±(r + 1)`, where `r = chainBotCoeff α β` is the largest integer with `β - r α` a root
of the pinned datum.

```lean
TauCeti.DynkinType.structureConstant_eq_natCast_or_eq_neg_natCast {t : TauCeti.DynkinType}
  {ht : t.Valid} {α β : Fin t.numRoots}
  (h :
    (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β ∈
      Set.range ⇑(t.simplyConnectedRootDatum ht).root) :
  t.structureConstant ht α β = ↑(RootPairing.chainBotCoeff α β + 1) ∨
    t.structureConstant ht α β = -↑(RootPairing.chainBotCoeff α β + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.structureConstant_eq_natCast_or_eq_neg_natCast`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/StructureConstant.html#TauCeti.DynkinType.structureConstant_eq_natCast_or_eq_neg_natCast).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.structureConstant_eq_natCast_or_eq_neg_natCast`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/StructureConstant.html#TauCeti.DynkinType.structureConstant_eq_natCast_or_eq_neg_natCast)
- [Source of `TauCeti.DynkinType.structureConstant_eq_natCast_or_eq_neg_natCast` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/StructureConstant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/StructureConstant.lean#L135)
