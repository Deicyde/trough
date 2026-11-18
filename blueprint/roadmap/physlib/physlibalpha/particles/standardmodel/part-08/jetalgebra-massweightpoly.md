---
declaration: module
origin: cited
lean: StandardModel.JetAlgebra.commute_monomial, StandardModel.JetAlgebra.commute_mapAlgHom, StandardModel.JetAlgebra.commute_mapAlgHom_includeGauge, StandardModel.JetAlgebra.fermionMassWeightPoly, StandardModel.JetAlgebra.higgsMassWeightPoly, StandardModel.JetAlgebra.gaugeMassWeightPoly, StandardModel.JetAlgebra.fermionFactorMassWeightPoly, StandardModel.JetAlgebra.bosonFactorMassWeightPoly
statement: formalized
proof: formalized
---

# The mass-weight polynomial on the jet algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.MassWeightPoly`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean): 35 declarations, 33 with a docstring; 1 private, not shown.

## i. Overview

> Each of the three sectors of the jet algebra of the Standard Model carries its own
> mass-weight grading: `FermionicAlgebra.massWeightPoly 3` on the fermions, whose symbols have
> mass dimension `3/2`, `BosonicAlgebra.massWeightPoly 2` on the Higgs and
> `LocalGaugeFieldAlgebra.complexMassWeightPoly` on the gauge bosons, whose symbols have mass
> dimension one. This file assembles them into a single grading
>
> `massWeightPoly : JetAlgebra →ₐ[ℂ] Polynomial JetAlgebra`
>
> and computes it on every generating family.
>
> The assembly is two applications of the universal property of the tensor product of
> algebras. Each sector grading is first transported into `Polynomial JetAlgebra` along
> `Polynomial.mapAlgHom` of that sector's inclusion; the two matter gradings are then read on
> the two matter factors of the carrier through the sector equivalences of
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Basic`, lifted over the matter
> factor `GaugeFieldData.MatterAlgebra`, and that lift over the whole algebra. The connection
> factor needs no equivalence, being the gauge sector itself. Both lifts need a commutation
> side condition, and both reduce to the statistics already proved in
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.Generators`: two polynomials commute as soon as
> their coefficients do, the Higgs sector commutes with the fermionic sector, and the gauge
> sector is central.
>
> Because each sector's generator lemma has the shape `massWeightPoly g = monomial n g` — the
> generator *itself* as the coefficient — transporting it along `Polynomial.mapAlgHom` is a
> single rewrite by `Polynomial.mapAlgHom_monomial`. So every generating family of the full
> algebra is again a monomial eigenvector, of exactly the weight `AlgebraRealization` predicts:
> `2 * (1 + |s|)` for the bosons, `3 + 2 * |s|` for the fermions.

## ii. Key results

> - `JetAlgebra.massWeightPoly` : the mass-weight grading on the jet algebra of the Standard
>   Model.
> - `JetAlgebra.fermionFactorMassWeightPoly`, `bosonFactorMassWeightPoly` : the two matter
>   sector gradings read on the two matter factors of the carrier.
> - `JetAlgebra.massWeightPoly_includeFermion`, `massWeightPoly_includeHiggs`,
>   `massWeightPoly_includeGauge` : the grading restricted to each sector.
> - `JetAlgebra.massWeightPoly_higgsField`, `massWeightPoly_gaugeField`,
>   `massWeightPoly_leptonDoubletField`, … : the fifteen generator families are monomial
>   eigenvectors.

## iv. References

> * None.

## A. Commuting polynomials over the jet algebra

> The two lifts that assemble the grading each demand that the images of the two factors
> commute. Both images consist of polynomials, and in both cases the commutation is already
> known one coefficient at a time — so the work of this section is to promote a commutation
> of coefficients to a commutation of polynomials, which is an induction over monomials.

**`StandardModel.JetAlgebra.commute_monomial`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L100).

> Two monomials with commuting coefficients commute: the variable is central, so the two
> products are the same monomial.

```lean
lemma commute_monomial {C : Type*} [Semiring C] {a b : C} (h : Commute a b)
    (n m : ℕ) : Commute (Polynomial.monomial n a) (Polynomial.monomial m b)
```

