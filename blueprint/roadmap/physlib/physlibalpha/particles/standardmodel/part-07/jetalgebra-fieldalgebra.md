---
declaration: module
origin: cited
lean: StandardModel.JetAlgebra.generators, StandardModel.JetAlgebra.gaugeField_mem_generators, StandardModel.JetAlgebra.higgsField_mem_generators, StandardModel.JetAlgebra.conjHiggsField_mem_generators, StandardModel.JetAlgebra.downSingletField_mem_generators, StandardModel.JetAlgebra.conjDownSingletField_mem_generators, StandardModel.JetAlgebra.upSingletField_mem_generators, StandardModel.JetAlgebra.conjUpSingletField_mem_generators
statement: formalized
proof: formalized
---

# The field algebra of the Standard Model is everything

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.FieldAlgebra`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean): 33 declarations, 33 with a docstring; 3 private, not shown.

## i. Overview

> The thirteen generator families of `JetAlgebra.Generators` — the gauge field, the Higgs and
> its conjugate, and the five fermion species in three generations each with a conjugate —
> generate the whole jet algebra of the Standard Model. Physically: every element of the
> algebra in which a Standard Model Lagrangian lives is a polynomial in the fields and their
> derivatives, because there is nothing else to write down.
>
> The set adjoined is `JetAlgebra.generators`, written to match the body of
> `AlgebraRealization.fieldAlgebra` verbatim, so that once the `AlgebraRealization` instance on the
> jet algebra exists the two are identified by `rfl`.
>
> The proof factors along the two tensor products. `Algebra.TensorProduct.adjoin_tmul_eq_top`
> reduces the whole algebra to its pure tensors, and a pure tensor is the product of the
> three sector inclusions applied to its factors; so it is enough that each sector inclusion
> lands in the adjoined algebra. Each of those is the sector's own generation theorem —
> `FermionicAlgebra.adjoin_iteratedJetDeriv_eq_top`, its bosonic counterpart, and
> `LocalGaugeFieldAlgebra.adjoin_iteratedJetDeriv_eq_top` — pushed through the inclusion.
>
> Two things do not come for free. The fermion families are indexed by covectors on the
> *individual species*, while the fermionic generation theorem produces every covector on the
> total target space `FermionSpace`; the gap is closed by
> `FermionSpace.span_speciesDual_eq_top`, which says the pulled-back covectors span. And the
> gauge sector's generation theorem is a statement over `ℝ` about
> `LocalGaugeFieldAlgebra GaugeAlgebra`, whereas the gauge tensor factor is the complexification
> `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra GaugeAlgebra`; the extra complex
> scalar is supplied by the algebra map, since `z ⊗ₜ x = (z ⊗ₜ 1) * (1 ⊗ₜ x)` and the first
> factor is the image of `z` under `algebraMap`.

## ii. Key results

> - `JetAlgebra.generators` : the derivative symbols of every field of the Standard Model.
> - `JetAlgebra.adjoin_generators_eq_top` : they generate the whole jet algebra.

## iv. References

> * None.

## A. The generating set

**`StandardModel.JetAlgebra.generators`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L88).

> The derivative symbols of every field of the Standard Model: the gauge field, the Higgs
> and its conjugate, and the three generations of each of the five fermion species with
> their conjugates. The set is written in exactly the shape of the body of
> `AlgebraRealization.fieldAlgebra`, so that the field algebra of the eventual
> `AlgebraRealization` instance on the jet algebra is this set adjoined.

```lean
noncomputable def generators : Set JetAlgebra
```

### A.1. Membership of the generating set

**`StandardModel.JetAlgebra.gaugeField_mem_generators`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L106).

> The gauge-field symbols are generators.

```lean
lemma gaugeField_mem_generators (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) : gaugeField s μ φ ∈ generators
```

**`StandardModel.JetAlgebra.higgsField_mem_generators`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L111).

> The Higgs symbols are generators.

```lean
lemma higgsField_mem_generators (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ HiggsVec) : higgsField s φ ∈ generators
```

**`StandardModel.JetAlgebra.conjHiggsField_mem_generators`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L116).

> The conjugate Higgs symbols are generators.

```lean
lemma conjHiggsField_mem_generators (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) : conjHiggsField s φ ∈ generators
```

**`StandardModel.JetAlgebra.downSingletField_mem_generators`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L122).

> The symbols of the `i`-th generation down-type quark singlet are
> generators.

```lean
lemma downSingletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet) : downSingletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.conjDownSingletField_mem_generators`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L129).

> The conjugate symbols of the `i`-th generation down-type quark singlet are
> generators.

```lean
lemma conjDownSingletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) : conjDownSingletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.upSingletField_mem_generators`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L136).

> The symbols of the `i`-th generation up-type quark singlet are
> generators.

```lean
lemma upSingletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ UpSinglet) : upSingletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.conjUpSingletField_mem_generators`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L143).

> The conjugate symbols of the `i`-th generation up-type quark singlet are
> generators.

```lean
lemma conjUpSingletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) : conjUpSingletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.quarkDoubletField_mem_generators`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L150).

> The symbols of the `i`-th generation quark doublet are
> generators.

```lean
lemma quarkDoubletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ QuarkDoublet) : quarkDoubletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.conjQuarkDoubletField_mem_generators`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L157).

> The conjugate symbols of the `i`-th generation quark doublet are
> generators.

```lean
lemma conjQuarkDoubletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) : conjQuarkDoubletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.leptonDoubletField_mem_generators`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L164).

> The symbols of the `i`-th generation lepton doublet are
> generators.

```lean
lemma leptonDoubletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonDoubletV) : leptonDoubletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.conjLeptonDoubletField_mem_generators`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L171).

> The conjugate symbols of the `i`-th generation lepton doublet are
> generators.

```lean
lemma conjLeptonDoubletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) : conjLeptonDoubletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.leptonSingletField_mem_generators`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L178).

> The symbols of the `i`-th generation charged-lepton singlet are
> generators.

```lean
lemma leptonSingletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonSinglet) : leptonSingletField i s φ ∈ generators
```

**`StandardModel.JetAlgebra.conjLeptonSingletField_mem_generators`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L185).

> The conjugate symbols of the `i`-th generation charged-lepton singlet are
> generators.

```lean
lemma conjLeptonSingletField_mem_generators (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) : conjLeptonSingletField i s φ ∈ generators
```

## B. The three sectors lie in the generated algebra

### B.1. Adjoining through an algebra map

### B.2. The Higgs sector

**`StandardModel.JetAlgebra.higgsField_eq_includeHiggs`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L229).

> A Higgs symbol is the Higgs sector's own derivative symbol, included.

```lean
lemma higgsField_eq_includeHiggs (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ HiggsVec) :
    higgsField s φ
      = includeHiggs (BosonicAlgebra.iteratedJetDeriv s (BosonicAlgebra.ofField φ))
