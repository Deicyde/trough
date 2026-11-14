---
declaration: module
origin: cited
lean: FTheory.SU5.Fluxes, FTheory.SU5.Fluxes.ext_iff, FTheory.SU5.Fluxes.zero_M, FTheory.SU5.Fluxes.zero_N, FTheory.SU5.Fluxes.add_M, FTheory.SU5.Fluxes.add_N, FTheory.SU5.FluxesFive, FTheory.SU5.FluxesFive.HasNoZero
statement: formalized
proof: formalized
---

# Fluxes of representations

The module `Physlib.StringTheory.FTheory.SU5.Fluxes.Basic`, [Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean): 40 declarations (8 instances with no name), 22 with a docstring.

## i. Overview

> Associated with each matter curve `Σ` are `G₄`-fluxes and `hypercharge` fluxes.
>
> For a given matter curve `Σ`, and a Standard Model representation `R`,
> these two fluxes contribute to the chiral index `χ(R)` of the representation
> (eq 17 of [1]).
>
> The chiral index is equal to the difference the number of left-handed minus
> the number of right-handed fermions `Σ` leads to in the representation `R`.
> Thus, for example, if `χ(R) = 0`, then all fermions in the representation `R`
> arising from `Σ` arise in vector-like pairs, and can be given a mass term without
> the presence of a Higgs like-particle.
>
> For a 10d representation matter curve the non-zero chiral indices can be parameterized in terms
> of two integers `M : ℤ` and `N : ℤ`. For the SM representation
> - `Q = (3,2)_{1/6}` the chirality index is `M`
> - `U = (bar 3,1)_{-2/3}` the chirality index is `M - N`
> - `E = (1,1)_{1}` the chirality index is `M + N`
> We call refer to `M` as the chirality flux of the 10d representation, and
> `N` as the hypercharge flux. There exact definitions are given in (eq 19 of [1]).
>
> Similarly, for the 5-bar representation matter curve the non-zero chiral indices can be
> likewise be parameterized in terms of two integers `M : ℤ` and `N : ℤ`. For the SM representation
> - `D = (bar 3,1)_{1/3}` the chirality index is `M`
> - `L = (1,2)_{-1/2}` the chirality index is `M + N`
> We again refer to `M` as the chirality flux of the 5-bar representation, and
> `N` as the hypercharge flux. The exact definitions are given in (eq 19 of [1]).
>
> If one wishes to put the condition of no chiral exotics in the spectrum, then
> we must ensure that the chiral indices above give the chiral content of the MSSM.
> These correspond to the following conditions:
> 1. The two higgs `Hu` and `Hd` must arise from different 5d-matter curves. Otherwise
>   they will give a `μ`-term.
> 2. The matter curve containing `Hu` must give one anti-chiral `(1,2)_{-1/2}` and
>   no `(bar 3,1)_{1/3}`. Thus `N = -1` and `M = 0`.
> 3. The matter curve containing `Hd` must give one chiral `(1,2)_{-1/2}` and
>   no `(bar 3,1)_{1/3}`. Thus `N = 1` and `M = 0`.
> 4. We should have no anti-chiral `(3,2)_{1/6}` and anti-chiral `(bar 3,1)_{-2/3}`.
>   Thus `0 ≤ M ` for all 10d-matter curves and 5d matter curves.
> 5. For the 10d-matter curves we should have no anti-chiral `(bar 3,1)_{-2/3}`
>     and no anti-chiral `(1,1)_{1}`. Thus `-M ≤ N ≤ M` for all 10d-matter curves.
> 6. For the 5d-matter curves we should have no anti-chiral `(1,2)_{-1/2}` (the only
>   anti-chiral one present is the one from `Hu`) and thus
>   `-M ≤ N` for all 5d-matter curves.
> 7. To ensure we have 3-families of fermions we must have that `∑ M = 3` and
>     `∑ N = 0` for the matter 10d and 5bar matter curves, and in addition `∑ (M + N) = 3` for the
>     matter 5d matter curves.
> See the conditions in equation 26 - 28 of [1].

## ii. Key results

