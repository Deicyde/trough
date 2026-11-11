---
declaration: section
origin: cited
lean: catalan_le_four_pow, MetaMathlibExt.CatalanGeneratingFunction.catalan_generating_function_sqrt
statement: formalized
proof: formalized
---

# Catalan numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/catalan-numbers/index.html).

## Catalan numbers are at most $4^n$

The `n`th Catalan number is at most `4 ^ n`.

Formalized by `catalan_le_four_pow`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Catalan/Bounds.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Catalan/Bounds.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/catalan-numbers/index.html#catalan-le-four-pow).

## Closed form of the Catalan generating function

Let $C_n$ be the $n$th Catalan number.
For every real number $x$ with $|x| < 1/4$ and $x \neq 0$,

$$
\sum_{n=0}^{\infty} C_n x^n = \frac{1 - \sqrt{1 - 4x}}{2x}.
$$

The hypothesis $x \neq 0$ excludes the removable singularity of the right-hand side at $x = 0$.

## Sources

- Paul Barry, "A Note on a Family of Generalized Pascal Matrices Defined by Riordan Arrays", Journal of Integer Sequences 16 (2013), Article 13.5.4, proposition lines 380–388, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Barry2/barry231.tex>. Mathlib has `PowerSeries.catalanSeries` and its quadratic functional equation, but its source file explicitly lists the square-root closed form as a TODO; this theorem records the analytic closed form rather than duplicating the formal series definition.

Formalized by `MetaMathlibExt.CatalanGeneratingFunction.catalan_generating_function_sqrt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CatalanGeneratingFunction.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/CatalanGeneratingFunction.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/catalan-numbers/index.html#catalan-generating-function-sqrt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Catalan numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/catalan-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/catalan-numbers)
