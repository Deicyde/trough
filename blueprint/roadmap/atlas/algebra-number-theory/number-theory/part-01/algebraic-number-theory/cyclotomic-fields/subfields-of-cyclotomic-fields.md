---
declaration: section
origin: cited
lean: CyclotomicField.existsUnique_intermediateField_finrank, CyclotomicField.intermediateFieldOfFinrank, CyclotomicField.eq_intermediateFieldOfFinrank_iff, CyclotomicField.sup_eq_top_of_lcm_eq, CyclotomicField.inf_ne_bot_of_lt_of_lcm_eq
statement: formalized
proof: formalized
---

# Subfields of cyclotomic fields

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields/index.html).

## Unique subfield of each degree in the $p$-th cyclotomic field

Let $p$ be a prime and let
$s$ be a natural number dividing $p - 1$. Then the $p$-th cyclotomic field $\mathbb{Q}(\zeta_p)$
has exactly one intermediate field $K$ over $\mathbb{Q}$ with $[K : \mathbb{Q}] = s$.

Formalized by `CyclotomicField.existsUnique_intermediateField_finrank`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields/index.html#exists-unique-intermediate-field-finrank).

## The degree-$s$ subfield of the $p$-th cyclotomic field

For a prime $p$ and a natural
number $s$ dividing $p - 1$, this is the unique intermediate field $K$ of the $p$-th cyclotomic
field $\mathbb{Q}(\zeta_p)$ over $\mathbb{Q}$ with $[K : \mathbb{Q}] = s$.

Formalized by `CyclotomicField.intermediateFieldOfFinrank`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields/index.html#intermediate-field-of-finrank).

## Characterization of the degree-$s$ subfield of the $p$-th cyclotomic field

Let $p$ be a
prime, let $s$ be a natural number dividing $p - 1$, and let $K$ be an intermediate field of the
$p$-th cyclotomic field $\mathbb{Q}(\zeta_p)$ over $\mathbb{Q}$. Then $K$ is the degree-$s$
subfield of $\mathbb{Q}(\zeta_p)$ if and only if $[K : \mathbb{Q}] = s$.

Formalized by `CyclotomicField.eq_intermediateFieldOfFinrank_iff`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields/index.html#eq-intermediate-field-of-finrank-iff).

## Two cyclotomic subfields whose levels have lcm $m$ generate the $m$-th cyclotomic field

Let $n_0$, $n_1$ and $m$ be natural numbers with $n_0, n_1 \neq 0$ and
$\operatorname{lcm}(n_0, n_1) = m$. Let $E_0$ and $E_1$ be intermediate fields of the $m$-th
cyclotomic field $\mathbb{Q}(\zeta_m)$ over $\mathbb{Q}$ such that $E_0$ is generated over
$\mathbb{Q}$ by a primitive $n_0$-th root of unity and $E_1$ by a primitive $n_1$-th root of
unity. Then the compositum of $E_0$ and $E_1$ is all of $\mathbb{Q}(\zeta_m)$.

Formalized by `CyclotomicField.sup_eq_top_of_lcm_eq`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields/index.html#sup-eq-top-of-lcm-eq).

## A field strictly above one cyclotomic subfield meets the other

Let $n_0$, $n_1$ and $m$
be natural numbers with $n_0, n_1 \neq 0$ and $\operatorname{lcm}(n_0, n_1) = m$. Let $E_0$ and
$E_1$ be intermediate fields of the $m$-th cyclotomic field $\mathbb{Q}(\zeta_m)$ over
$\mathbb{Q}$ such that $E_0$ is generated over $\mathbb{Q}$ by a primitive $n_0$-th root of unity
and $E_1$ by a primitive $n_1$-th root of unity. If $F$ is an intermediate field of
$\mathbb{Q}(\zeta_m)$ with $E_0 \subsetneq F$, then $F \cap E_1 \neq \mathbb{Q}$.

Formalized by `CyclotomicField.inf_ne_bot_of_lt_of_lcm_eq`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/IntermediateField.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields/index.html#inf-ne-bot-of-lt-of-lcm-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subfields of cyclotomic fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/subfields-of-cyclotomic-fields)