**`StandardModel.JetAlgebra.commute_mapAlgHom`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L109).

> Polynomials pushed forward along two algebra maps with commuting images commute: every
> polynomial is a sum of monomials, and monomials with commuting coefficients commute.

```lean
lemma commute_mapAlgHom {A B C : Type*} [Semiring A] [Algebra ℂ A] [Semiring B]
    [Algebra ℂ B] [Semiring C] [Algebra ℂ C] (f : A →ₐ[ℂ] C) (g : B →ₐ[ℂ] C)
    (h : ∀ (a : A) (b : B), Commute (f a) (g b)) (p : Polynomial A) (q : Polynomial B) :
    Commute (Polynomial.mapAlgHom f p) (Polynomial.mapAlgHom g q)
```

**`StandardModel.JetAlgebra.commute_mapAlgHom_includeGauge`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L125).

> Every polynomial over the jet algebra commutes with a polynomial whose coefficients lie
> in the gauge sector: the gauge sector is central, so the commutation holds coefficient by
> coefficient.

```lean
lemma commute_mapAlgHom_includeGauge (p : Polynomial JetAlgebra)
    (q : Polynomial (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra))) :
    Commute p (Polynomial.mapAlgHom includeGauge q)
```

## B. The mass-weight polynomial on the jet algebra

> Each sector's grading is transported into `Polynomial JetAlgebra` along
> `Polynomial.mapAlgHom` of that sector's inclusion, and the three transported gradings are
> assembled by the universal property of the tensor product — first over the matter factor,
> then over the whole algebra.

**`StandardModel.JetAlgebra.fermionMassWeightPoly`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L151).

> The fermionic mass-weight grading, transported into the full jet algebra. The fermionic
> symbols have mass dimension `3/2`, hence mass weight three.

```lean
noncomputable def fermionMassWeightPoly :
    FermionJetAlgebra →ₐ[ℂ] Polynomial JetAlgebra
```

**`StandardModel.JetAlgebra.higgsMassWeightPoly`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L157).

> The Higgs mass-weight grading, transported into the full jet algebra. The Higgs symbols
> have mass dimension one, hence mass weight two.

```lean
noncomputable def higgsMassWeightPoly : HiggsJetAlgebra →ₐ[ℂ] Polynomial JetAlgebra
```

**`StandardModel.JetAlgebra.gaugeMassWeightPoly`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L162).

> The gauge-boson mass-weight grading, transported into the full jet algebra. The gauge
> symbols have mass dimension one, hence mass weight two.

```lean
noncomputable def gaugeMassWeightPoly :
    (ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) →ₐ[ℂ] Polynomial JetAlgebra
```

**`StandardModel.JetAlgebra.fermionFactorMassWeightPoly`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L169).

> The fermionic grading read on the fermionic factor of the carrier: the fermionic sector
> grading, precomposed with the sector equivalence. The sector helper above keeps its own
> domain, the fermionic sector algebra; this is the map the carrier's factor needs.

```lean
noncomputable def fermionFactorMassWeightPoly :
    ExteriorAlgebra ℂ fieldData.FermionGenerators →ₐ[ℂ] Polynomial JetAlgebra
```

**`StandardModel.JetAlgebra.bosonFactorMassWeightPoly`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L174).

> The Higgs grading read on the bosonic factor of the carrier.

```lean
noncomputable def bosonFactorMassWeightPoly :
    SymmetricAlgebra ℂ fieldData.BosonGenerators →ₐ[ℂ] Polynomial JetAlgebra
```

**`StandardModel.JetAlgebra.fermionFactorMassWeightPoly_apply`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L178).

```lean
lemma fermionFactorMassWeightPoly_apply (a : ExteriorAlgebra ℂ fieldData.FermionGenerators) :
    fermionFactorMassWeightPoly a
      = Polynomial.mapAlgHom includeFermion
        (FermionicAlgebra.massWeightPoly 3 (fermionAlgebraEquiv.symm a))
```

