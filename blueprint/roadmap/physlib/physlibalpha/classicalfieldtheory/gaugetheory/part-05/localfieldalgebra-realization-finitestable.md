---
declaration: module
origin: cited
lean: GlobalGaugeGroup.MatterField.repDualCoeff_gaugeJetOfConstant_inv, GlobalGaugeGroup.MatterField.repDualCoeff_repConj_gaugeJetOfConstant_inv, GlobalGaugeGroup.MatterField.continuousCoeff_rep, GlobalGaugeGroup.MatterField.continuousCoeff_repDualCoeff, GlobalGaugeGroup.MatterField.continuousCoeff_repDualCoeff_repConj, GlobalGaugeGroup.MatterField.LorentzContinuous.continuousCoeff_dual, GlobalGaugeGroup.MatterField.LorentzContinuous.continuousCoeff_conj_dual, GlobalGaugeGroup.MatterField.GaugeLorentzCommute.repDualCoeff_dual
statement: formalized
proof: formalized
---

# Finite-dimensional stable subspaces of the covariant field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.Realization.FiniteStable`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean): 33 declarations, 21 with a docstring.

> Every covariant expression lies in a finite-dimensional subspace stable under the gauge and
> Lorentz groups, on which both act continuously.

## i. Overview

> The Haar average over the gauge group and the Casimir projection for the Lorentz group act on
> finite-dimensional spaces with continuous actions. To use them on the covariant field algebra,
> every covariant expression must lie in such a space. This file constructs one, stable under the
> joint action of the ordinary gauge group and the Lorentz group.
>
> Two conditions are needed. The Lorentz representation of every species must be continuous,
> `GaugeFieldData.LorentzContinuous`, and the gauge and Lorentz representations of every species
> must commute, `GaugeFieldData.GaugeLorentzCommute`. The second makes the two actions on the
> covariant field algebra commute, so that together they form one representation
> `repGaugeLorentz` of `G × SL(2,ℂ)`.
>
> The construction is by generation, through the continuous families of
> `PhyslibAlpha.Mathematics.RepresentationTheory.Reynolds.ContinuousFamily`. A finite family of
> vectors is a continuous family when each group element maps every vector of the family to a
> combination of the family with coefficients depending continuously on the group element. The
> span of a continuous family for both groups is a finite-dimensional subrepresentation on which
> both groups act continuously. Each covariant generator lies in such a span.
>
> - The field strength `∇_l F_μν^φ` with `l` of fixed length, over a basis of the adjoint index
>   `φ`. The gauge group acts on `φ` through the adjoint representation, and the Lorentz group
>   mixes the directions and the two indices by the Lorentz matrix.
> - The covariant tower `∇_l ψ^φ` of a species with `l` of fixed length, over a basis of the value
>   index `φ`. The gauge group acts on `φ` through the gauge representation, and the Lorentz group
>   mixes the directions by the Lorentz matrix and acts on `φ` through the Lorentz representation.
>   The same holds for the conjugate towers.
>
> The scalars span a continuous family, sums of elements lie in the span of the union of their
> families, and products in the span of the products of their families, since both groups act by
> algebra maps. So every element of the covariant field algebra lies in the span of a continuous
> family.

## ii. Key results

> - `GaugeFieldData.LocalCovFieldAlgebra.commute_repValue_repLorentzGroup` : the gauge and Lorentz
>   actions on the covariant field algebra commute.
> - `GaugeFieldData.LocalCovFieldAlgebra.repGaugeLorentz` : the joint action of `G × SL(2,ℂ)`.
> - `GaugeFieldData.LocalCovFieldAlgebra.exists_subrepresentation` : every covariant expression
>   lies in a finite-dimensional subrepresentation of the joint action on which both groups act
>   with continuous matrix coefficients.
> - `GaugeFieldData.LocalCovFieldAlgebra.finiteSubrep` : a chosen such subrepresentation.

## iv. References

> * None.

## A. The actions on the value space of a matter field

### A.1. Continuity

**`GlobalGaugeGroup.MatterField.repDualCoeff_gaugeJetOfConstant_inv`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L101).

> A constant gauge jet acts on the dual of the value space through the gauge representation of
> the inverse of its value.

