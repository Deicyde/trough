---
declaration: module
origin: cited
lean: StandardModel.expI, StandardModel.expI_zpow_injective, StandardModel.expI_ne_zero, StandardModel.expI_inv_eq_star, StandardModel.expI_mul_conj, StandardModel.conj_mul_expI, Matrix.mem_specialUnitaryGroup_diagonal, StandardModel.su3ExpIOne
statement: formalized
proof: formalized
---

# Gauge weight decompositions

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.GaugeWeight`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean): 61 declarations, 49 with a docstring.

## i. Overview

> The operators that may appear in a Standard Model Lagrangian are those the gauge group leaves
> fixed, and finding them means searching a large space of composite operators.
>
> The maximal torus of the gauge group is four-dimensional, and a **gauge weight** is the
> quadruple of charges
>
>   `(colour₁, colour₂, isospin, hypercharge) : ℤ × ℤ × ℤ × ℤ`,
>
> recording how a vector scales under four chosen elements of it. Two count colour, one counts
> weak isospin normalized as `2T₃`, and one counts hypercharge normalized as `6Y`. A **gauge
> weight decomposition** of a submodule `V` presents it as a finitely supported family of
> subspaces on each of which those four elements act by one such character.
>
> Carrying all four charges at once costs nothing, since the four elements commute. They lie in
> different factors of the product group, and the two colour elements are both diagonal, so the
> four gradings are simultaneously realizable. An invariant operator is fixed by the whole gauge
> group, so in particular by these four elements, so it carries zero weight and the search can
> be confined to the zero-weight piece.
>
> In the adjoint representation this grading is the root decomposition of the gauge algebra.
> That identification cannot be made here, since the file recording the root data imports
> this one; it is `GaugeAlgebra.adjointDecomposition` in
> `PhyslibAlpha.Particles.StandardModel.GaugeAlgebra.RootDecomposition`.

## ii. Key results

> - `gaugeTorusGen` : the four commuting torus generators.
> - `GaugeWeight` : the quadruple of charges measured against them.
> - `GaugeWeightDecomposition` : a finitely supported family of pure-weight subspaces with
>   supremum `V`.
> - `GaugeWeightDecomposition.sup` : decompositions combine one weight at a time along
>   `V ⊔ V'`.
> - `GaugeWeightDecomposition.mul` : weights add under multiplication, decomposing `V * V'`.
> - `GaugeWeightDecomposition.piece_eq_inf` : the pieces are cut out of `V` by the torus alone.
> - `GaugeWeightDecomposition.mem_zero_of_invariant` : a gauge-invariant element lies in the
>   zero-weight piece.
> - `GaugeWeightDecomposition.reducesInvariantsTo_piece_zero` : modulo a torus-stable
>   submodule `S`, an element fixed by the four torus generators lies in the zero-weight
>   piece; `mem_piece_zero_sup_of_invariant` is the unfolded form.

## iv. References

> * None.

## A. The scalar `exp i` and the torus generators

> Every charge here is measured by one scalar. The unit complex number `exp i` has infinite
> order, since `π` is irrational, so its integer powers are pairwise distinct and a single
> element of the torus already separates all the weights in a given direction.
>
> The torus generators are built by placing `exp i` and its inverse on a diagonal. The maximal
> torus of `SU(3)` is two-dimensional, so colour is a two-component charge and needs the two
> elements `diag (exp i, exp (-i), 1)` and `diag (1, exp i, exp (-i))`. Weak isospin needs one,
> `diag (exp i, exp (-i))`. Each lies in its special unitary group because the diagonal entries
> have modulus one and multiply to one. Hypercharge needs no matrix, since its factor of the
> gauge group is already the unit circle.
>
> The generators are elements of the group, and the purity of a weight space is recorded by a
> character equation `rep g x = c • x`.

**`StandardModel.expI`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L101).

> The unitary scalar `exp i`, a point of the unit circle of infinite order.

```lean
noncomputable def expI : unitary ℂ
```

**`StandardModel.expI_zpow_injective`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L112).

> The powers of `exp i` are pairwise distinct, by the irrationality of `π`.

