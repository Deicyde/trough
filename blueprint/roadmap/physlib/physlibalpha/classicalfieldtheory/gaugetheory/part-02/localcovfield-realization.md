---
declaration: module
origin: cited
lean: GaugeFieldData.LocalCovFieldAlgebra.Realization, GaugeFieldData.LocalCovFieldAlgebra.Realization.id, GaugeFieldData.LocalCovFieldAlgebra.Realization.id_toAlgHom, GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repValue, GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repLorentz, GaugeFieldData.LocalCovFieldAlgebra.Realization.repGauge_mul, GaugeFieldData.LocalCovFieldAlgebra.Realization.repLorentz_mul, GaugeFieldData.LocalCovFieldAlgebra.Realization.fieldStrength
statement: formalized
proof: formalized
---

# Realizations of the covariant field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalCovField.Realization`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean): 46 declarations, 22 with a docstring.

## i. Overview

> A complex algebra `B` carries the covariant expressions of a gauge-field datum when the
> covariant field algebra maps into it by a complex algebra map equivariant for the ordinary
> gauge group `G₀` and for the Lorentz group, both acting on `B` by algebra endomorphisms:
> `GaugeFieldData.LocalCovFieldAlgebra.Realization`. The gauge compatibility is with `G₀`
> alone because the source action of the ordinary gauge group is the jet action at the
> constant jets; the Lorentz action of the source exists only under
> `GaugeFieldData.GaugeLorentzCompatible`, which the structure therefore carries.
>
> The covariant field algebra is a subalgebra of `J(T)` and is not free on its five towers,
> so a realization is its algebra map and not an assignment of the towers; generation gives
> uniqueness only (`Realization.ext_towers`). A realization of the local field algebra
> restricts to one of the covariant field algebra
> (`GaugeFieldData.Realization.restrict`), with `G₀` acting on the target through the
> constant jets. The converse extension is not claimed.
>
> Under `GaugeFieldData.PureJetsActTrivially` the jet action factors through evaluation on
> the realized covariant image, in the two forms of section D. That hypothesis is needed
> nowhere else.

## ii. Key results

> - `GaugeFieldData.LocalCovFieldAlgebra.Realization` : an algebra carrying the covariant
>   towers, with the tower images `fieldStrength`, `fermion`, `conjFermion`, `boson`,
>   `conjBoson` and their gauge and Lorentz laws.
> - `GaugeFieldData.Realization.restrict` : restriction to the covariant field algebra, with
>   `restrict_fieldStrength_eq_iteratedCovDerivAdjoint` and
>   `restrict_fermion_eq_covDerivIter` identifying its towers.
> - `GaugeFieldData.Realization.repJet_restrict_toAlgHom` and
>   `GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repJet` : the factorization through
>   evaluation under `GaugeFieldData.PureJetsActTrivially`.

## iv. References

> * None.

## A. Realizations

**`GaugeFieldData.LocalCovFieldAlgebra.Realization`**, an abbrev, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L91).

> A complex algebra `B` carrying the covariant expressions of the datum `T`: a complex
> algebra map out of the covariant field algebra, equivariant for the ordinary gauge group
> and the Lorentz group, both acting on the whole of `B` by algebra endomorphisms. The
> Lorentz action of the source needs `GaugeFieldData.GaugeLorentzCompatible`, which is a
> parameter; no other species condition is used. It is built from the fields `toAlgHom`,
> `map_fst`, `map_snd`, `fst_mul`, `snd_mul` of `Representation.EquivariantAlgHom`, which
> the lemmas `map_repValue`, `map_repLorentz`, `repGauge_mul` and `repLorentz_mul` name.

```lean
abbrev Realization (T : GaugeFieldData jets) (hGL : T.GaugeLorentzCompatible) (B : Type)
    [Semiring B] [Algebra ℂ B] (repGauge : Representation ℂ G₀ B)
    (repLorentz : Representation ℂ SL(2,ℂ) B)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.id`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L103).

> The covariant field algebra realized in itself, by the identity.

```lean
noncomputable def id : Realization T hGL (↥T.LocalCovFieldAlgebra) (repValue T)
    (repLorentzGroup T hGL)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.id_toAlgHom`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L108).

```lean
lemma id_toAlgHom : (id T hGL).toAlgHom = AlgHom.id ℂ ↥T.LocalCovFieldAlgebra
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repValue`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L113).

> The map is equivariant for the ordinary gauge group.

```lean
lemma map_repValue (g : G₀) (x : ↥T.LocalCovFieldAlgebra) :
    k.toAlgHom (repValue T g x) = repGauge g (k.toAlgHom x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repLorentz`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L118).

