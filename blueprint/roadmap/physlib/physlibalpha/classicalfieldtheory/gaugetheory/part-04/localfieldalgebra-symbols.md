---
declaration: module
origin: cited
lean: GaugeFieldData.gaugeField, GaugeFieldData.gaugeField_apply, GaugeFieldData.transformsAsGaugeField_gaugeField, GaugeFieldData.lorentzTransformsAsGaugeField_gaugeField, GaugeFieldData.fermionSymbolMap, GaugeFieldData.conjFermionSymbolMap, GaugeFieldData.bosonSymbolMap, GaugeFieldData.conjBosonSymbolMap
statement: formalized
proof: formalized
---

# The field symbols of the local field algebra and their transformation laws

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.Symbols`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean): 32 declarations, 27 with a docstring; 2 private, not shown.

> The derivative symbols of the matter species as families in the local field algebra, with their
> gauge and Lorentz laws.

## i. Overview

> The generators of the local field algebra `J(T)` of a field datum are the derivative
> symbols of its species. These are `∂_s ψ^φ`, indexed by a derivative multiset `s` and a covector `φ`
> of the value space, the conjugate symbols `∂_s ψ̄^φ`, indexed by a covector of the
> conjugate value space, and the gauge-field symbols `∂_s A_μ^φ` of the connection factor.
> This file packages the matter symbols of each species as families over `s` and proves
> their two transformation laws, the Leibniz convolution law for the jet gauge action and
> `IsLorentzDerivTransforms` for the Lorentz action. The gauge-field symbols of `J(T)` are those
> of the gauge-boson jet algebra carried in by the inclusion of the connection factor,
> `GaugeFieldData.gaugeField`. The inclusion intertwines both actions, so they transform
> as a gauge field under both, and the covariant derivative theory of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.CovariantDeriv`
> applies inside `J(T)`.

## ii. Key results

> - `GaugeFieldData.gaugeField` : the gauge-field symbols of `J(T)`.
> - `GaugeFieldData.transformsAsGaugeField_gaugeField`,
>   `GaugeFieldData.lorentzTransformsAsGaugeField_gaugeField` : their gauge and Lorentz laws.
> - `GaugeFieldData.fermionSymbol`, `GaugeFieldData.conjFermionSymbol`,
>   `GaugeFieldData.bosonSymbol`, `GaugeFieldData.conjBosonSymbol` : the matter symbols.
> - `GaugeFieldData.repJet_fermionSymbol`,
>   `GaugeFieldData.isLorentzDerivTransforms_fermionSymbol` and companions : their gauge
>   and Lorentz laws.

## iv. References

> * None.

## A. The gauge-field symbols of the connection factor

**`GaugeFieldData.gaugeField`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L77).

> The gauge-field symbols `∂_s A_μ^φ` of `J(T)`, the symbols of the gauge-boson jet algebra
> carried in by the inclusion of the connection factor. The real structure on `J(T)` is the
> one restricted from its complex structure, as for every family of symbols in a complex
> algebra.

```lean
noncomputable def gaugeField
```

