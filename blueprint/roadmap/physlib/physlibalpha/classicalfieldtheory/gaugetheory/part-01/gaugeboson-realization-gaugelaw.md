---
declaration: module
origin: cited
lean: GaugeAlgebraRealization.dualPairEquiv, GaugeAlgebraRealization.tensorBracket, GaugeAlgebraRealization.commutator, GaugeAlgebraRealization.repGauge_apply, GaugeAlgebraRealization.repGauge_deriv_apply, GaugeAlgebraRealization.dualPairEquiv_tmul, GaugeAlgebraRealization.tensorBracket_tmul, GaugeAlgebraRealization.dualPairEquiv_map_left
statement: formalized
proof: formalized
---

# The gauge law on brackets and iterated derivatives

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeBoson.Realization.GaugeLaw`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean): 47 declarations, 24 with a docstring.

## i. Overview

> The gauge law of a realization, `GaugeAlgebraRealization.gauge_apply_deriv`, gives the
> action of a jet `U` on a single derivative symbol `∂_s A_μ^φ`. This file works out what it
> does to the expressions built from the symbols: their brackets, the commutator families
> `[A_μ, A_ν]` and the derivatives of those. The tools are the tensor-level bookkeeping
> `dualPairEquiv` and `tensorBracket`, which let the adjoint index be contracted with a
> bracket of the gauge algebra, and the bracket of component families `bracketFam`, whose
> gauge transformation `repGauge_bracketFam` is the convolution of the transformations of the
> factors against the adjoint Taylor coefficients.
>
> Everything here is stated for a realization `h`; the definitions on families of symbols
> (`bracketFam`, `commutatorFam`) take an arbitrary family, so that they also apply to the
> covariant families built later.
>
>
> - `GaugeAlgebraRealization.dualPairEquiv`, `GaugeAlgebraRealization.tensorBracket` : the
>   tensor bookkeeping of the adjoint index.
> - `GaugeAlgebraRealization.bracketFam`, `GaugeAlgebraRealization.commutatorFam` : the
>   bracket of two component families, and the derived commutators `∂_s [A_μ, A_ν]`.
> - `GaugeAlgebraRealization.repGauge_bracketFam` : the gauge transformation of a bracket.
> - `GaugeAlgebraRealization.repGauge_commutatorFam` : the gauge transformation of the derived
>   commutators.

## ii. Key results

> - `dualPairEquiv` : the canonical equivalence, through finite-dimensional duality, between
>   algebra-valued fields `B ⊗ 𝔤` and their component families `φ ↦ A^φ`: the element `b ⊗ a`
>   corresponds to the family `φ ↦ φ(a) b`
> - `tensorBracket`
> - `bracketFam` : the bracket of two arbitrary component families, generalizing `commutator` (which
>   is the case of two field symbols): assemble into `B ⊗ 𝔤` by `dualPairEquiv.symm`, bracket by
>   `tensorBracket`, read back out as components
> - `commutatorFam` : the derived commutator family: the `s`-derivative of the commutator term, given
>   by the Leibniz convolution of the derivative symbols over the multiset antidiagonal
> - `repGauge_bracketFam` : the gauge transformation of the bracket of two component families with
>   affine transformation laws `f ↦ f' + φ(c_f)·1` and `g ↦ g' + φ(c_g)·1`: the bracket of the
>   transformed families, two `ad` cross terms, and the constant bracket `⁅c_f, c_g⁆`

## iv. References

> * None.

**`GaugeAlgebraRealization.dualPairEquiv`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L92).

> The canonical equivalence, through finite-dimensional duality, between
> algebra-valued fields `B ⊗ 𝔤` and their component families `φ ↦ A^φ`: the element
> `b ⊗ a` corresponds to the family `φ ↦ φ(a) b`.

```lean
noncomputable def dualPairEquiv :
    (B ⊗[ℝ] 𝔤) ≃ₗ[ℝ] (Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
```

**`GaugeAlgebraRealization.tensorBracket`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L101).

> The bracket of two algebra-valued fields: multiplication in `B` on the first
> factors, the Lie bracket of the gauge algebra on the second, so that on pure
> tensors `⁅b₁ ⊗ a₁, b₂ ⊗ a₂⁆ = (b₁ b₂) ⊗ ⁅a₁, a₂⁆`.

```lean
noncomputable def tensorBracket :
    (B ⊗[ℝ] 𝔤) →ₗ[ℝ] (B ⊗[ℝ] 𝔤) →ₗ[ℝ] B ⊗[ℝ] 𝔤
```

**`GaugeAlgebraRealization.commutator`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L114).

> The commutator term `⁅A_μ, A_ν⁆` of the field strength, as a component family:
> the physicists' `f^a_{bc} A_μ^b A_ν^c` contracted with a dual adjoint vector, but
> basis-free — the two fields are assembled into `B ⊗ 𝔤` by `dualPairEquiv.symm`,
> bracketed there by `tensorBracket`, and read back out as components.

```lean
noncomputable def commutator
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) : Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`GaugeAlgebraRealization.repGauge_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L132).

> The gauge transformation of the underived symbol `A_μ^φ`: the special case `s = 0`
> of `gauge_apply_deriv`, with no Leibniz convolution left over — the dual adjoint
> action of the value of `U⁻¹` plus the Maurer–Cartan shift.

```lean
lemma repGauge_apply (U : GJ)
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repGauge U (h.A 0 μ φ) = h.A 0 μ (jets.adjointDualCoeff U⁻¹ ∅ φ) +
      algebraMap ℂ B (φ (jets.evalLie (jets.maurerCartan U⁻¹ μ)))
