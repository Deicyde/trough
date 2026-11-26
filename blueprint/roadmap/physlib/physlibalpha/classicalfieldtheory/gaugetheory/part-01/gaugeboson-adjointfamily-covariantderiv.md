---
declaration: module
origin: cited
lean: GaugeBoson.fieldStrength, GaugeBoson.fieldStrength_apply, GaugeBoson.fieldStrength_zero, GaugeBoson.pair_eq_fieldStrength_sub_commutatorFam, GaugeBoson.fieldStrength_swap, GaugeBoson.fieldStrength_map, GaugeBoson.bracketFamConv, GaugeBoson.covDerivAdjoint
statement: formalized
proof: formalized
---

# The field strength and the covariant derivative of an adjoint family

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.AdjointFamily.CovariantDeriv`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean): 26 declarations, 24 with a docstring.

> The field strength of a family of gauge-field symbols, the covariant derivative in the
> adjoint, and the gauge law of an adjoint gauge tensor.

## i. Overview

> Let `A` be a family of gauge-field symbols `∂_s A_μ^φ` in an algebra `B`, indexed by a
> derivative multiset `s`, a direction `μ` and a dual vector `φ` of the gauge algebra. Its field
> strength is
> ```
>   F_{μν} = ∂_μ A_ν − ∂_ν A_μ + ⁅A_μ, A_ν⁆
> ```
> with `⁅·,·⁆` the gauge-algebra bracket, which carries the physicists' factor of `i` (on the
> matrix factors `⁅a, b⁆ = i(ab − ba)`). In terms of the plain matrix commutator this is
> `F_{μν} = ∂_μ A_ν − ∂_ν A_μ + i [A_μ, A_ν]`, the sign forced by the convention
> `ω_μ(g) = i (∂_μ g) g⁻¹` for the Maurer–Cartan form. With the derivative symbols as primitives
> the field strength is itself a family of derivative symbols `s ↦ [∂_s F_μν]`. The derivative
> terms shift the multiset index, and the commutator term is the Leibniz convolution
> `commutatorFam`.
>
> The covariant derivative of an adjoint family `F` is `∇_ρ F = [∂_ρ F] + ⁅A_ρ, F⁆`, and
> `iteratedCovDerivAdjoint` iterates it along a list of directions. All of these are formulas in
> an arbitrary algebra `B`, natural under multiplicative linear maps (`fieldStrength_map`,
> `iteratedCovDerivAdjoint_map`).
>
> A family transforms in the adjoint, `TransformsInAdjoint`, when every derivative symbol
> transforms by the Leibniz convolution of the dual adjoint coefficients of the jet, with no
> inhomogeneous term. That the field strength and its covariant derivatives transform in the
> adjoint is proved in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.AdjointFamily.GaugeLaw`.

## ii. Key results

> - `GaugeBoson.fieldStrength` : the field strength of a family of gauge-field symbols.
> - `GaugeBoson.covDerivAdjoint`, `GaugeBoson.iteratedCovDerivAdjoint` : the covariant derivative
>   of an adjoint family and its iterates.
> - `GaugeBoson.sum_bracketFam_conv_eq` : the derived bracket against the dual adjoint
>   coefficients, regrouped by the exchange of the four-fold splitting.
> - `GaugeBoson.iteratedCovDerivAdjoint_fieldStrength_map` : the covariant field-strength tower
>   is natural in the algebra.
> - `GaugeBoson.TransformsInAdjoint` : a family transforms in the adjoint.
> - `GaugeBoson.iteratedCovDerivAdjoint_mem_massWeightEigenspace` : the mass weight of an adjoint
>   covariant tower.

## iv. References

> * None.

## A. The field strength

> The field strength is antisymmetric in its two covector indices as soon as the symbols of the
> gauge field commute with one another in `B`.

**`GaugeBoson.fieldStrength`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L102).

