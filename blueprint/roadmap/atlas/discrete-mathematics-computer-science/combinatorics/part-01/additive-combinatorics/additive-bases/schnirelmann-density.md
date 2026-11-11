---
declaration: section
origin: cited
lean: schnirelmannDensity_add_lower_bound, exists_additive_basis_of_pos_schnirelmannDensity
statement: formalized
proof: formalized
---

# Schnirelmann density

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/schnirelmann-density/index.html).

## Schnirelmann's inequality

For a set $A$ of natural numbers, let
$\sigma(A) = \inf_{n \ge 1} |A \cap \{1, \dots, n\}| / n$ be its Schnirelmann density. If $A$
and $B$ are sets of natural numbers that both contain $0$, then their sumset
$A + B = \{a + b : a \in A,\ b \in B\}$ satisfies
$\sigma(A) + \sigma(B) - \sigma(A)\sigma(B) \le \sigma(A + B)$.

Formalized by `schnirelmannDensity_add_lower_bound`, a theorem declared in [MathlibExt/Combinatorics/Schnirelmann.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Schnirelmann.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/schnirelmann-density/index.html#schnirelmann-density-add-lower-bound).

## Schnirelmann's basis theorem

Let $A$ be a set of natural numbers with $0 \in A$ whose
Schnirelmann density $\sigma(A) = \inf_{n \ge 1} |A \cap \{1, \dots, n\}| / n$ is positive.
Then $A$ is an additive basis of finite order: there is a natural number $h$ such that every
natural number $n$ can be written as $n = a_1 + \dots + a_h$ with $a_1, \dots, a_h \in A$,
repetitions allowed.

## Sources

- Lemma 1 of Tim Jameson's notes on Linnik's proof of the Waring-Hilbert theorem.

Formalized by `exists_additive_basis_of_pos_schnirelmannDensity`, a theorem declared in [MathlibExt/Combinatorics/Schnirelmann.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Schnirelmann.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/schnirelmann-density/index.html#exists-additive-basis-of-pos-schnirelman).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schnirelmann density](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/schnirelmann-density/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/schnirelmann-density)
