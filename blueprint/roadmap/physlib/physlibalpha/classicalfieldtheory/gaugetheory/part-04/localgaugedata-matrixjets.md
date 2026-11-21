---
declaration: module
origin: cited
lean: LocalGaugeData.MatrixJets, LocalGaugeData.MatrixJets.toMatJ_mul_inv, LocalGaugeData.MatrixJets.toMatJ_inv_mul, LocalGaugeData.MatrixJets.eval_ofConstant, LocalGaugeData.MatrixJets.evalLie_lie, LocalGaugeData.MatrixJets.ofConstantLie_lie, LocalGaugeData.MatrixJets.evalLie_ofConstantLie, LocalGaugeData.MatrixJets.deriv_comm
statement: formalized
proof: formalized
---

# Matrix jet groups

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.MatrixJets`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean): 39 declarations, 11 with a docstring.

## i. Overview

> Matrix gauge groups present their local gauge data in the same way: the gauge jets are
> invertible matrices of jets, the Lie algebra jets are matrices of jets, evaluation is the
> entrywise constant coefficient, constants embed entrywise, the derivative and the
> coordinates act entrywise, the adjoint action is conjugation `U a U⁻¹` and the
> Maurer–Cartan form is `i (∂_μ U) U⁻¹`. Every law of `LocalGaugeData` then follows from
> matrix identities over the jet ring. For `U(1)` and `SU(n)` the gauge jets are unitary, so
> `U⁻¹ = U†`, and the Lie algebra jets are hermitian.
>
> `MatrixJets` records such a presentation: injective maps of the four carriers into matrices,
> and what each structure map is in matrices. From it, `MatrixJets.toLocalGaugeData` proves
> the laws once, `MatrixJets.faithful` shows the package is faithful, `MatrixJets.free`
> reduces its freeness to three conditions on the carriers, and `MatrixJets.suFactor` is its
> canonical `SU`-type factor when the presentation is unitary. The concrete packages `u1`,
> `su n` and the local gauge data of a `GlobalGaugeGroup` are instances.

## ii. Key results

> - `LocalGaugeData.MatrixJets` : a presentation of gauge jets by matrices of jets.
> - `LocalGaugeData.MatrixJets.toLocalGaugeData` : the local gauge data it presents.
> - `LocalGaugeData.MatrixJets.faithful` : that local gauge data is faithful.
> - `LocalGaugeData.MatrixJets.suFactor` : its canonical `SU`-type factor.
> - `LocalGaugeData.MatrixJets.free` : a criterion for that local gauge data to be free.

## iv. References

> * None.

## A. The presentation

**`LocalGaugeData.MatrixJets`**, a structure, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L74).

> **A presentation of gauge jets by matrices**: the value group, its Lie algebra, the jet
> group and its Lie algebra of jets embed into `κ × κ` matrices, and every structure map of
> the local gauge data is what it is for matrices: the entrywise constant coefficient,
> inclusion of constants, derivative and coordinate multiplication, conjugation for the
> adjoint actions and `i (∂_μ U) U⁻¹` for the Maurer–Cartan form.

```lean
structure MatrixJets (κ : Type) [Fintype κ] [DecidableEq κ] (G₀ : Type) [Group G₀]
    (𝔤 : Type) [LieRing 𝔤] [LieAlgebra ℝ 𝔤] (GJ : Type) [Group GJ]
    (𝔤J : Type) [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J] where
  /-- The matrix of a value. -/
  toMat₀ : G₀ →* Matrix κ κ ℂ
  toMat₀_injective : Function.Injective toMat₀
  /-- The matrix of jets of a gauge jet. -/
  toMatJ : GJ →* Matrix κ κ SpaceTimeAlgebra
  toMatJ_injective : Function.Injective toMatJ
  /-- The matrix of a Lie algebra element. -/
  lie₀ : 𝔤 →ₗ[ℝ] Matrix κ κ ℂ
  lie₀_injective : Function.Injective lie₀
  lie₀_bracket : ∀ a b, lie₀ ⁅a, b⁆ = Complex.I • (lie₀ a * lie₀ b - lie₀ b * lie₀ a)
  /-- The matrix of jets of a Lie algebra jet. -/
  lieJ : 𝔤J →ₗ[ℝ] Matrix κ κ SpaceTimeAlgebra
  lieJ_injective : Function.Injective lieJ
  lieJ_bracket : ∀ a b, lieJ ⁅a, b⁆ = Complex.I • (lieJ a * lieJ b - lieJ b * lieJ a)
  /-- Evaluation of a gauge jet at the base point. -/
  eval : GJ →* G₀
  toMat₀_eval : ∀ U, toMat₀ (eval U) = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (toMatJ U)
  /-- A constant gauge transformation as a jet. -/
  ofConstant : G₀ →* GJ
  toMatJ_ofConstant : ∀ g, toMatJ (ofConstant g) = (C : ℂ →+* SpaceTimeAlgebra).mapMatrix (toMat₀ g)
  /-- Evaluation of a Lie algebra jet at the base point. -/
  evalLie : 𝔤J →ₗ[ℝ] 𝔤
  lie₀_evalLie : ∀ a, lie₀ (evalLie a) = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (lieJ a)
  /-- A constant Lie algebra element as a jet. -/
  ofConstantLie : 𝔤 →ₗ[ℝ] 𝔤J
  lieJ_ofConstantLie : ∀ a, lieJ (ofConstantLie a) = (C : ℂ →+* SpaceTimeAlgebra).mapMatrix (lie₀ a)
  /-- The formal derivative in the direction `μ`. -/
  deriv : (Fin 1 ⊕ Fin 3) → 𝔤J →ₗ[ℝ] 𝔤J
  lieJ_deriv : ∀ μ a, lieJ (deriv μ a) = (lieJ a).map (pderiv μ)
  /-- Multiplication of a jet by the spacetime coordinate `x_μ`. -/
  coord : (Fin 1 ⊕ Fin 3) → 𝔤J →ₗ[ℝ] 𝔤J
  lieJ_coord : ∀ μ a, lieJ (coord μ a) = (X μ : SpaceTimeAlgebra) • lieJ a
  /-- The adjoint action of the jet group on the jet Lie algebra. -/
  adjoint : Representation ℝ GJ 𝔤J
  lieJ_adjoint : ∀ U a, lieJ (adjoint U a) = toMatJ U * lieJ a * toMatJ U⁻¹
  /-- The adjoint representation of the value group on its Lie algebra. -/
  adjointValue : Representation ℝ G₀ 𝔤
  lie₀_adjointValue : ∀ g a, lie₀ (adjointValue g a) = toMat₀ g * lie₀ a * toMat₀ g⁻¹
  /-- The Maurer–Cartan form `i (∂_μ U) U⁻¹` of a gauge jet. -/
  maurerCartan : GJ → (Fin 1 ⊕ Fin 3) → 𝔤J
  lieJ_maurerCartan : ∀ U μ, lieJ (maurerCartan U μ)
    = Complex.I • ((toMatJ U).map (pderiv μ) * toMatJ U⁻¹)
