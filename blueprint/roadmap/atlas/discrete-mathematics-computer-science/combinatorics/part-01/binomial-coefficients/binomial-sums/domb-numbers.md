---
declaration: section
origin: cited
lean: MetaMathlibExt.dombNumber, MetaMathlibExt.dombNumber_unfold
statement: formalized
proof: formalized
---

# Domb numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/domb-numbers/index.html).

## Domb numbers

For a natural number $n$, the Domb number $\mathrm{Domb}(n)$ is the
Domb-type sum $D(n,2,1,1)$, that is,
$\mathrm{Domb}(n) = \sum_{k=0}^{n} \binom{n}{k}^2 \binom{2k}{k} \binom{2(n-k)}{n-k}$
(OEIS A002895).

Formalized by `MetaMathlibExt.dombNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/DombNumber.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DombNumber.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/domb-numbers/index.html#domb-number).

## Explicit formula for the Domb numbers

For every natural number $n$, the Domb number
$\mathrm{Domb}(n)$ equals $\sum_{k=0}^{n} \binom{n}{k}^2 \binom{2k}{k} \binom{2(n-k)}{n-k}$.

Formalized by `MetaMathlibExt.dombNumber_unfold`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DombNumber.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DombNumber.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/domb-numbers/index.html#domb-number-unfold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Domb numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/domb-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/domb-numbers)
