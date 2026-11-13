---
declaration: module
origin: cited
lean: StandardModel.AlgebraRealization.repGlobal, StandardModel.AlgebraRealization.repGlobal_apply, StandardModel.AlgebraRealization.repGlobal_mul, StandardModel.AlgebraRealization.Species, StandardModel.AlgebraRealization.Species.tower, StandardModel.AlgebraRealization.Species.comm_A, StandardModel.AlgebraRealization.speciesH, StandardModel.AlgebraRealization.speciesBarH
statement: formalized
proof: formalized
---

# From the jet Standard Model to its covariant form

The module `PhyslibAlpha.Particles.StandardModel.Realization.CovStandardModel`, [PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean): 170 declarations, 56 with a docstring.

## i. Overview

> `AlgebraRealization` records the Standard Model in terms of the *bare* symbols
> `[∂_s A_μ^a]`, `[∂_s H^i]`, `[∂_s ψ^α]`, on which the whole jet gauge group
> `JetGaugeGroupI` acts — a gauge transformation together with all of its derivatives at
> the base point. The covariant form of the theory is written instead in terms of the
> covariant towers `∇_l F_{μν}`, `∇_l H`, `∇_l ψ`, on which only the global gauge group
> `GaugeGroupI` acts.
>
> This file builds the bridge, in two halves. The first proves the *reduction theorem*:
> inside the field algebra, invariance under the full jet gauge group is exactly
> membership of the covariant subalgebra together with invariance under the global gauge
> group; adjoining the Lorentz condition, which the reduction leaves untouched, gives the
> form used for classifying Lagrangians. The second establishes the laws the towers
> satisfy, which `CovAlgebraRealization` collects into the covariant form of the theory:
> their global gauge equivariance, their mass weights and their statistics. The twelve
> matter towers are treated uniformly: section B packages a matter species as its
> gauge-algebra action, its bare family, and the two facts about the family every argument
> uses — it commutes with the gauge field and it is a mass-weight eigenvector — and each
> later law is proved once for an arbitrary species and read off twelve times. The Lorentz
> laws of the matter towers are section L of [`CovariantDeriv.lean`](../part-09/realization-covariantderiv.md);
> the one for the field-strength tower closes this file.

## ii. Key results

> - `AlgebraRealization.repGlobal` : the global gauge action, the jet action restricted
>   along the constant jets.
> - `AlgebraRealization.Species` : a matter species with the facts the laws below consume;
>   `AlgebraRealization.speciesH`, `AlgebraRealization.speciesD` and their companions are
>   the twelve matter families of the Standard Model.
> - `AlgebraRealization.forall_repJet_eq_iff` and
>   `AlgebraRealization.forall_repJet_and_repLorentz_eq_iff` : the reduction theorem, for
>   the gauge group alone and together with the Lorentz group.
> - `AlgebraRealization.repGlobal_covF`, `AlgebraRealization.repGlobal_covDerivH` and their
>   companions : the covariant towers are equivariant for the global gauge group.
> - `AlgebraRealization.covF_commute_of_mem_covAlgebra` : the field-strength tower is
>   central in the covariant algebra.
> - `AlgebraRealization.Species.massWeight_tower` and `AlgebraRealization.massWeight_covF` :
>   a covariant tower is a mass-weight eigenvector of the weight its species and
>   derivative order predict.
> - `AlgebraRealization.Species.commute_tower_tower` and
>   `AlgebraRealization.Species.anticomm_tower_tower` : the statistics of a pair of towers
>   is the statistics of the pair of bare families.
> - `AlgebraRealization.repLorentz_covF` : the Lorentz law of the field-strength tower.

## iv. References

> The classification of jet-gauge invariants that section D consumes is
> `AlgebraRealization.invariant_mem_adjoin_covDeriv` of
> [`CovFieldAlgebra/Basic.lean`](realization-covfieldalgebra-basic.md); the splitting of a gauge jet
> into a pure jet and a constant jet is `localGaugeData.eq_truncationProjZero_mul_ofConstant`.
> The laws of the second half are consumed by the three sector structures of
> [`IsGaugeSector/Basic.lean`](../part-06/isgaugesector-basic.md),
> [`HiggsAlgebraCovRealization/Basic.lean`](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsAlgebraCovRealization/Basic.lean) and
> [`IsFermionSector/Basic.lean`](../part-05/isfermionsector-basic.md).

## A. The global gauge action

> A global (constant) gauge transformation is a jet with no derivatives, so the global gauge
> group sits inside the jet gauge group as the constant jets. Restricting the jet action along
> that inclusion gives the global gauge action on the algebra, multiplicative like the jet action.

**`StandardModel.AlgebraRealization.repGlobal`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L111).

> The action of the global gauge group on the algebra: the jet action restricted
> along the inclusion of the constant jets.

```lean
noncomputable def repGlobal (repJet : Representation ℂ JetGaugeGroupI B) :
    Representation ℂ GaugeGroupI B
```

**`StandardModel.AlgebraRealization.repGlobal_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L117).

> The global gauge action is the jet action at the corresponding constant jet.

```lean
lemma repGlobal_apply (repJet : Representation ℂ JetGaugeGroupI B) (g : GaugeGroupI)
    (b : B) : repGlobal repJet g b = repJet (JetGaugeGroupI.ofConstant g) b
```

**`StandardModel.AlgebraRealization.repGlobal_mul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L123).

> The global gauge action is multiplicative: it is the jet action at a constant jet,
> and the jet action is an algebra map.

```lean
lemma repGlobal_mul (g : GaugeGroupI) (b₁ b₂ : B) :
    repGlobal repJet g (b₁ * b₂) = repGlobal repJet g b₁ * repGlobal repJet g b₂
```

## B. The twelve matter species

> Every matter tower is `GaugeAlgebraRealization.covDerivIter h.A act F n l 0` for the gauge-algebra
> action `act` of its species and its bare family `F`, and every law proved below for a
> matter tower uses only two facts about that family: its symbols commute with the
> gauge-field symbols, and they are mass-weight eigenvectors of weight `c + 2 * |t|` at the
> derivative multiset `t`. A `Species` records exactly this data, the twelve matter families
> of the Standard Model are its twelve instances, and `matterTowers_induction_species` and
> `covGenerators_cases` are the case splits that read a law proved for an arbitrary species
> off for all of them.

**`StandardModel.AlgebraRealization.Species`**, a structure, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L147).

> A matter species of the Standard Model, as the laws of this file consume it: the
> gauge-algebra action on its value space, its bare family of derivative symbols, the
> mass weight `c` of its undifferentiated symbols, and the two facts that the family
> commutes with the gauge-field symbols and has mass weight `c + 2 * |t|` at the
> derivative multiset `t`.

```lean
structure Species (V : Type) [AddCommGroup V] [Module ℂ V] where
  /-- The action of the gauge algebra on the value space. -/
  act : GaugeAlgebra →ₗ[ℝ] V →ₗ[ℂ] V
  /-- The bare derivative symbols of the species. -/
  F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B
  /-- The mass weight of the undifferentiated symbols. -/
  c : ℕ
  /-- The gauge-field symbols commute with the bare symbols. -/
  A_comm : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra)
    (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V), Commute (h.A p μ ψ) (F t χ)
  /-- The bare symbol at the derivative multiset `t` has mass weight `c + 2 * |t|`. -/
  massWeight : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V),
    massWeightPoly (F t χ) = Polynomial.monomial (c + 2 * Multiset.card t) (F t χ)
```

**`StandardModel.AlgebraRealization.Species.tower`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L167).

> The covariant tower of the species, in the ordered-tuple indexing of the covariant
> form of the theory.

```lean
noncomputable def tower {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) : Module.Dual ℂ V →ₗ[ℂ] B
```

**`StandardModel.AlgebraRealization.Species.comm_A`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L171).

> The tower commutes with the gauge-field symbols: it is a polynomial in symbols that do.

```lean
lemma comm_A {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V)
    (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra) :
    Commute (S.tower l φ) (h.A p μ ψ)
```

**`StandardModel.AlgebraRealization.speciesH`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L179).

> The Higgs field, of mass weight `2`.

```lean
noncomputable def speciesH : h.Species HiggsVec
```

**`StandardModel.AlgebraRealization.speciesBarH`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L184).

> The conjugate Higgs field, of mass weight `2`.

