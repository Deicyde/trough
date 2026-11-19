---
declaration: definition
origin: cited
lean: KummerCriterion.teichmullerCharQp
statement: formalized
---

# teichmuller

The *Teichmüller character* of the prime $p$ is the unique character

$$
\omega\colon\left(\mathbb{Z}/p\mathbb{Z}\right)^\times\to\mathbb{Z}_p^\times
$$

such that $\omega(a) \equiv a \pmod p$ and $\omega(a)^{p-1} = 1$ for every $a$; its values are the $(p-1)$st roots of unity in $\mathbb{Z}_p$. Composing with the inclusion $\mathbb{Z}_p \hookrightarrow \mathbb{Q}_p$ gives the $\mathbb{Q}_p$-valued Dirichlet character used below. The characters $\omega^j$ for $0 \le j \le p-2$ exhaust the characters modulo $p$, and $\omega^j$ is odd exactly when $j$ is odd.

## Depends on

- [dirichlet-character](def-dirichlet-character.md)

## Lean

Formalized as [`KummerCriterion.teichmullerCharQp`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.teichmullerCharQp).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 46](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L46)