```

**`GaugeAlgebraRealization.repGauge_deriv_apply`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L144).

> The gauge transformation of the once-derived symbol `∂_ρ A_σ`: the case `s = {ρ}`
> of `gauge_apply_deriv` — the two Leibniz splittings of one derivative, plus the
> base-point value of the derived Maurer–Cartan form.

```lean
lemma repGauge_deriv_apply
    (U : GJ) (ρ σ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repGauge U (h.A {ρ} σ φ) =
      h.A {ρ} σ (jets.adjointDualCoeff U⁻¹ 0 φ) + h.A 0 σ (jets.adjointDualCoeff U⁻¹ {ρ} φ) +
      algebraMap ℂ B (φ (jets.evalLie
        (jets.deriv ρ (jets.maurerCartan U⁻¹ σ))))
```

## A. Pure-tensor computations for `dualPairEquiv` and `tensorBracket`

**`GaugeAlgebraRealization.dualPairEquiv_tmul`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L178).

```lean
lemma dualPairEquiv_tmul (b : B) (a : 𝔤) (φ : Module.Dual ℝ 𝔤) :
    dualPairEquiv (b ⊗ₜ[ℝ] a) φ = φ a • b
```

**`GaugeAlgebraRealization.tensorBracket_tmul`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L184).

```lean
lemma tensorBracket_tmul (b₁ b₂ : B) (a₁ a₂ : 𝔤) :
    tensorBracket (b₁ ⊗ₜ[ℝ] a₁) (b₂ ⊗ₜ[ℝ] a₂) = (b₁ * b₂) ⊗ₜ[ℝ] ⁅a₁, a₂⁆
```

**`GaugeAlgebraRealization.dualPairEquiv_map_left`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L189).

```lean
lemma dualPairEquiv_map_left (Φ : B →ₗ[ℝ] B) (t : B ⊗[ℝ] 𝔤)
    (φ : Module.Dual ℝ 𝔤) :
    dualPairEquiv ((TensorProduct.map Φ LinearMap.id) t) φ = Φ (dualPairEquiv t φ)
```

**`GaugeAlgebraRealization.dualPairEquiv_map_right`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L197).

```lean
lemma dualPairEquiv_map_right (T : 𝔤 →ₗ[ℝ] 𝔤)
    (t : B ⊗[ℝ] 𝔤) (φ : Module.Dual ℝ 𝔤) :
    dualPairEquiv ((TensorProduct.map LinearMap.id T) t) φ =
      dualPairEquiv t (T.dualMap φ)
```

**`GaugeAlgebraRealization.symm_comp_left`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L206).

```lean
lemma symm_comp_left (Φ : B →ₗ[ℝ] B) (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    dualPairEquiv.symm (Φ ∘ₗ f) =
      (TensorProduct.map Φ LinearMap.id) (dualPairEquiv.symm f)
```

**`GaugeAlgebraRealization.symm_comp_right`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L216).

```lean
lemma symm_comp_right (T : 𝔤 →ₗ[ℝ] 𝔤)
    (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    dualPairEquiv.symm (f ∘ₗ T.dualMap) =
      (TensorProduct.map LinearMap.id T) (dualPairEquiv.symm f)
```

**`GaugeAlgebraRealization.tensorBracket_map_left`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L227).

```lean
lemma tensorBracket_map_left (Φ : B →ₗ[ℝ] B)
    (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂) (s t : B ⊗[ℝ] 𝔤) :
    tensorBracket ((TensorProduct.map Φ LinearMap.id) s)
        ((TensorProduct.map Φ LinearMap.id) t) =
      (TensorProduct.map Φ LinearMap.id) (tensorBracket s t)
```

**`GaugeAlgebraRealization.tensorBracket_map_right`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L242).

```lean
lemma tensorBracket_map_right (T : 𝔤 →ₗ[ℝ] 𝔤)
    (hT : ∀ a b, T ⁅a, b⁆ = ⁅T a, T b⁆) (s t : B ⊗[ℝ] 𝔤) :
    tensorBracket ((TensorProduct.map LinearMap.id T) s)
        ((TensorProduct.map LinearMap.id T) t) =
      (TensorProduct.map LinearMap.id T) (tensorBracket s t)
```

**`GaugeAlgebraRealization.tensorBracket_one_right`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L257).

```lean
lemma tensorBracket_one_right (c : 𝔤) (s : B ⊗[ℝ] 𝔤) :
    tensorBracket s ((1 : B) ⊗ₜ[ℝ] c) =
      -(TensorProduct.map LinearMap.id (LieAlgebra.ad ℝ 𝔤 c)) s
```

**`GaugeAlgebraRealization.tensorBracket_one_left`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L270).

```lean
lemma tensorBracket_one_left (c : 𝔤) (t : B ⊗[ℝ] 𝔤) :
    tensorBracket ((1 : B) ⊗ₜ[ℝ] c) t =
      (TensorProduct.map LinearMap.id (LieAlgebra.ad ℝ 𝔤 c)) t
```

## B. The gauge transformation of the commutator

**`GaugeAlgebraRealization.dualPairEquiv_one_tmul`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L292).

```lean
lemma dualPairEquiv_one_tmul (c : 𝔤) (φ : Module.Dual ℝ 𝔤) :
    dualPairEquiv ((1 : B) ⊗ₜ[ℝ] c) φ = algebraMap ℂ B (φ c)
```

**`GaugeAlgebraRealization.repGauge_commutator`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L310).

> The gauge transformation law of the commutator term: writing the field law as
> `A_μ ↦ Ad₀ A_μ + c_μ` with `Ad₀` the base-point adjoint of `U₀⁻¹` and
> `c_μ = maurerCartan(U⁻¹)_μ|₀` the constant Maurer–Cartan shift, bilinearity of the bracket
> gives
>
> `⁅A_μ, A_ν⁆ ↦ Ad₀ ⁅A_μ, A_ν⁆ + ⁅Ad₀ A_μ, c_ν⁆ + ⁅c_μ, Ad₀ A_ν⁆ + ⁅c_μ, c_ν⁆`:
>
> the adjoint-transported commutator, two cross terms linear in the field (the
> bracket against `c` acting on the dual index through `ad`), and the constant
> commutator of the two Maurer–Cartan shifts. Uses that the gauge action is by
> algebra homomorphisms (`GaugeAlgebraRealization.repJet_mul`) and that the base-point adjoint
> transport is a morphism of Lie algebras.

```lean
lemma repGauge_commutator
    (U : GJ) (μ ν : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repGauge U (commutator h.A μ ν φ) =
      commutator h.A μ ν (jets.adjointDualCoeff U⁻¹ 0 φ)
      - h.A 0 μ (jets.adjointDualCoeff U⁻¹ 0 (φ ∘ₗ LieAlgebra.ad ℝ 𝔤
          (jets.evalLie (jets.maurerCartan U⁻¹ ν))))
      + h.A 0 ν (jets.adjointDualCoeff U⁻¹ 0 (φ ∘ₗ LieAlgebra.ad ℝ 𝔤
          (jets.evalLie (jets.maurerCartan U⁻¹ μ))))
      + algebraMap ℂ B (φ ⁅jets.evalLie (jets.maurerCartan U⁻¹ μ),
          jets.evalLie (jets.maurerCartan U⁻¹ ν)⁆)
```

## C. Second derivatives of the gauge field

**`GaugeAlgebraRealization.repGauge_deriv_deriv_apply`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L399).

> The gauge transformation of the twice-derived symbol `∂_ρ ∂_σ A_τ`: the case
> `s = ρ ::ₘ {σ}` of `gauge_apply_deriv` — the four Leibniz splittings of two
> derivatives, plus the base-point value of the twice-derived Maurer–Cartan form.

```lean
lemma repGauge_deriv_deriv_apply
    (U : GJ) (ρ σ τ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repGauge U (h.A (ρ ::ₘ {σ}) τ φ) =
      h.A (ρ ::ₘ {σ}) τ (jets.adjointDualCoeff U⁻¹ 0 φ)
      + h.A {ρ} τ (jets.adjointDualCoeff U⁻¹ {σ} φ)
      + h.A {σ} τ (jets.adjointDualCoeff U⁻¹ {ρ} φ)
      + h.A 0 τ (jets.adjointDualCoeff U⁻¹ (ρ ::ₘ {σ}) φ)
      + algebraMap ℂ B (φ (jets.evalLie (jets.deriv ρ
          (jets.deriv σ (jets.maurerCartan U⁻¹ τ)))))
```

## D. The bracket of general component families

**`GaugeAlgebraRealization.bracketFam`**, a def, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L444).

> The bracket of two arbitrary component families, generalizing `commutator` (which
> is the case of two field symbols): assemble into `B ⊗ 𝔤` by `dualPairEquiv.symm`,
> bracket by `tensorBracket`, read back out as components.

```lean
noncomputable def bracketFam (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`GaugeAlgebraRealization.commutator_eq_bracketFam`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L448).

```lean
lemma commutator_eq_bracketFam
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) : commutator A μ ν = bracketFam (A 0 μ) (A 0 ν)
```

**`GaugeAlgebraRealization.commutatorFam`**, a def, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L456).

> **The derived commutator family**: the `s`-derivative of the commutator term, given
> by the Leibniz convolution of the derivative symbols over the multiset antidiagonal.
> With the derivative symbols as primitives this convolution is the definition; for
> `s = 0` it is the commutator itself (`commutatorFam_zero`).

```lean
noncomputable def commutatorFam
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    Module.Dual ℝ 𝔤 →ₗ[ℝ] B
```

**`GaugeAlgebraRealization.commutatorFam_zero`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L462).

```lean
lemma commutatorFam_zero
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) : commutatorFam A μ ν 0 = commutator A μ ν
```

**`GaugeAlgebraRealization.bracketFam_add_left`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L468).

```lean
lemma bracketFam_add_left (f₁ f₂ g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam (f₁ + f₂) g = bracketFam f₁ g + bracketFam f₂ g
```

**`GaugeAlgebraRealization.bracketFam_add_right`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L472).

```lean
lemma bracketFam_add_right (f g₁ g₂ : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam f (g₁ + g₂) = bracketFam f g₁ + bracketFam f g₂
```

**`GaugeAlgebraRealization.bracketFam_smul_left`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L476).

