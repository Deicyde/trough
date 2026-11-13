---
declaration: module
origin: cited
lean: Norm₂, InnerProductSpace', InnerProductSpace'.toNormWithL2, InnerProductSpace'.toInnerWithL2, InnerProductSpace'.toNormedAddCommGroupWitL2, InnerProductSpace'.norm_withLp2_eq_norm2, InnerProductSpace'.toNormedSpaceWithL2, InnerProductSpace'.toInnerProductSpaceWithL2
statement: formalized
proof: formalized
---

# Inner product space

The module `Physlib.Mathematics.InnerProductSpace.Basic`, [Physlib/Mathematics/InnerProductSpace/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean): 46 declarations (7 instances with no name), 11 with a docstring.

> In this module we define the type class `InnerProductSpace' 𝕜 E` which is a
> generalization of `InnerProductSpace 𝕜 E`, as it does not require the condition `‖x‖^2 = ⟪x,x⟫`
> but instead the condition `∃ (c > 0) (d > 0), c • ‖x‖^2 ≤ ⟪x,x⟫ ≤ d • ‖x‖^2`.
> Instead `E` is equipped with a L₂ norm `‖x‖₂` which satisfies `‖x‖₂ = √⟪x,x⟫`.
>
> This allows us to define the inner product space structure on product types `E × F` and
> pi types `ι → E`, which would otherwise not be possible due to the use of max norm on these types.
>
> We define the following maps:
>
> - `InnerProductSpace 𝕜 E → InnerProductSpace' 𝕜 E` which sets `‖x‖₂ = ‖x‖`.
> - `InnerProductSpace' 𝕜 E → InnerProductSpace 𝕜 (WithLp 2 E)` which uses the fact that the norm
>   defined on `WithLp 2 E` is L₂ norm.

**`Norm₂`**, a class, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L36).

> L₂ norm on `E`.
>
> In particular, on product types `X×Y` and pi types `ι → X` this class provides L₂ norm unlike `‖·‖`.

```lean
class Norm₂ (E : Type*) where
  norm₂ : E → ℝ
```

**`InnerProductSpace'`**, a class, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L72).

> Effectively as `InnerProductSpace 𝕜 E` but it does not requires that `‖x‖^2 = ⟪x,x⟫`. It is
> only required that they are equivalent `∃ (c > 0) (d > 0), c • ‖x‖^2 ≤ ⟪x,x⟫ ≤ d • ‖x‖^2`. The main
> purpose of this class is to provide inner product space structure on product types `ExF` and
> pi types `ι → E` without using `WithLp` gadget.
>
> If you want to access L₂ norm use `‖x‖₂ := √⟪x,x⟫`.
>
> This class induces `InnerProductSpace 𝕜 (WithLp 2 E)` which equips `‖·‖` on `X` with L₂ norm.
> This is very useful when translating results from `InnerProductSpace` to `InnerProductSpace'`
> together with `toL2 : E →L[𝕜] (WithLp 2 E)` and `fromL2 : (WithL2 2 E) →L[𝕜] E`.
>
> In short we have these implications:
> ```
>   InnerProductSpace 𝕜 E → InnerProductSpace' 𝕜 E
>   InnerProductSpace' 𝕜 E → InnerProductSpace 𝕜 (WithLp 2 E)
> ```
>
> The reason behind this type class is that with current mathlib design the requirement
> `‖x‖^2 = ⟪x,x⟫` prevents us to give inner product space structure on product type `E×F` and pi
> type `ι → E` as they are equipped with max norm. One has to work with `WithLp 2 (E×F)` and
> `WithLp 2 (ι → E)`. This places quite a bit inconvenience on users in certain scenarios.
> In particular, the main motivation behind this class is to make computations of `adjFDeriv` and
> `gradient` easy.

```lean
class InnerProductSpace' (𝕜 : Type*) (E : Type*) [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
    extends Norm₂ E where
  /-- Core inner product properties. -/
  core : InnerProductSpace.Core 𝕜 E
  /-- The inner product induces the L₂ norm. -/
  norm₂_sq_eq_re_inner : ∀ x : E, ‖x‖₂ ^ 2 = re (core.inner x x)
  /-- Norm induced by inner product is topologically equivalent to the given norm on E. -/
  inner_top_equiv_norm : ∃ c d : ℝ,
    0 < c ∧ 0 < d ∧
    ∀ x : E, (c • ‖x‖^2 ≤ re (core.inner x x)) ∧ (re (core.inner x x) ≤ d • ‖x‖^2)
```

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L87).

```lean
instance [inst : InnerProductSpace' 𝕜 E] : InnerProductSpace.Core 𝕜 E
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L89).

```lean
instance [inst : InnerProductSpace' 𝕜 E] : Inner 𝕜 E
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L91).