> The above theory is implemented by defining two data structures:
> - `Fluxes` : The data of the fluxes `(M, N)` carried by a matter field.
> - `FluxesTen` of type `Multiset Fluxes`
>   which contains the chirality `M` and hypercharge fluxes
>   `N` of the 10d-matter curves.
> - `FluxesFive` of type `Multiset Fluxes`
>   which contains the chirality `M` and hypercharge fluxes
>   `N` of the 5-bar-matter curves (excluding the higgses).
>
> Note: Neither `FluxesTen` or `FluxesFive` are fundamental to the theory,
> they can be derived from other data structures.

## iv. References

> * Rational F-Theory GUTs without exotics (arXiv:1401.5084). [ref: arxiv\_1401\_5084]
> * For an old version of the material in this module see PR #569.

## A. Fluxes

> To each matter curve we associate a pair of integers `(M, N)`,
> the former of which is the chirality flux and the latter the hypercharge flux.

**`FTheory.SU5.Fluxes`**, a structure, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L142).

> The data of the fluxes carried by a matter field.

```lean
structure Fluxes where
  /-- The chirality flux. -/
  M : ℤ
  /-- The hypercharge flux. -/
  N : ℤ
deriving DecidableEq
```

### A.1. Repr instance on `Fluxes`

**An instance with no name**, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L157).

```lean
instance : Repr Fluxes
```

### A.2. Extensionality lemma for the fluxes

**`FTheory.SU5.Fluxes.ext_iff`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L166).

```lean
lemma ext_iff {f1 f2 : Fluxes} : f1 = f2 ↔ f1.M = f2.M ∧ f1.N = f2.N
```

**An instance with no name**, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L169).

```lean
instance : Zero Fluxes
```

### A.3. The zero flux

**`FTheory.SU5.Fluxes.zero_M`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L178).

```lean
lemma zero_M : (0 : Fluxes).M = 0
```

**`FTheory.SU5.Fluxes.zero_N`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L181).

```lean
lemma zero_N : (0 : Fluxes).N = 0
```

### A.4. Addition of fluxes

**An instance with no name**, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L189).

```lean
instance : Add Fluxes
```

**`FTheory.SU5.Fluxes.add_M`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L193).

```lean
lemma add_M (f1 f2 : Fluxes) : (f1 + f2).M = f1.M + f2.M
```

**`FTheory.SU5.Fluxes.add_N`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L196).

```lean
lemma add_N (f1 f2 : Fluxes) : (f1 + f2).N = f1.N + f2.N
```

### A.5. The instance of an additive commutative monoid on fluxes

**An instance with no name**, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L204).

```lean
instance : AddCommMonoid Fluxes
```

## B. Fluxes of the 5d matter representation

**`FTheory.SU5.FluxesFive`**, an abbrev, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L222).

> The fluxes `(M, N)` of the 5-bar matter curves of a theory.

```lean
abbrev FluxesFive : Type
```

### B.1. Decidability instance on `FluxesFive`

**An instance with no name**, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L232).

```lean
instance : DecidableEq FluxesFive
```

### B.2. The proposition for no element to be zero

**`FTheory.SU5.FluxesFive.HasNoZero`**, an abbrev, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L243).

> The proposition on `FluxesFive` such that `(0, 0)` is not in `F`
> and as such each component in `F` leads to chiral matter.

```lean
abbrev HasNoZero (F : FluxesFive) : Prop
```

### B.3. The SM representation `D = (bar 3,1)_{1/3}`

#### B.3.1. Chiral indices of `D`

**`FTheory.SU5.FluxesFive.chiralIndicesOfD`**, a def, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L259).

> The multiset of chiral indices of the representation `D = (bar 3,1)_{1/3}`
> arising from the matter 5d representations.

```lean
def chiralIndicesOfD (F : FluxesFive) : Multiset ℤ
```

#### B.3.2. The number of chiral `D`

**`FTheory.SU5.FluxesFive.numChiralD`**, a def, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L269).

> The total number of chiral `D` representations arising from the matter 5d
> representations.

```lean
def numChiralD (F : FluxesFive) : ℤ
```

#### B.3.3. The number of anti-chiral `D`

