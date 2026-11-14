---
declaration: module
origin: cited
lean: CondensedMatter.Bloch.translation, CondensedMatter.Bloch.translation_single, CondensedMatter.Bloch.charFun, CondensedMatter.Bloch.ev, CondensedMatter.Bloch.ev_single, CondensedMatter.Bloch.ev_translation, CondensedMatter.Bloch.ev_single_zero, CondensedMatter.Bloch.ev_surjective
statement: formalized
proof: formalized
---

# Bloch's theorem on the lattice

The module `PhyslibAlpha.CondensedMatter.Bloch.Algebraic`, [PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean): 24 declarations, 15 with a docstring.

> A translation-invariant evolution of configurations of unit cells acts through its Bloch matrix.

## i. Overview

> Consider degrees of freedom attached to the cells of a lattice whose translation group is `Λ`,
> an abelian group such as `ℤ ^ d`. The contents of one unit cell, orbitals or spin components, form
> a module `M`, and a configuration is a finitely supported assignment of an element of `M` to each
> cell: `ψ : Λ →₀ M`. Translation acts by `(T a ψ) m = ψ (m - a)`. A crystal momentum is a character
> `χ` of `Λ`, and the Fourier transform of a configuration is `ev χ ψ = ∑ m, χ m • ψ m`.
>
> * The kernel of the Fourier transform is precisely the span that defines the momentum fiber. So the
>   fiber at momentum `χ` is a copy of the unit cell `M`: Bloch's reduction to a single cell.
> * Every translation-invariant linear map `D` satisfies `ev χ (D ψ) = H(k) (ev χ ψ)` for a matrix
>   `H(k)` on the unit cell, its *Bloch matrix*. No finite-range assumption is needed, as a
>   configuration has finite support, and the matrix is `H(k) v = ∑ m, χ m • (D (δ₀ v)) m`.
> * The Bloch matrix of a product is the product of Bloch matrices, and of the inverse the inverse.
> * A hopping Hamiltonian with amplitude `t n` to the cell displaced by `n` has
>   `H(k) = ∑ n, exp (i k n) t n`: the Fourier transform of its hoppings.
>
> No analysis, finite dimensionality or positivity is used. The analytic counterpart on `ℓ²` is in
> `RegularRep` and `Spectrum`, and the finite periodic crystal in `FiniteBloch`.

## ii. Key results

> - `translation` : translating a configuration of unit cells.
> - `ev` : the Fourier transform of a configuration at a crystal momentum.
> - `ker_ev` : the kernel of the Fourier transform defines the momentum fiber.
> - `fiberEquiv` : the fiber at momentum `χ` is the contents of a unit cell.
> - `symbol` : the Bloch matrix of a translation-invariant map.
> - `ev_apply` : Bloch's theorem, Fourier transform intertwines the map and its Bloch matrix.
> - `symbol_comp`, `symbol_id`, `isUnit_symbol` : the Bloch matrix of a product and of an inverse.
> - `hopping`, `symbol_hopping` : the Bloch Hamiltonian of a hopping model.

## iv. References

> * F. Bloch, Über die Quantenmechanik der Elektronen in Kristallgittern, Z. Phys. 52 (1929). [ref:
>   bloch\_1929]
> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapters 4 and 8.

## A. Translations and Fourier evaluation

**`CondensedMatter.Bloch.translation`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L83).

> Translation of finitely supported configurations: `(T a ψ) m = ψ (m - a)`.

```lean
noncomputable def translation : Multiplicative Λ →* Module.End K (Λ →₀ M)
```

**`CondensedMatter.Bloch.translation_single`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L100).

```lean
lemma translation_single (a : Multiplicative Λ) (m : Λ) (v : M) :
    translation (K := K) a (Finsupp.single m v)
      = Finsupp.single (m + Multiplicative.toAdd a) v
```

**`CondensedMatter.Bloch.charFun`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L106).

