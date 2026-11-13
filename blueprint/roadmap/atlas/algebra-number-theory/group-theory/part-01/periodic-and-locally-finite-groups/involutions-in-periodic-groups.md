---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.InvolutionClassOddProductsKourovka10Problem62Wanted.periodicGroupGeneratedByOddInvolutionClass, MathlibExt.GroupTheory.InvolutionClassOddProductsKourovka10Problem62Wanted.periodicGroupGeneratedByOddInvolutionClass_holds
statement: formalized
---

# Involutions in periodic groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/involutions-in-periodic-groups/index.html).

## Kourovka Problem 10.62 on involution classes with products of odd order

The proposition
(Kourovka 10.62, A. I. Sozutov) that there is a periodic group $G$ that has no subgroup of index
$2$ and contains an involution $x$ such that the conjugacy class $X$ of $x$ generates $G$ and the
product $yz$ has odd order for all $y, z \in X$.

The condition includes $y = z$, where $yz = 1$ has order $1$.

Formalized by `MathlibExt.GroupTheory.InvolutionClassOddProductsKourovka10Problem62Wanted.periodicGroupGeneratedByOddInvolutionClass`, a definition declared in [WantedExt/GroupTheory/InvolutionClassOddProductsKourovka10Problem62Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvolutionClassOddProductsKourovka10Problem62Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/involutions-in-periodic-groups/index.html#periodic-group-generated-by-odd-involuti).

## Positive answer to Kourovka Problem 10.62

There is a periodic group $G$ that has no
subgroup of index $2$ and contains an involution $x$ such that the conjugacy class $X$ of $x$
generates $G$ and the product $yz$ has odd order for all $y, z \in X$.

Kinyon and Urban's 2026 preprint (an AI-generated solution confirmed by M. Amelio; Section 3.7,
Proposition 3.5) constructs, for every sufficiently large odd prime $p$, an infinite
three-generated perfect group of exponent $2p$ whose involutions form one conjugacy class
generating the group, the product of any two distinct involutions having order $p$; being perfect,
it has no subgroup of index $2$. The Kourovka Notebook (21st issue) marks 10.62 solved, "Example
constructed".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 10.62 (A. I. Sozutov); resolution: M. Kinyon and J. Urban (with Codex gpt-6-astra), Results on problems from the Kourovka Notebook, preprint (2026), Section 3.7, Proposition 3.5 (built on Amelio's geometric construction); AI solution confirmed by M. Amelio; the Kourovka Notebook (21st issue) marks 10.62 solved, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.InvolutionClassOddProductsKourovka10Problem62Wanted.periodicGroupGeneratedByOddInvolutionClass_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/InvolutionClassOddProductsKourovka10Problem62Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/InvolutionClassOddProductsKourovka10Problem62Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/involutions-in-periodic-groups/index.html#periodic-group-generated-by-odd-involuti-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Involutions in periodic groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/involutions-in-periodic-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/involutions-in-periodic-groups)
