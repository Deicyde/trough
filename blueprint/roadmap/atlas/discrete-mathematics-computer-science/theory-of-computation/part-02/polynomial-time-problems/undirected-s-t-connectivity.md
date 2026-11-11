---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.USTCONInL.ustconDec, MetaMathlibExt.Complexity.KeyTheorems.USTCONInL.ustcon_in_l
statement: formalized
---

# Undirected s-t connectivity

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/undirected-s-t-connectivity/index.html).

## Undirected s-t connectivity as a decision problem

A bitstring $x$ is a yes-instance
exactly when bitstring decoding of $x$, as a tuple $(n, E, s, t)$ of natural numbers $n$, $s$, $t$
and a finite list $E$ of pairs of natural numbers, succeeds and returns $(n, E, s, t)$ such that
$s < n$, $t < n$, and there are pairwise distinct natural numbers $v_0, \dots, v_k$, all less than
$n$, with $v_0 = s$, $v_k = t$ and, for every $i < k$, $(v_i, v_{i+1}) \in E$ or
$(v_{i+1}, v_i) \in E$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.USTCONInL.ustconDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/USTCONInLWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/USTCONInLWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/undirected-s-t-connectivity/index.html#ustcon-dec).

## Undirected ST-connectivity is in L (Reingold)

The undirected $s$-$t$ connectivity
decision problem lies in the class $\mathsf{L}$ of decision problems decidable in deterministic
logarithmic space.

## Sources

- O. Reingold, "Undirected connectivity in log-space", Journal of the ACM 55 (2008), 1-24 (STOC 2005).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.USTCONInL.ustcon_in_l` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/USTCONInLWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/USTCONInLWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/undirected-s-t-connectivity/index.html#ustcon-in-l).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Undirected s-t connectivity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/polynomial-time-problems/undirected-s-t-connectivity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/polynomial-time-problems/undirected-s-t-connectivity)