```lean
lemma expI_zpow_injective : Function.Injective fun n : ℤ => ((expI : ℂ) ^ n)
```

**`StandardModel.expI_ne_zero`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L135).

> `exp i` is nonzero.

```lean
lemma expI_ne_zero : ((expI : ℂ)) ≠ 0
```

**`StandardModel.expI_inv_eq_star`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L141).

> The inverse of `exp i` is its star.

```lean
lemma expI_inv_eq_star : ((expI : ℂ))⁻¹ = star (expI : ℂ)
```

**`StandardModel.expI_mul_conj`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L145).

> `exp i` times its conjugate is one.

```lean
lemma expI_mul_conj : (expI : ℂ) * (starRingEnd ℂ) (expI : ℂ) = 1
```

**`StandardModel.conj_mul_expI`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L149).

> The conjugate of `exp i` times `exp i` is one.

```lean
lemma conj_mul_expI : (starRingEnd ℂ) (expI : ℂ) * (expI : ℂ) = 1
```

**`Matrix.mem_specialUnitaryGroup_diagonal`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L154).

> A diagonal matrix whose entries are unit scalars with product one lies in the special
> unitary group.

```lean
lemma _root_.Matrix.mem_specialUnitaryGroup_diagonal {n : Type*} [Fintype n] [DecidableEq n]
    (d : n → ℂ) (hd : ∀ i, d i * star (d i) = 1) (hdet : ∏ i, d i = 1) :
    Matrix.diagonal d ∈ Matrix.specialUnitaryGroup n ℂ
```

**`StandardModel.su3ExpIOne`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L166).

> The first colour torus generator, `diag (exp i, exp (-i), 1)`.

```lean
noncomputable def su3ExpIOne : specialUnitaryGroup (Fin 3) ℂ
```

**`StandardModel.su3ExpITwo`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L173).

> The second colour torus generator, `diag (1, exp i, exp (-i))`.

```lean
noncomputable def su3ExpITwo : specialUnitaryGroup (Fin 3) ℂ
```

**`StandardModel.su2ExpI`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L180).

> The `SU(2)` torus element, `diag (exp i, exp (-i))`.

```lean
noncomputable def su2ExpI : specialUnitaryGroup (Fin 2) ℂ
```

**`StandardModel.su2ExpI_coe`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L187).

> The underlying matrix of the `SU(2)` torus element.

```lean
lemma su2ExpI_coe :
    (su2ExpI : specialUnitaryGroup (Fin 2) ℂ).1
      = !![(expI : ℂ), 0; 0, star (expI : ℂ)]
```

**`StandardModel.su2ExpI_inv_coe`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L195).

> The inverse torus element is `diag (exp (-i), exp i)`, so on a doublet the two components
> are scaled by the reciprocal characters.

```lean
lemma su2ExpI_inv_coe :
    (su2ExpI⁻¹ : specialUnitaryGroup (Fin 2) ℂ).1
      = !![star (expI : ℂ), 0; 0, (expI : ℂ)]
```

## B. The four torus generators and gauge weights

> Weights are measured against four chosen elements of the maximal torus, one element per
> direction, collected in `gaugeTorusGen`. Four suffice because of the separation in section A.
>
> Both abelian charges are normalized to integers. Weak isospin is measured as `2T₃`, so the two
> components of a doublet carry weights `+1` and `-1`, and hypercharge as `6Y`, the smallest
> rescaling under which every Standard Model hypercharge is an integer, the quark doublet at `Y = 1/6`
> becoming `6Y = 1`. Integrality is what allows every eigenvalue here to be an integer power
> `(exp i) ^ k` of one scalar.
>
> `GaugeWeight.coord` reads a weight at a given generator. It is additive, which is why charges
> add when operators are multiplied, and injective, so a weight can be recovered from the four
> characters by which the torus acts.

**`StandardModel.gaugeTorusGen`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L220).

> The four commuting generators of the maximal torus of the gauge group.

```lean
noncomputable def gaugeTorusGen : Fin 4 → GaugeGroupI
```

**`StandardModel.GaugeWeight`**, an abbrev, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L225).

