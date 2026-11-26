---
declaration: module
origin: cited
lean: GaugeFieldData.covDerivFermion, GaugeFieldData.covDerivConjFermion, GaugeFieldData.covDerivBoson, GaugeFieldData.covDerivConjBoson, GaugeFieldData.covDerivFieldStrength, GaugeFieldData.covDerivFieldStrength_apply, GaugeFieldData.covDerivFieldStrength_nil, GaugeFieldData.covDerivFieldStrength_eq_iteratedCovDerivAdjoint
statement: formalized
proof: formalized
---

# The covariant derivatives in the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.CovariantDeriv`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean): 48 declarations, 41 with a docstring; 1 private, not shown.

> The iterated covariant derivatives of the matter fields and of the field strength in the local
> field algebra, with their gauge and Lorentz laws.

## i. Overview

> The covariant expressions of a gauge theory are the iterated covariant derivatives of its
> matter fields and of the field strength, built here inside the local field algebra `J(T)`
> of a field datum. For a matter species the tower is `GlobalGaugeGroup.covDerivIter`
> on the symbol family of the species, `∇_{l 0} ⋯ ∇_{l (n-1)} ψ` along an ordered tuple `l`
> of directions, with `∇_ρ F = [∂_ρ F] + A_ρ · F` through the infinitesimal action
> `repAlgebra` of the species on the value index, the conjugate components through the
> conjugate action. Zero derivatives is the undifferentiated symbol, and the ordered labels
> are kept, so nothing is identified with the multiset-indexed ordinary derivatives. For the
> gauge bosons the tower is the gauge-only `LocalGaugeFieldAlgebra.covDerivFieldStrength`,
> included through the connection factor.
>
> A jet acts on every tower through the base-point Taylor coefficient of its inverse on the
> value index alone, and the action on a matter tower factors through evaluation to the ordinary
> gauge group, since pure jets act trivially. A Lorentz transformation mixes the covariant
> slots by the columns of the Lorentz matrix and the value index contragrediently. For the
> matter towers this needs `GlobalGaugeGroup.MatterField.GaugeLorentzCompatible`, and for the
> field strength it holds unconditionally.

## ii. Key results

> - `GaugeFieldData.covDerivFermion`, `GaugeFieldData.covDerivConjFermion`,
>   `GaugeFieldData.covDerivBoson`, `GaugeFieldData.covDerivConjBoson`,
>   `GaugeFieldData.covDerivFieldStrength` : the covariant towers.
> - `GaugeFieldData.repJet_covDerivFermion` and companions : the gauge laws.
> - `GaugeFieldData.repJet_covDerivFermion_ofConstant_eval` and companions : the
>   factorization through evaluation.
> - `GaugeFieldData.repLorentzGroup_covDerivFermion` and companions : the Lorentz laws.
> - `GaugeFieldData.repLorentzGroup_covDerivFermion_mem` and companions : a Lorentz
>   transformation of a tower element lies in any subalgebra containing the tower.
> - `GaugeFieldData.commute_covDerivFieldStrength`, `GaugeFieldData.commute_covDerivBoson` : the
>   field-strength and bosonic towers are central.
> - `GaugeFieldData.covDerivFermion_anticomm_covDerivFermion` and companions : any two fermionic
>   towers anticommute.
> - `GaugeFieldData.covDerivFieldStrength_swap`,
>   `GaugeFieldData.covDerivFieldStrength_eq_of_perm_of_map_lie` : the field-strength tower is
>   antisymmetric in its covector indices, and symmetric in its derivative slots along a
>   functional vanishing on brackets.
> - `GaugeFieldData.massWeight_covDerivFermion` and companions : for a mass-weight algebra map
>   under which the gauge field has weight `2` and a species weight `c`, the covariant towers
>   are eigenvectors of the predicted weights.

## iv. References

> * None.

## A. The covariant matter towers

**`GaugeFieldData.covDerivFermion`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L97).

> The iterated covariant derivative `∇_{l 0} ⋯ ∇_{l (n-1)} ψ` of a fermionic species along
> an ordered tuple of directions, as a family over the covectors of its value space.

```lean
noncomputable def covDerivFermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivConjFermion`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L103).

> The iterated covariant derivative of the conjugate components of a fermionic species,
> through the conjugate infinitesimal action.

```lean
noncomputable def covDerivConjFermion (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivBoson`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L110).

