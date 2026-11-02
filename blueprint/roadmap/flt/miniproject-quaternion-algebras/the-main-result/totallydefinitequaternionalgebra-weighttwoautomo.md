---
declaration: theorem
origin: cited
---

# TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.finiteDimensional

Let $k$ be a field. Then the space $S^D(U;k)$ is a finite-dimensional $k$-vector space.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [NumberField.FiniteAdeleRing.DivisionAlgebra.units\_cocompact](../../miniproject-fujisakis-lemma/the-proof/numberfield-finiteadelering-divisionalgebra-unit.md)
- [NumberField.FiniteAdeleRing.DivisionAlgebra.finiteDoubleCoset](../../miniproject-fujisakis-lemma/the-proof/numberfield-finiteadelering-divisionalgebra-fini.md)

## Proof

The finite-dimensionality theorem is in fact an easy consequence of Fujisaki's lemma, proved in the Fukisaki miniproject, chapter [Miniproject: Fujisaki's Lemma](../../miniproject-fujisakis-lemma/README.md). Write $(D\otimes_F\mathbb{A}_F^\infty)^\times$ as a disjoint union of double cosets $\coprod_i D^\times g_i U$. This open cover descends to a disjoint open cover of $D^\times\backslash (D\otimes_F\mathbb{A}_F^\infty)^\times$, and this latter space is compact by theorem [Theorem NumberField.FiniteAdeleRing.DivisionAlgebra.units\_cocompact](../../miniproject-fujisakis-lemma/the-proof/numberfield-finiteadelering-divisionalgebra-unit.md). Hence the cover is finite; write the double coset representatives as $g_1,g_2,\ldots,g_n$. We claim that the function $S^D(U;k)\to W^n$ sending $f$ to $(f(g_1),f(g_2),\ldots,f(g_n))$ is injective and $k$-linear, which suffices by finite-dimensionality of $W$. $k$-linearity is easy, so let's talk about injectivity.

Say $f_1$ and $f_2$ are two elements of $S^D(U;k)$ which agree on each $g_i$. It suffices to prove that $f_1(g)=f_2(g)$ for all $g\in(D\otimes_F\mathbb{A}_F^\infty)^\times$. So say $g\in(D\otimes_F\mathbb{A}_F^\infty)^\times$, and write $g=\delta g_iu$ for $\delta \in D^\times$ and $u\in U$. Then $f_1(g)=f_1(\delta g_iu)=f_1(g_i)$ (by the definition of $S^D(U;k)$), and similarly $f_2(g)=f_2(g_i)$ and because $f_1(g_i)=f_2(g_i)$ by assumption, we deduce $f_1(g)=f_2(g)$ as required.

## Lean

The blueprint names [`TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.LevelStruct.instFiniteSubtypeMemSubmoduleFormOfIsSufficientlySmallOfIsFinite`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.LevelStruct.instFiniteSubtypeMemSubmoduleFormOfIsSufficientlySmallOfIsFinite).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/QuaternionAlgebraProject.tex, line 160](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/QuaternionAlgebraProject.tex#L160)
