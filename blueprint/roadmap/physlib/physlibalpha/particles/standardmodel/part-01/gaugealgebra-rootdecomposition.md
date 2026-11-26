---
declaration: module
origin: cited
lean: StandardModel.GaugeAlgebra.stdCoeff, StandardModel.GaugeAlgebra.eq_sum_stdCoeff, StandardModel.GaugeAlgebra.stdBasis_coord_apply, StandardModel.GaugeAlgebra.torusSU3Diag, StandardModel.GaugeAlgebra.torusSU2Diag, StandardModel.GaugeAlgebra.toSU3_inv_gaugeTorusGen, StandardModel.GaugeAlgebra.toSU2_inv_gaugeTorusGen, StandardModel.GaugeAlgebra.adjointMap_toSU3Matrix_apply_diagonal
statement: formalized
proof: formalized
---

# The root decomposition of the gauge algebra

The module `PhyslibAlpha.Particles.StandardModel.GaugeAlgebra.RootDecomposition`, [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean): 41 declarations, 41 with a docstring.

> The root and Cartan directions of the gauge algebra, read as a gauge weight decomposition.

## i. Overview

> The gauge torus acts on the gauge algebra by conjugation with a diagonal matrix, so it
> scales the matrix entry `(j, k)` of the `su(3)` and `su(2)` blocks by `d j * star (d k)`.
> Off the diagonal this makes the real and imaginary parts of an entry a rotating pair. These
> are the root directions, recorded by `rootIdx`, `rootEntry` and `rootWeight`. The diagonal
> directions and the `u(1)` generator are fixed, and are recorded by `cartanIdx`, which is
> assembled from the Cartan indices `su3CartanId` and `su2CartanId` of the individual factors.
>
> This is the adjoint analogue of the weights carried by the matter representations, and
> section E makes that a theorem. A gauge weight is a character of the torus, so the real Lie
> algebra carries no gauge weight decomposition of its own. But for any complex algebra receiving
> the dual adjoint action, `adjointDecomposition` decomposes the span of the resulting symbols,
> and its pieces are a single root line at each of the eight nonzero weights and the span of the
> four Cartan symbols at weight zero. In this sense the root decomposition and the gauge weight
> decomposition of the adjoint are the same thing.

## ii. Key results

> - `StandardModel.GaugeAlgebra.rootIdx` : the four root directions of the adjoint.
> - `StandardModel.GaugeAlgebra.rootWeight` : the gauge weight of each root direction.
> - `StandardModel.GaugeAlgebra.rootEntry` : the matrix entry scaled by the torus along each root
>   direction.
> - `StandardModel.GaugeAlgebra.cartanIdx` : the four weight-zero directions, the two `su(3)`
>   Cartan generators, the `su(2)` Cartan generator and the `u(1)` generator.
> - `StandardModel.GaugeAlgebra.adjointDecomposition` : the root decomposition read as a gauge
>   weight decomposition of the span of the symbols of a coadjoint map.
> - `StandardModel.GaugeAlgebra.adjointDecomposition_supp`,
>   `StandardModel.GaugeAlgebra.adjointDecomposition_piece_rootWeight`,
>   `StandardModel.GaugeAlgebra.adjointDecomposition_piece_zero` : its nine weights, a single root
>   line at each nonzero weight and the Cartan symbols at weight zero.

## iv. References

> * None.

## A. The coordinates of the standard basis

> The coordinates of an element of the gauge algebra in `stdBasis` are its Gell-Mann and Pauli
> coefficients and the real part of its `u(1)` component.

**`StandardModel.GaugeAlgebra.stdCoeff`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L79).

> The coordinates of an element of the gauge algebra in the standard basis `stdBasis`.

```lean
noncomputable def stdCoeff (x : GaugeAlgebra) : Fin 8 ⊕ Fin 3 ⊕ Fin 1 → ℝ
```

**`StandardModel.GaugeAlgebra.eq_sum_stdCoeff`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L86).

> An element of the gauge algebra is the sum of the standard basis weighted by its
> coordinates.

```lean
lemma eq_sum_stdCoeff (x : GaugeAlgebra) : x = ∑ y, stdCoeff x y • stdBasis y
```

