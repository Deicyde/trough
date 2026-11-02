---
declaration: lemma
origin: cited
lean: MeasureTheory.ringHaarChar_adeles_rat
statement: formalized
proof: formalized
---

# MeasureTheory.ringHaarChar\_adeles\_rat

If $x\in\mathbb{A}_{\mathbb{Q}}^\times$ then $\delta_{\mathbb{A}_{\mathbb{Q}}}(x)=\prod_v|x_v|_v.$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar\_prodCongr](../finite-products/measuretheory-addequivaddhaarchar-prodcongr.md)
- [MeasureTheory.ringHaarChar\_real](../examples/measuretheory-ringhaarchar-real.md)
- [MeasureTheory.addEquivAddHaarChar\_restrictedProductCongrRight](../restricted-products/measuretheory-addequivaddhaarchar-restrictedprod.md)
- [MeasureTheory.ringHaarChar\_padic](../examples/measuretheory-ringhaarchar-padic.md)

## Proof

By theorem [MeasureTheory.addEquivAddHaarChar\_prodCongr](../finite-products/measuretheory-addequivaddhaarchar-prodcongr.md) we have $\delta_{\mathbb{A}_{\mathbb{Q}}}(x)=\delta_{\mathbb{A}_{\mathbb{Q}}^\infty}(x^\infty)\times\delta_{\mathbb{R}}(x_\infty)$. By lemma [MeasureTheory.ringHaarChar\_real](../examples/measuretheory-ringhaarchar-real.md) we have $\delta_{\mathbb{R}}(x_\infty)=|x|_\infty$, and by theorem [MeasureTheory.addEquivAddHaarChar\_restrictedProductCongrRight](../restricted-products/measuretheory-addequivaddhaarchar-restrictedprod.md) we have $\delta_{\mathbb{A}_{\mathbb{Q}}^\infty}=\prod_p\delta_{\mathbb{Q}_p}(x_p)$. By lemma [MeasureTheory.ringHaarChar\_padic](../examples/measuretheory-ringhaarchar-padic.md) we have $\delta_{\mathbb{Q}_p}(x_p)=|x_p|_p$ and putting everything together we get the result.

## Lean

Formalized as [`MeasureTheory.ringHaarChar_adeles_rat`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_adeles_rat).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 812](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L812)