```

**`StandardModel.JetAlgebra.conjHiggsField_eq_includeHiggs`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L239).

> A conjugate Higgs symbol is the Higgs sector's own conjugate derivative symbol,
> included.

```lean
lemma conjHiggsField_eq_includeHiggs (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    conjHiggsField s φ
      = includeHiggs (BosonicAlgebra.iteratedJetDeriv s
          (BosonicAlgebra.ofConjField φ))
```

**`StandardModel.JetAlgebra.includeHiggs_mem_adjoin_generators`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L251).

> Every element of the Higgs sector lies in the algebra generated by the symbols: the
> Higgs jet algebra is generated by the Higgs field, its conjugate and their derivatives,
> and those are exactly the two Higgs families.

```lean
lemma includeHiggs_mem_adjoin_generators (h : HiggsJetAlgebra) :
    includeHiggs h ∈ Algebra.adjoin ℂ generators
```

### B.3. The fermionic sector

> The fermionic generation theorem produces the symbols of every covector on the total target
> space `FermionSpace`, while the ten families supply only the covectors pulled back from a
> single species and generation. Those span, by `FermionSpace.span_speciesDual_eq_top`, and
> the symbol map is linear, so the families reach every symbol.

**`StandardModel.JetAlgebra.fermionSymbol_eq_includeFermion`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L276).

> A fermionic symbol is the fermionic sector's own derivative symbol, included.

```lean
lemma fermionSymbol_eq_includeFermion (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ FermionSpace) :
    fermionSymbol s φ
      = includeFermion (FermionicAlgebra.iteratedJetDeriv s
          (FermionicAlgebra.ofField φ))
```

**`StandardModel.JetAlgebra.conjFermionSymbol_eq_includeFermion`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L287).

> A conjugate fermionic symbol is the fermionic sector's own conjugate derivative symbol,
> included.

```lean
lemma conjFermionSymbol_eq_includeFermion (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule FermionSpace)) :
    conjFermionSymbol s φ
      = includeFermion (FermionicAlgebra.iteratedJetDeriv s
          (FermionicAlgebra.ofConjField φ))