```lean
lemma bracketFam_smul_left (c : ℝ) (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam (c • f) g = c • bracketFam f g
```

**`GaugeAlgebraRealization.bracketFam_smul_right`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L480).

```lean
lemma bracketFam_smul_right (c : ℝ) (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam f (c • g) = c • bracketFam f g
```

**`GaugeAlgebraRealization.bracketFam_apply_eq_sum`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L487).

> The bracket of two component families expanded through a basis of the gauge
> algebra: the physicists' `f^a_{bc} f^b g^c`, with `φ⁅e_j, e_k⁆` the structure
> constants contracted with the dual vector.

```lean
lemma bracketFam_apply_eq_sum (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (φ : Module.Dual ℝ 𝔤) :
    bracketFam f g φ = ∑ j, ∑ k,
      φ ⁅Module.Free.chooseBasis ℝ 𝔤 j,
          Module.Free.chooseBasis ℝ 𝔤 k⁆ •
        (f ((Module.Free.chooseBasis ℝ 𝔤).coord j) *
          g ((Module.Free.chooseBasis ℝ 𝔤).coord k))
```

**`GaugeAlgebraRealization.bracketFam_apply_eq_zero_of_map_lie`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L521).

> A dual vector vanishing on every bracket of the gauge algebra, such as the coordinate of an
> abelian factor, vanishes on the bracket of any two families: every structure constant
> `φ⁅e_j, e_k⁆` it sees is zero.