> A **gauge weight**, the four exponents `(colour₁, colour₂, isospin, hypercharge)`
> recording how a vector scales under `gaugeTorusGen`.

```lean
abbrev GaugeWeight : Type
```

**`StandardModel.GaugeWeight.coord`**, a def, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L228).

> The exponent of a gauge weight against the `i`-th torus generator.

```lean
def GaugeWeight.coord (w : GaugeWeight) : Fin 4 → ℤ
```

**`StandardModel.GaugeWeight.coord_zero`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L231).

> The exponent at the first colour generator.

```lean
lemma GaugeWeight.coord_zero (w : GaugeWeight) : w.coord 0 = w.1
```

**`StandardModel.GaugeWeight.coord_one`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L234).

> The exponent at the second colour generator.

```lean
lemma GaugeWeight.coord_one (w : GaugeWeight) : w.coord 1 = w.2.1
```

**`StandardModel.GaugeWeight.coord_two`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L237).

> The exponent at the isospin generator, normalized as `2T₃`.

```lean
lemma GaugeWeight.coord_two (w : GaugeWeight) : w.coord 2 = w.2.2.1
```

**`StandardModel.GaugeWeight.coord_three`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L240).

> The exponent at the hypercharge generator, normalized as `6Y`.

```lean
lemma GaugeWeight.coord_three (w : GaugeWeight) : w.coord 3 = w.2.2.2
```

**`StandardModel.GaugeWeight.coord_neg`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L243).

> The zero gauge weight has vanishing exponent against every torus generator.

```lean
lemma GaugeWeight.coord_neg (w : GaugeWeight) (i : Fin 4) :
    (-w).coord i = -(w.coord i)
```

**`StandardModel.GaugeWeight.zero_coord`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L247).

```lean
lemma GaugeWeight.zero_coord (i : Fin 4) : (0 : GaugeWeight).coord i = 0
```

**`StandardModel.GaugeWeight.coord_add`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L252).

> Weights add coordinatewise. With `zero_coord` this says `coord` is additive, which is
> what makes gauge weights add under multiplication.

```lean
lemma GaugeWeight.coord_add (w w' : GaugeWeight) (i : Fin 4) :
    (w + w').coord i = w.coord i + w'.coord i
```

**`StandardModel.GaugeWeight.coord_injective`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L258).

> A gauge weight is determined by its four exponents. This is what lets a weight be
> recovered from the characters by which the torus acts; see `piece_eq_inf`.

```lean
lemma GaugeWeight.coord_injective : Function.Injective GaugeWeight.coord
```

## C. Gauge weight decompositions

> A gauge weight decomposition is the weight-space decomposition of a representation, with two
> differences. It is recorded rather than derived, since the submodules of interest are spans of
> explicitly given operators whose charges are read off directly, and it is required only to
> cover `V`. Independence of the pieces is not part of the data, because it is automatic, as
> section F shows.
>
> Multiplicativity of the representation is named by `IsMulRep` and stored in the `rep_mul`
> field, so that a decomposition of a product can be assembled from decompositions of the factors
> with no further input. `copy` moves a decomposition across an equality of submodules, needed
> because a submodule arising in practice is usually only propositionally the one for which a
> decomposition was recorded.

**`StandardModel.IsMulRep`**, an abbrev, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L292).

> A representation acts by algebra maps, respecting multiplication. This is the
> hypothesis under which charges are additive.

```lean
abbrev IsMulRep (rep : Representation ℂ GaugeGroupI B) : Prop
```

**`StandardModel.IsMulRep.map_one`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L297).

> A representation that respects multiplication respects the unit, since `g` is invertible
> and so `rep g 1` is cancellable.

```lean
lemma IsMulRep.map_one {rep : Representation ℂ GaugeGroupI B} (hmul : IsMulRep rep)
    (g : GaugeGroupI) : rep g 1 = 1
```

## D. Powers of `expI` under conjugation

**`StandardModel.starRingEnd_expI_pow`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L309).

```lean
lemma starRingEnd_expI_pow (n : ℕ) :
    ((starRingEnd ℂ) (expI : ℂ)) ^ n = ((expI : ℂ) ^ n)⁻¹
```