```

**`StandardModel.JetAlgebra.fermionSymbol_mem_adjoin_generators`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L299).

> Every fermionic symbol lies in the generated algebra. The families give the symbols of
> the covectors pulled back from a single species and generation; those span every covector
> on the total fermionic target space, and the symbol map is linear.

```lean
lemma fermionSymbol_mem_adjoin_generators (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ FermionSpace) :
    fermionSymbol s φ ∈ Algebra.adjoin ℂ generators
```

**`StandardModel.JetAlgebra.conjFermionSymbol_mem_adjoin_generators`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L328).

> Every conjugate fermionic symbol lies in the generated algebra, by the conjugate form
> of the spanning argument.

```lean
lemma conjFermionSymbol_mem_adjoin_generators (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule FermionSpace)) :
    conjFermionSymbol s φ ∈ Algebra.adjoin ℂ generators
```

**`StandardModel.JetAlgebra.includeFermion_mem_adjoin_generators`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L360).

> Every element of the fermionic sector lies in the algebra generated by the symbols.

```lean
lemma includeFermion_mem_adjoin_generators (f : FermionJetAlgebra) :
    includeFermion f ∈ Algebra.adjoin ℂ generators
```

### B.4. The gauge sector

> The gauge tensor factor is the complexification `ℂ ⊗[ℝ] LocalGaugeFieldAlgebra GaugeAlgebra`,
> while the gauge sector's generation theorem is a statement over `ℝ` about
> `LocalGaugeFieldAlgebra GaugeAlgebra` itself. The real part of the factor is handled by that
> lemma transported along the real algebra map `x ↦ 1 ⊗ₜ x`; the complex scalar is then
> supplied by `z ⊗ₜ x = (z ⊗ₜ 1) * (1 ⊗ₜ x)`, whose first factor is the image of `z` under
> `algebraMap` and so lies in every subalgebra.

**`StandardModel.JetAlgebra.iteratedD_complexJetDeriv_tmul`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L388).

> The iterated derivative of the complexification acts on a pure tensor through the
> gauge sector's own iterated derivative.

```lean
lemma iteratedD_complexJetDeriv_tmul (s : Multiset (Fin 1 ⊕ Fin 3)) (z : ℂ)
    (x : (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    Lorentz.iteratedD (LocalGaugeFieldAlgebra.complexJetDeriv GaugeAlgebra)
        LocalGaugeFieldAlgebra.complexJetDeriv_comm s (z ⊗ₜ[ℝ] x)
      = z ⊗ₜ[ℝ] (LocalGaugeFieldAlgebra.iteratedJetDeriv GaugeAlgebra) s x
```

**`StandardModel.JetAlgebra.includeGaugeReal`**, a def, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L406).

> The real gauge-boson jet algebra inside the jet algebra of the Standard Model: the
> inclusion of the gauge sector precomposed with the inclusion of the real part of the
> complexification. It is a map of `ℝ`-algebras, which is the level at which the gauge
> sector's generation theorem is stated.

```lean
noncomputable def includeGaugeReal : (LocalGaugeFieldAlgebra GaugeAlgebra) →ₐ[ℝ] JetAlgebra
```

**`StandardModel.JetAlgebra.includeGaugeReal_apply`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L414).

> The real gauge inclusion is the gauge inclusion of the pure tensor with complex part
> one.

```lean
lemma includeGaugeReal_apply (x : (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    includeGaugeReal x = includeGauge ((1 : ℂ) ⊗ₜ[ℝ] x)
```

**`StandardModel.JetAlgebra.gaugeField_eq_includeGaugeReal`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L419).

> A gauge-field symbol is the gauge sector's own derivative symbol, included through the
> real part of the complexification.

```lean
lemma gaugeField_eq_includeGaugeReal (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    gaugeField s μ φ
      = includeGaugeReal ((LocalGaugeFieldAlgebra.iteratedJetDeriv GaugeAlgebra) s
          ((LocalGaugeFieldAlgebra.ofA GaugeAlgebra) μ φ))
```

**`StandardModel.JetAlgebra.includeGaugeReal_mem_adjoin_generators`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L432).

> Every element of the real gauge sector lies in the algebra generated by the symbols:
> the gauge-boson jet algebra is generated over `ℝ` by the derivative symbols of the gauge
> field, and those are the gauge family.

```lean
lemma includeGaugeReal_mem_adjoin_generators (x : (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    includeGaugeReal x ∈ Algebra.adjoin ℂ generators
```

**`StandardModel.JetAlgebra.includeGauge_mem_adjoin_generators`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L446).

> Every element of the complexified gauge sector lies in the algebra generated by the
> symbols: a pure tensor splits as a complex scalar times the image of its real part.

```lean
lemma includeGauge_mem_adjoin_generators (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    includeGauge y ∈ Algebra.adjoin ℂ generators
```

### B.5. The two matter factors of the carrier

> The two matter sector inclusions factor through the sector equivalences, so a factor of
> the carrier is a sector element read through one of them.

**`StandardModel.JetAlgebra.includeFermionFactor_mem_adjoin_generators`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L474).

> Every element of the fermionic factor of the carrier lies in the generated algebra.

```lean
lemma includeFermionFactor_mem_adjoin_generators
    (a : ExteriorAlgebra ℂ fieldData.FermionGenerators) :
    fieldData.includeFermion a ∈ Algebra.adjoin ℂ generators
```

**`StandardModel.JetAlgebra.includeBosonFactor_mem_adjoin_generators`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L483).

> Every element of the bosonic factor of the carrier lies in the generated algebra.

```lean
lemma includeBosonFactor_mem_adjoin_generators
    (b : SymmetricAlgebra ℂ fieldData.BosonGenerators) :
    fieldData.includeBoson b ∈ Algebra.adjoin ℂ generators
```

## C. The generation theorem

**`StandardModel.JetAlgebra.includeFermionFactor_mul_includeBosonFactor_mul_includeConnection`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L510).

> A pure tensor of the jet algebra is the product of the three factor inclusions applied
> to its factors. The three inclusions are unfolded through the abstract `GaugeFieldData`
> rules, which is what keeps the computation out of the carrier's own instances.

```lean
lemma includeFermionFactor_mul_includeBosonFactor_mul_includeConnection
    (a : ExteriorAlgebra ℂ fieldData.FermionGenerators)
    (b : SymmetricAlgebra ℂ fieldData.BosonGenerators)
    (c : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    fieldData.includeFermion a * fieldData.includeBoson b * fieldData.includeConnection c
      = ((a ⊗ₜ[ℂ] b) ⊗ₜ[ℂ] c : JetAlgebra)
```

**`StandardModel.JetAlgebra.tmul_mem_adjoin_generators`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L525).

> Every pure tensor of the jet algebra lies in the algebra generated by the symbols.

```lean
lemma tmul_mem_adjoin_generators (w : fieldData.MatterAlgebra)
    (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    (w ⊗ₜ[ℂ] y : JetAlgebra) ∈ Algebra.adjoin ℂ generators
```

**`StandardModel.JetAlgebra.adjoin_generators_eq_top`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean#L548).

> The fields of the Standard Model generate its jet algebra. As a `ℂ`-algebra,
> `JetAlgebra` is adjoined by the derivative symbols of the gauge field, the Higgs and its
> conjugate, and the three generations of each of the five fermion species with their
> conjugates.
>
> Physically: every element of the algebra in which a Standard Model Lagrangian lives is a
> polynomial in the fields and their spacetime derivatives — nothing else is available to
> write down. Formally it is the statement that the field algebra of the eventual
> `AlgebraRealization` instance on the jet algebra is the whole of it.

```lean
lemma adjoin_generators_eq_top :
    Algebra.adjoin ℂ generators = (⊤ : Subalgebra ℂ JetAlgebra)
```

## Depends on

- [The generators of the jet algebra of the Standard Model](jetalgebra-generators.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/FieldAlgebra.lean)
