---
declaration: module
origin: cited
lean: LocalGaugeData, LocalGaugeData.eval_surjective, LocalGaugeData.ofConstant_injective, LocalGaugeData.evalLie_surjective, LocalGaugeData.ofConstantLie_injective, LocalGaugeData.adjoint_bracket, LocalGaugeData.deriv_adjointJ_ofConstant, LocalGaugeData.instRightCommutativeCompDeriv
statement: formalized
proof: formalized
---

# Local gauge data

The module `Physlib.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Basic`, [Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean): 23 declarations, 11 with a docstring.

> The jets of gauge transformations at a point, as the data a local Lagrangian sees.

## i. Overview

> The full gauge group of a theory is some class of functions from spacetime to a global gauge
> group `G₀` with Lie algebra `𝔤`; for the Standard Model `G₀ = SU(3) × SU(2) × U(1)`, ignoring
> discrete quotients. Physicists are usually agnostic about which class, because a local
> Lagrangian only sees how a gauge transformation acts on the fields and finitely many of their
> derivatives at a point `x`, and that depends only on the Taylor series of the gauge transformation
> at `x`. If every smooth function is an allowed gauge transformation — the one assumption made
> about the class — then by Borel's theorem every Taylor series compatible with the group
> arises, convergent or not. These Taylor series, the *jets* at `x`, form the group `GJ`, and
> their infinitesimal counterparts the Lie algebra `𝔤J` over `ℝ`.
>
> How best to present `GJ` depends on `G₀`, so it is taken as input rather than constructed.
> For a matrix group such as `SU(2)`, the jet of a gauge transformation is a matrix with entries
> in `SpaceTimeAlgebra`, the formal Taylor series at `x`. The Taylor series of a product is the
> product of the Taylor series, so the group law is still matrix multiplication, and `GJ` is cut
> out by the same equations `U† U = 1` and `det U = 1` read over `SpaceTimeAlgebra`; likewise
> `𝔤J` is the traceless self-adjoint matrices over `SpaceTimeAlgebra` with the usual bracket
> ` ⁅A, B⁆ = i(AB − BA)`.

## ii. Key results

> - `LocalGaugeData` : the structure.
> - `LocalGaugeData.adjoint_bracket` : the adjoint action of `G₀` on `𝔤` is by Lie algebra
>   automorphisms, from the jet-level law applied to constants.
> - `LocalGaugeData.iteratedDeriv` : the iterated derivative `∂_s` on `𝔤J` along a multiset
>   of directions, with `iteratedDeriv_cons`, `iteratedDeriv_add` and the iterated Leibniz
>   rule `iteratedDeriv_bracket`.
> - `LocalGaugeData.evalLie_iteratedDeriv_mulCoord` : the coordinate multiplication identity
> - `LocalGaugeData.Hom` : a morphism of local gauge data, with `Hom.id` and `Hom.comp`.

## iv. References

## A. The structure

> We package this local information of a gauge group into the structure `LocalGaugeData G₀ 𝔤 GJ 𝔤J`.
> Alongside the four carriers, it records the operations that the transformation laws of gauge fields
> and matter fields are built from, and the coordinates that place a jet around the base point.
> It consists of:
>
> * the inclusion of constants and evaluation at the base point, on the group and on the
>   Lie algebra;
> * the formal spacetime derivatives `deriv μ` on `𝔤J`, commuting, satisfying the Leibniz
>   rule for the bracket, and killing constants;
> * multiplication by the coordinates `mulCoord μ`, vanishing at the base point and central for
>   the bracket, with `∂_μ (x_ν a) = x_ν ∂_μ a + δ_{μν} a`;
> * the adjoint action of `GJ` on `𝔤J`, by Lie algebra automorphisms, evaluating at the base
>   point to the adjoint action of `G₀` on `𝔤`;
> * the Maurer–Cartan form `maurerCartan U μ = i (∂_μ U) U⁻¹`, with its cocycle law, its
>   flatness equation `maurerCartan_structure` and the Leibniz rule `deriv_adjointJ` for the
>   adjoint action.

**`LocalGaugeData`**, a structure, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L96).

> Local gauge data. A gauge group `G₀` with Lie algebra `𝔤`, its group of jets `GJ` with
> Lie algebra of jets `𝔤J`, evaluation at the base point, formal derivatives, the adjoint
> action and the Maurer–Cartan form, subject to the identities used by the transformation
> laws of gauge and matter fields.