**`StandardModel.starRingEnd_expI_zpow`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L314).

```lean
lemma starRingEnd_expI_zpow (z : ℤ) :
    (starRingEnd ℂ) ((expI : ℂ) ^ z) = (expI : ℂ) ^ (-z)
```

**`StandardModel.expI_zpow_ne_zero`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L321).

```lean
lemma expI_zpow_ne_zero (z : ℤ) : ((expI : ℂ) ^ z) ≠ 0
```

## E. The torus weights of the fundamental representations

> The colour and isospin weights of the fundamental representations of `SU(3)` and
> `SU(2)` against the torus generators.  They are the building blocks of the gauge
> weights of the matter representations.

**`StandardModel.colourWeight`**, a def, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L336).

> The colour weights of the fundamental of `SU(3)` against the two colour torus
> generators.

```lean
def colourWeight (c : Fin 3) : ℤ × ℤ
```

**`StandardModel.isoWeight`**, a def, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L340).

> The isospin weight of the fundamental of `SU(2)` against the isospin torus
> generator.

```lean
def isoWeight (s : Fin 2) : ℤ
```

## F. The torus action on dual and conjugate bases

> If the torus acts diagonally on a basis then it acts diagonally on the dual basis with
> the negated weights, and on the conjugate basis with the negated weights as well — so
> the conjugate-dual action carries the original weights back.

**`StandardModel.dual_gaugeTorusGen_coord`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L357).

```lean
lemma dual_gaugeTorusGen_coord (ρ : Representation ℂ GaugeGroupI V)
    (b : Module.Basis ι ℂ V) (g : GaugeGroupI) (w : ι → ℤ)
    (hb : ∀ j, ρ g (b j) = ((expI : ℂ) ^ w j) • b j) (j : ι) :
    ρ.dual g (b.coord j) = ((expI : ℂ) ^ (-(w j))) • b.coord j
```

**`StandardModel.conj_gaugeTorusGen_basis`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L379).

```lean
lemma conj_gaugeTorusGen_basis (ρ : Representation ℂ GaugeGroupI V)
    (b : Module.Basis ι ℂ V) (g : GaugeGroupI) (w : ι → ℤ)
    (hb : ∀ j, ρ g (b j) = ((expI : ℂ) ^ w j) • b j) (j : ι) :
    ρ.conj g (Basis.conj b j)
      = ((expI : ℂ) ^ (-(w j))) • Basis.conj b j
```

**`StandardModel.GaugeWeightDecomposition`**, a class, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L392).

> A **gauge weight decomposition** of a submodule `V`, a finitely supported family of
> subspaces of pure gauge weight whose supremum is `V`. Purity is recorded against the four
> commuting torus generators simultaneously.

```lean
class GaugeWeightDecomposition (rep : Representation ℂ GaugeGroupI B)
    (V : Submodule ℂ B) where
  /-- The piece of gauge weight `w`. -/
  piece : GaugeWeight → Submodule ℂ B
  /-- The finite set of gauge weights that occur. -/
  supp : Finset GaugeWeight
  /-- Gauge transformations act by algebra maps. -/
  rep_mul : IsMulRep rep
  /-- Each piece is of pure gauge weight, as seen by all four torus generators. -/
  piece_le : ∀ w, ∀ x, x ∈ piece w → ∀ i,
    rep (gaugeTorusGen i) x = ((expI : ℂ) ^ w.coord i) • x
  /-- Only the gauge weights in `supp` occur. -/
  piece_eq_bot : ∀ w ∉ supp, piece w = ⊥
  /-- The pieces exhaust `V`. -/
  iSup_piece : (⨆ w, piece w) = V
```

**`StandardModel.GaugeWeightDecomposition.piece_le_eigenspace`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L415).

> The weight-`w` piece lies in the eigenspace of the `i`-th torus generator at the
> eigenvalue `(exp i) ^ (w.coord i)`. This is `piece_le` phrased as an inequality of
> submodules.

```lean
lemma piece_le_eigenspace (d : GaugeWeightDecomposition rep V) (w : GaugeWeight) (i : Fin 4) :
    d.piece w ≤ Module.End.eigenspace (rep (gaugeTorusGen i)) ((expI : ℂ) ^ w.coord i)
```