```lean
noncomputable def speciesBarH : h.Species (ConjModule HiggsVec)
```

**`StandardModel.AlgebraRealization.speciesD`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L189).

> The down-type quarks of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesD (i : Fin 3) : h.Species DownSinglet
```

**`StandardModel.AlgebraRealization.speciesBarD`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L193).

> The conjugate down-type quarks of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesBarD (i : Fin 3) : h.Species (ConjModule DownSinglet)
```

**`StandardModel.AlgebraRealization.speciesU`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L198).

> The up-type quarks of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesU (i : Fin 3) : h.Species UpSinglet
```

**`StandardModel.AlgebraRealization.speciesBarU`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L202).

> The conjugate up-type quarks of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesBarU (i : Fin 3) : h.Species (ConjModule UpSinglet)
```

**`StandardModel.AlgebraRealization.speciesQ`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L207).

> The quark doublets of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesQ (i : Fin 3) : h.Species QuarkDoublet
```

**`StandardModel.AlgebraRealization.speciesBarQ`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L211).

> The conjugate quark doublets of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesBarQ (i : Fin 3) : h.Species (ConjModule QuarkDoublet)
```

**`StandardModel.AlgebraRealization.speciesL`**, a def, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L216).

> The lepton doublets of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesL (i : Fin 3) : h.Species LeptonDoubletV
```

**`StandardModel.AlgebraRealization.speciesBarL`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L220).

> The conjugate lepton doublets of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesBarL (i : Fin 3) : h.Species (ConjModule LeptonDoubletV)
```

**`StandardModel.AlgebraRealization.speciesE`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L225).

> The lepton singlets of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesE (i : Fin 3) : h.Species LeptonSinglet
```

**`StandardModel.AlgebraRealization.speciesBarE`**, a def, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L229).

> The conjugate lepton singlets of generation `i`, of mass weight `3`.

```lean
noncomputable def speciesBarE (i : Fin 3) : h.Species (ConjModule LeptonSinglet)
```

**`StandardModel.AlgebraRealization.matterTowers_induction_species`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L235).

> A property of every symbol of every matter tower is proved species by species: each
> matter tower is the tower of one of the twelve species.

```lean
lemma matterTowers_induction_species (P : B → Prop) {b : B} (hb : b ∈ h.matterTowers)
    (hS : ∀ {V : Type} [AddCommGroup V] [Module ℂ V] [FiniteDimensional ℂ V] (S : h.Species V)
      (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V), P (S.tower l φ)) : P b
```

**`StandardModel.AlgebraRealization.covGenerators_cases`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L245).

> A property of every covariant generator is proved for the field-strength tower and
> for the matter towers.

```lean
lemma covGenerators_cases (P : B → Prop) {b : B} (hb : b ∈ h.covGenerators)
    (hF : ∀ (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
      (φ : Module.Dual ℝ GaugeAlgebra), P (h.covF l μ ν φ))
    (hM : ∀ b ∈ h.matterTowers, P b) : P b
```

## C. Pure gauge jets fix the covariant algebra

> Section M of `AlgebraRealization.CovariantDeriv` shows that a gauge jet with trivial
> base-point value fixes every covariant generator. The jet action is multiplicative, so it
> fixes the whole algebra those generators span.

**`StandardModel.AlgebraRealization.repJet_algebraMap`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L269).

> Gauge jets fix the scalars: the action is multiplicative, hence unital, and
> complex-linear.

```lean
lemma repJet_algebraMap (U : JetGaugeGroupI) (c : ℂ) :
    repJet U (algebraMap ℂ B c) = algebraMap ℂ B c
```

**`StandardModel.AlgebraRealization.repJet_eq_of_mem_covGenerators_of_mem_truncationKer_zero`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L278).

> Pure gauge jets fix the covariant generators: the thirteen cases are section L of
> `AlgebraRealization.CovariantDeriv`.

```lean
lemma repJet_eq_of_mem_covGenerators_of_mem_truncationKer_zero
    (U : localGaugeData.truncationKer 0) {x : B} (hx : x ∈ h.covGenerators) :
    repJet U.1 x = x
```

**`StandardModel.AlgebraRealization.repJet_eq_of_mem_covAlgebra_of_mem_truncationKer_zero`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L299).

> Pure gauge jets fix the covariant algebra pointwise: they fix its generators, and
> the jet action is an algebra map.

```lean
lemma repJet_eq_of_mem_covAlgebra_of_mem_truncationKer_zero
    (U : localGaugeData.truncationKer 0) {x : B} (hx : x ∈ h.covAlgebra) :
    repJet U.1 x = x
```

## D. The reduction theorem

> Every gauge jet splits as a pure jet times a constant jet. On the covariant algebra the
> pure part acts trivially, so only the constant part — the global gauge group — is left.
> In the other direction the classification `AlgebraRealization.invariant_mem_adjoin_covDeriv`
> of `AlgebraRealization.CovFieldAlgebra.Basic` puts every jet-invariant of the field algebra
> inside the covariant algebra. Together: on the field algebra, jet invariance is membership
> of the covariant algebra plus global invariance.

**`StandardModel.AlgebraRealization.forall_repJet_eq_iff`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L324).

> The reduction of jet gauge invariance to global gauge invariance: an element of the
> field algebra is invariant under the whole jet gauge group exactly when it lies in
> the covariant algebra and is invariant under the global gauge group.

```lean
lemma forall_repJet_eq_iff {x : B} (hx : x ∈ h.fieldAlgebra) :
    (∀ U : JetGaugeGroupI, repJet U x = x) ↔
      x ∈ h.covAlgebra ∧ ∀ g : GaugeGroupI, repGlobal repJet g x = x
```

**`StandardModel.AlgebraRealization.forall_repJet_and_repLorentz_eq_iff`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L336).

> The reduction theorem in the form used for Lagrangians: on the field algebra, invariance
> under the jet gauge group and the Lorentz group is membership of the covariant algebra
> with invariance under the global gauge group and the Lorentz group.

```lean
lemma forall_repJet_and_repLorentz_eq_iff {x : B} (hx : x ∈ h.fieldAlgebra) :
    ((∀ U : JetGaugeGroupI, repJet U x = x) ∧ ∀ Λ : SL(2,ℂ), repLorentz Λ x = x) ↔
      (x ∈ h.covAlgebra ∧ (∀ g : GaugeGroupI, repGlobal repJet g x = x) ∧
        ∀ Λ : SL(2,ℂ), repLorentz Λ x = x)
```

## E. The covariant generators are globally equivariant

> Section L of `AlgebraRealization.CovariantDeriv` shows that a gauge jet acts on a covariant
> tower through the base-point Taylor coefficient of its representation alone. Evaluated on
> a constant jet, that coefficient is the corresponding action of the global gauge group,
> so each covariant tower is equivariant for `repGlobal` in the (contragredient of the)
> global representation of its species. These are exactly the `repGauge_*` obligations of
> `IsGaugeSector`, `HiggsAlgebraCovRealization` and `IsFermionSector`: `repGlobal_covF` for the
> field strength, and `repGlobal_covDerivH`, `repGlobal_covDerivD` and their companions for the
> twelve matter towers, each an instance of `repGlobal_of_repJet` or of its conjugate form.

**`StandardModel.AlgebraRealization.repCoeff_zero_ofConstant`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L359).

> The zeroth Taylor coefficient of a jet representation at a constant jet is the
> underlying action of the global gauge group.

```lean
lemma repCoeff_zero_ofConstant {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] V)}
    {repG : Representation ℂ GaugeGroupI V} {g : GaugeGroupI}
    (hg : rep (JetGaugeGroupI.ofConstant g) = TensorProduct.map LinearMap.id (repG g)) :
    GaugeAlgebraRealization.repCoeff rep (JetGaugeGroupI.ofConstant g) 0 = repG g