> The iterated covariant derivative of a bosonic species.

```lean
noncomputable def covDerivBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivConjBoson`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L115).

> The iterated covariant derivative of the conjugate components of a bosonic species.

```lean
noncomputable def covDerivConjBoson (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ] T.LocalFieldAlgebra
```

## B. The included field-strength tower

**`GaugeFieldData.covDerivFieldStrength`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L129).

> The field strength and its ordered covariant derivatives `∇_l F_μν^φ`, included from
> the real gauge-only algebra through the connection factor.

```lean
noncomputable def covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivFieldStrength_apply`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L138).

```lean
lemma covDerivFieldStrength_apply (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.covDerivFieldStrength l μ ν φ
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.covDerivFieldStrength G l μ ν φ)
```

**`GaugeFieldData.covDerivFieldStrength_nil`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L145).

> Zero covariant derivatives give the included field strength.

```lean
lemma covDerivFieldStrength_nil (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.covDerivFieldStrength [] μ ν φ
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.fieldStrength G μ ν
        φ)
```

**`GaugeFieldData.covDerivFieldStrength_eq_iteratedCovDerivAdjoint`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L153).

> The included tower is the covariant tower of the gauge-field symbols of `J(T)` computed
> by the realization theory, the tower being natural along the inclusion of the connection
> factor.

```lean
lemma covDerivFieldStrength_eq_iteratedCovDerivAdjoint (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.covDerivFieldStrength l μ ν φ
      = iteratedCovDerivAdjoint T.gaugeField l
          (fieldStrength T.gaugeField μ ν) 0 φ
```

## C. The gauge laws

**`GaugeFieldData.repJet_covDerivFermion`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L194).

> The gauge law of the covariant tower of a fermionic species. A jet acts through the
> zeroth dual Taylor coefficient of its inverse on the value index alone.

```lean
lemma repJet_covDerivFermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.repJet U (T.covDerivFermion i l φ)
      = T.covDerivFermion i l (repDualCoeff (T.fermion i).repJet U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivConjFermion`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L204).

> The gauge law of the conjugate covariant tower of a fermionic species, through the
> conjugate representation.

```lean
lemma repJet_covDerivConjFermion (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repJet U (T.covDerivConjFermion i l φ)
      = T.covDerivConjFermion i l
          (repDualCoeff (FieldDerivSpace.repConj (T.fermion i).repJet) U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivBoson`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L214).

> The gauge law of the covariant tower of a bosonic species.

```lean
lemma repJet_covDerivBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.repJet U (T.covDerivBoson j l φ)
      = T.covDerivBoson j l (repDualCoeff (T.boson j).repJet U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivConjBoson`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L223).

> The gauge law of the conjugate covariant tower of a bosonic species.

```lean
lemma repJet_covDerivConjBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repJet U (T.covDerivConjBoson j l φ)
      = T.covDerivConjBoson j l
          (repDualCoeff (FieldDerivSpace.repConj (T.boson j).repJet) U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivFieldStrength`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L234).

> The gauge law of the included field-strength tower. A jet acts through the dual
> adjoint action of the value of its inverse, from the gauge-only law.

```lean
lemma repJet_covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.repJet U (T.covDerivFieldStrength l μ ν φ)
      = T.covDerivFieldStrength l μ ν ((G.adjointRep (G.evalGaugeJet
        U⁻¹)).dualMap φ)
```

**`GaugeFieldData.repJet_covDerivFermion_ofConstant_eval`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L245).

> The jet action on the covariant tower of a species factors through evaluation, since pure
> jets act trivially. A jet acts as the constant jet of its value.

```lean
lemma repJet_covDerivFermion_ofConstant_eval (i : T.FermionSpecies)
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.repJet U (T.covDerivFermion i l φ)
      = T.repJet (G.gaugeJetOfConstant (G.evalGaugeJet U))
          (T.covDerivFermion i l φ)
```

**`GaugeFieldData.repJet_covDerivConjFermion_ofConstant_eval`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L255).

```lean
lemma repJet_covDerivConjFermion_ofConstant_eval (i : T.FermionSpecies)
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repJet U (T.covDerivConjFermion i l φ)
      = T.repJet (G.gaugeJetOfConstant (G.evalGaugeJet U)) (T.covDerivConjFermion i l
        φ)
```

**`GaugeFieldData.repJet_covDerivBoson_ofConstant_eval`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L267).

