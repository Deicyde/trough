---
catalog: module
lean: AdditiveNTT.fintype_card_gt_one_of_field, AdditiveNTT.U, AdditiveNTT.finrank_U, AdditiveNTT.fintype_U, AdditiveNTT.U_card, AdditiveNTT.U_i_is_union_of_cosets, AdditiveNTT.βᵢ_not_in_Uᵢ, AdditiveNTT.root_U_lift_down, AdditiveNTT.root_U_lift_up, AdditiveNTT.W, AdditiveNTT.degree_W, AdditiveNTT.W_monic, AdditiveNTT.W_ne_zero, AdditiveNTT.Wᵢ_eval_βᵢ_neq_zero, AdditiveNTT.Wᵢ_vanishing, AdditiveNTT.W₀_eq_X, AdditiveNTT.W_splits, AdditiveNTT.roots_W, AdditiveNTT.algEquivAevalXSubC, AdditiveNTT.comp_X_sub_C_eq_zero_iff, AdditiveNTT.rootMultiplicity_comp_X_sub_C, AdditiveNTT.roots_comp_X_sub_C, AdditiveNTT.Prod_W_comp_X_sub_C_ne_zero, AdditiveNTT.rootMultiplicity_W, AdditiveNTT.eval_W_eq_zero_iff_in_U, AdditiveNTT.rootMultiplicity_prod_W_comp_X_sub_C, AdditiveNTT.W_prod_comp_decomposition, AdditiveNTT.comp_sub_C_of_linear_eval, AdditiveNTT.inductive_rec_form_W_comp, AdditiveNTT.inductive_linear_map_W, AdditiveNTT.W_linearity, AdditiveNTT.polyEvalLinearMap, AdditiveNTT.W_linear_comp_decomposition, AdditiveNTT.W_is_additive, AdditiveNTT.kernel_W_eq_U, AdditiveNTT.W_add_U_invariant, AdditiveNTT.normalizedW, AdditiveNTT.normalizedWᵢ_eval_βᵢ_eq_1, AdditiveNTT.normalizedW₀_eq_1_div_β₀, AdditiveNTT.eval_normalizedW_succ_at_beta_prev, AdditiveNTT.degree_normalizedW, AdditiveNTT.β_lt_mem_U, AdditiveNTT.normalizedWᵢ_vanishing, AdditiveNTT.normalizedW_is_linear_map, AdditiveNTT.normalizedW_is_additive, AdditiveNTT.kernel_normalizedW_eq_U, AdditiveNTT.Xⱼ, AdditiveNTT.Xⱼ_zero_eq_one, AdditiveNTT.degree_Xⱼ, AdditiveNTT.basisVectors, AdditiveNTT.CoeffVecSpace, AdditiveNTT.finiteDimensionalCoeffVecSpace, AdditiveNTT.toCoeffsVec, AdditiveNTT.linearIndependent_rows_of_lower_triangular_ne_zero_diag, AdditiveNTT.changeOfBasisMatrix, AdditiveNTT.changeOfBasisMatrix_lower_triangular, AdditiveNTT.changeOfBasisMatrix_diag_ne_zero, AdditiveNTT.changeOfBasisMatrix_det_ne_zero, AdditiveNTT.changeOfBasisMatrix_invertible, AdditiveNTT.coeff_vectors_linear_independent, AdditiveNTT.basisVectors_linear_independent, AdditiveNTT.basisVectors_span, AdditiveNTT.novelPolynomialBasis, AdditiveNTT.polynomialFromNovelCoeffs, AdditiveNTT.polynomialFromNovelCoeffsF₂, AdditiveNTT.novelPolynomialBasis_is_basisVectors, AdditiveNTT.monomialToNovelCoeffs, AdditiveNTT.novelToMonomialCoeffs, AdditiveNTT.monomialToNovel_novelToMonomial_inverse, AdditiveNTT.novelToMonomial_monomialToNovel_inverse
statement: formalized
proof: formalized
---

# Novel Polynomial Basis

`CompPoly.Fields.Binary.AdditiveNTT.NovelPolynomialBasis`, in [CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean), by Chung Thai Nguyen, Quang Dao.

