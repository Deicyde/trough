---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BrauerCharacterInCyclotomicWanted.RepresentationTheory.brauer_character_in_cyclotomic, MathlibExt.GroupTheory.BrauerSplittingFieldWanted.RepresentationTheory.brauer_splitting_field
statement: formalized
---

# Brauer's splitting field theorem

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/brauer-s-splitting-field-theorem/index.html).

## Character values of a finite group lie in a cyclotomic field

Let $G$ be a finite group of
exponent $n$, and let $\mathbb{Q}(\zeta_n)$ be the $n$-th cyclotomic field. There is a ring
homomorphism $\varphi \colon \mathbb{Q}(\zeta_n) \to \mathbb{C}$ such that for every
finite-dimensional complex representation $\rho$ of $G$ on a vector space $V$ and every $g \in G$,
the trace of $\rho(g)$ lies in the image of $\varphi$.

## Sources

- R. Brauer, On the representation of a group of order g in the field of g-th roots of unity, Amer. J. Math. 67 (1945). Problem `brauer_character_in_cyclotomic` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.BrauerCharacterInCyclotomicWanted.RepresentationTheory.brauer_character_in_cyclotomic` is written with `theorem_wanted` in [WantedExt/GroupTheory/BrauerCharacterInCyclotomicWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BrauerCharacterInCyclotomicWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/brauer-s-splitting-field-theorem/index.html#brauer-character-in-cyclotomic).

## Brauer's splitting field theorem

Let $G$ be a finite group of exponent $n$, let
$K = \mathbb{Q}(\zeta_n)$ be the $n$-th cyclotomic field, and let $\rho$ be a representation of
$G$ on a finite-dimensional complex vector space $V$. Then there are a ring homomorphism
$\varphi \colon K \to \mathbb{C}$, a $K$-vector space $W$ with a representation $\sigma$ of $G$
on $W$, and a $\mathbb{C}$-linear isomorphism $f \colon \mathbb{C} \otimes_K W \to V$, where
$\mathbb{C}$ is regarded as a $K$-algebra via $\varphi$, such that
$f((\mathrm{id}_{\mathbb{C}} \otimes \sigma(g))(x)) = \rho(g)(f(x))$ for all $g \in G$ and all
$x \in \mathbb{C} \otimes_K W$.

## Sources

- R. Brauer, On the representation of a group of order g in the field of g-th roots of unity, Amer. J. Math. 67 (1945), 461–471. Problem `brauer_splitting_field` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.BrauerSplittingFieldWanted.RepresentationTheory.brauer_splitting_field` is written with `theorem_wanted` in [WantedExt/GroupTheory/BrauerSplittingFieldWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BrauerSplittingFieldWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/brauer-s-splitting-field-theorem/index.html#brauer-splitting-field).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brauer's splitting field theorem](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/brauer-s-splitting-field-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/characters-of-finite-groups/brauer-s-splitting-field-theorem)