> A character `χ` of `Λ`, viewed as a function on the multiplicative group of translations.

```lean
def charFun (χ : AddChar Λ K) : Multiplicative Λ → K
```

**`CondensedMatter.Bloch.ev`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L109).

> Fourier evaluation at the character `χ`: `ev χ ψ = ∑ m, χ m • ψ m`.

```lean
noncomputable def ev (χ : AddChar Λ K) : (Λ →₀ M) →ₗ[K] M
```

**`CondensedMatter.Bloch.ev_single`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L112).

```lean
lemma ev_single (χ : AddChar Λ K) (m : Λ) (v : M) :
    ev χ (Finsupp.single m v) = χ m • v
```

**`CondensedMatter.Bloch.ev_translation`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L116).

```lean
lemma ev_translation (χ : AddChar Λ K) (a : Multiplicative Λ) (ψ : Λ →₀ M) :
    ev χ (translation (K := K) a ψ) = charFun χ a • ev χ ψ
```

**`CondensedMatter.Bloch.ev_single_zero`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L125).

```lean
lemma ev_single_zero (χ : AddChar Λ K) (v : M) : ev χ (Finsupp.single 0 v) = v
```

**`CondensedMatter.Bloch.ev_surjective`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L127).

```lean
lemma ev_surjective (χ : AddChar Λ K) : Function.Surjective (ev (M := M) χ)
```

## B. The momentum fiber is the unit cell

**`CondensedMatter.Bloch.sub_single_ev_mem_cobound`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L138).

> Every configuration is congruent, modulo the fiber relations, to its Fourier evaluation
> placed in the origin cell.

```lean
lemma sub_single_ev_mem_cobound (χ : AddChar Λ K) (ψ : Λ →₀ M) :
    ψ - Finsupp.single 0 (ev χ ψ)
      ∈ cobound (translation (K := K) (Λ := Λ) (M := M)) (charFun χ)
```

**`CondensedMatter.Bloch.ker_ev`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L154).

> The kernel of Fourier evaluation is exactly the span defining the momentum fiber.

```lean
lemma ker_ev (χ : AddChar Λ K) :
    LinearMap.ker (ev (M := M) χ)
      = cobound (translation (K := K) (Λ := Λ) (M := M)) (charFun χ)
```

**`CondensedMatter.Bloch.fiberEquiv`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L167).

> The momentum fiber of the translation action at `χ` is canonically the unit-cell space
> `M`.

```lean
noncomputable def fiberEquiv (χ : AddChar Λ K) :
    Fiber (translation (K := K) (Λ := Λ) (M := M)) (charFun χ) ≃ₗ[K] M
```

**`CondensedMatter.Bloch.fiberEquiv_mk`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L172).

```lean
lemma fiberEquiv_mk (χ : AddChar Λ K) (ψ : Λ →₀ M) :
    fiberEquiv χ (Fiber.mk (translation (K := K)) (charFun χ) ψ) = ev χ ψ
```

## C. Bloch matrices

**`CondensedMatter.Bloch.symbol`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L184).

> The Bloch matrix of a linear map `D` at the character `χ`: apply `D` to the unit cell at the
> origin and Fourier-evaluate.

```lean
noncomputable def symbol (χ : AddChar Λ K) (D : (Λ →₀ M) →ₗ[K] (Λ →₀ M)) :
    M →ₗ[K] M
```

**`CondensedMatter.Bloch.symbol_apply`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L188).

```lean
lemma symbol_apply (χ : AddChar Λ K) (D : (Λ →₀ M) →ₗ[K] (Λ →₀ M)) (v : M) :
    symbol χ D v = ev χ (D (Finsupp.single 0 v))
```

**`CondensedMatter.Bloch.ev_apply`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L193).

> **Bloch theorem.** Fourier evaluation intertwines a translation-equivariant linear map with
> its Bloch matrix.