**`StandardModel.JetAlgebra.bosonFactorMassWeightPoly_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L183).

```lean
lemma bosonFactorMassWeightPoly_apply (b : SymmetricAlgebra ℂ fieldData.BosonGenerators) :
    bosonFactorMassWeightPoly b
      = Polynomial.mapAlgHom includeHiggs
        (BosonicAlgebra.massWeightPoly 2 (higgsAlgebraEquiv.symm b))
```

**`StandardModel.JetAlgebra.matterMassWeightPoly`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L192).

> The mass-weight grading on the matter factor of the jet algebra: the fermionic and
> Higgs gradings, lifted over the tensor product of the two matter factors of the carrier.
> The side condition is that the two images commute, which they do because the Higgs sector
> commutes with the fermionic sector.

```lean
noncomputable def matterMassWeightPoly :
    fieldData.MatterAlgebra →ₐ[ℂ] Polynomial JetAlgebra
```

**`StandardModel.JetAlgebra.massWeightPoly`**, a def, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L208).

> The mass-weight polynomial on the jet algebra of the Standard Model: the `ℂ`-algebra
> map sending a generator of mass weight `n` to `X ^ n` times itself, so that the
> coefficient of `X ^ n` in `massWeightPoly a` is the part of `a` of mass weight `n`. It is
> the three sector gradings lifted over the tensor product, the side condition for the
> outer lift being the centrality of the gauge sector.

```lean
noncomputable def massWeightPoly : JetAlgebra →ₐ[ℂ] Polynomial JetAlgebra
```

## C. The grading through the sector inclusions

> The lift is computed on pure tensors by construction, and each sector inclusion is a pure
> tensor with ones in the other factors. So on each sector the full grading is that sector's
> own grading, transported. These three lemmas are the whole content of the assembly: every
> generator computation below is one of them followed by a sector generator lemma.

**`StandardModel.JetAlgebra.massWeightPoly_tmul`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L226).

> On a pure tensor the grading is the product of the matter and gauge gradings.

```lean
lemma massWeightPoly_tmul (x : fieldData.MatterAlgebra)
    (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    massWeightPoly (x ⊗ₜ[ℂ] y) = matterMassWeightPoly x * gaugeMassWeightPoly y
```

**`StandardModel.JetAlgebra.matterMassWeightPoly_tmul`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L232).

> On a pure tensor the matter grading is the product of the fermionic and bosonic factor
> gradings.

```lean
lemma matterMassWeightPoly_tmul (a : ExteriorAlgebra ℂ fieldData.FermionGenerators)
    (b : SymmetricAlgebra ℂ fieldData.BosonGenerators) :
    matterMassWeightPoly (a ⊗ₜ[ℂ] b)
      = fermionFactorMassWeightPoly a * bosonFactorMassWeightPoly b
```

**`StandardModel.JetAlgebra.massWeightPoly_includeFermionFactor`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L240).

> On the fermionic factor the grading is that factor's own grading. Like every step
> below it is written as an equation chain, which never abstracts a pattern out of a goal
> mentioning the jet algebra.

```lean
lemma massWeightPoly_includeFermionFactor
    (a : ExteriorAlgebra ℂ fieldData.FermionGenerators) :
    massWeightPoly (fieldData.includeFermion a) = fermionFactorMassWeightPoly a
```

**`StandardModel.JetAlgebra.massWeightPoly_includeBosonFactor`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L254).

> On the bosonic factor the grading is that factor's own grading.

```lean
lemma massWeightPoly_includeBosonFactor
    (b : SymmetricAlgebra ℂ fieldData.BosonGenerators) :
    massWeightPoly (fieldData.includeBoson b) = bosonFactorMassWeightPoly b
```

**`StandardModel.JetAlgebra.massWeightPoly_includeConnection`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L268).

> On the connection factor the grading is the generic gauge-boson grading.

```lean
lemma massWeightPoly_includeConnection (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    massWeightPoly (fieldData.includeConnection y) = gaugeMassWeightPoly y
```

**`StandardModel.JetAlgebra.massWeightPoly_includeFermion`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L277).

> On the fermionic sector the grading is the fermionic sector's own grading, pushed
> forward along the fermionic inclusion.

```lean
lemma massWeightPoly_includeFermion (a : FermionJetAlgebra) :
    massWeightPoly (includeFermion a)
      = Polynomial.mapAlgHom includeFermion (FermionicAlgebra.massWeightPoly 3 a)
```

**`StandardModel.JetAlgebra.massWeightPoly_includeHiggs`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L287).

> On the Higgs sector the grading is the Higgs sector's own grading, pushed forward along
> the Higgs inclusion.

```lean
lemma massWeightPoly_includeHiggs (h : HiggsJetAlgebra) :
    massWeightPoly (includeHiggs h)
      = Polynomial.mapAlgHom includeHiggs (BosonicAlgebra.massWeightPoly 2 h)
```

**`StandardModel.JetAlgebra.massWeightPoly_includeGauge`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L298).

> On the gauge sector the grading is the gauge sector's own grading, pushed forward along
> the gauge inclusion. The gauge sector inclusion is the connection inclusion of the datum,
> so there is nothing to transport here.

```lean
lemma massWeightPoly_includeGauge (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    massWeightPoly (includeGauge y)
      = Polynomial.mapAlgHom includeGauge (LocalGaugeFieldAlgebra.complexMassWeightPoly y)
```

## D. The mass weight of the Higgs symbols

> The Higgs field has mass dimension one, so the symbol `∂_s H_φ` has mass dimension
> `1 + |s|` and mass weight twice that. The exponent is written in the form
> `2 * (1 + |s|)` that `AlgebraRealization` asks for.

**`StandardModel.JetAlgebra.massWeightPoly_higgsField`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L322).

> The Higgs symbol `∂_s H_φ` is a monomial eigenvector of mass weight `2 * (1 + |s|)`:
> the Higgs field has mass dimension one and each derivative adds one more.

```lean
lemma massWeightPoly_higgsField (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ HiggsVec) :
    massWeightPoly (higgsField s φ)
      = Polynomial.monomial (2 * (1 + Multiset.card s)) (higgsField s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_conjHiggsField`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L338).

> The conjugate Higgs symbol `∂_s H̄_φ` is a monomial eigenvector of the same mass weight
> `2 * (1 + |s|)` as the symbol it conjugates.

```lean
lemma massWeightPoly_conjHiggsField (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule HiggsVec)) :
    massWeightPoly (conjHiggsField s φ)
      = Polynomial.monomial (2 * (1 + Multiset.card s)) (conjHiggsField s φ)
```

## E. The mass weight of the gauge-field symbols

> The gauge field, like the Higgs, has mass dimension one. Its symbols reach the full jet
> algebra through the complexification of the real gauge-boson jet algebra, so the
> computation passes through the complexified grading of that sector.

**`StandardModel.JetAlgebra.massWeightPoly_gaugeField`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L365).

> The gauge-field symbol `∂_s A_μ^φ` is a monomial eigenvector of mass weight
> `2 * (1 + |s|)`: the gauge field has mass dimension one and each derivative adds one
> more.

```lean
lemma massWeightPoly_gaugeField (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    massWeightPoly (gaugeField s μ φ)
      = Polynomial.monomial (2 * (1 + Multiset.card s)) (gaugeField s μ φ)
```

## F. The mass weight of the fermion symbols

> Every fermion of the Standard Model has mass dimension `3/2`, so a fermionic symbol
> `∂_s ψ_φ` has mass dimension `3/2 + |s|` and mass weight `3 + 2 |s|` — the exponent form
> `AlgebraRealization` asks for. The computation is the same for all ten species families,
> because each of them reduces, by the lemmas of
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.Generators`, to a fermionic symbol on the total
> target space; so section F.2 is ten instantiations of section F.1 and nothing more.

### F.1. The symbols on the total fermionic target space

**`StandardModel.JetAlgebra.massWeightPoly_fermionSymbol`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L407).

> A fermionic symbol `∂_s ψ_φ` on the total fermionic target space is a monomial
> eigenvector of mass weight `3 + 2 |s|`: a fermion has mass dimension `3/2` and each
> derivative adds one more.

```lean
lemma massWeightPoly_fermionSymbol (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ FermionSpace) :
    massWeightPoly (fermionSymbol s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (fermionSymbol s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_conjFermionSymbol`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L422).

> A conjugate fermionic symbol `∂_s ψ̄_φ` on the total fermionic target space is a
> monomial eigenvector of the same mass weight `3 + 2 |s|` as the symbol it conjugates.

```lean
lemma massWeightPoly_conjFermionSymbol (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule FermionSpace)) :
    massWeightPoly (conjFermionSymbol s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (conjFermionSymbol s φ)
```

### F.2. The ten species families

**`StandardModel.JetAlgebra.massWeightPoly_leptonDoubletField`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L443).

> The symbol `∂_s ψ_φ` of the `i`-th generation lepton doublet is a monomial eigenvector
> of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_leptonDoubletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonDoubletV) :
    massWeightPoly (leptonDoubletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (leptonDoubletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_conjLeptonDoubletField`**, a lemma, [line 454](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L454).

> The conjugate symbol `∂_s ψ̄_φ` of the `i`-th generation lepton doublet is a monomial
> eigenvector of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_conjLeptonDoubletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule LeptonDoubletV)) :
    massWeightPoly (conjLeptonDoubletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (conjLeptonDoubletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_leptonSingletField`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L465).

> The symbol `∂_s ψ_φ` of the `i`-th generation charged-lepton singlet is a monomial eigenvector
> of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_leptonSingletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ LeptonSinglet) :
    massWeightPoly (leptonSingletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (leptonSingletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_conjLeptonSingletField`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L476).

> The conjugate symbol `∂_s ψ̄_φ` of the `i`-th generation charged-lepton singlet is a monomial
> eigenvector of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_conjLeptonSingletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule LeptonSinglet)) :
    massWeightPoly (conjLeptonSingletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (conjLeptonSingletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_quarkDoubletField`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L487).

> The symbol `∂_s ψ_φ` of the `i`-th generation quark doublet is a monomial eigenvector
> of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_quarkDoubletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ QuarkDoublet) :
    massWeightPoly (quarkDoubletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (quarkDoubletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_conjQuarkDoubletField`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L498).

> The conjugate symbol `∂_s ψ̄_φ` of the `i`-th generation quark doublet is a monomial
> eigenvector of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_conjQuarkDoubletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule QuarkDoublet)) :
    massWeightPoly (conjQuarkDoubletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (conjQuarkDoubletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_upSingletField`**, a lemma, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L509).

> The symbol `∂_s ψ_φ` of the `i`-th generation up-type quark singlet is a monomial eigenvector
> of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_upSingletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ UpSinglet) :
    massWeightPoly (upSingletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (upSingletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_conjUpSingletField`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L520).

> The conjugate symbol `∂_s ψ̄_φ` of the `i`-th generation up-type quark singlet is a monomial
> eigenvector of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_conjUpSingletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule UpSinglet)) :
    massWeightPoly (conjUpSingletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (conjUpSingletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_downSingletField`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L531).

> The symbol `∂_s ψ_φ` of the `i`-th generation down-type quark singlet is a monomial eigenvector
> of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_downSingletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ DownSinglet) :
    massWeightPoly (downSingletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (downSingletField i s φ)
```

**`StandardModel.JetAlgebra.massWeightPoly_conjDownSingletField`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean#L542).

> The conjugate symbol `∂_s ψ̄_φ` of the `i`-th generation down-type quark singlet is a monomial
> eigenvector of mass weight `3 + 2 |s|`.

```lean
lemma massWeightPoly_conjDownSingletField (i : Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule DownSinglet)) :
    massWeightPoly (conjDownSingletField i s φ)
      = Polynomial.monomial (3 + 2 * Multiset.card s) (conjDownSingletField i s φ)
```

## Depends on

- [The mass-weight polynomial on the gauge-boson jet algebra](../../../classicalfieldtheory/gaugetheory/part-01/gaugeboson-localgauge-massweightpoly.md)
- [The generators of the jet algebra of the Standard Model](../part-07/jetalgebra-generators.md)
- [The mass-weight polynomial on the bosonic algebra](matter-bosonic-massweightpoly.md)
- [The mass-weight polynomial on the fermionic algebra](../part-09/matter-fermionic-massweightpoly.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/MassWeightPoly.lean)
