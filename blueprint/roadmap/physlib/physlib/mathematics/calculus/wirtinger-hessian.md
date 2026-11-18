---
declaration: module
origin: cited
lean: Physlib.Wirtinger.hessianMatrixOf, Physlib.Wirtinger.hessianMatrixOfR, Physlib.Wirtinger.hessianMatrixOfR_isHermitian, Physlib.Wirtinger.restrict, Physlib.Wirtinger.restrict_apply, Physlib.Wirtinger.restrict_single_same, Physlib.Wirtinger.restrict_single_ne, Physlib.Wirtinger.dWirtingerCoord_block_own
statement: formalized
proof: formalized
---

# The mixed Wirtinger Hessian

The module `Physlib.Mathematics.Calculus.Wirtinger.Hessian`, [Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean): 22 declarations, 19 with a docstring; 1 private, not shown.

> The mixed Wirtinger Hessian, and its block-diagonal form for a sum of sector functions.

## i. Overview

> In an `N = 1` supersymmetric theory the kinetic terms of the complex scalar fields `φ^I` are
> weighted by the Kähler metric
>
>   `g_{IJ̄}(φ) = ∂_I ∂̄_J K(φ)`,   `∂_I = ∂/∂φ^I`,   `∂̄_J = ∂/∂φ̄^J`,
>
> of the real Kähler potential `K`. The metric is Hermitian, `(g_{JĪ})^* = g_{IJ̄}`, so the kinetic
> term is real.
>
> Suppose the fields split into sectors `k`, with fields `φ_k = (φ_k^a)` in sector `k`, and the
> Kähler potential is a sum of sector potentials with no term mixing two sectors:
>
>   `K(φ) = ∑_k K_k(φ_k)`,
>
> as for several moduli `T_k` with `K = -∑_k n_k log(T_k + T̄_k)` and positive constants `n_k`.
> Then the metric is block-diagonal and the sectors have no kinetic mixing:
>
>   `∂²K / ∂φ_k^a ∂φ̄_l^b = δ_{kl} ∂²K_k / ∂φ_k^a ∂φ̄_k^b`.
>
> Each `K_k` need only be `C²` at the point considered, so potentials defined on a proper
> subdomain, such as `log`, are covered.
>
> In Lean, the fields of sector `k` are labelled by a finite type `ι k`, and the field `φ_k^a`
> by the pair `⟨k, a⟩ : Σ k, ι k`. A point `φ` in field space is a function
> `q : (Σ k, ι k) → ℂ` with `q ⟨k, a⟩ = φ_k^a`, and the sector fields `φ_k` are
> `q ∘ Sigma.mk k`, the function `a ↦ q ⟨k, a⟩`. The sector potentials `K_k` are `f k`. The
> metric `g_{IJ̄}(φ)` is `hessianMatrixOfR K q`, or `hessianMatrixOf` for a complex-valued
> function. At a point `u`, the block-diagonal statement reads
>
>   `hessianMatrixOf (fun q => ∑ k, f k (q ∘ Sigma.mk k)) u`
>   `  = blockDiagonal' (fun k => hessianMatrixOf (f k) (u ∘ Sigma.mk k))`.
>
> The two-sector case over `ι₁ ⊕ ι₂` is stated with `Matrix.fromBlocks`.

## ii. Key results

> - `Physlib.Wirtinger.hessianMatrixOf` : the mixed Wirtinger Hessian.
> - `Physlib.Wirtinger.hessianMatrixOfR` : the same for a real-valued function.
> - `Physlib.Wirtinger.hessianMatrixOfR_isHermitian` : the Hessian of a real `C²` function is
>     Hermitian.
> - `Physlib.Wirtinger.dWirtingerAntiCoord_block_sum` : `∂̄` of a sum of sector functions along a
>     sector-`k` coordinate is the `∂̄` of the sector-`k` function; `dWirtingerCoord_block_sum` is
>     the same for `∂`.
> - `Physlib.Wirtinger.hessianMatrixOf_sum_eq_blockDiagonal'` : the Hessian of a sum of sector
>     functions is block-diagonal.
> - `Physlib.Wirtinger.hessianMatrixOf_comp_equiv` : relabelling the coordinates by `ε` reindexes
>     the Hessian by `ε`.
> - `Physlib.Wirtinger.hessianMatrixOf_add_eq_fromBlocks` : the two-sector case, as
>     `Matrix.fromBlocks`.

