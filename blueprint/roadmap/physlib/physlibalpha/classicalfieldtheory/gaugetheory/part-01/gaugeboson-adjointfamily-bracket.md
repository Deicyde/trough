---
declaration: module
origin: cited
lean: GaugeBoson.dualPairEquiv, GaugeBoson.tensorBracket, GaugeBoson.commutator, GaugeBoson.dualPairEquiv_tmul, GaugeBoson.tensorBracket_tmul, GaugeBoson.dualPairEquiv_map_left, GaugeBoson.dualPairEquiv_map_right, GaugeBoson.symm_comp_left
statement: formalized
proof: formalized
---

# The bracket of adjoint families

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.AdjointFamily.Bracket`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean): 50 declarations, 28 with a docstring.

> Families of symbols with one adjoint index, valued in an arbitrary algebra, and their bracket.

## i. Overview

> A gauge field in an algebra `B` of local expressions is a family of symbols `A^φ`, indexed by a
> dual vector `φ` of the gauge algebra, that is a linear map
> `Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B`. Such an adjoint family is assembled into a field in
> `B ⊗ G.lieSubalgebra` by `dualPairEquiv`, so that its adjoint index can be contracted with the
> Lie bracket. This gives the bracket of two families, `bracketFam`, the physicists'
> `f^a_{bc} f^b g^c`, and the derived commutators `commutatorFam`, the Leibniz convolutions
> `∂_s ⁅A_μ, A_ν⁆` of the derivative symbols.
>
> Nothing here assumes that `B` is commutative, and no gauge action is part of the data. The
> gauge action enters only in `repGauge_bracketFam`, for an action by multiplicative maps. The field
> strength and the covariant derivative in the adjoint are built from these formulas in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.AdjointFamily.CovariantDeriv`.

## ii. Key results

> - `GaugeBoson.dualPairEquiv`, `GaugeBoson.tensorBracket` : the tensor bookkeeping of the
>   adjoint index.
> - `GaugeBoson.bracketFam` : the bracket of two adjoint families.
> - `GaugeBoson.commutatorFam` : the derived commutators `∂_s ⁅A_μ, A_ν⁆`.
> - `GaugeBoson.repGauge_bracketFam` : the gauge transformation of a bracket of two families with
>   affine transformation laws.
> - `GaugeBoson.bracketFam_adjointDualCoeff` : the bracket against the dual adjoint Taylor
>   coefficients of a jet.
> - `GaugeBoson.massWeightEigenspace`, `GaugeBoson.anticommuteSubmodule` : the submodules through
>   which the mass weights and the statistics of covariant towers are checked term by term.

## iv. References

> * None.

**`GaugeBoson.dualPairEquiv`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L76).

> The canonical equivalence, through finite-dimensional duality, between
> algebra-valued fields `B ⊗ G.lieSubalgebra` and their component families `φ ↦ A^φ`, the element
> `b ⊗ a` corresponds to the family `φ ↦ φ(a) b`.

```lean
noncomputable def dualPairEquiv :
    (B ⊗[ℝ] G.lieSubalgebra) ≃ₗ[ℝ] (Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
```

**`GaugeBoson.tensorBracket`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L85).

> The bracket of two algebra-valued fields, multiplication in `B` on the first
> factors, the Lie bracket of the gauge algebra on the second, so that on pure
> tensors `⁅b₁ ⊗ a₁, b₂ ⊗ a₂⁆ = (b₁ b₂) ⊗ ⁅a₁, a₂⁆`.

```lean
noncomputable def tensorBracket :
    (B ⊗[ℝ] G.lieSubalgebra) →ₗ[ℝ] (B ⊗[ℝ] G.lieSubalgebra) →ₗ[ℝ] B ⊗[ℝ] G.lieSubalgebra
```

**`GaugeBoson.commutator`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L98).

> The commutator term `⁅A_μ, A_ν⁆` of the field strength, as a component family. It is
> the physicists' `f^a_{bc} A_μ^b A_ν^c` contracted with a dual adjoint vector, without a
> basis. The two fields are assembled into `B ⊗ G.lieSubalgebra` by `dualPairEquiv.symm`,
> bracketed there by `tensorBracket`, and read back out as components.

