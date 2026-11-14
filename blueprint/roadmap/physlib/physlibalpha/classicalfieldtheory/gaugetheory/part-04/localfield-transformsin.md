---
declaration: module
origin: cited
lean: GaugeFieldData.gaugeRealization, GaugeFieldData.gaugeRealization_toAlgHom, GaugeFieldData.gaugeRealization_A, GaugeFieldData.fermionSymbolMap, GaugeFieldData.conjFermionSymbolMap, GaugeFieldData.bosonSymbolMap, GaugeFieldData.conjBosonSymbolMap, GaugeFieldData.fermionSymbol
statement: formalized
proof: formalized
---

# The field symbols of the local field algebra and their transformation laws

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.TransformsIn`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean): 31 declarations, 25 with a docstring; 2 private, not shown.

## i. Overview

> The generators of the local field algebra `J(T)` of a field datum are the derivative
> symbols of its species: `∂_s ψ^φ`, indexed by a derivative multiset `s` and a covector `φ`
> of the value space, the conjugate symbols `∂_s ψ̄^φ`, indexed by a covector of the
> conjugate value space, and the gauge-field symbols `∂_s A_μ^φ` of the connection factor.
> This file packages the matter symbols of each species as families over `s` and proves
> their two transformation laws, `LocalGaugeData.TransformsIn` for the jet gauge action and
> `IsLorentzDerivTransforms` for the Lorentz action, and packages the connection factor as
> a realization of the gauge bosons in `J(T)`, so that the covariant derivative theory of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.CovariantDeriv` applies inside `J(T)`.

## ii. Key results

> - `GaugeFieldData.gaugeRealization` : the connection factor as a realization of the gauge
>   bosons in `J(T)`.
> - `GaugeFieldData.fermionSymbol`, `GaugeFieldData.conjFermionSymbol`,
>   `GaugeFieldData.bosonSymbol`, `GaugeFieldData.conjBosonSymbol` : the matter symbols.
> - `GaugeFieldData.transformsIn_fermionSymbol`,
>   `GaugeFieldData.isLorentzDerivTransforms_fermionSymbol` and companions : their gauge
>   and Lorentz laws.

## iv. References

> * None.

## A. The connection factor as a realization of the gauge bosons

**`GaugeFieldData.gaugeRealization`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L68).

> The connection factor as a realization of the gauge bosons in `J(T)`: the inclusion of
> the complexified gauge-only algebra, equivariant for both actions, with the included
> gauge-field symbols as its symbols.

```lean
noncomputable def gaugeRealization :
    GaugeAlgebraRealization jets T.LocalFieldAlgebra T.repJet T.repLorentzGroup
```

**`GaugeFieldData.gaugeRealization_toAlgHom`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L81).

```lean
lemma gaugeRealization_toAlgHom : T.gaugeRealization.toAlgHom = T.includeConnection
```

**`GaugeFieldData.gaugeRealization_A`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L83).

```lean
lemma gaugeRealization_A (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    T.gaugeRealization.A s μ φ
      = T.includeConnection (LocalGaugeFieldAlgebra.gaugeField 𝔤 s μ φ)
```

## B. The matter symbol families

**`GaugeFieldData.fermionSymbolMap`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L98).

> The unconjugated symbols of a fermionic species, as a linear map on the unconjugated
> half of its component space.

```lean
noncomputable def fermionSymbolMap (i : T.FermionSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjFermionSymbolMap`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L104).

> The conjugate symbols of a fermionic species, as a linear map on the conjugate half of
> its component space.

```lean
noncomputable def conjFermionSymbolMap (i : T.FermionSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ]
      T.LocalFieldAlgebra
```

**`GaugeFieldData.bosonSymbolMap`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L111).

> The unconjugated symbols of a bosonic species, as a linear map on the unconjugated
> half of its component space.

```lean
noncomputable def bosonSymbolMap (j : T.BosonSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjBosonSymbolMap`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L117).

> The conjugate symbols of a bosonic species, as a linear map on the conjugate half of
> its component space.

```lean
noncomputable def conjBosonSymbolMap (j : T.BosonSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ]
      T.LocalFieldAlgebra
```

**`GaugeFieldData.fermionSymbol`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L124).

> The derivative symbols `∂_s ψ^φ` of a fermionic species: the family over the
> derivative multiset `s`, indexed by the covectors of the value space.

