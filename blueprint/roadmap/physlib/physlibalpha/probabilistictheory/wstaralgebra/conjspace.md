---
declaration: module
origin: cited
lean: ProbabilisticTheory.ConjSpace, ProbabilisticTheory.ConjSpace.toConj, ProbabilisticTheory.ConjSpace.ofConj, ProbabilisticTheory.ConjSpace.ofConj_toConj, ProbabilisticTheory.ConjSpace.toConj_ofConj, ProbabilisticTheory.ConjSpace.instAddCommGroup, ProbabilisticTheory.ConjSpace.ofConj_add, ProbabilisticTheory.ConjSpace.ofConj_zero
statement: formalized
proof: formalized
---

# The complex conjugate of a normed space

The module `PhyslibAlpha.ProbabilisticTheory.WStarAlgebra.ConjSpace`, [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean): 19 declarations, 7 with a docstring.

> The complex conjugate `ConjSpace X` of a complex normed space, with twisted scalar action.

## i. Overview

> `ConjSpace X` is `X` with scalar multiplication twisted by complex conjugation: `c • x` in
> `ConjSpace X` is `conj c • x` in `X`. It turns conjugate-linear maps on `X` into linear maps on
> `ConjSpace X`.

## ii. Key results

> - `ConjSpace` : the complex conjugate of a normed space.
> - `ConjSpace.toConj`, `ConjSpace.ofConj` : the identity maps between `X` and `ConjSpace X`.
> - `ConjSpace.instNormedSpace` : the conjugate normed space structure.

## iv. References

> * None.

## A. The conjugate space and the identity maps

**`ProbabilisticTheory.ConjSpace`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L55).

> The complex conjugate of `X`: the same type, with `c • x = conj c • x`.

```lean
def ConjSpace (X : Type*) : Type _
```

**`ProbabilisticTheory.ConjSpace.toConj`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L64).

> The identity, viewed as the map from `X` into `ConjSpace X`. Spelled out explicitly (instead
> of relying on the bare definitional equality `ConjSpace X := X`) to keep instance search from
> having to guess which scalar action a plain type ascription intends.

```lean
def toConj (x : X) : ConjSpace X
```

**`ProbabilisticTheory.ConjSpace.ofConj`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L67).

> The identity, viewed as the map from `ConjSpace X` back into `X`.

```lean
def ofConj (x : ConjSpace X) : X
```

**`ProbabilisticTheory.ConjSpace.ofConj_toConj`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L69).

```lean
lemma ofConj_toConj (x : X) : ofConj (toConj x) = x
```

**`ProbabilisticTheory.ConjSpace.toConj_ofConj`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L70).

```lean
lemma toConj_ofConj (x : ConjSpace X) : toConj (ofConj x) = x
```

## B. The additive and normed group structure

**`ProbabilisticTheory.ConjSpace.instAddCommGroup`**, an instance, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L78).

```lean
instance instAddCommGroup [AddCommGroup X] : AddCommGroup (ConjSpace X)
```

**`ProbabilisticTheory.ConjSpace.ofConj_add`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L80).

```lean
lemma ofConj_add [AddCommGroup X] (x y : ConjSpace X) :
    ofConj (x + y) = ofConj x + ofConj y
```

**`ProbabilisticTheory.ConjSpace.ofConj_zero`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L83).

```lean
lemma ofConj_zero [AddCommGroup X] : ofConj (0 : ConjSpace X) = 0
```

**`ProbabilisticTheory.ConjSpace.toConj_add`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L85).

```lean
lemma toConj_add [AddCommGroup X] (x y : X) :
    toConj (x + y) = toConj x + toConj y
```

**`ProbabilisticTheory.ConjSpace.toConj_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L88).

```lean
lemma toConj_zero [AddCommGroup X] : toConj (0 : X) = 0
```

**`ProbabilisticTheory.ConjSpace.instNormedAddCommGroup`**, an instance, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L90).

```lean
instance instNormedAddCommGroup [NormedAddCommGroup X] :
    NormedAddCommGroup (ConjSpace X)
```

**`ProbabilisticTheory.ConjSpace.norm_ofConj`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L93).

```lean
lemma norm_ofConj [NormedAddCommGroup X] (x : ConjSpace X) : ‖ofConj x‖ = ‖x‖
```

**`ProbabilisticTheory.ConjSpace.norm_toConj`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L95).

```lean
lemma norm_toConj [NormedAddCommGroup X] (x : X) : ‖toConj x‖ = ‖x‖
```

## C. The conjugate scalar action

**`ProbabilisticTheory.ConjSpace.instSMul`**, an instance, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L107).

> The twisted scalar action: `c • x := (starRingEnd ℂ c) • ofConj x`, moved back into
> `ConjSpace X` via `toConj`.

```lean
instance instSMul : SMul ℂ (ConjSpace X)
```

**`ProbabilisticTheory.ConjSpace.smul_def`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L110).

```lean
lemma smul_def (c : ℂ) (x : ConjSpace X) :
    c • x = toConj ((starRingEnd ℂ c) • ofConj x)
```

**`ProbabilisticTheory.ConjSpace.ofConj_smul`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L113).

```lean
lemma ofConj_smul (c : ℂ) (x : ConjSpace X) :
    ofConj (c • x) = (starRingEnd ℂ c) • ofConj x
```

**`ProbabilisticTheory.ConjSpace.instModule`**, an instance, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L117).

> The conjugate module structure on `ConjSpace X`.

```lean
instance instModule : Module ℂ (ConjSpace X)
```

**`ProbabilisticTheory.ConjSpace.instNormedSpace`**, an instance, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L130).

> The norm on `ConjSpace X` is literally `X`'s norm (via `ofConj`), so `norm_smul_le` reduces to
> `‖conj c‖ = ‖c‖` (`Complex.norm_conj`) composed with `X`'s own `norm_smul_le`.

```lean
instance instNormedSpace : NormedSpace ℂ (ConjSpace X)
```

**`ProbabilisticTheory.ConjSpace.instCompleteSpace`**, an instance, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean#L136).

> `ConjSpace X` is complete when `X` is.

```lean
instance instCompleteSpace [CompleteSpace X] : CompleteSpace (ConjSpace X)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/ConjSpace.lean)