> This file defines the components of a novel polynomial basis over a field `L` with degree `r` as an
> algebra over its prime-characteristic subfield `𝔽q`, and an `𝔽q`-basis `β` for `L`.
>
> ## Main Definitions
>
> - `Uᵢ`: `𝔽q`-linear span of the initial `i` vectors of our basis `β`
> - `Wᵢ(X)`: subspace vanishing polynomial over `Uᵢ`, with normalized form `Ŵᵢ(X)`
> - `{Xⱼ(X), j ∈ Fin 2^ℓ}`: basis vectors of `L⦃<2^ℓ⦄[X]` over `L` constructed from `Ŵᵢ(X)`
> - `novelPolynomialBasis`: the novel polynomial basis for `L⦃<2^ℓ⦄[X]`
> - `W_prod_comp_decomposition`: decomposition of `Wᵢ` into a product of compositions `Π c ∈ Uᵢ, (Wᵢ₋₁
>   ∘ (X - c • βᵢ₋₁))`
> - `W_linearity`: `Wᵢ` is `𝔽q`-linear and satisfies the recursion formula `Wᵢ = (Wᵢ₋₁)^|𝔽q| -
>   ((Wᵢ₋₁)(βᵢ₋₁))^(|𝔽q|-1) * Wᵢ₋₁`
>
> …
>
> ## References
>
> * [Lin, S., Chung, W., and Han, Y.S, *Novel polynomial basis and its application to
>     Reed–Solomon erasure codes*][LCH14]
> * [Von zur Gathen, J., and Gerhard, J., *Arithmetic and factorization of polynomial
>     over F2 (extended abstract)*][GGJ96]

`AdditiveNTT.fintype_card_gt_one_of_field` (lemma, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L64))

```lean
lemma fintype_card_gt_one_of_field (K : Type*) [Field K] [Fintype K] :
    1 < Fintype.card K
```

`AdditiveNTT.U` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L75))

> **𝔽q-linear subspaces `Uᵢ`**
>
> `∀ i ∈ {0, ..., r-1}`, we define `Uᵢ:= <β₀, ..., βᵢ₋₁>_{𝔽q}`
> as the `𝔽q`-linear span of the initial `i` vectors of our basis `β`.
>
> NOTE: We might allow `i = r` in the future if needed.

```lean
def U (i : Fin r) : Subspace 𝔽q L
```

`AdditiveNTT.finrank_U` (lemma, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L85))

```lean
lemma finrank_U (i : Fin r) :
    Module.finrank 𝔽q (U 𝔽q β i) = i
```

`AdditiveNTT.fintype_U` (instance, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L133))

```lean
noncomputable instance fintype_U (i : Fin r) : Fintype (U 𝔽q β i)
```

`AdditiveNTT.U_card` (lemma, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L138))

```lean
lemma U_card (i : Fin r) :
    Fintype.card (U 𝔽q β i) = (Fintype.card 𝔽q)^i.val
```

`AdditiveNTT.U_i_is_union_of_cosets` (lemma, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L149))

> An essential helper lemma showing that `Uᵢ` is the union of all cosets of `Uᵢ₋₁`
> generated by scaling `βᵢ₋₁` by elements of `𝔽q`.

```lean
lemma U_i_is_union_of_cosets (i : Fin r) (hi : 0 < i) :
    (U 𝔽q β i : Set L) = ⋃ (c : 𝔽q), (fun u => c • β (i-1) + u) '' (U 𝔽q β (i - 1))
```

`AdditiveNTT.βᵢ_not_in_Uᵢ` (lemma, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L182))

> The basis vector `βᵢ` is not an element of the subspace `Uᵢ`.

```lean
lemma βᵢ_not_in_Uᵢ (i : Fin r) :
    β i ∉ U 𝔽q β i
```

`AdditiveNTT.root_U_lift_down` (theorem, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L215))

```lean
theorem root_U_lift_down
    (i : Fin r) (h_i_add_1 : i + 1 < r) (a : L) :
  a ∈ (U 𝔽q β (i+1)) → ∃! x: 𝔽q, a - x • β i ∈ (U 𝔽q β i)
```

`AdditiveNTT.root_U_lift_up` (theorem, [line 263](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L263))

```lean
theorem root_U_lift_up (i : Fin r) (h_i_add_1 : i + 1 < r) (a : L) (x : 𝔽q) :
    a - x • β i ∈ (U 𝔽q β i) → a ∈ (U 𝔽q β (i+1))
```

