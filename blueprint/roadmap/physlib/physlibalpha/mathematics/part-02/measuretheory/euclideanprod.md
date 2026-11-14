---
declaration: module
origin: cited
lean: EuclideanProd.integral_withLp_prod, EuclideanProd.integrable_withLp_prod, EuclideanProd.norm_le_norm_toLp_right, EuclideanProd.norm_toLp_zero
statement: formalized
proof: formalized
---

# Integration over the Euclidean product

The module `PhyslibAlpha.Mathematics.MeasureTheory.EuclideanProd`, [PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean): 4 declarations, 4 with a docstring.

> The Euclidean product `WithLp 2 (E × F)` carries the product of the Lebesgue measures.

## i. Overview

> The `L²` product of two finite dimensional inner product spaces is measure preservingly equivalent
> to the plain product. Integrals over it are iterated integrals. The norm of a point dominates the
> norm of each coordinate.

## ii. Key results

> - `EuclideanProd.integral_withLp_prod` : integration over the Euclidean product.
> - `EuclideanProd.integrable_withLp_prod` : integrability over the Euclidean product.

## iv. References

> None.

## A. Integration

> - `EuclideanProd.integral_withLp_prod` : integration over the Euclidean product.
> - `EuclideanProd.integrable_withLp_prod` : integrability over the Euclidean product.

## B. Norms

> - `EuclideanProd.norm_le_norm_toLp_right` : the second coordinate is dominated by the norm.
> - `EuclideanProd.norm_toLp_zero` : the norm of a point with vanishing second coordinate.

**`EuclideanProd.integral_withLp_prod`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean#L61).

> Integration over the Euclidean product is iterated integration.

```lean
lemma integral_withLp_prod {G : Type*} [NormedAddCommGroup G] [NormedSpace ℝ G]
    (φ : WithLp 2 (E × F) → G) :
    ∫ z, φ z = ∫ p : E × F, φ (WithLp.toLp 2 p)
```

**`EuclideanProd.integrable_withLp_prod`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean#L69).

> Integrability over the Euclidean product is integrability over the product.

```lean
lemma integrable_withLp_prod {G : Type*} [NormedAddCommGroup G] {φ : WithLp 2 (E × F) → G}
    (hφ : Integrable φ) : Integrable (fun p : E × F => φ (WithLp.toLp 2 p))
```

**`EuclideanProd.norm_le_norm_toLp_right`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean#L77).

> The second coordinate is dominated by the norm of the point.

```lean
lemma norm_le_norm_toLp_right (x : E) (y : F) : ‖y‖ ≤ ‖WithLp.toLp 2 (x, y)‖
```

**`EuclideanProd.norm_toLp_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean#L84).

> The norm of a point with vanishing second coordinate.

```lean
lemma norm_toLp_zero (ξ : E) : ‖WithLp.toLp 2 (ξ, (0 : F))‖ = ‖ξ‖
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/EuclideanProd.lean)
