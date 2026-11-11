---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.WeilConjecturesWanted.AlgebraicGeometry.WeilConjectures.weil_conjectures
statement: formalized
---

# Arithmetic geometry: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/index.html).

Rational points and point counts of varieties over number fields and finite fields, including the Mordell conjecture and the Weil conjectures.

## The Weil conjectures

Let $F$ be a finite field with $q$ elements, and let $X$ be a scheme
over $\operatorname{Spec} F$ whose structure morphism is proper, geometrically irreducible and
smooth of relative dimension $d$. Then there is a sequence $A_0, A_1, A_2, \dots$ of finite
multisets of complex numbers with $A_0 = \{1\}$ such that, for every $0 \le i \le 2d$, the
multiset $A_{2d-i}$ is the image of $A_i$ under $\alpha \mapsto q^d/\alpha$, the multiset $A_i$
is invariant under every field automorphism of $\mathbb{C}$, and every $\alpha \in A_i$ is an
algebraic integer with $|\alpha| = \sqrt{q^i}$. Moreover, for every finite field extension $E$
of $F$ of degree $m$, the number of morphisms $\operatorname{Spec} E \to X$ over
$\operatorname{Spec} F$ equals $\sum_{i=0}^{2d} (-1)^i \sum_{\alpha \in A_i} \alpha^m$, where
the inner sums count multiplicities.

## Sources

- P. Deligne, 'La conjecture de Weil. I', Publications Mathématiques de l'Institut des Hautes Études Scientifiques, Volume 43, pages 273–307 (1974), https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf. See also references in the Lean file. Problem `weil_conjectures` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.WeilConjecturesWanted.AlgebraicGeometry.WeilConjectures.weil_conjectures` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/WeilConjecturesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/WeilConjecturesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/index.html#weil-conjectures).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic geometry](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/arithmetic-geometry)
