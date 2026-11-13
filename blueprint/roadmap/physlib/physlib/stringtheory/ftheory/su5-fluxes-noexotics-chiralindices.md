---
declaration: module
origin: cited
lean: FTheory.SU5.FluxesFive.chiralIndicesOfD_noneg_of_noExotics, FTheory.SU5.FluxesFive.chiralIndicesOfL_noneg_of_noExotics, FTheory.SU5.FluxesTen.chiralIndicesOfQ_noneg_of_noExotics, FTheory.SU5.FluxesTen.chiralIndicesOfU_noneg_of_noExotics, FTheory.SU5.FluxesTen.chiralIndicesOfE_noneg_of_noExotics, FTheory.SU5.FluxesFive.chiralIndicesOfD_sum_eq_three_of_noExotics, FTheory.SU5.FluxesFive.chiralIndicesOfL_sum_eq_three_of_noExotics, FTheory.SU5.FluxesTen.chiralIndicesOfQ_sum_eq_three_of_noExotics
statement: formalized
proof: formalized
---

# Constraints on chiral indices from the condition of no chiral exotics

The module `Physlib.StringTheory.FTheory.SU5.Fluxes.NoExotics.ChiralIndices`, [Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean): 25 declarations, 14 with a docstring.

## i. Overview

> The chiral indices of each of the standard model representations
> satisfy certain constraints if there are no chiral exotics in the spectrum.
> We give prove these constraints in this file.

## ii. Key results

> Each of the following results holds for each of the standard model representations,
> we state them for the representation `D = (bar 3,1)_{1/3}` only:
> - Each chiral index is non-negative, `FluxesFive.chiralIndicesOfD_noneg_of_noExotics`.
> - The sum of the chiral indices is equal to three,
>   `FluxesFive.chiralIndicesOfD_sum_eq_three_of_noExotics`.
> - Each chiral index is less then or equal to three,
>   `FluxesFive.chiralIndicesOfD_le_three_of_noExotics`.
> - Each chiral index is `0`, `1`, `2` or `3`,
>   `FluxesFive.mem_chiralIndicesOfD_mem_of_noExotics`
> - The sum of a subset of the chiral indices is less then or equal to three,
>   `FluxesFive.chiralIndicesOfD_subset_sum_le_three_of_noExotics`.

## iv. References

> * None.

## A. Positivity of the chiral indices given no exotics

> The chiral indices of all the SM representations are non-negative if there are no chiral exotics.

**`FTheory.SU5.FluxesFive.chiralIndicesOfD_noneg_of_noExotics`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L66).

> The chiral indices of the representations `D = (bar 3,1)_{1/3}` are all non-negative if
> there are no chiral exotics in the spectrum.

```lean
lemma FluxesFive.chiralIndicesOfD_noneg_of_noExotics (F : FluxesFive) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfD) : 0 ≤ ci
```

**`FTheory.SU5.FluxesFive.chiralIndicesOfL_noneg_of_noExotics`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L84).

> The chiral indices of the representations `L = (1,2)_{-1/2}` are all non-negative if
> there are no chiral exotics in the spectrum.

```lean
lemma FluxesFive.chiralIndicesOfL_noneg_of_noExotics (F : FluxesFive) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfL) : 0 ≤ ci
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfQ_noneg_of_noExotics`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L102).

> The chiral indices of the representations `Q = (3,2)_{1/6}` are all non-negative if
> there are no chiral exotics in the spectrum.

```lean
lemma FluxesTen.chiralIndicesOfQ_noneg_of_noExotics (F : FluxesTen) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfQ) : 0 ≤ ci
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfU_noneg_of_noExotics`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L120).

> The chiral indices of the representations `U = (bar 3,1)_{-2/3}` are all non-negative if
> there are no chiral exotics in the spectrum.

```lean
lemma FluxesTen.chiralIndicesOfU_noneg_of_noExotics (F : FluxesTen) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfU) : 0 ≤ ci
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfE_noneg_of_noExotics`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L136).

```lean
lemma FluxesTen.chiralIndicesOfE_noneg_of_noExotics (F : FluxesTen) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfE) : 0 ≤ ci
```