`AdditiveNTT.W` (definition, [line 292](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L292))

> The subspace vanishing polynomial `Wᵢ(X) := ∏_{u ∈ Uᵢ} (X - u), ∀ i ∈ {0, ..., r-1}`.
> The degree of `Wᵢ(X)` is `|Uᵢ| = 2^i`.
> - [LCH14, Lemma 1]: `Wᵢ(X)` is an `𝔽q`-linearized polynomial, i.e.,
>   `Wᵢ(x) = ∑_{j=0}^i a_{i, j} x^{2^j}` for some constants `a_{i, j} ∈ L` (Equation (3)).
> - The additive property: `Wᵢ(x + y) = Wᵢ(x) + Wᵢ(y)` for all `x, y ∈ L` (Equation (4)).
> - For all `y ∈ Uᵢ`, `Wᵢ(x + y) = Wᵢ(x)` (Equation (14)).

```lean
noncomputable def W (i : Fin r) : L[X]
```

`AdditiveNTT.degree_W` (lemma, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L297))

> The degree of the subspace vanishing polynomial `Wᵢ(X)` is `2ⁱ`.

```lean
lemma degree_W (i : Fin r) : (W 𝔽q β i).degree = (Fintype.card 𝔽q)^i.val
```

`AdditiveNTT.W_monic` (lemma, [line 318](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L318))

> The subspace vanishing polynomial `Wᵢ(X)` is monic.

```lean
lemma W_monic (i : Fin r) : (W 𝔽q β i).Monic
```

`AdditiveNTT.W_ne_zero` (lemma, [line 325](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L325))

```lean
lemma W_ne_zero (i : Fin r) : (W 𝔽q β i) ≠ 0
```

`AdditiveNTT.Wᵢ_eval_βᵢ_neq_zero` (lemma, [line 336](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L336))

> The evaluation of `Wᵢ(X)` at `βᵢ` is non-zero.

```lean
lemma Wᵢ_eval_βᵢ_neq_zero
    (i : Fin r): (W 𝔽q β i).eval (β i) ≠ 0
```

`AdditiveNTT.Wᵢ_vanishing` (lemma, [line 358](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L358))

```lean
lemma Wᵢ_vanishing (i : Fin r) :
    ∀ u ∈ U 𝔽q β i, (W 𝔽q β i).eval u = 0
```

`AdditiveNTT.W₀_eq_X` (lemma, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L369))

```lean
lemma W₀_eq_X : W 𝔽q β 0 = X
```

> ### Formalization of linearity of subspace vanishing polynomials
>
> This section formalizes the key properties of the subspace vanishing polynomials `Wᵢ`,
> including their recursive structure and `𝔽q`-linearity as described in Lemma 2.3 of [GGJ96].
> The proofs are done by simultaneous induction on `i`.

`AdditiveNTT.W_splits` (lemma, [line 400](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L400))

> The subspace vanishing polynomial `Wᵢ(X)` splits into linear factors over `L`.

```lean
lemma W_splits (i : Fin r) : (W 𝔽q β i).Splits
```

`AdditiveNTT.roots_W` (lemma, [line 412](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L412))

> The roots of `Wᵢ(X)` are precisely the elements of the subspace `Uᵢ`.

```lean
lemma roots_W (i : Fin r) : -- converts root Multiset into (univ: Uᵢ.val.map)
    (W 𝔽q β i).roots = (univ : Finset (U 𝔽q β i)).val.map (fun u => u.val)
```

`AdditiveNTT.algEquivAevalXSubC` (definition, [line 435](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L435))

```lean
noncomputable def algEquivAevalXSubC {R : Type*} [CommRing R] (t : R) : R[X] ≃ₐ[R] R[X]
```

`AdditiveNTT.comp_X_sub_C_eq_zero_iff` (lemma, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L445))

```lean
lemma comp_X_sub_C_eq_zero_iff (p : L[X]) (a : L) :
    p.comp (X - C a) = 0 ↔ p = 0
```

`AdditiveNTT.rootMultiplicity_comp_X_sub_C` (lemma, [line 454](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L454))

> The multiplicity of a root `x` in a polynomial `p` composed with `(X - a)` is equal to the
> multiplicity of the root `x - a` in `p`.

```lean
lemma rootMultiplicity_comp_X_sub_C (p : L[X]) (a x : L) :
    rootMultiplicity x (p.comp (X - C a)) = rootMultiplicity (x - a) p
```

