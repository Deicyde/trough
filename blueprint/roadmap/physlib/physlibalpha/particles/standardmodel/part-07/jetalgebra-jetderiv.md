---
declaration: module
origin: cited
lean: StandardModel.JetAlgebra.jetDerivFermionFactor, StandardModel.JetAlgebra.jetDerivBosonFactor, StandardModel.JetAlgebra.jetDeriv, StandardModel.JetAlgebra.jetDeriv_tmul, StandardModel.JetAlgebra.jetDeriv_includeFermionFactor, StandardModel.JetAlgebra.jetDeriv_includeBosonFactor, StandardModel.JetAlgebra.jetDeriv_includeConnection, StandardModel.JetAlgebra.jetDeriv_includeFermion
statement: formalized
proof: formalized
---

# The total derivative on the jet algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.JetDeriv`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean): 17 declarations, 16 with a docstring; 10 private, not shown.

## i. Overview

> The formal total derivative on the jet algebra of the Standard Model is the sum of the
> total derivatives of its three factors, each acting on its own tensor factor. On the two
> matter factors it is the free-algebra derivation extending the derivative shift
> `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α` of the generator space of the field datum — an even derivation
> of the exterior algebra on the fermionic side, an ordinary derivation of the symmetric
> algebra on the bosonic side — and on the connection factor it is the generic gauge-boson
> derivative. It obeys the Leibniz rule, its components commute, and through each sector
> inclusion it restricts to that sector's own derivative, for a single direction and for an
> iterated multiset of directions alike.
>
> The Leibniz rule and the commutation are assembled from the factor facts through abstract
> lemmas proved at small types and instantiated, which keeps the proofs outside the full
> tensor product.

## ii. Key results

> - `JetAlgebra.jetDeriv` : the formal total derivative.
> - `JetAlgebra.jetDeriv_mul` : the Leibniz rule.
> - `JetAlgebra.jetDeriv_comm` : the total derivatives commute.
> - `JetAlgebra.jetDeriv_includeGauge`, `jetDeriv_includeFermion`, `jetDeriv_includeHiggs` :
>   the restrictions to the three sectors.
> - `JetAlgebra.iteratedD_includeFermion`, `iteratedD_includeHiggs`,
>   `iteratedD_includeGauge` : the same for the
>   iterated derivative.

## iv. References

> * None.

## A. The formal total derivative

**`StandardModel.JetAlgebra.jetDerivFermionFactor`**, an abbrev, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L77).

> The total derivative on the fermionic factor: the even derivation of the exterior
> algebra extending the derivative shift on the fermionic generator space of the datum.

```lean
noncomputable abbrev jetDerivFermionFactor (μ : Fin 1 ⊕ Fin 3) :
    ExteriorAlgebra ℂ fieldData.FermionGenerators →ₗ[ℂ]
      ExteriorAlgebra ℂ fieldData.FermionGenerators
```

**`StandardModel.JetAlgebra.jetDerivBosonFactor`**, an abbrev, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L84).

> The total derivative on the bosonic factor: the derivation of the symmetric algebra
> extending the derivative shift on the bosonic generator space of the datum.

```lean
noncomputable abbrev jetDerivBosonFactor (μ : Fin 1 ⊕ Fin 3) :
    SymmetricAlgebra ℂ fieldData.BosonGenerators →ₗ[ℂ]
      SymmetricAlgebra ℂ fieldData.BosonGenerators
```

**`StandardModel.JetAlgebra.jetDeriv`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L91).

> **The formal total derivative on the jet algebra of the Standard Model**: the sum of
> the total derivatives of the three factors, each acting on its own factor.

```lean
noncomputable def jetDeriv (μ : Fin 1 ⊕ Fin 3) : JetAlgebra →ₗ[ℂ] JetAlgebra
```

### A.1. The action on pure tensors

**`StandardModel.JetAlgebra.jetDeriv_tmul`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L105).

