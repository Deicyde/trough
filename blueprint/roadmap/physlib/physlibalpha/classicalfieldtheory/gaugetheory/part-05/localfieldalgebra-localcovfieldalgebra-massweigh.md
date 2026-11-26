---
declaration: module
origin: cited
lean: GaugeFieldData.LocalCovFieldAlgebra.IsMassWeightPoly, GaugeFieldData.LocalCovFieldAlgebra.isMassWeightPoly_of, GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule, GaugeFieldData.LocalCovFieldAlgebra.mem_massWeightSubmodule_iff, GaugeFieldData.LocalCovFieldAlgebra.mul_mem_massWeightSubmodule, GaugeFieldData.LocalCovFieldAlgebra.one_mem_massWeightSubmodule_zero, GaugeFieldData.LocalCovFieldAlgebra.mem_massWeightSubmodule_of_mem_weightedGenerators, GaugeFieldData.LocalCovFieldAlgebra.mem_massWeightSubmodule_of_mem_weightedMonomials
statement: formalized
proof: formalized
---

# The mass-weight grading of the covariant field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.LocalCovFieldAlgebra.MassWeight`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean): 39 declarations, 35 with a docstring.

> The grading of the covariant field algebra by mass weight, its components and its filtration.

## i. Overview

> The mass weight of a covariant expression is twice its mass dimension. It is recorded by an
> algebra map `P` from the covariant field algebra to the polynomials over it, the element `b`
> of weight `w` going to `b X ^ w`. The statement `IsMassWeightPoly P` says that `P` gives every
> covariant generator its mass weight: `4 + 2 |l|` for the field-strength tower `∇_l F_μν`, and
> `c + 2 n` for the tower of `n` covariant derivatives of a species of mass weight `c`.
>
> The weight-`n` piece `massWeightSubmodule P n` is the set of elements `x` with `P x = x X ^ n`.
> Products add weights. Under `IsMassWeightPoly P` the weight-`n` piece is spanned by the products
> of generators of total weight `n`. The weight-`k` component `massWeightComponent P k x` of an
> element is the coefficient of `X ^ k` in `P x`. It lies in the weight-`k` piece, and every element
> is the sum of its components.
>
> The gauge and Lorentz groups carry each generator into a combination of generators of the same
> weight, so they preserve every weight piece and commute with taking components. The components
> of an invariant element are therefore invariant. The filtration `massWeightSubmoduleLE P w` is the
> join of the pieces of weight at most `w`, and an element of it is the sum of its components of
> weight at most `w`.
>
> When every species has positive mass weight, the weight-zero piece is the constants. When the
> fermionic species have odd mass weight and the bosonic species even mass weight, elements of
> weights `v` and `w` exchange up to the sign `(-1) ^ (v * w)`.

## ii. Key results

> - `GaugeFieldData.LocalCovFieldAlgebra.IsMassWeightPoly` : `P` gives every generator its mass
>   weight, with the constructor `isMassWeightPoly_of` from the towers.
> - `GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule`,
>   `GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmoduleLE` : the weight pieces and the
>   filtration.
> - `GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent` : the projection onto a weight.
> - `GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule_eq_span` : the weight-`n` piece is
>   spanned by the products of generators of weight `n`.
> - `GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_mem_invariants_repValue` and its
>   Lorentz companion : the components of an invariant are invariant.
> - `GaugeFieldData.LocalCovFieldAlgebra.sum_massWeightComponent_of_mem_massWeightSubmoduleLE` :
>   an element of the filtration is the sum of its low-weight components.
> - `GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule_zero` : the weight-zero piece is the
>   constants.
> - `GaugeFieldData.LocalCovFieldAlgebra.mul_eq_smul_mul_of_mem_massWeightSubmodule` : elements of
>   given weights supercommute.

## iv. References

> * None.

## A. Mass-weight polynomials

**`GaugeFieldData.LocalCovFieldAlgebra.IsMassWeightPoly`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L97).

> An algebra map `P` from the covariant field algebra to the polynomials over it is a
> mass-weight polynomial when every covariant generator of mass weight `w` is homogeneous of
> weight `w`, `P b = b X ^ w`.

```lean
def IsMassWeightPoly : Prop
```

**`GaugeFieldData.LocalCovFieldAlgebra.isMassWeightPoly_of`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L103).