```lean
lemma repDualCoeff_gaugeJetOfConstant_inv (g : G.group) :
    repDualCoeff M.repJet (G.gaugeJetOfConstant g)⁻¹ 0 =
      ((M.rep g⁻¹ : M.V →L[ℂ] M.V) : M.V →ₗ[ℂ] M.V).dualMap
```

**`GlobalGaugeGroup.MatterField.repDualCoeff_repConj_gaugeJetOfConstant_inv`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L109).

> A constant gauge jet acts on the dual of the conjugate value space through the conjugate of
> the gauge representation of the inverse of its value.

```lean
lemma repDualCoeff_repConj_gaugeJetOfConstant_inv (g : G.group) :
    repDualCoeff (FieldDerivSpace.repConj M.repJet) (G.gaugeJetOfConstant g)⁻¹ 0 =
      (ConjModule.endConj ((M.rep g⁻¹ : M.V →L[ℂ] M.V) : M.V →ₗ[ℂ] M.V)).dualMap
```

**`GlobalGaugeGroup.MatterField.continuousCoeff_rep`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L117).

```lean
lemma continuousCoeff_rep :
    ContinuousCoeff fun g : G.group => ((M.rep g : M.V →L[ℂ] M.V) : Module.End ℂ M.V)
```

**`GlobalGaugeGroup.MatterField.continuousCoeff_repDualCoeff`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L122).

> The gauge group acts on the dual of the value space with continuous coefficients.

```lean
lemma continuousCoeff_repDualCoeff :
    ContinuousCoeff fun g : G.group => repDualCoeff M.repJet (G.gaugeJetOfConstant g)⁻¹ 0
```

**`GlobalGaugeGroup.MatterField.continuousCoeff_repDualCoeff_repConj`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L129).

> The gauge group acts on the dual of the conjugate value space with continuous
> coefficients.

```lean
lemma continuousCoeff_repDualCoeff_repConj : ContinuousCoeff fun g : G.group =>
    repDualCoeff (FieldDerivSpace.repConj M.repJet) (G.gaugeJetOfConstant g)⁻¹ 0
```

**`GlobalGaugeGroup.MatterField.LorentzContinuous.continuousCoeff_dual`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L136).

> For a continuous Lorentz representation, the Lorentz group acts on the dual of the value
> space with continuous coefficients.

```lean
lemma LorentzContinuous.continuousCoeff_dual {M : G.MatterField} (hM : M.LorentzContinuous) :
    ContinuousCoeff fun Λ : SL(2,ℂ) => M.repLorentz.dual Λ
```

**`GlobalGaugeGroup.MatterField.LorentzContinuous.continuousCoeff_conj_dual`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L143).

> For a continuous Lorentz representation, the Lorentz group acts on the dual of the
> conjugate value space with continuous coefficients.

```lean
lemma LorentzContinuous.continuousCoeff_conj_dual {M : G.MatterField}
    (hM : M.LorentzContinuous) : ContinuousCoeff fun Λ : SL(2,ℂ) => M.repLorentz.conj.dual Λ
```

### A.2. Commutation

**`GlobalGaugeGroup.MatterField.GaugeLorentzCommute.repDualCoeff_dual`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L157).

> When the gauge and Lorentz representations commute, so do their actions on the dual of the
> value space.

```lean
lemma GaugeLorentzCommute.repDualCoeff_dual {M : G.MatterField} (hM : M.GaugeLorentzCommute)
    (g : G.group) (Λ : SL(2,ℂ)) (φ : Module.Dual ℂ M.V) :
    repDualCoeff M.repJet (G.gaugeJetOfConstant g)⁻¹ 0 (M.repLorentz.dual Λ φ) =
      M.repLorentz.dual Λ (repDualCoeff M.repJet (G.gaugeJetOfConstant g)⁻¹ 0 φ)
```

**`GlobalGaugeGroup.MatterField.GaugeLorentzCommute.repDualCoeff_conj_dual`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L169).

> When the gauge and Lorentz representations commute, so do their actions on the dual of the
> conjugate value space.

```lean
lemma GaugeLorentzCommute.repDualCoeff_conj_dual {M : G.MatterField}
    (hM : M.GaugeLorentzCommute) (g : G.group) (Λ : SL(2,ℂ))
    (φ : Module.Dual ℂ (ConjModule M.V)) :
    repDualCoeff (FieldDerivSpace.repConj M.repJet) (G.gaugeJetOfConstant g)⁻¹ 0
        (M.repLorentz.conj.dual Λ φ) =
      M.repLorentz.conj.dual Λ
        (repDualCoeff (FieldDerivSpace.repConj M.repJet) (G.gaugeJetOfConstant g)⁻¹ 0 φ)
```