```

**`LocalGaugeData.MatrixJets.toMatJ_mul_inv`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L125).

```lean
lemma toMatJ_mul_inv (U : GJ) : M.toMatJ U * M.toMatJ U⁻¹ = 1
```

**`LocalGaugeData.MatrixJets.toMatJ_inv_mul`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L129).

```lean
lemma toMatJ_inv_mul (U : GJ) : M.toMatJ U⁻¹ * M.toMatJ U = 1
```

## B. The local gauge data

> Every law is an identity of matrices, read through the injective maps `lieJ` and `toMat₀`.

**`LocalGaugeData.MatrixJets.eval_ofConstant`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L140).

```lean
lemma eval_ofConstant (g : G₀) : M.eval (M.ofConstant g) = g
```

**`LocalGaugeData.MatrixJets.evalLie_lie`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L146).

```lean
lemma evalLie_lie (a b : 𝔤J) : M.evalLie ⁅a, b⁆ = ⁅M.evalLie a, M.evalLie b⁆
```

**`LocalGaugeData.MatrixJets.ofConstantLie_lie`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L151).

```lean
lemma ofConstantLie_lie (a b : 𝔤) :
    M.ofConstantLie ⁅a, b⁆ = ⁅M.ofConstantLie a, M.ofConstantLie b⁆
