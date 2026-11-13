---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ExactlyOneNoncommutatorKourovka17Problem76Wanted.exactlyOneNoncommutator, MathlibExt.GroupTheory.ExactlyOneNoncommutatorKourovka17Problem76Wanted.exactlyOneNoncommutator_holds
statement: formalized
---

# Non-commutators in finite groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/non-commutators-in-finite-groups/index.html).

## Kourovka Problem 17.76 (finite groups with exactly one non-commutator)

This is the
statement that there is a finite group $G$ of order greater than $2$ in which exactly one element is
not a commutator, that is, not of the form $x^{-1}y^{-1}xy$ with $x, y \in G$.

Formalized by `MathlibExt.GroupTheory.ExactlyOneNoncommutatorKourovka17Problem76Wanted.exactlyOneNoncommutator`, a definition declared in [WantedExt/GroupTheory/ExactlyOneNoncommutatorKourovka17Problem76Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ExactlyOneNoncommutatorKourovka17Problem76Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/non-commutators-in-finite-groups/index.html#exactly-one-noncommutator).

## A finite group with exactly one non-commutator

There is a finite group $G$ of order greater
than $2$ in which exactly one element is not a commutator, that is, not of the form $x^{-1}y^{-1}xy$
with $x, y \in G$.

Resolved true: Skresanov constructs an infinite series of finite groups with exactly one element
that is not a commutator, the smallest of order 16609443840, and Hatem and Siniora find two such
groups of order 368640, the smallest possible order. The Kourovka Notebook (21st issue) answers
17.76 "Yes".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 17.76 (D. MacHale); resolution: S. V. Skresanov, Siberian Electron. Math. Rep. 23 (2026), 603-607 (preprint On finite groups with exactly one noncommutator, arXiv:2509.17587); O. Hatem and D. Siniora, Int. J. Group Theory 15 (2026), 161-167 (preprint A group with exactly one noncommutator, arXiv:2511.00541), Skresanov, abstract (an infinite series of such groups, the smallest of order 16609443840); Hatem-Siniora, abstract (two non-isomorphic groups of order 368640, the smallest order); the Kourovka Notebook (21st issue) marks 17.76 solved (Yes, such groups do exist, and there are infinitely many examples), https://arxiv.org/abs/2509.17587.

Stated but not proved: `MathlibExt.GroupTheory.ExactlyOneNoncommutatorKourovka17Problem76Wanted.exactlyOneNoncommutator_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ExactlyOneNoncommutatorKourovka17Problem76Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ExactlyOneNoncommutatorKourovka17Problem76Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/non-commutators-in-finite-groups/index.html#exactly-one-noncommutator-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Non-commutators in finite groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/non-commutators-in-finite-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/non-commutators-in-finite-groups)
