---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.embed, PhyslibAlpha.Sl2.cgEquiv_symm_sumVec, PhyslibAlpha.Sl2.embed_vNat, PhyslibAlpha.Sl2.embed_normVec, PhyslibAlpha.Sl2.tensorF_embed, PhyslibAlpha.Sl2.tensorE_embed, PhyslibAlpha.Sl2.tensorH_embed, PhyslibAlpha.Sl2.tensorForm_embed
statement: formalized
proof: formalized
---

# The two coupling schemes of three angular momenta

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.CouplingSchemes`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean): 45 declarations, 14 with a docstring.

> The irreducible components of `V(m) ⊗ V(n)` as isometric embeddings, the triple tensor product
> `V(a) ⊗ V(b) ⊗ V(c)` with its Casimir operator, and the two ways of coupling three angular
> momenta.

## i. Overview

> Three angular momenta `j₁ = a/2`, `j₂ = b/2`, `j₃ = c/2` live on
> `V(a) ⊗ V(b) ⊗ V(c)`. A state of total angular momentum `J` and projection `M` can be built in
> two ways:
>
> - `|(j₁ j₂) j₁₂, j₃; J M⟩`: first couple `j₁` and `j₂` to `j₁₂`, then `j₁₂` and `j₃` to `J`;
> - `|j₁, (j₂ j₃) j₂₃; J M⟩`: first couple `j₂` and `j₃` to `j₂₃`, then `j₁` and `j₂₃` to `J`.
>
> Both are built from the Clebsch–Gordan states `coupledVec` of `ClebschGordanCoefficients`. The
> `k`-th irreducible component of `V(m) ⊗ V(n)` is the image of the isometric embedding
> `embed : V(m + n - 2k) → V(m) ⊗ V(n)`, `u_l ↦ |J, J - l⟩`, which intertwines `E`, `F` and `H`
> (it is a rescaled inverse of `cgEquiv`). The first scheme is `embed ⊗ 1` applied to the coupled
> states of `V(a + b - 2k₁) ⊗ V(c)`, the second is `1 ⊗ embed` followed by the associator.
>
> The recoupling coefficients between the two schemes and the 6j symbols are in `SixJ`.

## ii. Key results

> - `embed`, `tensorForm_embed`, `tensorF_embed`: the isometric intertwining embeddings.
> - `Triple`, `tripleForm`, `tripleE`, `tripleF`, `tripleH`: the triple tensor product with its
>   contravariant form and the total `E`, `F`, `H`.
> - `tensorCas`, `tripleCas`: the Casimir operators.
> - `stateA`, `stateB`: the two coupling schemes.

## iv. References

> - A. R. Edmonds, *Angular Momentum in Quantum Mechanics*, Princeton University Press (1957),
>   chapter 6.

## A. The irreducible components as isometric embeddings

**`PhyslibAlpha.Sl2.embed`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L75).

> The isometric embedding `V(m + n - 2k) → V(m) ⊗ V(n)` onto the `k`-th irreducible component,
> `u_l ↦ |J, J - l⟩`.

```lean
def embed : StandardSl2Module ℝ (m + n - 2 * (k : ℕ)) →ₗ[ℝ]
    StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n
```

**`PhyslibAlpha.Sl2.cgEquiv_symm_sumVec`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L80).

```lean
lemma cgEquiv_symm_sumVec (l : ℕ) :
    (cgEquiv (K := ℝ) hmn).symm (DirectSum.lof ℝ _ (CGSummand ℝ m n) k (vNat _ l)) =
      stringVec m n k l
```

**`PhyslibAlpha.Sl2.embed_vNat`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L85).

```lean
lemma embed_vNat (l : ℕ) :
    embed hmn k (vNat _ l) = (Real.sqrt (hwNormSq m n k))⁻¹ • stringVec m n k l
```

**`PhyslibAlpha.Sl2.embed_normVec`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L90).

```lean
lemma embed_normVec (l : ℕ) : embed hmn k (normVec _ l) = coupledVec m n k l
```

**`PhyslibAlpha.Sl2.tensorF_embed`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L94).

```lean
lemma tensorF_embed (x : StandardSl2Module ℝ (m + n - 2 * (k : ℕ))) :
    tensorF m n (embed hmn k x) = embed hmn k (ρF x)
```

**`PhyslibAlpha.Sl2.tensorE_embed`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L101).

```lean
lemma tensorE_embed (x : StandardSl2Module ℝ (m + n - 2 * (k : ℕ))) :
    tensorE m n (embed hmn k x) = embed hmn k (ρE x)
```

**`PhyslibAlpha.Sl2.tensorH_embed`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L108).

```lean
lemma tensorH_embed (x : StandardSl2Module ℝ (m + n - 2 * (k : ℕ))) :
    tensorH m n (embed hmn k x) = embed hmn k (ρH x)
