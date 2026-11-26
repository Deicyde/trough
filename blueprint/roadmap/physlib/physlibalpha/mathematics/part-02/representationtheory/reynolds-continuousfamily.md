---
declaration: module
origin: cited
lean: Representation.ContinuousCoeff, Representation.ContinuousCoeff.comp, Representation.ContinuousCoeff.dualMap, Representation.ContinuousCoeff.continuous_coord, Representation.ContinuousCoeff.endConj, Representation.IsContinuousFamily, Representation.isContinuousFamily_one, Representation.IsContinuousFamily.sumElim
statement: formalized
proof: formalized
---

# Continuous families of a representation

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Reynolds.ContinuousFamily`, [PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean): 21 declarations, 20 with a docstring.

> Finite families of vectors on which a representation acts with continuous coefficients, and the
> finite-dimensional subrepresentations they span.

## i. Overview

> A Reynolds element of a compact group or of `SL(2,ℂ)` exists on a finite-dimensional
> subrepresentation on which the group acts continuously. This file gives a way to produce such
> subrepresentations by generation.
>
> An operator family `σ : H → Module.End 𝕜 D` has continuous coefficients when every matrix
> coefficient `h ↦ ψ (σ h x)` is continuous. A finite family of vectors `v` is a continuous family
> for a representation `ρ` when each `ρ h` maps every `v i` to a combination of the family with
> coefficients depending continuously on `h`. Its span is then a finite-dimensional
> subrepresentation with continuous matrix coefficients. For two commuting representations the span
> of a family continuous for both is a subrepresentation of the product group.
>
> Continuous families are closed under the operations of an algebra. The scalars form one, the
> union of two is one, and when the group acts by algebra maps so are the pairwise products of two.

## ii. Key results

> - `Representation.ContinuousCoeff` : continuity of an operator family through its matrix
>   coefficients.
> - `Representation.IsContinuousFamily` : a finite family on which a representation acts with
>   continuous coefficients.
> - `Representation.HasContinuousSpan` : lying in the span of a continuous family for two
>   representations.
> - `Representation.exists_subrepresentation_of_isContinuousFamily` : the span of a continuous
>   family for two commuting representations is a finite-dimensional subrepresentation of the
>   product with continuous matrix coefficients.

## iv. References

> * None.

## A. Operator families with continuous coefficients

**`Representation.ContinuousCoeff`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L75).

> A family `σ` of operators on `D` has continuous coefficients if every matrix coefficient
> `h ↦ ψ (σ h x)`, with `ψ` a linear functional on `D`, is continuous. For a finite-dimensional
> `D` this is continuity of `σ` for the unique vector space topology on its operators.

```lean
def ContinuousCoeff (σ : H → Module.End 𝕜 D) : Prop
```

**`Representation.ContinuousCoeff.comp`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L79).

> Continuous coefficients stay continuous after precomposing with a continuous map.

```lean
lemma ContinuousCoeff.comp {σ : H → Module.End 𝕜 D} (hσ : ContinuousCoeff σ) {f : H' → H}
    (hf : Continuous f) : ContinuousCoeff fun h => σ (f h)
```

**`Representation.ContinuousCoeff.dualMap`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L85).

> The transposes of an operator family with continuous coefficients on a finite-dimensional
> space have continuous coefficients.

```lean
lemma ContinuousCoeff.dualMap [FiniteDimensional 𝕜 D] {σ : H → Module.End 𝕜 D}
    (hσ : ContinuousCoeff σ) : ContinuousCoeff fun h => (σ h).dualMap
```

**`Representation.ContinuousCoeff.continuous_coord`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L92).

> The coefficients of an operator family in a basis are continuous.

```lean
lemma ContinuousCoeff.continuous_coord {ι : Type*} {σ : H → Module.End 𝕜 D}
    (hσ : ContinuousCoeff σ) (b : Module.Basis ι 𝕜 D) (i j : ι) :
    Continuous fun h => b.coord j (σ h (b i))
```

**`Representation.ContinuousCoeff.endConj`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L101).

> The conjugates of an operator family with continuous coefficients have continuous
> coefficients.

```lean
lemma ContinuousCoeff.endConj {H D : Type*} [TopologicalSpace H] [AddCommGroup D] [Module ℂ D]
    {σ : H → Module.End ℂ D} (hσ : ContinuousCoeff σ) :
    ContinuousCoeff fun h => ConjModule.endConj (σ h)
```

## B. Families with continuous coefficients

**`Representation.IsContinuousFamily`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L122).

> The representation acts on the finite family `v` by continuous coefficients,
> `ρ h (v i) = Σ j, a i j h • v j`.

```lean
def IsContinuousFamily (ρ : Representation ℂ H V) {ι : Type*} [Fintype ι] (v : ι → V) : Prop
```

**`Representation.isContinuousFamily_one`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L126).

> The family consisting of the unit, for a representation fixing the unit.

```lean
lemma isContinuousFamily_one (h1 : ∀ h, ρ h 1 = 1) :
    IsContinuousFamily ρ fun _ : Unit => (1 : A)
```

**`Representation.IsContinuousFamily.sumElim`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L131).

> The union of two families with continuous coefficients has continuous coefficients.

```lean
lemma IsContinuousFamily.sumElim {ι ι' : Type*} [Fintype ι] [Fintype ι'] {v : ι → V}
    {u : ι' → V} (hv : IsContinuousFamily ρV v) (hu : IsContinuousFamily ρV u) :
    IsContinuousFamily ρV (Sum.elim v u)
```

**`Representation.IsContinuousFamily.mul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L143).

> For a representation acting by algebra maps, the products of two families with continuous
> coefficients have continuous coefficients.

```lean
lemma IsContinuousFamily.mul (hmul : ∀ h x y, ρ h (x * y) = ρ h x * ρ h y) {ι ι' : Type*}
    [Fintype ι] [Fintype ι'] {v : ι → A} {u : ι' → A} (hv : IsContinuousFamily ρ v)
    (hu : IsContinuousFamily ρ u) : IsContinuousFamily ρ fun p : ι × ι' => v p.1 * u p.2
```

**`Representation.isContinuousFamily_tower`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L156).

