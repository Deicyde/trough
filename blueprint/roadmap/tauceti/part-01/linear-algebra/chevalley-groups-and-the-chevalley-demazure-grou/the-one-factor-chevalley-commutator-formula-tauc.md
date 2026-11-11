---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add
statement: formalized
proof: formalized
---

# The one-factor Chevalley commutator formula (`TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add`)

If `γ = α + β` is a root while `2α + β` and
`α + 2β` are not, then `⁅x_α(u), x_β(v)⁆ = x_γ(N_{α,β} u v)` in the points of `D` over every
commutative ring.

```lean
TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add.{v}
  {t : TauCeti.DynkinType} {ht : t.Valid} (D : t.ChevalleyDatum ht) {α β γ : Fin t.numRoots}
  (hγ :
    (t.simplyConnectedRootDatum ht).root γ =
      (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β)
  (hα :
    2 • (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β ∉
      Set.range ⇑(t.simplyConnectedRootDatum ht).root)
  (hβ :
    (t.simplyConnectedRootDatum ht).root α + 2 • (t.simplyConnectedRootDatum ht).root β ∉
      Set.range ⇑(t.simplyConnectedRootDatum ht).root)
  (A : Type v) [CommRing A] (u v : A) :
  ⁅(D.rootSubgroupPoints α A) (Multiplicative.ofAdd u),
      (D.rootSubgroupPoints β A) (Multiplicative.ofAdd v)⁆ =
    (D.rootSubgroupPoints γ A) (Multiplicative.ofAdd (↑(t.structureConstant ht α β) * (u * v)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The one-factor Chevalley commutator formula (`TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_add`)](../root-system/the-one-factor-chevalley-commutator-formula-tauc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator.html#TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator.html#TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add)
- [Source of `TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add` in TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator.lean#L80)
