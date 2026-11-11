---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.inversions, MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.weakLE, MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.weakOrderSperner, MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.weakOrderSperner_holds
statement: formalized
---

# Sperner property of the weak order

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/sperner-property-of-the-weak-order/index.html).

## Inversion set of a permutation

For a permutation $\sigma$ of $\{0, \dots, n-1\}$, the
inversion set of $\sigma$ is the set of pairs of positions $(i, j)$ with $i < j$ and
$\sigma(j) < \sigma(i)$.

Formalized by `MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.inversions`, a definition declared in [WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/sperner-property-of-the-weak-order/index.html#inversions).

## Weak order on the symmetric group

For permutations $\sigma$ and $\tau$ of
$\{0, \dots, n-1\}$, $\sigma \le \tau$ in the weak order when the inversion set of $\sigma$ (its
pairs of positions $(i, j)$ with $i < j$ and $\sigma(j) < \sigma(i)$) is contained in the inversion
set of $\tau$.

Formalized by `MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.weakLE`, a definition declared in [WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/sperner-property-of-the-weak-order/index.html#weak-le).

## Sperner property of the weak order

This is the statement that for every $n$ and every
antichain $A$ of the weak order on the permutations of $\{0, \dots, n-1\}$ (where $\sigma \le \tau$
when the inversion set of $\sigma$ is contained in that of $\tau$), there is a $k$ such that $A$
has at most as many elements as there are permutations with exactly $k$ inversions. Equivalently,
no antichain is larger than the largest rank level, the rank of a permutation being its number of
inversions.

Formalized by `MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.weakOrderSperner`, a definition declared in [WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/sperner-property-of-the-weak-order/index.html#weak-order-sperner).

## The weak order on the symmetric group is Sperner

For every $n$ and every antichain $A$ of the
weak order on the symmetric group $S_n$ of permutations of $\{0, \dots, n-1\}$ (where
$\sigma \le \tau$ when the inversion set of $\sigma$ is contained in that of $\tau$), there is a $k$
such that $A$ has at most as many elements as there are permutations with exactly $k$ inversions.

Resolved true: Gaetz and Gao prove Stanley's conjecture that the weak order on $S_n$ is strongly
Sperner (a Peck poset); in particular it is Sperner.

## Sources

- J. Cooper, Combinatorial Problems I Like (2020 snapshot), Matroids, Lattices, and Posets, item 39, https://people.math.sc.edu/cooper/combprob.html; resolution: C. Gaetz and Y. Gao, A combinatorial sl₂-action and the Sperner property for the weak order, Proc. Amer. Math. Soc. 148 (2020); arXiv:1811.05501, abstract: the sl₂-representation resolves Stanley's conjecture that the weak order has the strong Sperner property (and is a Peck poset); strongly Sperner implies Sperner, https://doi.org/10.1090/proc/14655.

Stated but not proved: `MathlibExt.Combinatorics.WeakOrderSpernerAMR30Problem0039Wanted.weakOrderSperner_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/WeakOrderSpernerAMR30Problem0039Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/sperner-property-of-the-weak-order/index.html#weak-order-sperner-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sperner property of the weak order](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/sperner-property-of-the-weak-order/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/partially-ordered-sets/sperner-property-of-the-weak-order)