> `P` is a mass-weight polynomial when the field-strength tower `∇_l F_μν` has weight
> `4 + 2 |l|` and the towers of `n` covariant derivatives of a species of mass weight `c`, and of
> its conjugate, have weight `c + 2 n`.

```lean
lemma isMassWeightPoly_of
    (hF : ∀ (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra),
      P (covFieldStrength T l μ ν φ)
        = Polynomial.monomial (4 + 2 * l.length) (covFieldStrength T l μ ν φ))
    (hψ : ∀ (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (T.FermionValue i)),
      P (covFermion T i l φ)
        = Polynomial.monomial ((T.fermion i).massWeight + 2 * n) (covFermion T i l φ))
    (hψc : ∀ (i : T.FermionSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (ConjModule (T.FermionValue i))),
      P (covConjFermion T i l φ)
        = Polynomial.monomial ((T.fermion i).massWeight + 2 * n) (covConjFermion T i l φ))
    (hφ : ∀ (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (T.BosonValue j)),
      P (covBoson T j l φ)
        = Polynomial.monomial ((T.boson j).massWeight + 2 * n) (covBoson T j l φ))
    (hφc : ∀ (j : T.BosonSpecies) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3))
      (φ : Module.Dual ℂ (ConjModule (T.BosonValue j))),
      P (covConjBoson T j l φ)
        = Polynomial.monomial ((T.boson j).massWeight + 2 * n) (covConjBoson T j l φ)) :
    IsMassWeightPoly P
```

## B. The weight pieces

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L149).

> The weight-`n` piece of the covariant field algebra, the elements `x` with
> `P x = x X ^ n`.

```lean
noncomputable def massWeightSubmodule (n : ℕ) : Submodule ℂ T.LocalCovFieldAlgebra
```

**`GaugeFieldData.LocalCovFieldAlgebra.mem_massWeightSubmodule_iff`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L156).

```lean
lemma mem_massWeightSubmodule_iff {n : ℕ} {x : T.LocalCovFieldAlgebra} :
    x ∈ massWeightSubmodule P n ↔ P x = Polynomial.monomial n x
```

**`GaugeFieldData.LocalCovFieldAlgebra.mul_mem_massWeightSubmodule`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L162).

> The weight pieces are multiplicative, since weights add under multiplication.

```lean
lemma mul_mem_massWeightSubmodule {v w : ℕ} {x y : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule P v) (hy : y ∈ massWeightSubmodule P w) :
    x * y ∈ massWeightSubmodule P (v + w)
```

**`GaugeFieldData.LocalCovFieldAlgebra.one_mem_massWeightSubmodule_zero`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L170).

> The unit has weight zero.

```lean
lemma one_mem_massWeightSubmodule_zero :
    (1 : T.LocalCovFieldAlgebra) ∈ massWeightSubmodule P 0
```

### B.1. Products of generators are homogeneous

**`GaugeFieldData.LocalCovFieldAlgebra.mem_massWeightSubmodule_of_mem_weightedGenerators`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L181).

> Under `IsMassWeightPoly P`, a generator of mass weight `w` lies in the weight-`w` piece.

```lean
lemma mem_massWeightSubmodule_of_mem_weightedGenerators (hP : IsMassWeightPoly P) {k : FieldKind}
    {w : ℕ} {b : T.LocalCovFieldAlgebra} (hb : b ∈ T.weightedGenerators k w) :
    b ∈ massWeightSubmodule P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.mem_massWeightSubmodule_of_mem_weightedMonomials`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L188).

> Under `IsMassWeightPoly P`, a product of generators of total mass weight `w` lies in the
> weight-`w` piece.

```lean
lemma mem_massWeightSubmodule_of_mem_weightedMonomials (hP : IsMassWeightPoly P)
    {A : Finset FieldKind} {w : ℕ} {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ T.weightedMonomials A w) : x ∈ massWeightSubmodule P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.span_weightedMonomials_le_massWeightSubmodule`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L202).

> Under `IsMassWeightPoly P`, the combinations of products of generators of weight `w` lie in
> the weight-`w` piece.

```lean
lemma span_weightedMonomials_le_massWeightSubmodule (hP : IsMassWeightPoly P) (w : ℕ) :
    Submodule.span ℂ (⋃ A, T.weightedMonomials A w) ≤ massWeightSubmodule P w
```