## B. The joint action of the gauge and Lorentz groups

**`GaugeFieldData.LocalCovFieldAlgebra.repJet_repLorentzGroup_covDerivFieldStrength`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L200).

> A constant gauge jet commutes with the Lorentz group on the field-strength tower.

```lean
lemma repJet_repLorentzGroup_covDerivFieldStrength (g : G.group) (Λ : SL(2,ℂ))
    (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    T.repJet (G.gaugeJetOfConstant g) (T.repLorentzGroup Λ (T.covDerivFieldStrength l μ ν φ)) =
      T.repLorentzGroup Λ
        (T.repJet (G.gaugeJetOfConstant g) (T.covDerivFieldStrength l μ ν φ))
```

**`GaugeFieldData.LocalCovFieldAlgebra.repJet_repLorentzGroup_covDerivFermion`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L211).

> A constant gauge jet commutes with the Lorentz group on the tower of a fermionic species.

```lean
lemma repJet_repLorentzGroup_covDerivFermion (hC : T.GaugeLorentzCommute) (g : G.group)
    (Λ : SL(2,ℂ)) (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.repJet (G.gaugeJetOfConstant g) (T.repLorentzGroup Λ (T.covDerivFermion i l φ)) =
      T.repLorentzGroup Λ (T.repJet (G.gaugeJetOfConstant g) (T.covDerivFermion i l φ))
```

**`GaugeFieldData.LocalCovFieldAlgebra.repJet_repLorentzGroup_covDerivConjFermion`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L220).

```lean
lemma repJet_repLorentzGroup_covDerivConjFermion (hC : T.GaugeLorentzCommute) (g : G.group)
    (Λ : SL(2,ℂ)) (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.repJet (G.gaugeJetOfConstant g) (T.repLorentzGroup Λ (T.covDerivConjFermion i l φ)) =
      T.repLorentzGroup Λ (T.repJet (G.gaugeJetOfConstant g) (T.covDerivConjFermion i l φ))
```

**`GaugeFieldData.LocalCovFieldAlgebra.repJet_repLorentzGroup_covDerivBoson`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L229).

```lean
lemma repJet_repLorentzGroup_covDerivBoson (hC : T.GaugeLorentzCommute) (g : G.group)
    (Λ : SL(2,ℂ)) (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.repJet (G.gaugeJetOfConstant g) (T.repLorentzGroup Λ (T.covDerivBoson j l φ)) =
      T.repLorentzGroup Λ (T.repJet (G.gaugeJetOfConstant g) (T.covDerivBoson j l φ))
```

**`GaugeFieldData.LocalCovFieldAlgebra.repJet_repLorentzGroup_covDerivConjBoson`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L238).

```lean
lemma repJet_repLorentzGroup_covDerivConjBoson (hC : T.GaugeLorentzCommute) (g : G.group)
    (Λ : SL(2,ℂ)) (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.repJet (G.gaugeJetOfConstant g) (T.repLorentzGroup Λ (T.covDerivConjBoson j l φ)) =
      T.repLorentzGroup Λ (T.repJet (G.gaugeJetOfConstant g) (T.covDerivConjBoson j l φ))
```

**`GaugeFieldData.LocalCovFieldAlgebra.repJet_repLorentzGroup_comm`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L249).

> On the covariant field algebra, a constant gauge jet commutes with the Lorentz group when
> the gauge and Lorentz representations of every species commute.

```lean
lemma repJet_repLorentzGroup_comm (hC : T.GaugeLorentzCommute) (g : G.group) (Λ : SL(2,ℂ))
    {x : T.LocalFieldAlgebra} (hx : x ∈ T.LocalCovFieldAlgebra) :
    T.repJet (G.gaugeJetOfConstant g) (T.repLorentzGroup Λ x) =
      T.repLorentzGroup Λ (T.repJet (G.gaugeJetOfConstant g) x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.repValue_apply_one`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L268).

```lean
lemma repValue_apply_one (g : G.group) : repValue T g 1 = 1
```

**`GaugeFieldData.LocalCovFieldAlgebra.repLorentzGroup_apply_one`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L271).

