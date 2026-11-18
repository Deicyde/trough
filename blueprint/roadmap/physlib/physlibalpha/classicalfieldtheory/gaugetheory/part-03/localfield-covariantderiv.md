---
declaration: module
origin: cited
lean: GaugeFieldData.covDerivFermion, GaugeFieldData.covDerivConjFermion, GaugeFieldData.covDerivBoson, GaugeFieldData.covDerivConjBoson, GaugeFieldData.covDerivFermion_zero, GaugeFieldData.covDerivConjFermion_zero, GaugeFieldData.covDerivBoson_zero, GaugeFieldData.covDerivConjBoson_zero
statement: formalized
proof: formalized
---

# The covariant derivatives in the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.CovariantDeriv`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean): 36 declarations, 23 with a docstring; 1 private, not shown.

## i. Overview

> The covariant expressions of a gauge theory are the iterated covariant derivatives of its
> matter fields and of the field strength, built here inside the local field algebra `J(T)`
> of a field datum. For a matter species the tower is `GaugeAlgebraRealization.covDerivIter`
> on the symbol family of the species: `∇_{l 0} ⋯ ∇_{l (n-1)} ψ` along an ordered tuple `l`
> of directions, with `∇_ρ F = [∂_ρ F] + A_ρ · F` through the infinitesimal action
> `repAlgebra` of the species on the value index, the conjugate components through the
> conjugate action. Zero derivatives is the undifferentiated symbol, and the ordered labels
> are kept: nothing is identified with the multiset-indexed ordinary derivatives. For the
> gauge bosons the tower is the gauge-only `LocalGaugeFieldAlgebra.covDerivFieldStrength`,
> included through the connection factor.
>
> A jet acts on every tower through the base-point Taylor coefficient of its inverse on the
> value index alone, unconditionally; under `MatterField.PureJetsActTrivially` the action on
> a matter tower factors through evaluation to the ordinary gauge group. A Lorentz
> transformation mixes the covariant slots by the columns of the Lorentz matrix and the value
> index contragrediently, under `MatterField.GaugeLorentzCompatible` for the matter towers
> and unconditionally for the field strength.

## ii. Key results

> - `GaugeFieldData.covDerivFermion`, `GaugeFieldData.covDerivConjFermion`,
>   `GaugeFieldData.covDerivBoson`, `GaugeFieldData.covDerivConjBoson`,
>   `GaugeFieldData.covDerivFieldStrength` : the covariant towers.
> - `GaugeFieldData.repJet_covDerivFermion` and companions : the gauge laws;
>   `GaugeFieldData.repJet_covDerivFermion_ofConstant_eval` and companions : the
>   factorization through evaluation.
> - `GaugeFieldData.repLorentzGroup_covDerivFermion` and companions : the Lorentz laws;
>   `GaugeFieldData.repLorentzGroup_covDerivFermion_mem` and companions : a Lorentz
>   transformation of a tower element lies in any subalgebra containing the tower.

## iv. References

> * None.

## A. The covariant matter towers

**`GaugeFieldData.covDerivFermion`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L80).

> The iterated covariant derivative `∇_{l 0} ⋯ ∇_{l (n-1)} ψ` of a fermionic species along
> an ordered tuple of directions, as a family over the covectors of its value space.

```lean
noncomputable def covDerivFermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivConjFermion`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L86).

> The iterated covariant derivative of the conjugate components of a fermionic species,
> through the conjugate infinitesimal action.

```lean
noncomputable def covDerivConjFermion (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivBoson`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L93).

> The iterated covariant derivative of a bosonic species.

```lean
noncomputable def covDerivBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivConjBoson`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L98).

> The iterated covariant derivative of the conjugate components of a bosonic species.

```lean
noncomputable def covDerivConjBoson (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivFermion_zero`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L107).

> Zero covariant derivatives: the undifferentiated symbol.

```lean
lemma covDerivFermion_zero (i : T.FermionSpecies) (l : Fin 0 → (Fin 1 ⊕ Fin 3)) :
    T.covDerivFermion i l = T.fermionSymbol i 0
```

**`GaugeFieldData.covDerivConjFermion_zero`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L110).

```lean
lemma covDerivConjFermion_zero (i : T.FermionSpecies) (l : Fin 0 → (Fin 1 ⊕ Fin 3)) :
    T.covDerivConjFermion i l = T.conjFermionSymbol i 0
```

**`GaugeFieldData.covDerivBoson_zero`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L113).

```lean
lemma covDerivBoson_zero (j : T.BosonSpecies) (l : Fin 0 → (Fin 1 ⊕ Fin 3)) :
    T.covDerivBoson j l = T.bosonSymbol j 0
```

