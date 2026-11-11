---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.finitelyManySimpleWithFullSpectrumSubgroup, MathlibExt.GroupTheory.SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.finitelyManySimpleWithFullSpectrumSubgroup_refuted
statement: formalized
---

# Subgroups with all prime divisors of a simple group

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/subgroups-with-all-prime-divisors-of-a-simple-gr/index.html).

## Kourovka Problem 11.64 (Monakhov)

The statement that there is a natural number $N$ such
that every finite simple group $G$ that is not isomorphic to the alternating group $A_n$ for any
natural number $n$ and has a proper subgroup $H$ with $\pi(H) = \pi(G)$ satisfies $|G| \le N$,
where $\pi(X)$ denotes the set of prime divisors of the order $|X|$.

Since there are finitely many groups of each order, this says that only finitely many such groups
$G$ exist up to isomorphism.

Formalized by `MathlibExt.GroupTheory.SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.finitelyManySimpleWithFullSpectrumSubgroup`, a definition declared in [WantedExt/GroupTheory/SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/subgroups-with-all-prime-divisors-of-a-simple-gr/index.html#finitely-many-simple-with-full-spectrum).

## Infinitely many simple groups with proper subgroups of equal prime set

Resolved false: the Kourovka Archive records (V. I. Zenkov) that the symplectic groups `G =
S_{4k}(2^s)` have proper subgroups `H ≅ Ω⁻_{4k}(2^s)` with `π(H) = π(G)`, an infinite family of
non-alternating finite simple groups. Source: E. I. Khukhro and V. D. Mazurov (eds.), Unsolved
Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of
Solved Problems, Problem 11.64 (V. S. Monakhov); resolution: V. I. Zenkov, letter of 10 March 1994,
Kourovka Archive, Problem 11.64: "No, there are infinitely many such groups. If `G = S_{4k}(2^s)`
and `H ≅ Ω⁻_{4k}(2^s)`, then `π(G) = π(H)`", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.finitelyManySimpleWithFullSpectrumSubgroup_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupPrimeSpectrumSubgroupKourovka11Problem64Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/subgroups-with-all-prime-divisors-of-a-simple-gr/index.html#finitely-many-simple-with-full-spectrum-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgroups with all prime divisors of a simple group](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orders-and-spectra/subgroups-with-all-prime-divisors-of-a-simple-gr/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orders-and-spectra/subgroups-with-all-prime-divisors-of-a-simple-gr)