```lean
lemma repJet_covDerivBoson_ofConstant_eval (j : T.BosonSpecies)
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.repJet U (T.covDerivBoson j l φ)
      = T.repJet (G.gaugeJetOfConstant (G.evalGaugeJet U)) (T.covDerivBoson j l φ)
```

**`GaugeFieldData.repJet_covDerivConjBoson_ofConstant_eval`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L276).

```lean
lemma repJet_covDerivConjBoson_ofConstant_eval (j : T.BosonSpecies)
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repJet U (T.covDerivConjBoson j l φ)
      = T.repJet (G.gaugeJetOfConstant (G.evalGaugeJet U)) (T.covDerivConjBoson j l
        φ)
```

**`GaugeFieldData.repJet_covDerivFieldStrength_ofConstant_eval`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L290).

> The jet action on the field-strength tower factors through evaluation, with no
> condition.

```lean
lemma repJet_covDerivFieldStrength_ofConstant_eval (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.repJet U (T.covDerivFieldStrength l μ ν φ)
      = T.repJet (G.gaugeJetOfConstant (G.evalGaugeJet U)) (T.covDerivFieldStrength l
        μ ν φ)
```

## D. The Lorentz laws

**`GaugeFieldData.repLorentzGroup_covDerivFermion`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L317).

> The Lorentz law of the covariant tower of a fermionic species, under
> `GlobalGaugeGroup.MatterField.GaugeLorentzCompatible` for the species. Every covariant slot
> mixes by the columns of the Lorentz matrix and the value index transforms contragrediently.

```lean
lemma repLorentzGroup_covDerivFermion (i : T.FermionSpecies)
    (hi : (T.fermion i).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.repLorentzGroup Λ (T.covDerivFermion i l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivFermion i p ((T.fermion i).repLorentz.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivConjFermion`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L328).

> The Lorentz law of the conjugate covariant tower of a fermionic species.

```lean
lemma repLorentzGroup_covDerivConjFermion (i : T.FermionSpecies)
    (hi : (T.fermion i).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repLorentzGroup Λ (T.covDerivConjFermion i l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivConjFermion i p ((T.fermion i).repLorentz.conj.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivBoson`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L339).

> The Lorentz law of the covariant tower of a bosonic species.

```lean
lemma repLorentzGroup_covDerivBoson (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.repLorentzGroup Λ (T.covDerivBoson j l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivBoson j p ((T.boson j).repLorentz.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivConjBoson`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L350).

> The Lorentz law of the conjugate covariant tower of a bosonic species.

```lean
lemma repLorentzGroup_covDerivConjBoson (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repLorentzGroup Λ (T.covDerivConjBoson j l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivConjBoson j p ((T.boson j).repLorentz.conj.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivFieldStrength`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L370).

> The Lorentz law of the field-strength tower, with no condition. Every covariant slot
> and both covector indices mix by the columns of the Lorentz matrix.

```lean
lemma repLorentzGroup_covDerivFieldStrength {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.repLorentzGroup Λ (T.covDerivFieldStrength (List.ofFn l) μ ν φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • T.covDerivFieldStrength (List.ofFn p) a b φ
```

### D.1. Transformed tower elements in a subalgebra containing the tower

> The Lorentz laws mix a tower element only with elements of the same tower, so its Lorentz
> transformation lies in any subalgebra containing the required tower elements. This says
> nothing about the other elements of such a subalgebra; the covariant field algebra and its
> sector subalgebras obtain their stability from it by generation.

**`GaugeFieldData.repLorentzGroup_covDerivFermion_mem`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L404).

> Under `GlobalGaugeGroup.MatterField.GaugeLorentzCompatible` for the species, a Lorentz
> transformation
> carries an element of the covariant tower of a fermionic species into any subalgebra
> containing the tower of that length.

```lean
lemma repLorentzGroup_covDerivFermion_mem (i : T.FermionSpecies)
    (hi : (T.fermion i).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i))
    (hS : ∀ (p : Fin n → (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℂ (T.FermionValue i)),
      T.covDerivFermion i p ψ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivFermion i l φ) ∈ S
```

**`GaugeFieldData.repLorentzGroup_covDerivConjFermion_mem`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L413).