**`GaugeFieldData.covDerivConjBoson_zero`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L116).

```lean
lemma covDerivConjBoson_zero (j : T.BosonSpecies) (l : Fin 0 → (Fin 1 ⊕ Fin 3)) :
    T.covDerivConjBoson j l = T.conjBosonSymbol j 0
```

**`GaugeFieldData.covDerivFermion_succ`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L122).

> One more covariant derivative, peeled off the front of the tuple: the derivative symbol
> `[∂_{l 0} ∇_{l'} ψ]` of the lower tower plus the derived action `A_{l 0} · ∇_{l'} ψ` of the
> gauge field on its value index, both read off the lower tower as a family.

```lean
lemma covDerivFermion_succ (i : T.FermionSpecies) {n : ℕ} (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) :
    T.covDerivFermion i l
      = covDerivIter T.gaugeRealization.A (T.fermion i).repAlgebra (T.fermionSymbol i) n
          (fun k => l k.succ) {l 0}
        + actionFamConv T.gaugeRealization.A (T.fermion i).repAlgebra (l 0)
          (covDerivIter T.gaugeRealization.A (T.fermion i).repAlgebra (T.fermionSymbol i) n
            fun k => l k.succ) 0
```

**`GaugeFieldData.covDerivConjFermion_succ`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L130).

```lean
lemma covDerivConjFermion_succ (i : T.FermionSpecies) {n : ℕ}
    (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) :
    T.covDerivConjFermion i l
      = covDerivIter T.gaugeRealization.A (LocalGaugeData.actionConj (T.fermion i).repAlgebra)
          (T.conjFermionSymbol i) n (fun k => l k.succ) {l 0}
        + actionFamConv T.gaugeRealization.A (LocalGaugeData.actionConj (T.fermion i).repAlgebra)
          (l 0) (covDerivIter T.gaugeRealization.A
            (LocalGaugeData.actionConj (T.fermion i).repAlgebra) (T.conjFermionSymbol i) n
            fun k => l k.succ) 0
```

**`GaugeFieldData.covDerivBoson_succ`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L140).

```lean
lemma covDerivBoson_succ (j : T.BosonSpecies) {n : ℕ} (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) :
    T.covDerivBoson j l
      = covDerivIter T.gaugeRealization.A (T.boson j).repAlgebra (T.bosonSymbol j) n
          (fun k => l k.succ) {l 0}
        + actionFamConv T.gaugeRealization.A (T.boson j).repAlgebra (l 0)
          (covDerivIter T.gaugeRealization.A (T.boson j).repAlgebra (T.bosonSymbol j) n
            fun k => l k.succ) 0
```

**`GaugeFieldData.covDerivConjBoson_succ`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L148).

```lean
lemma covDerivConjBoson_succ (j : T.BosonSpecies) {n : ℕ}
    (l : Fin (n + 1) → (Fin 1 ⊕ Fin 3)) :
    T.covDerivConjBoson j l
      = covDerivIter T.gaugeRealization.A (LocalGaugeData.actionConj (T.boson j).repAlgebra)
          (T.conjBosonSymbol j) n (fun k => l k.succ) {l 0}
        + actionFamConv T.gaugeRealization.A (LocalGaugeData.actionConj (T.boson j).repAlgebra)
          (l 0) (covDerivIter T.gaugeRealization.A
            (LocalGaugeData.actionConj (T.boson j).repAlgebra) (T.conjBosonSymbol j) n
            fun k => l k.succ) 0
```

## B. The included field-strength tower

**`GaugeFieldData.covDerivFieldStrength`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L168).

> The field strength and its ordered covariant derivatives `∇_l F_μν^φ`, included from
> the real gauge-only algebra through the connection factor.

```lean
noncomputable def covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] T.LocalFieldAlgebra
```

**`GaugeFieldData.covDerivFieldStrength_apply`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L177).

```lean
lemma covDerivFieldStrength_apply (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    T.covDerivFieldStrength l μ ν φ
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.covDerivFieldStrength 𝔤 l μ ν φ)
```

**`GaugeFieldData.covDerivFieldStrength_nil`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L184).

> Zero covariant derivatives: the included field strength.

```lean
lemma covDerivFieldStrength_nil (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    T.covDerivFieldStrength [] μ ν φ
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.fieldStrength 𝔤 μ ν φ)
```

**`GaugeFieldData.covDerivFieldStrength_eq_iteratedCovDerivAdjoint`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L191).

> The included tower is the covariant tower of the gauge-field symbols of `J(T)` computed
> by the realization theory, the tower being natural along the inclusion of the connection
> factor.

