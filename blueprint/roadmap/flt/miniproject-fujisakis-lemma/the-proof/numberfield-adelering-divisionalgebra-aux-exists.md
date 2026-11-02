---
declaration: lemma
origin: cited
lean: NumberField.AdeleRing.DivisionAlgebra.Aux.existsE
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.DivisionAlgebra.Aux.existsE

There's a compact subset $E$ of $D_{\mathbb{A}}$ with the property that for all $x\in D_{\mathbb{A}}^{(1)}$, the obvious map $xE\to D\backslash D_{\mathbb{A}}$ is not injective.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We know that if we pick a $\mathbb{Q}$-basis for $D$ of size $d$ then this identifies $D$ with $\mathbb{Q}^d$, $D_{\mathbb{A}}$ with $\mathbb{A}_{\mathbb{Q}}^d$, and $D\backslash D_{\mathbb{A}}$ with $(\mathbb{Q}\backslash\mathbb{A}_{\mathbb{Q}})^d$. Now $\mathbb{Q}$ is discrete in $\mathbb{A}_{\mathbb{Q}}$ by theorem [Theorem NumberField.AdeleRing.discrete](../../miniproject-adeles/discreteness-and-compactness/numberfield-adelering-discrete.md), and the quotient $\mathbb{Q}\backslash \mathbb{A}_{\mathbb{Q}}$ is compact by theorem [Theorem Rat.AdeleRing.cocompact](../../miniproject-adeles/discreteness-and-compactness/rat-adelering-cocompact.md). Hence $D$ is discrete in $D_{\mathbb{A}}$ and the quotient $D\backslash D_{\mathbb{A}}$ is compact.

Fix a Haar measure $\mu$ on $D_{\mathbb{A}}$ and push it forward to $D\backslash D_{\mathbb{A}}$; by compactness this quotient has finite and positive measure, say $m\in\mathbb{R}_{>0}$. Choose any compact $E\subseteq D_{\mathbb{A}}$ with measure $> m$ (for example, choose a $\mathbb{Z}$-lattice $L\cong\mathbb{Z}^d$ in $D\cong\mathbb{Q}^d$, define $E_f:=\prod_p L_p\in D\otimes_{\mathbb{Q}}\mathbb{A}_{\mathbb{Q}}^\infty$, and define $E_{\infty}\subseteq D\otimes_{\mathbb{Q}}\mathbb{R}\cong\mathbb{R}^n$ to be a huge closed ball, large enough to ensure the measure of $E:=E_f\times E_{\infty}$ is bigger than $m$). Then $\mu(xE)=\mu(E)>m$ so the map can't be injective.

## Lean

Formalized as [`NumberField.AdeleRing.DivisionAlgebra.Aux.existsE`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.DivisionAlgebra.Aux.existsE).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 100](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L100)