`AdditiveNTT.roots_comp_X_sub_C` (lemma, [line 483](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L483))

```lean
lemma roots_comp_X_sub_C (p : L[X]) (a : L) :
    (p.comp (X - C a)).roots = p.roots.map (fun r => r + a)
```

`AdditiveNTT.Prod_W_comp_X_sub_C_ne_zero` (lemma, [line 510](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L510))

```lean
lemma Prod_W_comp_X_sub_C_ne_zero (i : Fin r) :
    (univ : Finset 𝔽q).prod (fun c => (W 𝔽q β i).comp (X - C (c • β i))) ≠ 0
```

`AdditiveNTT.rootMultiplicity_W` (lemma, [line 528](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L528))

> The polynomial `Wᵢ(X)` has simple roots (multiplicity 1) for each element in the
> subspace `Uᵢ`, and no other roots.

```lean
lemma rootMultiplicity_W (i : Fin r) (a : L) :
    rootMultiplicity a (W 𝔽q β i) = if a ∈ (U 𝔽q β i : Set L) then 1 else 0
```

`AdditiveNTT.eval_W_eq_zero_iff_in_U` (lemma, [line 598](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L598))

```lean
lemma eval_W_eq_zero_iff_in_U (i : Fin r) (a : L) :
    (W 𝔽q β i).eval a = 0 ↔ a ∈ U 𝔽q β i
```

`AdditiveNTT.rootMultiplicity_prod_W_comp_X_sub_C` (lemma, [line 624](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L624))

```lean
lemma rootMultiplicity_prod_W_comp_X_sub_C
    (i : Fin r) (h_i_add_1 : i + 1 < r) (a : L) :
    rootMultiplicity a ((univ : Finset 𝔽q).prod (fun c => (W 𝔽q β i).comp (X - C (c • β i)))) =
    if a ∈ (U 𝔽q β (i+1) : Set L) then 1 else 0
```

`AdditiveNTT.W_prod_comp_decomposition` (lemma, [line 757](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L757))

> The generic product form of the recursion for `Wᵢ`.
> This follows the first line of the proof for (i) in the description.
> `Wᵢ(X) = ∏_{c ∈ 𝔽q} Wᵢ₋₁ ∘ (X - cβᵢ₋₁)`.

```lean
lemma W_prod_comp_decomposition
    (i : Fin r) (hi : i > 0) :
    (W 𝔽q β i) = ∏ c: 𝔽q, (W 𝔽q β (i-1)).comp (X - C (c • β (i-1)))
```

`AdditiveNTT.comp_sub_C_of_linear_eval` (lemma, [line 817](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L817))

```lean
lemma comp_sub_C_of_linear_eval (p : L[X])
    (h_lin : IsLinearMap 𝔽q (f := fun inner_p ↦ p.comp inner_p)) (a : L) :
    p.comp (X - C a) = p - C (eval a p)
```

`AdditiveNTT.inductive_rec_form_W_comp` (lemma, [line 835](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L835))

```lean
lemma inductive_rec_form_W_comp (i : Fin r) (h_i_add_1 : i + 1 < r)
    (h_prev_linear_map : IsLinearMap (R := 𝔽q) (M := L[X]) (M₂ := L[X])
      (f := fun inner_p ↦ (W 𝔽q β i).comp inner_p)) :
    ∀ p: L[X], (W 𝔽q β (i + 1)).comp p =
      ((W 𝔽q β i).comp p) ^ Fintype.card 𝔽q -
        C (eval (β i) (W 𝔽q β i)) ^ (Fintype.card 𝔽q - 1) * ((W 𝔽q β i).comp p)
```

`AdditiveNTT.inductive_linear_map_W` (lemma, [line 968](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L968))

```lean
lemma inductive_linear_map_W (i : Fin r) (h_i_add_1 : i + 1 < r)
    (h_prev_linear_map : IsLinearMap 𝔽q (f := fun inner_p ↦ (W 𝔽q β i).comp inner_p)) :
    IsLinearMap 𝔽q (f := fun inner_p ↦ (W 𝔽q β (i + 1)).comp inner_p)
```

`AdditiveNTT.W_linearity` (theorem, [line 1064](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1064))

