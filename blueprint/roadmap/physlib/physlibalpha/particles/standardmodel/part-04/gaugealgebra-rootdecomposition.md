---
declaration: module
origin: cited
lean: StandardModel.star_expI_zpow, StandardModel.GaugeAlgebra.stdCoeff, StandardModel.GaugeAlgebra.eq_sum_stdCoeff, StandardModel.GaugeAlgebra.stdBasis_coord_apply, StandardModel.torusSU3Diag, StandardModel.torusSU2Diag, StandardModel.toSU3_inv_gaugeTorusGen, StandardModel.toSU2_inv_gaugeTorusGen
statement: formalized
proof: formalized
---

# The root decomposition of the gauge algebra

The module `PhyslibAlpha.Particles.StandardModel.GaugeAlgebra.RootDecomposition`, [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean): 55 declarations, 43 with a docstring.

## i. Overview

> The gauge torus acts on the gauge algebra by conjugation with a diagonal matrix, so it
> scales the matrix entry `(j, k)` of the `su(3)` and `su(2)` blocks by `d j * star (d k)`.
> Off the diagonal this makes the real and imaginary parts of an entry a rotating pair —
> the root directions, recorded by `rootIdx`, `rootEntry` and `rootWeight` — while the
> diagonal directions and the `u(1)` generator are fixed, and are recorded by `cartanIdx`,
> which is assembled from the Cartan indices `su3CartanId` and `su2CartanId` of the
> individual factors.
>
> This is the adjoint analogue of the weights carried by the matter representations, and
> is what the gauge sector's gauge weight decomposition is built from.
>
> Section E makes that last sentence a theorem. A gauge weight is a character of the torus,
> so the real Lie algebra carries no gauge weight decomposition of its own; but for any
> complex algebra receiving the dual adjoint action, `adjointDecomposition` decomposes the
> span of the resulting symbols, and its pieces are a single root line at each of the eight
> nonzero weights and the span of the four Cartan symbols at weight zero. That is the sense
> in which the root decomposition and the gauge weight decomposition of the adjoint are the
> same thing.

## ii. Key results

> - `rootIdx` : the four root directions of the adjoint
> - `rootWeight` : the gauge weight of each root direction
> - `rootEntry` : the matrix entry scaled by the torus along each root direction
> - `su3CartanId` : the Gell-Mann indices of the two Cartan directions of `su(3)`
> - `su2CartanId` : the Pauli index of the Cartan direction of `su(2)`
> - `cartanIdx` : the four weight-zero directions: the two `su(3)` Cartan generators, the `su(2)`
>   Cartan generator and the `u(1)` generator
> - `adjointDecomposition` : the root decomposition read as a gauge weight decomposition: the span of
>   the symbols of a coadjoint map, joined out of the twelve root and Cartan lines

## iv. References

> * None.

**`StandardModel.star_expI_zpow`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L68).

> Conjugation inverts a power of `expI`.

```lean
lemma star_expI_zpow (z : ℤ) : star ((expI : ℂ) ^ z) = (expI : ℂ) ^ (-z)
```

## A. The coordinates of the standard basis

**`StandardModel.GaugeAlgebra.stdCoeff`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L80).

> coords

```lean
noncomputable def stdCoeff (x : GaugeAlgebra) : Fin 8 ⊕ Fin 3 ⊕ Fin 1 → ℝ
```

**`StandardModel.GaugeAlgebra.eq_sum_stdCoeff`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L85).

```lean
lemma eq_sum_stdCoeff (x : GaugeAlgebra) : x = ∑ y, stdCoeff x y • stdBasis y
```