## iv. References

> * None.

## A. The mixed Wirtinger Hessian

> For a real Kähler potential `K` the mixed Wirtinger Hessian is the Kähler metric `g_{IJ̄}`.
> Reality of `K` and Schwarz's theorem make it Hermitian.

**`Physlib.Wirtinger.hessianMatrixOf`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L97).

> The mixed Wirtinger Hessian of `f` at `u`: the matrix with `(I, J)` entry `∂_I ∂̄_J f`.

```lean
noncomputable def hessianMatrixOf (f : (ι → ℂ) → ℂ) (u : ι → ℂ) : Matrix ι ι ℂ
```

**`Physlib.Wirtinger.hessianMatrixOfR`**, an abbrev, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L102).

> The mixed Wirtinger Hessian of a real-valued `K`, through `Complex.ofReal`. An `abbrev`, so
> lemmas about `hessianMatrixOf` apply to it.

```lean
noncomputable abbrev hessianMatrixOfR (K : (ι → ℂ) → ℝ) (u : ι → ℂ) : Matrix ι ι ℂ
```

**`Physlib.Wirtinger.hessianMatrixOfR_isHermitian`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L107).

> The mixed Wirtinger Hessian of a real function `C²` at `u` is Hermitian,
> `(g_{JĪ})^* = g_{IJ̄}`.

```lean
lemma hessianMatrixOfR_isHermitian {K : (ι → ℂ) → ℝ} {u : ι → ℂ} (hK : ContDiffAt ℝ 2 K u) :
    Matrix.IsHermitian (hessianMatrixOfR K u)
```

## B. Block-diagonal Hessian of a sum over sectors

> The fields are labelled by `Σ k, ι k`, with `ι k` labelling the fields of sector `k`. A potential
> that is a sum of sector potentials has a block-diagonal Hessian.

**`Physlib.Wirtinger.restrict`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L140).

> The restriction `q ↦ q ∘ Sigma.mk k` to sector `k`, as a continuous ℝ-linear map.

```lean
noncomputable def restrict (k : K) : ((Σ k, ι k) → ℂ) →L[ℝ] (ι k → ℂ)
```

**`Physlib.Wirtinger.restrict_apply`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L144).

```lean
lemma restrict_apply (k : K) (q : (Σ k, ι k) → ℂ) : restrict k q = q ∘ Sigma.mk k
```

**`Physlib.Wirtinger.restrict_single_same`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L148).

> `restrict k` sends the basis vector of field `⟨k, a'⟩` to the basis vector of field `a'`.

```lean
lemma restrict_single_same (k : K) (a' : ι k) (z : ℂ) :
    restrict k (Pi.single (⟨k, a'⟩ : Σ k, ι k) z) = Pi.single a' z
```

**`Physlib.Wirtinger.restrict_single_ne`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L156).

> `restrict k` sends the basis vector of a field of another sector to zero.

```lean
lemma restrict_single_ne {k k' : K} (h : k ≠ k') (a' : ι k') (z : ℂ) :
    restrict k (Pi.single (⟨k', a'⟩ : Σ k, ι k) z) = 0
```

**`Physlib.Wirtinger.dWirtingerCoord_block_own`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L163).

> `∂_⟨k, a⟩` of a function of sector `k` alone is its `∂_a`.

```lean
lemma dWirtingerCoord_block_own {k : K} (g : (ι k → ℂ) → ℂ) (a : ι k)
    (u : (Σ k, ι k) → ℂ) (hg : DifferentiableAt ℝ g (u ∘ Sigma.mk k)) :
    dWirtingerCoord (fun q => g (q ∘ Sigma.mk k)) (⟨k, a⟩ : Σ k, ι k) u
      = dWirtingerCoord g a (u ∘ Sigma.mk k)
```

