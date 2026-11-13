---
declaration: section
origin: cited
lean: MetaMathlibExt.compositionHalfIndexSet, MetaMathlibExt.mem_compositionHalfIndexSet, MetaMathlibExt.compositionHalfIndexSet_zero, MetaMathlibExt.compositionIndexSet, MetaMathlibExt.mem_compositionIndexSet, MetaMathlibExt.compositionIndexSet_zero, MetaMathlibExt.compositionHalfIndexSet_double
statement: formalized
proof: formalized
---

# Compositions with an odd number of parts

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html).

## The index set $S(m, n, q)$

For natural numbers $m$, $n$ and $q$, the set $S(m, n, q)$
consists of the natural numbers $k$ such that $2k \equiv n - q \pmod{m}$, where the difference
$n - q$ is taken in the integers, and $2k < n$.

For natural numbers the bound $2k < n$ is equivalent to $k \le \lfloor (n - 1)/2 \rfloor$; in
particular the set is empty when $n = 0$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Theorem 13 (`jis-2024-24.3.6-thm-13`).

Formalized by `MetaMathlibExt.compositionHalfIndexSet`, a definition declared in [MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html#composition-half-index-set).

## Membership in $S(m, n, q)$

For natural numbers $m$, $n$, $q$ and $k$, the number $k$
lies in the index set $S(m, n, q)$ if and only if $2k \equiv n - q \pmod{m}$, with the difference
taken in the integers, and $2k < n$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Theorem 13 (`jis-2024-24.3.6-thm-13`).

Formalized by `MetaMathlibExt.mem_compositionHalfIndexSet`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html#mem-composition-half-index-set).

## The index set $S(m, 0, q)$ is empty

For all natural numbers $m$ and $q$, the index set
$S(m, 0, q)$ is empty.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Theorem 13 (`jis-2024-24.3.6-thm-13`).

Formalized by `MetaMathlibExt.compositionHalfIndexSet_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html#composition-half-index-set-zero).

## The index set $T(m, n, q)$

For natural numbers $m$, $n$ and $q$, the set $T(m, n, q)$
consists of the natural numbers $k$ such that $k \equiv n - q \pmod{m}$, where the difference
$n - q$ is taken in the integers, and $k < n$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Theorem 17 (`jis-2024-24.3.6-thm-17`).

Formalized by `MetaMathlibExt.compositionIndexSet`, a definition declared in [MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html#composition-index-set).

## Membership in $T(m, n, q)$

For natural numbers $m$, $n$, $q$ and $k$, the number $k$
lies in the index set $T(m, n, q)$ if and only if $k \equiv n - q \pmod{m}$, with the difference
taken in the integers, and $k < n$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Theorem 17 (`jis-2024-24.3.6-thm-17`).

Formalized by `MetaMathlibExt.mem_compositionIndexSet`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html#mem-composition-index-set).

## The index set $T(m, 0, q)$ is empty

For all natural numbers $m$ and $q$, the index set
$T(m, 0, q)$ is empty.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Theorem 17 (`jis-2024-24.3.6-thm-17`).

Formalized by `MetaMathlibExt.compositionIndexSet_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html#composition-index-set-zero).

## Doubling identity for the composition index sets

For natural numbers $m$, $n$ and $q$,
let $S(m, n, q)$ be the set of natural numbers $k$ with $2k \equiv n - q \pmod{m}$ and $2k < n$,
and let $T(m, n, q)$ be the set of natural numbers $k$ with $k \equiv n - q \pmod{m}$ and
$k < n$, where the difference $n - q$ is taken in the integers. Then for all natural numbers
$m$, $n$ and $q$ the sets satisfy $S(2m, 2n, 2q) = T(m, n, q)$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Lemma 18 (`jis-2024-24.3.6-lem-18`).

Formalized by `MetaMathlibExt.compositionHalfIndexSet_double`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CompositionIndexSets.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html#composition-half-index-set-double).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compositions with an odd number of parts](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-compositions/compositions-with-an-odd-number-of-parts)