```

**`PhyslibAlpha.Sl2.tensorForm_embed`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L116).

> The embedding is an isometry.

```lean
lemma tensorForm_embed (x y : StandardSl2Module ℝ (m + n - 2 * (k : ℕ))) :
    tensorForm m n (embed hmn k x) (embed hmn k y) = invForm ℝ _ x y
```

**`PhyslibAlpha.Sl2.tensorForm_embed_of_ne`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L146).

> Different components are orthogonal.

```lean
lemma tensorForm_embed_of_ne {k' : Fin (min m n + 1)} (hkk : k ≠ k')
    (x : StandardSl2Module ℝ (m + n - 2 * (k : ℕ)))
    (y : StandardSl2Module ℝ (m + n - 2 * (k' : ℕ))) :
    tensorForm m n (embed hmn k x) (embed hmn k' y) = 0
```

## B. The triple tensor product

**`PhyslibAlpha.Sl2.Triple`**, an abbrev, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L175).

> `V(a) ⊗ V(b) ⊗ V(c)`, bracketed as `(V(a) ⊗ V(b)) ⊗ V(c)`.

```lean
abbrev Triple : Type
```

**`PhyslibAlpha.Sl2.tripleForm`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L179).

> The contravariant form on the triple product.

```lean
def tripleForm : LinearMap.BilinForm ℝ (Triple a b c)
```

**`PhyslibAlpha.Sl2.tripleE`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L183).

> The total raising operator on the triple product.

```lean
def tripleE : Module.End ℝ (Triple a b c)
```

**`PhyslibAlpha.Sl2.tripleF`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L186).

> The total lowering operator on the triple product.

```lean
def tripleF : Module.End ℝ (Triple a b c)
```

**`PhyslibAlpha.Sl2.tripleH`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L189).

> The total weight operator on the triple product.

```lean
def tripleH : Module.End ℝ (Triple a b c)
```

**`PhyslibAlpha.Sl2.tripleForm_tmul`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L193).

```lean
lemma tripleForm_tmul (x x' : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ b)
    (y y' : StandardSl2Module ℝ c) :
    tripleForm a b c (x ⊗ₜ y) (x' ⊗ₜ y') = tensorForm a b x x' * invForm ℝ c y y'
```

**`PhyslibAlpha.Sl2.tripleBilin_ext`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L198).

```lean
lemma tripleBilin_ext {B B' : LinearMap.BilinForm ℝ (Triple a b c)}
    (h : ∀ x y z x' y' z', B ((x ⊗ₜ y) ⊗ₜ z) ((x' ⊗ₜ y') ⊗ₜ z') =
      B' ((x ⊗ₜ y) ⊗ₜ z) ((x' ⊗ₜ y') ⊗ₜ z')) : B = B'
```

**`PhyslibAlpha.Sl2.invForm_ρF_apply`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L204).

```lean
lemma invForm_ρF_apply {n : ℕ} (x y : StandardSl2Module ℝ n) :
    invForm ℝ n (ρF x) y = invForm ℝ n x (ρE y)
```

**`PhyslibAlpha.Sl2.tripleForm_tripleF`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L208).

```lean
lemma tripleForm_tripleF (u v : Triple a b c) :
    tripleForm a b c (tripleF a b c u) v = tripleForm a b c u (tripleE a b c v)
```

**`PhyslibAlpha.Sl2.tripleForm_tripleE`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L217).

```lean
lemma tripleForm_tripleE (u v : Triple a b c) :
    tripleForm a b c (tripleE a b c u) v = tripleForm a b c u (tripleF a b c v)
```

**`PhyslibAlpha.Sl2.tripleForm_tripleH`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L226).

```lean
lemma tripleForm_tripleH (u v : Triple a b c) :
    tripleForm a b c (tripleH a b c u) v = tripleForm a b c u (tripleH a b c v)
```

**`PhyslibAlpha.Sl2.tripleForm_assoc_symm`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L235).

```lean
lemma tripleForm_assoc_symm (x x' : StandardSl2Module ℝ a)
    (w w' : StandardSl2Module ℝ b ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleForm a b c ((TensorProduct.assoc ℝ _ _ _).symm (x ⊗ₜ w))
      ((TensorProduct.assoc ℝ _ _ _).symm (x' ⊗ₜ w')) = invForm ℝ a x x' * tensorForm b c w w'
```

**`PhyslibAlpha.Sl2.tripleF_assoc_symm`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L253).

```lean
lemma tripleF_assoc_symm (x : StandardSl2Module ℝ a)
    (w : StandardSl2Module ℝ b ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleF a b c ((TensorProduct.assoc ℝ _ _ _).symm (x ⊗ₜ w)) =
      (TensorProduct.assoc ℝ _ _ _).symm (ρF x ⊗ₜ w + x ⊗ₜ tensorF b c w)
```

**`PhyslibAlpha.Sl2.tripleE_assoc_symm`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L266).

```lean
lemma tripleE_assoc_symm (x : StandardSl2Module ℝ a)
    (w : StandardSl2Module ℝ b ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleE a b c ((TensorProduct.assoc ℝ _ _ _).symm (x ⊗ₜ w)) =
      (TensorProduct.assoc ℝ _ _ _).symm (ρE x ⊗ₜ w + x ⊗ₜ tensorE b c w)
```

**`PhyslibAlpha.Sl2.tripleH_assoc_symm`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L279).

```lean
lemma tripleH_assoc_symm (x : StandardSl2Module ℝ a)
    (w : StandardSl2Module ℝ b ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleH a b c ((TensorProduct.assoc ℝ _ _ _).symm (x ⊗ₜ w)) =
      (TensorProduct.assoc ℝ _ _ _).symm (ρH x ⊗ₜ w + x ⊗ₜ tensorH b c w)
```

**`PhyslibAlpha.Sl2.tripleForm_comm`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L292).

```lean
lemma tripleForm_comm (u v : Triple a b c) : tripleForm a b c u v = tripleForm a b c v u
```

## C. The Casimir operator

**`PhyslibAlpha.Sl2.tensorCas`**, a def, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L312).

> `2 J² = E F + F E + H²/2` on `V(m) ⊗ V(n)`.

```lean
def tensorCas : Module.End ℝ (StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n)
```

**`PhyslibAlpha.Sl2.tensorCas_stringVec`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L316).

> `2 J² = N(N + 2)/2 = 2 J(J + 1)` on the `k`-th string, `N = m + n - 2k`.

```lean
lemma tensorCas_stringVec {k : ℕ} (hmn : 0 < m + n) (hkm : k ≤ m) (hkn : k ≤ n) (l : ℕ) :
    tensorCas m n (stringVec m n k l) =
      (((m + n - 2 * k : ℕ) : ℝ) * (((m + n - 2 * k : ℕ) : ℝ) + 2) / 2) • stringVec m n k l
```

**`PhyslibAlpha.Sl2.tensorCas_coupledVec`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L329).

```lean
lemma tensorCas_coupledVec {k : ℕ} (hmn : 0 < m + n) (hkm : k ≤ m) (hkn : k ≤ n) (l : ℕ) :
    tensorCas m n (coupledVec m n k l) =
      (((m + n - 2 * k : ℕ) : ℝ) * (((m + n - 2 * k : ℕ) : ℝ) + 2) / 2) • coupledVec m n k l
```

**`PhyslibAlpha.Sl2.tripleCas`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L336).

> `2 J²` on the triple product.

```lean
def tripleCas : Module.End ℝ (Triple a b c)
```

**`PhyslibAlpha.Sl2.tripleForm_tripleCas`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L340).

```lean
lemma tripleForm_tripleCas {a b c : ℕ} (u v : Triple a b c) :
    tripleForm a b c (tripleCas a b c u) v = tripleForm a b c u (tripleCas a b c v)
```

## D. The two coupling schemes

**`PhyslibAlpha.Sl2.stateA`**, a def, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L361).

> `|(j₁ j₂) j₁₂, j₃; J, M⟩`: `j₁ = a/2`, `j₂ = b/2`, `j₃ = c/2`, `j₁₂ = (a + b)/2 - k₁`,
> `J = j₁₂ + j₃ - k₂`, `M = J - l`.

```lean
def stateA (hab : 0 < a + b) (k₁ : Fin (min a b + 1)) (k₂ l : ℕ) : Triple a b c
```

**`PhyslibAlpha.Sl2.assocEmbed`**, a def, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L366).

> `V(a) ⊗ V(b + c - 2k₃) → V(a) ⊗ V(b) ⊗ V(c)`, through the `k₃`-th component of
> `V(b) ⊗ V(c)`.

```lean
def assocEmbed (hbc : 0 < b + c) (k₃ : Fin (min b c + 1)) :
    StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃ : ℕ)) →ₗ[ℝ] Triple a b c
```

**`PhyslibAlpha.Sl2.stateB`**, a def, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L371).

> `|j₁, (j₂ j₃) j₂₃; J, M⟩`: `j₂₃ = (b + c)/2 - k₃`, `J = j₁ + j₂₃ - k₄`, `M = J - l`.

```lean
def stateB (hbc : 0 < b + c) (k₃ : Fin (min b c + 1)) (k₄ l : ℕ) : Triple a b c
```

**`PhyslibAlpha.Sl2.tripleF_rTensor_embed`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L378).

```lean
lemma tripleF_rTensor_embed
    (u : StandardSl2Module ℝ (a + b - 2 * (k₁ : ℕ)) ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleF a b c ((embed hab k₁).rTensor _ u) = (embed hab k₁).rTensor _ (tensorF _ c u)
```

**`PhyslibAlpha.Sl2.tripleE_rTensor_embed`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L388).

```lean
lemma tripleE_rTensor_embed
    (u : StandardSl2Module ℝ (a + b - 2 * (k₁ : ℕ)) ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleE a b c ((embed hab k₁).rTensor _ u) = (embed hab k₁).rTensor _ (tensorE _ c u)
```

**`PhyslibAlpha.Sl2.tripleH_rTensor_embed`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L398).

```lean
lemma tripleH_rTensor_embed
    (u : StandardSl2Module ℝ (a + b - 2 * (k₁ : ℕ)) ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleH a b c ((embed hab k₁).rTensor _ u) = (embed hab k₁).rTensor _ (tensorH _ c u)
```

**`PhyslibAlpha.Sl2.tripleCas_rTensor_embed`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L408).

```lean
lemma tripleCas_rTensor_embed
    (u : StandardSl2Module ℝ (a + b - 2 * (k₁ : ℕ)) ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleCas a b c ((embed hab k₁).rTensor _ u) = (embed hab k₁).rTensor _ (tensorCas _ c u)
```

**`PhyslibAlpha.Sl2.tripleForm_rTensor_embed`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L414).

```lean
lemma tripleForm_rTensor_embed
    (u u' : StandardSl2Module ℝ (a + b - 2 * (k₁ : ℕ)) ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleForm a b c ((embed hab k₁).rTensor _ u) ((embed hab k₁).rTensor _ u') =
      tensorForm _ c u u'
```

**`PhyslibAlpha.Sl2.tripleForm_rTensor_embed_of_ne`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L425).

```lean
lemma tripleForm_rTensor_embed_of_ne {k₁' : Fin (min a b + 1)} (hk : k₁ ≠ k₁')
    (u : StandardSl2Module ℝ (a + b - 2 * (k₁ : ℕ)) ⊗[ℝ] StandardSl2Module ℝ c)
    (u' : StandardSl2Module ℝ (a + b - 2 * (k₁' : ℕ)) ⊗[ℝ] StandardSl2Module ℝ c) :
    tripleForm a b c ((embed hab k₁).rTensor _ u) ((embed hab k₁').rTensor _ u') = 0
```

**`PhyslibAlpha.Sl2.tripleF_assocEmbed`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L442).

```lean
lemma tripleF_assocEmbed
    (w : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃ : ℕ))) :
    tripleF a b c (assocEmbed hbc k₃ w) = assocEmbed hbc k₃ (tensorF a _ w)
```

**`PhyslibAlpha.Sl2.tripleE_assocEmbed`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L453).

```lean
lemma tripleE_assocEmbed
    (w : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃ : ℕ))) :
    tripleE a b c (assocEmbed hbc k₃ w) = assocEmbed hbc k₃ (tensorE a _ w)
```

**`PhyslibAlpha.Sl2.tripleH_assocEmbed`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L464).

```lean
lemma tripleH_assocEmbed
    (w : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃ : ℕ))) :
    tripleH a b c (assocEmbed hbc k₃ w) = assocEmbed hbc k₃ (tensorH a _ w)
```

**`PhyslibAlpha.Sl2.tripleCas_assocEmbed`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L475).

```lean
lemma tripleCas_assocEmbed
    (w : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃ : ℕ))) :
    tripleCas a b c (assocEmbed hbc k₃ w) = assocEmbed hbc k₃ (tensorCas a _ w)
```

**`PhyslibAlpha.Sl2.tripleForm_assocEmbed`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L481).

```lean
lemma tripleForm_assocEmbed
    (w w' : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃ : ℕ))) :
    tripleForm a b c (assocEmbed hbc k₃ w) (assocEmbed hbc k₃ w') = tensorForm a _ w w'
```

**`PhyslibAlpha.Sl2.tripleForm_assocEmbed_of_ne`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean#L492).

```lean
lemma tripleForm_assocEmbed_of_ne {k₃' : Fin (min b c + 1)} (hk : k₃ ≠ k₃')
    (w : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃ : ℕ)))
    (w' : StandardSl2Module ℝ a ⊗[ℝ] StandardSl2Module ℝ (b + c - 2 * (k₃' : ℕ))) :
    tripleForm a b c (assocEmbed hbc k₃ w) (assocEmbed hbc k₃' w') = 0
```

## Depends on

- [Clebsch–Gordan coefficients](clebschgordancoefficients.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/CouplingSchemes.lean)