**`FTheory.SU5.FluxesFive.numAntiChiralD`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L280).

> The total number of anti-chiral `D` representations arising from the matter 5d
> representations.

```lean
def numAntiChiralD (F : FluxesFive) : ℤ
```

#### B.3.4. Relation between number of chiral and anti-chiral `D`

**`FTheory.SU5.FluxesFive.numChiralD_eq_sum_sub_numAntiChiralD`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L289).

```lean
lemma numChiralD_eq_sum_sub_numAntiChiralD (F : FluxesFive) :
    F.numChiralD = (chiralIndicesOfD F).sum - F.numAntiChiralD
```

### B.4. The SM representation `L = (1,2)_{-1/2}`

#### B.4.1. Chiral indices of `L`

**`FTheory.SU5.FluxesFive.chiralIndicesOfL`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L308).

> The multiset of chiral indices of the representation `L = (1,2)_{-1/2}`
> arising from the matter 5d representations.

```lean
def chiralIndicesOfL (F : FluxesFive) : Multiset ℤ
```

#### B.4.2. The number of chiral `L`

**`FTheory.SU5.FluxesFive.numChiralL`**, a def, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L318).

> The total number of chiral `L` representations arising from the matter 5d
> representations.

```lean
def numChiralL (F : FluxesFive) : ℤ
```

#### B.4.3. The number of anti-chiral `L`

**`FTheory.SU5.FluxesFive.numAntiChiralL`**, a def, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L329).

> The total number of anti-chiral `L` representations arising from the matter 5d
> representations.

```lean
def numAntiChiralL (F : FluxesFive) : ℤ
```

#### B.4.4. Relation between number of chiral and anti-chiral `L`

**`FTheory.SU5.FluxesFive.numChiralL_eq_sum_sub_numAntiChiralL`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L338).

```lean
lemma numChiralL_eq_sum_sub_numAntiChiralL (F : FluxesFive) :
    F.numChiralL = (chiralIndicesOfL F).sum - F.numAntiChiralL
```

### B.5. No exotics from the 5-bar matter fields

**`FTheory.SU5.FluxesFive.NoExotics`**, a def, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L354).

> The condition that the 5d-matter representations do not lead to exotic chiral matter in the
>   MSSM spectrum. This corresponds to the conditions that:
> - There are 3 chiral `L` representations and no anti-chiral `L` representations.
> - There are 3 chiral `D` representations and no anti-chiral `D` representations.

```lean
def NoExotics (F : FluxesFive) : Prop
```

**An instance with no name**, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L357).

```lean
instance (F : FluxesFive) : Decidable (F.NoExotics)
```

## C. Fluxes of the 10d matter representation

**`FTheory.SU5.FluxesTen`**, an abbrev, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L369).

> The fluxes `(M, N)` of the 10d matter curves of a theory.

```lean
abbrev FluxesTen : Type
```

### C.1. Decidability instance on `FluxesTen`

**An instance with no name**, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L379).

```lean
instance : DecidableEq FluxesTen
```

### C.2. The proposition for no element to be zero

**`FTheory.SU5.FluxesTen.HasNoZero`**, an abbrev, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L390).

> The proposition on `FluxesTen` such that `(0, 0)` is not in `F`
> and as such each component in `F` leads to chiral matter.

```lean
abbrev HasNoZero (F : FluxesTen) : Prop
```

### C.3. The SM representation `Q = (3,2)_{1/6}`

#### C.3.1. Chiral indices of `Q`

**`FTheory.SU5.FluxesTen.chiralIndicesOfQ`**, a def, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L406).

> The multiset of chiral indices of the representation `Q = (3,2)_{1/6}`
> arising from the matter 10d representations, corresponding to `M`.

```lean
def chiralIndicesOfQ (F : FluxesTen) : Multiset ℤ
```

#### C.3.2. The number of chiral `Q`

**`FTheory.SU5.FluxesTen.numChiralQ`**, a def, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L416).

> The total number of chiral `Q` representations arising from the matter 10d
> representations.

```lean
def numChiralQ (F : FluxesTen) : ℤ
```

#### C.3.3. The number of anti-chiral `Q`