```lean
noncomputable def fermionSymbol (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjFermionSymbol`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L130).

> The conjugate derivative symbols `∂_s ψ̄^φ` of a fermionic species, indexed by the
> covectors of the conjugate value space.

```lean
noncomputable def conjFermionSymbol (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.bosonSymbol`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L135).

> The derivative symbols `∂_s φ^χ` of a bosonic species.

```lean
noncomputable def bosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjBosonSymbol`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L140).

> The conjugate derivative symbols `∂_s φ̄^χ` of a bosonic species.

```lean
noncomputable def conjBosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.fermionSymbol_apply`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L146).

```lean
lemma fermionSymbol_apply (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.fermionSymbol i s φ = T.ιFermion i (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0)
```

**`GaugeFieldData.conjFermionSymbol_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L150).

```lean
lemma conjFermionSymbol_apply (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.conjFermionSymbol i s φ = T.ιFermion i (0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
```

**`GaugeFieldData.bosonSymbol_apply`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L154).

```lean
lemma bosonSymbol_apply (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.bosonSymbol j s φ = T.ιBoson j (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0)
```

**`GaugeFieldData.conjBosonSymbol_apply`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L158).

```lean
lemma conjBosonSymbol_apply (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.conjBosonSymbol j s φ = T.ιBoson j (0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
```

## C. The jet gauge transformation of the matter symbols

> Each symbol map intertwines the jet gauge action on `J(T)` with `JetComponentSpace.repDual`
> on its half of the component space, and the law of the symbols is
> `JetComponentSpace.repDual_basis_tmul` pushed through the symbol map.

**`GaugeFieldData.repJet_fermionSymbolMap`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L192).

> The unconjugated fermionic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_fermionSymbolMap (i : T.FermionSpecies) (U : GJ)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.FermionValue i)) :
    T.repJet U (T.fermionSymbolMap i x)
      = T.fermionSymbolMap i
        (JetComponentSpace.repDual (T.fermion i).repJet (T.fermion i).repJet_smul U x)
```

**`GaugeFieldData.repJet_conjFermionSymbolMap`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L202).

> The conjugate fermionic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_conjFermionSymbolMap (i : T.FermionSpecies) (U : GJ)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repJet U (T.conjFermionSymbolMap i x)
      = T.conjFermionSymbolMap i
        (JetComponentSpace.repDual (JetComponentSpace.repConj (T.fermion i).repJet)
          (JetComponentSpace.repConj_smul_comm (T.fermion i).repJet_smul) U x)
```

**`GaugeFieldData.repJet_bosonSymbolMap`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L213).

> The unconjugated bosonic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_bosonSymbolMap (j : T.BosonSpecies) (U : GJ)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.BosonValue j)) :
    T.repJet U (T.bosonSymbolMap j x)
      = T.bosonSymbolMap j
        (JetComponentSpace.repDual (T.boson j).repJet (T.boson j).repJet_smul U x)
```

**`GaugeFieldData.repJet_conjBosonSymbolMap`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L223).

> The conjugate bosonic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_conjBosonSymbolMap (j : T.BosonSpecies) (U : GJ)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repJet U (T.conjBosonSymbolMap j x)
      = T.conjBosonSymbolMap j
        (JetComponentSpace.repDual (JetComponentSpace.repConj (T.boson j).repJet)
          (JetComponentSpace.repConj_smul_comm (T.boson j).repJet_smul) U x)
```

**`GaugeFieldData.transformsIn_fermionSymbol`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L235).

> The symbols of a fermionic species transform in the jet gauge representation of the
> species.

```lean
lemma transformsIn_fermionSymbol (i : T.FermionSpecies) :
    LocalGaugeData.TransformsIn (B := T.LocalFieldAlgebra) T.repJet (T.fermion i).repJet
      (T.fermionSymbol i)
```

**`GaugeFieldData.transformsIn_conjFermionSymbol`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L242).

> The conjugate symbols of a fermionic species transform in the conjugate of the jet
> gauge representation of the species.

```lean
lemma transformsIn_conjFermionSymbol (i : T.FermionSpecies) :
    LocalGaugeData.TransformsIn (B := T.LocalFieldAlgebra) T.repJet
      (JetComponentSpace.repConj (T.fermion i).repJet) (T.conjFermionSymbol i)
```

**`GaugeFieldData.transformsIn_bosonSymbol`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L249).

> The symbols of a bosonic species transform in the jet gauge representation of the
> species.

```lean
lemma transformsIn_bosonSymbol (j : T.BosonSpecies) :
    LocalGaugeData.TransformsIn (B := T.LocalFieldAlgebra) T.repJet (T.boson j).repJet
      (T.bosonSymbol j)
```

**`GaugeFieldData.transformsIn_conjBosonSymbol`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L256).

> The conjugate symbols of a bosonic species transform in the conjugate of the jet gauge
> representation of the species.

```lean
lemma transformsIn_conjBosonSymbol (j : T.BosonSpecies) :
    LocalGaugeData.TransformsIn (B := T.LocalFieldAlgebra) T.repJet
      (JetComponentSpace.repConj (T.boson j).repJet) (T.conjBosonSymbol j)
```

## D. The Lorentz transformation of the matter symbols

> Each symbol map intertwines the Lorentz action on `J(T)` with the tensor product of the
> action on derivative labels and the contragredient action on the value index, and the law
> of the symbols is that of the derivative monomials,
> `SpaceTimeDerivAlgebraℂ.repLorentzGroup_basis_ofFn`.

**`GaugeFieldData.repLorentzGroup_fermionSymbolMap`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L297).

> The unconjugated fermionic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_fermionSymbolMap (i : T.FermionSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.FermionValue i)) :
    T.repLorentzGroup Λ (T.fermionSymbolMap i x)
      = T.fermionSymbolMap i
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod (T.fermion i).repLorentz.dual) Λ x)
```

**`GaugeFieldData.repLorentzGroup_conjFermionSymbolMap`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L307).

> The conjugate fermionic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_conjFermionSymbolMap (i : T.FermionSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repLorentzGroup Λ (T.conjFermionSymbolMap i x)
      = T.conjFermionSymbolMap i
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod
            (T.fermion i).repLorentz.conj.dual) Λ x)
```

**`GaugeFieldData.repLorentzGroup_bosonSymbolMap`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L319).

> The unconjugated bosonic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_bosonSymbolMap (j : T.BosonSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.BosonValue j)) :
    T.repLorentzGroup Λ (T.bosonSymbolMap j x)
      = T.bosonSymbolMap j
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod (T.boson j).repLorentz.dual) Λ x)
```

**`GaugeFieldData.repLorentzGroup_conjBosonSymbolMap`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L329).