**`Physlib.Wirtinger.dWirtingerCoord_block_ne`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L171).

> `∂_⟨k, a⟩` of a function of another sector vanishes.

```lean
lemma dWirtingerCoord_block_ne {k k' : K} (h : k ≠ k') (g : (ι k' → ℂ) → ℂ) (a : ι k)
    (u : (Σ k, ι k) → ℂ) (hg : DifferentiableAt ℝ g (u ∘ Sigma.mk k')) :
    dWirtingerCoord (fun q => g (q ∘ Sigma.mk k')) (⟨k, a⟩ : Σ k, ι k) u = 0
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_block_own`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L178).

> Anti-holomorphic mirror of `dWirtingerCoord_block_own`.

```lean
lemma dWirtingerAntiCoord_block_own {k : K} (g : (ι k → ℂ) → ℂ) (a : ι k)
    (u : (Σ k, ι k) → ℂ) (hg : DifferentiableAt ℝ g (u ∘ Sigma.mk k)) :
    dWirtingerAntiCoord (fun q => g (q ∘ Sigma.mk k)) (⟨k, a⟩ : Σ k, ι k) u
      = dWirtingerAntiCoord g a (u ∘ Sigma.mk k)
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_block_ne`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L186).

> Anti-holomorphic mirror of `dWirtingerCoord_block_ne`.

```lean
lemma dWirtingerAntiCoord_block_ne {k k' : K} (h : k ≠ k') (g : (ι k' → ℂ) → ℂ) (a : ι k)
    (u : (Σ k, ι k) → ℂ) (hg : DifferentiableAt ℝ g (u ∘ Sigma.mk k')) :
    dWirtingerAntiCoord (fun q => g (q ∘ Sigma.mk k')) (⟨k, a⟩ : Σ k, ι k) u = 0
```

**`Physlib.Wirtinger.dWirtingerCoord_block_sum`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L193).

> `∂_⟨k₀, a⟩` of a sum of sector functions is the `∂_a` of the sector-`k₀` function.

```lean
lemma dWirtingerCoord_block_sum (f : ∀ k, (ι k → ℂ) → ℂ) (k₀ : K) (a : ι k₀)
    (u : (Σ k, ι k) → ℂ) (hf : ∀ k, DifferentiableAt ℝ (f k) (u ∘ Sigma.mk k)) :
    dWirtingerCoord (fun q => ∑ k, f k (q ∘ Sigma.mk k)) ⟨k₀, a⟩ u
      = dWirtingerCoord (f k₀) a (u ∘ Sigma.mk k₀)
```

**`Physlib.Wirtinger.dWirtingerAntiCoord_block_sum`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L205).

> `∂̄_⟨k₀, a⟩` of a sum of sector functions is the `∂̄_a` of the sector-`k₀` function.

```lean
lemma dWirtingerAntiCoord_block_sum (f : ∀ k, (ι k → ℂ) → ℂ) (k₀ : K) (a : ι k₀)
    (u : (Σ k, ι k) → ℂ) (hf : ∀ k, DifferentiableAt ℝ (f k) (u ∘ Sigma.mk k)) :
    dWirtingerAntiCoord (fun q => ∑ k, f k (q ∘ Sigma.mk k)) ⟨k₀, a⟩ u
      = dWirtingerAntiCoord (f k₀) a (u ∘ Sigma.mk k₀)
```

**`Physlib.Wirtinger.hessianMatrixOf_sum_eq_blockDiagonal'`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L218).

> The Hessian of a sum of sector functions is the block-diagonal matrix of the sector
> Hessians.

```lean
lemma hessianMatrixOf_sum_eq_blockDiagonal' (f : ∀ k, (ι k → ℂ) → ℂ) (u : (Σ k, ι k) → ℂ)
    (hf : ∀ k, ContDiffAt ℝ 2 (f k) (u ∘ Sigma.mk k)) :
    hessianMatrixOf (fun q => ∑ k, f k (q ∘ Sigma.mk k)) u
      = blockDiagonal' (fun k => hessianMatrixOf (f k) (u ∘ Sigma.mk k))
```