## B. Chiral indices sum to three given no exotics

> The sum of the chiral indices of each representation is equal to three if
> there are no chiral exotics.

**`FTheory.SU5.FluxesFive.chiralIndicesOfD_sum_eq_three_of_noExotics`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L163).

> The sum of the chiral indices of the representations `D = (bar 3,1)_{1/3}` is equal
> to `3` in the presences of no exotics.

```lean
lemma FluxesFive.chiralIndicesOfD_sum_eq_three_of_noExotics (F : FluxesFive) (hF : NoExotics F) :
    F.chiralIndicesOfD.sum = 3
```

**`FTheory.SU5.FluxesFive.chiralIndicesOfL_sum_eq_three_of_noExotics`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L171).

> The sum of the chiral indices of the representations `L = (1,2)_{-1/2}` is equal
> to `3` in the presences of no exotics.

```lean
lemma FluxesFive.chiralIndicesOfL_sum_eq_three_of_noExotics (F : FluxesFive) (hF : NoExotics F) :
    F.chiralIndicesOfL.sum = 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfQ_sum_eq_three_of_noExotics`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L179).

> The sum of the chiral indices of the representations `Q = (3,2)_{1/6}` is equal
> to `3` in the presences of no exotics.

```lean
lemma FluxesTen.chiralIndicesOfQ_sum_eq_three_of_noExotics (F : FluxesTen) (hF : NoExotics F) :
    F.chiralIndicesOfQ.sum = 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfU_sum_eq_three_of_noExotics`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L187).

> The sum of the chiral indices of the representations `U = (bar 3,1)_{-2/3}` is equal
> to `3` in the presences of no exotics.

```lean
lemma FluxesTen.chiralIndicesOfU_sum_eq_three_of_noExotics (F : FluxesTen) (hF : NoExotics F) :
    F.chiralIndicesOfU.sum = 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfE_sum_eq_three_of_noExotics`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L195).

> The sum of the chiral indices of the representations `E = (1,1)_{1}` is equal
> to `3` in the presences of no exotics.

```lean
lemma FluxesTen.chiralIndicesOfE_sum_eq_three_of_noExotics (F : FluxesTen) (hF : NoExotics F) :
    F.chiralIndicesOfE.sum = 3
```

## C. Each chiral index is less then or equal to three given no exotics

**`FTheory.SU5.FluxesFive.chiralIndicesOfD_le_three_of_noExotics`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L209).

> The chiral indices of the representation `D = (bar 3,1)_{1/3}` are less then
> or equal to `3`.

```lean
lemma FluxesFive.chiralIndicesOfD_le_three_of_noExotics (F : FluxesFive) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfD) : ci ≤ 3
```

**`FTheory.SU5.FluxesFive.chiralIndicesOfL_le_three_of_noExotics`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L217).

> The chiral indices of the representation `L = (1,2)_{-1/2}` are less then
> or equal to `3`.

```lean
lemma FluxesFive.chiralIndicesOfL_le_three_of_noExotics (F : FluxesFive) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfL) : ci ≤ 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfQ_le_three_of_noExotics`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L225).

> The chiral indices of the representation `Q = (3,2)_{1/6}` are less then
> or equal to `3`.

```lean
lemma FluxesTen.chiralIndicesOfQ_le_three_of_noExotics (F : FluxesTen) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfQ) : ci ≤ 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfU_le_three_of_noExotics`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L233).

> The chiral indices of the representation `U = (bar 3,1)_{-2/3}` are less then
> or equal to `3`.

```lean
lemma FluxesTen.chiralIndicesOfU_le_three_of_noExotics (F : FluxesTen) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfU) : ci ≤ 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfE_le_three_of_noExotics`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L241).

> The chiral indices of the representation `E = (1,1)_{1}` are less then
> or equal to `3`.

```lean
lemma FluxesTen.chiralIndicesOfE_le_three_of_noExotics (F : FluxesTen) (hF : NoExotics F)
    (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfE) : ci ≤ 3
```

## D. Each chiral index is 0, 1, 2, or 3 given no exotics

