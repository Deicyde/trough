---
declaration: module
origin: cited
lean: GaugeFieldData.totalDerivFermionFactor, GaugeFieldData.totalDerivBosonFactor, GaugeFieldData.totalDeriv, GaugeFieldData.totalDeriv_includeFermionFactor, GaugeFieldData.totalDeriv_includeBosonFactor, GaugeFieldData.totalDeriv_includeConnection, GaugeFieldData.totalDeriv_mul, GaugeFieldData.totalDerivFermionFactor_comm
statement: formalized
proof: formalized
---

# The total derivative on the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.TotalDeriv`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean): 23 declarations, 23 with a docstring; 32 private, not shown.

> The formal total derivative `∂_μ` on the local field algebra of a field datum, its Leibniz
> rule, its action on the symbols and its Lorentz covariance.

## i. Overview

> The formal total derivative on the local field algebra of a field datum `T` is the sum of
> the total derivatives of its three factors, each acting on its own tensor factor. On the two
> matter factors it is the free-algebra derivation extending the derivative shift
> `∂_s ψ_α ↦ ∂_{s + {μ}} ψ_α` of the generator space of the datum, an even derivation of the
> exterior algebra on the fermionic side and an ordinary derivation of the symmetric algebra on
> the bosonic side. On the connection factor it is the derivative of the complexified
> gauge-boson algebra. It obeys the Leibniz rule, its components commute, and on each factor
> it is that factor's own derivative.
>
> On a matter symbol the total derivative appends the direction `μ` to the derivative label,
> `∂_μ (∂_s ψ^φ) = ∂_{s + {μ}} ψ^φ`, so the symbol `∂_s ψ^φ` is the iterated total derivative
> along `s` of the undifferentiated symbol. On the connection factor the iterated total
> derivative is the iterated derivative of the gauge-boson algebra.
>
> The total derivative is a Lorentz vector. The Lorentz action of the datum intertwines `∂_μ`
> with `∑_a Λ_{a μ} ∂_a`. This is proved for the action written factor by factor, through the
> covariance of the derivation extending a linear endomorphism on each free-algebra factor,
> and transported to `T.repLorentzGroup`, which agrees with it.
>
> The Leibniz rule, the commutation and the covariance are assembled from the factor facts
> through abstract lemmas proved at small types and instantiated, which keeps the proofs
> outside the full tensor product. The name `totalDeriv` distinguishes the derivative from the
> `jetDeriv` on `V`-valued jets.

## ii. Key results

> - `GaugeFieldData.totalDeriv` : the formal total derivative.
> - `GaugeFieldData.totalDeriv_mul` : the Leibniz rule.
> - `GaugeFieldData.totalDeriv_comm` : the total derivatives commute.
> - `GaugeFieldData.totalDeriv_includeFermionFactor`, `totalDeriv_includeBosonFactor`,
>   `totalDeriv_includeConnection` : the restrictions to the three factors.
> - `GaugeFieldData.iteratedD_includeConnection` : the iterated derivative on the connection
>   factor.
> - `GaugeFieldData.totalDeriv_fermionSymbol`, `totalDeriv_bosonSymbol` and their conjugates :
>   the total derivative appends a direction to the derivative label.
> - `GaugeFieldData.iteratedD_fermionSymbol`, `iteratedD_bosonSymbol` and their conjugates :
>   the iterated total derivative appends a multiset of directions.
> - `GaugeFieldData.repLorentzGroup_totalDeriv` : the total derivative is a Lorentz vector.

## iv. References

> * None.

## A. The formal total derivative

**`GaugeFieldData.totalDerivFermionFactor`**, an abbrev, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L101).

> The total derivative on the fermionic factor, the even derivation of the exterior
> algebra extending the derivative shift on the fermionic generator space of the datum.

```lean
noncomputable abbrev totalDerivFermionFactor (μ : Fin 1 ⊕ Fin 3) :
    ExteriorAlgebra ℂ T.FermionGenerators →ₗ[ℂ]
      ExteriorAlgebra ℂ T.FermionGenerators
```

**`GaugeFieldData.totalDerivBosonFactor`**, an abbrev, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L108).

