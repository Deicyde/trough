---
declaration: theorem
origin: cited
lean: NumberField.FiniteAdeleRing.DivisionAlgebra.units_cocompact
statement: formalized
proof: formalized
---

# NumberField.FiniteAdeleRing.DivisionAlgebra.units_cocompact

$D^\times\backslash(D\otimes_K\mathbb{A}_K^\infty)^\times$ is compact.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [NumberField.AdeleRing.DivisionAlgebra.compact_quotient](../enter-the-adeles/numberfield-adelering-divisionalgebra-compact-qu.md)

## Proof

There's a natural map $\alpha$ from $D^\times\backslash D_{\mathbb{A}}^{(1)}$ to $D^\times\backslash (D\otimes_K \mathbb{A}_K^\infty)^\times$. We claim that it's surjective. Granted this claim, we are home, because if we put the quotient topology on $D^\times\backslash (D\otimes_K \mathbb{A}_K^\infty)^\times$ coming from $(D\otimes_K \mathbb{A}_K^\infty)^\times$ then it's readily verified that $\alpha$ is continuous, and the continuous image of a compact space is compact.

As for surjectivity: say $x\in (D\otimes_K \mathbb{A}_K^\infty)^\times$. We need to extend $x$ to an element $(x,y)\in (D\otimes_K \mathbb{A}_K^\infty)^\times\times(D\otimes_K K_\infty)^\times$ which is in the kernel of $\delta_{D_{\mathbb{A}}}$. Because $\delta_{D_{\mathbb{A}}}(x,1)$ is some positive real number, it will suffice to show that if $r$ is any positive real number then we can find $y\in (D\otimes_K \mathbb{A}_K^\infty)^\times=(D\otimes_{\mathbb{Q}}\mathbb{R})^\times$ with $\delta_{D_{\mathbb{A}}}(1,y)=r$, or equivalently (setting $D_{\mathbb{R}}=D\otimes_{\mathbb{Q}}\mathbb{R}$) that $\delta_{D_{\mathbb{R}}}(y)=r$. But $D\not=0$ as it is a division algebra,and hence $\mathbb{Q}\subseteq D$, meaning $\mathbb{R}\subseteq D_{\mathbb{R}}$, and if $x\in\mathbb{R}^\times\subseteq D_{\mathbb{R}}^\times$ then $\delta(x)=|x|^d$ with $d=\dim_{\mathbb{Q}}(D)$, as multiplication by $x$ is just scaling by a factor of $x$ on $D_{\mathbb{R}}\cong\mathbb{R}^d$. In particular we can set $x=y^{1/d}$.

## Lean

Formalized as [`NumberField.FiniteAdeleRing.DivisionAlgebra.units_cocompact`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.FiniteAdeleRing.DivisionAlgebra.units_cocompact).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 319](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L319)