```lean
lemma repLorentzGroup_apply_one (hGL : T.GaugeLorentzCompatible) (Λ : SL(2,ℂ)) :
    repLorentzGroup T hGL Λ 1 = 1
```

**`GaugeFieldData.LocalCovFieldAlgebra.commute_repValue_repLorentzGroup`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L277).

> The ordinary gauge group and the Lorentz group act on the covariant field algebra by
> commuting operators, when the gauge and Lorentz representations of every species commute.

```lean
lemma commute_repValue_repLorentzGroup (hC : T.GaugeLorentzCommute) (g : G.group) (Λ : SL(2,ℂ)) :
    Commute (repValue T g) (repLorentzGroup T hC.gaugeLorentzCompatible Λ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.repGaugeLorentz`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L284).

> The action of `G × SL(2,ℂ)` on the covariant field algebra, built from the commuting actions
> of the ordinary gauge group and of the Lorentz group.

```lean
noncomputable def repGaugeLorentz (hC : T.GaugeLorentzCommute) :
    Representation ℂ (G.group × SL(2,ℂ)) T.LocalCovFieldAlgebra
```

**`GaugeFieldData.LocalCovFieldAlgebra.repGaugeLorentz_comp_inl`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L289).

```lean
lemma repGaugeLorentz_comp_inl (hC : T.GaugeLorentzCommute) :
    (repGaugeLorentz T hC).comp (MonoidHom.inl G.group SL(2,ℂ)) = repValue T
```

**`GaugeFieldData.LocalCovFieldAlgebra.repGaugeLorentz_comp_inr`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L293).

```lean
lemma repGaugeLorentz_comp_inr (hC : T.GaugeLorentzCommute) :
    (repGaugeLorentz T hC).comp (MonoidHom.inr G.group SL(2,ℂ)) =
      repLorentzGroup T hC.gaugeLorentzCompatible
```

## C. Continuity on the covariant towers

### C.1. The Lorentz matrix

**`GaugeFieldData.LocalCovFieldAlgebra.continuous_toLorentzGroup_apply`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L307).

> The entries of the Lorentz matrix of `Λ : SL(2,ℂ)` depend continuously on `Λ`.

```lean
lemma continuous_toLorentzGroup_apply (b a : Fin 1 ⊕ Fin 3) :
    Continuous fun Λ : SL(2,ℂ) => L[Λ] b a
```

### C.2. The field-strength tower

**`GaugeFieldData.LocalCovFieldAlgebra.continuousCoeff_adjointRep`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L321).

> The adjoint representation of the gauge group has continuous coefficients.

```lean
lemma continuousCoeff_adjointRep : ContinuousCoeff fun g : G.group => G.adjointRep g
```

**`GaugeFieldData.LocalCovFieldAlgebra.covFieldStrength_eq_sum`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L338).

> The field-strength tower is real-linear in its adjoint index.

```lean
lemma covFieldStrength_eq_sum (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    covFieldStrength T l μ ν φ = ∑ j, ((Module.finBasis ℝ _ |>.repr φ j : ℝ) : ℂ) •
      covFieldStrength T l μ ν (Module.finBasis ℝ (Module.Dual ℝ G.lieSubalgebra) j)
```

**`GaugeFieldData.LocalCovFieldAlgebra.hasContinuousSpan_covFieldStrength`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L351).

> The field-strength tower has a continuous span.

```lean
lemma hasContinuousSpan_covFieldStrength (hGL : T.GaugeLorentzCompatible) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    HasContinuousSpan (repValue T) (repLorentzGroup T hGL)
      (covFieldStrength T (List.ofFn l) μ ν φ)
```

### C.3. The matter towers

**`GaugeFieldData.LocalCovFieldAlgebra.hasContinuousSpan_tower`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L389).

> A tower `t p x`, linear in `x`, on which the gauge group acts through an operator family with
> continuous coefficients on `x`, and the Lorentz group through the Lorentz matrix on the
> directions `p` and an operator family with continuous coefficients on `x`, has a continuous
> span.