> The total derivative on the bosonic factor, the derivation of the symmetric algebra
> extending the derivative shift on the bosonic generator space of the datum.

```lean
noncomputable abbrev totalDerivBosonFactor (μ : Fin 1 ⊕ Fin 3) :
    SymmetricAlgebra ℂ T.BosonGenerators →ₗ[ℂ]
      SymmetricAlgebra ℂ T.BosonGenerators
```

**`GaugeFieldData.totalDeriv`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L115).

> The formal total derivative on the local field algebra, the sum of the total
> derivatives of the three factors, each acting on its own factor.

```lean
noncomputable def totalDeriv (μ : Fin 1 ⊕ Fin 3) :
    T.LocalFieldAlgebra →ₗ[ℂ] T.LocalFieldAlgebra
```

### A.1. The action on the three factors

> Each factor inclusion sends a factor element to a pure tensor whose other two factors are
> `1`, and the total derivative annihilates `1` in every factor; so only that factor's own
> derivative survives.

**`GaugeFieldData.totalDeriv_includeFermionFactor`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L240).

> The derivative acts on the fermionic factor through that factor's own derivation. The
> factor inclusions are unfolded through the generic `GaugeFieldData` rules rather than by
> `rfl`, since at a concrete datum the definitional unfolding of the units has to see
> through the unexposed ring congruence of the symmetric algebra.

```lean
lemma totalDeriv_includeFermionFactor (μ : Fin 1 ⊕ Fin 3)
    (f : ExteriorAlgebra ℂ T.FermionGenerators) :
    T.totalDeriv μ (T.includeFermion f)
      = T.includeFermion (T.totalDerivFermionFactor μ f)
```

**`GaugeFieldData.totalDeriv_includeBosonFactor`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L250).

> The derivative acts on the bosonic factor through that factor's own derivation.

```lean
lemma totalDeriv_includeBosonFactor (μ : Fin 1 ⊕ Fin 3)
    (h : SymmetricAlgebra ℂ T.BosonGenerators) :
    T.totalDeriv μ (T.includeBoson h)
      = T.includeBoson (T.totalDerivBosonFactor μ h)
```

**`GaugeFieldData.totalDeriv_includeConnection`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L261).

> The derivative acts on the connection factor through the generic gauge-boson
> derivative.

```lean
lemma totalDeriv_includeConnection (μ : Fin 1 ⊕ Fin 3)
    (y : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra G) :
    T.totalDeriv μ (T.includeConnection y)
      = T.includeConnection
          (_root_.LocalGaugeFieldAlgebra.complexJetDeriv G μ y)
```

## B. The Leibniz rule

**`GaugeFieldData.totalDeriv_mul`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L299).

> The Leibniz rule for the total derivative on the local field algebra.

```lean
lemma totalDeriv_mul (μ : Fin 1 ⊕ Fin 3) (x y : T.LocalFieldAlgebra) :
    T.totalDeriv μ (x * y) = T.totalDeriv μ x * y + x * T.totalDeriv μ y
```

## C. Commutativity

**`GaugeFieldData.totalDerivFermionFactor_comm`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L359).

> The total derivatives on the fermionic factor commute.

```lean
lemma totalDerivFermionFactor_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (T.totalDerivFermionFactor μ).comp (T.totalDerivFermionFactor ν)
      = (T.totalDerivFermionFactor ν).comp (T.totalDerivFermionFactor μ)
```

**`GaugeFieldData.totalDerivBosonFactor_comm`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L367).

> The total derivatives on the bosonic factor commute.

```lean
lemma totalDerivBosonFactor_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (T.totalDerivBosonFactor μ).comp (T.totalDerivBosonFactor ν)
      = (T.totalDerivBosonFactor ν).comp (T.totalDerivBosonFactor μ)
```

**`GaugeFieldData.totalDeriv_comm`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L375).

> The total derivatives on the local field algebra commute.

```lean
lemma totalDeriv_comm (μ ν : Fin 1 ⊕ Fin 3) :
    (T.totalDeriv μ).comp (T.totalDeriv ν) = (T.totalDeriv ν).comp (T.totalDeriv μ)
```

