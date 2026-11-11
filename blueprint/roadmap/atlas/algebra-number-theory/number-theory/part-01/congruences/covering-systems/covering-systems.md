---
declaration: section
origin: cited
lean: CoveringSystem, StrictCoveringSystem
statement: formalized
proof: formalized
---

# Covering systems: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/index.html).

Covering and exact covering systems of residue classes, minimum moduli, Erdős–Graham and Fraenkel-type results.

## Covering system

A covering system of a commutative semiring $R$ is a finite family of cosets
$r_i + I_i = \{r_i + a : a \in I_i\}$, where each $I_i$ is an ideal of $R$ different from both
$\{0\}$ and $R$, whose union is all of $R$. In the case $R = \mathbb{Z}$, this corresponds to a
choice of finitely many congruences $x \equiv r_i \pmod{n_i}$ with moduli $n_i \ge 2$ such that
every integer satisfies at least one of them.

Formalized by `CoveringSystem`, a structure declared in [MathlibExt/NumberTheory/CoveringSystem.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CoveringSystem.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/index.html#covering-system).

## Strict covering system

A covering system of a commutative semiring $R$, given by cosets
$r_i + I_i$, is strict if the ideals $I_i$ are pairwise distinct. In the case $R = \mathbb{Z}$, this
means that the congruences defining it have pairwise distinct moduli.

This corresponds to the notion of covering system that Erdős and Graham use.

## Sources

- [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number theory. Monographies de L'Enseignement Mathematique (1980).

Formalized by `StrictCoveringSystem`, a structure declared in [MathlibExt/NumberTheory/CoveringSystem.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CoveringSystem.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/index.html#strict-covering-system).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Covering systems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/covering-systems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/covering-systems)