```lean
lemma jetDeriv_tmul (μ : Fin 1 ⊕ Fin 3) (f : ExteriorAlgebra ℂ fieldData.FermionGenerators)
    (h : SymmetricAlgebra ℂ fieldData.BosonGenerators)
    (g : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra GaugeAlgebra) :
    jetDeriv μ ((f ⊗ₜ[ℂ] h) ⊗ₜ[ℂ] g)
      = ((jetDerivFermionFactor μ f) ⊗ₜ[ℂ] h) ⊗ₜ[ℂ] g
        + (f ⊗ₜ[ℂ] (jetDerivBosonFactor μ h)) ⊗ₜ[ℂ] g
        + (f ⊗ₜ[ℂ] h) ⊗ₜ[ℂ] (_root_.LocalGaugeFieldAlgebra.complexJetDeriv GaugeAlgebra μ g)
```

### A.2. The action on the three factors

> Each factor inclusion sends a factor element to a pure tensor whose other two factors are
> `1`, and the total derivative annihilates `1` in every factor; so only that factor's own
> derivative survives.

**`StandardModel.JetAlgebra.jetDeriv_includeFermionFactor`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L227).

> The derivative acts on the fermionic factor through that factor's own derivation. The
> factor inclusions are unfolded through the generic `GaugeFieldData` rules rather than by
> `rfl`: at the Standard Model datum the definitional unfolding of the units has to see
> through the unexposed ring congruence of the symmetric algebra.

```lean
lemma jetDeriv_includeFermionFactor (μ : Fin 1 ⊕ Fin 3)
    (f : ExteriorAlgebra ℂ fieldData.FermionGenerators) :
    jetDeriv μ (fieldData.includeFermion f)
      = fieldData.includeFermion (jetDerivFermionFactor μ f)
```

**`StandardModel.JetAlgebra.jetDeriv_includeBosonFactor`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L237).

> The derivative acts on the bosonic factor through that factor's own derivation.

```lean
lemma jetDeriv_includeBosonFactor (μ : Fin 1 ⊕ Fin 3)
    (h : SymmetricAlgebra ℂ fieldData.BosonGenerators) :
    jetDeriv μ (fieldData.includeBoson h)
      = fieldData.includeBoson (jetDerivBosonFactor μ h)
```

**`StandardModel.JetAlgebra.jetDeriv_includeConnection`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L248).

> The derivative acts on the connection factor through the generic gauge-boson
> derivative.

```lean
lemma jetDeriv_includeConnection (μ : Fin 1 ⊕ Fin 3)
    (y : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra GaugeAlgebra) :
    jetDeriv μ (fieldData.includeConnection y)
      = fieldData.includeConnection
          (_root_.LocalGaugeFieldAlgebra.complexJetDeriv GaugeAlgebra μ y)
```

### A.3. The action on the three sectors

> The three sector inclusions factor through the sector equivalences,
>   which are maps of differential algebras; so the derivative restricts to each
> sector's own derivative under its existing name.

**`StandardModel.JetAlgebra.jetDeriv_includeFermion`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L279).

> The derivative acts on the fermionic sector through the fermionic sector's own
> derivative.

```lean
lemma jetDeriv_includeFermion (μ : Fin 1 ⊕ Fin 3) (f : FermionJetAlgebra) :
    jetDeriv μ (includeFermion f) = includeFermion (FermionicAlgebra.jetDeriv μ f)
```

**`StandardModel.JetAlgebra.jetDeriv_includeHiggs`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L287).

> The derivative acts on the Higgs sector through the Higgs sector's own derivative.

```lean
lemma jetDeriv_includeHiggs (μ : Fin 1 ⊕ Fin 3) (h : HiggsJetAlgebra) :
    jetDeriv μ (includeHiggs h) = includeHiggs (BosonicAlgebra.jetDeriv μ h)
```

**`StandardModel.JetAlgebra.jetDeriv_includeGauge`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L297).

> The derivative acts on the gauge sector through the gauge sector's own derivative. The
> gauge sector inclusion is the connection inclusion of the datum, the Standard Model gauge
> bosons being the generic ones at `GaugeAlgebra`.

```lean
lemma jetDeriv_includeGauge (μ : Fin 1 ⊕ Fin 3)
    (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    jetDeriv μ (includeGauge y)
      = includeGauge (_root_.LocalGaugeFieldAlgebra.complexJetDeriv GaugeAlgebra μ y)
```

## B. Derivations on tensor products