```

**`StandardModel.AlgebraRealization.repGlobal_of_repJet`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L372).

> A tower that transforms through the base-point dual coefficient of a gauge jet is
> equivariant for the global gauge group, in the contragredient of the global
> representation.

```lean
lemma repGlobal_of_repJet {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] V)}
    {repG : Representation ℂ GaugeGroupI V} {T : Module.Dual ℂ V →ₗ[ℂ] B}
    (hT : ∀ (U : JetGaugeGroupI) (φ : Module.Dual ℂ V),
      repJet U (T φ) = T (GaugeAlgebraRealization.repDualCoeff rep U⁻¹ 0 φ))
    (hg : ∀ g : GaugeGroupI,
      rep (JetGaugeGroupI.ofConstant g) = TensorProduct.map LinearMap.id (repG g))
    (g : GaugeGroupI) (φ : Module.Dual ℂ V) :
    repGlobal repJet g (T φ) = T (repG.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_of_repJet_conj`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L388).

> The conjugate form of `repGlobal_of_repJet`: a tower transforming through the dual
> coefficient of the conjugate representation is equivariant in its conjugate contragredient.

```lean
lemma repGlobal_of_repJet_conj {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] V)}
    {repG : Representation ℂ GaugeGroupI V} {T : Module.Dual ℂ (ConjModule V) →ₗ[ℂ] B}
    (hT : ∀ (U : JetGaugeGroupI) (φ : Module.Dual ℂ (ConjModule V)), repJet U (T φ) =
      T (GaugeAlgebraRealization.repDualCoeff (JetComponentSpace.repConj rep) U⁻¹ 0 φ))
    (hg : ∀ g : GaugeGroupI,
      rep (JetGaugeGroupI.ofConstant g) = TensorProduct.map LinearMap.id (repG g))
    (g : GaugeGroupI) (φ : Module.Dual ℂ (ConjModule V)) :
    repGlobal repJet g (T φ) = T (repG.conj.dual g φ)
```

**`StandardModel.AlgebraRealization.localGaugeData.adjointDualCoeff_zero_ofConstant_inv`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L404).

> At an inverse constant jet the dual adjoint coefficient is the contragredient
> adjoint action of the global gauge group.

```lean
lemma localGaugeData.adjointDualCoeff_zero_ofConstant_inv (g : GaugeGroupI) :
    localGaugeData.adjointDualCoeff (JetGaugeGroupI.ofConstant g)⁻¹ 0 =
      (GaugeAlgebra.adjointMap g⁻¹).dualMap