```lean
structure LocalGaugeData (G₀ : Type) [Group G₀] (𝔤 : Type) [LieRing 𝔤] [LieAlgebra ℝ 𝔤]
    (GJ : Type) [Group GJ] (𝔤J : Type) [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J] where
  /-- Evaluation of a gauge jet at the base point. -/
  eval : GJ →* G₀
  /-- A constant gauge transformation as a jet. -/
  ofConstant : G₀ →* GJ
  eval_ofConstant : ∀ g, eval (ofConstant g) = g
  /-- Evaluation of a Lie algebra jet at the base point. -/
  evalLie : 𝔤J →ₗ⁅ℝ⁆ 𝔤
  /-- A constant Lie algebra element as a jet. -/
  ofConstantLie : 𝔤 →ₗ⁅ℝ⁆ 𝔤J
  evalLie_ofConstantLie : ∀ a, evalLie (ofConstantLie a) = a
  /-- The formal derivative in the direction `μ`. -/
  deriv : (Fin 1 ⊕ Fin 3) → 𝔤J →ₗ[ℝ] 𝔤J
  deriv_comm : ∀ (μ ν : Fin 1 ⊕ Fin 3) (a : 𝔤J), deriv μ (deriv ν a) = deriv ν (deriv μ a)
  deriv_bracket : ∀ (μ : Fin 1 ⊕ Fin 3) (x y : 𝔤J),
    deriv μ ⁅x, y⁆ = ⁅deriv μ x, y⁆ + ⁅x, deriv μ y⁆
  deriv_ofConstantLie : ∀ (μ : Fin 1 ⊕ Fin 3) (a : 𝔤), deriv μ (ofConstantLie a) = 0
  /-- Multiplication of a jet by the spacetime coordinate `x_μ`. -/
  mulCoord : (Fin 1 ⊕ Fin 3) → 𝔤J →ₗ[ℝ] 𝔤J
  /-- The Leibniz rule for a coordinate: `∂_μ (x_ν a) = x_ν ∂_μ a + δ_{μν} a`. -/
  deriv_mulCoord : ∀ (μ ν : Fin 1 ⊕ Fin 3) (a : 𝔤J),
    deriv μ (mulCoord ν a) = mulCoord ν (deriv μ a) + if μ = ν then a else 0
  /-- A multiple of a coordinate vanishes at the base point. -/
  evalLie_mulCoord : ∀ (μ : Fin 1 ⊕ Fin 3) (a : 𝔤J), evalLie (mulCoord μ a) = 0
  /-- Multiplication by a coordinate commutes with the bracket. -/
  mulCoord_bracket : ∀ (μ : Fin 1 ⊕ Fin 3) (a b : 𝔤J), ⁅mulCoord μ a, b⁆ = mulCoord μ ⁅a, b⁆
  /-- The adjoint action of the jet group on the jet Lie algebra. -/
  adjointJ : Representation ℝ GJ 𝔤J
  adjointJ_bracket : ∀ (U : GJ) (x y : 𝔤J), adjointJ U ⁅x, y⁆ = ⁅adjointJ U x, adjointJ U y⁆
  /-- The adjoint representation of the value group on its Lie algebra. -/
  adjoint : Representation ℝ G₀ 𝔤
  /-- At the base point the adjoint action of a jet is the adjoint action of its value. -/
  evalLie_adjointJ : ∀ (U : GJ) (x : 𝔤J), evalLie (adjointJ U x) = adjoint (eval U) (evalLie x)
  /-- The Maurer–Cartan form `i (∂_μ U) U⁻¹` of a gauge jet. -/
  maurerCartan : GJ → (Fin 1 ⊕ Fin 3) → 𝔤J
  /-- A constant gauge transformation has vanishing Maurer–Cartan form: it has no
    spacetime dependence to differentiate. -/
  maurerCartan_ofConstant : ∀ (g : G₀) (μ : Fin 1 ⊕ Fin 3), maurerCartan (ofConstant g) μ = 0
  /-- The Maurer–Cartan form is a cocycle for the adjoint action. -/
  maurerCartan_cocycle : ∀ (U V : GJ) (μ : Fin 1 ⊕ Fin 3),
    maurerCartan (U * V) μ = maurerCartan U μ + adjointJ U (maurerCartan V μ)
  /-- The Maurer–Cartan form is flat. -/
  maurerCartan_structure : ∀ (U : GJ) (μ ν : Fin 1 ⊕ Fin 3),
    deriv μ (maurerCartan U ν) - deriv ν (maurerCartan U μ)
      + ⁅maurerCartan U μ, maurerCartan U ν⁆ = 0
  /-- The Leibniz rule for the adjoint action. -/
  deriv_adjointJ : ∀ (U : GJ) (μ : Fin 1 ⊕ Fin 3) (x : 𝔤J),
    deriv μ (adjointJ U x) = adjointJ U (deriv μ x) - ⁅maurerCartan U μ, adjointJ U x⁆
```