**`StandardModel.GaugeAlgebra.stdBasis_coord_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L108).

> The coordinate functionals of `stdBasis` read off a gauge-algebra element's matrix
> entries.

```lean
lemma stdBasis_coord_apply (y : GaugeAlgebra) (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    stdBasis.coord a y = stdCoeff y a
```

## B. The torus acts by conjugation with a diagonal matrix

> The inverses of the four torus generators have diagonal `SU(3)` and `SU(2)` factors, so their
> adjoint action scales each matrix entry by a phase.

**`StandardModel.GaugeAlgebra.torusSU3Diag`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L127).

> The diagonals of the `SU(3)` factors of the inverses of the four torus generators.

```lean
noncomputable def torusSU3Diag : Fin 4 → Fin 3 → ℂ
```

**`StandardModel.GaugeAlgebra.torusSU2Diag`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L131).

> The diagonals of the `SU(2)` factors of the inverses of the four torus generators.

```lean
noncomputable def torusSU2Diag : Fin 4 → Fin 2 → ℂ
```

**`StandardModel.GaugeAlgebra.toSU3_inv_gaugeTorusGen`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L135).

> The `SU(3)` factor of the inverse of a torus generator is diagonal.

```lean
lemma toSU3_inv_gaugeTorusGen (i : Fin 4) :
    ((GaugeGroupI.toSU3 (gaugeTorusGen i)⁻¹ : specialUnitaryGroup (Fin 3) ℂ) :
      Matrix (Fin 3) (Fin 3) ℂ) = Matrix.diagonal (torusSU3Diag i)
```

**`StandardModel.GaugeAlgebra.toSU2_inv_gaugeTorusGen`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L146).

> The `SU(2)` factor of the inverse of a torus generator is diagonal.

```lean
lemma toSU2_inv_gaugeTorusGen (i : Fin 4) :
    ((GaugeGroupI.toSU2 (gaugeTorusGen i)⁻¹ : specialUnitaryGroup (Fin 2) ℂ) :
      Matrix (Fin 2) (Fin 2) ℂ) = Matrix.diagonal (torusSU2Diag i)
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU3Matrix_apply_diagonal`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L158).

> Conjugation by a diagonal colour factor `d` scales the entry `(j, k)` of the `su(3)`
> component by `d j * star (d k)`.

```lean
lemma adjointMap_toSU3Matrix_apply_diagonal {g : GaugeGroupI} {d : Fin 3 → ℂ}
    (hg : ((GaugeGroupI.toSU3 g : specialUnitaryGroup (Fin 3) ℂ) :
      Matrix (Fin 3) (Fin 3) ℂ) = Matrix.diagonal d)
    (x : GaugeAlgebra) (j k : Fin 3) :
    (adjointMap g x).toSU3Matrix j k = d j * star (d k) * x.toSU3Matrix j k
```

**`StandardModel.GaugeAlgebra.adjointMap_toSU2Matrix_apply_diagonal`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L169).

> Conjugation by a diagonal isospin factor `d` scales the entry `(j, k)` of the `su(2)`
> component by `d j * star (d k)`.

```lean
lemma adjointMap_toSU2Matrix_apply_diagonal {g : GaugeGroupI} {d : Fin 2 → ℂ}
    (hg : ((GaugeGroupI.toSU2 g : specialUnitaryGroup (Fin 2) ℂ) :
      Matrix (Fin 2) (Fin 2) ℂ) = Matrix.diagonal d)
    (x : GaugeAlgebra) (j k : Fin 2) :
    (adjointMap g x).toSU2Matrix j k = d j * star (d k) * x.toSU2Matrix j k
```

**`StandardModel.GaugeAlgebra.torusSU3Diag_mul_star`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L179).

> The diagonal entries of the `SU(3)` factors of the torus generators are phases.

```lean
lemma torusSU3Diag_mul_star (i : Fin 4) (j : Fin 3) :
    torusSU3Diag i j * star (torusSU3Diag i j) = 1
```

**`StandardModel.GaugeAlgebra.torusSU2Diag_mul_star`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L185).

> The diagonal entries of the `SU(2)` factors of the torus generators are phases.

```lean
lemma torusSU2Diag_mul_star (i : Fin 4) (j : Fin 2) :
    torusSU2Diag i j * star (torusSU2Diag i j) = 1
```

## C. An entrywise scaling rotates the real pair of coordinate functionals

**`StandardModel.GaugeAlgebra.dualMap_pair_of_entry`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L198).

> If an element scales a complex coordinate `e` by `star z`, its dual action rotates the
> pair of real functionals `re e` and `-im e` by `z`.

```lean
lemma dualMap_pair_of_entry {g : GaugeGroupI} {e : GaugeAlgebra → ℂ}
    {φ₁ φ₂ : Module.Dual ℝ GaugeAlgebra} {z : ℂ}
    (h1 : ∀ x, φ₁ x = (e x).re) (h2 : ∀ x, φ₂ x = -(e x).im)
    (he : ∀ x, e (adjointMap g x) = star z * e x) :
    (adjointMap g).dualMap φ₁ = z.re • φ₁ - z.im • φ₂ ∧
      (adjointMap g).dualMap φ₂ = z.im • φ₁ + z.re • φ₂
```

## D. The root and Cartan directions of the adjoint

> The `su(3)` and `su(2)` blocks each contribute root directions, pairs of standard basis
> indices whose coordinate functionals are the real part and minus the imaginary part of one
> matrix entry. They also contribute Cartan directions, on which the torus acts trivially, and
> the `u(1)` generator is fixed as well.
>
> The Cartan directions are named one factor at a time first, by `su3CartanId` in the
> Gell-Mann indices and `su2CartanId` in the Pauli indices, and `cartanIdx` assembles those
> with the `u(1)` generator into the four weight-zero directions of the whole algebra. The
> factorwise names are reducible, so they behave exactly like the index literals they name.

**`StandardModel.GaugeAlgebra.rootIdx`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L226).

> The four root directions of the adjoint.

```lean
def rootIdx : Fin 4 → (Fin 8 ⊕ Fin 3 ⊕ Fin 1) × (Fin 8 ⊕ Fin 3 ⊕ Fin 1)
```

**`StandardModel.GaugeAlgebra.rootWeight`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L233).

> The gauge weight of each root direction.

```lean
def rootWeight : Fin 4 → GaugeWeight
```

**`StandardModel.GaugeAlgebra.rootEntry`**, a def, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L240).

> The matrix entry scaled by the torus along each root direction.

```lean
def rootEntry : Fin 4 → GaugeAlgebra → ℂ
```

**`StandardModel.GaugeAlgebra.su3CartanId`**, an abbrev, [line 247](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L247).

> The Gell-Mann indices of the two Cartan directions of `su(3)`.

```lean
abbrev su3CartanId : Fin 2 → Fin 8
```

**`StandardModel.GaugeAlgebra.su2CartanId`**, an abbrev, [line 252](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L252).

> The Pauli index of the Cartan direction of `su(2)`.

```lean
abbrev su2CartanId : Fin 3
```

**`StandardModel.GaugeAlgebra.cartanIdx`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L256).

> The four weight-zero directions, the two `su(3)` Cartan generators, the `su(2)`
> Cartan generator and the `u(1)` generator.

```lean
def cartanIdx : Fin 4 → (Fin 8 ⊕ Fin 3 ⊕ Fin 1)
```

**`StandardModel.GaugeAlgebra.coord_rootIdx_fst`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L263).

> The first coordinate of a root pair is the real part of the root entry.

```lean
lemma coord_rootIdx_fst (r : Fin 4) (x : GaugeAlgebra) :
    stdBasis.coord (rootIdx r).1 x = (rootEntry r x).re
```

**`StandardModel.GaugeAlgebra.coord_rootIdx_snd`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L268).

> The second coordinate of a root pair is minus the imaginary part of the root entry.

```lean
lemma coord_rootIdx_snd (r : Fin 4) (x : GaugeAlgebra) :
    stdBasis.coord (rootIdx r).2 x = -(rootEntry r x).im
```

**`StandardModel.GaugeAlgebra.rootEntry_adjointMap`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L274).

> The inverse of a torus generator scales the root entry by the conjugate of the character
> of the root weight.

```lean
lemma rootEntry_adjointMap (r : Fin 4) (i : Fin 4) (x : GaugeAlgebra) :
    rootEntry r (adjointMap (gaugeTorusGen i)⁻¹ x)
      = star ((expI : ℂ) ^ GaugeWeight.coord (rootWeight r) i) * rootEntry r x
```

**`StandardModel.GaugeAlgebra.dualMap_coord_cartanIdx`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L302).

> The torus fixes the coordinate functional of each Cartan direction.

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
> dual adjoint action. That is a real-linear map `F` out of `Module.Dual ℝ GaugeAlgebra`
> intertwining the gauge action with the coadjoint one, which is how the field strength of
> the gauge sector meets the adjoint.
>
> For such an `F` the root data of section D is exactly a gauge weight decomposition of the
> span of the symbols. Each root contributes the two combinations `F φ₁ ± i F φ₂` of its
> paired coordinate symbols, of weights `± rootWeight r`, and each Cartan direction
> contributes its symbol, of weight zero. `exists_rootIdx_or_cartanIdx` says these twelve
> vectors are enough, and `adjointDecomposition` joins their lines one weight at a time.
>
> The pieces are the identification itself. `adjointDecomposition_piece_rootWeight` and
> `adjointDecomposition_piece_neg_rootWeight` give a single root line at each of the eight
> nonzero weights, and `adjointDecomposition_piece_zero` gives the span of the four Cartan
> symbols at weight zero. The root directions are the nonzero-weight pieces and the Cartan
> directions are the zero-weight piece.

**`StandardModel.GaugeAlgebra.IsCoadjointSymbol`**, a def, [line 352](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L352).

> A coadjoint symbol map, a real-linear map from the dual of the gauge algebra into a
> complex algebra which intertwines the gauge action with the dual adjoint action. The
> field strength of the gauge sector is one such map.

```lean
def IsCoadjointSymbol (rep : Representation ℂ GaugeGroupI B)
    (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) : Prop
```

**`StandardModel.GaugeAlgebra.AdjIdx`**, an abbrev, [line 359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L359).

> The index type of the adjoint weight vectors, four positive roots, four negative
> roots and four Cartan directions.

```lean
abbrev AdjIdx : Type
```

**`StandardModel.GaugeAlgebra.adjWeight`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L362).

> The gauge weight carried by each adjoint weight vector.

```lean
def adjWeight : AdjIdx → GaugeWeight
```

**`StandardModel.GaugeAlgebra.adjVec`**, a def, [line 370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L370).

> The weight vectors of the adjoint in the image of a coadjoint symbol map. For each root
> they are the two combinations of its paired coordinate symbols, and for each Cartan
> direction the symbol itself.

```lean
noncomputable def adjVec (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) : AdjIdx → B
```

**`StandardModel.GaugeAlgebra.exists_rootIdx_or_cartanIdx`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L379).

> The root and Cartan directions exhaust the standard basis. Every standard index is
> one of the two members of a root pair, or a Cartan index.

```lean
lemma exists_rootIdx_or_cartanIdx (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    (∃ r : Fin 4, a = (rootIdx r).1) ∨ (∃ r : Fin 4, a = (rootIdx r).2)
      ∨ ∃ c : Fin 4, a = cartanIdx c
```

**`StandardModel.GaugeAlgebra.rep_pair_add`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L386).

> The positive combination of a rotating pair of symbols is scaled by the rotation.

```lean
lemma rep_pair_add (hF : IsCoadjointSymbol rep F) (g : GaugeGroupI)
    (φ₁ φ₂ : Module.Dual ℝ GaugeAlgebra) (z : ℂ)
    (h1 : (adjointMap g⁻¹).dualMap φ₁ = z.re • φ₁ - z.im • φ₂)
    (h2 : (adjointMap g⁻¹).dualMap φ₂ = z.im • φ₁ + z.re • φ₂) :
    rep g (F φ₁ + Complex.I • F φ₂) = z • (F φ₁ + Complex.I • F φ₂)
```

**`StandardModel.GaugeAlgebra.rep_pair_sub`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L400).

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

**`StandardModel.GaugeAlgebra.rep_fixed`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L415).

> A symbol at a fixed coordinate functional is itself fixed.

```lean
lemma rep_fixed (hF : IsCoadjointSymbol rep F) (g : GaugeGroupI)
    (φ : Module.Dual ℝ GaugeAlgebra) (h1 : (adjointMap g⁻¹).dualMap φ = φ) :
    rep g (F φ) = F φ
```

**`StandardModel.GaugeAlgebra.rep_adjVec`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L422).

> Each adjoint weight vector is a simultaneous eigenvector of the four torus
> generators, at the character of its weight.

```lean
lemma rep_adjVec (hF : IsCoadjointSymbol rep F) (k : AdjIdx) (i : Fin 4) :
    rep (gaugeTorusGen i) (adjVec F k)
      = ((expI : ℂ) ^ GaugeWeight.coord (adjWeight k) i) • adjVec F k
```

**`StandardModel.GaugeAlgebra.symbol_rootIdx_fst`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L450).

> The first symbol of a root pair, recovered from the two weight vectors.

```lean
lemma symbol_rootIdx_fst (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) (r : Fin 4) :
    F (stdBasis.coord (rootIdx r).1)
      = (2 : ℂ)⁻¹ • (adjVec F (Sum.inl r) + adjVec F (Sum.inr (Sum.inl r)))
```

**`StandardModel.GaugeAlgebra.symbol_rootIdx_snd`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L460).

> The second symbol of a root pair, recovered from the two weight vectors.

```lean
lemma symbol_rootIdx_snd (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) (r : Fin 4) :
    F (stdBasis.coord (rootIdx r).2)
      = (-(Complex.I / 2)) • (adjVec F (Sum.inl r) - adjVec F (Sum.inr (Sum.inl r)))
```

**`StandardModel.GaugeAlgebra.symbol_mem_iSup`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L471).

> Every standard coordinate symbol lies in the join of the twelve weight lines.

```lean
lemma symbol_mem_iSup (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B)
    (a : Fin 8 ⊕ Fin 3 ⊕ Fin 1) :
    F (stdBasis.coord a) ∈ ⨆ k : AdjIdx, Submodule.span ℂ {adjVec F k}
```

**`StandardModel.GaugeAlgebra.span_range_eq_iSup`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L484).

> The span of the symbols is the join of the twelve weight lines.

```lean
lemma span_range_eq_iSup (F : Module.Dual ℝ GaugeAlgebra →ₗ[ℝ] B) :
    Submodule.span ℂ (Set.range F) = ⨆ k : AdjIdx, Submodule.span ℂ {adjVec F k}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition`**, a def, [line 504](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L504).

> The root decomposition read as a gauge weight decomposition. The span of the symbols
> of a coadjoint map is joined out of the twelve root and Cartan lines.

```lean
noncomputable def adjointDecomposition (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) :
    GaugeWeightDecomposition rep (Submodule.span ℂ (Set.range F))
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_supp`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L516).

> The gauge weights of the adjoint are the six `su(3)` roots, the two `su(2)` roots and
> the zero weight of the Cartan and `u(1)` directions. Every one of them has vanishing
> hypercharge.

```lean
lemma adjointDecomposition_supp (hmul : IsMulRep rep) (hF : IsCoadjointSymbol rep F) :
    (adjointDecomposition hmul hF).supp
      = {((2, -1, 0, 0) : GaugeWeight), (1, 1, 0, 0), (-1, 2, 0, 0), (0, 0, 2, 0),
        (-2, 1, 0, 0), (-1, -1, 0, 0), (1, -2, 0, 0), (0, 0, -2, 0), (0, 0, 0, 0)}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L525).

> The weight-`w` piece of the decomposition is the join of the weight lines whose weight
> is `w`.

```lean
lemma adjointDecomposition_piece (hmul : IsMulRep rep) (hF : IsCoadjointSymbol rep F)
    (w : GaugeWeight) :
    (adjointDecomposition hmul hF).piece w
      = ⨆ k : AdjIdx, if w = adjWeight k then Submodule.span ℂ {adjVec F k} else ⊥
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece_rootWeight`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L531).