```lean
lemma repLorentzGroup_covDerivConjFermion_mem (i : T.FermionSpecies)
    (hi : (T.fermion i).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i)))
    (hS : ∀ (p : Fin n → (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℂ (ConjModule (T.FermionValue i))),
      T.covDerivConjFermion i p ψ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivConjFermion i l φ) ∈ S
```

**`GaugeFieldData.repLorentzGroup_covDerivBoson_mem`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L422).

```lean
lemma repLorentzGroup_covDerivBoson_mem (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j))
    (hS : ∀ (p : Fin n → (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℂ (T.BosonValue j)),
      T.covDerivBoson j p ψ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivBoson j l φ) ∈ S
```

**`GaugeFieldData.repLorentzGroup_covDerivConjBoson_mem`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L431).

```lean
lemma repLorentzGroup_covDerivConjBoson_mem (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j)))
    (hS : ∀ (p : Fin n → (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℂ (ConjModule (T.BosonValue j))),
      T.covDerivConjBoson j p ψ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivConjBoson j l φ) ∈ S
```

**`GaugeFieldData.repLorentzGroup_covDerivFieldStrength_mem`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L442).

> A Lorentz transformation carries an element of the field-strength tower into any
> subalgebra containing the whole tower of its adjoint covector, with no condition.

```lean
lemma repLorentzGroup_covDerivFieldStrength_mem (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra)
    (hS : ∀ (l' : List (Fin 1 ⊕ Fin 3)) (a b : Fin 1 ⊕ Fin 3),
      T.covDerivFieldStrength l' a b φ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivFieldStrength l μ ν φ) ∈ S
```

## E. Statistics and symmetries of the towers

> The connection factor of `J(T)` is central and the bosonic generators commute with every
> generator, so the field-strength tower and the bosonic towers are central. Every term of a
> fermionic tower is a product of gauge-field symbols with a single fermionic generator, so
> two fermionic towers anticommute, whatever their species.

### E.1. Centrality of the bosonic towers

**`GaugeFieldData.gaugeField_commute`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L470).

> The gauge-field symbols are central, since they lie in the connection factor.

```lean
lemma gaugeField_commute (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ G.lieSubalgebra) (x : T.LocalFieldAlgebra) :
    Commute (T.gaugeField p μ ψ) x
```

**`GaugeFieldData.commute_covDerivFieldStrength`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L477).

> The field-strength tower is central, since it lies in the connection factor.

```lean
lemma commute_covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) (x : T.LocalFieldAlgebra) :
    Commute (T.covDerivFieldStrength l μ ν φ) x
```

**`GaugeFieldData.commute_covDerivBoson`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L485).

> The covariant tower of a bosonic species is central, since it is a polynomial in the
> gauge-field symbols and the generators of the species, all of which are central.

```lean
lemma commute_covDerivBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) (x : T.LocalFieldAlgebra) :
    Commute (T.covDerivBoson j l φ) x
```

**`GaugeFieldData.commute_covDerivConjBoson`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L497).

> The conjugate covariant tower of a bosonic species is central.

```lean
lemma commute_covDerivConjBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) (x : T.LocalFieldAlgebra) :
    Commute (T.covDerivConjBoson j l φ) x
```

### E.2. Anticommutation of the fermionic towers

**`GaugeFieldData.covDerivFermion_mem_anticommuteSubmodule`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L516).

> An element commuting with the connection factor and anticommuting with every fermionic
> generator anticommutes with every element of a fermionic tower.

```lean
lemma covDerivFermion_mem_anticommuteSubmodule (i : T.FermionSpecies) {x : T.LocalFieldAlgebra}
    (hx : ∀ (j : T.FermionSpecies) (y : FieldDerivSpace (T.fermion j)),
      x * T.ιFermion j y = -(T.ιFermion j y * x))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.covDerivFermion i l φ ∈ GaugeBoson.anticommuteSubmodule x
```

**`GaugeFieldData.covDerivConjFermion_mem_anticommuteSubmodule`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L529).

> The conjugate form of `covDerivFermion_mem_anticommuteSubmodule`.

```lean
lemma covDerivConjFermion_mem_anticommuteSubmodule (i : T.FermionSpecies)
    {x : T.LocalFieldAlgebra}
    (hx : ∀ (j : T.FermionSpecies) (y : FieldDerivSpace (T.fermion j)),
      x * T.ιFermion j y = -(T.ιFermion j y * x))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.covDerivConjFermion i l φ ∈ GaugeBoson.anticommuteSubmodule x
```

