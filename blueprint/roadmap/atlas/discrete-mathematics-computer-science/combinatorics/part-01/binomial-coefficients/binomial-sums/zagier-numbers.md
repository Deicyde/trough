---
declaration: section
origin: cited
lean: MetaMathlibExt.dombTypeSum, MetaMathlibExt.zagierNumber
statement: formalized
proof: formalized
---

# Zagier numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/zagier-numbers/index.html).

## Domb-type sums

For natural numbers $n$, $r$, $s$ and $t$, the Domb-type sum is the
natural number

$$D(n, r, s, t) = \sum_{k=0}^{n} \binom{n}{k}^r \binom{2k}{k}^s \binom{2(n-k)}{n-k}^t.$$

The paper uses positive $r$; the same finite formula is meaningful at $r = 0$.

Formalized by `MetaMathlibExt.dombTypeSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ZagierNumber.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ZagierNumber.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/zagier-numbers/index.html#domb-type-sum).

## Zagier numbers

For a natural number $n$, the Zagier number $Z(n)$ is the Domb-type sum
$D(n, 1, 1, 1)$, that is,

$$Z(n) = \sum_{k=0}^{n} \binom{n}{k} \binom{2k}{k} \binom{2(n-k)}{n-k}.$$

These are the numbers of OEIS A081085.

Formalized by `MetaMathlibExt.zagierNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/ZagierNumber.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ZagierNumber.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/zagier-numbers/index.html#zagier-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zagier numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/zagier-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/zagier-numbers)