```lean
lemma bracketFam_apply_eq_zero_of_map_lie {φ : Module.Dual ℝ 𝔤}
    (hφ : ∀ x y : 𝔤, φ ⁅x, y⁆ = 0) (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam f g φ = 0
```

**`GaugeAlgebraRealization.bracketFam_map`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L528).

> The bracket of families is natural in the algebra: a multiplicative linear map carries
> the bracket of two families to the bracket of their images.

```lean
lemma bracketFam_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam (Φ ∘ₗ f) (Φ ∘ₗ g) = Φ ∘ₗ bracketFam f g
```

**`GaugeAlgebraRealization.commutatorFam_map`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L541).

> The derived commutator family is natural in the algebra.

```lean
lemma commutatorFam_map {B' : Type} [Ring B'] [Module ℝ B'] [SMulCommClass ℝ B' B']
    [IsScalarTower ℝ B' B'] (Φ : B →ₗ[ℝ] B') (hΦ : ∀ b₁ b₂, Φ (b₁ * b₂) = Φ b₁ * Φ b₂)
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (μ ν : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    commutatorFam (fun p ρ => Φ ∘ₗ A p ρ) μ ν s = Φ ∘ₗ commutatorFam A μ ν s
```

**`GaugeAlgebraRealization.bracketFam_comp_dualMap`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L556).