> **Simultaneous Proof of Linearity for `Wᵢ`** from the paper [GGJ96] (Lemma 2.3)
> `Wᵢ` is an 𝔽q-linearized polynomial. This means for all polynomials `f, g` with coefficients
>   in `L` (i.e. `L[X]`) and for all `c ∈ 𝔽q`, we have: `Wᵢ(f + g) = Wᵢ(f) + Wᵢ(g)` and
>   `Wᵢ(c * f) = c * Wᵢ(f)`. As a corollary of this, `Wᵢ` is 𝔽q-linear when evaluated on elements
>   of `L`: `Wᵢ(x + y) = Wᵢ(x) + Wᵢ(y)` for all `x, y ∈ L`.

```lean
theorem W_linearity (i : Fin r) :
    IsLinearMap 𝔽q (f := fun inner_p ↦ (W 𝔽q β i).comp inner_p)
```

`AdditiveNTT.polyEvalLinearMap` (definition, [line 1099](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1099))

> Helper function to create a linear map from a polynomial whose evaluation is additive.

```lean
noncomputable def polyEvalLinearMap {L 𝔽q : Type*} [Field L] [Field 𝔽q] [Algebra 𝔽q L]
  (p : L[X]) (hp_add : IsLinearMap 𝔽q (fun x : L => p.eval x)) : L →ₗ[𝔽q] L
```

`AdditiveNTT.W_linear_comp_decomposition` (theorem, [line 1108](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1108))

```lean
theorem W_linear_comp_decomposition (i : Fin r) (h_i_add_1 : i + 1 < r) :
    ∀ p: L[X], (W 𝔽q β (i + 1)).comp p =
      ((W 𝔽q β i).comp p) ^ Fintype.card 𝔽q -
        C (eval (β i) (W 𝔽q β i)) ^ (Fintype.card 𝔽q - 1) * ((W 𝔽q β i).comp p)
```

`AdditiveNTT.W_is_additive` (lemma, [line 1117](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1117))

> The additive property of `Wᵢ`: `Wᵢ(x + y) = Wᵢ(x) + Wᵢ(y)`.

```lean
lemma W_is_additive
    (i : Fin r) :
  IsLinearMap (R := 𝔽q) (M := L) (M₂ := L) (f := fun x ↦ (W 𝔽q β i).eval x)
```

`AdditiveNTT.kernel_W_eq_U` (theorem, [line 1124](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1124))

```lean
theorem kernel_W_eq_U (i : Fin r) :
    LinearMap.ker (polyEvalLinearMap (W 𝔽q β i)
    (W_is_additive 𝔽q β i)) = U 𝔽q β i
```

`AdditiveNTT.W_add_U_invariant` (lemma, [line 1135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1135))

> For all `y ∈ Uᵢ`, `Wᵢ(x + y) = Wᵢ(x)`.

```lean
lemma W_add_U_invariant
    (i : Fin r) :
  ∀ x : L, ∀ y ∈ U 𝔽q β i, (W 𝔽q β i).eval (x + y) = (W 𝔽q β i).eval x
```

> # Normalized Subspace Vanishing Polynomials `Ŵᵢ(X) := Wᵢ(X) / Wᵢ(βᵢ), ∀ i ∈ {0, ..., r-1}`

`AdditiveNTT.normalizedW` (definition, [line 1143](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1143))

```lean
noncomputable def normalizedW (i : Fin r) : L[X]
```

`AdditiveNTT.normalizedWᵢ_eval_βᵢ_eq_1` (lemma, [line 1148](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1148))

> The evaluation of the normalized polynomial `Ŵᵢ(X)` at `βᵢ` is 1.

```lean
lemma normalizedWᵢ_eval_βᵢ_eq_1 {i : Fin r} :
    (normalizedW (𝔽q := 𝔽q) (β := β) (i :=i)).eval (β i) = 1
```

`AdditiveNTT.normalizedW₀_eq_1_div_β₀` (lemma, [line 1161](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1161))

```lean
lemma normalizedW₀_eq_1_div_β₀ : normalizedW (𝔽q := 𝔽q) (β := β) (i :=0) = X * C (1 / (β 0))
```

`AdditiveNTT.eval_normalizedW_succ_at_beta_prev` (lemma, [line 1169](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1169))

