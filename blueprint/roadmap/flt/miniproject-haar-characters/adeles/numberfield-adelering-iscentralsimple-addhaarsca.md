---
declaration: theorem
origin: cited
lean: NumberField.AdeleRing.isCentralSimple_addHaarScalarFactor_left_mul_eq_right_mul
statement: formalized
---

# NumberField.AdeleRing.isCentralSimple_addHaarScalarFactor_left_mul_eq_right_mul

Let $B$ be a finite-dimensional central simple $K$-algebra. Say $u\in B_{\mathbb{A}}^\times$, and define $\ell_u$ and $r_u:B_{\mathbb{A}}\to B_{\mathbb{A}}$ by $\ell_u(x)=ux$ and $r_u(x)=xu$. Then $d_{B_{\mathbb{A}}}(\ell_u)=d_{B_{\mathbb{A}}}(r_u)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar_restrictedProductCongrRight](../restricted-products/measuretheory-addequivaddhaarchar-restrictedprod.md)
- [IsSimpleRing.ringHaarChar_eq_addEquivAddHaarChar_mulRight](../left-and-right-multiplication/issimplering-ringhaarchar-eq-addequivaddhaarchar.md)

## Proof

We think of $B_{\mathbb{A}}$ as $B\otimes_K\mathbb{A}_K$. If $u=(u_v)$ as $v$ runs through the places of $K$ then $d_{B_{\mathbb{A}}}(\ell_u)=\prod_v d_{B_v}(\ell_{u_v})$ by theorem [MeasureTheory.addEquivAddHaarChar_restrictedProductCongrRight](../restricted-products/measuretheory-addequivaddhaarchar-restrictedprod.md) (and the product is finite). By corollary [IsSimpleRing.ringHaarChar_eq_addEquivAddHaarChar_mulRight](../left-and-right-multiplication/issimplering-ringhaarchar-eq-addequivaddhaarchar.md) this equals $\prod_v d_{B_v}(r_{u_v})$, and again by theorem [MeasureTheory.addEquivAddHaarChar_restrictedProductCongrRight](../restricted-products/measuretheory-addequivaddhaarchar-restrictedprod.md) this is $d_{B_{\mathbb{A}}}(r_u)$.

## Lean

Stated as [`NumberField.AdeleRing.isCentralSimple_addHaarScalarFactor_left_mul_eq_right_mul`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.isCentralSimple_addHaarScalarFactor_left_mul_eq_right_mul); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 787](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L787)