**`FTheory.SU5.FluxesFive.mem_chiralIndicesOfD_mem_of_noExotics`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L253).

```lean
lemma FluxesFive.mem_chiralIndicesOfD_mem_of_noExotics (F : FluxesFive)
    (hF : NoExotics F) (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfD) :
    ci ∈ ({0, 1, 2, 3} : Finset ℤ)
```

**`FTheory.SU5.FluxesFive.mem_chiralIndicesOfL_mem_of_noExotics`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L261).

```lean
lemma FluxesFive.mem_chiralIndicesOfL_mem_of_noExotics (F : FluxesFive)
    (hF : NoExotics F) (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfL) :
    ci ∈ ({0, 1, 2, 3} : Finset ℤ)
```

**`FTheory.SU5.FluxesTen.mem_chiralIndicesOfQ_mem_of_noExotics`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L269).

```lean
lemma FluxesTen.mem_chiralIndicesOfQ_mem_of_noExotics (F : FluxesTen)
    (hF : NoExotics F) (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfQ) :
    ci ∈ ({0, 1, 2, 3} : Finset ℤ)
```

**`FTheory.SU5.FluxesTen.mem_chiralIndicesOfU_mem_of_noExotics`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L277).

```lean
lemma FluxesTen.mem_chiralIndicesOfU_mem_of_noExotics (F : FluxesTen)
    (hF : NoExotics F) (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfU) :
    ci ∈ ({0, 1, 2, 3} : Finset ℤ)
```

**`FTheory.SU5.FluxesTen.mem_chiralIndicesOfE_mem_of_noExotics`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L285).

```lean
lemma FluxesTen.mem_chiralIndicesOfE_mem_of_noExotics (F : FluxesTen)
    (hF : NoExotics F) (ci : ℤ) (hci : ci ∈ F.chiralIndicesOfE) :
    ci ∈ ({0, 1, 2, 3} : Finset ℤ)
```

## E. Sum of a subset of chiral indices is less then or equal to 3 given no exotics

**`FTheory.SU5.FluxesFive.chiralIndicesOfD_subset_sum_le_three_of_noExotics`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L299).

```lean
lemma FluxesFive.chiralIndicesOfD_subset_sum_le_three_of_noExotics (F : FluxesFive)
    (hF : NoExotics F) (S : Multiset Fluxes)
    (hSle : S ≤ F) : (S.map (fun x => x.1)).sum ≤ 3
```

**`FTheory.SU5.FluxesFive.chiralIndicesOfL_subset_sum_le_three_of_noExotics`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L312).

```lean
lemma FluxesFive.chiralIndicesOfL_subset_sum_le_three_of_noExotics (F : FluxesFive)
    (hF : NoExotics F) (S : Multiset Fluxes)
    (hSle : S ≤ F) : (S.map (fun x => (x.1 + x.2))).sum ≤ 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfQ_subset_sum_le_three_of_noExotics`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L325).

```lean
lemma FluxesTen.chiralIndicesOfQ_subset_sum_le_three_of_noExotics (F : FluxesTen)
    (hF : NoExotics F) (S : Multiset Fluxes)
    (hSle : S ≤ F) : (S.map (fun x => x.1)).sum ≤ 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfU_subset_sum_le_three_of_noExotics`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L338).

```lean
lemma FluxesTen.chiralIndicesOfU_subset_sum_le_three_of_noExotics (F : FluxesTen)
    (hF : NoExotics F) (S : Multiset Fluxes)
    (hSle : S ≤ F) : (S.map (fun x => (x.1 - x.2))).sum ≤ 3
```

**`FTheory.SU5.FluxesTen.chiralIndicesOfE_subset_sum_le_three_of_noExotics`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean#L351).

```lean
lemma FluxesTen.chiralIndicesOfE_subset_sum_le_three_of_noExotics (F : FluxesTen)
    (hF : NoExotics F) (S : Multiset Fluxes)
    (hSle : S ≤ F) : (S.map (fun x => (x.1 + x.2))).sum ≤ 3
```

## Depends on

- [Fluxes of representations](su5-fluxes-basic.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Fluxes/NoExotics/ChiralIndices.lean)