```lean
lemma hasContinuousSpan_tower (hGL : T.GaugeLorentzCompatible) {D : Type} [AddCommGroup D]
    [Module ℂ D] [FiniteDimensional ℂ D] {n : ℕ}
    (t : (Fin n → Fin 1 ⊕ Fin 3) → D →ₗ[ℂ] T.LocalCovFieldAlgebra)
    {σ₁ : G.group → Module.End ℂ D} (hσ₁ : ContinuousCoeff σ₁)
    (h₁ : ∀ g p x, repValue T g (t p x) = t p (σ₁ g x))
    {σ₂ : SL(2,ℂ) → Module.End ℂ D} (hσ₂ : ContinuousCoeff σ₂)
    (h₂ : ∀ Λ p x, repLorentzGroup T hGL Λ (t p x) =
      ∑ p', (∏ k, L[Λ] (p' k) (p k)) • t p' (σ₂ Λ x))
    (l : Fin n → Fin 1 ⊕ Fin 3) (x : D) :
    HasContinuousSpan (repValue T) (repLorentzGroup T hGL) (t l x)
```

## D. Finite-dimensional stable subspaces

**`GaugeFieldData.LocalCovFieldAlgebra.hasContinuousSpan`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L423).

> Every element of the covariant field algebra lies in the span of a finite family on which
> the ordinary gauge group and the Lorentz group act with continuous coefficients.

```lean
lemma hasContinuousSpan (hGL : T.GaugeLorentzCompatible) (hL : T.LorentzContinuous)
    (a : T.LocalCovFieldAlgebra) : HasContinuousSpan (repValue T) (repLorentzGroup T hGL) a
```

**`GaugeFieldData.LocalCovFieldAlgebra.exists_subrepresentation`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L464).

> Every element of the covariant field algebra lies in a finite-dimensional subrepresentation
> for the joint action of the gauge and Lorentz groups, on which both groups act with continuous
> matrix coefficients.

```lean
lemma exists_subrepresentation (hL : T.LorentzContinuous) (hC : T.GaugeLorentzCommute)
    (a : T.LocalCovFieldAlgebra) :
    ∃ W : Subrepresentation (repGaugeLorentz T hC), a ∈ W.toSubmodule ∧
      FiniteDimensional ℂ W.toSubmodule ∧
      Representation.ContinuousMatrixCoeff (W.comp (MonoidHom.inl G.group SL(2,ℂ))) ∧
      Representation.ContinuousMatrixCoeff (W.comp (MonoidHom.inr G.group SL(2,ℂ)))
```

**`GaugeFieldData.LocalCovFieldAlgebra.finiteSubrep`**, a def, [line 477](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L477).

> A chosen finite-dimensional subrepresentation for the joint action of the gauge and Lorentz
> groups containing `a`, on which both groups act with continuous matrix coefficients.

```lean
noncomputable def finiteSubrep (hL : T.LorentzContinuous) (hC : T.GaugeLorentzCommute)
    (a : T.LocalCovFieldAlgebra) :
    Subrepresentation (repGaugeLorentz T hC)
```

**`GaugeFieldData.LocalCovFieldAlgebra.mem_finiteSubrep`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L484).

```lean
lemma mem_finiteSubrep : a ∈ (finiteSubrep hL hC a).toSubmodule
```

**`GaugeFieldData.LocalCovFieldAlgebra.finiteDimensional_finiteSubrep`**, an instance, [line 487](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L487).

```lean
instance finiteDimensional_finiteSubrep :
    FiniteDimensional ℂ (finiteSubrep hL hC a).toSubmodule
```

**`GaugeFieldData.LocalCovFieldAlgebra.continuousMatrixCoeff_finiteSubrep_inl`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L491).

```lean
lemma continuousMatrixCoeff_finiteSubrep_inl : Representation.ContinuousMatrixCoeff
    ((finiteSubrep hL hC a).comp (MonoidHom.inl G.group SL(2,ℂ)))
```

**`GaugeFieldData.LocalCovFieldAlgebra.continuousMatrixCoeff_finiteSubrep_inr`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean#L495).

```lean
lemma continuousMatrixCoeff_finiteSubrep_inr : Representation.ContinuousMatrixCoeff
    ((finiteSubrep hL hC a).comp (MonoidHom.inr G.group SL(2,ℂ)))
```

## Depends on

- [The covariant field algebra of a gauge theory](localfieldalgebra-localcovfieldalgebra-basic.md)
- [Conditions for the reduction of invariants](localfieldalgebra-realization-conditions.md)
- [Continuous families of a representation](../../../mathematics/part-02/representationtheory/reynolds-continuousfamily.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/FiniteStable.lean)