## C. The weight components

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent`**, a def, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L216).

> The weight-`k` component of an element of the covariant field algebra, the coefficient of
> `X ^ k` in its image under `P`.

```lean
noncomputable def massWeightComponent (k : ℕ) :
    T.LocalCovFieldAlgebra →ₗ[ℂ] T.LocalCovFieldAlgebra
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_apply`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L231).

```lean
lemma massWeightComponent_apply (k : ℕ) (x : T.LocalCovFieldAlgebra) :
    massWeightComponent P k x = (P x).coeff k
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_of_mem`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L236).

> The weight-`k` component of an element of the weight-`w` piece is the element itself when
> `w = k`, and zero otherwise.

```lean
lemma massWeightComponent_of_mem {w : ℕ} {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule P w) (k : ℕ) :
    massWeightComponent P k x = if w = k then x else 0
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_self`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L241).

```lean
lemma massWeightComponent_self {w : ℕ} {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule P w) : massWeightComponent P w x = x
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_mem_span`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L248).

> Under `IsMassWeightPoly P`, the weight-`k` component of any element is a combination of
> products of generators of weight `k`. On a product of generators the component is the product
> or zero, and both sides are linear.

```lean
lemma massWeightComponent_mem_span (hP : IsMassWeightPoly P) (k : ℕ)
    (x : T.LocalCovFieldAlgebra) :
    massWeightComponent P k x ∈ Submodule.span ℂ (⋃ A, T.weightedMonomials A k)
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_mem_massWeightSubmodule`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L266).

> Under `IsMassWeightPoly P`, the weight-`k` component lies in the weight-`k` piece.

```lean
lemma massWeightComponent_mem_massWeightSubmodule (hP : IsMassWeightPoly P) (k : ℕ)
    (x : T.LocalCovFieldAlgebra) : massWeightComponent P k x ∈ massWeightSubmodule P k
```

**`GaugeFieldData.LocalCovFieldAlgebra.eq_sum_coeff`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L273).

> Under `IsMassWeightPoly P`, every element of the covariant field algebra is the sum of its
> weight components, the coefficients of its image under `P`. It holds on the products of
> generators, which are homogeneous, and both sides are linear.

```lean
lemma eq_sum_coeff (hP : IsMassWeightPoly P) (x : T.LocalCovFieldAlgebra) :
    x = (P x).sum fun _ a => a
```

### C.1. The weight pieces as spans of products

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule_eq_span`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L300).

> Under `IsMassWeightPoly P`, the weight-`w` piece is exactly the span of the products of
> generators of total weight `w`.

```lean
lemma massWeightSubmodule_eq_span (hP : IsMassWeightPoly P) (w : ℕ) :
    massWeightSubmodule P w = Submodule.span ℂ (⋃ A, T.weightedMonomials A w)
```

**`GaugeFieldData.LocalCovFieldAlgebra.map_massWeightComponent`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L308).

> Under `IsMassWeightPoly P`, a linear map preserving every weight piece commutes with taking
> weight components.

```lean
lemma map_massWeightComponent (hP : IsMassWeightPoly P)
    {f : T.LocalCovFieldAlgebra →ₗ[ℂ] T.LocalCovFieldAlgebra}
    (hf : ∀ w y, y ∈ massWeightSubmodule P w → f y ∈ massWeightSubmodule P w) (k : ℕ)
    (x : T.LocalCovFieldAlgebra) :
    f (massWeightComponent P k x) = massWeightComponent P k (f x)
```

## D. Stability under the gauge and Lorentz groups

**`GaugeFieldData.LocalCovFieldAlgebra.map_mem_massWeightSubmodule`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L335).

> A map preserving the span of the products of every given kinds and weight preserves every
> weight piece.

```lean
lemma map_mem_massWeightSubmodule (hP : IsMassWeightPoly P)
    {f : T.LocalCovFieldAlgebra →ₗ[ℂ] T.LocalCovFieldAlgebra}
    (hf : ∀ (A : Finset FieldKind) (w : ℕ) (x : T.LocalCovFieldAlgebra),
      x ∈ Submodule.span ℂ (T.weightedMonomials A w) →
        f x ∈ Submodule.span ℂ (T.weightedMonomials A w))
    {w : ℕ} {x : T.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule P w) :
    f x ∈ massWeightSubmodule P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.repJet_mem_massWeightSubmodule`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L350).

> The jet gauge group preserves every weight piece.

```lean
lemma repJet_mem_massWeightSubmodule (hP : IsMassWeightPoly P) (U : G.gaugeJetGroup) {w : ℕ}
    {x : T.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule P w) :
    repJet T U x ∈ massWeightSubmodule P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.repValue_mem_massWeightSubmodule`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L356).

