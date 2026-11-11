---
declaration: section
origin: cited
lean: HilbertNullstellensatz.vanishingIdeal_singleton_eq_ker_aeval, HilbertNullstellensatz.isMaximal_iff_eq_ker_aeval, HilbertNullstellensatz.isMaximal_quotient_iff_exists_common_zero
statement: formalized
proof: formalized
---

# Hilbert's Nullstellensatz

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/hilbert-s-nullstellensatz/index.html).

## Vanishing ideal of a point

For a point $a \in \mathbb{C}^n$, the ideal of polynomials in
$\mathbb{C}[x_1, \ldots, x_n]$ that vanish on $\{a\}$ equals the kernel of the evaluation
homomorphism $\mathbb{C}[x_1, \ldots, x_n] \to \mathbb{C}$, $f \mapsto f(a)$.

Formalized by `HilbertNullstellensatz.vanishingIdeal_singleton_eq_ker_aeval`, a theorem declared in [MathlibExt/RingTheory/Nullstellensatz.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Nullstellensatz.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/hilbert-s-nullstellensatz/index.html#vanishing-ideal-singleton-eq-ker-aeval).

## Weak Nullstellensatz, kernel form

Let $n$ be a natural number. An ideal $I$ of the
polynomial ring $\mathbb{C}[x_1, \ldots, x_n]$ is maximal if and only if there is a point
$a \in \mathbb{C}^n$ such that $I$ is the kernel of the evaluation homomorphism
$\mathbb{C}[x_1, \ldots, x_n] \to \mathbb{C}$, $f \mapsto f(a)$.

Formalized by `HilbertNullstellensatz.isMaximal_iff_eq_ker_aeval`, a theorem declared in [MathlibExt/RingTheory/Nullstellensatz.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Nullstellensatz.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/hilbert-s-nullstellensatz/index.html#is-maximal-iff-eq-ker-aeval).

## Weak Nullstellensatz, quotient form

Let $P_1, \ldots, P_m$ be polynomials in
$\mathbb{C}[x_1, \ldots, x_n]$ and let $A = \mathbb{C}[x_1, \ldots, x_n]/(P_1, \ldots, P_m)$.
An ideal $J$ of $A$ is maximal if and only if there is a common zero $a \in \mathbb{C}^n$ of
$P_1, \ldots, P_m$ such that $J$ is the image in $A$ of the ideal of polynomials vanishing at
$a$.

Formalized by `HilbertNullstellensatz.isMaximal_quotient_iff_exists_common_zero`, a theorem declared in [MathlibExt/RingTheory/Nullstellensatz.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Nullstellensatz.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/hilbert-s-nullstellensatz/index.html#is-maximal-quotient-iff-exists-common-ze).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert's Nullstellensatz](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ideals-and-constructions/hilbert-s-nullstellensatz/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ideals-and-constructions/hilbert-s-nullstellensatz)