> The field strength `F_μν = ∂_μ A_ν − ∂_ν A_μ + ⁅A_μ, A_ν⁆` of a family of
> gauge-field symbols, as a family of derivative symbols. The `s`-th derivative has
> the derivative terms through the shifted symbols `A (μ ::ₘ s) ν`, and the commutator
> term through the Leibniz convolution `commutatorFam`. This is the physicists'
> `F_μν^a = ∂_μ A_ν^a − ∂_ν A_μ^a + f^a_{bc} A_μ^b A_ν^c`. The gauge-algebra bracket
> already carries the physicists' factor of `i`, so no explicit factor appears. This is
> the normalization of the structural equation of the Maurer–Cartan form, which makes the
> field strength transform without inhomogeneous terms
> (`TransformsAsGaugeField.repGauge_fieldStrength`).

```lean
noncomputable def fieldStrength
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

**`GaugeBoson.fieldStrength_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L109).

```lean
lemma fieldStrength_apply
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    fieldStrength A μ ν s φ = A (μ ::ₘ s) ν φ - A (ν ::ₘ s) μ φ + commutatorFam A μ ν s φ
```

**`GaugeBoson.fieldStrength_zero`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L117).

> The underived field strength, derivative symbols on singletons, plus the plain
> commutator.

```lean
lemma fieldStrength_zero
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength A μ ν 0 = A {μ} ν - A {ν} μ + commutator A μ ν
```

**`GaugeBoson.pair_eq_fieldStrength_sub_commutatorFam`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L126).

> The antisymmetrized pair of derivative symbols is the field strength minus its
> commutator term.

```lean
lemma pair_eq_fieldStrength_sub_commutatorFam
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ν μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    A (ν ::ₘ s) μ - A (μ ::ₘ s) ν = fieldStrength A ν μ s - commutatorFam A ν μ s
```

**`GaugeBoson.fieldStrength_swap`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L135).

> The field strength is antisymmetric in its two covector indices when the symbols of
> the gauge field commute. The two derivative terms swap outright, and the commutator term
> swaps by `commutatorFam_swap`.

```lean
lemma fieldStrength_swap
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (hA : ∀ (s s' : Multiset (Fin 1 ⊕ Fin 3)) (μ μ' : Fin 1 ⊕ Fin 3)
      (ψ ψ' : Module.Dual ℝ G.lieSubalgebra), Commute (A s μ ψ) (A s' μ' ψ'))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    fieldStrength A ν μ s = - fieldStrength A μ ν s
```

**`GaugeBoson.fieldStrength_map`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L146).

> The field strength is natural in the algebra. A multiplicative linear map carries the
> field strength of a family to the field strength of its image.

```lean
lemma fieldStrength_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    fieldStrength (fun p ρ => Φ ∘ₗ A p ρ) μ ν s = Φ ∘ₗ fieldStrength A μ ν s
```

## B. The covariant derivative in the adjoint

**`GaugeBoson.bracketFamConv`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L163).

> The derived bracket family `⁅A_ρ, F⁆`, the `s`-derivative of the bracket of the
> gauge field against a family, given by the Leibniz convolution of the derivative
> symbols over the multiset antidiagonal.

```lean
noncomputable def bracketFamConv
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) : Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

**`GaugeBoson.covDerivAdjoint`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L176).

> The covariant derivative `∇_ρ F = [∂_ρ F] + ⁅A_ρ, F⁆` of an adjoint-valued family
> of derivative symbols, the extra derivative on the symbol plus the derived bracket
> against the gauge field. The gauge-algebra bracket carries the physicists' `i`, so
> in matrix terms this is `∂_ρ F + i [A_ρ, F]`, the adjoint-representation covariant
> derivative in the same `D = ∂ + i A` convention as the field strength. It preserves
> `TransformsInAdjoint` (`TransformsInAdjoint.covDerivAdjoint`).

```lean
noncomputable def covDerivAdjoint
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

**`GaugeBoson.covDerivAdjoint_apply`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L184).

```lean
lemma covDerivAdjoint_apply
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    covDerivAdjoint A F ρ s φ = F (ρ ::ₘ s) φ + bracketFamConv A ρ F s φ
```

**`GaugeBoson.covDerivAdjoint_apply_of_map_lie`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L192).

> At a dual vector vanishing on every bracket the derived bracket term drops out and the
> covariant derivative is the ordinary one, `(∇_ρ F)^φ = ∂_ρ F^φ`.