**`StandardModel.GaugeWeightDecomposition.piece_eq_zero_of_not_mem_supp`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L421).

> A weight outside the support has vanishing piece. This is the `piece_eq_bot` field, in
> the form a `simp` set can use to discard the absent weights of a computed product.

```lean
lemma piece_eq_zero_of_not_mem_supp (d : GaugeWeightDecomposition rep V) (w : GaugeWeight)
    (hw : w ∉ d.supp) : d.piece w = ⊥
```

**`StandardModel.GaugeWeightDecomposition.piece_le_self`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L425).

> A weight piece lies inside the submodule it decomposes.

```lean
lemma piece_le_self (d : GaugeWeightDecomposition rep V) (w : GaugeWeight) :
    d.piece w ≤ V
```

**`StandardModel.GaugeWeightDecomposition.copy`**, a def, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L430).

> Transport a decomposition along an equality of submodules.

```lean
def copy (d : GaugeWeightDecomposition rep V) (W : Submodule ℂ B) (hW : W = V) :
    GaugeWeightDecomposition rep W
```

**`StandardModel.GaugeWeightDecomposition.copy_piece`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L440).

```lean
lemma copy_piece (d : GaugeWeightDecomposition rep V) (W : Submodule ℂ B) (hW : W = V) :
    (copy d W hW).piece = d.piece
```

## G. Joins

> If `V` and `V'` are decomposed then so is their join `V ⊔ V'`, one weight at a time. Its
> weight-`w` piece is the join of the two weight-`w` pieces, and its support is the union of the
> supports. A vector of the join need not have definite charge, but it is a sum of vectors that
> do, which is all a decomposition claims.
>
> The binary case `sup`, the empty case `bot`, a finite indexed family `iSup` and a join over a
> proposition `iSupProp` are all the same construction. Multiplicativity of `rep` is recovered
> from a summand where there is one and supplied as an argument where there is not, since `bot`
> decomposes the zero submodule and the indexed forms may range over an empty family.

**`StandardModel.GaugeWeightDecomposition.sup`**, an instance, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L460).

> The join of two gauge weight decompositions, decomposing `V ⊔ V'`. Pieces and supports
> combine one weight at a time.

```lean
noncomputable instance sup [d : GaugeWeightDecomposition rep V]
    [d' : GaugeWeightDecomposition rep V'] : GaugeWeightDecomposition rep (V ⊔ V')
```

**`StandardModel.GaugeWeightDecomposition.sup_piece`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L475).

```lean
lemma sup_piece [GaugeWeightDecomposition rep V] [GaugeWeightDecomposition rep V']
    (w : GaugeWeight) : piece rep (V ⊔ V') w = piece rep V w ⊔ piece rep V' w
```

**`StandardModel.GaugeWeightDecomposition.bot`**, a def, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L480).

> The zero submodule carries the empty decomposition.

```lean
def bot (hmul : IsMulRep rep) :
    GaugeWeightDecomposition rep (⊥ : Submodule ℂ B)
```

**`StandardModel.GaugeWeightDecomposition.bot_piece`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L493).

```lean
lemma bot_piece (hmul : IsMulRep rep)
    (w : GaugeWeight) : (bot hmul).piece w = ⊥
```

**`StandardModel.GaugeWeightDecomposition.bot_supp`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L497).

```lean
lemma bot_supp (hmul : IsMulRep rep) :
    (bot hmul).supp = ∅
```

**`StandardModel.GaugeWeightDecomposition.spanSingleton`**, a def, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L504).

> The span of a single simultaneous eigenvector of the gauge torus, as a
> decomposition concentrated in its one weight. This is the base case from which the
> decompositions of spans of weight vectors are assembled by `iSup` and `sup`.

```lean
noncomputable def spanSingleton (hmul : IsMulRep rep) (x : B) (w : GaugeWeight)
    (hx : ∀ i, rep (gaugeTorusGen i) x = ((expI : ℂ) ^ w.coord i) • x) :
    GaugeWeightDecomposition rep (Submodule.span ℂ {x})
```