```lean
instance {𝕜 : Type*} {E : Type*} [RCLike 𝕜] [NormedAddCommGroup E] [inst : InnerProductSpace 𝕜 E] :
    InnerProductSpace' 𝕜 E
```

## B. Deriving the inner product structure on `WithLp 2 E` from `InnerProductSpace' 𝕜 E`

**`InnerProductSpace'.toNormWithL2`**, an instance, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L123).

> Attach L₂ norm to `WithLp 2 E`

```lean
scoped instance toNormWithL2 : Norm (WithLp 2 E)
```

**`InnerProductSpace'.toInnerWithL2`**, an instance, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L128).

> Attach inner product to `WithLp 2 E`

```lean
scoped instance toInnerWithL2 : Inner 𝕜 (WithLp 2 E)
```

**`InnerProductSpace'.toNormedAddCommGroupWitL2`**, an instance, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L133).

> Attach normed group structure to `WithLp 2 E` with L₂ norm.

```lean
scoped instance toNormedAddCommGroupWitL2 : NormedAddCommGroup (WithLp 2 E)
```

**`InnerProductSpace'.norm_withLp2_eq_norm2`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L146).

```lean
lemma norm_withLp2_eq_norm2 (x : WithLp 2 E) :
    ‖x‖ = |norm₂ (WithLp.equiv 2 E x)|
```

**`InnerProductSpace'.toNormedSpaceWithL2`**, an instance, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L153).

> Attach normed space structure to `WithLp 2 E` with L₂ norm.

```lean
scoped instance toNormedSpaceWithL2 : NormedSpace 𝕜 (WithLp 2 E)
```

**`InnerProductSpace'.toInnerProductSpaceWithL2`**, an instance, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L161).

> Attach inner product space structure to `WithLp 2 E`.

```lean
instance toInnerProductSpaceWithL2 : InnerProductSpace 𝕜 (WithLp 2 E)
```

**`InnerProductSpace'.toL2`**, a def, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L172).

> Continuous linear map from `E` to `WithLp 2 E`.
>
> This map is continuous because we require topological equivalence between `‖·‖` and `‖·‖₂`.

```lean
def toL2 : E →L[𝕜] WithLp 2 E
```

**`InnerProductSpace'.fromL2`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L195).

> Continuous linear map from `WithLp 2 E` to `E`.
>
> This map is continuous because we require topological equivalence between `‖·‖` and `‖·‖₂`.

```lean
def fromL2 : WithLp 2 E →L[𝕜] E
```

**`InnerProductSpace'.fromL2_inner_left`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L218).

```lean
lemma fromL2_inner_left (x : WithLp 2 E) (y : E) : ⟪fromL2 𝕜 x, y⟫ = ⟪x, toL2 𝕜 y⟫
```

**`InnerProductSpace'.ofLp_inner_left`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L220).

```lean
lemma ofLp_inner_left (x : E) (y : WithLp 2 E) : ⟪WithLp.ofLp y, x⟫ = ⟪y, WithLp.toLp 2 x⟫
```

**`InnerProductSpace'.toL2_inner_left`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L223).

```lean
lemma toL2_inner_left (x : E) (y : WithLp 2 E) : ⟪toL2 𝕜 x, y⟫ = ⟪x, fromL2 𝕜 y⟫
```

**`InnerProductSpace'.toLp_inner_left`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L225).

```lean
lemma toLp_inner_left (x : WithLp 2 E) (y : E) : ⟪WithLp.toLp 2 y, x⟫ = ⟪y, WithLp.ofLp x⟫
```

**`InnerProductSpace'.toL2_fromL2`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L229).

```lean
lemma toL2_fromL2 (x : WithLp 2 E) : toL2 𝕜 (fromL2 𝕜 x) = x
```

**`InnerProductSpace'.fromL2_toL2`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L231).

```lean
lemma fromL2_toL2 (x : E) : fromL2 𝕜 (toL2 𝕜 x) = x
```

**`InnerProductSpace'.equivL2`**, a def, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L236).

> Continuous linear equivalence between `WithLp 2 E` and `E` under `InnerProductSpace' 𝕜 E`.

```lean
def equivL2 : (WithLp 2 E) ≃L[𝕜] E
```

**An instance with no name**, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L246).

```lean
instance [CompleteSpace E] : CompleteSpace (WithLp 2 E)
```

## C. Basic properties of the inner product

**`ext_inner_left'`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L264).

```lean
lemma ext_inner_left' {x y : E} (h : ∀ v, ⟪v, x⟫ = ⟪v, y⟫) : x = y
```

**`ext_inner_right'`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L269).

```lean
lemma ext_inner_right' {x y : E} (h : ∀ v, ⟪x, v⟫ = ⟪y, v⟫) : x = y
```

