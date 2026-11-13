---
declaration: section
origin: cited
lean: MetaMathlibExt.sulankeB, MetaMathlibExt.sulankeA
statement: formalized
proof: formalized
---

# Sulanke arrays

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/sulanke-arrays/index.html).

## Sulanke array B

The Sulanke array $B$ assigns a natural number $B(k, i)$ to every pair of
natural numbers $k$ and $i$. It is defined by recursion on $k$: $B(0, 0) = 1$, $B(0, i) = 0$ for
$i \ge 1$, $B(k+1, 0) = B(k, 0)$, and for all $k$ and $i$

$$B(k+1, i+1) = \bigl(B(k, i+1) + 2B(k, i)\bigr) + \bigl(B(k, i) + 2B(k, i-1)\bigr),$$

where $B(k, -1)$ is read as $0$.

This is the recurrence obtained by eliminating the Sulanke array $A$, given by
$A(k+1, i) = B(k, i) + 2B(k, i-1)$, from $B(k+1, i) = A(k+1, i) + A(k+1, i-1)$, with values at
negative indices read as $0$.

Formalized by `MetaMathlibExt.sulankeB`, a definition declared in [MathlibExt/Combinatorics/SulankeNumber.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SulankeNumber.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/sulanke-arrays/index.html#sulanke-b).

## Sulanke array A

The Sulanke array $A$ assigns a natural number $A(k, i)$ to every pair of
natural numbers $k$ and $i$. It is defined from the Sulanke array $B$ by $A(0, i) = 0$ for every
$i$, $A(k+1, 0) = B(k, 0)$ for every $k$, and $A(k+1, i+1) = B(k, i+1) + 2B(k, i)$ for all $k$
and $i$.

Formalized by `MetaMathlibExt.sulankeA`, a definition declared in [MathlibExt/Combinatorics/SulankeNumber.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SulankeNumber.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/sulanke-arrays/index.html#sulanke-a).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sulanke arrays](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/sulanke-arrays/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/sulanke-arrays)