> The ordinary gauge group preserves every weight piece.

```lean
lemma repValue_mem_massWeightSubmodule (hP : IsMassWeightPoly P) (g : G.group) {w : ℕ}
    {x : T.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmodule P w) :
    repValue T g x ∈ massWeightSubmodule P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.repLorentzGroup_mem_massWeightSubmodule`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L362).

> The Lorentz group preserves every weight piece.

```lean
lemma repLorentzGroup_mem_massWeightSubmodule (hP : IsMassWeightPoly P)
    (hGL : T.GaugeLorentzCompatible) (Λ : SL(2,ℂ)) {w : ℕ} {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule P w) : repLorentzGroup T hGL Λ x ∈ massWeightSubmodule P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_repValue`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L369).

> Taking a weight component commutes with the ordinary gauge group.

```lean
lemma massWeightComponent_repValue (hP : IsMassWeightPoly P) (g : G.group) (k : ℕ)
    (x : T.LocalCovFieldAlgebra) :
    massWeightComponent P k (repValue T g x) = repValue T g (massWeightComponent P k x)
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_repLorentzGroup`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L375).

> Taking a weight component commutes with the Lorentz group.

```lean
lemma massWeightComponent_repLorentzGroup (hP : IsMassWeightPoly P)
    (hGL : T.GaugeLorentzCompatible) (Λ : SL(2,ℂ)) (k : ℕ) (x : T.LocalCovFieldAlgebra) :
    massWeightComponent P k (repLorentzGroup T hGL Λ x)
      = repLorentzGroup T hGL Λ (massWeightComponent P k x)
```

### D.1. The components of invariants

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_mem_invariants_repValue`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L389).

> The weight components of a gauge invariant are gauge invariant.

```lean
lemma massWeightComponent_mem_invariants_repValue (hP : IsMassWeightPoly P) (k : ℕ)
    {x : T.LocalCovFieldAlgebra} (hx : x ∈ Representation.invariants (repValue T)) :
    massWeightComponent P k x ∈ Representation.invariants (repValue T)
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_mem_invariants_repLorentzGroup`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L397).

> The weight components of a Lorentz invariant are Lorentz invariant.

```lean
lemma massWeightComponent_mem_invariants_repLorentzGroup (hP : IsMassWeightPoly P)
    (hGL : T.GaugeLorentzCompatible) (k : ℕ) {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ Representation.invariants (repLorentzGroup T hGL)) :
    massWeightComponent P k x ∈ Representation.invariants (repLorentzGroup T hGL)
```

## E. The mass-weight filtration

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmoduleLE`**, a def, [line 414](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L414).

> The mass-weight filtration, the join of the weight pieces of weight at most `w`. A
> Lagrangian of mass dimension at most `w / 2` lies in it.

```lean
noncomputable def massWeightSubmoduleLE (w : ℕ) : Submodule ℂ T.LocalCovFieldAlgebra
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule_le_massWeightSubmoduleLE`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L418).

> Each weight piece of weight at most `w` sits inside the filtration at `w`.

```lean
lemma massWeightSubmodule_le_massWeightSubmoduleLE {k w : ℕ} (hk : k ≤ w) :
    massWeightSubmodule P k ≤ massWeightSubmoduleLE P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.mem_massWeightSubmoduleLE`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L422).

```lean
lemma mem_massWeightSubmoduleLE {k w : ℕ} (hk : k ≤ w) {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule P k) : x ∈ massWeightSubmoduleLE P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmoduleLE_le`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L428).

> A submodule containing every weight piece of weight at most `w` contains the filtration
> at `w`.

```lean
lemma massWeightSubmoduleLE_le {w : ℕ} {V : Submodule ℂ T.LocalCovFieldAlgebra}
    (hV : ∀ k ≤ w, massWeightSubmodule P k ≤ V) : massWeightSubmoduleLE P w ≤ V
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmoduleLE_eq_iSup`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L433).

> The filtration as a join over a finite index type.

```lean
lemma massWeightSubmoduleLE_eq_iSup (w : ℕ) :
    massWeightSubmoduleLE P w = ⨆ k : Fin (w + 1), massWeightSubmodule P (k : ℕ)
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightComponent_mem_massWeightSubmoduleLE`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L441).