> The bracket of families against a common Lie-algebra morphism on the dual index.

```lean
lemma bracketFam_comp_dualMap (T : 𝔤 →ₗ[ℝ] 𝔤)
    (hT : ∀ a b, T ⁅a, b⁆ = ⁅T a, T b⁆) (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam (f ∘ₗ T.dualMap) (g ∘ₗ T.dualMap) = bracketFam f g ∘ₗ T.dualMap
```

**`GaugeAlgebraRealization.tensorBracket_map_left_derivation`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L570).

> `tensorBracket` is a derivation in the algebra factor: for `Δ` satisfying the
> Leibniz rule on `B`, applying `Δ ⊗ id` to a bracket distributes over the two
> arguments.

```lean
lemma tensorBracket_map_left_derivation (Δ : B →ₗ[ℝ] B)
    (hΔ : ∀ b₁ b₂, Δ (b₁ * b₂) = Δ b₁ * b₂ + b₁ * Δ b₂) (s t : B ⊗[ℝ] 𝔤) :
    (TensorProduct.map Δ LinearMap.id) (tensorBracket s t) =
      tensorBracket ((TensorProduct.map Δ LinearMap.id) s) t +
      tensorBracket s ((TensorProduct.map Δ LinearMap.id) t)
```

**`GaugeAlgebraRealization.bracketFam_derivation`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L588).

> The bracket of families under a derivation of the algebra: the Leibniz rule, in
> family form.

```lean
lemma bracketFam_derivation (Δ : B →ₗ[ℝ] B)
    (hΔ : ∀ b₁ b₂, Δ (b₁ * b₂) = Δ b₁ * b₂ + b₁ * Δ b₂) (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    Δ ∘ₗ bracketFam f g = bracketFam (Δ ∘ₗ f) g + bracketFam f (Δ ∘ₗ g)
```

