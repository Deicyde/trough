---
declaration: theorem
origin: cited
lean: Rat.AdeleRing.zero_discrete
statement: formalized
---

# Rat.AdeleRing.zero_discrete

There's an open subset of $\mathbb{A}_{\mathbb{Q}}$ whose intersection with $\mathbb{Q}$ is $\{0\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Use $\prod_p{\mathbb{Z}_p}\times(-1,1)$. Any rational $q$ in this set is a $p$-adic integer for all primes $p$ and hence (writing it in lowest terms as $q=n/d$) satisfies $p\nmid d$, meaning that $d=\pm1$ and thus $q\in\mathbb{Z}$. The fact that $q\in(-1,1)$ implies $q=0$.

## Lean

Stated as [`Rat.AdeleRing.zero_discrete`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/Rat.AdeleRing.zero_discrete); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 974](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L974)
