---
declaration: section
origin: cited
lean: MetaMathlibExt.patalanGeneralizedBinomial, MetaMathlibExt.PQPatalanParams, MetaMathlibExt.pqPatalanNumber, MetaMathlibExt.pqSuperPatalanNumber, MetaMathlibExt.superPatalanNumber
statement: formalized
proof: formalized
---

# Patalan numbers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers/index.html).

## Binomial coefficient with rational upper argument

For a rational number $r$ and a natural
number $k$, the generalized binomial coefficient is the rational number
$\binom{r}{k} = r(r-1)\cdots(r-k+1)/k!$, which is $1$ for $k = 0$.

It is the binomial coefficient with fractional upper argument used in the $(p,q)$-Patalan
numbers.

## Sources

- Thomas M. Richardson, "The Super Patalan Numbers," Journal of Integer Sequences 18 (2015), Article 15.3.3, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Richardson/rich2.tex>.

Formalized by `MetaMathlibExt.patalanGeneralizedBinomial`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PQPatalanNumbers.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PQPatalanNumbers.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers/index.html#patalan-generalized-binomial).

## Admissible parameters for the (p,q)-Patalan numbers

An admissible parameter pair for the
$(p,q)$-Patalan numbers is a pair of natural numbers $p$ and $q$ with $p > 1$ and $0 < q < p$.

## Sources

- Thomas M. Richardson, "The Super Patalan Numbers," Journal of Integer Sequences 18 (2015), Article 15.3.3, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Richardson/rich2.tex>.

Formalized by `MetaMathlibExt.PQPatalanParams`, a structure declared in [MathlibExt/Combinatorics/Enumerative/PQPatalanNumbers.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PQPatalanNumbers.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers/index.html#pqpatalan-params).

## The (p,q)-Patalan numbers

For natural numbers $p$ and $q$ with $p > 1$ and $0 < q < p$,
the $(p,q)$-Patalan number with index $n \in \mathbb{N}$ is the rational number
$b(n) = -p^{2n+1} \binom{n - q/p}{n+1}$, where $\binom{r}{k} = r(r-1)\cdots(r-k+1)/k!$ is the
binomial coefficient with rational upper argument $r$.

## Sources

- Thomas M. Richardson, "The Super Patalan Numbers," Journal of Integer Sequences 18 (2015), Article 15.3.3, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Richardson/rich2.tex>.

Formalized by `MetaMathlibExt.pqPatalanNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PQPatalanNumbers.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PQPatalanNumbers.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers/index.html#pq-patalan-number).

## The (p,q)-super Patalan numbers

For natural numbers $p$ and $q$ with $p > 1$ and
$0 < q < p$, and natural numbers $i$ and $j$, the $(p,q)$-super Patalan number is the rational
number $Q(i,j) = (-1)^j p^{2(i+j)} \binom{i - q/p}{i+j}$, where
$\binom{r}{k} = r(r-1)\cdots(r-k+1)/k!$ is the binomial coefficient with rational upper
argument $r$.

## Sources

- Thomas M. Richardson, "The Super Patalan Numbers," Journal of Integer Sequences 18 (2015), Article 15.3.3.

Formalized by `MetaMathlibExt.pqSuperPatalanNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PQSuperPatalanNumbers.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PQSuperPatalanNumbers.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers/index.html#pq-super-patalan-number).

## Super Patalan numbers of order p

For a natural number $p > 1$ and natural numbers $i$ and
$j$, the super Patalan number of order $p$ is the $(p,q)$-super Patalan number with $q = 1$, that
is, the rational number $(-1)^j p^{2(i+j)} \binom{i - 1/p}{i+j}$, where
$\binom{r}{k} = r(r-1)\cdots(r-k+1)/k!$ is the binomial coefficient with rational upper
argument $r$.

Formalized by `MetaMathlibExt.superPatalanNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PQSuperPatalanNumbers.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PQSuperPatalanNumbers.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers/index.html#super-patalan-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Patalan numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/patalan-numbers)
