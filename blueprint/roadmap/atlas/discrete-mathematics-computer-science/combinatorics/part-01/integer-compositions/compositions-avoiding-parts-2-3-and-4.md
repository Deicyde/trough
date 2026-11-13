---
declaration: section
origin: cited
lean: MetaMathlibExt.octagonalPyramidalNumber, MetaMathlibExt.octagonalPyramidalCompositions, MetaMathlibExt.octagonalPyramidalNumber_eq_composition_card
statement: formalized
proof: formalized
---

# Compositions avoiding parts 2, 3 and 4

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-avoiding-parts-2-3-and-4/index.html).

## Octagonal pyramidal numbers

For a natural number $k$, the $k$-th octagonal pyramidal
number is $k(k+1)(2k-1)/2$.

Formalized by `MetaMathlibExt.octagonalPyramidalNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/OctagonalPyramidalNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/OctagonalPyramidalNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-avoiding-parts-2-3-and-4/index.html#octagonal-pyramidal-number).

## Compositions avoiding parts 2, 3 and 4

For a natural number $k$, the restricted
compositions of $k + 14$ are the ordered compositions of $k + 14$ into $k$ positive parts with no
part equal to $2$, $3$ or $4$, that is, the tuples $(c_1, \dots, c_k)$ of positive integers with
$c_1 + \dots + c_k = k + 14$ and $c_i \notin \{2, 3, 4\}$ for every $i$.

Formalized by `MetaMathlibExt.octagonalPyramidalCompositions`, a definition declared in [MathlibExt/Combinatorics/Enumerative/OctagonalPyramidalNumber.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/OctagonalPyramidalNumber.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-avoiding-parts-2-3-and-4/index.html#octagonal-pyramidal-compositions).

## Octagonal pyramidal numbers count restricted compositions

For every positive integer $k$,
the number of ordered compositions of $k + 14$ into $k$ positive parts with no part equal to $2$,
$3$ or $4$ is the $k$-th octagonal pyramidal number $k(k+1)(2k-1)/2$.

## Sources

- Milan Janjić, *Binomial Coefficients and Enumeration of Restricted Words*, Journal of Integer Sequences 19 (2016), Article 16.7.3, the corollary.

Formalized by `MetaMathlibExt.octagonalPyramidalNumber_eq_composition_card`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/OctagonalPyramidalComposition.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/OctagonalPyramidalComposition.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-avoiding-parts-2-3-and-4/index.html#octagonal-pyramidal-number-eq-compositio).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compositions avoiding parts 2, 3 and 4](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-avoiding-parts-2-3-and-4/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-compositions/compositions-avoiding-parts-2-3-and-4)