> The map is equivariant for the Lorentz group.

```lean
lemma map_repLorentz (Λ : SL(2,ℂ)) (x : ↥T.LocalCovFieldAlgebra) :
    k.toAlgHom (repLorentzGroup T hGL Λ x) = repLorentz Λ (k.toAlgHom x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.repGauge_mul`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L124).

> The ordinary gauge group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repGauge_mul (g : G₀) (b₁ b₂ : B) :
    repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.repLorentz_mul`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L130).

> The Lorentz group acts on the whole of `B` by algebra endomorphisms.

```lean
lemma repLorentz_mul (Λ : SL(2,ℂ)) (b₁ b₂ : B) :
    repLorentz Λ (b₁ * b₂) = repLorentz Λ b₁ * repLorentz Λ b₂
```

## B. The covariant towers of a realization

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.fieldStrength`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L141).

> The realized field-strength tower `∇_l F_μν^φ`.

```lean
noncomputable def fieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) : B
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.fermion`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L146).

> The realized covariant tower `∇_l ψ^φ` of a fermionic species.

```lean
noncomputable def fermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.FermionValue i) →ₗ[ℂ] B
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.conjFermion`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L151).

> The realized conjugate covariant tower of a fermionic species.

```lean
noncomputable def conjFermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.FermionValue i)) →ₗ[ℂ] B
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.boson`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L156).

> The realized covariant tower of a bosonic species.

```lean
noncomputable def boson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (T.BosonValue j) →ₗ[ℂ] B
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.conjBoson`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L161).

> The realized conjugate covariant tower of a bosonic species.

```lean
noncomputable def conjBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℂ (ConjModule (T.BosonValue j)) →ₗ[ℂ] B
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.fermion_apply`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L165).

```lean
lemma fermion_apply (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    k.fermion i l φ = k.toAlgHom (covFermion T i l φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.conjFermion_apply`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L169).

```lean
lemma conjFermion_apply (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    k.conjFermion i l φ = k.toAlgHom (covConjFermion T i l φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.boson_apply`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L173).

```lean
lemma boson_apply (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    k.boson j l φ = k.toAlgHom (covBoson T j l φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.conjBoson_apply`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L177).

```lean
lemma conjBoson_apply (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    k.conjBoson j l φ = k.toAlgHom (covConjBoson T j l φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.id_fermion`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L182).

```lean
lemma id_fermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    (id T hGL).fermion i l = covFermion T i l
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.id_fieldStrength`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L186).

```lean
lemma id_fieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    (id T hGL).fieldStrength l μ ν = covFieldStrength T l μ ν
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.ext_towers`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L192).

> Two realizations with the same five towers are equal. This is uniqueness only: the
> covariant field algebra is not free on its towers, so an assignment of the tower images
> does not by itself define a realization.

```lean
lemma ext_towers {k₁ k₂ : Realization T hGL B repGauge repLorentz}
    (hF : ∀ (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤),
      k₁.fieldStrength l μ ν φ = k₂.fieldStrength l μ ν φ)
    (hψ : ∀ (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (T.FermionValue i)), k₁.fermion i l φ = k₂.fermion i l φ)
    (hψc : ∀ (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))),
      k₁.conjFermion i l φ = k₂.conjFermion i l φ)
    (hφ : ∀ (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (T.BosonValue j)), k₁.boson j l φ = k₂.boson j l φ)
    (hφc : ∀ (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))),
      k₁.conjBoson j l φ = k₂.conjBoson j l φ) : k₁ = k₂
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.gauge_fieldStrength`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L209).

> The gauge law of the realized field-strength tower: the adjoint index rotates through
> the dual adjoint action of the inverse.

```lean
lemma gauge_fieldStrength (g : G₀) (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repGauge g (k.fieldStrength l μ ν φ)
      = k.fieldStrength l μ ν ((jets.adjoint g⁻¹).dualMap φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.gauge_fermion`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L221).

> The gauge law of a realized matter tower: the value index rotates through the zeroth
> dual Taylor coefficient of the inverse constant jet.

```lean
lemma gauge_fermion (g : G₀) (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    repGauge g (k.fermion i l φ)
      = k.fermion i l (repDualCoeff (T.fermion i).repJet (jets.ofConstant g)⁻¹ 0 φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.gauge_conjFermion`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L228).

