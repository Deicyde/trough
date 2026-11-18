---
declaration: module
origin: cited
lean: LinearEquiv.ofRelabel, LinearEquiv.euclideanOfRelabel, LinearEquiv.ofRelabel_refl, LinearEquiv.euclideanOfRelabel_refl, Matrix.reindex_toLin', Matrix.reindex_toEuclideanLin, Matrix.reindex_right_toLin', Matrix.reindex_right_toEuclideanLin
statement: formalized
proof: formalized
---

# Relabelling linear equivalences

The module `QuantumInfo.ForMathlib.LinearEquiv`, [QuantumInfo/ForMathlib/LinearEquiv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean): 10 declarations, 2 with a docstring.

## i. Overview

> This module provides linear equivalences obtained by relabelling the index type of a finite
> function space `d → R` or of `EuclideanSpace 𝕜 d` along an index equivalence `e : d ≃ d₂`,
> together with lemmas relating them to `Matrix.reindex`.

## ii. Key results

> - `LinearEquiv.ofRelabel` : the `R`-linear equivalence `(d₂ → R) ≃ₗ[R] (d → R)` induced by an
>   index equivalence `e : d ≃ d₂`.
> - `LinearEquiv.euclideanOfRelabel` : the `EuclideanSpace` analogue of `ofRelabel`.
> - `Matrix.reindex_toLin'` and `Matrix.reindex_toEuclideanLin` : reindexing a matrix conjugates
>   its associated linear map by these relabelling equivalences.

## iv. References

> * None.

## A. Relabelling linear equivalences

**`LinearEquiv.ofRelabel`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L56).

> The `R`-linear equivalence `(d₂ → R) ≃ₗ[R] (d → R)` that relabels the coordinates of a
> function along an index equivalence `e : d ≃ d₂`. This is the linear-equivalence packaging of
> `Equiv.piCongrLeft`.

```lean
def ofRelabel (e : d ≃ d₂) : (d₂ → R) ≃ₗ[R] (d → R)
```

**`LinearEquiv.euclideanOfRelabel`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L68).

> The `𝕜`-linear equivalence `EuclideanSpace 𝕜 d₂ ≃ₗ[𝕜] EuclideanSpace 𝕜 d` that relabels the
> coordinates of a vector along an index equivalence `e : d ≃ d₂`. This is the `EuclideanSpace`
> analogue of `LinearEquiv.ofRelabel`, obtained by transporting it across the `WithLp`
> identifications.

```lean
def euclideanOfRelabel (e : d ≃ d₂) : EuclideanSpace 𝕜 d₂ ≃ₗ[𝕜] EuclideanSpace 𝕜 d
```

**`LinearEquiv.ofRelabel_refl`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L72).

```lean
lemma ofRelabel_refl : ofRelabel R (.refl d) = LinearEquiv.refl R (d → R)
```

**`LinearEquiv.euclideanOfRelabel_refl`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L76).

```lean
lemma euclideanOfRelabel_refl : euclideanOfRelabel 𝕜 (.refl d) =
    LinearEquiv.refl 𝕜 (EuclideanSpace 𝕜 d)
```

## B. Reindexing matrices and their linear maps

**`Matrix.reindex_toLin'`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L94).

```lean
lemma reindex_toLin' (e : d₁ ≃ d₃) (f : d₂ ≃ d) (M : Matrix d₁ d₂ R) :
    (M.reindex e f).toLin' = (LinearEquiv.ofRelabel R e.symm) ∘ₗ
      M.toLin' ∘ₗ (LinearEquiv.ofRelabel R f)
```

**`Matrix.reindex_toEuclideanLin`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L100).

```lean
lemma reindex_toEuclideanLin (e : d₁ ≃ d₃) (f : d₂ ≃ d) (M : Matrix d₁ d₂ 𝕜) :
    (M.reindex e f).toEuclideanLin = (LinearEquiv.euclideanOfRelabel 𝕜 e.symm) ∘ₗ
      M.toEuclideanLin ∘ₗ (LinearEquiv.euclideanOfRelabel 𝕜 f)
```

**`Matrix.reindex_right_toLin'`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L106).

```lean
lemma reindex_right_toLin' (e : d ≃ d₂) (M : Matrix d₃ d R) :
    (M.reindex (.refl d₃) e).toLin' = M.toLin' ∘ₗ (LinearEquiv.ofRelabel R e)
```

**`Matrix.reindex_right_toEuclideanLin`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L111).

```lean
lemma reindex_right_toEuclideanLin (e : d ≃ d₂) (M : Matrix d₃ d 𝕜) :
    (M.reindex (.refl d₃) e).toEuclideanLin =
      M.toEuclideanLin ∘ₗ (LinearEquiv.euclideanOfRelabel 𝕜 e)
```

**`Matrix.reindex_left_toLin'`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L117).

```lean
lemma reindex_left_toLin' (e : d₁ ≃ d₃) (M : Matrix d₁ d₂ R) :
    (M.reindex e (.refl d₂)).toLin' = (LinearEquiv.ofRelabel R e.symm) ∘ M.toLin'
```

**`Matrix.reindex_left_toEuclideanLin`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean#L122).

```lean
lemma reindex_left_toEuclideanLin (e : d₁ ≃ d₃) (M : Matrix d₁ d₂ 𝕜) :
    (M.reindex e (.refl d₂)).toEuclideanLin =
      (LinearEquiv.euclideanOfRelabel 𝕜 e.symm) ∘ M.toEuclideanLin
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/LinearEquiv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/LinearEquiv.lean)