> The conjugate bosonic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_conjBosonSymbolMap (j : T.BosonSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repLorentzGroup Λ (T.conjBosonSymbolMap j x)
      = T.conjBosonSymbolMap j
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod (T.boson j).repLorentz.conj.dual) Λ x)
```

**`GaugeFieldData.isLorentzDerivTransforms_fermionSymbol`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L341).

> The symbols of a fermionic species transform as the derivative symbols of a field in
> the Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_fermionSymbol (i : T.FermionSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.fermion i).repLorentz (T.fermionSymbol i)
```

**`GaugeFieldData.isLorentzDerivTransforms_conjFermionSymbol`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L348).

> The conjugate symbols of a fermionic species transform as the derivative symbols of a
> field in the conjugate of the Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_conjFermionSymbol (i : T.FermionSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.fermion i).repLorentz.conj (T.conjFermionSymbol i)
```

**`GaugeFieldData.isLorentzDerivTransforms_bosonSymbol`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L355).

> The symbols of a bosonic species transform as the derivative symbols of a field in the
> Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_bosonSymbol (j : T.BosonSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.boson j).repLorentz (T.bosonSymbol j)
```

**`GaugeFieldData.isLorentzDerivTransforms_conjBosonSymbol`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean#L362).

> The conjugate symbols of a bosonic species transform as the derivative symbols of a
> field in the conjugate of the Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_conjBosonSymbol (j : T.BosonSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.boson j).repLorentz.conj (T.conjBosonSymbol j)
```

## Depends on

- [The jet gauge action on the local field algebra](../part-03/localfield-gaugeaction.md)
- [The Lorentz action on the local field algebra](../part-03/localfield-lorentzaction.md)

## Proof depends on

- [The transformation law of a derivative symbol](../part-06/matterfield-jetcomponent-transformsin.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/TransformsIn.lean)