> The evaluation `Ŵᵢ₊₁(βᵢ)` is 0. This is because `Ŵᵢ₊₁ = q⁽ⁱ⁾ ∘ Ŵᵢ` and `q⁽ⁱ⁾(1) = 0`.

```lean
lemma eval_normalizedW_succ_at_beta_prev (i : Fin r) (h_i_add_1 : i + 1 < r) :
    (normalizedW 𝔽q β (i + 1)).eval (β i) = 0
```

`AdditiveNTT.degree_normalizedW` (lemma, [line 1183](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1183))

> The degree of `Ŵᵢ(X)` remains `|𝔽q|ⁱ`.

```lean
lemma degree_normalizedW (i : Fin r) :
    (normalizedW 𝔽q β i).degree = (Fintype.card 𝔽q)^(i.val)
```

`AdditiveNTT.β_lt_mem_U` (lemma, [line 1198](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1198))

```lean
lemma β_lt_mem_U (i : Fin r) (j : Fin i) :
    β ⟨j, by omega⟩ ∈ U 𝔽q β (i:=i)
```

`AdditiveNTT.normalizedWᵢ_vanishing` (lemma, [line 1209](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1209))

> The normalized polynomial `Ŵᵢ(X)` vanishes on `Uᵢ`.

```lean
lemma normalizedWᵢ_vanishing (i : Fin r) :
    ∀ u ∈ U 𝔽q β i, (normalizedW 𝔽q β i).eval u = 0
```

`AdditiveNTT.normalizedW_is_linear_map` (theorem, [line 1218](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1218))

> The normalized subspace vanishing polynomial `Ŵᵢ(X)` is `𝔽q`-linear.

```lean
theorem normalizedW_is_linear_map (i : Fin r) :
    IsLinearMap 𝔽q (f := fun inner_p ↦ (normalizedW 𝔽q β i).comp inner_p)
```

`AdditiveNTT.normalizedW_is_additive` (theorem, [line 1274](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1274))

```lean
theorem normalizedW_is_additive (i : Fin r) :
    IsLinearMap 𝔽q (f := fun x ↦ (normalizedW 𝔽q β i).eval x)
```

`AdditiveNTT.kernel_normalizedW_eq_U` (theorem, [line 1280](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1280))

```lean
theorem kernel_normalizedW_eq_U (i : Fin r) :
    LinearMap.ker (polyEvalLinearMap (normalizedW 𝔽q β i)
    (normalizedW_is_additive 𝔽q β i))
    = U 𝔽q β i
```

`AdditiveNTT.Xⱼ` (definition, [line 1300](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1300))

> The Novel Polynomial Basis {`Xⱼ(X)`, j ∈ Fin 2^ℓ} for the space `L⦃<2^ℓ⦄[X]` over `L`

```lean
noncomputable def Xⱼ (ℓ : ℕ) (h_ℓ : ℓ ≤ r) (j : Fin (2 ^ ℓ)) : L[X]
```

`AdditiveNTT.Xⱼ_zero_eq_one` (lemma, [line 1306](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1306))

> The zero-th element of the novel polynomial basis is the constant 1

```lean
lemma Xⱼ_zero_eq_one (ℓ : ℕ) (h_ℓ : ℓ ≤ r) :
    Xⱼ 𝔽q β ℓ h_ℓ ⟨0, by exact Nat.two_pow_pos ℓ⟩ = 1
```

`AdditiveNTT.degree_Xⱼ` (lemma, [line 1315](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1315))

> The degree of `Xⱼ(X)` is `j`:
> `deg(Xⱼ(X)) = Σ_{i=0}^{ℓ-1} jᵢ * deg(Ŵᵢ(X)) = Σ_{i=0}^{ℓ-1} jᵢ * 2ⁱ = j`

```lean
lemma degree_Xⱼ (ℓ : ℕ) (h_ℓ : ℓ ≤ r) (j : Fin (2 ^ ℓ)) :
    (Xⱼ 𝔽q β ℓ h_ℓ j).degree = j
```

`AdditiveNTT.basisVectors` (definition, [line 1387](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1387))

> The basis vectors `{Xⱼ(X), j ∈ Fin 2^ℓ}` forms a basis for `L⦃<2^ℓ⦄[X]`

```lean
noncomputable def basisVectors (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
  Fin (2 ^ ℓ) → L⦃<2^ℓ⦄[X]
```

`AdditiveNTT.CoeffVecSpace` (abbreviation, [line 1397](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1397))