**`GaugeFieldData.gaugeField_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L83).

```lean
lemma gaugeField_apply (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.gaugeField s μ φ = T.includeConnection (LocalGaugeFieldAlgebra.gaugeField G s μ φ)
```

**`GaugeFieldData.transformsAsGaugeField_gaugeField`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L89).

> The gauge-field symbols of `J(T)` transform as a gauge field under the jet gauge group,
> since the inclusion of the connection factor intertwines the two actions.

```lean
lemma transformsAsGaugeField_gaugeField :
    GaugeBoson.TransformsAsGaugeField G T.repJet T.gaugeField
```

**`GaugeFieldData.lorentzTransformsAsGaugeField_gaugeField`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L95).

> The gauge-field symbols of `J(T)` transform as a gauge field under the Lorentz group.

```lean
lemma lorentzTransformsAsGaugeField_gaugeField :
    GaugeBoson.LorentzTransformsAsGaugeField T.repLorentzGroup T.gaugeField
```

## B. The matter symbol families

**`GaugeFieldData.fermionSymbolMap`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L110).

> The unconjugated symbols of a fermionic species, as a linear map on the unconjugated
> half of its component space.

```lean
noncomputable def fermionSymbolMap (i : T.FermionSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjFermionSymbolMap`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L116).

> The conjugate symbols of a fermionic species, as a linear map on the conjugate half of
> its component space.

```lean
noncomputable def conjFermionSymbolMap (i : T.FermionSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ]
      T.LocalFieldAlgebra
```

**`GaugeFieldData.bosonSymbolMap`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L123).

> The unconjugated symbols of a bosonic species, as a linear map on the unconjugated
> half of its component space.

```lean
noncomputable def bosonSymbolMap (j : T.BosonSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjBosonSymbolMap`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L129).

> The conjugate symbols of a bosonic species, as a linear map on the conjugate half of
> its component space.

```lean
noncomputable def conjBosonSymbolMap (j : T.BosonSpecies) :
    SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ]
      T.LocalFieldAlgebra
```

**`GaugeFieldData.fermionSymbol`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L136).

> The derivative symbols `∂_s ψ^φ` of a fermionic species, the family over the
> derivative multiset `s`, indexed by the covectors of the value space.

```lean
noncomputable def fermionSymbol (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjFermionSymbol`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L142).

> The conjugate derivative symbols `∂_s ψ̄^φ` of a fermionic species, indexed by the
> covectors of the conjugate value space.

```lean
noncomputable def conjFermionSymbol (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.bosonSymbol`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L147).

> The derivative symbols `∂_s φ^χ` of a bosonic species.

```lean
noncomputable def bosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.conjBosonSymbol`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L152).

> The conjugate derivative symbols `∂_s φ̄^χ` of a bosonic species.

```lean
noncomputable def conjBosonSymbol (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.fermionSymbol_apply`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L158).

```lean
lemma fermionSymbol_apply (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.fermionSymbol i s φ = T.ιFermion i (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0)
```

**`GaugeFieldData.conjFermionSymbol_apply`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L162).

```lean
lemma conjFermionSymbol_apply (i : T.FermionSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.conjFermionSymbol i s φ = T.ιFermion i (0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
```

**`GaugeFieldData.bosonSymbol_apply`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L166).

```lean
lemma bosonSymbol_apply (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.bosonSymbol j s φ = T.ιBoson j (SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0)
```

**`GaugeFieldData.conjBosonSymbol_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L170).

```lean
lemma conjBosonSymbol_apply (j : T.BosonSpecies) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.conjBosonSymbol j s φ = T.ιBoson j (0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ)
```

## C. The jet gauge transformation of the matter symbols

> Each symbol map intertwines the jet gauge action on `J(T)` with `FieldDerivSpace.repDual`
> on its half of the component space, and the law of the symbols is
> `FieldDerivSpace.repDual_basis_tmul` pushed through the symbol map.

**`GaugeFieldData.repJet_fermionSymbolMap`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L206).

> The unconjugated fermionic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_fermionSymbolMap (i : T.FermionSpecies) (U : G.gaugeJetGroup)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.FermionValue i)) :
    T.repJet U (T.fermionSymbolMap i x)
      = T.fermionSymbolMap i
        (FieldDerivSpace.repDual (T.fermion i).repJet (T.fermion i).repJet_smul U x)
```

**`GaugeFieldData.repJet_conjFermionSymbolMap`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L216).

> The conjugate fermionic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_conjFermionSymbolMap (i : T.FermionSpecies) (U : G.gaugeJetGroup)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repJet U (T.conjFermionSymbolMap i x)
      = T.conjFermionSymbolMap i
        (FieldDerivSpace.repDual (FieldDerivSpace.repConj (T.fermion i).repJet)
          (FieldDerivSpace.repConj_smul_comm (T.fermion i).repJet_smul) U x)
```

**`GaugeFieldData.repJet_bosonSymbolMap`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L227).

> The unconjugated bosonic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_bosonSymbolMap (j : T.BosonSpecies) (U : G.gaugeJetGroup)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.BosonValue j)) :
    T.repJet U (T.bosonSymbolMap j x)
      = T.bosonSymbolMap j
        (FieldDerivSpace.repDual (T.boson j).repJet (T.boson j).repJet_smul U x)
```

**`GaugeFieldData.repJet_conjBosonSymbolMap`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L237).

> The conjugate bosonic symbol map intertwines the jet gauge actions.

```lean
lemma repJet_conjBosonSymbolMap (j : T.BosonSpecies) (U : G.gaugeJetGroup)
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repJet U (T.conjBosonSymbolMap j x)
      = T.conjBosonSymbolMap j
        (FieldDerivSpace.repDual (FieldDerivSpace.repConj (T.boson j).repJet)
          (FieldDerivSpace.repConj_smul_comm (T.boson j).repJet_smul) U x)
```

**`GaugeFieldData.repJet_fermionSymbol`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L250).

> The symbols of a fermionic species transform in the jet gauge representation of the
> species, each derivative symbol by the Leibniz convolution of the dual base-point
> coefficients against the lower symbols.

```lean
lemma repJet_fermionSymbol (i : T.FermionSpecies) (U : G.gaugeJetGroup)
    (φ : Module.Dual ℂ (T.FermionValue i)) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    T.repJet U (T.fermionSymbol i s φ) =
      (s.antidiagonal.map fun p =>
        T.fermionSymbol i p.2 (repDualCoeff (T.fermion i).repJet U⁻¹ p.1 φ)).sum
```

**`GaugeFieldData.repJet_conjFermionSymbol`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L259).

> The conjugate symbols of a fermionic species transform in the conjugate of the jet
> gauge representation of the species.

```lean
lemma repJet_conjFermionSymbol (i : T.FermionSpecies) (U : G.gaugeJetGroup)
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    T.repJet U (T.conjFermionSymbol i s φ) =
      (s.antidiagonal.map fun p =>
        T.conjFermionSymbol i p.2
          (repDualCoeff (FieldDerivSpace.repConj (T.fermion i).repJet) U⁻¹ p.1 φ)).sum
```

**`GaugeFieldData.repJet_bosonSymbol`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L269).

> The symbols of a bosonic species transform in the jet gauge representation of the
> species.

```lean
lemma repJet_bosonSymbol (j : T.BosonSpecies) (U : G.gaugeJetGroup)
    (φ : Module.Dual ℂ (T.BosonValue j)) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    T.repJet U (T.bosonSymbol j s φ) =
      (s.antidiagonal.map fun p =>
        T.bosonSymbol j p.2 (repDualCoeff (T.boson j).repJet U⁻¹ p.1 φ)).sum
```

**`GaugeFieldData.repJet_conjBosonSymbol`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L278).

> The conjugate symbols of a bosonic species transform in the conjugate of the jet gauge
> representation of the species.

```lean
lemma repJet_conjBosonSymbol (j : T.BosonSpecies) (U : G.gaugeJetGroup)
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    T.repJet U (T.conjBosonSymbol j s φ) =
      (s.antidiagonal.map fun p =>
        T.conjBosonSymbol j p.2
          (repDualCoeff (FieldDerivSpace.repConj (T.boson j).repJet) U⁻¹ p.1 φ)).sum
```

## D. The Lorentz transformation of the matter symbols

> Each symbol map intertwines the Lorentz action on `J(T)` with the tensor product of the
> action on derivative labels and the contragredient action on the value index, and the law
> of the symbols is that of the derivative monomials,
> `SpaceTimeDerivAlgebraℂ.repLorentzGroup_basis_ofFn`.

**`GaugeFieldData.repLorentzGroup_fermionSymbolMap`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L322).

> The unconjugated fermionic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_fermionSymbolMap (i : T.FermionSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.FermionValue i)) :
    T.repLorentzGroup Λ (T.fermionSymbolMap i x)
      = T.fermionSymbolMap i
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod (T.fermion i).repLorentz.dual) Λ x)
```

**`GaugeFieldData.repLorentzGroup_conjFermionSymbolMap`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L332).

> The conjugate fermionic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_conjFermionSymbolMap (i : T.FermionSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repLorentzGroup Λ (T.conjFermionSymbolMap i x)
      = T.conjFermionSymbolMap i
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod
            (T.fermion i).repLorentz.conj.dual) Λ x)