**`inner_conj_symm'`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L274).

```lean
lemma inner_conj_symm' (x y : E) : ⟪y, x⟫† = ⟪x, y⟫
```

**`inner_smul_left'`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L277).

```lean
lemma inner_smul_left' (x y : E) (r : 𝕜) : ⟪r • x, y⟫ = r† * ⟪x, y⟫
```

**`inner_smul_right'`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L280).

```lean
lemma inner_smul_right' (x y : E) (r : 𝕜) : ⟪x, r • y⟫ = r * ⟪x, y⟫
```

**`inner_zero_left'`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L284).

```lean
lemma inner_zero_left' (x : E) : ⟪0, x⟫ = 0
```

**`inner_zero_right'`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L288).

```lean
lemma inner_zero_right' (x : E) : ⟪x, 0⟫ = 0
```

**`inner_add_left'`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L291).

```lean
lemma inner_add_left' (x y z : E) : ⟪x + y, z⟫ = ⟪x, z⟫ + ⟪y, z⟫
```

**`inner_add_right'`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L294).

```lean
lemma inner_add_right' (x y z : E) : ⟪x, y + z⟫ = ⟪x, y⟫ + ⟪x, z⟫
```

**`inner_sub_left'`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L297).

```lean
lemma inner_sub_left' (x y z : E) : ⟪x - y, z⟫ = ⟪x, z⟫ - ⟪y, z⟫
```

**`inner_sub_right'`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L300).

```lean
lemma inner_sub_right' (x y z : E) : ⟪x, y - z⟫ = ⟪x, y⟫ - ⟪x, z⟫
```

**`inner_neg_left'`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L304).

```lean
lemma inner_neg_left' (x y : E) : ⟪-x, y⟫ = -⟪x, y⟫
```

**`inner_neg_right'`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L308).

```lean
lemma inner_neg_right' (x y : E) : ⟪x, -y⟫ = -⟪x, y⟫
```

**`inner_self_eq_zero'`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L312).

```lean
lemma inner_self_eq_zero' {x : E} : ⟪x, x⟫ = 0 ↔ x = 0
```

**`inner_sum'`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L317).

```lean
lemma inner_sum'{ι : Type*} [Fintype ι] (x : E) (g : ι → E) :
    ⟪x, ∑ i, g i⟫ = ∑ i, ⟪x, g i⟫
```

**`Continuous.inner'`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L322).

```lean
lemma Continuous.inner' {α} [TopologicalSpace α] (f g : α → E)
    (hf : Continuous f) (hg : Continuous g) : Continuous (fun a => ⟪f a, g a⟫)
```

**`real_inner_self_nonneg'`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L335).

```lean
lemma real_inner_self_nonneg' {x : F} : 0 ≤ re (⟪x, x⟫)
```

**`real_inner_comm'`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L338).

```lean
lemma real_inner_comm' (x y : F) : ⟪y, x⟫ = ⟪x, y⟫
```

**`ContDiffAt.inner'`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L342).

```lean
lemma ContDiffAt.inner' {f g : E → F} {x : E}
    (hf : ContDiffAt ℝ n f x) (hg : ContDiffAt ℝ n g x) :
    ContDiffAt ℝ n (fun x => ⟪f x, g x⟫) x
```

**`ContDiff.inner'`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L349).

```lean
lemma ContDiff.inner' {f g : E → F}
    (hf : ContDiff ℝ n f) (hg : ContDiff ℝ n g) :
    ContDiff ℝ n (fun x => ⟪f x, g x⟫)
```

**An instance with no name**, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L373).

> Inner product on product types `E×F` defined as `⟪x,y⟫ = ⟪x.fst,y.fst⟫ + ⟪x.snd,y.snd⟫`.
>
> This is just local instance as it is superseded by the following instance for
> `InnerProductSpace'`.

```lean
local instance : Inner 𝕜 (E×F)
```

**`prod_inner_apply'`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L376).

```lean
lemma prod_inner_apply' (x y : (E × F)) : ⟪x, y⟫ = ⟪x.fst, y.fst⟫ + ⟪x.snd, y.snd⟫
```

**An instance with no name**, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L381).

```lean
instance : InnerProductSpace' 𝕜 (E × F)
```

**An instance with no name**, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L446).

```lean
instance {ι : Type*} [Fintype ι] : InnerProductSpace' 𝕜 (ι → E)
```

**`isBoundedBilinearMap_inner'`**, a lemma, [line 544](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean#L544).

```lean
lemma _root_.isBoundedBilinearMap_inner' :
    IsBoundedBilinearMap ℝ fun p : E × E => ⟪p.1, p.2⟫
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/InnerProductSpace/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Basic.lean)
