---
declaration: section
origin: cited
lean: MetaMathlibExt.catalan_odd_iff, MetaMathlibExt.catalan_not_perfect_power
statement: formalized
proof: formalized
---

# Arithmetic properties of Catalan numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/arithmetic-properties-of-catalan-numbers/index.html).

## Parity of Catalan numbers

For every natural number $n$, the $n$th Catalan number $C_n$
is odd if and only if $n = 2^a - 1$ for some natural number $a$.

## Sources

- Alon Regev, "The Central Component of a Triangulation", Journal of Integer Sequences 16 (2013), Article 13.4.1, theorem `oddcats`, lines 132–147 of <https://cs.uwaterloo.ca/journals/JIS/VOL16/Regev/regev4.tex>. This entry records the displayed theorem statement. Lines 85–88 define `C_n` with the standard indexing used by Mathlib's `catalan`, so no index shift is required. The natural subtraction in `2 ^ a - 1` is safe because `2 ^ a` is positive. No parallel Catalan definition is introduced.

Formalized by `MetaMathlibExt.catalan_odd_iff`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CatalanParity.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CatalanParity.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/arithmetic-properties-of-catalan-numbers/index.html#catalan-odd-iff).

## Catalan numbers other than $1$ are not perfect powers

For every natural number $n \ge 2$, the
$n$-th Catalan number $C_n$ is not a perfect power: there are no natural numbers $m$ and $k$
with $k \ge 2$ and $C_n = m^k$.

The proof of Checcoli and D'Adderio checks small cases directly, and for $n \ge 6$ uses a
Ramanujan prime $p$ with $n + 2 \le p < 2n$, which divides $C_n$ exactly once, so $C_n = m^k$
with $k \ge 2$ is impossible.

## Sources

- Nathaniel Benjamin, Grant Fickes, Eugene Fiorini, Edgar Jaramillo Rodriguez, Eric Jovinelly, and Tony W. H. Wong, "Primes and Perfect Powers in the Catalan Triangle," Journal of Integer Sequences 22 (2019), Article 19.7.6, Theorem [Checcoli–D'Adderio], lines 148–150, https://cs.uwaterloo.ca/journals/JIS/VOL22/Fiorini/fiorini3.tex

Formalized by `MetaMathlibExt.catalan_not_perfect_power`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CatalanPerfectPower.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CatalanPerfectPower.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/arithmetic-properties-of-catalan-numbers/index.html#catalan-not-perfect-power).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic properties of Catalan numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/arithmetic-properties-of-catalan-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/arithmetic-properties-of-catalan-numbers)