**`GaugeFieldData.ιFermion_anticomm_covDerivFermion`**, a lemma, [line 544](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L544).

> A fermionic generator anticommutes with every element of a fermionic tower.

```lean
lemma ιFermion_anticomm_covDerivFermion (j : T.FermionSpecies) (y : FieldDerivSpace (T.fermion j))
    (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.ιFermion j y * T.covDerivFermion i l φ = -(T.covDerivFermion i l φ * T.ιFermion j y)
```

**`GaugeFieldData.ιFermion_anticomm_covDerivConjFermion`**, a lemma, [line 551](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L551).

> A fermionic generator anticommutes with every element of a conjugate fermionic tower.

```lean
lemma ιFermion_anticomm_covDerivConjFermion (j : T.FermionSpecies)
    (y : FieldDerivSpace (T.fermion j)) (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.ιFermion j y * T.covDerivConjFermion i l φ
      = -(T.covDerivConjFermion i l φ * T.ιFermion j y)
```

**`GaugeFieldData.covDerivFermion_anticomm_covDerivFermion`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L559).

> Two fermionic towers anticommute, of the same species or of different ones.

```lean
lemma covDerivFermion_anticomm_covDerivFermion (i j : T.FermionSpecies) {n m : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i))
    (l' : Fin m → (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (T.FermionValue j)) :
    T.covDerivFermion i l φ * T.covDerivFermion j l' φ'
      = -(T.covDerivFermion j l' φ' * T.covDerivFermion i l φ)
```

**`GaugeFieldData.covDerivFermion_anticomm_covDerivConjFermion`**, a lemma, [line 569](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L569).

> A fermionic tower anticommutes with a conjugate fermionic tower.

```lean
lemma covDerivFermion_anticomm_covDerivConjFermion (i j : T.FermionSpecies) {n m : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i))
    (l' : Fin m → (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule (T.FermionValue j))) :
    T.covDerivFermion i l φ * T.covDerivConjFermion j l' φ'
      = -(T.covDerivConjFermion j l' φ' * T.covDerivFermion i l φ)
```

**`GaugeFieldData.covDerivConjFermion_anticomm_covDerivFermion`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L579).

> A conjugate fermionic tower anticommutes with a fermionic tower.

```lean
lemma covDerivConjFermion_anticomm_covDerivFermion (i j : T.FermionSpecies) {n m : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i)))
    (l' : Fin m → (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (T.FermionValue j)) :
    T.covDerivConjFermion i l φ * T.covDerivFermion j l' φ'
      = -(T.covDerivFermion j l' φ' * T.covDerivConjFermion i l φ)
```

**`GaugeFieldData.covDerivConjFermion_anticomm_covDerivConjFermion`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L589).

> Two conjugate fermionic towers anticommute.

```lean
lemma covDerivConjFermion_anticomm_covDerivConjFermion (i j : T.FermionSpecies) {n m : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i)))
    (l' : Fin m → (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ (ConjModule (T.FermionValue j))) :
    T.covDerivConjFermion i l φ * T.covDerivConjFermion j l' φ'
      = -(T.covDerivConjFermion j l' φ' * T.covDerivConjFermion i l φ)
```

### E.3. The symmetries of the field-strength tower

**`GaugeFieldData.covDerivFieldStrength_swap`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L607).

> The field-strength tower is antisymmetric in its two covector indices. The field strength
> is, the gauge-field symbols commuting, and the iterated covariant derivative is linear in
> the family it differentiates.

```lean
lemma covDerivFieldStrength_swap (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.covDerivFieldStrength l ν μ φ = - T.covDerivFieldStrength l μ ν φ
```

**`GaugeFieldData.covDerivFieldStrength_eq_of_perm_of_map_lie`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L623).

> Along a functional vanishing on every bracket, such as a hypercharge coordinate, the
> field-strength tower depends only on the multiset of its derivative slots, since there the
> covariant derivatives are the ordinary ones, which commute.

```lean
lemma covDerivFieldStrength_eq_of_perm_of_map_lie {φ : Module.Dual ℝ G.lieSubalgebra}
    (hφ : ∀ x y : G.lieSubalgebra, φ ⁅x, y⁆ = 0) {l l' : List (Fin 1 ⊕ Fin 3)}
    (hl : l.Perm l') (μ ν : Fin 1 ⊕ Fin 3) :
    T.covDerivFieldStrength l μ ν φ = T.covDerivFieldStrength l' μ ν φ
```