> A tower `t p x`, linear in `x` up to the scalar map `ι𝕜`, on which the representation acts
> by continuous coefficients on the label `p` and by an operator family with continuous
> coefficients on `x`, gives a family with continuous coefficients over a basis of `x`.

```lean
lemma isContinuousFamily_tower {𝕜 D P : Type*} [Field 𝕜] [TopologicalSpace 𝕜] [AddCommGroup D]
    [Module 𝕜 D] [FiniteDimensional 𝕜 D] [Fintype P] (ι𝕜 : 𝕜 → ℂ) (hι𝕜 : Continuous ι𝕜)
    (t : P → D → V)
    (ht : ∀ p x, t p x = ∑ j, ι𝕜 (Module.finBasis 𝕜 D |>.repr x j) •
      t p (Module.finBasis 𝕜 D j))
    (σ : H → Module.End 𝕜 D) (hσ : ContinuousCoeff σ) (c : P → P → H → ℂ)
    (hc : ∀ p p', Continuous (c p p'))
    (hρ : ∀ h p x, ρV h (t p x) = ∑ p', c p p' h • t p' (σ h x)) :
    IsContinuousFamily ρV fun q : P × Fin (Module.finrank 𝕜 D) =>
      t q.1 (Module.finBasis 𝕜 D q.2)
```

## C. Elements spanned by continuous families

**`Representation.HasContinuousSpan`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L189).

> The element `a` lies in the span of a finite family on which both representations act by
> continuous coefficients.

```lean
def HasContinuousSpan (ρ₁ : Representation ℂ H₁ A) (ρ₂ : Representation ℂ H₂ A) (a : A) : Prop
```

**`Representation.HasContinuousSpan.of_mem_span`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L195).

> An element of the span of a family continuous for both representations has a
> continuous span.

```lean
lemma HasContinuousSpan.of_mem_span {ι : Type} [Fintype ι] {v : ι → A}
    (h₁ : IsContinuousFamily ρ₁ v) (h₂ : IsContinuousFamily ρ₂ v) {a : A}
    (ha : a ∈ Submodule.span ℂ (Set.range v)) : HasContinuousSpan ρ₁ ρ₂ a
```

**`Representation.hasContinuousSpan_smul_one`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L201).

> The scalars have a continuous span, for representations fixing the unit.

```lean
lemma hasContinuousSpan_smul_one (h₁ : ∀ h, ρ₁ h 1 = 1) (h₂ : ∀ h, ρ₂ h 1 = 1) (z : ℂ) :
    HasContinuousSpan ρ₁ ρ₂ (z • 1)
```

**`Representation.HasContinuousSpan.add`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L207).

> Having a continuous span is closed under addition.

```lean
lemma HasContinuousSpan.add {a b : A} (ha : HasContinuousSpan ρ₁ ρ₂ a)
    (hb : HasContinuousSpan ρ₁ ρ₂ b) : HasContinuousSpan ρ₁ ρ₂ (a + b)
```

**`Representation.HasContinuousSpan.mul`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L219).

> Having a continuous span is closed under multiplication when both representations
> are multiplicative.