```

**`LocalGaugeData.MatrixJets.evalLie_ofConstantLie`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L157).

```lean
lemma evalLie_ofConstantLie (a : 𝔤) : M.evalLie (M.ofConstantLie a) = a
```

**`LocalGaugeData.MatrixJets.deriv_comm`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L163).

```lean
lemma deriv_comm (μ ν : Fin 1 ⊕ Fin 3) (a : 𝔤J) :
    M.deriv μ (M.deriv ν a) = M.deriv ν (M.deriv μ a)
```

**`LocalGaugeData.MatrixJets.deriv_bracket`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L170).

```lean
lemma deriv_bracket (μ : Fin 1 ⊕ Fin 3) (x y : 𝔤J) :
    M.deriv μ ⁅x, y⁆ = ⁅M.deriv μ x, y⁆ + ⁅x, M.deriv μ y⁆
```

**`LocalGaugeData.MatrixJets.deriv_ofConstantLie`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L180).

```lean
lemma deriv_ofConstantLie (μ : Fin 1 ⊕ Fin 3) (a : 𝔤) : M.deriv μ (M.ofConstantLie a) = 0
```

**`LocalGaugeData.MatrixJets.deriv_coord`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L186).

```lean
lemma deriv_coord (μ ν : Fin 1 ⊕ Fin 3) (a : 𝔤J) :
    M.deriv μ (M.coord ν a) = M.coord ν (M.deriv μ a) + if μ = ν then a else 0
```

**`LocalGaugeData.MatrixJets.evalLie_coord`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L201).

```lean
lemma evalLie_coord (μ : Fin 1 ⊕ Fin 3) (a : 𝔤J) : M.evalLie (M.coord μ a) = 0
```

**`LocalGaugeData.MatrixJets.coord_lie`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L207).

```lean
lemma coord_lie (μ : Fin 1 ⊕ Fin 3) (a b : 𝔤J) : ⁅M.coord μ a, b⁆ = M.coord μ ⁅a, b⁆
```

**`LocalGaugeData.MatrixJets.conj_mul_conj`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L214).

> Conjugation by an invertible matrix respects products.

```lean
lemma conj_mul_conj (U : GJ) (A B : Matrix κ κ SpaceTimeAlgebra) :
    (M.toMatJ U * A * M.toMatJ U⁻¹) * (M.toMatJ U * B * M.toMatJ U⁻¹)
      = M.toMatJ U * (A * B) * M.toMatJ U⁻¹
```

**`LocalGaugeData.MatrixJets.adjoint_lie`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L221).

```lean
lemma adjoint_lie (U : GJ) (x y : 𝔤J) :
    M.adjoint U ⁅x, y⁆ = ⁅M.adjoint U x, M.adjoint U y⁆
```

**`LocalGaugeData.MatrixJets.evalLie_adjoint`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L228).

```lean
lemma evalLie_adjoint (U : GJ) (x : 𝔤J) :
    M.evalLie (M.adjoint U x) = M.adjointValue (M.eval U) (M.evalLie x)
```

**`LocalGaugeData.MatrixJets.maurerCartan_ofConstant`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L234).

```lean
lemma maurerCartan_ofConstant (g : G₀) (μ : Fin 1 ⊕ Fin 3) :
    M.maurerCartan (M.ofConstant g) μ = 0
