---
catalog: module
lean: CompPoly.CPolynomial.SubproductTree.leafCount, CompPoly.CPolynomial.SubproductTree.interpolateAux, CompPoly.CPolynomial.interpolateSubproduct, CompPoly.CPolynomial.interpolateSubproduct_eq_interpolateArrays
statement: formalized
proof: formalized
---

# Subproduct-Tree Interpolation

`CompPoly.Univariate.BatchEval.Interpolation`, in [CompPoly/Univariate/BatchEval/Interpolation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Interpolation.lean), by Derek Sorensen.

> Fast interpolation on arbitrary distinct nodes, reusing the subproduct tree of
> `BatchEval/SubproductTree.lean`. With `G = ∏ (X - xᵢ)` at the root, the interpolant of the
> values `yᵢ` is
>
>   `∑ᵢ cᵢ · G / (X - xᵢ)`, where `cᵢ = yᵢ / G'(xᵢ)`,
>
> and both halves run over the tree. The weights come from descending with `G'` by
> remainders, as batch evaluation descends with `p`. The sum is then assembled bottom-up as
> `L · M_right + R · M_left` at each node. With an NTT-backed `MulContext` this is the
> classical `O(M(n) log n)` algorithm; it needs no root of unity and no power-of-two size.
>
> ## Main definitions
>
> * `SubproductTree.interpolateAux`: the fused descent and recombination over one tree.
> * `interpolateSubproduct`: interpolation of values on an array of nodes.
>
> ## Main results
>
> * `interpolateSubproduct_eq_interpolateArrays`: for pairwise distinct nodes, the result is
>   the Lagrange interpolant `CLagrange.interpolateArrays`.

`CompPoly.CPolynomial.SubproductTree.leafCount` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Interpolation.lean#L49))

> The number of leaves of a subproduct tree.

```lean
def leafCount [Zero R] : SubproductTree R → Nat
```

`CompPoly.CPolynomial.SubproductTree.interpolateAux` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Interpolation.lean#L58))

> Descend with remainders of `r` and recombine the weighted leaves bottom-up.
>
> At a leaf `x` holding the value `y` the contribution is the constant `y / r(x)`; at a node
> the two children's contributions are cross-multiplied by the sibling's product polynomial.
> Called with `r = G'` on the whole tree this is the Lagrange interpolant.

```lean
def interpolateAux [Field R] [BEq R] [LawfulBEq R] (M : MulContext R) (D : ModContext R) :
    SubproductTree R → CPolynomial R → List R → CPolynomial R
```

`CompPoly.CPolynomial.interpolateSubproduct` (definition, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Interpolation.lean#L72))

> Interpolate the values `ys` on the nodes `xs` through a subproduct tree.
>
> Missing values default to `0`, as in `CLagrange.interpolateArrays`.

```lean
def interpolateSubproduct [Field R] [BEq R] [LawfulBEq R]
    (M : MulContext R) (D : ModContext R) (xs ys : Array R) : CPolynomial R
```

> ### Correctness

`CompPoly.CPolynomial.interpolateSubproduct_eq_interpolateArrays` (theorem, [line 295](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Interpolation.lean#L295))

> On pairwise distinct nodes, subproduct-tree interpolation is Lagrange interpolation.

```lean
theorem interpolateSubproduct_eq_interpolateArrays [Field R] [BEq R] [LawfulBEq R]
    (M : MulContext R) (D : ModContext R) (xs ys : Array R) (hxs : xs.toList.Nodup) :
    interpolateSubproduct M D xs ys = CLagrange.interpolateArrays xs ys
```

## Depends on

- [Subproduct-Tree Batch Evaluation](subproducttree.md)
- [Formal Derivative and Taylor Shift of Computable Univariate Polynomials](../deriv.md)
- [Array Wrappers for Computable Lagrange Interpolation](../lagrangearray.md)

## Proof depends on

- [Batch Evaluation Correctness](correctness.md)
- [`C`, `eval₂`, and coefficient-mapping as ring homomorphisms](../../part-02/topoly/ringhom.md)

## Sources

- [CompPoly/Univariate/BatchEval/Interpolation.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/BatchEval/Interpolation.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.BatchEval.Interpolation.json)
