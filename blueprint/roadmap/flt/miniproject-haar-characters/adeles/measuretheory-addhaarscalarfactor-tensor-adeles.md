---
declaration: theorem
origin: cited
lean: MeasureTheory.addHaarScalarFactor_tensor_adeles_eq_one
statement: formalized
proof: formalized
---

# MeasureTheory.addHaarScalarFactor\_tensor\_adeles\_eq\_one

In the above situation ($V$ a finite-dimensional $\mathbb{Q}$-vector space, $\phi:V\cong V$ is $\mathbb{Q}$-linear, $\phi_{\mathbb{A}}$ the base extension to $V_{\mathbb{A}}:=V\otimes_{\mathbb{Q}}{\mathbb{A}_{\mathbb{Q}}}$, a continuous linear endomorphism of $V_{\mathbb{A}}$ with the $\mathbb{A}_{\mathbb{Q}}$-module topology), we have $d_{V_{\mathbb{A}}}(\phi_{\mathbb{A}})=1.$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar\_restrictedProductCongrRight](../restricted-products/measuretheory-addequivaddhaarchar-restrictedprod.md)
- [NumberField.AdeleRing.ModuleBaseChangeContinuousLinearEquiv](numberfield-adelering-modulebasechangecontinuous.md)

## Proof

The original blueprint proof of this was that $\phi_{\mathbb{A}} : V_{\mathbb{A}}\to V_{\mathbb{A}}$ could be written as a restricted product of $\phi_v:V\otimes_{\mathbb{Q}}{\mathbb{Q}_v} \to V\otimes_{\mathbb{Q}}\mathbb{Q}_v$ and hence by theorem [MeasureTheory.addEquivAddHaarChar\_restrictedProductCongrRight](../restricted-products/measuretheory-addequivaddhaarchar-restrictedprod.md) we have $d_{V_{\mathbb{A}}}(\phi_{\mathbb{A}})=\prod_p d_{V_p}(\phi_p)\times d_{V_\infty}(\phi_\infty)$, and then applying Lemma MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det this is equal to $\prod_v\delta_{\mathbb{Q}_v}(\det(\phi_v))\prod_v\delta_{\mathbb{Q}_v}(\det(\phi))=1$.

This turned out to be a nightmare to formalize, because commuting the tensor product and the restricted product cannot be done naively, as the tensor product is over $\mathbb{Q}$ and the submodules in the restricted product defining $\mathbb{A}_{\mathbb{Q}}$ are not $\mathbb{Q}$-modules. So one has to choose a $\mathbb{Z}$-lattice in $V$ and use the isomorphisms $V\otimes_{\mathbb{Q}}\mathbb{A}=\Lambda\otimes_{\mathbb{Z}}\mathbb{A}= \Lambda\otimes_{\mathbb{Z}}\mathbb{Q}_\infty\times\prod'_p[\Lambda\otimes_{\mathbb{Z}}\mathbb{Q}_p;\Lambda\otimes_{\mathbb{Z}}\mathbb{Z}_p]= V\otimes_{\mathbb{Q}}\mathbb{Q}_\infty\times\prod'_p[V\otimes_{\mathbb{Q}}\mathbb{Q}_p;im(\Lambda\otimes_{\mathbb{Z}}\mathbb{Z}_p)]$ and check that all of these canonical maps are continuous (and one of these claims boils down to yet another claim of the form "if you do something to the factors and then take the restricted product, then this is topologically the same as doing it to the restriced product", with the thing being $\Lambda\otimes_{\mathbb{Z}}$ in this case, something which needs checking).

So here is the proof which we actually formalized. Say an automorphism of a finite free $R$-module is *nice* if it's a product of transvections and diagonal matrices with unit entries. Mathlib has the fact that if $R$ is a field then all automorphisms are nice, and the base change of a nice morphism is nice. Hence $\phi_{\mathbb{A}}$ is nice, and we can simply prove Lemma \[MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det\] for nice endomorphisms over a commutative ring, which gives the result we want immediately by the product formula.

## Lean

Formalized as [`MeasureTheory.addHaarScalarFactor_tensor_adeles_eq_one`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addHaarScalarFactor_tensor_adeles_eq_one).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 859](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L859)