```

**`LocalGaugeData.MatrixJets.maurerCartan_cocycle`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L241).

```lean
lemma maurerCartan_cocycle (U V : GJ) (μ : Fin 1 ⊕ Fin 3) :
    M.maurerCartan (U * V) μ = M.maurerCartan U μ + M.adjoint U (M.maurerCartan V μ)
```

**`LocalGaugeData.MatrixJets.maurerCartan_structure`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L249).

```lean
lemma maurerCartan_structure (U : GJ) (μ ν : Fin 1 ⊕ Fin 3) :
    M.deriv μ (M.maurerCartan U ν) - M.deriv ν (M.maurerCartan U μ)
      + ⁅M.maurerCartan U μ, M.maurerCartan U ν⁆ = 0
```

**`LocalGaugeData.MatrixJets.deriv_adjoint`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L276).

```lean
lemma deriv_adjoint (U : GJ) (μ : Fin 1 ⊕ Fin 3) (x : 𝔤J) :
    M.deriv μ (M.adjoint U x) = M.adjoint U (M.deriv μ x)
      - ⁅M.maurerCartan U μ, M.adjoint U x⁆
```

**`LocalGaugeData.MatrixJets.evalLieHom`**, a def, [line 294](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L294).

> Evaluation of Lie algebra jets, as a morphism of Lie algebras.

```lean
noncomputable def evalLieHom : 𝔤J →ₗ⁅ℝ⁆ 𝔤
```

**`LocalGaugeData.MatrixJets.evalLieHom_apply`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L299).

```lean
lemma evalLieHom_apply (a : 𝔤J) : M.evalLieHom a = M.evalLie a
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L302).

> **The local gauge data presented by matrices of jets.**

```lean
noncomputable def toLocalGaugeData : LocalGaugeData G₀ 𝔤 GJ 𝔤J
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_eval`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L327).

```lean
lemma toLocalGaugeData_eval : M.toLocalGaugeData.eval = M.eval
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_ofConstant`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L328).

```lean
lemma toLocalGaugeData_ofConstant : M.toLocalGaugeData.ofConstant = M.ofConstant
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_evalLie_apply`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L329).

```lean
lemma toLocalGaugeData_evalLie_apply (a : 𝔤J) :
    M.toLocalGaugeData.evalLie a = M.evalLie a
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_ofConstantLie`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L331).

```lean
lemma toLocalGaugeData_ofConstantLie :
    M.toLocalGaugeData.ofConstantLie = M.ofConstantLie
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_deriv`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L333).

```lean
lemma toLocalGaugeData_deriv (μ : Fin 1 ⊕ Fin 3) :
    M.toLocalGaugeData.deriv μ = M.deriv μ
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_mulCoord`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L335).

```lean
lemma toLocalGaugeData_mulCoord (μ : Fin 1 ⊕ Fin 3) :
    M.toLocalGaugeData.mulCoord μ = M.coord μ
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_adjointJ`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L337).

```lean
lemma toLocalGaugeData_adjointJ : M.toLocalGaugeData.adjointJ = M.adjoint
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_adjoint`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L338).

```lean
lemma toLocalGaugeData_adjoint :
    M.toLocalGaugeData.adjoint = M.adjointValue
```

**`LocalGaugeData.MatrixJets.toLocalGaugeData_maurerCartan`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L340).

```lean
lemma toLocalGaugeData_maurerCartan :
    M.toLocalGaugeData.maurerCartan = M.maurerCartan
```

## C. The iterated derivative and faithfulness

**`LocalGaugeData.MatrixJets.lieJ_iteratedDeriv`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L350).

> The iterated derivative is the entrywise iterated formal derivative.

```lean
lemma lieJ_iteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J) :
    M.lieJ (M.toLocalGaugeData.iteratedDeriv s a)
      = (M.lieJ a).map fun f => SpaceTimeAlgebra.iteratedPDeriv s f
```

**`LocalGaugeData.MatrixJets.lie₀_evalLie_iteratedDeriv`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L366).

