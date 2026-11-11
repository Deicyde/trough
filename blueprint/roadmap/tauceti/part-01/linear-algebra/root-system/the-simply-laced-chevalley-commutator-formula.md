---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_isSimplyLaced
statement: formalized
proof: formalized
---

# The simply-laced Chevalley commutator formula

At every root sum `γ = α + β`,
`⁅x_α(u), x_β(v)⁆ = x_γ(N_{α,β}uv)`. The structure constant and both vanishing higher brackets
are determined by the pinned Chevalley system. The value ring may have arbitrary characteristic.

```lean
TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_isSimplyLaced.{u_1, u_2}
  {t : TauCeti.DynkinType} {ht : t.Valid} {V : Type u_1} [AddCommGroup V] [_root_.Module ℚ V]
  (ρ : UniversalEnvelopingAlgebra ℚ ↥(t.lieAlgebra ht) →ₐ[ℚ] Module.End ℚ V) (M : AddSubgroup V)
  (hM :
    ∀
      u ∈
        TauCeti.UniversalEnvelopingAlgebra.kostantForm (t.lieBasis ht).rootGenerator
          (t.lieBasis ht).h,
      ∀ v ∈ M, (ρ u) v ∈ M)
  (hnil :
    ∀ (i : Fin t.rank ⊕ Fin t.rank),
      IsNilpotent (ρ ((UniversalEnvelopingAlgebra.ι ℚ) ((t.lieBasis ht).rootGenerator i))))
  (hs : t.IsSimplyLaced) {α β γ : Fin t.numRoots}
  (hγ :
    (t.simplyConnectedRootDatum ht).root γ =
      (t.simplyConnectedRootDatum ht).root α + (t.simplyConnectedRootDatum ht).root β)
  (A : CommAlgCat ℤ) (u v : ↑A) :
  ⁅(TauCeti.DynkinType.chevalleyRootSubgroup ρ M hM hnil α A) (Multiplicative.ofAdd u),
      (TauCeti.DynkinType.chevalleyRootSubgroup ρ M hM hnil β A) (Multiplicative.ofAdd v)⁆ =
    (TauCeti.DynkinType.chevalleyRootSubgroup ρ M hM hnil γ A)
      (Multiplicative.ofAdd (↑(t.structureConstant ht α β) * (u * v)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_isSimplyLaced`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/SimplyLaced.html#TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_isSimplyLaced).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_isSimplyLaced`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/SimplyLaced.html#TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_isSimplyLaced)
- [Source of `TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_isSimplyLaced` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/SimplyLaced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/SimplyLaced.lean#L60)