```lean
noncomputable def commutator
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

## A. Pure-tensor computations for `dualPairEquiv` and `tensorBracket`

**`GaugeBoson.dualPairEquiv_tmul`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L117).

```lean
lemma dualPairEquiv_tmul (b : B) (a : G.lieSubalgebra) (φ : Module.Dual ℝ G.lieSubalgebra) :
    dualPairEquiv (b ⊗ₜ[ℝ] a) φ = φ a • b
```

**`GaugeBoson.tensorBracket_tmul`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L122).

```lean
lemma tensorBracket_tmul (b₁ b₂ : B) (a₁ a₂ : G.lieSubalgebra) :
    tensorBracket (b₁ ⊗ₜ[ℝ] a₁) (b₂ ⊗ₜ[ℝ] a₂) = (b₁ * b₂) ⊗ₜ[ℝ] ⁅a₁, a₂⁆
```

**`GaugeBoson.dualPairEquiv_map_left`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L127).

```lean
lemma dualPairEquiv_map_left (Φ : B →ₗ[ℝ] B) (t : B ⊗[ℝ] G.lieSubalgebra)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    dualPairEquiv ((TensorProduct.map Φ LinearMap.id) t) φ = Φ (dualPairEquiv t φ)
```

**`GaugeBoson.dualPairEquiv_map_right`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L135).

```lean
lemma dualPairEquiv_map_right (T : G.lieSubalgebra →ₗ[ℝ] G.lieSubalgebra)
    (t : B ⊗[ℝ] G.lieSubalgebra) (φ : Module.Dual ℝ G.lieSubalgebra) :
    dualPairEquiv ((TensorProduct.map LinearMap.id T) t) φ =
      dualPairEquiv t (T.dualMap φ)
