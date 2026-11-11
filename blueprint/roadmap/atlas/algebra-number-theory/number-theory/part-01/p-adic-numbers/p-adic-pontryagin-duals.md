---
declaration: section
origin: cited
lean: MetaMathlibExt.PadicQuotientInt, MetaMathlibExt.PadicPontryaginDual, MetaMathlibExt.PadicPontryaginDual_ext, MetaMathlibExt.padicQuotientMap, MetaMathlibExt.padicQuotientMap_algebraMap_eq_zero, MetaMathlibExt.padicQuotientMap_mkQ_eq, MetaMathlibExt.contragredientSMul, MetaMathlibExt.smul_apply
statement: formalized
proof: formalized
---

# p-adic Pontryagin duals

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html).

## The quotient $\mathbb{Q}_p/\mathbb{Z}_p$

For a prime $p$, $\mathbb{Q}_p/\mathbb{Z}_p$ is
the quotient of $\mathbb{Q}_p$, viewed as a $\mathbb{Z}_p$-module, by the image of
$\mathbb{Z}_p$ under the canonical inclusion $\mathbb{Z}_p \to \mathbb{Q}_p$.

Formalized by `MetaMathlibExt.PadicQuotientInt`, an abbreviation declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#padic-quotient-int).

## Algebraic $p$-adic Pontryagin dual

For a prime $p$ and a $\mathbb{Z}_p$-module $A$, the
algebraic $p$-adic Pontryagin dual of $A$ is the $\mathbb{Z}_p$-module
$\operatorname{Hom}_{\mathbb{Z}_p}(A, \mathbb{Q}_p/\mathbb{Z}_p)$ of all $\mathbb{Z}_p$-linear maps
from $A$ to $\mathbb{Q}_p/\mathbb{Z}_p$; no topology or continuity condition is imposed.

Formalized by `MetaMathlibExt.PadicPontryaginDual`, an abbreviation declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#padic-pontryagin-dual).

## Extensionality for the $p$-adic Pontryagin dual

Let $p$ be a prime and $A$ a
$\mathbb{Z}_p$-module. If two elements $\varphi, \psi$ of the algebraic $p$-adic Pontryagin dual
of $A$ satisfy $\varphi(a) = \psi(a)$ for every $a \in A$, then $\varphi = \psi$.

Formalized by `MetaMathlibExt.PadicPontryaginDual_ext`, a theorem declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#padic-pontryagin-dual-ext).

## The quotient map $\mathbb{Q}_p \to \mathbb{Q}_p/\mathbb{Z}_p$

For a prime $p$, this is
the canonical projection $\mathbb{Q}_p \to \mathbb{Q}_p/\mathbb{Z}_p$, $x \mapsto x + \mathbb{Z}_p$,
as a $\mathbb{Z}_p$-linear map.

Formalized by `MetaMathlibExt.padicQuotientMap`, a definition declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#padic-quotient-map).

## The quotient map vanishes on $\mathbb{Z}_p$

For a prime $p$ and every
$z \in \mathbb{Z}_p$, the quotient map $\mathbb{Q}_p \to \mathbb{Q}_p/\mathbb{Z}_p$ sends the
image of $z$ in $\mathbb{Q}_p$ to $0$.

Formalized by `MetaMathlibExt.padicQuotientMap_algebraMap_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#padic-quotient-map-algebra-map-eq-zero).

## The quotient map is the quotient projection

For a prime $p$ and every
$x \in \mathbb{Q}_p$, the quotient map $\mathbb{Q}_p \to \mathbb{Q}_p/\mathbb{Z}_p$ sends $x$ to
its class $x + \mathbb{Z}_p$ in the quotient module.

Formalized by `MetaMathlibExt.padicQuotientMap_mkQ_eq`, a theorem declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#padic-quotient-map-mk-q-eq).

## Contragredient action on the $p$-adic Pontryagin dual

Let $p$ be a prime, $G$ a group
and $A$ a $\mathbb{Z}_p$-module on which $G$ acts by additive maps commuting with the
$\mathbb{Z}_p$-action. For $g \in G$ and $\varphi$ in the algebraic $p$-adic Pontryagin dual of
$A$, $g \cdot \varphi$ is the element $a \mapsto \varphi(g^{-1} a)$ of the dual.

Formalized by `MetaMathlibExt.contragredientSMul`, a definition declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#contragredient-smul).

## Evaluating the contragredient action

Let $p$ be a prime, $G$ a group and $A$ a
$\mathbb{Z}_p$-module on which $G$ acts by additive maps commuting with the
$\mathbb{Z}_p$-action. For $g \in G$, $\varphi$ in the algebraic $p$-adic Pontryagin dual of $A$
and $a \in A$, the contragredient action satisfies $(g \cdot \varphi)(a) = \varphi(g^{-1} a)$.

Formalized by `MetaMathlibExt.smul_apply`, a theorem declared in [MathlibExt/NumberTheory/Padics/PontryaginDual.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/PontryaginDual.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html#smul-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: p-adic Pontryagin duals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/p-adic-numbers/p-adic-pontryagin-duals)
