---
declaration: definition
origin: cited
lean: GaloisRepresentation.IsHardlyRamified
statement: formalized
---

# hardly\_ramified

Let $R$ be a coefficient ring with finite residue field of characteristic $\ell\geq3$. Let $V$ be a finite free $R$-module of rank 2, equipped with the product topology. A continuous representation $\rho: \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to \operatorname{GL}_R(V)$ is said to be *hardly ramified* if it satisfies the following four conditions:

1. $\det(\rho):\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to R^\times$ is the cyclotomic character;
2. $\rho$ is unramified outside $2\ell$;
3. The restriction of $\rho$ to $\operatorname{Gal}(\overline{\mathbb{Q}}_2/\mathbb{Q}_2)$ is reducible (more precisely, there is a short exact sequence $0\to R\to V\to R\to 0$ which is stable under the action of $\operatorname{Gal}(\overline{\mathbb{Q}}_2/\mathbb{Q}_2)$) and the Galois action on the 1-dimensional quotient is an unramified representation of $\operatorname{Gal}(\overline{\mathbb{Q}}_2/\mathbb{Q}_2)$ whose square is trivial;
4. The restriction of $\rho$ to $\operatorname{Gal}(\overline{\mathbb{Q}}_\ell/\mathbb{Q}_\ell)$ is flat, by which we mean that for all open ideals $I$ of $R$, the (finite image) representation $\rho$ mod $I:\operatorname{Gal}(\overline{\mathbb{Q}}_\ell/\mathbb{Q}_\ell)\to \operatorname{GL}_{R/I}(V/I)$ comes from a finite flat group scheme.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`GaloisRepresentation.IsHardlyRamified`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/GaloisRepresentation.IsHardlyRamified).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch03freyreduction.tex, line 73](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch03freyreduction.tex#L73)