```lean
lemma covDerivFieldStrength_eq_iteratedCovDerivAdjoint (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    T.covDerivFieldStrength l μ ν φ
      = iteratedCovDerivAdjoint T.gaugeRealization.A l
          (fieldStrength T.gaugeRealization.A μ ν) 0 φ
```

## C. The gauge laws

**`GaugeFieldData.repJet_covDerivFermion`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L232).

> The gauge law of the covariant tower of a fermionic species: a jet acts through the
> zeroth dual Taylor coefficient of its inverse on the value index alone.

```lean
lemma repJet_covDerivFermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.repJet U (T.covDerivFermion i l φ)
      = T.covDerivFermion i l (repDualCoeff (T.fermion i).repJet U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivConjFermion`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L241).

> The gauge law of the conjugate covariant tower of a fermionic species, through the
> conjugate representation.

```lean
lemma repJet_covDerivConjFermion (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repJet U (T.covDerivConjFermion i l φ)
      = T.covDerivConjFermion i l
          (repDualCoeff (JetComponentSpace.repConj (T.fermion i).repJet) U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivBoson`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L251).

> The gauge law of the covariant tower of a bosonic species.

```lean
lemma repJet_covDerivBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.repJet U (T.covDerivBoson j l φ)
      = T.covDerivBoson j l (repDualCoeff (T.boson j).repJet U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivConjBoson`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L259).

> The gauge law of the conjugate covariant tower of a bosonic species.

```lean
lemma repJet_covDerivConjBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repJet U (T.covDerivConjBoson j l φ)
      = T.covDerivConjBoson j l
          (repDualCoeff (JetComponentSpace.repConj (T.boson j).repJet) U⁻¹ 0 φ)
```

**`GaugeFieldData.repJet_covDerivFieldStrength`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L269).

> The gauge law of the included field-strength tower: a jet acts through the dual
> adjoint action of the value of its inverse, from the gauge-only law.

```lean
lemma repJet_covDerivFieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    T.repJet U (T.covDerivFieldStrength l μ ν φ)
      = T.covDerivFieldStrength l μ ν ((jets.adjoint (jets.eval U⁻¹)).dualMap φ)
```

**`GaugeFieldData.repJet_covDerivFermion_ofConstant_eval`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L280).

> Under `MatterField.PureJetsActTrivially` for the species, the jet action on its
> covariant tower factors through evaluation: a jet acts as the constant jet of its
> value.

```lean
lemma repJet_covDerivFermion_ofConstant_eval (i : T.FermionSpecies)
    (hi : (T.fermion i).PureJetsActTrivially) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.repJet U (T.covDerivFermion i l φ)
      = T.repJet (jets.ofConstant (jets.eval U)) (T.covDerivFermion i l φ)
```

**`GaugeFieldData.repJet_covDerivConjFermion_ofConstant_eval`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L289).

```lean
lemma repJet_covDerivConjFermion_ofConstant_eval (i : T.FermionSpecies)
    (hi : (T.fermion i).PureJetsActTrivially) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repJet U (T.covDerivConjFermion i l φ)
      = T.repJet (jets.ofConstant (jets.eval U)) (T.covDerivConjFermion i l φ)
```

**`GaugeFieldData.repJet_covDerivBoson_ofConstant_eval`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L300).

```lean
lemma repJet_covDerivBoson_ofConstant_eval (j : T.BosonSpecies)
    (hj : (T.boson j).PureJetsActTrivially) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.repJet U (T.covDerivBoson j l φ)
      = T.repJet (jets.ofConstant (jets.eval U)) (T.covDerivBoson j l φ)
```

**`GaugeFieldData.repJet_covDerivConjBoson_ofConstant_eval`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L309).

```lean
lemma repJet_covDerivConjBoson_ofConstant_eval (j : T.BosonSpecies)
    (hj : (T.boson j).PureJetsActTrivially) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repJet U (T.covDerivConjBoson j l φ)
      = T.repJet (jets.ofConstant (jets.eval U)) (T.covDerivConjBoson j l φ)
```

**`GaugeFieldData.repJet_covDerivFieldStrength_ofConstant_eval`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L321).

> The jet action on the field-strength tower factors through evaluation, with no
> condition.

```lean
lemma repJet_covDerivFieldStrength_ofConstant_eval (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    T.repJet U (T.covDerivFieldStrength l μ ν φ)
      = T.repJet (jets.ofConstant (jets.eval U)) (T.covDerivFieldStrength l μ ν φ)
```

## D. The Lorentz laws

**`GaugeFieldData.repLorentzGroup_covDerivFermion`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L347).

> The Lorentz law of the covariant tower of a fermionic species, under
> `MatterField.GaugeLorentzCompatible` for the species: every covariant slot mixes by the
> columns of the Lorentz matrix and the value index transforms contragrediently.

