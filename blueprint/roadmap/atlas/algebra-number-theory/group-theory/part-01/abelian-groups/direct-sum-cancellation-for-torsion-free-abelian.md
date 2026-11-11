---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.IsTorsionFreeAddGroup, MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummand, MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummandOfIso, MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummand_refuted, MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummandOfIso_refuted
statement: formalized
---

# Direct-sum cancellation for torsion-free abelian groups

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian/index.html).

## Torsion-free abelian group

An abelian group $A$, written additively, is torsion-free when
for every natural number $n \ne 0$ and every $a \in A$, $n a = 0$ implies $a = 0$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.IsTorsionFreeAddGroup`, a definition declared in [WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian/index.html#is-torsion-free-add-group).

## Bergman's absorption question (Kourovka 17.21(a))

The statement that for all torsion-free
abelian groups $A$, $B$, $C$, if $A \cong A \oplus B \oplus C$ then $A \cong A \oplus B$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummand`, a definition declared in [WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian/index.html#torsion-free-absorbs-direct-summand).

## Bergman's absorption question for isomorphic summands (Kourovka 17.21(b))

The statement
that for all torsion-free abelian groups $A$, $B$, $C$ with $B \cong C$, if
$A \cong A \oplus B \oplus C$ then $A \cong A \oplus B$.

Formalized by `MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummandOfIso`, a definition declared in [WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian/index.html#torsion-free-absorbs-direct-summand-of-i).

## Failure of direct-summand absorption for torsion-free abelian groups

There exist torsion-free
abelian groups $A$, $B$, $C$ with $A \cong A \oplus B \oplus C$ but $A \not\cong A \oplus B$; thus
the answer to Kourovka Problem 17.21(a) is negative.

The Kourovka Archive answers 17.21 "No, not necessarily, even in case b)", citing Corner (1964)
and Bergman (letter of 2011, an example with $B$ and $C$ of rank 1).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.21 (G. M. Bergman); resolution: A. L. S. Corner, in Proc. Colloq. Abelian Groups (Tihany, 1963), Budapest, 1964, 43-48; G. M. Bergman, letter of 20 February 2011, as recorded in the Kourovka Archive, Kourovka Archive, Problem 17.21 (No, not necessarily, even in case b); see Corner (1964); Bergman also has an example with B and C of rank 1).

Stated but not proved: `MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummand_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian/index.html#torsion-free-absorbs-direct-summand-refu).

## Failure of direct-summand absorption with isomorphic summands

There exist torsion-free abelian
groups $A$, $B$, $C$ with $B \cong C$ and $A \cong A \oplus B \oplus C$ but
$A \not\cong A \oplus B$; thus the answer to Kourovka Problem 17.21(b) is negative.

The Kourovka Archive answers 17.21(b) negatively as well ("even in case b)", Corner 1964; Bergman,
letter of 2011).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.21 (G. M. Bergman); resolution: A. L. S. Corner, in Proc. Colloq. Abelian Groups (Tihany, 1963), Budapest, 1964, 43-48; G. M. Bergman, letter of 20 February 2011, as recorded in the Kourovka Archive, Kourovka Archive, Problem 17.21 (No, not necessarily, even in case b); see Corner (1964); Bergman also has an example with B and C of rank 1).

Stated but not proved: `MathlibExt.GroupTheory.TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.torsionFreeAbsorbsDirectSummandOfIso_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TorsionFreeAbelianDirectSumCancellationKourovka17Problem21Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian/index.html#torsion-free-absorbs-direct-summand-of-i-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Direct-sum cancellation for torsion-free abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/abelian-groups/direct-sum-cancellation-for-torsion-free-abelian)