**`TensorProduct.map_derivation_left`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L310).

> A derivation of the left factor extends to a derivation of the tensor product.

```lean
lemma _root_.TensorProduct.map_derivation_left {A B : Type*} [Ring A] [Algebra ℂ A]
    [Ring B] [Algebra ℂ B] (D : A →ₗ[ℂ] A)
    (hD : ∀ x y, D (x * y) = D x * y + x * D y) (x y : A ⊗[ℂ] B) :
    TensorProduct.map D LinearMap.id (x * y)
      = TensorProduct.map D LinearMap.id x * y
        + x * TensorProduct.map D LinearMap.id y
```

**`TensorProduct.map_derivation_right`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L332).

> A derivation of the right factor extends to a derivation of the tensor product.

```lean
lemma _root_.TensorProduct.map_derivation_right {A B : Type*} [Ring A] [Algebra ℂ A]
    [Ring B] [Algebra ℂ B] (D : B →ₗ[ℂ] B)
    (hD : ∀ x y, D (x * y) = D x * y + x * D y) (x y : A ⊗[ℂ] B) :
    TensorProduct.map LinearMap.id D (x * y)
      = TensorProduct.map LinearMap.id D x * y
        + x * TensorProduct.map LinearMap.id D y
```

## C. The Leibniz rule

**`StandardModel.JetAlgebra.jetDeriv_mul`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L372).

> **The Leibniz rule** for the total derivative on the jet algebra.

```lean
lemma jetDeriv_mul (μ : Fin 1 ⊕ Fin 3) (x y : JetAlgebra) :
    jetDeriv μ (x * y) = jetDeriv μ x * y + x * jetDeriv μ y
```

## D. Commutativity

**`StandardModel.JetAlgebra.jetDeriv_comm`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L413).

> The total derivatives on the jet algebra commute.

```lean
lemma jetDeriv_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (jetDeriv μ).comp (jetDeriv ν) = (jetDeriv ν).comp (jetDeriv μ)
```

## E. The iterated derivative

> Iterating the sector restrictions of section A.3 along a multiset of directions: the
> iterated total derivative restricts to the sector's own iterated derivative. These are the
> forms the generator families of each sector consume.

**`StandardModel.JetAlgebra.iteratedD_includeFermion`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L489).

> The iterated total derivative acts on the fermionic sector through the fermionic
> sector's own iterated derivative.

```lean
lemma iteratedD_includeFermion (s : Multiset (Fin 1 ⊕ Fin 3)) (f : FermionJetAlgebra) :
    Lorentz.iteratedD jetDeriv jetDeriv_comm s (includeFermion f)
      = includeFermion (FermionicAlgebra.iteratedJetDeriv s f)
```

**`StandardModel.JetAlgebra.iteratedD_includeHiggs`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L499).

> The iterated total derivative acts on the Higgs sector through the Higgs sector's own
> iterated derivative.

```lean
lemma iteratedD_includeHiggs (s : Multiset (Fin 1 ⊕ Fin 3)) (h : HiggsJetAlgebra) :
    Lorentz.iteratedD jetDeriv jetDeriv_comm s (includeHiggs h)
      = includeHiggs (BosonicAlgebra.iteratedJetDeriv s h)
```

**`StandardModel.JetAlgebra.iteratedD_includeGauge`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean#L510).

> The iterated total derivative acts on the gauge sector through the gauge sector's own
> iterated derivative. Like its two siblings this instantiates the abstract
> `iteratedD_map` rather than running the induction inside the jet algebra.

```lean
lemma iteratedD_includeGauge (s : Multiset (Fin 1 ⊕ Fin 3))
    (y : ℂ ⊗[ℝ] (LocalGaugeFieldAlgebra GaugeAlgebra)) :
    Lorentz.iteratedD jetDeriv jetDeriv_comm s (includeGauge y)
      = includeGauge (Lorentz.iteratedD
          (_root_.LocalGaugeFieldAlgebra.complexJetDeriv GaugeAlgebra)
          _root_.LocalGaugeFieldAlgebra.complexJetDeriv_comm s y)
```

## Depends on

- [The jet algebra of the Standard Model](jetalgebra-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/JetDeriv.lean)