```lean
lemma ev_apply {D : (Λ →₀ M) →ₗ[K] (Λ →₀ M)}
    (hD : IsEquivariant (translation (K := K)) (translation (K := K)) D)
    (χ : AddChar Λ K) (ψ : Λ →₀ M) : ev χ (D ψ) = symbol χ D (ev χ ψ)
```

**`CondensedMatter.Bloch.symbol_id`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L202).

> The Bloch matrix of the identity is the identity.

```lean
lemma symbol_id (χ : AddChar Λ K) :
    symbol χ (LinearMap.id : (Λ →₀ M) →ₗ[K] _) = .id
```

**`CondensedMatter.Bloch.symbol_comp`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L207).

> The Bloch matrix is multiplicative: only the left factor needs to be equivariant.

```lean
lemma symbol_comp {D₁ D₂ : (Λ →₀ M) →ₗ[K] (Λ →₀ M)}
    (h₁ : IsEquivariant (translation (K := K)) (translation (K := K)) D₁)
    (χ : AddChar Λ K) : symbol χ (D₁ ∘ₗ D₂) = symbol χ D₁ ∘ₗ symbol χ D₂
```

**`CondensedMatter.Bloch.symbol_add`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L216).

> The Bloch matrix is additive.

```lean
lemma symbol_add (χ : AddChar Λ K) (D₁ D₂ : (Λ →₀ M) →ₗ[K] (Λ →₀ M)) :
    symbol χ (D₁ + D₂) = symbol χ D₁ + symbol χ D₂
```

**`CondensedMatter.Bloch.isUnit_symbol`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L222).

> If an equivariant map is invertible by an equivariant map, its Bloch matrix is invertible a
> every momentum.

```lean
lemma isUnit_symbol {D E : (Λ →₀ M) →ₗ[K] (Λ →₀ M)}
    (hD : IsEquivariant (translation (K := K)) (translation (K := K)) D)
    (hE : IsEquivariant (translation (K := K)) (translation (K := K)) E)
    (h₁ : D ∘ₗ E = LinearMap.id) (h₂ : E ∘ₗ D = LinearMap.id) (χ : AddChar Λ K) :
    IsUnit (symbol χ D)
```

## D. Hopping operators

**`CondensedMatter.Bloch.hop`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L240).

> One hopping term: apply `Hn` in each cell, then translate by `n`.

```lean
noncomputable def hop (n : Λ) (Hn : M →ₗ[K] M) : (Λ →₀ M) →ₗ[K] (Λ →₀ M)
```

**`CondensedMatter.Bloch.hopping`**, a def, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L245).

> A finite-range hopping operator with hopping matrices `H n : M → M`:
> `(hopping H ψ) m = ∑ n, H n (ψ (m - n))`.

```lean
noncomputable def hopping (H : Λ →₀ (M →ₗ[K] M)) : (Λ →₀ M) →ₗ[K] (Λ →₀ M)
```

**`CondensedMatter.Bloch.isEquivariant_hop`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L248).

```lean
lemma isEquivariant_hop (n : Λ) (Hn : M →ₗ[K] M) :
    IsEquivariant (translation (K := K)) (translation (K := K)) (hop n Hn)
```

**`CondensedMatter.Bloch.isEquivariant_hopping`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L259).

```lean
lemma isEquivariant_hopping (H : Λ →₀ (M →ₗ[K] M)) :
    IsEquivariant (translation (K := K)) (translation (K := K)) (hopping H)
```

**`CondensedMatter.Bloch.symbol_hopping`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean#L266).

> **Bloch Hamiltonian.** The Bloch matrix of a hopping operator is `∑ n, χ n • H n`.

```lean
lemma symbol_hopping (χ : AddChar Λ K) (H : Λ →₀ (M →ₗ[K] M)) :
    symbol χ (hopping H) = H.sum fun n Hn => χ n • Hn
```

## Depends on

- [Crystal momentum sectors](../../probabilistictheory/representation/momentumsectors.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Algebraic.lean)