> Under `IsMassWeightPoly P`, the weight-`k` component of any element lies in the filtration
> at every `w ≥ k`.

```lean
lemma massWeightComponent_mem_massWeightSubmoduleLE (hP : IsMassWeightPoly P) {k w : ℕ}
    (hk : k ≤ w) (x : T.LocalCovFieldAlgebra) :
    massWeightComponent P k x ∈ massWeightSubmoduleLE P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmoduleLE_le_eqLocus`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L447).

> The filtration at `w` is fixed by the sum of the weight components of weight at most `w`.

```lean
lemma massWeightSubmoduleLE_le_eqLocus (w : ℕ) :
    massWeightSubmoduleLE P w ≤ LinearMap.eqLocus
      (∑ k ∈ Finset.range (w + 1), massWeightComponent P k) LinearMap.id
```

**`GaugeFieldData.LocalCovFieldAlgebra.sum_massWeightComponent_of_mem_massWeightSubmoduleLE`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L457).

> An element of the filtration at `w` is the sum of its weight components of weight at
> most `w`. No hypothesis on `P` is needed, since each weight piece has a single component.

```lean
lemma sum_massWeightComponent_of_mem_massWeightSubmoduleLE {w : ℕ} {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmoduleLE P w) :
    ∑ k ∈ Finset.range (w + 1), massWeightComponent P k x = x
```

**`GaugeFieldData.LocalCovFieldAlgebra.map_mem_massWeightSubmoduleLE`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L465).

> A map preserving every weight piece preserves the filtration.

```lean
lemma map_mem_massWeightSubmoduleLE {f : T.LocalCovFieldAlgebra →ₗ[ℂ] T.LocalCovFieldAlgebra}
    (hf : ∀ k y, y ∈ massWeightSubmodule P k → f y ∈ massWeightSubmodule P k) {w : ℕ}
    {x : T.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmoduleLE P w) :
    f x ∈ massWeightSubmoduleLE P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.repValue_mem_massWeightSubmoduleLE`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L473).

> The ordinary gauge group preserves the filtration.

```lean
lemma repValue_mem_massWeightSubmoduleLE (hP : IsMassWeightPoly P) (g : G.group) {w : ℕ}
    {x : T.LocalCovFieldAlgebra} (hx : x ∈ massWeightSubmoduleLE P w) :
    repValue T g x ∈ massWeightSubmoduleLE P w
```

**`GaugeFieldData.LocalCovFieldAlgebra.repLorentzGroup_mem_massWeightSubmoduleLE`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L479).

> The Lorentz group preserves the filtration.

```lean
lemma repLorentzGroup_mem_massWeightSubmoduleLE (hP : IsMassWeightPoly P)
    (hGL : T.GaugeLorentzCompatible) (Λ : SL(2,ℂ)) {w : ℕ} {x : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmoduleLE P w) : repLorentzGroup T hGL Λ x ∈ massWeightSubmoduleLE P w
```

## F. The weight-zero piece

**`GaugeFieldData.LocalCovFieldAlgebra.massWeightSubmodule_zero`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L494).

> When every species has positive mass weight, the weight-zero piece is the constants. The
> only product of generators of weight zero is the empty one, whose value is the unit. This is
> the constant term of a Lagrangian, the cosmological term.

```lean
lemma massWeightSubmodule_zero (hP : IsMassWeightPoly P) (hpos : T.HasPositiveMassWeights) :
    massWeightSubmodule P 0 = 1
```

## G. Supercommutativity of homogeneous elements

**`GaugeFieldData.LocalCovFieldAlgebra.mul_eq_smul_mul_of_mem_massWeightSubmodule`**, a lemma, [line 515](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L515).

> When the fermionic species have odd mass weight and the bosonic species even mass weight,
> elements of weights `v` and `w` exchange up to the sign `(-1) ^ (v * w)`, since the fermion
> parity is the parity of the mass weight.

```lean
lemma mul_eq_smul_mul_of_mem_massWeightSubmodule (hP : IsMassWeightPoly P)
    (hpar : T.HasMassWeightParity) {v w : ℕ} {x y : T.LocalCovFieldAlgebra}
    (hx : x ∈ massWeightSubmodule P v) (hy : y ∈ massWeightSubmodule P w) :
    x * y = ((-1 : ℂ) ^ (v * w)) • (y * x)
```

## Depends on

- [The covariant generators by kind and mass weight](localfieldalgebra-localcovfieldalgebra-generator.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean)