**`GaugeAlgebraRealization.tensorBracket_map_right_derivation`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L602).

> `tensorBracket` under a relative derivation on the Lie factor: if
> `T₁ ⁅a, b⁆ = ⁅T₁ a, T₀ b⁆ + ⁅T₀ a, T₁ b⁆`, the two mixed brackets sum to the
> `T₁`-image of the bracket. This is how the once-derived adjoint transport
> distributes over the commutator.

```lean
lemma tensorBracket_map_right_derivation (T₀ T₁ : 𝔤 →ₗ[ℝ] 𝔤)
    (hT : ∀ a b, T₁ ⁅a, b⁆ = ⁅T₁ a, T₀ b⁆ + ⁅T₀ a, T₁ b⁆) (s t : B ⊗[ℝ] 𝔤) :
    tensorBracket ((TensorProduct.map LinearMap.id T₁) s)
        ((TensorProduct.map LinearMap.id T₀) t) +
      tensorBracket ((TensorProduct.map LinearMap.id T₀) s)
        ((TensorProduct.map LinearMap.id T₁) t) =
      (TensorProduct.map LinearMap.id T₁) (tensorBracket s t)
```

**`GaugeAlgebraRealization.bracketFam_dualMap_derivation`**, a lemma, [line 624](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L624).

> The family-level form of `tensorBracket_map_right_derivation`: a relative
> derivation on the dual index distributes over the bracket of families.

```lean
lemma bracketFam_dualMap_derivation (T₀ T₁ : 𝔤 →ₗ[ℝ] 𝔤)
    (hT : ∀ a b, T₁ ⁅a, b⁆ = ⁅T₁ a, T₀ b⁆ + ⁅T₀ a, T₁ b⁆)
    (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam (f ∘ₗ T₁.dualMap) (g ∘ₗ T₀.dualMap) +
      bracketFam (f ∘ₗ T₀.dualMap) (g ∘ₗ T₁.dualMap) =
      bracketFam f g ∘ₗ T₁.dualMap
```

**`GaugeAlgebraRealization.repGauge_bracketFam`**, a lemma, [line 657](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L657).

> The gauge transformation of the bracket of two component families with affine
> transformation laws `f ↦ f' + φ(c_f)·1` and `g ↦ g' + φ(c_g)·1`: the bracket of the
> transformed families, two `ad` cross terms, and the constant bracket `⁅c_f, c_g⁆`.
> Pure bilinearity, with `tensorBracket_one_left/right` computing the cross terms;
> `repGauge_commutator` is the special case of two field symbols.

```lean
lemma repGauge_bracketFam
    (U : GJ) {f g f' g' : Module.Dual ℝ 𝔤 →ₗ[ℝ] B}
    {cf cg : 𝔤}
    (hf : ∀ ψ : Module.Dual ℝ 𝔤,
      repGauge U (f ψ) = f' ψ + algebraMap ℂ B (ψ cf))
    (hg : ∀ ψ : Module.Dual ℝ 𝔤,
      repGauge U (g ψ) = g' ψ + algebraMap ℂ B (ψ cg))
    (φ : Module.Dual ℝ 𝔤) :
    repGauge U (bracketFam f g φ) =
      bracketFam f' g' φ
      + g' (φ ∘ₗ LieAlgebra.ad ℝ 𝔤 cf)
      - f' (φ ∘ₗ LieAlgebra.ad ℝ 𝔤 cg)
      + algebraMap ℂ B (φ ⁅cf, cg⁆)
```

## E. Multiset combinatorics for iterated Leibniz sums

> The convolution sums of the iterated transformation laws are indexed by the multiset
> antidiagonal. The two lemmas below are the coassociativity and cocommutativity-exchange
> of this "comultiplication": a sum over splittings-of-splittings does not depend on the
> grouping. Both are proven by a cons-induction with the summand universally quantified,
> so that the inductive hypothesis absorbs the modified summands.