**`StandardModel.GaugeAlgebra.stdBasis_coord_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L107).

> The coordinate functionals of `stdBasis` read off a gauge-algebra element's matrix
> entries.

```lean
lemma stdBasis_coord_apply (y : GaugeAlgebra) (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    stdBasis.coord a y = stdCoeff y a
```

## B. The torus acts by conjugation with a diagonal matrix

**`StandardModel.torusSU3Diag`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L125).

> su3 diagonals of inverse torus gens

```lean
noncomputable def torusSU3Diag : Fin 4 → Fin 3 → ℂ
```

**`StandardModel.torusSU2Diag`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L129).

> su2

```lean
noncomputable def torusSU2Diag : Fin 4 → Fin 2 → ℂ
```

**`StandardModel.toSU3_inv_gaugeTorusGen`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L132).

```lean
lemma toSU3_inv_gaugeTorusGen (i : Fin 4) :
    ((GaugeGroupI.toSU3 (gaugeTorusGen i)⁻¹ : specialUnitaryGroup (Fin 3) ℂ) :
      Matrix (Fin 3) (Fin 3) ℂ) = Matrix.diagonal (torusSU3Diag i)
```

**`StandardModel.toSU2_inv_gaugeTorusGen`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L142).

```lean
lemma toSU2_inv_gaugeTorusGen (i : Fin 4) :
    ((GaugeGroupI.toSU2 (gaugeTorusGen i)⁻¹ : specialUnitaryGroup (Fin 2) ℂ) :
      Matrix (Fin 2) (Fin 2) ℂ) = Matrix.diagonal (torusSU2Diag i)
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU3Matrix_apply_diagonal`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L154).

```lean
lemma adjointMap_toSU3Matrix_apply_diagonal {g : GaugeGroupI} {d : Fin 3 → ℂ}
    (hg : ((GaugeGroupI.toSU3 g : specialUnitaryGroup (Fin 3) ℂ) :
      Matrix (Fin 3) (Fin 3) ℂ) = Matrix.diagonal d)
    (x : GaugeAlgebra) (j k : Fin 3) :
    (adjointMap g x).toSU3Matrix j k = d j * star (d k) * x.toSU3Matrix j k
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU2Matrix_apply_diagonal`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L163).

```lean
lemma adjointMap_toSU2Matrix_apply_diagonal {g : GaugeGroupI} {d : Fin 2 → ℂ}
    (hg : ((GaugeGroupI.toSU2 g : specialUnitaryGroup (Fin 2) ℂ) :
      Matrix (Fin 2) (Fin 2) ℂ) = Matrix.diagonal d)
    (x : GaugeAlgebra) (j k : Fin 2) :
    (adjointMap g x).toSU2Matrix j k = d j * star (d k) * x.toSU2Matrix j k
```

**`StandardModel.torusSU3Diag_mul_star`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L174).

```lean
lemma torusSU3Diag_mul_star (i : Fin 4) (j : Fin 3) :
    torusSU3Diag i j * star (torusSU3Diag i j) = 1
```

**`StandardModel.torusSU2Diag_mul_star`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L179).

```lean
lemma torusSU2Diag_mul_star (i : Fin 4) (j : Fin 2) :
    torusSU2Diag i j * star (torusSU2Diag i j) = 1
```

## C. An entrywise scaling rotates the real pair of coordinate functionals

**`StandardModel.GaugeAlgebra.dualMap_pair_of_entry`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L192).

```lean
lemma dualMap_pair_of_entry {g : GaugeGroupI} {e : GaugeAlgebra → ℂ}
    {φ₁ φ₂ : Module.Dual ℝ GaugeAlgebra} {z : ℂ}
    (h1 : ∀ x, φ₁ x = (e x).re) (h2 : ∀ x, φ₂ x = -(e x).im)
    (he : ∀ x, e (adjointMap g x) = star z * e x) :
    (adjointMap g).dualMap φ₁ = z.re • φ₁ - z.im • φ₂ ∧
      (adjointMap g).dualMap φ₂ = z.im • φ₁ + z.re • φ₂
```

## D. The root and Cartan directions of the adjoint

> The `su(3)` and `su(2)` blocks each contribute root directions — pairs of standard
> basis indices whose coordinate functionals are the real part and minus the imaginary
> part of one matrix entry — together with Cartan directions on which the torus acts
> trivially; the `u(1)` generator is also fixed.
>
> The Cartan directions are named one factor at a time first, by `su3CartanId` in the
> Gell-Mann indices and `su2CartanId` in the Pauli indices, and `cartanIdx` assembles those
> with the `u(1)` generator into the four weight-zero directions of the whole algebra. The
> factorwise names are the ones section F uses; they are reducible, so they behave exactly
> like the index literals they name.

**`StandardModel.GaugeAlgebra.rootIdx`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L225).

> The four root directions of the adjoint.

```lean
def rootIdx : Fin 4 → (Fin 8 ⊕ Fin 3 ⊕ Fin 1) × (Fin 8 ⊕ Fin 3 ⊕ Fin 1)
```

**`StandardModel.GaugeAlgebra.rootWeight`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L232).

> The gauge weight of each root direction.

```lean
def rootWeight : Fin 4 → GaugeWeight
```

**`StandardModel.GaugeAlgebra.rootEntry`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L239).

> The matrix entry scaled by the torus along each root direction.

```lean
def rootEntry : Fin 4 → GaugeAlgebra → ℂ
```

**`StandardModel.GaugeAlgebra.su3CartanId`**, an abbrev, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L246).

> The Gell-Mann indices of the two Cartan directions of `su(3)`.

```lean
abbrev su3CartanId : Fin 2 → Fin 8
```

**`StandardModel.GaugeAlgebra.su2CartanId`**, an abbrev, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L251).

> The Pauli index of the Cartan direction of `su(2)`.

```lean
abbrev su2CartanId : Fin 3
```

**`StandardModel.GaugeAlgebra.cartanIdx`**, a def, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L255).

> The four weight-zero directions: the two `su(3)` Cartan generators, the `su(2)`
> Cartan generator and the `u(1)` generator.

```lean
def cartanIdx : Fin 4 → (Fin 8 ⊕ Fin 3 ⊕ Fin 1)
```

**`StandardModel.GaugeAlgebra.coord_rootIdx_fst`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L261).

```lean
lemma coord_rootIdx_fst (r : Fin 4) (x : GaugeAlgebra) :
    stdBasis.coord (rootIdx r).1 x = (rootEntry r x).re
```

**`StandardModel.GaugeAlgebra.coord_rootIdx_snd`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L265).

```lean
lemma coord_rootIdx_snd (r : Fin 4) (x : GaugeAlgebra) :
    stdBasis.coord (rootIdx r).2 x = -(rootEntry r x).im
```

**`StandardModel.GaugeAlgebra.rootEntry_adjointMap`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L269).

```lean
lemma rootEntry_adjointMap (r : Fin 4) (i : Fin 4) (x : GaugeAlgebra) :
    rootEntry r (adjointMap (gaugeTorusGen i)⁻¹ x)
      = star ((expI : ℂ) ^ GaugeWeight.coord (rootWeight r) i) * rootEntry r x
```

**`StandardModel.GaugeAlgebra.dualMap_coord_cartanIdx`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L296).

```lean
lemma dualMap_coord_cartanIdx (c : Fin 4) (i : Fin 4) :
    (adjointMap (gaugeTorusGen i)⁻¹).dualMap (stdBasis.coord (cartanIdx c))
      = stdBasis.coord (cartanIdx c)
```

## E. The root decomposition as a gauge weight decomposition

> A gauge weight is a character of the torus, so the vectors carrying one are complex,
> whereas the gauge algebra is a real Lie algebra and `GaugeWeightDecomposition` asks for a
> complex algebra. The relation is therefore not a statement about `GaugeAlgebra`, which
> carries no gauge weight decomposition at all, but about any complex algebra receiving the
> dual adjoint action: a real-linear map `F` out of `Module.Dual ℝ GaugeAlgebra`
> intertwining the gauge action with the coadjoint one, which is how the field strength of
> the gauge sector meets the adjoint.
>
> For such an `F` the root data of section D is exactly a gauge weight decomposition of the
> span of the symbols. Each root contributes the two combinations `F φ₁ ± i F φ₂` of its
> paired coordinate symbols, of weights `± rootWeight r`, and each Cartan direction
> contributes its symbol, of weight zero; `exists_rootIdx_or_cartanIdx` says these twelve
> vectors are enough, and `adjointDecomposition` joins their lines one weight at a time.
>
> The pieces are the identification itself. `adjointDecomposition_piece_rootWeight` and
> `adjointDecomposition_piece_neg_rootWeight` give a single root line at each of the eight
> nonzero weights, and `adjointDecomposition_piece_zero` gives the span of the four Cartan
> symbols at weight zero: the root directions are the nonzero-weight pieces and the Cartan
> directions are the zero-weight piece.
>
> Section F gives the Gell-Mann and Pauli coordinates of the vectors `adjVec` that belong to one
> non-abelian factor.

**`StandardModel.GaugeAlgebra.real_smul_eq_complex_smul`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L351).

> A real scalar acts on a complex algebra through its complex image.

```lean
lemma real_smul_eq_complex_smul (r : ℝ) (b : B) : r • b = ((r : ℂ)) • b
```

**`StandardModel.GaugeAlgebra.IsCoadjointSymbol`**, a def, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L357).

> A coadjoint symbol map: a real-linear map from the dual of the gauge algebra into a
> complex algebra which intertwines the gauge action with the dual adjoint action. The
> field strength of the gauge sector is one such map.

```lean
def IsCoadjointSymbol (rep : Representation ℂ GaugeGroupI B)
    (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) : Prop
```

**`StandardModel.GaugeAlgebra.AdjIdx`**, an abbrev, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L364).

> The index type of the adjoint weight vectors: four positive roots, four negative
> roots and four Cartan directions.

```lean
abbrev AdjIdx : Type
```

**`StandardModel.GaugeAlgebra.adjWeight`**, a def, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L367).

> The gauge weight carried by each adjoint weight vector.

```lean
def adjWeight : AdjIdx → GaugeWeight
```

**`StandardModel.GaugeAlgebra.adjVec`**, a def, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L375).

> The weight vectors of the adjoint in the image of a coadjoint symbol map: for each
> root the two combinations of its paired coordinate symbols, and for each Cartan
> direction the symbol itself.

```lean
noncomputable def adjVec (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) : AdjIdx → B
```

**`StandardModel.GaugeAlgebra.adjWeight_eq_zero_iff`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L384).

> A weight vector carries zero gauge weight exactly when it is a Cartan direction; the
> eight root directions all carry a nonzero weight.

```lean
lemma adjWeight_eq_zero_iff (k : AdjIdx) :
    adjWeight k = 0 ↔ ∃ c : Fin 4, k = Sum.inr (Sum.inr c)
```

**`StandardModel.GaugeAlgebra.exists_rootIdx_or_cartanIdx`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L391).

> The root and Cartan directions exhaust the standard basis: every standard index is
> one of the two members of a root pair, or a Cartan index.

```lean
lemma exists_rootIdx_or_cartanIdx (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    (∃ r : Fin 4, a = (rootIdx r).1) ∨ (∃ r : Fin 4, a = (rootIdx r).2)
      ∨ ∃ c : Fin 4, a = cartanIdx c
```

**`StandardModel.GaugeAlgebra.rep_pair_add`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L398).

> The positive combination of a rotating pair of symbols is scaled by the rotation.

```lean
lemma rep_pair_add (hF : IsCoadjointSymbol rep F) (g : GaugeGroupI)
    (φ₁ φ₂ : Module.Dual ℝ GaugeAlgebra) (z : ℂ)
    (h1 : (adjointMap g⁻¹).dualMap φ₁ = z.re • φ₁ - z.im • φ₂)
    (h2 : (adjointMap g⁻¹).dualMap φ₂ = z.im • φ₁ + z.re • φ₂) :
    rep g (F φ₁ + Complex.I • F φ₂) = z • (F φ₁ + Complex.I • F φ₂)
```

**`StandardModel.GaugeAlgebra.rep_pair_sub`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L411).

> The negative combination of a rotating pair of symbols is scaled by the conjugate
> rotation.

```lean
lemma rep_pair_sub (hF : IsCoadjointSymbol rep F) (g : GaugeGroupI)
    (φ₁ φ₂ : Module.Dual ℝ GaugeAlgebra) (z : ℂ)
    (h1 : (adjointMap g⁻¹).dualMap φ₁ = z.re • φ₁ - z.im • φ₂)
    (h2 : (adjointMap g⁻¹).dualMap φ₂ = z.im • φ₁ + z.re • φ₂) :
    rep g (F φ₁ - Complex.I • F φ₂)
      = (starRingEnd ℂ z) • (F φ₁ - Complex.I • F φ₂)
```

**`StandardModel.GaugeAlgebra.rep_fixed`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L425).

> A symbol at a fixed coordinate functional is itself fixed.

```lean
lemma rep_fixed (hF : IsCoadjointSymbol rep F) (g : GaugeGroupI)
    (φ : Module.Dual ℝ GaugeAlgebra) (h1 : (adjointMap g⁻¹).dualMap φ = φ) :
    rep g (F φ) = F φ
```

**`StandardModel.GaugeAlgebra.rep_adjVec`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L432).

> Each adjoint weight vector is a simultaneous eigenvector of the four torus
> generators, at the character of its weight.

```lean
lemma rep_adjVec (hF : IsCoadjointSymbol rep F) (k : AdjIdx) (i : Fin 4) :
    rep (gaugeTorusGen i) (adjVec F k)
      = ((expI : ℂ) ^ GaugeWeight.coord (adjWeight k) i) • adjVec F k
```

**`StandardModel.GaugeAlgebra.symbol_rootIdx_fst`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L460).

> The first symbol of a root pair, recovered from the two weight vectors.

```lean
lemma symbol_rootIdx_fst (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) (r : Fin 4) :
    F (stdBasis.coord (rootIdx r).1)
      = (2 : ℂ)⁻¹ • (adjVec F (Sum.inl r) + adjVec F (Sum.inr (Sum.inl r)))
```

**`StandardModel.GaugeAlgebra.symbol_rootIdx_snd`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L470).

> The second symbol of a root pair, recovered from the two weight vectors.

```lean
lemma symbol_rootIdx_snd (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) (r : Fin 4) :
    F (stdBasis.coord (rootIdx r).2)
      = (-(Complex.I / 2)) • (adjVec F (Sum.inl r) - adjVec F (Sum.inr (Sum.inl r)))
```

**`StandardModel.GaugeAlgebra.symbol_mem_iSup`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L480).

> Every standard coordinate symbol lies in the join of the twelve weight lines.

```lean
lemma symbol_mem_iSup (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    F (stdBasis.coord a) ∈ ⨆ k : AdjIdx, Submodule.span ℂ {adjVec F k}
```

**`StandardModel.GaugeAlgebra.span_range_eq_iSup`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L493).

> The span of the symbols is the join of the twelve weight lines.

```lean
lemma span_range_eq_iSup (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) :
    Submodule.span ℂ (Set.range F) = ⨆ k : AdjIdx, Submodule.span ℂ {adjVec F k}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition`**, a def, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L513).

> The root decomposition read as a gauge weight decomposition: the span of the symbols
> of a coadjoint map, joined out of the twelve root and Cartan lines.

```lean
noncomputable def adjointDecomposition (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) :
    GaugeWeightDecomposition rep (Submodule.span ℂ (Set.range F))
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_supp`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L525).

> The gauge weights of the adjoint: the six `su(3)` roots, the two `su(2)` roots and
> the zero weight of the Cartan and `u(1)` directions. Every one of them has vanishing
> hypercharge.

```lean
lemma adjointDecomposition_supp (hmul : IsMulRep rep) (hF : IsCoadjointSymbol rep F) :
    (adjointDecomposition hmul hF).supp
      = {((2, -1, 0, 0) : GaugeWeight), (1, 1, 0, 0), (-1, 2, 0, 0), (0, 0, 2, 0),
        (-2, 1, 0, 0), (-1, -1, 0, 0), (1, -2, 0, 0), (0, 0, -2, 0), (0, 0, 0, 0)}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L534).

> The pieces of the decomposition: the weight-`w` piece is the join of the weight lines
> whose weight is `w`.

```lean
lemma adjointDecomposition_piece (hmul : IsMulRep rep) (hF : IsCoadjointSymbol rep F)
    (w : GaugeWeight) :
    (adjointDecomposition hmul hF).piece w
      = ⨆ k : AdjIdx, if w = adjWeight k then Submodule.span ℂ {adjVec F k} else ⊥
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece_rootWeight`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L540).

> The piece at a root weight is the line of that root alone.

```lean
lemma adjointDecomposition_piece_rootWeight (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) (r : Fin 4) :
    (adjointDecomposition hmul hF).piece (rootWeight r)
      = Submodule.span ℂ {adjVec F (Sum.inl r)}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece_neg_rootWeight`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L556).

