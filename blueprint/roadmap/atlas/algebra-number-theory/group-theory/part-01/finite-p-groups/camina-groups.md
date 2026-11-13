---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.nilpotentCaminaClassBounded, MathlibExt.GroupTheory.NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.nilpotentCaminaClassBounded_refuted
statement: formalized
---

# Camina groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/camina-groups/index.html).

## Bounded class for nilpotent Camina-type groups

Kourovka Problem 17.47 (S. H. Ghate,
A. S. Muktibodh) asks whether this proposition holds: there is a natural number $c$ such that
every nilpotent group $G$ in which, for every $x \notin [G, G]$, the coset $x[G, G]$ of the
commutator subgroup $[G, G]$ equals the conjugacy class $x^G$ of $x$, has nilpotency class at
most $c$.

Formalized by `MathlibExt.GroupTheory.NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.nilpotentCaminaClassBounded`, a definition declared in [WantedExt/GroupTheory/NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/camina-groups/index.html#nilpotent-camina-class-bounded).

## Nilpotent Camina-type groups have unbounded class

There is no natural number $c$ such that
every nilpotent group $G$ in which, for every $x \notin [G, G]$, the coset $x[G, G]$ of the
commutator subgroup $[G, G]$ equals the conjugacy class $x^G$ of $x$, has nilpotency class at
most $c$. So Kourovka Problem 17.47 has a negative answer.

Ionin and Semidetnov (Answer 4.2) construct, for every integer $c \ge 2$, a nilpotent group of
class exactly $c$ in which $x^G = x[G, G]$ for every $x \notin [G, G]$. The Kourovka Notebook
(21st issue) answers 17.47 "No, there is no such bound".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 17.47 (S. H. Ghate, A. S. Muktibodh); resolution: V. Ionin and A. Semidetnov, On some more problems from the Kourovka Notebook, preprint, arXiv:2608.29219 (2026; solutions found with the assistance of large language models and checked by the authors, per its abstract), Answer 4.2 (for every integer c ≥ 2 there exists a nilpotent Camina group of class exactly c); the Kourovka Notebook (21st issue) marks 17.47 solved (No, there is no such bound), https://arxiv.org/abs/2608.29219.

Stated but not proved: `MathlibExt.GroupTheory.NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.nilpotentCaminaClassBounded_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentCaminaClassUnboundedKourovka17Problem47Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/camina-groups/index.html#nilpotent-camina-class-bounded-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Camina groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/camina-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/finite-p-groups/camina-groups)