> The vector space of coefficients for polynomials of degree < 2^ℓ.

```lean
abbrev CoeffVecSpace (L : Type u) (ℓ : Nat)
```

`AdditiveNTT.finiteDimensionalCoeffVecSpace` (instance, [line 1399](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1399))

```lean
noncomputable instance finiteDimensionalCoeffVecSpace (ℓ : ℕ) :
  FiniteDimensional (K := L) (V := CoeffVecSpace L ℓ)
```

`AdditiveNTT.toCoeffsVec` (definition, [line 1405](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1405))

> The linear map from polynomials (in the subtype) to their coefficient vectors.

```lean
def toCoeffsVec (ℓ : Nat) : L⦃<2^ℓ⦄[X] →ₗ[L] CoeffVecSpace L ℓ
```

`AdditiveNTT.linearIndependent_rows_of_lower_triangular_ne_zero_diag` (lemma, [line 1415](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1415))

> The rows of a square lower-triangular matrix with
> non-zero diagonal entries are linearly independent.

```lean
lemma linearIndependent_rows_of_lower_triangular_ne_zero_diag
    {n : ℕ} {R : Type*} [Field R] (A : Matrix (Fin n) (Fin n) R)
  (h_lower_triangular : A.BlockTriangular ⇑OrderDual.toDual) (h_diag : ∀ i, A i i ≠ 0) :
  LinearIndependent R A
```

`AdditiveNTT.changeOfBasisMatrix` (definition, [line 1428](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1428))

> The change-of-basis matrix from the novel basis to the monomial basis.
> Aⱼᵢ = coeff of Xⁱ in novel basis vector 𝕏ⱼ. novel_coeffs * A = monomial_coeffs

```lean
noncomputable def changeOfBasisMatrix (ℓ : Nat) (h_ℓ : ℓ ≤ r) : Matrix (Fin (2^ℓ)) (Fin (2^ℓ)) L
```

`AdditiveNTT.changeOfBasisMatrix_lower_triangular` (theorem, [line 1433](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1433))

```lean
theorem changeOfBasisMatrix_lower_triangular
    (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
  (changeOfBasisMatrix 𝔽q β ℓ h_ℓ).BlockTriangular ⇑OrderDual.toDual
```

`AdditiveNTT.changeOfBasisMatrix_diag_ne_zero` (theorem, [line 1452](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1452))

```lean
theorem changeOfBasisMatrix_diag_ne_zero
    (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
  (∀ i, (changeOfBasisMatrix 𝔽q β ℓ h_ℓ) i i ≠ 0)
```

`AdditiveNTT.changeOfBasisMatrix_det_ne_zero` (theorem, [line 1463](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1463))

> The determinant of the change-of-basis matrix is non-zero.

```lean
theorem changeOfBasisMatrix_det_ne_zero
    (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
  (changeOfBasisMatrix 𝔽q β ℓ h_ℓ).det ≠ 0
```

`AdditiveNTT.changeOfBasisMatrix_invertible` (instance, [line 1478](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1478))

> The change-of-basis matrix is invertible, this is required by the proofs
> of inversion between monomial and novel polynomial basis coefficients.

```lean
noncomputable instance changeOfBasisMatrix_invertible
  (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
  Invertible (changeOfBasisMatrix 𝔽q β ℓ h_ℓ)
```

`AdditiveNTT.coeff_vectors_linear_independent` (lemma, [line 1492](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1492))

> The coefficient vectors of the novel basis polynomials are linearly independent.
> This is proven by showing that the change-of-basis matrix to the monomial basis
> is lower-triangular with a non-zero diagonal.

```lean
lemma coeff_vectors_linear_independent
    (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
    LinearIndependent L (toCoeffsVec (ℓ := ℓ) ∘ (basisVectors 𝔽q β ℓ h_ℓ))
```

`AdditiveNTT.basisVectors_linear_independent` (theorem, [line 1507](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1507))

> The basis vectors are linearly independent over `L`.

```lean
theorem basisVectors_linear_independent (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
    LinearIndependent L (basisVectors 𝔽q β ℓ h_ℓ)
```

`AdditiveNTT.basisVectors_span` (theorem, [line 1518](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1518))

> The basis vectors span the space of polynomials with degree less than `2^ℓ`.

