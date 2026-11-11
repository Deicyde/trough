---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NormalClosureMinimalElementKourovka11Problem82Wanted.minimalNormalClosureElementConj, MathlibExt.GroupTheory.NormalClosureMinimalElementKourovka11Problem82Wanted.minimalNormalClosureElementConj_refuted
statement: formalized
---

# Normal closures in free groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/normal-closures-in-free-groups/index.html).

## Shortest elements of normal closures in free groups (Kourovka 11.82, Remeslennikov)

The
statement that for every free group $F$ and every $r \ne 1$ in $F$, if $s$ is a nontrivial element
of the normal closure $R$ of $r$ in $F$ whose reduced word length is minimal among the nontrivial
elements of $R$, then $s$ is conjugate to $r$, to $r^{-1}$, or, for some $f \in F$, to
$[r, f] = r^{-1} f^{-1} r f$ or to $[r^{-1}, f] = r f^{-1} r^{-1} f$.

Formalized by `MathlibExt.GroupTheory.NormalClosureMinimalElementKourovka11Problem82Wanted.minimalNormalClosureElementConj`, a definition declared in [WantedExt/GroupTheory/NormalClosureMinimalElementKourovka11Problem82Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NormalClosureMinimalElementKourovka11Problem82Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/normal-closures-in-free-groups/index.html#minimal-normal-closure-element-conj).

## Negative answer to Kourovka 11.82 on shortest elements of normal closures

There are a free
group $F$, an element $r \ne 1$ of $F$, and a nontrivial element $s$ of the normal closure $R$ of
$r$ in $F$ whose reduced word length is minimal among the nontrivial elements of $R$, such that $s$
is conjugate neither to $r$ nor to $r^{-1}$, nor, for any $f \in F$, to
$[r, f] = r^{-1} f^{-1} r f$ or to $[r^{-1}, f] = r f^{-1} r^{-1} f$.

The Kourovka Archive answers 11.82 "No, not always" (McCool).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.82 (V. N. Remeslennikov); resolution: J. McCool, Glasgow Math. J. 43, no. 1 (2001), 123-124, Kourovka Archive, Problem 11.82: "No, not always", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.NormalClosureMinimalElementKourovka11Problem82Wanted.minimalNormalClosureElementConj_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/NormalClosureMinimalElementKourovka11Problem82Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NormalClosureMinimalElementKourovka11Problem82Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/normal-closures-in-free-groups/index.html#minimal-normal-closure-element-conj-refu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal closures in free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/normal-closures-in-free-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/normal-closures-in-free-groups)