> The piece at a root weight is the line of that root alone.

```lean
lemma adjointDecomposition_piece_rootWeight (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) (r : Fin 4) :
    (adjointDecomposition hmul hF).piece (rootWeight r)
      = Submodule.span ℂ {adjVec F (Sum.inl r)}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece_neg_rootWeight`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L547).

> The piece at the opposite of a root weight is the line of the opposite root.

```lean
lemma adjointDecomposition_piece_neg_rootWeight (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) (r : Fin 4) :
    (adjointDecomposition hmul hF).piece (-(rootWeight r))
      = Submodule.span ℂ {adjVec F (Sum.inr (Sum.inl r))}
```

**`StandardModel.GaugeAlgebra.adjointDecomposition_piece_zero`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean#L566).

> The weight-zero piece is the span of the four Cartan symbols, of the two `su(3)` Cartan
> generators, the `su(2)` Cartan generator and the `u(1)` generator.

```lean
lemma adjointDecomposition_piece_zero (hmul : IsMulRep rep)
    (hF : IsCoadjointSymbol rep F) :
    (adjointDecomposition hmul hF).piece 0
      = ⨆ c : Fin 4, Submodule.span ℂ {F (stdBasis.coord (cartanIdx c))}
```

## Depends on

- [The standard basis of the gauge algebra](gaugealgebra-basis.md)
- [Gauge weight decompositions](../part-02/gaugegroup-gaugeweight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeAlgebra/RootDecomposition.lean)