> The piece at the opposite of a root weight is the line of the opposite root.

```lean
lemma adjointDecomposition_piece_neg_rootWeight (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) (r : Fin 4) :
    (adjointDecomposition hmul hF).piece (-(rootWeight r))
      = Submodule.span ℂ {adjVec F (Sum.inr (Sum.inl r))}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece_zero`**, a lemma, [line 575](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L575).

> The weight-zero piece is the span of the four Cartan symbols: the two `su(3)` Cartan
> generators, the `su(2)` Cartan generator and the `u(1)` generator.

```lean
lemma adjointDecomposition_piece_zero (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) :
    (adjointDecomposition hmul hF).piece 0
      = ⨆ c : Fin 4, Submodule.span ℂ {F (stdBasis.coord (cartanIdx c))}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece_eq_bot`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L588).

> Every weight outside the nine is absent from the adjoint.

```lean
lemma adjointDecomposition_piece_eq_bot (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) {w : GaugeWeight}
    (hw : w ∉ (adjointDecomposition hmul hF).supp) :
    (adjointDecomposition hmul hF).piece w = ⊥
```

## F. The weight coordinates of one factor

> The vectors `adjVec` that belong to the `su(3)` or the `su(2)` factor have Gell-Mann or Pauli
> coordinates `x₁ ± i x₂` on a root pair, and the Cartan coordinate itself on a Cartan
> direction. `su3WeightCoeff` and `su2WeightCoeff` record these coordinates, indexed by
> `su3WeightIdx` and `su2WeightIdx`. The lemmas `rootIdx_castSucc`, `cartanIdx_castSucc`,
> `rootIdx_three` and `cartanIdx_two` identify the root pairs and Cartan indices of one factor
> with those of the whole algebra.