## C. Coordinate reindexing of the Hessian

> Relabelling the fields by a bijection `ε` permutes the rows and columns of the Hessian.

**`Physlib.Wirtinger.precompEquiv`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L257).

> The relabelling `q ↦ q ∘ ε.symm` along `ε`, as a continuous ℝ-linear map.

```lean
noncomputable def precompEquiv (ε : ι ≃ ι') : (ι → ℂ) →L[ℝ] (ι' → ℂ)
```

**`Physlib.Wirtinger.precompEquiv_single`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L266).

> `precompEquiv ε` sends the basis vector of field `c` to the basis vector of field `ε c`.

```lean
lemma precompEquiv_single (ε : ι ≃ ι') (c : ι) (z : ℂ) :
    precompEquiv ε (Pi.single c z) = Pi.single (ε c) z
```

**`Physlib.Wirtinger.hessianMatrixOf_comp_equiv`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L272).

> Relabelling the coordinates by `ε` reindexes the Hessian by `ε`.

```lean
lemma hessianMatrixOf_comp_equiv (ε : ι ≃ ι') (H : (ι' → ℂ) → ℂ) (u : ι → ℂ)
    (hH : ContDiffAt ℝ 2 H (u ∘ ε.symm)) :
    hessianMatrixOf (fun q => H (q ∘ ε.symm)) u
      = (hessianMatrixOf H (u ∘ ε.symm)).submatrix ε ε
```

## D. Two sectors

> Two sectors with fields indexed by `ι₁ ⊕ ι₂`, obtained from §B by relabelling with §C.

**`Physlib.Wirtinger.restrictInl`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L304).

> The restriction `q ↦ q ∘ Sum.inl` to the first sector, as a continuous ℝ-linear map.

```lean
noncomputable def restrictInl : (ι₁ ⊕ ι₂ → ℂ) →L[ℝ] (ι₁ → ℂ)
```

**`Physlib.Wirtinger.restrictInr`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L308).

> The restriction `q ↦ q ∘ Sum.inr` to the second sector, as a continuous ℝ-linear map.

```lean
noncomputable def restrictInr : (ι₁ ⊕ ι₂ → ℂ) →L[ℝ] (ι₂ → ℂ)
```

**`Physlib.Wirtinger.restrictInl_apply`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L312).

```lean
lemma restrictInl_apply (q : ι₁ ⊕ ι₂ → ℂ) :
    restrictInl (ι₁ := ι₁) (ι₂ := ι₂) q = q ∘ Sum.inl
```

**`Physlib.Wirtinger.restrictInr_apply`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L316).

```lean
lemma restrictInr_apply (q : ι₁ ⊕ ι₂ → ℂ) :
    restrictInr (ι₁ := ι₁) (ι₂ := ι₂) q = q ∘ Sum.inr
```

**`Physlib.Wirtinger.hessianMatrixOf_add_eq_fromBlocks`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean#L321).

> The Hessian of `f₁ (q ∘ Sum.inl) + f₂ (q ∘ Sum.inr)` is `fromBlocks` of the two sector
> Hessians.

```lean
lemma hessianMatrixOf_add_eq_fromBlocks
    (f₁ : (ι₁ → ℂ) → ℂ) (f₂ : (ι₂ → ℂ) → ℂ) (u : ι₁ ⊕ ι₂ → ℂ)
    (hf₁ : ContDiffAt ℝ 2 f₁ (u ∘ Sum.inl)) (hf₂ : ContDiffAt ℝ 2 f₂ (u ∘ Sum.inr)) :
    hessianMatrixOf (fun q => f₁ (q ∘ Sum.inl) + f₂ (q ∘ Sum.inr)) u
      = Matrix.fromBlocks (hessianMatrixOf f₁ (u ∘ Sum.inl)) 0 0
          (hessianMatrixOf f₂ (u ∘ Sum.inr))
```

## Depends on

- [Partial Wirtinger derivatives `∂_I`, `∂̄_I` in a complex coordinate basis on `ℂ^n`](wirtinger-coordinate.md)

## Sources

- [Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Wirtinger/Hessian.lean)
