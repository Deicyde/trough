---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.primeOrderElementManyEigenvalues, MathlibExt.GroupTheory.LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.primeOrderElementManyEigenvalues_holds
statement: formalized
---

# Eigenvalues of elements of prime order

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/eigenvalues-of-elements-of-prime-order/index.html).

## Zalesskiĭ's problem on eigenvalues of elements of prime order (Kourovka 11.35)

The
statement that for every $n$, every finite subgroup $H$ of $\mathrm{GL}_n(\mathbb{C})$ and every
$h \in H$ of prime order $p$ that lies in no abelian normal subgroup of $H$, the element $h$ has at
least $(p - 1)/2$ distinct eigenvalues, that is, $p - 1 \le 2k$ where $k$ is the number of distinct
roots of the characteristic polynomial of $h$.

Formalized by `MathlibExt.GroupTheory.LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.primeOrderElementManyEigenvalues`, a definition declared in [WantedExt/GroupTheory/LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/eigenvalues-of-elements-of-prime-order/index.html#prime-order-element-many-eigenvalues).

## Robinson's theorem on eigenvalues of elements of prime order

For every $n$, if $H$ is a finite
subgroup of $\mathrm{GL}_n(\mathbb{C})$ and $h \in H$ has prime order $p$ and lies in no abelian
normal subgroup of $H$, then $h$ has at least $(p - 1)/2$ distinct eigenvalues, that is,
$p - 1 \le 2k$ where $k$ is the number of distinct roots of the characteristic polynomial of $h$.
This answers Kourovka Notebook Problem 11.35 (A. E. Zalesskiĭ) in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.35 (A. E. Zalesskiĭ); resolution: G. R. Robinson, J. Algebra 178, no. 2 (1995), 635-642, Kourovka Archive, Problem 11.35: "Yes, it is", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.primeOrderElementManyEigenvalues_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LinearGroupPrimeOrderEigenvaluesKourovka11Problem35Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/eigenvalues-of-elements-of-prime-order/index.html#prime-order-element-many-eigenvalues-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eigenvalues of elements of prime order](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/eigenvalues-of-elements-of-prime-order/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/linear-groups/eigenvalues-of-elements-of-prime-order)