```

**`StandardModel.AlgebraRealization.repGlobal_covF`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L417).

> The field-strength tower is equivariant for the global gauge group, in the
> contragredient adjoint representation.

```lean
lemma repGlobal_covF (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ GaugeAlgebra) :
    repGlobal repJet g (h.covF l μ ν φ) =
      h.covF l μ ν ((GaugeAlgebra.adjointMap g⁻¹).dualMap φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivH`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L423).

```lean
lemma repGlobal_covDerivH (φ : Module.Dual ℂ HiggsVec) :
    repGlobal repJet g (h.covDerivH l φ) = h.covDerivH l (HiggsVec.repGaugeGroupI.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivBarH`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L427).

```lean
lemma repGlobal_covDerivBarH (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    repGlobal repJet g (h.covDerivBarH l φ) =
      h.covDerivBarH l (HiggsVec.repGaugeGroupI.conj.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivD`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L432).

```lean
lemma repGlobal_covDerivD (φ : Module.Dual ℂ DownSinglet) :
    repGlobal repJet g (h.covDerivD i l φ) =
      h.covDerivD i l (DownSinglet.repGaugeGroupI.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivBarD`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L437).

```lean
lemma repGlobal_covDerivBarD (φ : Module.Dual ℂ (ConjModule DownSinglet)) :
    repGlobal repJet g (h.covDerivBarD i l φ) =
      h.covDerivBarD i l (DownSinglet.repGaugeGroupI.conj.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivU`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L442).

```lean
lemma repGlobal_covDerivU (φ : Module.Dual ℂ UpSinglet) :
    repGlobal repJet g (h.covDerivU i l φ) = h.covDerivU i l (UpSinglet.repGaugeGroupI.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivBarU`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L446).

```lean
lemma repGlobal_covDerivBarU (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    repGlobal repJet g (h.covDerivBarU i l φ) =
      h.covDerivBarU i l (UpSinglet.repGaugeGroupI.conj.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivQ`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L451).

```lean
lemma repGlobal_covDerivQ (φ : Module.Dual ℂ QuarkDoublet) :
    repGlobal repJet g (h.covDerivQ i l φ) =
      h.covDerivQ i l (QuarkDoublet.repGaugeGroupI.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivBarQ`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L456).

```lean
lemma repGlobal_covDerivBarQ (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    repGlobal repJet g (h.covDerivBarQ i l φ) =
      h.covDerivBarQ i l (QuarkDoublet.repGaugeGroupI.conj.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivL`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L461).

```lean
lemma repGlobal_covDerivL (φ : Module.Dual ℂ LeptonDoubletV) :
    repGlobal repJet g (h.covDerivL i l φ) =
      h.covDerivL i l (LeptonDoubletV.repGaugeGroupI.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivBarL`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L466).

```lean
lemma repGlobal_covDerivBarL (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    repGlobal repJet g (h.covDerivBarL i l φ) =
      h.covDerivBarL i l (LeptonDoubletV.repGaugeGroupI.conj.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivE`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L472).

```lean
lemma repGlobal_covDerivE (φ : Module.Dual ℂ LeptonSinglet) :
    repGlobal repJet g (h.covDerivE i l φ) =
      h.covDerivE i l (LeptonSinglet.repGaugeGroupI.dual g φ)
```

**`StandardModel.AlgebraRealization.repGlobal_covDerivBarE`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L477).

```lean
lemma repGlobal_covDerivBarE (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    repGlobal repJet g (h.covDerivBarE i l φ) =
      h.covDerivBarE i l (LeptonSinglet.repGaugeGroupI.conj.dual g φ)
```

## F. The field-strength tower is central in the covariant algebra

> The gauge field is bosonic, so its symbols commute with each other and with every matter
> symbol. Every covariant generator is a polynomial in those symbols, so the covariant
> generators all commute with the gauge-field symbols; and the field-strength tower, being
> itself a polynomial in the gauge-field symbols, therefore commutes with the whole covariant
> algebra. This discharges the `F_comm_F` obligation of `IsGaugeSector` and the cross-sector
> `F_comm_*` rules at once.

**`StandardModel.AlgebraRealization.covF_mem_adjoin_gaugeSymbols`**, a lemma, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L500).

> The covariant derivatives of the field strength are polynomials in the gauge-field
> symbols.

```lean
lemma covF_mem_adjoin_gaugeSymbols {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ GaugeAlgebra) :
    h.covF l μ ν φ ∈ Algebra.adjoin ℂ {b : B | ∃ (s : Multiset (Fin 1 ⊕ Fin 3))
      (ρ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra), b = h.A s ρ ψ}
```

**`StandardModel.AlgebraRealization.covF_comm_of_comm_A`**, a lemma, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L509).

> The field-strength tower commutes with anything the gauge-field symbols commute
> with.

```lean
lemma covF_comm_of_comm_A {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) {y : B}
    (hy : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (ρ : Fin 1 ⊕ Fin 3) (ψ' : Module.Dual ℝ GaugeAlgebra),
      Commute (h.A p ρ ψ') y) : Commute (h.covF l μ ν ψ) y
```

**`StandardModel.AlgebraRealization.commute_gaugeSymbol_of_mem_covGenerators`**, a lemma, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L519).

> Every covariant generator commutes with every gauge-field symbol: the covariant towers
> are polynomials in the gauge-field and matter symbols, and the gauge field is bosonic.

```lean
lemma commute_gaugeSymbol_of_mem_covGenerators (p : Multiset (Fin 1 ⊕ Fin 3))
    (ρ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra) {y : B}
    (hy : y ∈ h.covGenerators) : Commute y (h.A p ρ ψ)
```

**`StandardModel.AlgebraRealization.covF_commute_of_mem_covAlgebra`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L529).

> The field-strength tower is central in the covariant algebra: it commutes with every
> covariant generator, and commutation extends to the algebra they generate.

```lean
lemma covF_commute_of_mem_covAlgebra {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra) {x : B}
    (hx : x ∈ h.covAlgebra) : Commute (h.covF l μ ν ψ) x
```

## G. Sums of products: the two family pairings

> Both correction terms of a covariant derivative — the action pairing `act` on a matter
> family and the gauge-algebra bracket on an adjoint family — are, after expansion in a basis,
> finite sums of scalar multiples of products of the two families' components. So each lands
> in any submodule of `B` containing all those products, which is all sections H and I use.

**`StandardModel.AlgebraRealization.actionFam_apply_mem_submodule`**, a lemma, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L549).

> The action pairing of two families lands in any submodule containing the products of
> their components: expanded in bases it is a finite sum of scalar multiples of them.

```lean
lemma actionFam_apply_mem_submodule {V : Type} [AddCommGroup V] [Module ℂ V]
    [FiniteDimensional ℂ V] {act : GaugeAlgebra →ₗ[ℝ] V →ₗ[ℂ] V} {M : Submodule ℂ B}
    {f : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B} {g : Module.Dual ℂ V →ₗ[ℂ] B}
    (hfg : ∀ ψ χ, f ψ * g χ ∈ M) (φ : Module.Dual ℂ V) :
    GaugeAlgebraRealization.actionFam act f g φ ∈ M
```

**`StandardModel.AlgebraRealization.bracketFam_apply_mem_submodule`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L563).

> The bracket pairing of two adjoint families lands in any submodule containing the
> products of their components: it is the sum of the structure constants against them.

```lean
lemma bracketFam_apply_mem_submodule {M : Submodule ℂ B}
    {f g : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B}
    (hfg : ∀ ψ χ, f ψ * g χ ∈ M) (φ : Module.Dual ℝ GaugeAlgebra) :
    GaugeAlgebraRealization.bracketFam f g φ ∈ M
```

## H. The mass weights of the covariant towers

> `massWeightPoly` is pinned down on the bare symbols only, while a covariant tower is a sum
> of products of them. The weight-`w` eigenspace of `massWeightPoly` is a submodule, and the
> product of a weight-`w` and a weight-`w'` element has weight `w + w'`; the recursion defining
> a covariant derivative adds one derivative on one branch and one gauge-field factor on the
> other, which cost the same two units of weight. Both towers are therefore eigenvectors, of
> the weights `IsGaugeSector`, `HiggsAlgebraCovRealization` and `IsFermionSector` demand.

**`StandardModel.AlgebraRealization.massWeightEigenspace`**, a def, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L587).

> The weight-`w` part of the algebra: the elements on which the mass-weight algebra
> map is the monomial `X ^ w`.

```lean
noncomputable def massWeightEigenspace (massWeightPoly : B →ₐ[ℂ] Polynomial B) (w : ℕ) :
    Submodule ℂ B
```

**`StandardModel.AlgebraRealization.mem_massWeightEigenspace_iff`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L593).

> Membership of the weight-`w` part is the eigenvector equation itself.

```lean
lemma mem_massWeightEigenspace_iff {w : ℕ} {b : B} :
    b ∈ massWeightEigenspace massWeightPoly w ↔
      massWeightPoly b = Polynomial.monomial w b
```

**`StandardModel.AlgebraRealization.mul_mem_massWeightEigenspace`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L602).

> The mass weight is additive on products: `massWeightPoly` is an algebra map and
> monomials multiply by adding their degrees.

```lean
lemma mul_mem_massWeightEigenspace {w w' : ℕ} {b b' : B}
    (hb : b ∈ massWeightEigenspace massWeightPoly w)
    (hb' : b' ∈ massWeightEigenspace massWeightPoly w') :
    b * b' ∈ massWeightEigenspace massWeightPoly (w + w')
```

**`StandardModel.AlgebraRealization.A_mem_massWeightEigenspace`**, a lemma, [line 610](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L610).

> A gauge-field symbol with `|p|` derivatives has mass weight `2 * (1 + |p|)`.

```lean
lemma A_mem_massWeightEigenspace (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) :
    h.A p μ ψ ∈ massWeightEigenspace massWeightPoly (2 * (1 + Multiset.card p))
```

**`StandardModel.AlgebraRealization.Species.covDerivIter_mem_massWeightEigenspace`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L623).

> The mass weight of a matter covariant tower: the `n`-fold covariant derivative of the
> family at the derivative multiset `s` has weight `c + 2 * n + 2 * |s|`. Each covariant
> derivative costs two units, whether it lands on the derivative index or brings down a
> gauge-field factor.

```lean
lemma covDerivIter_mem_massWeightEigenspace {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    GaugeAlgebraRealization.covDerivIter h.A S.act S.F n l s φ ∈
      massWeightEigenspace massWeightPoly (S.c + 2 * n + 2 * Multiset.card s)
```

**`StandardModel.AlgebraRealization.Species.massWeight_tower`**, a lemma, [line 651](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L651).

> The mass weight of the tower of a species is `c + 2 * n`: the form in which the
> sector structures ask for it.

```lean
lemma massWeight_tower {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    massWeightPoly (S.tower l φ) = Polynomial.monomial (S.c + 2 * n) (S.tower l φ)
```

**`StandardModel.AlgebraRealization.fieldStrength_mem_massWeightEigenspace`**, a lemma, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L660).

> The mass weight of the bare field strength: two gauge-field symbols, or one with an
> extra derivative, in either case weight `4 + 2 * |s|`.

```lean
lemma fieldStrength_mem_massWeightEigenspace (μ ν : Fin 1 ⊕ Fin 3)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ GaugeAlgebra) :
    GaugeAlgebraRealization.fieldStrength h.A μ ν s φ ∈
      massWeightEigenspace massWeightPoly (4 + 2 * Multiset.card s)
```

**`StandardModel.AlgebraRealization.iteratedCovDerivAdjoint_mem_massWeightEigenspace`**, a lemma, [line 687](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L687).

> The mass weight of an adjoint covariant tower: the adjoint analogue of
> `Species.covDerivIter_mem_massWeightEigenspace`, with the bracket pairing in place of
> the action pairing.

```lean
lemma iteratedCovDerivAdjoint_mem_massWeightEigenspace (c : ℕ)
    (G : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (hG : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℝ GaugeAlgebra),
      G t χ ∈ massWeightEigenspace massWeightPoly (c + 2 * Multiset.card t))
    (l : List (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ GaugeAlgebra) :
    GaugeAlgebraRealization.iteratedCovDerivAdjoint h.A l G s φ ∈
      massWeightEigenspace massWeightPoly (c + 2 * l.length + 2 * Multiset.card s)
```

### H.1. The mass weights, species by species

> The two towers of section H, evaluated at the empty derivative multiset, give the
> mass weights that `IsGaugeSector`, `HiggsAlgebraCovRealization` and `IsFermionSector`
> demand: `2 * (2 + n)` for the field strength (`massWeight_covF`), `2 * (1 + n)` for the
> Higgs (`massWeight_covDerivH`) and `3 + 2 * n` for the fermions (`massWeight_covDerivD`
> and its companions), the matter cases each being `Species.massWeight_tower` at the
> corresponding species.

**`StandardModel.AlgebraRealization.massWeight_covF`**, a lemma, [line 739](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L739).

> The mass weight of the field-strength tower is `2 * (2 + n)`: mass dimension `2 + n`.

```lean
lemma massWeight_covF (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ GaugeAlgebra) :
    massWeightPoly (h.covF l μ ν φ) = Polynomial.monomial (2 * (2 + n)) (h.covF l μ ν φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivH`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L746).

```lean
lemma massWeight_covDerivH (φ : Module.Dual ℂ HiggsVec) :
    massWeightPoly (h.covDerivH l φ) = Polynomial.monomial (2 * (1 + n)) (h.covDerivH l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivBarH`**, a lemma, [line 751](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L751).

```lean
lemma massWeight_covDerivBarH (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    massWeightPoly (h.covDerivBarH l φ) =
      Polynomial.monomial (2 * (1 + n)) (h.covDerivBarH l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivD`**, a lemma, [line 757](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L757).

```lean
lemma massWeight_covDerivD (φ : Module.Dual ℂ DownSinglet) :
    massWeightPoly (h.covDerivD i l φ) = Polynomial.monomial (3 + 2 * n) (h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivBarD`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L761).

```lean
lemma massWeight_covDerivBarD (φ : Module.Dual ℂ (ConjModule DownSinglet)) :
    massWeightPoly (h.covDerivBarD i l φ) =
      Polynomial.monomial (3 + 2 * n) (h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivU`**, a lemma, [line 766](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L766).

```lean
lemma massWeight_covDerivU (φ : Module.Dual ℂ UpSinglet) :
    massWeightPoly (h.covDerivU i l φ) = Polynomial.monomial (3 + 2 * n) (h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivBarU`**, a lemma, [line 770](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L770).

```lean
lemma massWeight_covDerivBarU (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    massWeightPoly (h.covDerivBarU i l φ) =
      Polynomial.monomial (3 + 2 * n) (h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivQ`**, a lemma, [line 775](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L775).

```lean
lemma massWeight_covDerivQ (φ : Module.Dual ℂ QuarkDoublet) :
    massWeightPoly (h.covDerivQ i l φ) = Polynomial.monomial (3 + 2 * n) (h.covDerivQ i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivBarQ`**, a lemma, [line 779](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L779).

```lean
lemma massWeight_covDerivBarQ (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    massWeightPoly (h.covDerivBarQ i l φ) =
      Polynomial.monomial (3 + 2 * n) (h.covDerivBarQ i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivL`**, a lemma, [line 784](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L784).

```lean
lemma massWeight_covDerivL (φ : Module.Dual ℂ LeptonDoubletV) :
    massWeightPoly (h.covDerivL i l φ) = Polynomial.monomial (3 + 2 * n) (h.covDerivL i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivBarL`**, a lemma, [line 788](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L788).

```lean
lemma massWeight_covDerivBarL (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    massWeightPoly (h.covDerivBarL i l φ) =
      Polynomial.monomial (3 + 2 * n) (h.covDerivBarL i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivE`**, a lemma, [line 793](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L793).

```lean
lemma massWeight_covDerivE (φ : Module.Dual ℂ LeptonSinglet) :
    massWeightPoly (h.covDerivE i l φ) = Polynomial.monomial (3 + 2 * n) (h.covDerivE i l φ)
```

**`StandardModel.AlgebraRealization.massWeight_covDerivBarE`**, a lemma, [line 797](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L797).

```lean
lemma massWeight_covDerivBarE (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    massWeightPoly (h.covDerivBarE i l φ) =
      Polynomial.monomial (3 + 2 * n) (h.covDerivBarE i l φ)
```

## I. The statistics of the covariant towers

> Every covariant tower is a polynomial in the gauge-field symbols and the bare symbols of
> its own species, and each of its terms carries exactly one of the latter. So the statistics
> of a pair of towers is decided by the statistics of the pair of bare families: two towers
> whose bare symbols commute with the gauge field and with each other commute, and two whose
> bare symbols commute with the gauge field and anticommute with each other anticommute. The
> anticommutation is checked term by term, through the submodule of elements anticommuting
> with a fixed one.

**`StandardModel.AlgebraRealization.anticommuteSubmodule`**, a def, [line 820](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L820).

> The elements of the algebra anticommuting with a fixed element. It is a submodule,
> which is what lets the anticommutation of a tower be checked term by term.

```lean
def anticommuteSubmodule (x : B) : Submodule ℂ B
```

**`StandardModel.AlgebraRealization.mem_anticommuteSubmodule_iff`**, a lemma, [line 829](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L829).

> Membership of the anticommutant is the anticommutation relation itself.

```lean
lemma mem_anticommuteSubmodule_iff {x y : B} :
    y ∈ anticommuteSubmodule x ↔ x * y = -(y * x)
```

**`StandardModel.AlgebraRealization.anticomm_symm`**, a lemma, [line 834](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L834).

> Anticommutation is symmetric in its two arguments.

```lean
lemma anticomm_symm {a b : B} (hab : a * b = -(b * a)) : b * a = -(a * b)
```

**`StandardModel.AlgebraRealization.mul_mem_anticommuteSubmodule`**, a lemma, [line 839](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L839).

> Multiplying an anticommuting element on the left by a commuting one keeps it
> anticommuting.

```lean
lemma mul_mem_anticommuteSubmodule {x a b : B} (ha : Commute x a)
    (hb : b ∈ anticommuteSubmodule x) : a * b ∈ anticommuteSubmodule x
```

**`StandardModel.AlgebraRealization.Species.commute_tower`**, a lemma, [line 851](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L851).

> Anything commuting with every gauge-field symbol and with every bare symbol of the
> species commutes with its tower.

```lean
lemma commute_tower {y : B}
    (hyA : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra),
      Commute (h.A p μ ψ) y)
    (hyF : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V), Commute (S.F t χ) y)
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) : Commute (S.tower l φ) y
```

**`StandardModel.AlgebraRealization.Species.commute_tower_tower`**, a lemma, [line 863](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L863).

> The towers of two species whose bare families commute with each other commute. The
> hypothesis is stated in the shape of the bare laws `H_comm_d`.

```lean
lemma commute_tower_tower (T : h.Species W)
    (hST : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V) (t' : Multiset (Fin 1 ⊕ Fin 3))
      (χ' : Module.Dual ℂ W), Commute (S.F t χ) (T.F t' χ'))
    {n m : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V)
    (l' : Fin m → (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ W) :
    Commute (S.tower l φ) (T.tower l' φ')
```

**`StandardModel.AlgebraRealization.Species.anticomm_tower`**, a lemma, [line 876](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L876).

> Anything commuting with every gauge-field symbol and anticommuting with every bare
> symbol of the species anticommutes with its tower: each term of the tower is a product
> of gauge-field symbols with a single bare symbol.

```lean
lemma anticomm_tower {x : B}
    (hxA : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ GaugeAlgebra),
      Commute x (h.A p μ ψ))
    (hxF : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V), x * S.F t χ = -(S.F t χ * x))
    {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    x * S.tower l φ = -(S.tower l φ * x)
```

**`StandardModel.AlgebraRealization.Species.anticomm_tower_tower`**, a lemma, [line 902](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L902).

> The towers of two species whose bare families anticommute with each other
> anticommute. The hypothesis is stated in the shape of the bare laws `d_anticomm_bard`.

```lean
lemma anticomm_tower_tower (T : h.Species W)
    (hST : ∀ (t t' : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℂ V) (χ' : Module.Dual ℂ W),
      S.F t χ * T.F t' χ' = -(T.F t' χ' * S.F t χ))
    {n m : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V)
    (l' : Fin m → (Fin 1 ⊕ Fin 3)) (φ' : Module.Dual ℂ W) :
    S.tower l φ * T.tower l' φ' = -(T.tower l' φ' * S.tower l φ)
```

**`StandardModel.AlgebraRealization.Species.covF_comm_tower`**, a lemma, [line 913](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L913).

> The field-strength tower commutes with the tower of every species.

```lean
lemma covF_comm_tower {k n : ℕ} (l : Fin k → (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (ψ : Module.Dual ℝ GaugeAlgebra) (l' : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ V) :
    Commute (h.covF l μ ν ψ) (S.tower l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covF`**, a lemma, [line 922](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L922).

> Two field-strength towers commute: both are polynomials in the gauge-field symbols,
> and the gauge field is bosonic.

```lean
lemma covF_comm_covF {n m : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (l' : Fin m → (Fin 1 ⊕ Fin 3)) (μ ν μ' ν' : Fin 1 ⊕ Fin 3)
    (ψ ψ' : Module.Dual ℝ GaugeAlgebra) :
    Commute (h.covF l μ ν ψ) (h.covF l' μ' ν' ψ')
```

### I.1. The statistics, species by species

> The field-strength tower is central; the Higgs towers are bosonic and commute with
> everything; the fermion towers anticommute with one another. These are exactly the
> commutation obligations of the three sector structures: `covF_comm_covX` for the
> field-strength tower against the tower of the species `X`, `covH_comm_covX` and
> `covBarH_comm_covX` for the two Higgs towers, and `covX_anticomm_covY` for each pair of
> fermion species — each `Species.covF_comm_tower`, `Species.commute_tower_tower` or
> `Species.anticomm_tower_tower` at the corresponding species, fed the bare law of the pair.

**`StandardModel.AlgebraRealization.covF_comm_covH`**, a lemma, [line 948](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L948).

```lean
lemma covF_comm_covH (φ : Module.Dual ℂ HiggsVec) :
    Commute (h.covF l μ ν ψ) (h.covDerivH l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covBarH`**, a lemma, [line 952](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L952).

```lean
lemma covF_comm_covBarH (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    Commute (h.covF l μ ν ψ) (h.covDerivBarH l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covD`**, a lemma, [line 956](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L956).

```lean
lemma covF_comm_covD (φ : Module.Dual ℂ DownSinglet) :
    Commute (h.covF l μ ν ψ) (h.covDerivD i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covBarD`**, a lemma, [line 960](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L960).

```lean
lemma covF_comm_covBarD (φ : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (h.covF l μ ν ψ) (h.covDerivBarD i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covU`**, a lemma, [line 964](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L964).

```lean
lemma covF_comm_covU (φ : Module.Dual ℂ UpSinglet) :
    Commute (h.covF l μ ν ψ) (h.covDerivU i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covBarU`**, a lemma, [line 968](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L968).

```lean
lemma covF_comm_covBarU (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (h.covF l μ ν ψ) (h.covDerivBarU i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covQ`**, a lemma, [line 972](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L972).

```lean
lemma covF_comm_covQ (φ : Module.Dual ℂ QuarkDoublet) :
    Commute (h.covF l μ ν ψ) (h.covDerivQ i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covBarQ`**, a lemma, [line 976](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L976).

```lean
lemma covF_comm_covBarQ (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (h.covF l μ ν ψ) (h.covDerivBarQ i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covL`**, a lemma, [line 980](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L980).

```lean
lemma covF_comm_covL (φ : Module.Dual ℂ LeptonDoubletV) :
    Commute (h.covF l μ ν ψ) (h.covDerivL i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covBarL`**, a lemma, [line 984](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L984).

```lean
lemma covF_comm_covBarL (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (h.covF l μ ν ψ) (h.covDerivBarL i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covE`**, a lemma, [line 988](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L988).

```lean
lemma covF_comm_covE (φ : Module.Dual ℂ LeptonSinglet) :
    Commute (h.covF l μ ν ψ) (h.covDerivE i l' φ)
```

**`StandardModel.AlgebraRealization.covF_comm_covBarE`**, a lemma, [line 992](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L992).

```lean
lemma covF_comm_covBarE (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (h.covF l μ ν ψ) (h.covDerivBarE i l' φ)
```

**`StandardModel.AlgebraRealization.covH_comm_covH`**, a lemma, [line 1002](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1002).

```lean
lemma covH_comm_covH (φ φ' : Module.Dual ℂ HiggsVec) :
    Commute (h.covDerivH l φ) (h.covDerivH l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covBarH`**, a lemma, [line 1006](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1006).

```lean
lemma covH_comm_covBarH (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ (ConjModule HiggsVec)) :
    Commute (h.covDerivH l φ) (h.covDerivBarH l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covBarH`**, a lemma, [line 1010](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1010).

```lean
lemma covBarH_comm_covBarH (φ φ' : Module.Dual ℂ (ConjModule HiggsVec)) :
    Commute (h.covDerivBarH l φ) (h.covDerivBarH l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covD`**, a lemma, [line 1015](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1015).

```lean
lemma covH_comm_covD (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ DownSinglet) :
    Commute (h.covDerivH l φ) (h.covDerivD i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covBarD`**, a lemma, [line 1019](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1019).

```lean
lemma covH_comm_covBarD (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (h.covDerivH l φ) (h.covDerivBarD i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covU`**, a lemma, [line 1023](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1023).

```lean
lemma covH_comm_covU (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ UpSinglet) :
    Commute (h.covDerivH l φ) (h.covDerivU i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covBarU`**, a lemma, [line 1027](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1027).

```lean
lemma covH_comm_covBarU (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (h.covDerivH l φ) (h.covDerivBarU i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covQ`**, a lemma, [line 1031](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1031).

```lean
lemma covH_comm_covQ (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ QuarkDoublet) :
    Commute (h.covDerivH l φ) (h.covDerivQ i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covBarQ`**, a lemma, [line 1035](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1035).

```lean
lemma covH_comm_covBarQ (φ : Module.Dual ℂ HiggsVec)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (h.covDerivH l φ) (h.covDerivBarQ i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covL`**, a lemma, [line 1040](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1040).

```lean
lemma covH_comm_covL (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ LeptonDoubletV) :
    Commute (h.covDerivH l φ) (h.covDerivL i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covBarL`**, a lemma, [line 1044](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1044).

```lean
lemma covH_comm_covBarL (φ : Module.Dual ℂ HiggsVec)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (h.covDerivH l φ) (h.covDerivBarL i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covE`**, a lemma, [line 1049](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1049).

```lean
lemma covH_comm_covE (φ : Module.Dual ℂ HiggsVec) (φ' : Module.Dual ℂ LeptonSinglet) :
    Commute (h.covDerivH l φ) (h.covDerivE i l' φ')
```

**`StandardModel.AlgebraRealization.covH_comm_covBarE`**, a lemma, [line 1053](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1053).

```lean
lemma covH_comm_covBarE (φ : Module.Dual ℂ HiggsVec)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (h.covDerivH l φ) (h.covDerivBarE i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covD`**, a lemma, [line 1058](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1058).

```lean
lemma covBarH_comm_covD (φ : Module.Dual ℂ (ConjModule HiggsVec)) (φ' : Module.Dual ℂ DownSinglet) :
    Commute (h.covDerivBarH l φ) (h.covDerivD i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covBarD`**, a lemma, [line 1062](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1062).

```lean
lemma covBarH_comm_covBarD (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    Commute (h.covDerivBarH l φ) (h.covDerivBarD i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covU`**, a lemma, [line 1067](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1067).

```lean
lemma covBarH_comm_covU (φ : Module.Dual ℂ (ConjModule HiggsVec)) (φ' : Module.Dual ℂ UpSinglet) :
    Commute (h.covDerivBarH l φ) (h.covDerivU i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covBarU`**, a lemma, [line 1071](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1071).

```lean
lemma covBarH_comm_covBarU (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    Commute (h.covDerivBarH l φ) (h.covDerivBarU i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covQ`**, a lemma, [line 1076](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1076).

```lean
lemma covBarH_comm_covQ (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ QuarkDoublet) :
    Commute (h.covDerivBarH l φ) (h.covDerivQ i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covBarQ`**, a lemma, [line 1081](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1081).

```lean
lemma covBarH_comm_covBarQ (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    Commute (h.covDerivBarH l φ) (h.covDerivBarQ i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covL`**, a lemma, [line 1086](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1086).

```lean
lemma covBarH_comm_covL (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    Commute (h.covDerivBarH l φ) (h.covDerivL i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covBarL`**, a lemma, [line 1091](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1091).

```lean
lemma covBarH_comm_covBarL (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    Commute (h.covDerivBarH l φ) (h.covDerivBarL i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covE`**, a lemma, [line 1096](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1096).

```lean
lemma covBarH_comm_covE (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ LeptonSinglet) :
    Commute (h.covDerivBarH l φ) (h.covDerivE i l' φ')
```

**`StandardModel.AlgebraRealization.covBarH_comm_covBarE`**, a lemma, [line 1101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1101).

```lean
lemma covBarH_comm_covBarE (φ : Module.Dual ℂ (ConjModule HiggsVec))
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    Commute (h.covDerivBarH l φ) (h.covDerivBarE i l' φ')
```

**`StandardModel.AlgebraRealization.covD_anticomm_covD`**, a lemma, [line 1106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1106).

```lean
lemma covD_anticomm_covD (φ φ' : Module.Dual ℂ DownSinglet) :
    h.covDerivD i l φ * h.covDerivD j l' φ' = -(h.covDerivD j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covBarD`**, a lemma, [line 1110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1110).

```lean
lemma covD_anticomm_covBarD (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    h.covDerivD i l φ * h.covDerivBarD j l' φ' = -(h.covDerivBarD j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covU`**, a lemma, [line 1115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1115).

```lean
lemma covD_anticomm_covU (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ UpSinglet) :
    h.covDerivD i l φ * h.covDerivU j l' φ' = -(h.covDerivU j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covBarU`**, a lemma, [line 1119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1119).

```lean
lemma covD_anticomm_covBarU (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    h.covDerivD i l φ * h.covDerivBarU j l' φ' = -(h.covDerivBarU j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covQ`**, a lemma, [line 1124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1124).

```lean
lemma covD_anticomm_covQ (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ QuarkDoublet) :
    h.covDerivD i l φ * h.covDerivQ j l' φ' = -(h.covDerivQ j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covBarQ`**, a lemma, [line 1128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1128).

```lean
lemma covD_anticomm_covBarQ (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    h.covDerivD i l φ * h.covDerivBarQ j l' φ' = -(h.covDerivBarQ j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covL`**, a lemma, [line 1133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1133).

```lean
lemma covD_anticomm_covL (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ LeptonDoubletV) :
    h.covDerivD i l φ * h.covDerivL j l' φ' = -(h.covDerivL j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covBarL`**, a lemma, [line 1137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1137).

```lean
lemma covD_anticomm_covBarL (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivD i l φ * h.covDerivBarL j l' φ' = -(h.covDerivBarL j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covE`**, a lemma, [line 1142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1142).

```lean
lemma covD_anticomm_covE (φ : Module.Dual ℂ DownSinglet) (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivD i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covD_anticomm_covBarE`**, a lemma, [line 1146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1146).

```lean
lemma covD_anticomm_covBarE (φ : Module.Dual ℂ DownSinglet)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivD i l φ * h.covDerivBarE j l' φ' = -(h.covDerivBarE j l' φ' * h.covDerivD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covBarD`**, a lemma, [line 1151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1151).

```lean
lemma covBarD_anticomm_covBarD (φ φ' : Module.Dual ℂ (ConjModule DownSinglet)) :
    h.covDerivBarD i l φ * h.covDerivBarD j l' φ' =
      -(h.covDerivBarD j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covU`**, a lemma, [line 1156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1156).

```lean
lemma covBarD_anticomm_covU (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ UpSinglet) :
    h.covDerivBarD i l φ * h.covDerivU j l' φ' = -(h.covDerivU j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covBarU`**, a lemma, [line 1161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1161).

```lean
lemma covBarD_anticomm_covBarU (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    h.covDerivBarD i l φ * h.covDerivBarU j l' φ' =
      -(h.covDerivBarU j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covQ`**, a lemma, [line 1167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1167).

```lean
lemma covBarD_anticomm_covQ (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ QuarkDoublet) :
    h.covDerivBarD i l φ * h.covDerivQ j l' φ' = -(h.covDerivQ j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covBarQ`**, a lemma, [line 1172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1172).

```lean
lemma covBarD_anticomm_covBarQ (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    h.covDerivBarD i l φ * h.covDerivBarQ j l' φ' =
      -(h.covDerivBarQ j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covL`**, a lemma, [line 1178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1178).

```lean
lemma covBarD_anticomm_covL (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    h.covDerivBarD i l φ * h.covDerivL j l' φ' = -(h.covDerivL j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covBarL`**, a lemma, [line 1183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1183).

```lean
lemma covBarD_anticomm_covBarL (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivBarD i l φ * h.covDerivBarL j l' φ' =
      -(h.covDerivBarL j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covE`**, a lemma, [line 1189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1189).

```lean
lemma covBarD_anticomm_covE (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivBarD i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covBarD_anticomm_covBarE`**, a lemma, [line 1194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1194).

```lean
lemma covBarD_anticomm_covBarE (φ : Module.Dual ℂ (ConjModule DownSinglet))
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivBarD i l φ * h.covDerivBarE j l' φ' =
      -(h.covDerivBarE j l' φ' * h.covDerivBarD i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covU`**, a lemma, [line 1200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1200).

```lean
lemma covU_anticomm_covU (φ φ' : Module.Dual ℂ UpSinglet) :
    h.covDerivU i l φ * h.covDerivU j l' φ' = -(h.covDerivU j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covBarU`**, a lemma, [line 1204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1204).

```lean
lemma covU_anticomm_covBarU (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    h.covDerivU i l φ * h.covDerivBarU j l' φ' = -(h.covDerivBarU j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covQ`**, a lemma, [line 1209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1209).

```lean
lemma covU_anticomm_covQ (φ : Module.Dual ℂ UpSinglet) (φ' : Module.Dual ℂ QuarkDoublet) :
    h.covDerivU i l φ * h.covDerivQ j l' φ' = -(h.covDerivQ j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covBarQ`**, a lemma, [line 1213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1213).

```lean
lemma covU_anticomm_covBarQ (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    h.covDerivU i l φ * h.covDerivBarQ j l' φ' = -(h.covDerivBarQ j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covL`**, a lemma, [line 1218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1218).

```lean
lemma covU_anticomm_covL (φ : Module.Dual ℂ UpSinglet) (φ' : Module.Dual ℂ LeptonDoubletV) :
    h.covDerivU i l φ * h.covDerivL j l' φ' = -(h.covDerivL j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covBarL`**, a lemma, [line 1222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1222).

```lean
lemma covU_anticomm_covBarL (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivU i l φ * h.covDerivBarL j l' φ' = -(h.covDerivBarL j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covE`**, a lemma, [line 1227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1227).

```lean
lemma covU_anticomm_covE (φ : Module.Dual ℂ UpSinglet) (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivU i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covU_anticomm_covBarE`**, a lemma, [line 1231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1231).

```lean
lemma covU_anticomm_covBarE (φ : Module.Dual ℂ UpSinglet)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivU i l φ * h.covDerivBarE j l' φ' = -(h.covDerivBarE j l' φ' * h.covDerivU i l φ)
```

**`StandardModel.AlgebraRealization.covBarU_anticomm_covBarU`**, a lemma, [line 1236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1236).

```lean
lemma covBarU_anticomm_covBarU (φ φ' : Module.Dual ℂ (ConjModule UpSinglet)) :
    h.covDerivBarU i l φ * h.covDerivBarU j l' φ' =
      -(h.covDerivBarU j l' φ' * h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.covBarU_anticomm_covQ`**, a lemma, [line 1241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1241).

```lean
lemma covBarU_anticomm_covQ (φ : Module.Dual ℂ (ConjModule UpSinglet))
    (φ' : Module.Dual ℂ QuarkDoublet) :
    h.covDerivBarU i l φ * h.covDerivQ j l' φ' = -(h.covDerivQ j l' φ' * h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.covBarU_anticomm_covBarQ`**, a lemma, [line 1246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1246).

```lean
lemma covBarU_anticomm_covBarQ (φ : Module.Dual ℂ (ConjModule UpSinglet))
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    h.covDerivBarU i l φ * h.covDerivBarQ j l' φ' =
      -(h.covDerivBarQ j l' φ' * h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.covBarU_anticomm_covL`**, a lemma, [line 1252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1252).

```lean
lemma covBarU_anticomm_covL (φ : Module.Dual ℂ (ConjModule UpSinglet))
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    h.covDerivBarU i l φ * h.covDerivL j l' φ' = -(h.covDerivL j l' φ' * h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.covBarU_anticomm_covBarL`**, a lemma, [line 1257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1257).

```lean
lemma covBarU_anticomm_covBarL (φ : Module.Dual ℂ (ConjModule UpSinglet))
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivBarU i l φ * h.covDerivBarL j l' φ' =
      -(h.covDerivBarL j l' φ' * h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.covBarU_anticomm_covE`**, a lemma, [line 1263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1263).

```lean
lemma covBarU_anticomm_covE (φ : Module.Dual ℂ (ConjModule UpSinglet))
    (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivBarU i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.covBarU_anticomm_covBarE`**, a lemma, [line 1268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1268).

```lean
lemma covBarU_anticomm_covBarE (φ : Module.Dual ℂ (ConjModule UpSinglet))
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivBarU i l φ * h.covDerivBarE j l' φ' =
      -(h.covDerivBarE j l' φ' * h.covDerivBarU i l φ)
```

**`StandardModel.AlgebraRealization.covQ_anticomm_covQ`**, a lemma, [line 1274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1274).

```lean
lemma covQ_anticomm_covQ (φ φ' : Module.Dual ℂ QuarkDoublet) :
    h.covDerivQ i l φ * h.covDerivQ j l' φ' = -(h.covDerivQ j l' φ' * h.covDerivQ i l φ)
```

**`StandardModel.AlgebraRealization.covQ_anticomm_covBarQ`**, a lemma, [line 1278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1278).

```lean
lemma covQ_anticomm_covBarQ (φ : Module.Dual ℂ QuarkDoublet)
    (φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    h.covDerivQ i l φ * h.covDerivBarQ j l' φ' = -(h.covDerivBarQ j l' φ' * h.covDerivQ i l φ)
```

**`StandardModel.AlgebraRealization.covQ_anticomm_covL`**, a lemma, [line 1283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1283).

```lean
lemma covQ_anticomm_covL (φ : Module.Dual ℂ QuarkDoublet) (φ' : Module.Dual ℂ LeptonDoubletV) :
    h.covDerivQ i l φ * h.covDerivL j l' φ' = -(h.covDerivL j l' φ' * h.covDerivQ i l φ)
```

**`StandardModel.AlgebraRealization.covQ_anticomm_covBarL`**, a lemma, [line 1287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1287).

```lean
lemma covQ_anticomm_covBarL (φ : Module.Dual ℂ QuarkDoublet)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivQ i l φ * h.covDerivBarL j l' φ' = -(h.covDerivBarL j l' φ' * h.covDerivQ i l φ)
```

**`StandardModel.AlgebraRealization.covQ_anticomm_covE`**, a lemma, [line 1292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1292).

```lean
lemma covQ_anticomm_covE (φ : Module.Dual ℂ QuarkDoublet) (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivQ i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivQ i l φ)
```

**`StandardModel.AlgebraRealization.covQ_anticomm_covBarE`**, a lemma, [line 1296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1296).

```lean
lemma covQ_anticomm_covBarE (φ : Module.Dual ℂ QuarkDoublet)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivQ i l φ * h.covDerivBarE j l' φ' = -(h.covDerivBarE j l' φ' * h.covDerivQ i l φ)
```

**`StandardModel.AlgebraRealization.covBarQ_anticomm_covBarQ`**, a lemma, [line 1301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1301).

```lean
lemma covBarQ_anticomm_covBarQ (φ φ' : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    h.covDerivBarQ i l φ * h.covDerivBarQ j l' φ' =
      -(h.covDerivBarQ j l' φ' * h.covDerivBarQ i l φ)
```

**`StandardModel.AlgebraRealization.covBarQ_anticomm_covL`**, a lemma, [line 1306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1306).

```lean
lemma covBarQ_anticomm_covL (φ : Module.Dual ℂ (ConjModule QuarkDoublet))
    (φ' : Module.Dual ℂ LeptonDoubletV) :
    h.covDerivBarQ i l φ * h.covDerivL j l' φ' = -(h.covDerivL j l' φ' * h.covDerivBarQ i l φ)
```

**`StandardModel.AlgebraRealization.covBarQ_anticomm_covBarL`**, a lemma, [line 1311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1311).

```lean
lemma covBarQ_anticomm_covBarL (φ : Module.Dual ℂ (ConjModule QuarkDoublet))
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivBarQ i l φ * h.covDerivBarL j l' φ' =
      -(h.covDerivBarL j l' φ' * h.covDerivBarQ i l φ)
```

**`StandardModel.AlgebraRealization.covBarQ_anticomm_covE`**, a lemma, [line 1317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1317).

```lean
lemma covBarQ_anticomm_covE (φ : Module.Dual ℂ (ConjModule QuarkDoublet))
    (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivBarQ i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivBarQ i l φ)
```

**`StandardModel.AlgebraRealization.covBarQ_anticomm_covBarE`**, a lemma, [line 1322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1322).

```lean
lemma covBarQ_anticomm_covBarE (φ : Module.Dual ℂ (ConjModule QuarkDoublet))
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivBarQ i l φ * h.covDerivBarE j l' φ' =
      -(h.covDerivBarE j l' φ' * h.covDerivBarQ i l φ)
```

**`StandardModel.AlgebraRealization.covL_anticomm_covL`**, a lemma, [line 1328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1328).

```lean
lemma covL_anticomm_covL (φ φ' : Module.Dual ℂ LeptonDoubletV) :
    h.covDerivL i l φ * h.covDerivL j l' φ' = -(h.covDerivL j l' φ' * h.covDerivL i l φ)
```

**`StandardModel.AlgebraRealization.covL_anticomm_covBarL`**, a lemma, [line 1332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1332).

```lean
lemma covL_anticomm_covBarL (φ : Module.Dual ℂ LeptonDoubletV)
    (φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivL i l φ * h.covDerivBarL j l' φ' = -(h.covDerivBarL j l' φ' * h.covDerivL i l φ)
```

**`StandardModel.AlgebraRealization.covL_anticomm_covE`**, a lemma, [line 1337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1337).

```lean
lemma covL_anticomm_covE (φ : Module.Dual ℂ LeptonDoubletV) (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivL i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivL i l φ)
```

**`StandardModel.AlgebraRealization.covL_anticomm_covBarE`**, a lemma, [line 1341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1341).

```lean
lemma covL_anticomm_covBarE (φ : Module.Dual ℂ LeptonDoubletV)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivL i l φ * h.covDerivBarE j l' φ' = -(h.covDerivBarE j l' φ' * h.covDerivL i l φ)
```

**`StandardModel.AlgebraRealization.covBarL_anticomm_covBarL`**, a lemma, [line 1346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1346).

```lean
lemma covBarL_anticomm_covBarL (φ φ' : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    h.covDerivBarL i l φ * h.covDerivBarL j l' φ' =
      -(h.covDerivBarL j l' φ' * h.covDerivBarL i l φ)
```

**`StandardModel.AlgebraRealization.covBarL_anticomm_covE`**, a lemma, [line 1351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1351).

```lean
lemma covBarL_anticomm_covE (φ : Module.Dual ℂ (ConjModule LeptonDoubletV))
    (φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivBarL i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivBarL i l φ)
```

**`StandardModel.AlgebraRealization.covBarL_anticomm_covBarE`**, a lemma, [line 1356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1356).

```lean
lemma covBarL_anticomm_covBarE (φ : Module.Dual ℂ (ConjModule LeptonDoubletV))
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivBarL i l φ * h.covDerivBarE j l' φ' =
      -(h.covDerivBarE j l' φ' * h.covDerivBarL i l φ)
```

**`StandardModel.AlgebraRealization.covE_anticomm_covE`**, a lemma, [line 1362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1362).

```lean
lemma covE_anticomm_covE (φ φ' : Module.Dual ℂ LeptonSinglet) :
    h.covDerivE i l φ * h.covDerivE j l' φ' = -(h.covDerivE j l' φ' * h.covDerivE i l φ)
```

**`StandardModel.AlgebraRealization.covE_anticomm_covBarE`**, a lemma, [line 1366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1366).

```lean
lemma covE_anticomm_covBarE (φ : Module.Dual ℂ LeptonSinglet)
    (φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivE i l φ * h.covDerivBarE j l' φ' = -(h.covDerivBarE j l' φ' * h.covDerivE i l φ)
```

**`StandardModel.AlgebraRealization.covBarE_anticomm_covBarE`**, a lemma, [line 1371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1371).

```lean
lemma covBarE_anticomm_covBarE (φ φ' : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    h.covDerivBarE i l φ * h.covDerivBarE j l' φ' =
      -(h.covDerivBarE j l' φ' * h.covDerivBarE i l φ)
```

## J. The Lorentz law of the field-strength tower

> The Lorentz laws of the matter towers are section L of
> [`CovariantDeriv.lean`](../part-09/realization-covariantderiv.md); the one for the field-strength tower is
> `repLorentz_covF` just below, which is
> `GaugeAlgebraRealization.repLorentz_iteratedCovDerivAdjoint_fieldStrength` read in the
> ordered-tuple indexing.

**`StandardModel.AlgebraRealization.repLorentz_covF`**, a lemma, [line 1393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean#L1393).

> The Lorentz law of the covariant field-strength tower: the covariant derivative
> slots mix by their own columns of the Lorentz matrix, and the two covector indices
> of the field strength mix by theirs.

```lean
lemma repLorentz_covF (Λ : SL(2,ℂ)) (n : ℕ) (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ GaugeAlgebra) :
    repLorentz Λ (h.covF l μ ν φ) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
        (∏ i, (((SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ) : ℂ)) •
      ∑ a, (((SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
      ∑ b, (((SL2C.toLorentzGroup Λ).1 b ν : ℝ) : ℂ) • h.covF p a b φ
```

## Depends on

- [The statistics of the Standard Model fields](../part-09/realization-commutations.md)
- [The covariant field algebra](realization-covfieldalgebra-basic.md)
- [The mass weights of the fields of an algebra realization](../part-11/realization-massweight-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Realization/CovStandardModel.lean)