```lean
lemma gauge_conjFermion (g : G₀) (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    repGauge g (k.conjFermion i l φ) = k.conjFermion i l
      (repDualCoeff (JetComponentSpace.repConj (T.fermion i).repJet)
        (jets.ofConstant g)⁻¹ 0 φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.gauge_boson`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L236).

```lean
lemma gauge_boson (g : G₀) (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    repGauge g (k.boson j l φ)
      = k.boson j l (repDualCoeff (T.boson j).repJet (jets.ofConstant g)⁻¹ 0 φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.gauge_conjBoson`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L243).

```lean
lemma gauge_conjBoson (g : G₀) (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    repGauge g (k.conjBoson j l φ) = k.conjBoson j l
      (repDualCoeff (JetComponentSpace.repConj (T.boson j).repJet)
        (jets.ofConstant g)⁻¹ 0 φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.lorentz_fieldStrength`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L253).

> The Lorentz law of the realized field-strength tower: every covariant slot and both
> covector indices mix by the columns of the Lorentz matrix.

```lean
lemma lorentz_fieldStrength (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repLorentz Λ (k.fieldStrength (List.ofFn l) μ ν φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ a, L[Λ] (p a) (l a)) •
          ∑ a, L[Λ] a μ • ∑ b, L[Λ] b ν • k.fieldStrength (List.ofFn p) a b φ
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.lorentz_fermion`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L271).

> The Lorentz law of a realized matter tower: every covariant slot mixes by the columns of
> the Lorentz matrix and the value index transforms contragrediently.

```lean
lemma lorentz_fermion (Λ : SL(2,ℂ)) (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    repLorentz Λ (k.fermion i l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ a, L[Λ] (p a) (l a)) •
          k.fermion i p ((T.fermion i).repLorentz.dual Λ φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.lorentz_conjFermion`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L281).

```lean
lemma lorentz_conjFermion (Λ : SL(2,ℂ)) (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    repLorentz Λ (k.conjFermion i l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ a, L[Λ] (p a) (l a)) •
          k.conjFermion i p ((T.fermion i).repLorentz.conj.dual Λ φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.lorentz_boson`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L291).

```lean
lemma lorentz_boson (Λ : SL(2,ℂ)) (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)) :
    repLorentz Λ (k.boson j l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ a, L[Λ] (p a) (l a)) •
          k.boson j p ((T.boson j).repLorentz.dual Λ φ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.lorentz_conjBoson`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L301).

```lean
lemma lorentz_conjBoson (Λ : SL(2,ℂ)) (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    repLorentz Λ (k.conjBoson j l φ)
      = ∑ p : Fin n → (Fin 1 ⊕ Fin 3), (∏ a, L[Λ] (p a) (l a)) •
          k.conjBoson j p ((T.boson j).repLorentz.conj.dual Λ φ)
```

## C. Restriction from the local field algebra

**`GaugeFieldData.Realization.restrict`**, a def, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L330).

> The restriction of a realization of the local field algebra to the covariant field
> algebra, along the inclusion; the ordinary gauge group acts on the target through the
> constant jets. No species condition beyond `hGL` is used.

```lean
noncomputable def restrict :
    LocalCovFieldAlgebra.Realization T hGL B (repJet.comp jets.ofConstant) repLorentz
```

**`GaugeFieldData.Realization.restrict_toAlgHom`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L336).

```lean
lemma restrict_toAlgHom : (h.restrict hGL).toAlgHom = h.toAlgHom.comp T.LocalCovFieldAlgebra.val
```

**`GaugeFieldData.Realization.restrict_toAlgHom_apply`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L340).

```lean
lemma restrict_toAlgHom_apply (x : ↥T.LocalCovFieldAlgebra) :
    (h.restrict hGL).toAlgHom x = h.toAlgHom x
```

**`GaugeFieldData.Realization.restrict_id_toAlgHom`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L343).

```lean
lemma restrict_id_toAlgHom :
    ((id T).restrict hGL).toAlgHom = T.LocalCovFieldAlgebra.val
```

**`GaugeFieldData.Realization.restrict_fieldStrength`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L347).

```lean
lemma restrict_fieldStrength (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    (h.restrict hGL).fieldStrength l μ ν φ = h.toAlgHom (T.covDerivFieldStrength l μ ν φ)
```

**`GaugeFieldData.Realization.restrict_fermion`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L352).

```lean
lemma restrict_fermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    (h.restrict hGL).fermion i l φ = h.toAlgHom (T.covDerivFermion i l φ)
```

**`GaugeFieldData.Realization.restrict_conjFermion`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L356).

```lean
lemma restrict_conjFermion (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    (h.restrict hGL).conjFermion i l φ = h.toAlgHom (T.covDerivConjFermion i l φ)
```