**`StandardModel.GaugeAlgebra.su3WeightIdx`**, an abbrev, [line 613](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L613).

> The index type of the `su(3)` weight coordinates: three positive roots, three negative
> roots and two Cartan directions.

```lean
abbrev su3WeightIdx : Type
```

**`StandardModel.GaugeAlgebra.su3RootPair`**, a def, [line 616](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L616).

> The pairs of Gell-Mann indices making up the three root directions of `su(3)`.

```lean
def su3RootPair : Fin 3 → Fin 8 × Fin 8
```

**`StandardModel.GaugeAlgebra.rootIdx_castSucc`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L622).

> The `su(3)` root pairs are the first three root pairs of the whole gauge algebra.

```lean
lemma rootIdx_castSucc (r : Fin 3) :
    rootIdx r.castSucc = (Sum.inl (su3RootPair r).1, Sum.inl (su3RootPair r).2)
```

**`StandardModel.GaugeAlgebra.cartanIdx_castSucc`**, a lemma, [line 628](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L628).

> The `su(3)` Cartan indices are the first two Cartan indices of the whole gauge
> algebra.

```lean
lemma cartanIdx_castSucc (c : Fin 2) :
    cartanIdx c.castSucc.castSucc = Sum.inl (su3CartanId c)
```

**`StandardModel.GaugeAlgebra.su3WeightCoeff`**, a def, [line 634](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L634).