```

**`GaugeBoson.symm_comp_left`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L144).

```lean
lemma symm_comp_left (Φ : B →ₗ[ℝ] B) (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    dualPairEquiv.symm (Φ ∘ₗ f) =
      (TensorProduct.map Φ LinearMap.id) (dualPairEquiv.symm f)
```

**`GaugeBoson.symm_comp_right`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L154).

```lean
lemma symm_comp_right (T : G.lieSubalgebra →ₗ[ℝ] G.lieSubalgebra)
    (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    dualPairEquiv.symm (f ∘ₗ T.dualMap) =
      (TensorProduct.map LinearMap.id T) (dualPairEquiv.symm f)
```

**`GaugeBoson.tensorBracket_map_left`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L164).

```lean
lemma tensorBracket_map_left (Φ : B →ₗ[ℝ] B)
    (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂) (s t : B ⊗[ℝ] G.lieSubalgebra) :
    tensorBracket ((TensorProduct.map Φ LinearMap.id) s)
        ((TensorProduct.map Φ LinearMap.id) t) =
      (TensorProduct.map Φ LinearMap.id) (tensorBracket s t)
```

**`GaugeBoson.tensorBracket_one_right`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L178).

```lean
lemma tensorBracket_one_right (c : G.lieSubalgebra) (s : B ⊗[ℝ] G.lieSubalgebra) :
    tensorBracket s ((1 : B) ⊗ₜ[ℝ] c) =
      -(TensorProduct.map LinearMap.id (LieAlgebra.ad ℝ G.lieSubalgebra c)) s
```

**`GaugeBoson.tensorBracket_one_left`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L190).

```lean
lemma tensorBracket_one_left (c : G.lieSubalgebra) (t : B ⊗[ℝ] G.lieSubalgebra) :
    tensorBracket ((1 : B) ⊗ₜ[ℝ] c) t =
      (TensorProduct.map LinearMap.id (LieAlgebra.ad ℝ G.lieSubalgebra c)) t
```

**`GaugeBoson.dualPairEquiv_one_tmul`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L203).

```lean
lemma dualPairEquiv_one_tmul (c : G.lieSubalgebra) (φ : Module.Dual ℝ G.lieSubalgebra) :
    dualPairEquiv ((1 : B) ⊗ₜ[ℝ] c) φ = algebraMap ℂ B (φ c)
```

## B. The bracket of general component families

**`GaugeBoson.bracketFam`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L223).

> The bracket of two arbitrary component families, generalizing `commutator` (which
> is the case of two field symbols). The families are assembled into `B ⊗ G.lieSubalgebra`
> by `dualPairEquiv.symm`, bracketed by `tensorBracket`, and read back out as components.

```lean
noncomputable def bracketFam (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

**`GaugeBoson.commutator_eq_bracketFam`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L227).

```lean
lemma commutator_eq_bracketFam
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) : commutator A μ ν = bracketFam (A 0 μ) (A 0 ν)
```

**`GaugeBoson.commutatorFam`**, a def, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L235).

> The derived commutator family, the `s`-derivative of the commutator term, given
> by the Leibniz convolution of the derivative symbols over the multiset antidiagonal.
> With the derivative symbols as primitives this convolution is the definition. For
> `s = 0` it is the commutator itself (`commutatorFam_zero`).

```lean
noncomputable def commutatorFam
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

**`GaugeBoson.commutatorFam_zero`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L241).

```lean
lemma commutatorFam_zero
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) : commutatorFam A μ ν 0 = commutator A μ ν
```

**`GaugeBoson.bracketFam_add_left`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L247).

```lean
lemma bracketFam_add_left (f₁ f₂ g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam (f₁ + f₂) g = bracketFam f₁ g + bracketFam f₂ g
```

**`GaugeBoson.bracketFam_add_right`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L251).

```lean
lemma bracketFam_add_right (f g₁ g₂ : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam f (g₁ + g₂) = bracketFam f g₁ + bracketFam f g₂
```

**`GaugeBoson.bracketFam_smul_left`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L255).

```lean
lemma bracketFam_smul_left (c : ℝ) (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam (c • f) g = c • bracketFam f g
```

**`GaugeBoson.bracketFam_smul_right`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L259).

```lean
lemma bracketFam_smul_right (c : ℝ) (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam f (c • g) = c • bracketFam f g
```

**`GaugeBoson.bracketFam_apply_eq_sum`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L266).

> The bracket of two component families expanded through a basis of the gauge
> algebra, the physicists' `f^a_{bc} f^b g^c`, with `φ⁅e_j, e_k⁆` the structure
> constants contracted with the dual vector.

```lean
lemma bracketFam_apply_eq_sum (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    bracketFam f g φ = ∑ j, ∑ k,
      φ ⁅Module.Free.chooseBasis ℝ G.lieSubalgebra j,
          Module.Free.chooseBasis ℝ G.lieSubalgebra k⁆ •
        (f ((Module.Free.chooseBasis ℝ G.lieSubalgebra).coord j) *
          g ((Module.Free.chooseBasis ℝ G.lieSubalgebra).coord k))
```

**`GaugeBoson.bracketFam_apply_eq_zero_of_map_lie`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L300).

> A dual vector vanishing on every bracket of the gauge algebra, such as the coordinate of an
> abelian factor, vanishes on the bracket of any two families. Every structure constant
> `φ⁅e_j, e_k⁆` it sees is zero.

```lean
lemma bracketFam_apply_eq_zero_of_map_lie {φ : Module.Dual ℝ G.lieSubalgebra}
    (hφ : ∀ x y : G.lieSubalgebra, φ ⁅x, y⁆ = 0) (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam f g φ = 0
```

**`GaugeBoson.bracketFam_map`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L307).

> The bracket of families is natural in the algebra. A multiplicative linear map carries
> the bracket of two families to the bracket of their images.

```lean
lemma bracketFam_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam (Φ ∘ₗ f) (Φ ∘ₗ g) = Φ ∘ₗ bracketFam f g
```

**`GaugeBoson.commutatorFam_map`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L320).

> The derived commutator family is natural in the algebra.

```lean
lemma commutatorFam_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    commutatorFam (fun p ρ => Φ ∘ₗ A p ρ) μ ν s = Φ ∘ₗ commutatorFam A μ ν s
```

**`GaugeBoson.tensorBracket_map_left_derivation`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L337).

> `tensorBracket` is a derivation in the algebra factor. For `Δ` satisfying the
> Leibniz rule on `B`, applying `Δ ⊗ id` to a bracket distributes over the two
> arguments.

```lean
lemma tensorBracket_map_left_derivation (Δ : B →ₗ[ℝ] B)
    (hΔ : ∀ b₁ b₂, Δ (b₁ * b₂) = Δ b₁ * b₂ + b₁ * Δ b₂) (s t : B ⊗[ℝ] G.lieSubalgebra) :
    (TensorProduct.map Δ LinearMap.id) (tensorBracket s t) =
      tensorBracket ((TensorProduct.map Δ LinearMap.id) s) t +
      tensorBracket s ((TensorProduct.map Δ LinearMap.id) t)
```

**`GaugeBoson.bracketFam_derivation`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L355).

> The bracket of families under a derivation of the algebra, the Leibniz rule, in
> family form.

```lean
lemma bracketFam_derivation (Δ : B →ₗ[ℝ] B)
    (hΔ : ∀ b₁ b₂, Δ (b₁ * b₂) = Δ b₁ * b₂ + b₁ * Δ b₂)
      (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    Δ ∘ₗ bracketFam f g = bracketFam (Δ ∘ₗ f) g + bracketFam f (Δ ∘ₗ g)
```

## C. Antisymmetry and order of the derived commutators

> The bracket of two families is antisymmetric as soon as the values of the two families
> commute, and every derived commutator is a polynomial in symbols of no higher order.

**`GaugeBoson.bracketFam_swap_of_commute`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L383).

> The bracket of two component families with commuting values is antisymmetric. In
> the basis expansion the structure constants are antisymmetric in the two gauge
> indices, and the two field factors of each term may be exchanged.

```lean
lemma bracketFam_swap_of_commute {f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    (hfg : ∀ φ ψ, Commute (f φ) (g ψ)) :
    bracketFam g f = - bracketFam f g
```

**`GaugeBoson.commutatorFam_swap`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L401).

> The derived commutator term is antisymmetric in its two directions when the symbols
> of the gauge field commute. Swapping the two parts of the antidiagonal matches the
> Leibniz convolution with the swapped one termwise.

```lean
lemma commutatorFam_swap
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (hA : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (μ μ' : Fin 1 ⊕ Fin 3)
      (ψ ψ' : Module.Dual ℝ G.lieSubalgebra), Commute (A s μ ψ) (A s' μ' ψ'))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    commutatorFam A ν μ s = - commutatorFam A μ ν s
```

**`GaugeBoson.bracketFam_neg_right`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L414).

> The bracket of families is odd in its second argument.

```lean
lemma bracketFam_neg_right (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam f (-g) = - bracketFam f g
```

**`GaugeBoson.commutatorFam_mem`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L429).

> Every derived commutator term is a polynomial in derivative symbols of order at
> most that of the derivative. Each Leibniz splitting contributes a product of two
> lower-order symbols.

```lean
lemma commutatorFam_mem
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (ν lam : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    commutatorFam A ν lam s' φ ∈
      Algebra.adjoin ℂ {b : B | ∃ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
        (φ : Module.Dual ℝ G.lieSubalgebra), p.card ≤ s'.card ∧ b = A p μ φ}
```

## D. The gauge transformation of a bracket

**`GaugeBoson.map_dualPairEquiv_symm_of_affine`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L467).

> An affine transformation law of a family, read on the field it assembles. If `Φ` sends
> each component `f ψ` to `f' ψ + ψ(c)·1`, then `Φ ⊗ id` sends the field of `f` to the field of
> `f'` plus `1 ⊗ c`.

```lean
lemma map_dualPairEquiv_symm_of_affine (Φ : B →ₗ[ℝ] B)
    {f f' : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B} {c : G.lieSubalgebra}
    (hf : ∀ ψ : Module.Dual ℝ G.lieSubalgebra, Φ (f ψ) = f' ψ + algebraMap ℂ B (ψ c)) :
    (TensorProduct.map Φ LinearMap.id) (dualPairEquiv.symm f) =
      dualPairEquiv.symm f' + (1 : B) ⊗ₜ[ℝ] c
```

**`GaugeBoson.tensorBracket_add_one_tmul`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L479).

> The bracket of two fields shifted by constant fields `1 ⊗ c_f` and `1 ⊗ c_g`. It is the
> bracket of the unshifted fields, two `ad` cross terms, and the constant bracket.

```lean
lemma tensorBracket_add_one_tmul (s t : B ⊗[ℝ] G.lieSubalgebra) (cf cg : G.lieSubalgebra) :
    tensorBracket (s + (1 : B) ⊗ₜ[ℝ] cf) (t + (1 : B) ⊗ₜ[ℝ] cg) =
      tensorBracket s t
      + (TensorProduct.map LinearMap.id (LieAlgebra.ad ℝ G.lieSubalgebra cf)) t
      - (TensorProduct.map LinearMap.id (LieAlgebra.ad ℝ G.lieSubalgebra cg)) s
      + (1 : B) ⊗ₜ[ℝ] ⁅cf, cg⁆
```

**`GaugeBoson.repGauge_bracketFam`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L494).

> The gauge transformation of the bracket of two component families with affine
> transformation laws `f ↦ f' + φ(c_f)·1` and `g ↦ g' + φ(c_g)·1` is the bracket of the
> transformed families, two `ad` cross terms, and the constant bracket `⁅c_f, c_g⁆`.
> Pure bilinearity, with `tensorBracket_add_one_tmul` computing the cross terms. Only the
> multiplicativity of the action of `U` is used.

```lean
lemma repGauge_bracketFam
    (U : G.gaugeJetGroup)
    (hmul : ∀ b₁ b₂ : B, repGauge U (b₁ * b₂) = repGauge U b₁ * repGauge U b₂)
    {f g f' g' : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    {cf cg : G.lieSubalgebra}
    (hf : ∀ ψ : Module.Dual ℝ G.lieSubalgebra,
      repGauge U (f ψ) = f' ψ + algebraMap ℂ B (ψ cf))
    (hg : ∀ ψ : Module.Dual ℝ G.lieSubalgebra,
      repGauge U (g ψ) = g' ψ + algebraMap ℂ B (ψ cg))
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (bracketFam f g φ) =
      bracketFam f' g' φ
      + g' (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra cf)
      - f' (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra cg)
      + algebraMap ℂ B (φ ⁅cf, cg⁆)
```

## E. Iterated Leibniz expansions

**`GaugeBoson.bracketFam_zero_left`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L556).

```lean
lemma bracketFam_zero_left (g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam 0 g = 0
```

**`GaugeBoson.bracketFam_zero_right`**, a lemma, [line 560](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L560).

```lean
lemma bracketFam_zero_right (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam f 0 = 0
```

**`GaugeBoson.bracketFam_sum_left`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L564).

```lean
lemma bracketFam_sum_left (S : Multiset (Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B))
    (g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam S.sum g = (S.map fun f => bracketFam f g).sum
```

**`GaugeBoson.bracketFam_sum_right`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L571).

```lean
lemma bracketFam_sum_right (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (S : Multiset (Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)) :
    bracketFam f S.sum = (S.map fun g => bracketFam f g).sum
```

**`GaugeBoson.bracketFam_finset_sum_left`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L578).

```lean
lemma bracketFam_finset_sum_left {ι : Type*} (S : Finset ι)
    (f : ι → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) (g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam (∑ i ∈ S, f i) g = ∑ i ∈ S, bracketFam (f i) g
```

**`GaugeBoson.bracketFam_finset_sum_right`**, a lemma, [line 583](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L583).

```lean
lemma bracketFam_finset_sum_right {ι : Type*} (S : Finset ι)
    (f : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) (g : ι → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    bracketFam f (∑ i ∈ S, g i) = ∑ i ∈ S, bracketFam f (g i)
```

## F. The bracket of families against the adjoint coefficients

**`GaugeBoson.tensorBracket_map_right_antidiagonal`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L597).

> `tensorBracket` under an antidiagonal family of transports on the Lie factor. If `T x`
> distributes over the bracket as the antidiagonal convolution of the
> `T m`, so does `id ⊗ T x` over `tensorBracket`.

```lean
lemma tensorBracket_map_right_antidiagonal
    (T : Multiset (Fin 1 ⊕ Fin 3) → G.lieSubalgebra →ₗ[ℝ] G.lieSubalgebra)
    (x : Multiset (Fin 1 ⊕ Fin 3))
    (hT : ∀ a b : G.lieSubalgebra, T x ⁅a, b⁆ =
      (x.antidiagonal.map fun p => ⁅T p.1 a, T p.2 b⁆).sum)
    (s t : B ⊗[ℝ] G.lieSubalgebra) :
    (x.antidiagonal.map fun p =>
      tensorBracket ((TensorProduct.map LinearMap.id (T p.1)) s)
        ((TensorProduct.map LinearMap.id (T p.2)) t)).sum =
      (TensorProduct.map LinearMap.id (T x)) (tensorBracket s t)
```

**`GaugeBoson.bracketFam_adjointDualCoeff`**, a lemma, [line 625](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L625).

> The bracket of families against an iterated dual adjoint coefficient is the
> antidiagonal convolution of the brackets against the coefficients of the two factors.

```lean
lemma bracketFam_adjointDualCoeff (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3))
    (f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) (φ : Module.Dual ℝ G.lieSubalgebra) :
    bracketFam f g (G.adjointDualCoeff U x φ) =
      (x.antidiagonal.map fun p =>
        bracketFam (f ∘ₗ G.adjointDualCoeff U p.1)
          (g ∘ₗ G.adjointDualCoeff U p.2) φ).sum
```

## G. Mass-weight eigenspaces and anticommutants

> A covariant tower is a sum of products of symbols, so its mass weight and its statistics
> can be checked term by term once each property is a submodule. The weight-`w` eigenspace of
> an algebra map `P : B →ₐ[ℂ] Polynomial B` and the elements anticommuting with a fixed one
> are both submodules, and the bracket of two families lands in any submodule containing the
> products of their components.

**`GaugeBoson.bracketFam_apply_mem_submodule`**, a lemma, [line 665](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L665).

> The bracket pairing of two adjoint families lands in any submodule containing the
> products of their components. It is the sum of the structure constants against them.

```lean
lemma bracketFam_apply_mem_submodule {M : Submodule ℂ B}
    {f g : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    (hfg : ∀ ψ χ, f ψ * g χ ∈ M) (φ : Module.Dual ℝ G.lieSubalgebra) :
    bracketFam f g φ ∈ M
```

**`GaugeBoson.massWeightEigenspace`**, a def, [line 676](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L676).

> The weight-`w` part of `B` for a mass-weight algebra map `P`, the elements on which `P`
> is the monomial `X ^ w`.

```lean
noncomputable def massWeightEigenspace (P : B →ₐ[ℂ] Polynomial B) (w : ℕ) : Submodule ℂ B
```

**`GaugeBoson.mem_massWeightEigenspace_iff`**, a lemma, [line 681](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L681).

> Membership of the weight-`w` part is the eigenvector equation itself.

```lean
lemma mem_massWeightEigenspace_iff {P : B →ₐ[ℂ] Polynomial B} {w : ℕ} {b : B} :
    b ∈ massWeightEigenspace P w ↔ P b = Polynomial.monomial w b
```

**`GaugeBoson.mul_mem_massWeightEigenspace`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L689).

> The mass weight is additive on products. `P` is an algebra map and monomials multiply by
> adding their degrees.

```lean
lemma mul_mem_massWeightEigenspace {P : B →ₐ[ℂ] Polynomial B} {w w' : ℕ} {b b' : B}
    (hb : b ∈ massWeightEigenspace P w) (hb' : b' ∈ massWeightEigenspace P w') :
    b * b' ∈ massWeightEigenspace P (w + w')
```

**`GaugeBoson.anticommuteSubmodule`**, a def, [line 697](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L697).

> The elements of `B` anticommuting with a fixed element. It is a submodule, which is what
> lets the anticommutation of a tower be checked term by term.

```lean
def anticommuteSubmodule (x : B) : Submodule ℂ B
```

**`GaugeBoson.mem_anticommuteSubmodule_iff`**, a lemma, [line 706](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L706).

> Membership of the anticommutant is the anticommutation relation itself.

```lean
lemma mem_anticommuteSubmodule_iff {x y : B} :
    y ∈ anticommuteSubmodule x ↔ x * y = -(y * x)
```

**`GaugeBoson.anticomm_symm`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L711).

> Anticommutation is symmetric in its two arguments.

```lean
lemma anticomm_symm {a b : B} (hab : a * b = -(b * a)) : b * a = -(a * b)
```

**`GaugeBoson.mul_mem_anticommuteSubmodule`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean#L716).

> Multiplying an anticommuting element on the left by a commuting one keeps it
> anticommuting.

```lean
lemma mul_mem_anticommuteSubmodule {x a b : B} (ha : Commute x a)
    (hb : b ∈ anticommuteSubmodule x) : a * b ∈ anticommuteSubmodule x
```

## Depends on

- [The Taylor coefficients of the adjoint action](../part-02/globalgaugegroup-adjointcoeff.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/Bracket.lean)
