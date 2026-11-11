---
declaration: section
origin: cited
lean: Algebra.norm_baseChange, Algebra.trace_baseChange, Algebra.norm_prod, Algebra.norm_of_subsingleton
statement: formalized
proof: formalized
---

# Norm and trace of algebras

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/norm-and-trace-of-algebras/index.html).

## The norm commutes with base change

Let $A$, $A'$ and $B$ be commutative rings, where
$A'$ and $B$ are $A$-algebras and $B$ is a free $A$-module of finite rank. Then for every
$b \in B$, the image of the norm $N_{B/A}(b)$ under the structure map $A \to A'$ equals the norm
$N_{(A' \otimes_A B)/A'}(1 \otimes b)$ of $1 \otimes b$ in the $A'$-algebra $A' \otimes_A B$.

## Sources

- ATLAS `NumberTheoryI`, Lemma 4.49 (norm clause).

Formalized by `Algebra.norm_baseChange`, a theorem declared in [MathlibExt/RingTheory/NormTrace/BaseChange.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/NormTrace/BaseChange.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/norm-and-trace-of-algebras/index.html#norm-base-change).

## The trace commutes with base change

Let $A$, $A'$ and $B$ be commutative rings, where
$A'$ and $B$ are $A$-algebras and $B$ is a free $A$-module of finite rank. Then for every
$b \in B$, the image of the trace $T_{B/A}(b)$ under the structure map $A \to A'$ equals the trace
$T_{(A' \otimes_A B)/A'}(1 \otimes b)$ of $1 \otimes b$ in the $A'$-algebra $A' \otimes_A B$.

## Sources

- ATLAS `NumberTheoryI`, Lemma 4.49 (trace clause).

Formalized by `Algebra.trace_baseChange`, a theorem declared in [MathlibExt/RingTheory/NormTrace/BaseChange.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/NormTrace/BaseChange.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/norm-and-trace-of-algebras/index.html#trace-base-change).

## Norm in a product algebra is the product of norms

The norm of a product algebra is the product of the norms of the
components: left multiplication by `(x₁, x₂)` is the product map of the
left multiplications, and the determinant of a product map is the product
of the determinants.

Formalized by `Algebra.norm_prod`, a theorem declared in [MathlibExt/RingTheory/NormTrace/Prod.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/NormTrace/Prod.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/norm-and-trace-of-algebras/index.html#norm-prod).

## Norm on a subsingleton algebra is one

The norm on a subsingleton algebra is `1`: left multiplication by any
element is the identity map on a subsingleton module, hence has determinant
`1`.

Formalized by `Algebra.norm_of_subsingleton`, a theorem declared in [MathlibExt/RingTheory/NormTrace/Prod.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/NormTrace/Prod.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/norm-and-trace-of-algebras/index.html#norm-of-subsingleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Norm and trace of algebras](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/algebras-and-differentials/norm-and-trace-of-algebras/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/algebras-and-differentials/norm-and-trace-of-algebras)
