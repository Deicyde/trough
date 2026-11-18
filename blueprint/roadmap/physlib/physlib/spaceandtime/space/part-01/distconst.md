---
declaration: module
origin: cited
lean: Space.distConst, Space.distDeriv_distConst, Space.distGrad_distConst, Space.distDiv_distConst, Space.distCurl_distConst
statement: formalized
proof: formalized
---

# The constant distribution on space

The module `Physlib.SpaceAndTime.Space.DistConst`, [Physlib/SpaceAndTime/Space/DistConst.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistConst.lean): 5 declarations, 1 with a docstring.

## i. Overview

> In this module we define the constant distribution from `Space d` to a module `M`.
> That is the distribution which sends every Schwartz function to its
> integral multiplied by a fixed element `m : M`.
>
> We show that the derivatives of this constant distribution are zero.

## ii. Key results

> - `distConst` : The constant distribution from `Space d` to a module `M`.

## iv. References

> * None.

## A. The definition of the constant distribution

**`Space.distConst`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistConst.lean#L49).

> The constant distribution from `Space d` to a module `M` associated with
> `m : M`.

```lean
noncomputable def distConst {M } [NormedAddCommGroup M] [NormedSpace ℝ M] (d : ℕ) (m : M) :
    (Space d) →d[ℝ] M
```

## B. Derivatives of the constant distribution

**`Space.distDeriv_distConst`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistConst.lean#L59).

```lean
lemma distDeriv_distConst {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin d) (m : M) :
    distDeriv μ (distConst d m) = 0
```

**`Space.distGrad_distConst`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistConst.lean#L65).

```lean
lemma distGrad_distConst {d} (m : ℝ) :
    distGrad (distConst d m) = 0
```

**`Space.distDiv_distConst`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistConst.lean#L70).

```lean
lemma distDiv_distConst {d} (m : EuclideanSpace ℝ (Fin d)) :
    distDiv (distConst d m) = 0
```

**`Space.distCurl_distConst`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistConst.lean#L75).

```lean
lemma distCurl_distConst (m : EuclideanSpace ℝ (Fin 3)) :
    distCurl (distConst 3 m) = 0
```

## Depends on

- [Curl on Space](derivatives-curl.md)

## Sources

- [Physlib/SpaceAndTime/Space/DistConst.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistConst.lean)