```lean
lemma covDerivAdjoint_apply_of_map_lie {φ : Module.Dual ℝ G.lieSubalgebra}
    (hφ : ∀ x y : G.lieSubalgebra, φ ⁅x, y⁆ = 0)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    covDerivAdjoint A F ρ s φ = F (ρ ::ₘ s) φ
```

**`GaugeBoson.bracketFamConv_map`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L201).

> The derived bracket family is natural in the algebra.

```lean
lemma bracketFamConv_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    bracketFamConv (fun p σ => Φ ∘ₗ A p σ) ρ (fun p => Φ ∘ₗ F p) s =
      Φ ∘ₗ bracketFamConv A ρ F s
```

**`GaugeBoson.covDerivAdjoint_map`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L218).

> The covariant derivative is natural in the algebra.

```lean
lemma covDerivAdjoint_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    covDerivAdjoint (fun p σ => Φ ∘ₗ A p σ) (fun p => Φ ∘ₗ F p) ρ s =
      Φ ∘ₗ covDerivAdjoint A F ρ s
```

**`GaugeBoson.sum_comp_adjointDualCoeff_apply`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L230).

> A sum of families transported by the dual adjoint coefficients of a jet, evaluated at a
> dual vector.

```lean
lemma sum_comp_adjointDualCoeff_apply (U : G.gaugeJetGroup)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (t : Multiset (Fin 1 ⊕ Fin 3)) (ψ : Module.Dual ℝ G.lieSubalgebra) :
    ((t.antidiagonal.map fun r => F r.2 ∘ₗ G.adjointDualCoeff U r.1).sum) ψ =
      (t.antidiagonal.map fun r => F r.2 (G.adjointDualCoeff U r.1 ψ)).sum
```

**`GaugeBoson.sum_bracketFam_conv_eq`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L242).

> The derived bracket against the dual adjoint coefficients, regrouped. Bracketing the
> families `A` and `F` transported by the dual adjoint coefficients of a jet, summed over all
> splittings, gives the antidiagonal convolution of the derived bracket `⁅A_ρ, F⁆` against the
> coefficients. This is the exchange of the four-fold splitting.

```lean
lemma sum_bracketFam_conv_eq (U : G.gaugeJetGroup)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (ρ : Fin 1 ⊕ Fin 3) (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    (s.antidiagonal.map fun p =>
      bracketFam ((p.1.antidiagonal.map fun q => A q.2 ρ ∘ₗ G.adjointDualCoeff U q.1).sum)
        ((p.2.antidiagonal.map fun r => F r.2 ∘ₗ G.adjointDualCoeff U r.1).sum) φ).sum =
      (s.antidiagonal.map fun p => bracketFamConv A ρ F p.2 (G.adjointDualCoeff U p.1 φ)).sum
```

## C. Iterated covariant derivatives

**`GaugeBoson.iteratedCovDerivAdjoint`**, a def, [line 293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L293).

> The iterated covariant derivative `𝒟_l F` of an adjoint family of derivative
> symbols along a list of directions. Covariant derivatives do not commute (their
> commutator is an `ad F` term), so the iteration is order-dependent and indexed by a
> list. The result is again a family of derivative symbols, and the underived covariant
> tower is its value at the empty multiset.

```lean
noncomputable def iteratedCovDerivAdjoint
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    List (Fin 1 ⊕ Fin 3) →
      (Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) →
      Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B
```

**`GaugeBoson.iteratedCovDerivAdjoint_map`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L302).

> The iterated covariant derivative is natural in the algebra.

```lean
lemma iteratedCovDerivAdjoint_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (l : List (Fin 1 ⊕ Fin 3)) (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra
      →ₗ[ℝ] B) :
    iteratedCovDerivAdjoint (fun p σ => Φ ∘ₗ A p σ) l (fun p => Φ ∘ₗ F p) =
      fun p => Φ ∘ₗ iteratedCovDerivAdjoint A l F p
```

**`GaugeBoson.iteratedCovDerivAdjoint_neg_fam`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L319).