**`GaugeAlgebraRealization.commutatorFam_mem`**, a lemma, [line 736](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L736).

> Every derived commutator term is a polynomial in derivative symbols of order at
> most that of the derivative: each Leibniz splitting contributes a product of two
> lower-order symbols.

```lean
lemma commutatorFam_mem
    (A : Multiset (Fin 1 ⊕ Fin 3) → (Fin 1 ⊕ Fin 3) → Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (s' : Multiset (Fin 1 ⊕ Fin 3)) (ν lam : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    commutatorFam A ν lam s' φ ∈
      Algebra.adjoin ℂ {b : B | ∃ (p : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
        (φ : Module.Dual ℝ 𝔤), p.card ≤ s'.card ∧ b = A p μ φ}
```

## F. Iterated Leibniz expansions

**`GaugeAlgebraRealization.bracketFam_zero_left`**, a lemma, [line 771](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L771).

```lean
lemma bracketFam_zero_left (g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam 0 g = 0
```

**`GaugeAlgebraRealization.bracketFam_zero_right`**, a lemma, [line 775](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L775).

```lean
lemma bracketFam_zero_right (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam f 0 = 0
```

**`GaugeAlgebraRealization.bracketFam_sum_left`**, a lemma, [line 779](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L779).

```lean
lemma bracketFam_sum_left (S : Multiset (Module.Dual ℝ 𝔤 →ₗ[ℝ] B))
    (g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam S.sum g = (S.map fun f => bracketFam f g).sum
```

**`GaugeAlgebraRealization.bracketFam_sum_right`**, a lemma, [line 786](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L786).

```lean
lemma bracketFam_sum_right (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B)
    (S : Multiset (Module.Dual ℝ 𝔤 →ₗ[ℝ] B)) :
    bracketFam f S.sum = (S.map fun g => bracketFam f g).sum
```

**`GaugeAlgebraRealization.bracketFam_finset_sum_left`**, a lemma, [line 793](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L793).

```lean
lemma bracketFam_finset_sum_left {ι : Type*} (S : Finset ι)
    (f : ι → Module.Dual ℝ 𝔤 →ₗ[ℝ] B) (g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam (∑ i ∈ S, f i) g = ∑ i ∈ S, bracketFam (f i) g
```

**`GaugeAlgebraRealization.bracketFam_finset_sum_right`**, a lemma, [line 798](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L798).

```lean
lemma bracketFam_finset_sum_right {ι : Type*} (S : Finset ι)
    (f : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) (g : ι → Module.Dual ℝ 𝔤 →ₗ[ℝ] B) :
    bracketFam f (∑ i ∈ S, g i) = ∑ i ∈ S, bracketFam f (g i)
```

## G. The bracket of families against the adjoint coefficients

**`GaugeAlgebraRealization.tensorBracket_map_right_antidiagonal`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L813).

> `tensorBracket` under an antidiagonal family of transports on the Lie factor:
> if `T x` distributes over the bracket as the antidiagonal convolution of the
> `T m`, so does `id ⊗ T x` over `tensorBracket`.

```lean
lemma tensorBracket_map_right_antidiagonal
    (T : Multiset (Fin 1 ⊕ Fin 3) → 𝔤 →ₗ[ℝ] 𝔤)
    (x : Multiset (Fin 1 ⊕ Fin 3))
    (hT : ∀ a b : 𝔤, T x ⁅a, b⁆ =
      (x.antidiagonal.map fun p => ⁅T p.1 a, T p.2 b⁆).sum)
    (s t : B ⊗[ℝ] 𝔤) :
    (x.antidiagonal.map fun p =>
      tensorBracket ((TensorProduct.map LinearMap.id (T p.1)) s)
        ((TensorProduct.map LinearMap.id (T p.2)) t)).sum =
      (TensorProduct.map LinearMap.id (T x)) (tensorBracket s t)
```

**`GaugeAlgebraRealization.bracketFam_adjointDualCoeff`**, a lemma, [line 842](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L842).

> The bracket of families against an iterated dual adjoint coefficient: the
> antidiagonal convolution — the all-orders form of `bracketFam_comp_dualMap` and
> `bracketFam_dualMap_derivation`.

