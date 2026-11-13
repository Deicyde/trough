---
declaration: section
origin: cited
lean: MetaMathlibExt.eulerSeidelMatrix, MetaMathlibExt.eulerSeidelMatrix_eq_sum
statement: formalized
proof: formalized
---

# Euler–Seidel matrices

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/euler-seidel-matrices/index.html).

## Euler–Seidel matrix

Let $M$ be a type with an addition and let $(a_n)_{n \ge 0}$ be a
sequence in $M$. The Euler–Seidel matrix of $a$ is the array $(a_n^k)_{n, k \ge 0}$, with entry
$a_n^k$ in position $(n, k)$, defined by $a_n^0 = a_n$ and
$a_n^k = a_n^{k-1} + a_{n+1}^{k-1}$ for $k \ge 1$.

Formalized by `MetaMathlibExt.eulerSeidelMatrix`, a definition declared in [MathlibExt/Combinatorics/Enumerative/EulerSeidelMatrix.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/EulerSeidelMatrix.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/euler-seidel-matrices/index.html#euler-seidel-matrix).

## Closed form of the Euler–Seidel matrix

Let $M$ be an additive commutative monoid and let
$(a_n)_{n \ge 0}$ be a sequence in $M$. For all $n, k \ge 0$, the entry $a_n^k$ of the
Euler–Seidel matrix of $a$ equals $\sum_{i=0}^{k} \binom{k}{i} a_{n+i}$.

Formalized by `MetaMathlibExt.eulerSeidelMatrix_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/EulerSeidelMatrix.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/EulerSeidelMatrix.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/euler-seidel-matrices/index.html#euler-seidel-matrix-eq-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler–Seidel matrices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/euler-seidel-matrices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/euler-seidel-matrices)