> The iterated covariant derivative is odd in the family it differentiates.

```lean
lemma iteratedCovDerivAdjoint_neg_fam
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) :
    ∀ l : List (Fin 1 ⊕ Fin 3),
      iteratedCovDerivAdjoint A l (fun t => - F t) = fun t => - iteratedCovDerivAdjoint A l F t
```

**`GaugeBoson.iteratedCovDerivAdjoint_fieldStrength_map`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L334).

> The covariant tower of the field strength is natural in the algebra. The tower of the
> image family is the image of the tower.

```lean
lemma iteratedCovDerivAdjoint_fieldStrength_map {B' : Type} [Ring B'] [Module ℝ B']
    [SMulCommClass ℝ B' B'] [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B')
    (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (l : List (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ G.lieSubalgebra) :
    iteratedCovDerivAdjoint (fun p σ => Φ ∘ₗ A p σ) l
        (fieldStrength (fun p σ => Φ ∘ₗ A p σ) μ ν) 0 φ
      = Φ (iteratedCovDerivAdjoint A l (fieldStrength A μ ν) 0 φ)
```

**`GaugeBoson.iteratedCovDerivAdjoint_apply_of_map_lie`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L350).

> At a dual vector vanishing on every bracket, such as the coordinate of an abelian factor,
> the iterated covariant derivative is the ordinary derivative along the multiset of its
> directions. No bracket correction survives at any order.

```lean
lemma iteratedCovDerivAdjoint_apply_of_map_lie {φ : Module.Dual ℝ G.lieSubalgebra}
    (hφ : ∀ x y : G.lieSubalgebra, φ ⁅x, y⁆ = 0)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (l : List (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    iteratedCovDerivAdjoint A l F s φ = F (↑l + s) φ
```

**`GaugeBoson.iteratedCovDerivAdjoint_apply_perm_of_map_lie`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L364).

> Hence at such a dual vector the covariant derivatives commute. The iterated covariant
> derivative depends only on the multiset of its directions.

```lean
lemma iteratedCovDerivAdjoint_apply_perm_of_map_lie {φ : Module.Dual ℝ G.lieSubalgebra}
    (hφ : ∀ x y : G.lieSubalgebra, φ ⁅x, y⁆ = 0)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    {l l' : List (Fin 1 ⊕ Fin 3)} (hl : l.Perm l') (s : Multiset (Fin 1 ⊕ Fin 3)) :
    iteratedCovDerivAdjoint A l F s φ = iteratedCovDerivAdjoint A l' F s φ
```

## D. Families transforming in the adjoint

**`GaugeBoson.TransformsInAdjoint`**, a def, [line 391](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L391).

> A family of derivative symbols `F` transforms in the adjoint (is an adjoint gauge
> tensor) for the gauge representation `repGauge` when each symbol `[∂_s F^φ]`
> transforms by the Leibniz convolution of the dual adjoint coefficients against lower
> symbols. This is the shape of `TransformsAsGaugeField` with no Maurer–Cartan shift. At
> `s = 0` it is the homogeneous law `U • F^φ = F^{Ad₀^* φ}`.

```lean
def TransformsInAdjoint (repGauge : Representation ℂ G.gaugeJetGroup B)
    (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B) : Prop
```

**`GaugeBoson.TransformsInAdjoint.repGauge_zero`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L400).

> An adjoint gauge tensor transforms at the base point through the dual adjoint
> coefficient of the value of the gauge jet alone. The antidiagonal of the empty multiset
> has a single term.

```lean
lemma TransformsInAdjoint.repGauge_zero
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    (hF : TransformsInAdjoint G repGauge F) (U : G.gaugeJetGroup)
      (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (F 0 φ) = F 0 (G.adjointDualCoeff U⁻¹ 0 φ)
```

**`GaugeBoson.TransformsInAdjoint.repGauge_cons`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L412).

> If `F` transforms in the adjoint, so do its `κ ::ₘ s`-derived symbols, with the
> extra derivative traced through `GlobalGaugeGroup.adjointDualCoeff_cons`. The result is
> the Leibniz splittings where `κ` stays a derivative, minus the convolution where `κ` hits
> the adjoint, an `ad` of the derived Maurer–Cartan form.