```lean
lemma HasContinuousSpan.mul (hmul₁ : ∀ h x y, ρ₁ h (x * y) = ρ₁ h x * ρ₁ h y)
    (hmul₂ : ∀ h x y, ρ₂ h (x * y) = ρ₂ h x * ρ₂ h y) {a b : A}
    (ha : HasContinuousSpan ρ₁ ρ₂ a) (hb : HasContinuousSpan ρ₁ ρ₂ b) :
    HasContinuousSpan ρ₁ ρ₂ (a * b)
```

## D. Finite-dimensional subrepresentations

**`Subrepresentation.comp`**, an abbrev, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L243).

> A subrepresentation restricted along a monoid homomorphism, as a subrepresentation of the
> restricted representation with the same underlying subspace. It is reducible, so that
> instances on the underlying subspace, such as finite-dimensionality, carry over.

```lean
abbrev _root_.Subrepresentation.comp {k H H' V : Type*} [Semiring k] [Monoid H] [Monoid H']
    [AddCommMonoid V] [Module k V] {ρ : Representation k H V} (W : Subrepresentation ρ)
    (f : H' →* H) : Subrepresentation (ρ.comp f)
```

**`Subrepresentation.toSubmodule_comp`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L250).

```lean
lemma _root_.Subrepresentation.toSubmodule_comp {k H H' V : Type*} [Semiring k] [Monoid H]
    [Monoid H'] [AddCommMonoid V] [Module k V] {ρ : Representation k H V}
    (W : Subrepresentation ρ) (f : H' →* H) : (W.comp f).toSubmodule = W.toSubmodule
```

**`Representation.IsContinuousFamily.apply_mem_span`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L260).

> The span of a family with continuous coefficients is stable.

```lean
lemma IsContinuousFamily.apply_mem_span {ρ : Representation ℂ H V} {ι : Type*} [Fintype ι]
    {v : ι → V} (hv : IsContinuousFamily ρ v) (h : H) {x : V}
    (hx : x ∈ Submodule.span ℂ (Set.range v)) : ρ h x ∈ Submodule.span ℂ (Set.range v)
```

**`Representation.spanSubrepresentation`**, a def, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L271).

> The subrepresentation of the product spanned by a family with continuous coefficients
> for both factors.

```lean
def spanSubrepresentation {ρ₁ : Representation ℂ H₁ V} {ρ₂ : Representation ℂ H₂ V}
    (hc : ∀ a b, Commute (ρ₁ a) (ρ₂ b)) {ι : Type*} [Fintype ι] {v : ι → V}
    (h₁ : IsContinuousFamily ρ₁ v) (h₂ : IsContinuousFamily ρ₂ v) :
    Subrepresentation (prodOfCommute ρ₁ ρ₂ hc)
```

**`Representation.continuousMatrixCoeff_of_isContinuousFamily`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L282).

> A finite family with continuous coefficients gives a subrepresentation with continuous
> matrix coefficients.

```lean
lemma continuousMatrixCoeff_of_isContinuousFamily {ρ : Representation ℂ H V}
    (W : Subrepresentation ρ) {ι : Type*} [Fintype ι] {v : ι → V}
    (hW : W.toSubmodule = Submodule.span ℂ (Set.range v)) (hv : IsContinuousFamily ρ v) :
    ContinuousMatrixCoeff W
```

**`Representation.exists_subrepresentation_of_isContinuousFamily`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean#L293).

> A vector in the span of a finite family with continuous coefficients for two commuting
> representations lies in a finite-dimensional subrepresentation of the product, on which both
> factors act with continuous matrix coefficients.

```lean
lemma exists_subrepresentation_of_isContinuousFamily {ρ₁ : Representation ℂ H₁ V}
    {ρ₂ : Representation ℂ H₂ V} (hc : ∀ a b, Commute (ρ₁ a) (ρ₂ b)) {ι : Type*} [Fintype ι]
    {v : ι → V} (h₁ : IsContinuousFamily ρ₁ v) (h₂ : IsContinuousFamily ρ₂ v) {a : V}
    (ha_v : a ∈ Submodule.span ℂ (Set.range v)) :
    ∃ W : Subrepresentation (prodOfCommute ρ₁ ρ₂ hc), a ∈ W.toSubmodule ∧
      FiniteDimensional ℂ W.toSubmodule ∧
      ContinuousMatrixCoeff (W.comp (MonoidHom.inl H₁ H₂)) ∧
      ContinuousMatrixCoeff (W.comp (MonoidHom.inr H₁ H₂))
```

## Depends on

- [Algebras, duals and representations on a conjugate module](../modules/conjmodule.md)
- [Reynolds elements for compact groups](reynolds-compact.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Reynolds/ContinuousFamily.lean)