**`FTheory.SU5.FluxesTen.numAntiChiralQ`**, a def, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L426).

> The total number of anti-chiral `Q` representations arising from the matter 10d
> representations.

```lean
def numAntiChiralQ (F : FluxesTen) : ℤ
```

#### C.3.4. Relation between number of chiral and anti-chiral `Q`

**`FTheory.SU5.FluxesTen.numChiralQ_eq_sum_sub_numAntiChiralQ`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L434).

```lean
lemma numChiralQ_eq_sum_sub_numAntiChiralQ (F : FluxesTen) :
    F.numChiralQ = (chiralIndicesOfQ F).sum - F.numAntiChiralQ
```

### C.4. The SM representation `U = (bar 3,1)_{-2/3}`

#### C.4.1. Chiral indices of `U`

**`FTheory.SU5.FluxesTen.chiralIndicesOfU`**, a def, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L453).

> The multiset of chiral indices of the representation `U = (bar 3,1)_{-2/3}`
> arising from the matter 10d representations, corresponding to `M - N`

```lean
def chiralIndicesOfU (F : FluxesTen) : Multiset ℤ
```

#### C.4.2. The number of chiral `U`

**`FTheory.SU5.FluxesTen.numChiralU`**, a def, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L463).

> The total number of chiral `U` representations arising from the matter 10d
> representations.

```lean
def numChiralU (F : FluxesTen) : ℤ
```

#### C.4.3. The number of anti-chiral `U`

**`FTheory.SU5.FluxesTen.numAntiChiralU`**, a def, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L473).

> The total number of anti-chiral `U` representations arising from the matter 10d
> representations.

```lean
def numAntiChiralU (F : FluxesTen) : ℤ
```

**`FTheory.SU5.FluxesTen.numChiralU_eq_sum_sub_numAntiChiralU`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L481).

```lean
lemma numChiralU_eq_sum_sub_numAntiChiralU (F : FluxesTen) :
    F.numChiralU = (chiralIndicesOfU F).sum - F.numAntiChiralU
```

### C.5. The SM representation `E = (1,1)_{1}`

#### C.5.1. Chiral indices of `E`

**`FTheory.SU5.FluxesTen.chiralIndicesOfE`**, a def, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L499).

> The multiset of chiral indices of the representation `E = (1,1)_{1}`
> arising from the matter 10d representations, corresponding to `M + N`

```lean
def chiralIndicesOfE (F : FluxesTen) : Multiset ℤ
```

#### C.5.2. The number of chiral `E`

**`FTheory.SU5.FluxesTen.numChiralE`**, a def, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L509).

> The total number of chiral `E` representations arising from the matter 10d
> representations.

```lean
def numChiralE (F : FluxesTen) : ℤ
```

#### C.5.3. The number of anti-chiral `E`

**`FTheory.SU5.FluxesTen.numAntiChiralE`**, a def, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L519).

> The total number of anti-chiral `E` representations arising from the matter 10d
> representations.

```lean
def numAntiChiralE (F : FluxesTen) : ℤ
```

#### C.5.4. Relation between number of chiral and anti-chiral `E`

**`FTheory.SU5.FluxesTen.numChiralE_eq_sum_sub_numAntiChiralE`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L527).

```lean
lemma numChiralE_eq_sum_sub_numAntiChiralE (F : FluxesTen) :
    F.numChiralE = (chiralIndicesOfE F).sum - F.numAntiChiralE
```

### C.6. No exotics from the 10d matter fields

**`FTheory.SU5.FluxesTen.NoExotics`**, a def, [line 544](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L544).

> The condition that the 10d-matter representations do not lead to exotic chiral matter in the
>   MSSM spectrum. This corresponds to the conditions that:
> - There are 3 chiral `Q` representations and no anti-chiral `Q` representations.
> - There are 3 chiral `U` representations and no anti-chiral `U` representations.
> - There are 3 chiral `E` representations and no anti-chiral `E` representations.

```lean
def NoExotics (F : FluxesTen) : Prop
```

**An instance with no name**, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean#L549).

```lean
instance (F : FluxesTen) : Decidable (F.NoExotics)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/Basic.lean)