**`GaugeFieldData.Realization.restrict_boson`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L360).

```lean
lemma restrict_boson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    (h.restrict hGL).boson j l φ = h.toAlgHom (T.covDerivBoson j l φ)
```

**`GaugeFieldData.Realization.restrict_conjBoson`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L364).

```lean
lemma restrict_conjBoson (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    (h.restrict hGL).conjBoson j l φ = h.toAlgHom (T.covDerivConjBoson j l φ)
```

**`GaugeFieldData.Realization.restrict_fieldStrength_eq_iteratedCovDerivAdjoint`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L370).

> The field-strength tower of a restriction is the covariant tower of the realized
> gauge-boson symbols.

```lean
lemma restrict_fieldStrength_eq_iteratedCovDerivAdjoint (l : List (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    (h.restrict hGL).fieldStrength l μ ν φ
      = GaugeAlgebraRealization.iteratedCovDerivAdjoint h.gaugeRealization.A l
        (GaugeAlgebraRealization.fieldStrength h.gaugeRealization.A μ ν) 0 φ
```

**`GaugeFieldData.Realization.restrict_fermion_eq_covDerivIter`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L379).

> A matter tower of a restriction is the covariant tower of the realized symbols of the
> species, computed against the realized gauge-boson symbols.

```lean
lemma restrict_fermion_eq_covDerivIter (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    (h.restrict hGL).fermion i l φ
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A (T.fermion i).repAlgebra
        (h.fermionSymbol i) n l 0 φ
```

**`GaugeFieldData.Realization.restrict_conjFermion_eq_covDerivIter`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L386).

```lean
lemma restrict_conjFermion_eq_covDerivIter (i : T.FermionSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    (h.restrict hGL).conjFermion i l φ
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A
        (LocalGaugeData.actionConj (T.fermion i).repAlgebra) (h.conjFermionSymbol i) n l 0 φ
```

**`GaugeFieldData.Realization.restrict_boson_eq_covDerivIter`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L393).

```lean
lemma restrict_boson_eq_covDerivIter (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)) :
    (h.restrict hGL).boson j l φ
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A (T.boson j).repAlgebra
        (h.bosonSymbol j) n l 0 φ
```

**`GaugeFieldData.Realization.restrict_conjBoson_eq_covDerivIter`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L400).

```lean
lemma restrict_conjBoson_eq_covDerivIter (j : T.BosonSpecies) {n : ℕ}
    (l : Fin n → (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    (h.restrict hGL).conjBoson j l φ
      = GaugeAlgebraRealization.covDerivIter h.gaugeRealization.A
        (LocalGaugeData.actionConj (T.boson j).repAlgebra) (h.conjBosonSymbol j) n l 0 φ
```

**`GaugeFieldData.Realization.restrict_map_repJet`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L408).

> Full jet equivariance survives restriction, with no species condition.

```lean
lemma restrict_map_repJet (U : GJ) (x : ↥T.LocalCovFieldAlgebra) :
    (h.restrict hGL).toAlgHom (LocalCovFieldAlgebra.repJet T U x)
      = repJet U ((h.restrict hGL).toAlgHom x)
```

## D. Factorization through evaluation

**`GaugeFieldData.Realization.repJet_restrict_toAlgHom`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L422).

> Under `GaugeFieldData.PureJetsActTrivially`, a jet acts on the realized covariant image
> as the constant jet of its value; nothing is assumed about the jet action elsewhere in
> `B`.

```lean
lemma repJet_restrict_toAlgHom (hP : T.PureJetsActTrivially) (U : GJ)
    (x : ↥T.LocalCovFieldAlgebra) :
    repJet U ((h.restrict hGL).toAlgHom x)
      = repJet (jets.ofConstant (jets.eval U)) ((h.restrict hGL).toAlgHom x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.Realization.map_repJet`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean#L441).

> Under `GaugeFieldData.PureJetsActTrivially`, a covariant realization intertwines the
> source jet action with the target action of the ordinary gauge group at the value of the
> jet.

```lean
lemma map_repJet (k : Realization T hGL B repGauge repLorentz) (hP : T.PureJetsActTrivially)
    (U : GJ) (x : ↥T.LocalCovFieldAlgebra) :
    k.toAlgHom (repJet T U x) = repGauge (jets.eval U) (k.toAlgHom x)
```

## Depends on

- [The covariant field algebra of a gauge theory](localcovfield-basic.md)
- [Realizations of the local field algebra](../part-03/localfield-realization.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalCovField/Realization.lean)
