---
declaration: module
origin: cited
lean: LorentzGroup, LorentzGroup.mem_iff_self_mul_dual, LorentzGroup.mem_iff_dual_mul_self, LorentzGroup.mem_iff_transpose, LorentzGroup.mem_iff_neg_mem, LorentzGroup.mem_mul, LorentzGroup.one_mem, LorentzGroup.dual_mem
statement: formalized
proof: formalized
---

# The Lorentz Group

The module `Physlib.Relativity.LorentzGroup.Basic`, [Physlib/Relativity/LorentzGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean): 55 declarations (5 instances with no name), 22 with a docstring.

> We define the Lorentz group.

## References

> * Lorentz Transformations, Rotations, and Boosts, Jaffe.
>   <https://cdn.ku.edu.tr/cdn/files/amostafazadeh/phys517_518/phys517_2016f/Handouts/A_Jaffi_Lorentz_Group.pdf>.
>   [ref: jaffe\_lorentz\_notes]

## Matrices which preserves the Minkowski metric

> We start studying the properties of matrices which preserve `ηLin`.
> These matrices form the Lorentz group, which we will define in the next section at `lorentzGroup`.

**`LorentzGroup`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L48).

> The Lorentz group is the subset of matrices for which
> `Λ * dual Λ = 1`.

```lean
def LorentzGroup (d : ℕ) : Set (Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ)
```

## Membership conditions

**`LorentzGroup.mem_iff_self_mul_dual`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L64).

```lean
lemma mem_iff_self_mul_dual : Λ ∈ LorentzGroup d ↔ Λ * dual Λ = 1
```

**`LorentzGroup.mem_iff_dual_mul_self`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L67).

```lean
lemma mem_iff_dual_mul_self : Λ ∈ LorentzGroup d ↔ dual Λ * Λ = 1
```

**`LorentzGroup.mem_iff_transpose`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L71).

```lean
lemma mem_iff_transpose : Λ ∈ LorentzGroup d ↔ Λᵀ ∈ LorentzGroup d
```

**`LorentzGroup.mem_iff_neg_mem`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L84).

```lean
lemma mem_iff_neg_mem : Λ ∈ LorentzGroup d ↔ -Λ ∈ LorentzGroup d
```

**`LorentzGroup.mem_mul`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L88).

```lean
lemma mem_mul (hΛ : Λ ∈ LorentzGroup d) (hΛ' : Λ' ∈ LorentzGroup d) : Λ * Λ' ∈ LorentzGroup d
```

**`LorentzGroup.one_mem`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L95).

```lean
lemma one_mem : 1 ∈ LorentzGroup d
```

**`LorentzGroup.dual_mem`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L99).

```lean
lemma dual_mem (h : Λ ∈ LorentzGroup d) : dual Λ ∈ LorentzGroup d
```

**`LorentzGroup.mem_iff_transpose_mul_minkowskiMatrix_mul_self`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L106).

> A matrix `Λ` is in the Lorentz group if and only if it satisfies `Λᵀ * η * Λ = η`.

```lean
lemma mem_iff_transpose_mul_minkowskiMatrix_mul_self
    (Λ : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) :
    Λ ∈ LorentzGroup d ↔ Λᵀ * η * Λ = η
```

## The Lorentz group as a group

**`lorentzGroupIsGroup`**, an instance, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L133).

> The instance of a group on `LorentzGroup d`.

```lean
instance lorentzGroupIsGroup : Group (LorentzGroup d)
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L143).

> `LorentzGroup` has the subtype topology.

```lean
instance : TopologicalSpace (LorentzGroup d)
```

## Lorentz group as a closed subset of matrices

**`LorentzGroup.continuous_self_mul_dual`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L157).

```lean
lemma continuous_self_mul_dual {d : ℕ} :
    Continuous (fun Λ : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ => Λ * dual Λ)
```

**`LorentzGroup.isClosed`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L163).

> The Lorentz group is closed in the ambient matrix space.

```lean
lemma isClosed (d : ℕ) :
    IsClosed (LorentzGroup d : Set (Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ))