## F. Mass weights of the towers

> The statements take an algebra map `P : J(T) →ₐ[ℂ] Polynomial J(T)` under which every
> gauge-field symbol `∂_p A_μ` is an eigenvector of weight `2 * (1 + |p|)`, and under which the
> symbols of a species have weight `c + 2 * |s|`. The covariant towers are then eigenvectors of
> weight `c + 2 * n`, and the field-strength tower of weight `4 + 2 * |l|`. The mass-weight
> polynomial `GaugeFieldData.massWeightPoly`, defined in `LocalFieldAlgebra/MassWeight.lean`, is
> such a map (`GaugeFieldData.massWeightPoly_gaugeField`).

**`GaugeFieldData.gaugeField_mem_massWeightEigenspace`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L653).

> The gauge-field hypothesis in the form of the eigenspace submodules.

```lean
lemma gaugeField_mem_massWeightEigenspace (p : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ G.lieSubalgebra) :
    T.gaugeField p μ ψ ∈
      GaugeBoson.massWeightEigenspace P (2 * (1 + Multiset.card p))
```

**`GaugeFieldData.massWeight_covDerivFieldStrength`**, a lemma, [line 661](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L661).

> The mass weight of the field-strength tower is `4 + 2 * |l|`.

```lean
lemma massWeight_covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    P (T.covDerivFieldStrength l μ ν φ)
      = Polynomial.monomial (4 + 2 * l.length) (T.covDerivFieldStrength l μ ν φ)
```

**`GaugeFieldData.massWeight_covDerivFermion`**, a lemma, [line 677](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L677).

> The mass weight of the covariant tower of a fermionic species whose symbols have weight
> `c + 2 * |s|` is `c + 2 * n`.

```lean
lemma massWeight_covDerivFermion (i : T.FermionSpecies) (c : ℕ)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)),
      P (T.fermionSymbol i s φ)
        = Polynomial.monomial (c + 2 * Multiset.card s) (T.fermionSymbol i s φ))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    P (T.covDerivFermion i l φ) = Polynomial.monomial (c + 2 * n) (T.covDerivFermion i l φ)
```

**`GaugeFieldData.massWeight_covDerivConjFermion`**, a lemma, [line 693](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L693).

> The mass weight of the conjugate covariant tower of a fermionic species.

```lean
lemma massWeight_covDerivConjFermion (i : T.FermionSpecies) (c : ℕ)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))),
      P (T.conjFermionSymbol i s φ)
        = Polynomial.monomial (c + 2 * Multiset.card s) (T.conjFermionSymbol i s φ))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    P (T.covDerivConjFermion i l φ)
      = Polynomial.monomial (c + 2 * n) (T.covDerivConjFermion i l φ)
```

**`GaugeFieldData.massWeight_covDerivBoson`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L711).

> The mass weight of the covariant tower of a bosonic species whose symbols have weight
> `c + 2 * |s|` is `c + 2 * n`.

```lean
lemma massWeight_covDerivBoson (j : T.BosonSpecies) (c : ℕ)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)),
      P (T.bosonSymbol j s φ)
        = Polynomial.monomial (c + 2 * Multiset.card s) (T.bosonSymbol j s φ))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)) :
    P (T.covDerivBoson j l φ) = Polynomial.monomial (c + 2 * n) (T.covDerivBoson j l φ)
```

**`GaugeFieldData.massWeight_covDerivConjBoson`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean#L727).

> The mass weight of the conjugate covariant tower of a bosonic species.

```lean
lemma massWeight_covDerivConjBoson (j : T.BosonSpecies) (c : ℕ)
    (hF : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))),
      P (T.conjBosonSymbol j s φ)
        = Polynomial.monomial (c + 2 * Multiset.card s) (T.conjBosonSymbol j s φ))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    P (T.covDerivConjBoson j l φ)
      = Polynomial.monomial (c + 2 * n) (T.covDerivConjBoson j l φ)
```

## Depends on

- [The field strength in the local gauge field algebra](../part-01/gaugeboson-localgaugefieldalgebra-fieldstrength.md)
- [The field symbols of the local field algebra and their transformation laws](localfieldalgebra-symbols.md)

## Proof depends on

- [The Lorentz law of the covariant derivatives of a matter family](../part-06/matterfield-lorentzcovariantderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/CovariantDeriv.lean)