**`StandardModel.GaugeWeightDecomposition.spanSingleton_piece`**, a lemma, [line 529](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L529).

```lean
lemma spanSingleton_piece (hmul : IsMulRep rep) (x : B) (w : GaugeWeight)
    (hx : ∀ i, rep (gaugeTorusGen i) x = ((expI : ℂ) ^ w.coord i) • x)
    (w' : GaugeWeight) :
    (spanSingleton hmul x w hx).piece w'
      = if w' = w then Submodule.span ℂ {x} else ⊥
```

**`StandardModel.GaugeWeightDecomposition.iSup`**, a def, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L539).

> An indexed join of decompositions. A family of decompositions indexed by a finite type
> decomposes the join, its pieces joined and its supports united one weight at a time. This is
> the arbitrary-arity form of `sup`.

```lean
noncomputable def iSup {ι : Type*} [Fintype ι] {V : ι → Submodule ℂ B}
    (hmul : IsMulRep rep)
    (d : (a : ι) → GaugeWeightDecomposition rep (V a)) :
    GaugeWeightDecomposition rep (⨆ a, V a)
```

**`StandardModel.GaugeWeightDecomposition.piece_iSup`**, a lemma, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L557).

```lean
lemma piece_iSup {ι : Type*} [Fintype ι] {V : ι → Submodule ℂ B}
    (hmul : IsMulRep rep)
    (d : (a : ι) → GaugeWeightDecomposition rep (V a)) (w : GaugeWeight) :
    (iSup hmul d).piece w = ⨆ a, (d a).piece w
```

**`StandardModel.GaugeWeightDecomposition.iSup_supp`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L563).

> The support of an indexed join is the union of the supports.

```lean
lemma iSup_supp {ι : Type*} [Fintype ι] {V : ι → Submodule ℂ B}
    (hmul : IsMulRep rep)
    (d : (a : ι) → GaugeWeightDecomposition rep (V a)) :
    (iSup hmul d).supp = Finset.univ.biUnion fun a => (d a).supp
```

**`StandardModel.GaugeWeightDecomposition.iSupProp`**, a def, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L572).

> A join over a proposition. `⨆ _ : p, V` is `V` when `p` holds and `⊥` otherwise, so
> it is decomposed by the given decomposition or by `bot`. The argument is a function of the
> proof, so the decomposition of `V` may itself depend on `p`.

```lean
noncomputable def iSupProp {p : Prop} [Decidable p]
    (hmul : IsMulRep rep)
    (d : p → GaugeWeightDecomposition rep V) :
    GaugeWeightDecomposition rep (⨆ _ : p, V)
```

## H. Products

> Charges add when operators are multiplied, and this section is where we prove this fact.
> If the torus acts on `x` by the character of `w₁` and on `y` by the character of `w₂` then,
> because `rep` respects multiplication, it acts on `x * y` by the product of the two characters,
> which additivity of `GaugeWeight.coord` identifies with the character of `w₁ + w₂`. So the
> weight-`w` piece of `V * V'` is spanned by products of pieces whose weights sum to `w`, and the
> support of a product is the sumset of the supports.
>
> The defining formula `mul_piece` joins over all pairs of weights in `ℤ⁴ × ℤ⁴`. Only finitely
> many weights occur, so one of the two can always be eliminated against a support, and
> `mul_piece_eq_sub` and `mul_piece_eq_sub'` do this against the left and the right factor. The
> resulting finite joins are what make the weight pieces of a product computable.

**`StandardModel.GaugeWeightDecomposition.mul`**, an instance, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L596).

> The product of two gauge weight decompositions, decomposing `V * V'`.

```lean
noncomputable instance mul [d : GaugeWeightDecomposition rep V]
    [d' : GaugeWeightDecomposition rep V'] :
    GaugeWeightDecomposition rep (V * V')
```

**`StandardModel.GaugeWeightDecomposition.mul_supp`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L633).

> The support of a product is the pointwise sum of the supports.

```lean
lemma mul_supp [GaugeWeightDecomposition rep V] [GaugeWeightDecomposition rep V'] :
    supp rep (V * V') = supp rep V + supp rep V'
```

