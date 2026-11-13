---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.subsetSumCountBound, MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.fixedSizeSubsetSumCountBound, MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.subsetSumCountBound_holds, MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.fixedSizeSubsetSumCountBound_holds
statement: formalized
---

# Concentration of subset sums

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/concentration-of-subset-sums/index.html).

## Erdős Problem 362: subsets with a given sum

There is a real constant $C$ such that for
every nonempty finite set $A \subseteq \mathbb{N}$ with $N$ elements and every $t \in \mathbb{N}$,
the number of subsets $S \subseteq A$ with $\sum_{n \in S} n = t$ is at most
$C \cdot 2^N / N^{3/2}$.

Formalized by `MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.subsetSumCountBound`, a definition declared in [WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/concentration-of-subset-sums/index.html#subset-sum-count-bound).

## Erdős Problem 362: subsets of a given size with a given sum

There is a real constant $C$
such that for every nonempty finite set $A \subseteq \mathbb{N}$ with $N$ elements and all
$l, t \in \mathbb{N}$, the number of $l$-element subsets $S \subseteq A$ with
$\sum_{n \in S} n = t$ is at most $C \cdot 2^N / N^2$.

Formalized by `MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.fixedSizeSubsetSumCountBound`, a definition declared in [WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/concentration-of-subset-sums/index.html#fixed-size-subset-sum-count-bound).

## Sárközy–Szemerédi bound on subsets with a given sum

There is a real constant $C$ such that for
every nonempty finite set $A \subseteq \mathbb{N}$ with $N$ elements and every $t \in \mathbb{N}$,
the number of subsets $S \subseteq A$ with $\sum_{n \in S} n = t$ is at most
$C \cdot 2^N / N^{3/2}$.

Sárközy and Szemerédi removed the factor $(\log N)^{3/2}$ from the Erdős–Moser bound; Stanley later
found the extremal sets.

## Sources

- T. F. Bloom, Erdős Problems, Problem #362, https://www.erdosproblems.com/362 (status PROVED (LEAN)); resolution: A. Sárközy and E. Szemerédi, Über ein Problem von Erdős und Moser, Acta Arith. (1965), 205-208; G. Halász, Estimates for the concentration function of combinatorial number theory and probability, Period. Math. Hungar. (1977), 197-211, erdosproblems.com/362: the first question answered by Sárközy and Szemerédi, the second by Halász as a consequence of a multi-dimensional result.

Stated but not proved: `MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.subsetSumCountBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/concentration-of-subset-sums/index.html#subset-sum-count-bound-holds).

## Halász's bound on subsets of a given size with a given sum

There is a real constant $C$ such
that for every nonempty finite set $A \subseteq \mathbb{N}$ with $N$ elements and all
$l, t \in \mathbb{N}$, the number of $l$-element subsets $S \subseteq A$ with
$\sum_{n \in S} n = t$ is at most $C \cdot 2^N / N^2$.

Halász proved this as a consequence of a multi-dimensional concentration estimate.

## Sources

- T. F. Bloom, Erdős Problems, Problem #362, https://www.erdosproblems.com/362 (status PROVED (LEAN)); resolution: A. Sárközy and E. Szemerédi, Über ein Problem von Erdős und Moser, Acta Arith. (1965), 205-208; G. Halász, Estimates for the concentration function of combinatorial number theory and probability, Period. Math. Hungar. (1977), 197-211, erdosproblems.com/362: the first question answered by Sárközy and Szemerédi, the second by Halász as a consequence of a multi-dimensional result.

Stated but not proved: `MathlibExt.Combinatorics.SubsetSumConcentrationErdosProblem362Wanted.fixedSizeSubsetSumCountBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SubsetSumConcentrationErdosProblem362Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/concentration-of-subset-sums/index.html#fixed-size-subset-sum-count-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Concentration of subset sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/concentration-of-subset-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/concentration-of-subset-sums)
