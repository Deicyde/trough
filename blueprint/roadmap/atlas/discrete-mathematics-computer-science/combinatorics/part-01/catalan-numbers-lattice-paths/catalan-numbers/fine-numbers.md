---
declaration: section
origin: cited
lean: MetaMathlibExt.fineNumber, MetaMathlibExt.fineNumber_eq_sum
statement: formalized
proof: formalized
---

# Fine numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/fine-numbers/index.html).

## Fine numbers

For a natural number $n$, the Fine number $F(n)$, indexed from $0$ so
that $F(0) = 1$, is the rational number

$$F(n) = \frac{1}{n+1} \sum_{i=0}^{n} (-2)^i \, (i+1) \binom{2(n+1)}{n-i}.$$

## Sources

- Fine numbers (OEIS A000957), zero-based: `fineNumber n` is source `𝔽_(n+1)`. Source explicit formula `𝔽_n = (1/n) * ∑_{i=1}^n (-2)^(i-1) * i * C(2n, n-i)` with `𝔽_1 = 1`, from JIS VOL21/Janjic3/janjic96.tex lines 105-108 and 157-158. <https://cs.uwaterloo.ca/journals/JIS/VOL21/Janjic3/janjic96.tex>.

Formalized by `MetaMathlibExt.fineNumber`, a definition declared in [MathlibExt/Combinatorics/FineNumber.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/FineNumber.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/fine-numbers/index.html#fine-number).

## Explicit formula for the Fine numbers

For every natural number $n$, the Fine number
$F(n)$, indexed from $0$ so that $F(0) = 1$, satisfies

$$F(n) = \frac{1}{n+1} \sum_{i=0}^{n} (-2)^i \, (i+1) \binom{2(n+1)}{n-i}.$$

The source indexes from $1$: writing $\mathbb{F}_m = F(m - 1)$ for $m \ge 1$, it states
$\mathbb{F}_m = \frac{1}{m} \sum_{i=1}^{m} (-2)^{i-1} \, i \binom{2m}{m-i}$, which becomes the
formula above on setting $m = n + 1$ and shifting the summation index down by one.

Formalized by `MetaMathlibExt.fineNumber_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/FineNumber.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/FineNumber.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/fine-numbers/index.html#fine-number-eq-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fine numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/fine-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/fine-numbers)
