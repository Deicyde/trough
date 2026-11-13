---
declaration: section
origin: cited
lean: legendreSym.sum_linear_eq_zero
statement: formalized
proof: formalized
---

# Power residues and reciprocity: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/index.html).

Quadratic and cubic residues, Legendre, Jacobi and Kronecker symbols, quadratic reciprocity and its extensions, Legendre-symbol sums.

## Linear Legendre-symbol sums vanish

Let $p$ be an odd prime and let $b$ and $c$ be
integers with $p \nmid b$. Then the Legendre symbols $\left(\frac{b\ell + c}{p}\right)$ for
$\ell = 0, 1, \dots, p - 1$ sum to $0$.

## Sources

- This is the first corollary of Theorem `thm1` in Ram Krishna Pandey and Anshumaan Parashar, *On Certain Sums with Quadratic Expressions Involving the Legendre Symbol*, Journal of Integer Sequences 21 (2018), Article 18.4.7, lines 190–193, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Pandey/pandey14.tex>. The proof here reindexes Mathlib's `quadraticChar_sum_zero` through the affine permutation `x ↦ b * x + c` of `ZMod p`.

Formalized by `legendreSym.sum_linear_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/LegendreSymbol/LinearSum.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LegendreSymbol/LinearSum.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/index.html#sum-linear-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Power residues and reciprocity](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/power-residues-reciprocity)