> The `su(3)` weight coordinates in Gell-Mann coordinates: `x₁ ± i x₂` on each root pair,
> and the Cartan coordinates themselves.

```lean
noncomputable def su3WeightCoeff : su3WeightIdx → Fin 8 → ℂ
```

**`StandardModel.GaugeAlgebra.su2WeightIdx`**, an abbrev, [line 643](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L643).

> The index type of the `su(2)` weight coordinates: the positive root, the negative root
> and the Cartan direction.

```lean
abbrev su2WeightIdx : Type
```

**`StandardModel.GaugeAlgebra.su2RootPair`**, a def, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L646).

> The pair of Pauli indices making up the root direction of `su(2)`.

```lean
def su2RootPair : Fin 3 × Fin 3
```

**`StandardModel.GaugeAlgebra.rootIdx_three`**, a lemma, [line 649](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L649).

> The `su(2)` root pair is the fourth root pair of the whole gauge algebra.

```lean
lemma rootIdx_three :
    rootIdx 3 = (Sum.inr (Sum.inl su2RootPair.1), Sum.inr (Sum.inl su2RootPair.2))
```

**`StandardModel.GaugeAlgebra.cartanIdx_two`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L653).

> The `su(2)` Cartan index is the third Cartan index of the whole gauge algebra.

```lean
lemma cartanIdx_two : cartanIdx 2 = Sum.inr (Sum.inl su2CartanId)
```

**`StandardModel.GaugeAlgebra.su2WeightCoeff`**, a def, [line 657](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L657).

> The `su(2)` weight coordinates in Pauli coordinates: `x₁ ± i x₂` on the root pair, and
> the Cartan coordinate itself.

```lean
noncomputable def su2WeightCoeff : su2WeightIdx → Fin 3 → ℂ
```

## Depends on

- [The standard basis of the gauge algebra](gaugealgebra-basis.md)
- [Gauge weight decompositions](gaugegroup-gaugeweight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean)