> The base-point value of the iterated derivative, entrywise.

```lean
lemma lie₀_evalLie_iteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J) :
    M.lie₀ (M.toLocalGaugeData.evalLie (M.toLocalGaugeData.iteratedDeriv s a))
      = (M.lieJ a).map fun f => constantCoeff (SpaceTimeAlgebra.iteratedPDeriv s f)
```

**`LocalGaugeData.MatrixJets.faithful`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L376).

> **A package presented by matrices is faithful**: a jet is determined entrywise by the
> constant coefficients of its derivatives, and a jet with vanishing Maurer–Cartan form has
> constant entries.

```lean
lemma faithful : M.toLocalGaugeData.Faithful
```

## D. The canonical factor

**`LocalGaugeData.MatrixJets.suFactor`**, a def, [line 408](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L408).

> **The canonical `SU`-type factor** of a package presented by unitary matrices, those
> whose inverse is the conjugate transpose: the matrices of jets themselves.

```lean
noncomputable def suFactor (hstar : ∀ U, star (M.toMatJ U) = M.toMatJ U⁻¹) :
    SUFactor M.toLocalGaugeData κ
```

## E. Freeness

> A presentation by matrices is free when its carriers are large enough: the Lie algebra
> jets contain every matrix of jets with Taylor data in the Lie algebra, and the gauge jets
> contain the unitary fundamental solution `V` of the radial system `E V = −i P V` for every
> Lie algebra jet `P`. Taylor completeness and radial integrability then hold because they
> hold for matrices of jets.

**`LocalGaugeData.MatrixJets.lieJ_radial`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L433).

> The radial component of the Maurer–Cartan form, in matrices:
> `∑_μ x_μ · i (∂_μ U) U⁻¹`.

```lean
lemma lieJ_radial (U : GJ) :
    M.lieJ (M.toLocalGaugeData.radial U) =
      ∑ μ, (X μ : SpaceTimeAlgebra) •
          (Complex.I • ((M.toMatJ U).map (pderiv μ) * M.toMatJ U⁻¹))
```

**`LocalGaugeData.MatrixJets.mem_truncationKer_zero_iff`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L441).

> A gauge jet is pure exactly when its matrix is the identity at the base point.

```lean
lemma mem_truncationKer_zero_iff (U : GJ) :
    U ∈ M.toLocalGaugeData.truncationKer 0 ↔
      (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (M.toMatJ U) = 1
```

**`LocalGaugeData.MatrixJets.free`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean#L452).

> **A criterion for freeness.** A presentation by matrices is free when every matrix of
> jets built entrywise from Taylor data in `𝔤` is a Lie algebra jet, the Lie algebra jets
> are hermitian, and every unitary solution `V` of `E V = −i P V`, `V(0) = 1`, for a Lie
> algebra jet `P`, is a gauge jet.

```lean
lemma free
    (hTaylor : ∀ c : Multiset (Fin 1 ⊕ Fin 3) → 𝔤,
      ∃ Y, M.lieJ Y = SpaceTimeAlgebra.taylorMatrix fun s => M.lie₀ (c s))
    (hherm : ∀ a, star (M.lieJ a) = M.lieJ a)
    (hlift : ∀ (ρ : 𝔤J) (V : Matrix κ κ SpaceTimeAlgebra),
      (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix V = 1 → V * star V = 1 →
      ∑ μ, (X μ : SpaceTimeAlgebra) • V.map (pderiv μ) = ((-Complex.I) • M.lieJ ρ) * V →
      ∃ U, M.toMatJ U = V) :
    M.toLocalGaugeData.Free
```

## Depends on

- [The factors of a gauge group](localgaugedata-factor.md)
- [The truncation filtration of the jet gauge group](localgaugedata-truncation.md)
- [Taylor determinacy and completeness of jets](../../../spaceandtime/spacetime/spacetimealgebra-taylor.md)

## Proof depends on

- [Matrices over the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-matrix.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/MatrixJets.lean)
