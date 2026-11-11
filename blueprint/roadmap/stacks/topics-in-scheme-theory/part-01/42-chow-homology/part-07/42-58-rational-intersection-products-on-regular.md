---
declaration: section
origin: cited
lean: Stacks.Chow.rationalIntersectionProduct, Stacks.Chow.rationalIntersectionProduct_comm, Stacks.Chow.rationalIntersectionProduct_assoc, Stacks.Chow.rationalIntersectionProduct_eq_rationalChernCharacterComponentCap, Stacks.Chow.rationalIntersectionProduct_mem_codimensionChowSubmodule, Stacks.Chow.existsUnique_rationalIntersectionProduct, Stacks.Chow.rationalChernCharacterAlgEquiv, Stacks.Chow.rationalSecondAdams_eq_smul_of_rationalChernCharacterCap_mem
statement: formalized
proof: formalized
---

# 42.58 Rational intersection products on regular schemes

Section 42.58 of the Stacks Project, [Tag 0FEX](https://stacks.math.columbia.edu/tag/0FEX). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FEX, the section

[Tag 0FEX](https://stacks.math.columbia.edu/tag/0FEX) in the Stacks Project.

**`Stacks.Chow.rationalIntersectionProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L224). The attribute's comment: “the construction of the section: for X as in 0FEY (Noetherian, equivalently quasi-compact, given locally of finite type over S), α · β = ch(α') ∩ β with α' the unique class with ch(α') ∩ [X] = α; CH^*(X) ⊗ Q is CH\_*(X) ⊗ Q, the internal direct sum of the codimension pieces codimensionChowSubmodule”.

> **The intersection product of Stacks Section 0FEX** on `CH_*(X) ⊗ 𝐐`, for `X` Noetherian
> (equivalently quasi-compact), regular, of finite type over `S`, with affine diagonal and `δ_{X/S}`
> bounded: `α · β = ch(α') ∩ β`, where `α' ∈ K_0(Vect(X)) ⊗ 𝐐` is the unique class with
> `ch(α') ∩ [X] = α` (Stacks 0FEY, `Stacks.Chow.bijective_flip_rationalChernCharacterCap`).

```lean
def rationalIntersectionProduct : CHQ →ₗ[ℚ] CHQ →ₗ[ℚ] CHQ
```

**`Stacks.Chow.rationalIntersectionProduct_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L262). The attribute's comment: “the product of the section is symmetric: α · β = β · α, for X as in 0FEY”.

> **The product is commutative** (Section 0FEX: "this is a symmetric pairing"), the operators
> `ch(α') ∩ -` pairwise commuting.

```lean
theorem rationalIntersectionProduct_comm (α β : CHQ) :
    rationalIntersectionProduct hX hb α β = rationalIntersectionProduct hX hb β α
```

**`Stacks.Chow.rationalIntersectionProduct_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L271). The attribute's comment: “the product of the section is associative: (α · β) · γ = α · (β · γ), for X as in 0FEY”.

> **The product is associative** (Section 0FEX): both bracketings of `α · β · γ` are
> `ch(α') ∩ ch(β') ∩ ch(γ') ∩ [X]`, up to reordering the commuting operators.

```lean
theorem rationalIntersectionProduct_assoc (α β γ : CHQ) :
    rationalIntersectionProduct hX hb (rationalIntersectionProduct hX hb α β) γ =
      rationalIntersectionProduct hX hb α (rationalIntersectionProduct hX hb β γ)
```

**`Stacks.Chow.rationalIntersectionProduct_eq_rationalChernCharacterComponentCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L396). The attribute's comment: “the defining formula of the section: for α ∈ CH^i(X) ⊗ Q with ch(α') ∩ [X] = α, α · β = ch(α') ∩ β = ch\_i(α') ∩ β, for X as in 0FEY”.

> **The product of a class of codimension `i` is computed by `ch_i`** (Section 0FEX). If
> `α = ch(α') ∩ [X]` lies in `CH^i(X) ⊗ 𝐐` then `α · β = ch_i(α') ∩ β`, the definition of the
> source.

```lean
theorem rationalIntersectionProduct_eq_rationalChernCharacterComponentCap
    {i : ℕ} {α : CHQ} (hα : α ∈ codimensionChowSubmodule C sX i)
    {a : ℚ ⊗[ℤ] VectorBundleKZero X}
    (ha : rationalChernCharacterCap C sX a (rationalFundamentalClass C sX) = α) (β : CHQ) :
    rationalIntersectionProduct hX hb α β = rationalChernCharacterComponentCap C sX i a β
```

**`Stacks.Chow.rationalIntersectionProduct_mem_codimensionChowSubmodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L424). The attribute's comment: “the product of the section is graded: CH^i(X) ⊗ Q · CH^j(X) ⊗ Q ⊆ CH^\{i+j}(X) ⊗ Q, for X as in 0FEY”.

> **The product is graded by codimension** (Section 0FEX: `α · β ∈ CH^{i+j}(X) ⊗ 𝐐`):
> `CH^i(X) ⊗ 𝐐 · CH^j(X) ⊗ 𝐐 ⊆ CH^{i+j}(X) ⊗ 𝐐`.

```lean
theorem rationalIntersectionProduct_mem_codimensionChowSubmodule
    {i j : ℕ} {α β : CHQ} (hα : α ∈ codimensionChowSubmodule C sX i)
    (hβ : β ∈ codimensionChowSubmodule C sX j) :
    rationalIntersectionProduct hX hb α β ∈ codimensionChowSubmodule C sX (i + j)
```

**`Stacks.Chow.existsUnique_rationalIntersectionProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionRing.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionRing.lean#L107). The attribute's comment: “the closing reformulation of the section: for X as in 0FEY, there is a unique commutative, associative intersection product on CH^*(X) ⊗ Q compatible with the grading such that K\_0(Vect(X)) ⊗ Q → CH^*(X) ⊗ Q is a ring isomorphism, and it is the product of the section”.

> For `X` as in Stacks 0FEY (Noetherian, equivalently quasi-compact, regular, of finite type over
> `S`, with affine diagonal and `δ_{X/S}` bounded), `rationalIntersectionProduct` is the unique
> bilinear product on `CH^*(X) ⊗ 𝐐 = CH_*(X) ⊗ 𝐐` which is commutative, associative, graded by the
> codimension pieces `codimensionChowSubmodule`, and for which `α' ↦ ch(α') ∩ [X]` is multiplicative,
> that is, an isomorphism of rings.

```lean
theorem existsUnique_rationalIntersectionProduct :
    ∃! μ : CHQ →ₗ[ℚ] CHQ →ₗ[ℚ] CHQ,
      (∀ a b, μ (rationalChernCharacterCap C sX a (rationalFundamentalClass C sX))
          (rationalChernCharacterCap C sX b (rationalFundamentalClass C sX)) =
        rationalChernCharacterCap C sX (a * b) (rationalFundamentalClass C sX)) ∧
      (∀ α β, μ α β = μ β α) ∧ (∀ α β γ, μ (μ α β) γ = μ α (μ β γ)) ∧
      ∀ {i j : ℕ} {α β : CHQ}, α ∈ codimensionChowSubmodule C sX i →
        β ∈ codimensionChowSubmodule C sX j → μ α β ∈ codimensionChowSubmodule C sX (i + j)
```

**`Stacks.Chow.rationalChernCharacterAlgEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionRing.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionRing.lean#L193). The attribute's comment: “the closing sentence of the section: for X as in 0FEY, K\_0(Vect(X)) ⊗ Q → CH^*(X) ⊗ Q, α' ↦ ch(α') ∩ [X], is an isomorphism of rings for the product of the section”.

> **The map of Stacks 0FEY is an isomorphism of rings**: for `X` as in Stacks 0FEY,
> `α' ↦ ch(α') ∩ [X]` is an isomorphism of `𝐐`-algebras from `K_0(Vect(X)) ⊗ 𝐐` onto the rational
> Chow ring `CH^*(X) ⊗ 𝐐 = CH_*(X) ⊗ 𝐐` with the product `rationalIntersectionProduct`.

```lean
def rationalChernCharacterAlgEquiv :
    ℚ ⊗[ℤ] VectorBundleKZero X ≃ₐ[ℚ] RationalIntersectionRing hX hb
```

**`Stacks.Chow.rationalSecondAdams_eq_smul_of_rationalChernCharacterCap_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean#L318). The attribute's comment: “the eigenvalue statement of the section: for X as in 0FEY, α ∈ CH^i(X) ⊗ Q and α' ∈ K\_0(Vect(X)) ⊗ Q with ch(α') ∩ [X] = α, ψ²(α') = 2^i α', where ψ² is the second Adams operation of 0FEJ extended Q-linearly (Stacks.Chow.rationalSecondAdams); proved from 0FEN (Stacks.Chow.chernCharacterVectorBundle\_secondAdams) and the uniqueness in 0FEY, as in the source”.

> **Stacks Project, Section 0FEX: the class answering to a cycle class of codimension `i` is a
> `2^i`-eigenvector of `ψ²`.** Let `X` be as in Stacks 0FEY (Noetherian, equivalently quasi-compact,
> regular, of finite type over `S`, with affine diagonal and `δ_{X/S}` bounded). If
> `α ∈ CH^i(X) ⊗ 𝐐` and `α' ∈ K_0(Vect(X)) ⊗ 𝐐` is the (unique, by Stacks 0FEY) class with
> `ch(α') ∩ [X] = α`, then `ψ²(α') = 2^i α'`.

```lean
theorem rationalSecondAdams_eq_smul_of_rationalChernCharacterCap_mem (hX : IsRegular X)
    (hb : ∃ lo hi : ℤ, ∀ x : X, lo ≤ relativeDimension C.dimensionFunction sX x ∧
      relativeDimension C.dimensionFunction sX x ≤ hi)
    {i : ℕ} {a : ℚ ⊗[ℤ] VectorBundleKZero X}
    (ha : rationalChernCharacterCap C sX a (rationalFundamentalClass C sX) ∈
      codimensionChowSubmodule C sX i) :
    rationalSecondAdams X a = (2 ^ i : ℚ) • a
```

**`Stacks.Chow.rationalChernCharacterVectorBundle_eq_zero_of_rationalChernCharacterCap_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean#L367). The attribute's comment: “the vanishing statement of the section: for X as in 0FEY, α ∈ CH^i(X) ⊗ Q and α' ∈ K\_0(Vect(X)) ⊗ Q with ch(α') ∩ [X] = α, ch\_j(α') = 0 in A^j(X) ⊗ Q for every j ≠ i, from ψ²(α') = 2^i α' and 0FEN, as in the source”.

> **Stacks Project, Section 0FEX: the components of `ch(α')` off the codimension vanish.** For
> `X` as in Stacks 0FEY, `α ∈ CH^i(X) ⊗ 𝐐` and `α' ∈ K_0(Vect(X)) ⊗ 𝐐` with `ch(α') ∩ [X] = α`, one
> has `ch_j(α') = 0` in `A^j(X) ⊗ 𝐐` for every `j ≠ i`.

```lean
theorem rationalChernCharacterVectorBundle_eq_zero_of_rationalChernCharacterCap_mem
    (hX : IsRegular X)
    (hb : ∃ lo hi : ℤ, ∀ x : X, lo ≤ relativeDimension C.dimensionFunction sX x ∧
      relativeDimension C.dimensionFunction sX x ≤ hi)
    {i : ℕ} {a : ℚ ⊗[ℤ] VectorBundleKZero X}
    (ha : rationalChernCharacterCap C sX a (rationalFundamentalClass C sX) ∈
      codimensionChowSubmodule C sX i) {j : ℕ} (hj : j ≠ i) :
    rationalChernCharacterVectorBundle C sX a j = 0
```

**`Stacks.Chow.rationalChernCharacterComponentCap_rationalFundamentalClass_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/SecondAdamsChernCharacter.lean#L392). The attribute's comment: “the consequence the section draws from the vanishing statement: for X as in 0FEY, α ∈ CH^i(X) ⊗ Q and α' ∈ K\_0(Vect(X)) ⊗ Q with ch(α') ∩ [X] = α, ch\_\{i'}(α') ∩ [X] = 0 for i' ≠ i and ch\_i(α') ∩ [X] = α”.

> **Stacks Project, Section 0FEX: `ch_{i'}(α') ∩ [X] = 0` for `i' ≠ i` and
> `ch_i(α') ∩ [X] = α`.** For `X` as in Stacks 0FEY, `α ∈ CH^i(X) ⊗ 𝐐` and
> `α' ∈ K_0(Vect(X)) ⊗ 𝐐` with `ch(α') ∩ [X] = α`, the components of `ch(α')` other than the
> `i`-th cap `[X]` to zero, and the `i`-th one caps `[X]` to `α`.

```lean
theorem rationalChernCharacterComponentCap_rationalFundamentalClass_of_mem (hX : IsRegular X)
    (hb : ∃ lo hi : ℤ, ∀ x : X, lo ≤ relativeDimension C.dimensionFunction sX x ∧
      relativeDimension C.dimensionFunction sX x ≤ hi)
    {i : ℕ} {a : ℚ ⊗[ℤ] VectorBundleKZero X}
    (ha : rationalChernCharacterCap C sX a (rationalFundamentalClass C sX) ∈
      codimensionChowSubmodule C sX i) :
    (∀ j : ℕ, j ≠ i →
        rationalChernCharacterComponentCap C sX j a (rationalFundamentalClass C sX) = 0) ∧
      rationalChernCharacterComponentCap C sX i a (rationalFundamentalClass C sX) =
        rationalChernCharacterCap C sX a (rationalFundamentalClass C sX)
```

## Tag 0FEY, a lemma

[Tag 0FEY](https://stacks.math.columbia.edu/tag/0FEY) in the Stacks Project.

**`Stacks.Chow.bijective_rationalChernCharacterCapFundamentalClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/RationalIntersectionProduct.lean#L180). The attribute's comment: “the whole lemma: for X quasi-compact, regular, of finite type over S, with affine diagonal and δ\_\{X/S} bounded, α ↦ ch(α) ∩ [X], K\_0(Vect(X)) ⊗ Q → A^*(X) ⊗ Q → CH\_*(X) ⊗ Q, is bijective; ch is the ring map of 0FEM into ∏\_p A^p(X) ⊗ Q, whose cap with [X] is a finite sum since δ\_\{X/S} is bounded”.

> **Stacks Project, Tag 0FEY.** Let `(S, δ)` be as in Situation 42.7.1 and let `X` be a
> quasi-compact regular scheme of finite type over `S` with affine diagonal and `δ_{X/S}` bounded.
> Then the composition
>
>   `K_0(Vect(X)) ⊗ 𝐐 ⟶ ∏_p A^p(X) ⊗ 𝐐 ⟶ CH_*(X) ⊗ 𝐐`,   `α ↦ ch(α) ∩ [X]`,
>
> of the Chern character of Remark 0FEM and the map `c ↦ c ∩ [X]` is bijective.
>
> The map is `Stacks.Chow.rationalChernCharacterCapFundamentalClass`, the sum over `p` of
> `ch_p(α) ∩ [X]` (`Stacks.Chow.rationalChernCharacterCapFundamentalClass_eq_sum`). The proof is
> `Stacks.Chow.bijective_rationalChernCharacterCapFundamentalClass_of_chernFormula` (Proposition 0FEW
> for `X = Y`, Remark 0FEU) applied to Lemma 0FEG
> (`Stacks.Chow.isRegularImmersionChernFormula_of_compactSpace`).

```lean
theorem bijective_rationalChernCharacterCapFundamentalClass [CompactSpace X] (hX : IsRegular X)
    (hb : ∃ lo hi : ℤ, ∀ x : X, lo ≤ relativeDimension C.dimensionFunction sX x ∧
      relativeDimension C.dimensionFunction sX x ≤ hi) :
    haveI := isNoetherian_of_compactSpace sX
    Function.Bijective (rationalChernCharacterCapFundamentalClass C sX)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.58, Tag 0FEX](https://stacks.math.columbia.edu/tag/0FEX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
