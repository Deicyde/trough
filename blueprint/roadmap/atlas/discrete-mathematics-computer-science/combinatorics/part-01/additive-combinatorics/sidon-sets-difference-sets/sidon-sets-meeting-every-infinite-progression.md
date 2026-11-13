---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SidonSetComplementProgressionErdosProblem198Wanted.sidonComplementContainsProgression, MathlibExt.Combinatorics.SidonSetComplementProgressionErdosProblem198Wanted.sidonComplementContainsProgression_refuted
statement: formalized
---

# Sidon sets meeting every infinite progression

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets-meeting-every-infinite-progression/index.html).

## Erdős Problem 198

The proposition that the complement of every Sidon set
$A \subseteq \mathbb{N}$ contains an infinite arithmetic progression: for every Sidon set
$A \subseteq \mathbb{N}$ there are natural numbers $a$ and $d \ge 1$ such that $a + kd \notin A$
for every natural number $k$.

Formalized by `MathlibExt.Combinatorics.SidonSetComplementProgressionErdosProblem198Wanted.sidonComplementContainsProgression`, a definition declared in [WantedExt/Combinatorics/SidonSetComplementProgressionErdosProblem198Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SidonSetComplementProgressionErdosProblem198Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets-meeting-every-infinite-progression/index.html#sidon-complement-contains-progression).

## Erdős Problem 198 is false

It is not the case that the complement of every Sidon set
$A \subseteq \mathbb{N}$ contains an infinite arithmetic progression: there is a Sidon set
$A \subseteq \mathbb{N}$ such that for all natural numbers $a$ and $d \ge 1$ some term $a + kd$,
$k \in \mathbb{N}$, lies in $A$. Here $A$ is Sidon when $w + x = y + z$ with $w, x, y, z \in A$
forces $\{w, x\} = \{y, z\}$.

To construct such a set, enumerate the infinite progressions $P_1, P_2, \ldots$ and pick
$a_n \in P_n$ with $a_n > 2 a_{n-1}$; the resulting lacunary set is Sidon and meets every infinite
progression. erdosproblems.com/198 records this construction (implicit in Baumgartner's paper) and
the explicit example $\{(n + 1)! + n : n \ge 0\}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #198, https://www.erdosproblems.com/198 (status DISPROVED (LEAN)); resolution: J. E. Baumgartner, Partitioning vector spaces, J. Combin. Theory Ser. A 18 (1975), 231-233; construction recorded on erdosproblems.com/198, erdosproblems.com/198: answered no; a lacunary set with one element in each infinite progression (implicit in [Ba75]), or explicitly A = {(n + 1)! + n : n ≥ 0}, https://www.erdosproblems.com/198.

Stated but not proved: `MathlibExt.Combinatorics.SidonSetComplementProgressionErdosProblem198Wanted.sidonComplementContainsProgression_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/SidonSetComplementProgressionErdosProblem198Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SidonSetComplementProgressionErdosProblem198Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets-meeting-every-infinite-progression/index.html#sidon-complement-contains-progression-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sidon sets meeting every infinite progression](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets-meeting-every-infinite-progression/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/sidon-sets-meeting-every-infinite-progression)