## D. The iterated derivative on the connection factor

> Iterating the restriction of section A.2 to the connection factor along a multiset of
> directions: there the iterated total derivative is the iterated derivative of the
> complexified gauge-boson algebra.

**`GaugeFieldData.iteratedD_includeConnection`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L422).

> The iterated total derivative acts on the connection factor through the gauge sector's
> own iterated derivative. It instantiates the abstract `iteratedD_map` rather than running
> the induction inside the local field algebra.

```lean
lemma iteratedD_includeConnection (s : Multiset (Fin 1 ⊕ Fin 3))
    (y : ℂ ⊗[ℝ] _root_.LocalGaugeFieldAlgebra G) :
    Lorentz.iteratedD T.totalDeriv T.totalDeriv_comm s (T.includeConnection y)
      = T.includeConnection (Lorentz.iteratedD
          (_root_.LocalGaugeFieldAlgebra.complexJetDeriv G)
          _root_.LocalGaugeFieldAlgebra.complexJetDeriv_comm s y)
```

## E. The derivative shift on a component space

## F. The total derivative of the matter generators

> A matter generator lies in its free-algebra factor, where the total derivative is the
> derivation extending the derivative shift of the generator space. On a degree-one element
> that derivation is the shift itself, which acts species by species.

**`GaugeFieldData.totalDeriv_ιFermion`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L480).

> The total derivative of a fermionic generator is the generator of the shifted
> component.

```lean
lemma totalDeriv_ιFermion (μ : Fin 1 ⊕ Fin 3) (i : T.FermionSpecies)
    (x : FieldDerivSpace (T.fermion i)) :
    T.totalDeriv μ (T.ιFermion i x)
      = T.ιFermion i (FieldDerivSpace.jetDeriv μ x)
```

**`GaugeFieldData.totalDeriv_ιBoson`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L493).

> The total derivative of a bosonic generator is the generator of the shifted
> component.

```lean
lemma totalDeriv_ιBoson (μ : Fin 1 ⊕ Fin 3) (j : T.BosonSpecies)
    (y : FieldDerivSpace (T.boson j)) :
    T.totalDeriv μ (T.ιBoson j y)
      = T.ιBoson j (FieldDerivSpace.jetDeriv μ y)
```

## G. The total derivative of the matter symbols

**`GaugeFieldData.totalDeriv_fermionSymbol`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L513).

> The total derivative appends the direction `μ` to the derivative label of a fermionic
> symbol, `∂_μ (∂_s ψ^φ) = ∂_{s + {μ}} ψ^φ`.

```lean
lemma totalDeriv_fermionSymbol (μ : Fin 1 ⊕ Fin 3) (i : T.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.FermionValue i)) :
    T.totalDeriv μ (T.fermionSymbol i s φ) = T.fermionSymbol i (μ ::ₘ s) φ
```

**`GaugeFieldData.totalDeriv_conjFermionSymbol`**, a lemma, [line 522](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L522).

> The total derivative appends the direction `μ` to the derivative label of a conjugate
> fermionic symbol.

```lean
lemma totalDeriv_conjFermionSymbol (μ : Fin 1 ⊕ Fin 3) (i : T.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    T.totalDeriv μ (T.conjFermionSymbol i s φ)
      = T.conjFermionSymbol i (μ ::ₘ s) φ
```

**`GaugeFieldData.totalDeriv_bosonSymbol`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L532).

> The total derivative appends the direction `μ` to the derivative label of a bosonic
> symbol, `∂_μ (∂_s φ) = ∂_{s + {μ}} φ`.

```lean
lemma totalDeriv_bosonSymbol (μ : Fin 1 ⊕ Fin 3) (j : T.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (T.BosonValue j)) :
    T.totalDeriv μ (T.bosonSymbol j s φ) = T.bosonSymbol j (μ ::ₘ s) φ
```

**`GaugeFieldData.totalDeriv_conjBosonSymbol`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L541).

> The total derivative appends the direction `μ` to the derivative label of a conjugate
> bosonic symbol.

