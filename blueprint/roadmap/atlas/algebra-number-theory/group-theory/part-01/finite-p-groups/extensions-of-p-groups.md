---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FrattiniExtensionSequenceKourovka16Problem12Wanted.IsPhiExtension, MathlibExt.GroupTheory.FrattiniExtensionSequenceKourovka16Problem12Wanted.phiExtensionSequence, MathlibExt.GroupTheory.FrattiniExtensionSequenceKourovka16Problem12Wanted.phiExtensionSequence_holds
statement: formalized
---

# Φ-extensions of p-groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/extensions-of-p-groups/index.html).

## $\Phi$-extension (Berkovich)

For a natural number $p$ and groups $H$ and $G$, $H$ is a
$\Phi$-extension of $G$ when $H$ is a finite $p$-group with a normal subgroup $N$ of order $p$
such that $N \le \Phi(H)$, where $\Phi(H)$ is the Frattini subgroup of $H$, and $H/N \cong G$.

Formalized by `MathlibExt.GroupTheory.FrattiniExtensionSequenceKourovka16Problem12Wanted.IsPhiExtension`, a definition declared in [WantedExt/GroupTheory/FrattiniExtensionSequenceKourovka16Problem12Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrattiniExtensionSequenceKourovka16Problem12Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/extensions-of-p-groups/index.html#is-phi-extension).

## Kourovka Problem 16.12 (infinite chains of $\Phi$-extensions)

The statement, a question
of Ya. G. Berkovich, that for every prime $p$ and every nontrivial finite $p$-group $G$ there are
groups $G_0, G_1, G_2, \dots$ with $G_0 \cong G$ such that, for every $i \ge 0$, $G_{i+1}$ is a
$\Phi$-extension of $G_i$ for the prime $p$.

Formalized by `MathlibExt.GroupTheory.FrattiniExtensionSequenceKourovka16Problem12Wanted.phiExtensionSequence`, a definition declared in [WantedExt/GroupTheory/FrattiniExtensionSequenceKourovka16Problem12Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrattiniExtensionSequenceKourovka16Problem12Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/extensions-of-p-groups/index.html#phi-extension-sequence).

## Infinite chains of $\Phi$-extensions (Kourovka 16.12)

For every prime $p$ and every
nontrivial finite $p$-group $G$ there are groups $G_0, G_1, G_2, \dots$ with $G_0 \cong G$ such
that, for every $i \ge 0$, $G_{i+1}$ is a $\Phi$-extension of $G_i$ for the prime $p$. This answers
Kourovka Problem 16.12 in the affirmative: the Kourovka Archive answers "Yes, it is", citing
Kamornikov (2008).

The trivial group is excluded: it has no $\Phi$-extension, since a group of order $p$ has trivial
Frattini subgroup.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.12 (Ya. G. Berkovich); resolution: S. F. Kamornikov, Izv. Gomel' Univ. 5 (2008), 200-201 (Russian), Kourovka Archive, Problem 16.12 (Yes, it is).

Stated but not proved: `MathlibExt.GroupTheory.FrattiniExtensionSequenceKourovka16Problem12Wanted.phiExtensionSequence_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FrattiniExtensionSequenceKourovka16Problem12Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrattiniExtensionSequenceKourovka16Problem12Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/extensions-of-p-groups/index.html#phi-extension-sequence-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Φ-extensions of p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/extensions-of-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-p-groups/extensions-of-p-groups)
