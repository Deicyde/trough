---
declaration: theorem
origin: cited
lean: NumberField.AdeleRing.locallyCompactSpace
statement: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/253
---

# NumberField.AdeleRing.locallyCompactSpace

The adeles of a number field are locally compact.

## Depends on

- [NumberField.instCompactSpaceAdicCompletionIntegers](numberfield-instcompactspaceadiccompletionintege.md)

## Proof

The adeles of a number field are a product of the finite adeles and the infinite adeles so it suffices to prove that the finite and infinite adeles are locally compact. The infinite adeles are just isomorphic to $\mathbb{R}^n$ as a topological space, so they're certainly locally compact. As for the finite adeles, the mathlib theorem RestrictedProduct.locallyCompactSpace\_of\_addGroup says that a restricted product of locally compact additive groups with respect to open compact subgroups is locally compact, so this reduces us the previous result.

## Lean

Formalized as [`NumberField.AdeleRing.locallyCompactSpace`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.locallyCompactSpace).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 88](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L88)
