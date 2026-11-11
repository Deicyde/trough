---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add
statement: formalized
proof: formalized
---

# The two-factor Chevalley commutator formula (`TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add`)

If `γ = α + β` and `δ = 2α + β` are roots
while `3α + β` and `α + 2β` are not, then over every commutative ring of values

```text
⁅x_α(u), x_β(v)⁆ = x_γ(N_{α,β} u v) x_δ(M u² v),    M = N_{α,β} N_{α,γ} / 2,
```

where `M` is the integer with `(ad e_α)² e_β / 2 = M e_δ`; the division is exact. In the types
`B`, `C` and `F₄` this covers every pair `α`, `β` with `2α + β` a root.

```lean
TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add.{u_1, u_2}
  {t : TauCeti.DynkinType} {ht : t.Valid} {α β γ δ : Fin t.numRoots} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℚ V] (ρ : UniversalEnvelopingAlgebra ℚ ↥(t.lieAlgebra ht) →ₐ[ℚ] Module.End ℚ V)
  (M : AddSubgroup V)
  (hM :
    ∀
      u ∈
        TauCeti.UniversalEnvelopingAlgebra.kostantForm (t.lieBasis ht).rootGenerator
          (t.lieBasis ht).h,
      ∀ v ∈ M, (ρ u) v ∈ M)
  (hnil :
    ∀ (i : Fin t.rank ⊕ Fin t.rank),
      IsNilpotent (ρ ((UniversalEnvelopingAlgebra.ι ℚ) ((t.lieBasis ht).rootGenerator i))))
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
  (A : CommAlgCat ℤ) (u v : ↑A) :
  ⁅(TauCeti.DynkinType.chevalleyRootSubgroup ρ M hM hnil α A) (Multiplicative.ofAdd u),
      (TauCeti.DynkinType.chevalleyRootSubgroup ρ M hM hnil β A) (Multiplicative.ofAdd v)⁆ =
    (TauCeti.DynkinType.chevalleyRootSubgroup ρ M hM hnil γ A)
        (Multiplicative.ofAdd (↑(t.structureConstant ht α β) * (u * v))) *
      (TauCeti.DynkinType.chevalleyRootSubgroup ρ M hM hnil δ A)
        (Multiplicative.ofAdd
          (↑(t.structureConstant ht α β * t.structureConstant ht α γ / 2) * (u ^ 2 * v)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chevalley's theorem on structure constants](chevalleys-theorem-on-structure-constants.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/Basic.html#TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/Basic.html#TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add)
- [Source of `TauCeti.DynkinType.commutatorElement_chevalleyRootSubgroup_of_root_eq_two_nsmul_add` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/Root/Commutator/Basic.lean#L178)
