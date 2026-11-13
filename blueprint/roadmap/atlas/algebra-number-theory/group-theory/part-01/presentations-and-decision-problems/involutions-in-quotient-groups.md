---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.InvolutionFreeQuotientKourovka18Problem94Wanted.involutionFreeQuotientByNonSquarePower, MathlibExt.GroupTheory.InvolutionFreeQuotientKourovka18Problem94Wanted.involutionFreeQuotientByNonSquarePower_refuted
statement: formalized
---

# Involutions in quotient groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/involutions-in-quotient-groups/index.html).

## Sozutov's question on involutions in quotients (Kourovka 18.94)

This is the statement
that whenever $G$ is a group without involutions (if $g^2 = 1$ then $g = 1$), $a \in G$ is not the
square of any element of $G$, and $n$ is an odd natural number, the quotient of $G$ by the normal
closure of $a^n$ has no involutions: every element $y$ of the quotient with $y^2 = 1$ is $1$.

Formalized by `MathlibExt.GroupTheory.InvolutionFreeQuotientKourovka18Problem94Wanted.involutionFreeQuotientByNonSquarePower`, a definition declared in [WantedExt/GroupTheory/InvolutionFreeQuotientKourovka18Problem94Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvolutionFreeQuotientKourovka18Problem94Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/involutions-in-quotient-groups/index.html#involution-free-quotient-by-non-square-p).

## Quotients by the normal closure of an odd power of a non-square can have involutions

There
exist a group $G$ without involutions (if $g^2 = 1$ then $g = 1$), an element $a \in G$ that is
not the square of any element of $G$, and an odd natural number $n$ such that the quotient of $G$
by the normal closure of $a^n$ contains an involution, that is, an element $y \ne 1$ with
$y^2 = 1$. This answers Kourovka Problem 18.94 in the negative.

Besides an example of V. I. Trofimov, the group $G = \langle a, b \mid a^2 = b^2 \rangle$ with
$n = 1$ is an example: its quotient by the normal closure of $a$ has order $2$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.94 (A. I. Sozutov); resolution: V. I. Trofimov (example), as recorded in the Kourovka Archive, Problem 18.94, Kourovka Archive, Problem 18.94: No, not always, by an example of V. I. Trofimov; another example: G = ⟨a, b | a² = b²⟩ modulo ⟨a^G⟩ has order 2, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.InvolutionFreeQuotientKourovka18Problem94Wanted.involutionFreeQuotientByNonSquarePower_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/InvolutionFreeQuotientKourovka18Problem94Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvolutionFreeQuotientKourovka18Problem94Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/involutions-in-quotient-groups/index.html#involution-free-quotient-by-non-square-p-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Involutions in quotient groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/involutions-in-quotient-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/involutions-in-quotient-groups)
