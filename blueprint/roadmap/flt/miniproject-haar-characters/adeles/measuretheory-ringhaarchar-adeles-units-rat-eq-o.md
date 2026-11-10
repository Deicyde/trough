---
declaration: lemma
origin: cited
lean: MeasureTheory.ringHaarChar_adeles_units_rat_eq_one
statement: formalized
proof: formalized
---

# MeasureTheory.ringHaarChar_adeles_units_rat_eq_one

If $x\in\mathbb{Q}^\times\subseteq\mathbb{A}_{\mathbb{Q}}^\times$ then $\delta_{\mathbb{A}_{\mathbb{Q}}}(x)=1.$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.ringHaarChar_adeles_rat](measuretheory-ringhaarchar-adeles-rat.md)

## Proof

By lemma [MeasureTheory.ringHaarChar_adeles_rat](measuretheory-ringhaarchar-adeles-rat.md) we have $\delta_{\mathbb{A}_{\mathbb{Q}}}(x)=\prod_v|x|_v$. But the product formula says that this is 1. A quick proof: if $x=\pm\prod_pp^{e_p}$ then $\prod_p|x|_p=\prod_pp^{-e_p}$ and $|x|_\infty=\prod_pp^{e_p}$ so they cancel.

## Lean

Formalized as [`MeasureTheory.ringHaarChar_adeles_units_rat_eq_one`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_adeles_units_rat_eq_one).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 833](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L833)
