---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add, TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add_two_nsmul
statement: formalized
proof: formalized
---

# The two-factor Chevalley commutator formula (`TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add`)

If `γ = α + β` and `δ = 2α + β` are roots
while `3α + β` and `α + 2β` are not, then in the points of `D` over every commutative ring

```text
⁅x_α(u), x_β(v)⁆ = x_γ(N_{α,β} u v) x_δ(M u² v),    M = N_{α,β} N_{α,γ} / 2,
```

where `M` is the integer with `(ad e_α)² e_β / 2 = M e_δ`; the division is exact.

```lean
TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add.{v}
  {t : TauCeti.DynkinType} {ht : t.Valid} (D : t.ChevalleyDatum ht) {α β γ δ : Fin t.numRoots}
  (hγ :
    (t.simplyConnectedRootDatum ht).root γ =
      (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β)
  (hδ :
    (t.simplyConnectedRootDatum ht).root δ =
      2 • (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β)
  (hα :
    3 • (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β ∉
      Set.range ⇑(t.simplyConnectedRootDatum ht).root)
  (hβ :
    (t.simplyConnectedRootDatum ht).root α + 2 • (t.simplyConnectedRootDatum ht).root β ∉
      Set.range ⇑(t.simplyConnectedRootDatum ht).root)
  (A : Type v) [CommRing A] (u v : A) :
  ⁅(D.rootSubgroupPoints α A) (Multiplicative.ofAdd u),
      (D.rootSubgroupPoints β A) (Multiplicative.ofAdd v)⁆ =
    (D.rootSubgroupPoints γ A) (Multiplicative.ofAdd (↑(t.structureConstant ht α β) * (u * v))) *
      (D.rootSubgroupPoints δ A)
        (Multiplicative.ofAdd
          (↑(t.structureConstant ht α β * t.structureConstant ht α γ / 2) * (u ^ 2 * v)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The two-factor Chevalley commutator formula (`TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add`)](../../../linear-algebra/part-01/root-system/the-two-factor-chevalley-commutator-formula-tauc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator/Basic.html#TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add).

## Other forms

**The two-factor Chevalley commutator formula, long root first.** Formalized in Tau Ceti as [`TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add_two_nsmul`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator/Basic.html#TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add_two_nsmul).

```lean
TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_add_two_nsmul.{v}
  {t : TauCeti.DynkinType} {ht : t.Valid} (D : t.ChevalleyDatum ht) {α β γ δ : Fin t.numRoots}
  (hγ :
    (t.simplyConnectedRootDatum ht).root γ =
      (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β)
  (hδ :
    (t.simplyConnectedRootDatum ht).root δ =
      (t.simplyConnectedRootDatum ht).root α + 2 • (t.simplyConnectedRootDatum ht).root β)
  (hα :
    2 • (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β ∉
      Set.range ⇑(t.simplyConnectedRootDatum ht).root)
  (hβ :
    (t.simplyConnectedRootDatum ht).root α + 3 • (t.simplyConnectedRootDatum ht).root β ∉
      Set.range ⇑(t.simplyConnectedRootDatum ht).root)
  (A : Type v) [CommRing A] (u v : A) :
  ⁅(D.rootSubgroupPoints α A) (Multiplicative.ofAdd u),
      (D.rootSubgroupPoints β A) (Multiplicative.ofAdd v)⁆ =
    (D.rootSubgroupPoints γ A) (Multiplicative.ofAdd (↑(t.structureConstant ht α β) * (u * v))) *
      (D.rootSubgroupPoints δ A)
        (Multiplicative.ofAdd
          (↑(-(t.structureConstant ht β α * t.structureConstant ht β γ / 2)) * (u * v ^ 2)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator/Basic.html#TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add)
- [Source of `TauCeti.DynkinType.ChevalleyDatum.commutatorElement_rootSubgroup_of_root_eq_two_nsmul_add` in TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Chevalley/Commutator/Basic.lean#L108)