## B. Simple derived properties

**`LocalGaugeData.eval_surjective`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L165).

> Every global gauge transformation is the value of a jet, namely its constant jet.

```lean
lemma eval_surjective : Function.Surjective jets.eval
```

**`LocalGaugeData.ofConstant_injective`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L168).

```lean
lemma ofConstant_injective : Function.Injective jets.ofConstant
```

**`LocalGaugeData.evalLie_surjective`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L171).

```lean
lemma evalLie_surjective : Function.Surjective jets.evalLie
```

**`LocalGaugeData.ofConstantLie_injective`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L174).

```lean
lemma ofConstantLie_injective : Function.Injective jets.ofConstantLie
```

**`LocalGaugeData.adjoint_bracket`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L177).

```lean
lemma adjoint_bracket (g : G₀) (a b : 𝔤) :
    jets.adjoint g ⁅a, b⁆ = ⁅jets.adjoint g a, jets.adjoint g b⁆
```

**`LocalGaugeData.deriv_adjointJ_ofConstant`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L185).

```lean
lemma deriv_adjointJ_ofConstant (g : G₀) (μ : Fin 1 ⊕ Fin 3) (x : 𝔤J) :
    jets.deriv μ (jets.adjointJ (jets.ofConstant g) x) =
      jets.adjointJ (jets.ofConstant g) (jets.deriv μ x)
```

## C. The iterated derivative on the jet Lie algebra

### C.1. Commutativity of derivatives

**`LocalGaugeData.instRightCommutativeCompDeriv`**, an instance, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L203).

> Post-composition with `deriv` is right-commutative.

```lean
instance instRightCommutativeCompDeriv : RightCommutative
    (fun (D : 𝔤J →ₗ[ℝ] 𝔤J) (μ : Fin 1 ⊕ Fin 3) => D.comp (jets.deriv μ))
```

### C.2. Definition of the iterated derivative

**`LocalGaugeData.iteratedDeriv`**, a def, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L216).

> The iterated formal derivative on the jet Lie algebra.

```lean
noncomputable def iteratedDeriv (μs : Multiset (Fin 1 ⊕ Fin 3)) : 𝔤J →ₗ[ℝ] 𝔤J
```

### C.3. Properties of the iterated derivative

**`LocalGaugeData.iteratedDeriv_zero`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L226).

```lean
lemma iteratedDeriv_zero : jets.iteratedDeriv (0 : Multiset (Fin 1 ⊕ Fin 3)) = LinearMap.id
```

**`LocalGaugeData.iteratedDeriv_cons`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L229).

```lean
lemma iteratedDeriv_cons (μ : Fin 1 ⊕ Fin 3) (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    jets.iteratedDeriv (μ ::ₘ μs) = (jets.deriv μ).comp (jets.iteratedDeriv μs)
```

**`LocalGaugeData.iteratedDeriv_add`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L244).

> The iterated derivative is additive in the multiset.

```lean
lemma iteratedDeriv_add (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    jets.iteratedDeriv (s + t) = (jets.iteratedDeriv s).comp (jets.iteratedDeriv t)
```

**`LocalGaugeData.iteratedDeriv_singleton`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L253).

```lean
lemma iteratedDeriv_singleton (μ : Fin 1 ⊕ Fin 3) :
    jets.iteratedDeriv ({μ} : Multiset (Fin 1 ⊕ Fin 3)) = jets.deriv μ
```

**`LocalGaugeData.iteratedDeriv_cons_eq_comp_deriv`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L258).

```lean
lemma iteratedDeriv_cons_eq_comp_deriv (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    jets.iteratedDeriv (μ ::ₘ s) = (jets.iteratedDeriv s).comp (jets.deriv μ)
```

**`LocalGaugeData.iteratedDeriv_bracket`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L265).

> The iterated Leibniz rule for the bracket.