```

**`LorentzGroup.isClosedEmbedding_val`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L169).

> The coercion from the Lorentz group to its ambient matrix space is a closed embedding.

```lean
lemma isClosedEmbedding_val {d : ℕ} :
    Topology.IsClosedEmbedding
      (Subtype.val : LorentzGroup d → Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ)
```

## Inverses

**`LorentzGroup.inv_eq_dual`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L179).

```lean
lemma inv_eq_dual (Λ : LorentzGroup d) :
    (Λ⁻¹ : LorentzGroup d) = ⟨minkowskiMatrix.dual Λ.1, LorentzGroup.dual_mem Λ.2⟩
```

**`LorentzGroup.coe_inv`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L183).

```lean
lemma coe_inv : (Λ⁻¹).1 = Λ.1⁻¹
```

**An instance with no name**, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L186).

> The underlying matrix of a Lorentz transformation is invertible.

```lean
instance (M : LorentzGroup d) : Invertible M.1
```

**`LorentzGroup.subtype_inv_mul`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L195).

```lean
lemma subtype_inv_mul : (Subtype.val Λ)⁻¹ * (Subtype.val Λ) = 1
```

**`LorentzGroup.subtype_mul_inv`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L197).

```lean
lemma subtype_mul_inv : (Subtype.val Λ) * (Subtype.val Λ)⁻¹ = 1
```

**`LorentzGroup.mul_minkowskiMatrix_mul_transpose`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L200).

```lean
lemma mul_minkowskiMatrix_mul_transpose :
    (Subtype.val Λ) * minkowskiMatrix * (Subtype.val Λ).transpose = minkowskiMatrix
```

**`LorentzGroup.transpose_mul_minkowskiMatrix_mul_self`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L210).

```lean
lemma transpose_mul_minkowskiMatrix_mul_self :
    (Subtype.val Λ).transpose * minkowskiMatrix * (Subtype.val Λ) = minkowskiMatrix