```lean
lemma repLorentzGroup_covDerivFermion (i : T.FermionSpecies)
    (hi : (T.fermion i).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.repLorentzGroup Λ (T.covDerivFermion i l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivFermion i p ((T.fermion i).repLorentz.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivConjFermion`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L357).

> The Lorentz law of the conjugate covariant tower of a fermionic species.

```lean
lemma repLorentzGroup_covDerivConjFermion (i : T.FermionSpecies)
    (hi : (T.fermion i).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repLorentzGroup Λ (T.covDerivConjFermion i l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivConjFermion i p ((T.fermion i).repLorentz.conj.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivBoson`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L367).

> The Lorentz law of the covariant tower of a bosonic species.

```lean
lemma repLorentzGroup_covDerivBoson (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.repLorentzGroup Λ (T.covDerivBoson j l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivBoson j p ((T.boson j).repLorentz.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivConjBoson`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L377).

> The Lorentz law of the conjugate covariant tower of a bosonic species.

```lean
lemma repLorentzGroup_covDerivConjBoson (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repLorentzGroup Λ (T.covDerivConjBoson j l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          T.covDerivConjBoson j p ((T.boson j).repLorentz.conj.dual Λ φ)
```

**`GaugeFieldData.repLorentzGroup_covDerivFieldStrength`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L396).

> The Lorentz law of the field-strength tower, with no condition: every covariant slot
> and both covector indices mix by the columns of the Lorentz matrix.

```lean
lemma repLorentzGroup_covDerivFieldStrength {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    T.repLorentzGroup Λ (T.covDerivFieldStrength (List.ofFn l) μ ν φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ k, L[Λ] (p k) (l k)) •
          ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • T.covDerivFieldStrength (List.ofFn p) a b φ
```

### D.1. Transformed tower elements in a subalgebra containing the tower

> The Lorentz laws mix a tower element only with elements of the same tower, so its Lorentz
> transformation lies in any subalgebra containing the required tower elements. This says
> nothing about the other elements of such a subalgebra; the covariant field algebra and its
> sector subalgebras obtain their stability from it by generation.

**`GaugeFieldData.repLorentzGroup_covDerivFermion_mem`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L429).

> Under `MatterField.GaugeLorentzCompatible` for the species, a Lorentz transformation
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

**`GaugeFieldData.repLorentzGroup_covDerivConjFermion_mem`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L438).

```lean
lemma repLorentzGroup_covDerivConjFermion_mem (i : T.FermionSpecies)
    (hi : (T.fermion i).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i)))
    (hS : ∀ (p : Fin n → (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℂ (ConjModule (T.FermionValue i))),
      T.covDerivConjFermion i p ψ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivConjFermion i l φ) ∈ S
```

**`GaugeFieldData.repLorentzGroup_covDerivBoson_mem`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L447).

```lean
lemma repLorentzGroup_covDerivBoson_mem (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j))
    (hS : ∀ (p : Fin n → (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℂ (T.BosonValue j)),
      T.covDerivBoson j p ψ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivBoson j l φ) ∈ S
```

**`GaugeFieldData.repLorentzGroup_covDerivConjBoson_mem`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L456).

```lean
lemma repLorentzGroup_covDerivConjBoson_mem (j : T.BosonSpecies)
    (hj : (T.boson j).GaugeLorentzCompatible) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j)))
    (hS : ∀ (p : Fin n → (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℂ (ConjModule (T.BosonValue j))),
      T.covDerivConjBoson j p ψ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivConjBoson j l φ) ∈ S
```

**`GaugeFieldData.repLorentzGroup_covDerivFieldStrength_mem`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean#L467).

> A Lorentz transformation carries an element of the field-strength tower into any
> subalgebra containing the whole tower of its adjoint covector, with no condition.

```lean
lemma repLorentzGroup_covDerivFieldStrength_mem (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤)
    (hS : ∀ (l' : List (Fin 1 ⊕ Fin 3)) (a b : Fin 1 ⊕ Fin 3),
      T.covDerivFieldStrength l' a b φ ∈ S) :
    T.repLorentzGroup Λ (T.covDerivFieldStrength l μ ν φ) ∈ S
```

## Depends on

- [The field strength in the local gauge field algebra](../part-01/gaugeboson-localgauge-fieldstrength.md)
- [The field symbols of the local field algebra and their transformation laws](../part-04/localfield-transformsin.md)

## Proof depends on

- [The Lorentz law of the covariant derivatives of a matter family](../part-05/matterfield-lorentzcovariantderiv.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/CovariantDeriv.lean)