```lean
lemma totalDeriv_conjBosonSymbol (μ : Fin 1 ⊕ Fin 3) (j : T.BosonSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    T.totalDeriv μ (T.conjBosonSymbol j s φ)
      = T.conjBosonSymbol j (μ ::ₘ s) φ
```

## H. The iterated total derivative of the matter symbols

**`GaugeFieldData.iteratedD_fermionSymbol`**, a lemma, [line 569](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L569).

> The iterated total derivative along `s` appends `s` to the derivative label of a
> fermionic symbol. For `r = 0` it says that `∂_s ψ^φ` is the iterated total derivative of
> the undifferentiated symbol `ψ^φ`.

```lean
lemma iteratedD_fermionSymbol (i : T.FermionSpecies) (s r : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.FermionValue i)) :
    Lorentz.iteratedD T.totalDeriv T.totalDeriv_comm s (T.fermionSymbol i r φ)
      = T.fermionSymbol i (s + r) φ
```

**`GaugeFieldData.iteratedD_conjFermionSymbol`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L578).

> The iterated total derivative along `s` appends `s` to the derivative label of a
> conjugate fermionic symbol.

```lean
lemma iteratedD_conjFermionSymbol (i : T.FermionSpecies)
    (s r : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))) :
    Lorentz.iteratedD T.totalDeriv T.totalDeriv_comm s (T.conjFermionSymbol i r φ)
      = T.conjFermionSymbol i (s + r) φ
```

**`GaugeFieldData.iteratedD_bosonSymbol`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L587).

> The iterated total derivative along `s` appends `s` to the derivative label of a bosonic
> symbol.

```lean
lemma iteratedD_bosonSymbol (j : T.BosonSpecies) (s r : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (T.BosonValue j)) :
    Lorentz.iteratedD T.totalDeriv T.totalDeriv_comm s (T.bosonSymbol j r φ)
      = T.bosonSymbol j (s + r) φ
```

**`GaugeFieldData.iteratedD_conjBosonSymbol`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L596).

> The iterated total derivative along `s` appends `s` to the derivative label of a
> conjugate bosonic symbol.

```lean
lemma iteratedD_conjBosonSymbol (j : T.BosonSpecies) (s r : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))) :
    Lorentz.iteratedD T.totalDeriv T.totalDeriv_comm s (T.conjBosonSymbol j r φ)
      = T.conjBosonSymbol j (s + r) φ
```

## I. Lorentz covariance

### I.1. The factorwise action

### I.2. Multiplicativity

### I.3. The action on the three factors

### I.4. The total derivative is a Lorentz vector for the factorwise action

### I.5. Agreement with the generic action

**`GaugeFieldData.repLorentzGroup_totalDeriv`**, a lemma, [line 875](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L875).

> The total derivative is a Lorentz vector. The Lorentz action intertwines the total
> derivative through the columns of the Lorentz matrix.

```lean
lemma repLorentzGroup_totalDeriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3)
    (x : T.LocalFieldAlgebra) :
    T.repLorentzGroup Λ (T.totalDeriv μ x) =
      ∑ a, (((Lorentz.SL2C.toLorentzGroup Λ).1 a μ : ℝ) : ℂ) •
        T.totalDeriv a (T.repLorentzGroup Λ x)
```

**`GaugeFieldData.instIsLorentzDerivTotalDeriv`**, an instance, [line 885](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean#L885).

> The total derivatives on the local field algebra form a Lorentz derivative for the
> Lorentz action of the field datum.

```lean
instance instIsLorentzDerivTotalDeriv : Lorentz.IsLorentzDeriv T.repLorentzGroup T.totalDeriv
```

## Depends on

- [The field symbols of the local field algebra and their transformation laws](../part-04/localfieldalgebra-symbols.md)
- [Derivations and representations on the exterior algebra](../../../mathematics/part-01/exterioralgebra.md)

## Proof depends on

- [Representations acting by algebra maps](../../../mathematics/part-01/algebrarepresentation.md)
- [Derivations of one factor of a tensor product of algebras](../../../mathematics/part-02/formathlib/ringtheory-tensorproduct-derivation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/TotalDeriv.lean)