```lean
lemma TransformsInAdjoint.repGauge_cons
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    (hF : TransformsInAdjoint G repGauge F)
    (U : G.gaugeJetGroup) (κ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    repGauge U (F (κ ::ₘ s) φ) =
      (s.antidiagonal.map fun p =>
        F (κ ::ₘ p.2) (G.adjointDualCoeff U⁻¹ p.1 φ)).sum
      - (s.antidiagonal.map fun p =>
          (p.1.antidiagonal.map fun q =>
            F p.2 (G.adjointDualCoeff U⁻¹ q.2
              (φ ∘ₗ LieAlgebra.ad ℝ G.lieSubalgebra (G.evalLie
                (G.iteratedDerivJ q.1
                  (-G.maurerCartan U⁻¹ κ)))))).sum).sum
```

**`GaugeBoson.TransformsInAdjoint.repGauge_eq_of_mem_truncationKer_zero`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L445).

> Anything that transforms in the adjoint is invariant under the pure jets. At `s = 0`
> the transformation law is the dual adjoint action of the base-point value `U₀⁻¹ = 1`.

```lean
lemma TransformsInAdjoint.repGauge_eq_of_mem_truncationKer_zero
    {F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B}
    (hF : TransformsInAdjoint G repGauge F) (U : G.truncationKer 0)
    (φ : Module.Dual ℝ G.lieSubalgebra) : repGauge U.1 (F 0 φ) = F 0 φ
```

## E. Mass weights

**`GaugeBoson.fieldStrength_mem_massWeightEigenspace`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L468).

> The mass weight of the field strength is `4 + 2 * |s|` when each symbol `∂_p A_μ` has
> weight `2 * (1 + |p|)`. Each term is two gauge-field symbols, or one with an extra
> derivative.

```lean
lemma fieldStrength_mem_massWeightEigenspace
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (P : B →ₐ[ℂ] Polynomial B)
    (hA : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ G.lieSubalgebra),
      A p μ ψ ∈ massWeightEigenspace P (2 * (1 + Multiset.card p)))
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℝ G.lieSubalgebra) :
    fieldStrength A μ ν s φ ∈ massWeightEigenspace P (4 + 2 * Multiset.card s)
```

**`GaugeBoson.iteratedCovDerivAdjoint_mem_massWeightEigenspace`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean#L499).

> The mass weight of an adjoint covariant tower. If the gauge-field symbols `∂_p A_μ` have
> weight `2 * (1 + |p|)` and the family `G` has weight `c + 2 * |t|` at the derivative
> multiset `t`, then `𝒟_l G` has weight `c + 2 * |l| + 2 * |s|` at `s`. Each covariant
> derivative costs two units, whether it lands on the derivative index or brings down a
> gauge-field factor.

```lean
lemma iteratedCovDerivAdjoint_mem_massWeightEigenspace
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (P : B →ₐ[ℂ] Polynomial B)
    (hA : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) (ψ : Module.Dual ℝ G.lieSubalgebra),
      A p μ ψ ∈ massWeightEigenspace P (2 * (1 + Multiset.card p)))
    (c : ℕ) (F : Multiset (Fin 1 ⊕ Fin 3) → Module.Dual ℝ G.lieSubalgebra →ₗ[ℝ] B)
    (hF : ∀ (t : Multiset (Fin 1 ⊕ Fin 3)) (χ : Module.Dual ℝ G.lieSubalgebra),
      F t χ ∈ massWeightEigenspace P (c + 2 * Multiset.card t))
    (l : List (Fin 1 ⊕ Fin 3)) (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℝ G.lieSubalgebra) :
    iteratedCovDerivAdjoint A l F s φ ∈
      massWeightEigenspace P (c + 2 * l.length + 2 * Multiset.card s)
```

## Depends on

- [The bracket of adjoint families](gaugeboson-adjointfamily-bracket.md)
- [The truncation filtration of the jet gauge group](../part-02/globalgaugegroup-truncation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/AdjointFamily/CovariantDeriv.lean)
