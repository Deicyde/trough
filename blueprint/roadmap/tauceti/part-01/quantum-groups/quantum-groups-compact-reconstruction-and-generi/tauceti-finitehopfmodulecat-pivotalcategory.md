---
declaration: def
origin: cited
lean: TauCeti.FiniteHopfModuleCat.pivotalCategory
statement: formalized
---

# TauCeti.FiniteHopfModuleCat.pivotalCategory

For a group-like unit `g` implementing the square of the antipode, the double dual
comparisons `m ↦ (φ ↦ φ(g m))` form a pivotal structure on finite-dimensional `H`-modules. The
rigid structure is `rigidCategory`, whose left duals are the inverse-antipode contragredients;
the bijectivity of the antipode it needs is deduced from `hg`. This differs from
`pivotalCategoryOfRightRigid`, whose left duals are the right duals themselves. Not an instance,
since it depends on the choice of `g`.

```lean
TauCeti.FiniteHopfModuleCat.pivotalCategory.{u, v} {k : Type u} [Field k] {H : Type v} [Ring H]
  [HopfAlgebra k H] {g : Hˣ}
  (hg :
    ∀ (a : H), (HopfAlgebraStruct.antipode k) ((HopfAlgebraStruct.antipode k) a) = ↑g * a * ↑g⁻¹)
  (hg₁ : IsGroupLikeElem k ↑g) : TauCeti.PivotalCategory (TauCeti.FiniteHopfModuleCat k H)
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)
- [TauCeti.FiniteHopfModuleCat.rigidCategory](tauceti-finitehopfmodulecat-rigidcategory.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteHopfModuleCat.pivotalCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/Pivotal.html#TauCeti.FiniteHopfModuleCat.pivotalCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteHopfModuleCat.pivotalCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/Pivotal.html#TauCeti.FiniteHopfModuleCat.pivotalCategory)
- [Source of `TauCeti.FiniteHopfModuleCat.pivotalCategory` in TauCeti/Algebra/Category/FiniteHopfModuleCat/Pivotal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/FiniteHopfModuleCat/Pivotal.lean#L233)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
