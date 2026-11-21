---
catalog: module
lean: Polynomial.Bivariate.monomial, Polynomial.Bivariate.natWeightedDegree_add_le, Polynomial.Bivariate.natWeightedDegree_sum_le, Polynomial.Bivariate.natWeightedDegree_smul_le, Polynomial.Bivariate.degree_eval_le_weightedDegree, Polynomial.Bivariate.natWeightedDegree_monomial
statement: formalized
proof: formalized
---

# Mathlib-Facing Bivariate Weighted-Degree Helpers

`CompPoly.ToMathlib.Polynomial.BivariateWeightedDegree`, in [CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean), by Quang Dao.

> This file extends `Polynomial.Bivariate` with weighted-degree algebra that is generic
> and reusable across downstream protocol developments.

`Polynomial.Bivariate.monomial` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean#L35))

> The monomial `X^i Y^j` as a bivariate polynomial.

```lean
def monomial (i j : ℕ) : F[X][Y]
```

`Polynomial.Bivariate.natWeightedDegree_add_le` (lemma, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean#L39))

> The weighted degree of a sum is at most the maximum of the weighted degrees.

```lean
lemma natWeightedDegree_add_le (p q : F[X][Y]) (u v : ℕ) :
    natWeightedDegree (p + q) u v ≤ max (natWeightedDegree p u v) (natWeightedDegree q u v)
```

`Polynomial.Bivariate.natWeightedDegree_sum_le` (lemma, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean#L65))

> The weighted degree of a sum is bounded by the supremum of the weighted degrees.

```lean
lemma natWeightedDegree_sum_le {ι : Type*} (s : Finset ι) (f : ι → F[X][Y]) (u v : ℕ) :
    natWeightedDegree (∑ i ∈ s, f i) u v ≤ s.sup (fun i ↦ natWeightedDegree (f i) u v)
```

`Polynomial.Bivariate.natWeightedDegree_smul_le` (lemma, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean#L76))

> The weighted degree of a scalar multiple is at most the weighted degree of the polynomial.

```lean
lemma natWeightedDegree_smul_le (a : F) (p : F[X][Y]) (u v : ℕ) :
    natWeightedDegree (a • p) u v ≤ natWeightedDegree p u v
```

`Polynomial.Bivariate.degree_eval_le_weightedDegree` (lemma, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean#L90))

> The degree of `Q(X, P(X))` is bounded by the weighted degree of `Q`,
> provided `deg(P) ≤ k - 1`.

```lean
lemma degree_eval_le_weightedDegree (Q : F[X][Y]) (P : F[X]) (k : ℕ) (hP : P.natDegree ≤ k - 1) :
    (Q.eval P).natDegree ≤ natWeightedDegree Q 1 (k - 1)
```

`Polynomial.Bivariate.natWeightedDegree_monomial` (lemma, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean#L113))

> The weighted degree of `X^i Y^j` is `u * i + v * j`.

```lean
lemma natWeightedDegree_monomial (i j u v : ℕ) :
    natWeightedDegree (monomial (F := F) i j) u v = u * i + v * j
```

## Depends on

- [Mathlib-Facing Bivariate Degree Helpers](bivariatedegree.md)

## Sources

- [CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/ToMathlib/Polynomial/BivariateWeightedDegree.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Polynomial.BivariateWeightedDegree.json)
