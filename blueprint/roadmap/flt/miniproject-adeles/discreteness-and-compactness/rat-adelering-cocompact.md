---
declaration: theorem
origin: cited
lean: Rat.AdeleRing.cocompact
statement: formalized
---

# Rat.AdeleRing.cocompact

The quotient $\mathbb{A}_{\mathbb{Q}}/\mathbb{Q}$ is compact.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The space $\prod_p\mathbb{Z}_p\times[0,1]\subseteq\mathbb{A}_{\mathbb{Q}}$ is a product of compact spaces and is hence compact. I claim that it surjects onto $\mathbb{A}_{\mathbb{Q}}/\mathbb{Q}$. Indeed, if $a\in\mathbb{A}_{\mathbb{Q}}$ then for the finitely many prime numbers $p\in S$ such that $a_p\not\in\mathbb{Z}_p$ we have $a_p\in\frac{r_p}{p^{n_p}}+\mathbb{Z}_p$ with $r_p/p^{n_p}\in\mathbb{Q}$, and if $q=\sum_{p\in S}\frac{r_p}{p^{n_p}}\in\mathbb{Q}$ then $a-q\in \prod_p\mathbb{Z}_p\times\mathbb{R}$. Now just subtract $\lfloor a_{\infty}-q\rfloor$ to move into $\prod_p\mathbb{Z}_p\times[0,1)$ and we are done.

## Lean

Formalized as [`Rat.AdeleRing.cocompact`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Rat.AdeleRing.cocompact).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 1015](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L1015)