**`StandardModel.GaugeWeightDecomposition.mul_piece`**, a lemma, [line 638](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L638).

> Weights add under multiplication. The weight-`w` piece of a product is spanned by the
> products of pieces whose weights sum to `w`.

```lean
lemma mul_piece [GaugeWeightDecomposition rep V] [GaugeWeightDecomposition rep V']
    (w : GaugeWeight) :
    piece rep (V * V') w
      = ⨆ w₁, ⨆ w₂, ⨆ _ : w₁ + w₂ = w, piece rep V w₁ * piece rep V' w₂
```

**`StandardModel.GaugeWeightDecomposition.mul_piece_eq_sub`**, a lemma, [line 645](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L645).

> The product formula with the second weight eliminated against the support of the left
> factor, the right factor being read at the complement `w - w₁`.

```lean
lemma mul_piece_eq_sub [d : GaugeWeightDecomposition rep V]
    [d' : GaugeWeightDecomposition rep V'] (w : GaugeWeight) :
    piece rep (V * V') w = ⨆ w₁ ∈ supp rep V, piece rep V w₁ * piece rep V' (w - w₁)
```

**`StandardModel.GaugeWeightDecomposition.mul_piece_eq_sub'`**, a lemma, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L659).

> The mirror of `mul_piece_eq_sub`, joining over the weights of the right factor.

```lean
lemma mul_piece_eq_sub' [d : GaugeWeightDecomposition rep V]
    [d' : GaugeWeightDecomposition rep V'] (w : GaugeWeight) :
    piece rep (V * V') w = ⨆ w₂ ∈ supp rep V', piece rep V (w - w₂) * piece rep V' w₂
```

## I. Invariants

> A gauge-invariant element is fixed by the torus in particular, so it ought to have zero weight.
> Making that an argument requires knowing the pieces are independent. Along one generator this
> is immediate, since the pieces sit in eigenspaces of a single operator at the eigenvalues
> `(exp i) ^ k`, pairwise distinct because `exp i` is not a root of unity, and eigenspaces at
> distinct eigenvalues meet trivially. At rank four no single generator separates the weights, so
> the argument is made one generator at a time.
>
> What this yields is stronger than the statement about invariants. `piece_eq_inf` identifies the
> weight-`w` piece with the intersection of `V` and the joint eigenspace of the four generators,
> so the pieces depend only on `V` and the representation.
>
> Zero weight is necessary but not sufficient for invariance. The torus is abelian and sees only
> characters, so it cannot distinguish a true singlet from the neutral component of a higher
> multiplet. Both `H†H` and `H†σ³H` carry zero weight, and only the first is gauge invariant. So
> what passes `mem_zero_of_invariant` must still be checked against the non-abelian part of the
> group; no grading closes that gap, since a grading sees only the abelian subgroup generated by
> the elements it uses. The `Invariants` files do that check representation by representation.

**`StandardModel.GaugeWeightDecomposition.mem_iSup_of_eigenvector`**, a lemma, [line 697](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L697).

> The one-generator refinement step. A vector in the span of a family graded along a
> single operator, and an eigenvector of that operator at exponent `n`, lies in the span of
> just those pieces at exponent `n`.

```lean
lemma mem_iSup_of_eigenvector {ι : Type*} {T : Module.End ℂ B} {p : ι → Submodule ℂ B}
    {f : ι → ℤ} (hp : ∀ j, p j ≤ Module.End.eigenspace T ((expI : ℂ) ^ f j))
    {x : B} (hx : x ∈ ⨆ j, p j) {n : ℤ} (hT : T x = ((expI : ℂ) ^ n) • x) :
    x ∈ ⨆ j, ⨆ _ : f j = n, p j
```

**`StandardModel.GaugeWeightDecomposition.mem_iSup_of_forall_eigenvector`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L722).

> The many-generator refinement. The same for a finite family of operators. A vector in
> the span of the family and an eigenvector of every operator lies in the span of just those
> pieces whose exponents match throughout.

