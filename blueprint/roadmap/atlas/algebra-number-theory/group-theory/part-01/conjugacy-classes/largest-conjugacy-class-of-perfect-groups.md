---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.perfectCentrelessOrderLeMaxClassSq, MathlibExt.GroupTheory.PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.perfectCentrelessOrderLeMaxClassSq_refuted
statement: formalized
---

# Largest conjugacy class of perfect groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/largest-conjugacy-class-of-perfect-groups/index.html).

## Kourovka 20.30: the order of a perfect centreless group and its largest conjugacy class

The proposition that every finite group $G$ that is perfect ($[G, G] = G$) and has trivial centre
contains an element $x$ with $|G| \le |x^G|^2$, where $x^G$ is the conjugacy class of $x$.
Equivalently, $|G| \le n^2$, where $n$ is the largest size of a conjugacy class of $G$.

Formalized by `MathlibExt.GroupTheory.PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.perfectCentrelessOrderLeMaxClassSq`, a definition declared in [WantedExt/GroupTheory/PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/largest-conjugacy-class-of-perfect-groups/index.html#perfect-centreless-order-le-max-class-sq).

## Perfect centreless groups need not have order at most the square of the largest class size

It is not true that every finite group $G$ that is perfect ($[G, G] = G$) and has trivial centre
contains an element $x$ with $|G| \le |x^G|^2$, where $x^G$ is the conjugacy class of $x$. That
is, some perfect centreless finite group $G$ satisfies $|G| > n^2$, where $n$ is the largest size
of a conjugacy class of $G$.

Muliarchyk (Theorem 1.1) constructs a perfect centreless finite group of order $120 \cdot 5^{68}$
whose largest conjugacy class has size $30 \cdot 5^{32}$, so $|G| / n^2 = 250/3 > 1$; the 21st
issue of the Kourovka Notebook marks 20.30 solved ("No, not always"). The preprint acknowledges
assistance from ChatGPT.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.30 (P. M. Neumann and M. R. Vaughan-Lee; I. B. Gorshkov); resolution: K. Muliarchyk, Perfect centreless groups with large centralizers, preprint (2026), Kourovka Notebook site, Theorem 1.1: an explicit perfect centreless finite group of order 120·5^68 whose largest conjugacy class has size 30·5^32, so |G|/n² = 250/3 > 1 (built from a class-three Baker-Campbell-Hausdorff group over F₅ and an SL₂(F₅)-action); Theorem 6.1: no bound |G| ≤ C n^c holds for all perfect centreless finite groups; Kourovka Notebook (21st issue), Problem 20.30: No, not always, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka_20_30_solution.pdf.

Stated but not proved: `MathlibExt.GroupTheory.PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.perfectCentrelessOrderLeMaxClassSq_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PerfectCentrelessOrderMaxClassKourovka20Problem30Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/largest-conjugacy-class-of-perfect-groups/index.html#perfect-centreless-order-le-max-class-sq-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Largest conjugacy class of perfect groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/largest-conjugacy-class-of-perfect-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/conjugacy-classes/largest-conjugacy-class-of-perfect-groups)