```lean
theorem basisVectors_span (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
    Submodule.span L (Set.range (basisVectors 𝔽q β ℓ h_ℓ)) = ⊤
```

`AdditiveNTT.novelPolynomialBasis` (definition, [line 1540](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1540))

> The novel polynomial basis for `L⦃<2^ℓ⦄[X]`

```lean
noncomputable def novelPolynomialBasis (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
  Basis (Fin (2^ℓ)) (R := L) (M := L⦃<2^ℓ⦄[X])
```

`AdditiveNTT.polynomialFromNovelCoeffs` (definition, [line 1550](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1550))

> The polynomial `P(X)` derived from coefficients `a` in the novel polynomial basis `(Xⱼ)`,
> `P(X) := ∑_{j=0}^{2^ℓ-1} aⱼ ⋅ Xⱼ(X)`

```lean
noncomputable def polynomialFromNovelCoeffs (ℓ : ℕ) (h_ℓ : ℓ ≤ r)
  (a : Fin (2 ^ ℓ) → L) : L[X]
```

`AdditiveNTT.polynomialFromNovelCoeffsF₂` (definition, [line 1553](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1553))

```lean
noncomputable def polynomialFromNovelCoeffsF₂
  (ℓ : ℕ) (h_ℓ : ℓ ≤ r) (a : Fin (2 ^ ℓ) → L) : L⦃<2^ℓ⦄[X]
```

`AdditiveNTT.novelPolynomialBasis_is_basisVectors` (theorem, [line 1574](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1574))

> Proof that the novel polynomial basis is indeed the indicated basis vectors

```lean
theorem novelPolynomialBasis_is_basisVectors (ℓ : Nat) (h_ℓ : ℓ ≤ r) :
    (novelPolynomialBasis 𝔽q β ℓ h_ℓ)
    = basisVectors 𝔽q β ℓ h_ℓ
```

`AdditiveNTT.monomialToNovelCoeffs` (definition, [line 1582](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1582))

> Convert monomial coefficients to novel polynomial basis coefficients.
> Using row vectors: n = m * A⁻¹.

```lean
noncomputable def monomialToNovelCoeffs

  (ℓ : ℕ) (h_ℓ : ℓ ≤ r) (monomial_coeffs : Fin (2 ^ ℓ) → L) : Fin (2^ℓ) → L
```

`AdditiveNTT.novelToMonomialCoeffs` (definition, [line 1593](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1593))

> Convert novel polynomial basis coefficients to monomial coefficients.
> Using row vectors: m = n * A.

```lean
noncomputable def novelToMonomialCoeffs

  (ℓ : ℕ) (h_ℓ : ℓ ≤ r) (novel_coeffs : Fin (2 ^ ℓ) → L) : Fin (2^ℓ) → L
```

`AdditiveNTT.monomialToNovel_novelToMonomial_inverse` (theorem, [line 1601](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1601))

> The conversion functions are inverses of each other. (Monomial -> Novel -> Monomial)

```lean
theorem monomialToNovel_novelToMonomial_inverse
    (ℓ : ℕ) (h_ℓ : ℓ ≤ r) :
  ∀ coeffs : Fin (2^ℓ) → L,
    novelToMonomialCoeffs 𝔽q β ℓ h_ℓ
    (monomialToNovelCoeffs 𝔽q β ℓ h_ℓ coeffs) = coeffs
```

`AdditiveNTT.novelToMonomial_monomialToNovel_inverse` (theorem, [line 1623](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean#L1623))

> The conversion functions are inverses of each other. (Novel -> Monomial -> Novel)

```lean
theorem novelToMonomial_monomialToNovel_inverse
    (ℓ : ℕ) (h_ℓ : ℓ ≤ r) :
  ∀ coeffs : Fin (2^ℓ) → L,
    monomialToNovelCoeffs 𝔽q β ℓ h_ℓ
      (novelToMonomialCoeffs 𝔽q β ℓ h_ℓ coeffs) = coeffs
```

## Depends on

- [Bit operations on natural numbers](../../../data/nat/bitwise.md)

## Proof depends on

- [Frobenius polynomial identities](../../../data/polynomial/frobenius.md)
- [Monomial basis for algebra extensions](../../../data/polynomial/monomialbasis.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/AdditiveNTT/NovelPolynomialBasis.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.NovelPolynomialBasis.json)