```lean
lemma mem_iSup_of_forall_eigenvector {ι κ : Type*} [Fintype κ] [DecidableEq κ]
    {T : κ → Module.End ℂ B} {p : ι → Submodule ℂ B} {f : ι → κ → ℤ}
    (hp : ∀ j k, p j ≤ Module.End.eigenspace (T k) ((expI : ℂ) ^ f j k))
    {x : B} (hx : x ∈ ⨆ j, p j) {n : κ → ℤ}
    (hT : ∀ k, T k x = ((expI : ℂ) ^ n k) • x) :
    x ∈ ⨆ j, ⨆ _ : f j = n, p j
```

**`StandardModel.GaugeWeightDecomposition.piece_eq_inf`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L753).

> The pieces are canonical. The weight-`w` piece is exactly the part of `V` on which the
> four torus generators act by the weight-`w` characters. See `piece_congr`.

```lean
lemma piece_eq_inf (d : GaugeWeightDecomposition rep V) (w : GaugeWeight) :
    d.piece w
      = V ⊓ ⨅ i, Module.End.eigenspace (rep (gaugeTorusGen i)) ((expI : ℂ) ^ w.coord i)
```

**`StandardModel.GaugeWeightDecomposition.piece_congr`**, a lemma, [line 773](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L773).

> The pieces depend only on the submodule. Two decompositions of equal submodules have
> the same pieces, so a computation of `piece` may be carried along any equality of
> submodules.

```lean
lemma piece_congr {W : Submodule ℂ B} [d : GaugeWeightDecomposition rep V]
    [d' : GaugeWeightDecomposition rep W] (hVW : V = W) (w : GaugeWeight) :
    d.piece w = d'.piece w
```

**`StandardModel.GaugeWeightDecomposition.mem_zero_of_invariant`**, a lemma, [line 780](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L780).

> A gauge-invariant element sits in the zero-weight piece. Only invariance under the
> four torus generators is used. The converse is false; see the warning in section F.

```lean
lemma mem_zero_of_invariant (d : GaugeWeightDecomposition rep V) {x : B} (hx : x ∈ V)
    (hV : ∀ g : GaugeGroupI, rep g x = x) : x ∈ d.piece 0
```

**`StandardModel.GaugeWeightDecomposition.reducesInvariantsTo_piece_zero`**, a lemma, [line 792](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L792).

> The torus sieve as a reduction for the four torus generators: modulo a torus-stable
> submodule, their invariants in `V` lie in the weight-zero piece. Every other weight in the
> support is scaled by some generator by `(exp i) ^ n` with `n ≠ 0`, a scalar other than `1`,
> so its piece reduces to `⊥` by `reducesInvariantsTo_bot_of_apply_eq_smul`; each piece is
> carried into itself by the torus, and `ReducesInvariantsTo.iSup` joins the pieces.

```lean
lemma reducesInvariantsTo_piece_zero (dV : GaugeWeightDecomposition rep V) :
    ReducesInvariantsTo (fun i => rep (gaugeTorusGen i)) V (dV.piece 0)
```

**`StandardModel.GaugeWeightDecomposition.mem_piece_zero_sup_of_invariant`**, a lemma, [line 825](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean#L825).

> An element of `V ⊔ S` fixed by the four torus generators, for `S` closed under them,
> lies in the weight-zero piece joined with `S`. This is `reducesInvariantsTo_piece_zero`
> unfolded, the form used to sieve a sector with `S` the part already understood. Only the
> torus is used, so gauge invariance of the element and gauge stability of `S` are more than
> is needed.

```lean
lemma mem_piece_zero_sup_of_invariant {S : Submodule ℂ B}
    (dV : GaugeWeightDecomposition rep V)
    (hS : ∀ (i : Fin 4) (y : B), y ∈ S → rep (gaugeTorusGen i) y ∈ S)
    {x : B} (hx : x ∈ V ⊔ S) (hinv : ∀ i : Fin 4, rep (gaugeTorusGen i) x = x) :
    x ∈ dV.piece 0 ⊔ S
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)
- [Reducing invariants modulo a stable submodule](../../../mathematics/part-01/invariantreduction.md)
- [Algebras, duals and representations on a conjugate module](../../../mathematics/part-02/modules/conjmodule.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GaugeWeight.lean)