```lean
lemma bracketFam_adjointDualCoeff (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3))
    (f g : Module.Dual ℝ 𝔤 →ₗ[ℝ] B) (φ : Module.Dual ℝ 𝔤) :
    bracketFam f g (jets.adjointDualCoeff U x φ) =
      (x.antidiagonal.map fun p =>
        bracketFam (f ∘ₗ jets.adjointDualCoeff U p.1)
          (g ∘ₗ jets.adjointDualCoeff U p.2) φ).sum
```

## H. The gauge transformation of iterated derivatives

**`GaugeAlgebraRealization.repGauge_cons_apply`**, a lemma, [line 882](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L882).

> The `κ ::ₘ s` case of `gauge_apply_deriv` with the extra derivative traced through:
> the Leibniz splittings where `κ` stays a derivative, minus (by
> `LocalGaugeData.adjointDualCoeff_cons`) the splittings where `κ` hits the adjoint — an `ad` of the
> derived Maurer–Cartan form — plus the derived Maurer–Cartan shift.

```lean
lemma repGauge_cons_apply
    (U : GJ) (κ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (τ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℝ 𝔤) :
    repGauge U (h.A (κ ::ₘ s) τ φ) =
      (s.antidiagonal.map fun p =>
        h.A (κ ::ₘ p.2) τ (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
      - (s.antidiagonal.map fun p =>
          (p.1.antidiagonal.map fun q =>
            h.A p.2 τ (jets.adjointDualCoeff U⁻¹ q.2
              (φ ∘ₗ LieAlgebra.ad ℝ 𝔤 (jets.evalLie
                (jets.iteratedDeriv q.1 (jets.maurerCartan U⁻¹ κ)))))).sum).sum
      + algebraMap ℂ B (φ (jets.evalLie (jets.iteratedDeriv (κ ::ₘ s)
          (jets.maurerCartan U⁻¹ τ))))
```

**`GaugeAlgebraRealization.repGauge_commutatorFam`**, a lemma, [line 918](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean#L918).

> The all-orders gauge transformation of the derived commutator term: the Leibniz
> convolution of the transformed commutator, the two `ad` cross-term convolutions,
> and the convolution of Maurer–Cartan bracket shifts. This is `repGauge_commutator`
> at every derivative order simultaneously; the regrouping of the four-fold splitting
> is `Multiset.sum_antidiagonal_exchange`.

```lean
lemma repGauge_commutatorFam
    (U : GJ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3)
    (φ : Module.Dual ℝ 𝔤) :
    repGauge U (commutatorFam h.A μ ν s φ) =
      (s.antidiagonal.map fun p =>
        commutatorFam h.A μ ν p.2 (jets.adjointDualCoeff U⁻¹ p.1 φ)).sum
      + (s.antidiagonal.map fun p =>
          (p.2.antidiagonal.map fun r =>
            h.A r.2 ν (jets.adjointDualCoeff U⁻¹ r.1
              (φ ∘ₗ LieAlgebra.ad ℝ 𝔤 (jets.evalLie
                (jets.iteratedDeriv p.1 (jets.maurerCartan U⁻¹ μ)))))).sum).sum
      - (s.antidiagonal.map fun p =>
          (p.1.antidiagonal.map fun q =>
            h.A q.2 μ (jets.adjointDualCoeff U⁻¹ q.1
              (φ ∘ₗ LieAlgebra.ad ℝ 𝔤 (jets.evalLie
                (jets.iteratedDeriv p.2 (jets.maurerCartan U⁻¹ ν)))))).sum).sum
      + (s.antidiagonal.map fun p =>
          algebraMap ℂ B (φ ⁅jets.evalLie (jets.iteratedDeriv p.1
              (jets.maurerCartan U⁻¹ μ)),
            jets.evalLie (jets.iteratedDeriv p.2
              (jets.maurerCartan U⁻¹ ν))⁆)).sum
```

## Depends on

- [Realizations of the gauge-boson jet algebra](gaugeboson-realization-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeBoson/Realization/GaugeLaw.lean)