```

## Transpose of a Lorentz transformation

**`LorentzGroup.transpose`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L226).

> The transpose of a matrix in the Lorentz group is an element of the Lorentz group.

```lean
def transpose (Λ : LorentzGroup d) : LorentzGroup d
```

**`LorentzGroup.transpose_one`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L230).

```lean
lemma transpose_one : @transpose d 1 = 1
```

**`LorentzGroup.transpose_mul`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L233).

```lean
lemma transpose_mul : transpose (Λ * Λ') = transpose Λ' * transpose Λ
```

**`LorentzGroup.transpose_val`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L236).

```lean
lemma transpose_val : (transpose Λ).1 = Λ.1ᵀ
```

**`LorentzGroup.transpose_inv`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L238).

```lean
lemma transpose_inv : (transpose Λ)⁻¹ = transpose Λ⁻¹
```

**`LorentzGroup.comm_minkowskiMatrix`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L242).

```lean
lemma comm_minkowskiMatrix : Λ.1 * minkowskiMatrix = minkowskiMatrix * (transpose Λ⁻¹).1
```

**`LorentzGroup.minkowskiMatrix_comm`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L247).

```lean
lemma minkowskiMatrix_comm : minkowskiMatrix * Λ.1 = (transpose Λ⁻¹).1 * minkowskiMatrix
```

## Negation of a Lorentz transformation

**An instance with no name**, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L264).

> The negation of a Lorentz transform.

```lean
instance : Neg (LorentzGroup d)
```

**`LorentzGroup.coe_neg`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L268).

```lean
lemma coe_neg : (-Λ).1 = -Λ.1
```

**`LorentzGroup.inv_neg`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L270).

```lean
lemma inv_neg : (-Λ)⁻¹ = -Λ⁻¹
```

## Lorentz group as a topological group

> We now show that the Lorentz group is a topological group.
> We do this by showing that the natural map from the Lorentz group to `GL (Fin 4) ℝ` is an
> embedding.

**`LorentzGroup.toGL`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L285).

> The homomorphism of the Lorentz group into `GL (Fin 4) ℝ`.

```lean
def toGL : LorentzGroup d →* GL (Fin 1 ⊕ Fin d) ℝ
```

**`LorentzGroup.toGL_injective`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L293).

```lean
lemma toGL_injective : Function.Injective (@toGL d)
```

**`LorentzGroup.toProd`**, a def, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L301).

> The homomorphism from the Lorentz Group into the monoid of matrices times the opposite of
> the monoid of matrices.

```lean
def toProd : LorentzGroup d →* (Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) ×
    (Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ)ᵐᵒᵖ
```

**`LorentzGroup.toProd_eq_transpose_η`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L305).

```lean
lemma toProd_eq_transpose_η : toProd Λ = (Λ.1, MulOpposite.op $ minkowskiMatrix.dual Λ.1)
```

**`LorentzGroup.toProd_injective`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L307).

```lean
lemma toProd_injective : Function.Injective (@toProd d)
```

**`LorentzGroup.toProd_continuous`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L313).

```lean
lemma toProd_continuous : Continuous (@toProd d)
```

**`LorentzGroup.toProd_embedding`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L322).

> The embedding from the Lorentz Group into the monoid of matrices times the opposite of
> the monoid of matrices.

```lean
lemma toProd_embedding : IsEmbedding (@toProd d)
```

**`LorentzGroup.toGL_embedding`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L329).

> The embedding from the Lorentz Group into `GL (Fin 4) ℝ`.

```lean
lemma toGL_embedding : IsEmbedding (@toGL d).toFun
```

**An instance with no name**, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L339).

> The embedding of the Lorentz group into `GL(n, ℝ)` gives `LorentzGroup d` an instance
> of a topological group.

```lean
instance : IsTopologicalGroup (LorentzGroup d)
```

## Lorentz group as a closed subgroup of the general linear group

> Following the plan sketched by PrParadoxy and Joseph Tooby-Smith in physlib issue #833, we realise
> `LorentzGroup d` as a *closed* subgroup of `GL (Fin 1 ⊕ Fin d) ℝ`. This promotes the closed
> embedding into the ambient matrix space (`isClosedEmbedding_val`) to the level of the general
> linear group, and is the structural prerequisite for a Lie group structure on the Lorentz group.
>
> The remaining step of that plan, endowing `LorentzGroup d` with a Lie group structure as a closed
> subgroup of the Lie group `GL (Fin 1 ⊕ Fin d) ℝ` and thereby deriving its Lie algebra, needs the
> closed subgroup theorem (Cartan's theorem: a closed subgroup of a Lie group is an embedded Lie
> subgroup). That theorem is not yet available in Mathlib: there is no `LieSubgroup`, and no
> `ChartedSpace`/`IsManifold` instance is produced from a closed embedding (only
> `IsOpenEmbedding.singletonChartedSpace`, for open embeddings). The Lie group instance and the
> Lorentz algebra therefore remain open; …

**`LorentzGroup.range_toGL`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L364).

> The range of `toGL`, as a set in `GL (Fin 1 ⊕ Fin d) ℝ`, is exactly the preimage of the
> Lorentz group under the coercion `GL (Fin 1 ⊕ Fin d) ℝ → Matrix _ _ ℝ`: an element of the general
> linear group lies in the image precisely when its underlying matrix is a Lorentz transformation.

```lean
lemma range_toGL :
    Set.range (@toGL d).toFun =
      Units.val ⁻¹' (LorentzGroup d : Set (Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ))
```

**`LorentzGroup.toGL_isClosedEmbedding`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L378).

> The homomorphism `toGL` is a closed embedding of the Lorentz group into
> `GL (Fin 1 ⊕ Fin d) ℝ`. This strengthens `toGL_embedding`: the image is closed because it is the
> preimage, under the continuous coercion `GL (Fin 1 ⊕ Fin d) ℝ → Matrix _ _ ℝ`, of the closed set
> `LorentzGroup d` (`LorentzGroup.isClosed`).

```lean
lemma toGL_isClosedEmbedding : Topology.IsClosedEmbedding (@toGL d).toFun
```

**`LorentzGroup.toGLSubgroup`**, a def, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L386).

> The Lorentz group realised as a subgroup of `GL (Fin 1 ⊕ Fin d) ℝ`, namely the range of the
> embedding `toGL`.

```lean
def toGLSubgroup (d : ℕ) : Subgroup (GL (Fin 1 ⊕ Fin d) ℝ)
```

**`LorentzGroup.mem_toGLSubgroup`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L389).

```lean
lemma mem_toGLSubgroup {x : GL (Fin 1 ⊕ Fin d) ℝ} :
    x ∈ toGLSubgroup d ↔
      (x : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ) ∈ LorentzGroup d
```

**`LorentzGroup.coe_toGLSubgroup`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L398).

```lean
lemma coe_toGLSubgroup :
    (toGLSubgroup d : Set (GL (Fin 1 ⊕ Fin d) ℝ)) =
      Units.val ⁻¹' (LorentzGroup d : Set (Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ))
```

**`LorentzGroup.toClosedSubgroup`**, a def, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L406).

> The Lorentz group realised as a *closed* subgroup of `GL (Fin 1 ⊕ Fin d) ℝ`. The closedness is
> exactly the content of `toGL_isClosedEmbedding`, and is the hypothesis that the (not-yet-formalised)
> closed subgroup theorem would consume to produce a Lie group structure.

```lean
def toClosedSubgroup (d : ℕ) : ClosedSubgroup (GL (Fin 1 ⊕ Fin d) ℝ)
```

## To Complex matrices

**`LorentzGroup.toComplex`**, a def, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L421).

> The monoid homomorphisms taking the lorentz group to complex matrices.

```lean
def toComplex : LorentzGroup d →* Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℂ
```

**An instance with no name**, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L437).

> The image of a Lorentz transformation under `toComplex` is invertible.

```lean
instance (M : LorentzGroup d) : Invertible (toComplex M)
```

**`LorentzGroup.toComplex_inv`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L447).

```lean
lemma toComplex_inv (Λ : LorentzGroup d) : (toComplex Λ)⁻¹ = toComplex Λ⁻¹
```

**`LorentzGroup.star_toComplex_apply`**, a lemma, [line 454](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L454).

> The entries of `toComplex Λ` are real.

```lean
lemma star_toComplex_apply (Λ : LorentzGroup d) (i j : Fin 1 ⊕ Fin d) :
    star (toComplex Λ i j) = toComplex Λ i j
```

**`LorentzGroup.toComplex_mul_minkowskiMatrix_mul_transpose`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L459).

```lean
lemma toComplex_mul_minkowskiMatrix_mul_transpose (Λ : LorentzGroup d) :
    toComplex Λ * minkowskiMatrix.map ofRealHom * (toComplex Λ)ᵀ =
    minkowskiMatrix.map ofRealHom
```

**`LorentzGroup.toComplex_transpose_mul_minkowskiMatrix_mul_self`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L470).

```lean
lemma toComplex_transpose_mul_minkowskiMatrix_mul_self (Λ : LorentzGroup d) :
    (toComplex Λ)ᵀ * minkowskiMatrix.map ofRealHom * toComplex Λ =
    minkowskiMatrix.map ofRealHom
```

**`LorentzGroup.toComplex_mulVec_ofReal`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L480).

```lean
lemma toComplex_mulVec_ofReal (v : Fin 1 ⊕ Fin d → ℝ) (Λ : LorentzGroup d) :
    toComplex Λ *ᵥ (ofRealHom ∘ v) = ofRealHom ∘ (Λ *ᵥ v)
```

**`LorentzGroup.parity`**, a def, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L488).

> The parity transformation.

```lean
def parity : LorentzGroup d
```

## Equality conditions

**`LorentzGroup.eq_of_mulVec_eq`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean#L498).

```lean
lemma eq_of_mulVec_eq {Λ Λ' : LorentzGroup d}
    (h : ∀ (x : Fin 1 ⊕ Fin d → ℝ), Λ.1 *ᵥ x = Λ'.1 *ᵥ x) : Λ = Λ'
```

## Depends on

- [The Minkowski matrix](../minkowskimatrix.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Basic.lean)