```

**`GaugeFieldData.repLorentzGroup_bosonSymbolMap`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L344).

> The unconjugated bosonic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_bosonSymbolMap (j : T.BosonSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (T.BosonValue j)) :
    T.repLorentzGroup Λ (T.bosonSymbolMap j x)
      = T.bosonSymbolMap j
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod (T.boson j).repLorentz.dual) Λ x)
```

**`GaugeFieldData.repLorentzGroup_conjBosonSymbolMap`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L354).

> The conjugate bosonic symbol map intertwines the Lorentz actions.

```lean
lemma repLorentzGroup_conjBosonSymbolMap (j : T.BosonSpecies) (Λ : SL(2,ℂ))
    (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repLorentzGroup Λ (T.conjBosonSymbolMap j x)
      = T.conjBosonSymbolMap j
        ((SpaceTimeDerivAlgebraℂ.repLorentzGroup.tprod (T.boson j).repLorentz.conj.dual) Λ x)
```

**`GaugeFieldData.isLorentzDerivTransforms_fermionSymbol`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L366).

> The symbols of a fermionic species transform as the derivative symbols of a field in
> the Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_fermionSymbol (i : T.FermionSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.fermion i).repLorentz (T.fermionSymbol i)
```

**`GaugeFieldData.isLorentzDerivTransforms_conjFermionSymbol`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L373).

> The conjugate symbols of a fermionic species transform as the derivative symbols of a
> field in the conjugate of the Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_conjFermionSymbol (i : T.FermionSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.fermion i).repLorentz.conj (T.conjFermionSymbol i)
```

**`GaugeFieldData.isLorentzDerivTransforms_bosonSymbol`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L380).

> The symbols of a bosonic species transform as the derivative symbols of a field in the
> Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_bosonSymbol (j : T.BosonSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.boson j).repLorentz (T.bosonSymbol j)
```

**`GaugeFieldData.isLorentzDerivTransforms_conjBosonSymbol`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean#L387).

> The conjugate symbols of a bosonic species transform as the derivative symbols of a
> field in the conjugate of the Lorentz representation of the species.

```lean
lemma isLorentzDerivTransforms_conjBosonSymbol (j : T.BosonSpecies) :
    IsLorentzDerivTransforms (A := T.LocalFieldAlgebra) T.repLorentzGroup
      (T.boson j).repLorentz.conj (T.conjBosonSymbol j)
```

## Depends on

- [The gauge-field symbols of the jet algebra and their laws](../part-01/gaugeboson-localgaugefieldalgebra-gaugefield.md)
- [The jet gauge action on the local field algebra](localfieldalgebra-gaugeaction.md)
- [The Lorentz action on the local field algebra](localfieldalgebra-lorentzaction.md)

## Proof depends on

- [The transformation law of a derivative symbol](../part-07/matterfield-fieldderivspace-jetcoeffat.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Symbols.lean)