```lean
lemma iteratedDeriv_bracket (s : Multiset (Fin 1 ⊕ Fin 3)) (a b : 𝔤J) :
    jets.iteratedDeriv s ⁅a, b⁆ =
      (s.antidiagonal.map fun p =>
        ⁅jets.iteratedDeriv p.1 a, jets.iteratedDeriv p.2 b⁆).sum
```

**`LocalGaugeData.iteratedDeriv_ofConstantLie_of_ne_zero`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L287).

```lean
lemma iteratedDeriv_ofConstantLie_of_ne_zero {p : Multiset (Fin 1 ⊕ Fin 3)} (hp : p ≠ 0)
    (a : 𝔤) : jets.iteratedDeriv p (jets.ofConstantLie a) = 0
```

**`LocalGaugeData.iteratedDeriv_adjointJ_ofConstant`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L297).

```lean
lemma iteratedDeriv_adjointJ_ofConstant (g : G₀) (s : Multiset (Fin 1 ⊕ Fin 3)) (x : 𝔤J) :
    jets.iteratedDeriv s (jets.adjointJ (jets.ofConstant g) x) =
      jets.adjointJ (jets.ofConstant g) (jets.iteratedDeriv s x)
```

**`LocalGaugeData.evalLie_iteratedDeriv_mulCoord`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L304).

```lean
lemma evalLie_iteratedDeriv_mulCoord (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J) :
    jets.evalLie (jets.iteratedDeriv s (jets.mulCoord μ a)) =
      s.count μ • jets.evalLie (jets.iteratedDeriv (s.erase μ) a)
```

## D. Morphisms

**`LocalGaugeData.Hom`**, a structure, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L329).

> A morphism of local gauge data.
>
> `Hom` is the standard name for a morphism in Lean.

```lean
structure Hom (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) (jets' : LocalGaugeData G₀' 𝔤' GJ' 𝔤J') where
  /-- The map of gauge groups. -/
  group : G₀ →* G₀'
  /-- The map of jet groups. -/
  groupJ : GJ →* GJ'
  eval_groupJ : ∀ U, jets'.eval (groupJ U) = group (jets.eval U)
  groupJ_ofConstant : ∀ g, groupJ (jets.ofConstant g) = jets'.ofConstant (group g)
  /-- The map of Lie algebras. -/
  lie : 𝔤 →ₗ⁅ℝ⁆ 𝔤'
  /-- The map of Lie algebras of jets. -/
  lieJ : 𝔤J →ₗ⁅ℝ⁆ 𝔤J'
  lieJ_ofConstantLie : ∀ c, lieJ (jets.ofConstantLie c) = jets'.ofConstantLie (lie c)
  evalLie_lieJ : ∀ a, jets'.evalLie (lieJ a) = lie (jets.evalLie a)
  lieJ_deriv : ∀ μ a, lieJ (jets.deriv μ a) = jets'.deriv μ (lieJ a)
  lieJ_mulCoord : ∀ μ a, lieJ (jets.mulCoord μ a) = jets'.mulCoord μ (lieJ a)
  lieJ_adjointJ : ∀ U a, lieJ (jets.adjointJ U a) = jets'.adjointJ (groupJ U) (lieJ a)
  lieJ_maurerCartan : ∀ U μ, lieJ (jets.maurerCartan U μ) = jets'.maurerCartan (groupJ U) μ
```

### D.1. The adjoint action

**`LocalGaugeData.Hom.lie_adjoint`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L361).

> A morphism intertwines the adjoint actions of the gauge groups.

```lean
lemma lie_adjoint (g : G₀) (x : 𝔤) :
    f.lie (jets.adjoint g x) = jets'.adjoint (f.group g) (f.lie x)
```

### D.2. Relation to iterated derivatives

**`LocalGaugeData.Hom.lieJ_iteratedDeriv`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L375).

> A morphism commutes with iterated derivatives.

```lean
lemma lieJ_iteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J) :
    f.lieJ (jets.iteratedDeriv s a) = jets'.iteratedDeriv s (f.lieJ a)
```

### D.3. Identity morphisms

**`LocalGaugeData.Hom.id`**, a def, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L390).

> The identity morphism of local gauge data.

```lean
protected def id (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) : Hom jets jets
```

### D.4. Composition of morphisms

**`LocalGaugeData.Hom.comp`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean#L415).

> The composite `g ∘ f` of morphisms of local gauge data.

```lean
def comp (g : Hom jets' jets'') : Hom jets jets''
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Basic.lean)
