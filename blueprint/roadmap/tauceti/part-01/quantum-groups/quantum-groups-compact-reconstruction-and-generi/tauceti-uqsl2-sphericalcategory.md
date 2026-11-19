---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.sphericalCategory
statement: formalized
proof: formalized
---

# TauCeti.UqSl2.sphericalCategory

For `q - q⁻¹ ≠ 0`, the pivotal structure given by `K⁻¹` is spherical: the left and right
traces `tr_V(K f)` and `tr_V(K⁻¹ f)` of every module endomorphism agree.

```lean
TauCeti.UqSl2.sphericalCategory (q : ℂ) [Fact (q ≠ 0)] (hq : q - q⁻¹ ≠ 0) :
  TauCeti.SphericalCategory (TauCeti.FiniteHopfModuleCat ℂ (TauCeti.UqSl2 q))
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)
- [TauCeti.FiniteHopfModuleCat.pivotalCategory](tauceti-finitehopfmodulecat-pivotalcategory.md)
- [TauCeti.FiniteHopfModuleCat.rigidCategory](tauceti-finitehopfmodulecat-rigidcategory.md)

## Proof depends on

- [The Freyd–Yetter identity](../../category-theory/other-results/the-freyd-yetter-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.sphericalCategory`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Pivotal.html#TauCeti.UqSl2.sphericalCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.sphericalCategory`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/Pivotal.html#TauCeti.UqSl2.sphericalCategory)
- [Source of `TauCeti.UqSl2.sphericalCategory` in TauCeti/QuantumGroups/UqSl2/Pivotal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/UqSl2/Pivotal.lean#L114)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
