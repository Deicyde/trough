---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GaleRyserWanted.prefixSum, MathlibExt.Combinatorics.GaleRyserWanted.prefixSum_eq_sum_fin, MathlibExt.Combinatorics.GaleRyserWanted.gale_ryser
statement: formalized
proof: formalized
---

# Gale–Ryser theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/gale-ryser-theorem/index.html).

## Prefix sum

For a sequence $r = (r_0, \dots, r_{m-1})$ of natural numbers and a natural
number $k$, the prefix sum of $r$ of length $k$ is $\sum_{i < \min(k, m)} r_i$, the sum of the
first $k$ entries of $r$, or of all entries when $k \ge m$.

Formalized by `MathlibExt.Combinatorics.GaleRyserWanted.prefixSum`, a definition declared in [MathlibExt/Combinatorics/GaleRyser.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/GaleRyser.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/gale-ryser-theorem/index.html#prefix-sum).

## Prefix sums within the sequence length

For a sequence $r = (r_0, \dots, r_{m-1})$ of
natural numbers and a natural number $k \le m$, the prefix sum of $r$ of length $k$ equals
$\sum_{i=0}^{k-1} r_i$.

Formalized by `MathlibExt.Combinatorics.GaleRyserWanted.prefixSum_eq_sum_fin`, a theorem declared in [MathlibExt/Combinatorics/GaleRyser.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/GaleRyser.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/gale-ryser-theorem/index.html#prefix-sum-eq-sum-fin).

## Gale–Ryser theorem

Let $r = (r_0, \dots, r_{m-1})$ and $c = (c_0, \dots, c_{n-1})$ be
nonincreasing sequences of natural numbers. There is an $m \times n$ matrix with entries in
$\{0, 1\}$ whose $i$-th row sums to $r_i$ for every $i$ and whose $j$-th column sums to $c_j$ for
every $j$ if and only if $\sum_{i < m} r_i = \sum_{j < n} c_j$ and, for every $k \le m$,

$$\sum_{i < k} r_i \le \sum_{j < n} \min(k, c_j).$$

## Sources

- D. Gale, A theorem on flows in networks, Pacific J. Math. 7 (1957), 1073-1082, DOI 10.2140/pjm.1957.7.1073; H. J. Ryser, Combinatorial properties of matrices of zeros and ones, Canad. J. Math. 9 (1957), 371-377, DOI 10.4153/CJM-1957-044-3.

Formalized by `MathlibExt.Combinatorics.GaleRyserWanted.gale_ryser`, a theorem declared in [MathlibExt/Combinatorics/GaleRyser.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/GaleRyser.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/gale-ryser-theorem/index.html#gale-ryser).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gale–Ryser theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/gale-ryser-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/designs-latin-squares/gale-ryser-theorem)
