---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ErdosEntireFunctionCountableDensePreimageWanted.conjecture, MathlibExt.Analysis.ErdosEntireFunctionCountableDensePreimageWanted.conjecture_holds
statement: formalized
---

# Countable dense sets as preimages under entire functions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/countable-dense-sets-as-preimages-under-entire-f/index.html).

## Erdős's problem on countable dense preimages

This is the statement that for any two
countable dense subsets $A$ and $B$ of $\mathbb{C}$, there is an entire function
$f : \mathbb{C} \to \mathbb{C}$ such that for every $z \in \mathbb{C}$, $f(z) \in B$ if and only
if $z \in A$; that is, $f^{-1}(B) = A$.

## Sources

- Research Problems in Function Theory, Problem 2.31 (record AMR-022-2031).

Formalized by `MathlibExt.Analysis.ErdosEntireFunctionCountableDensePreimageWanted.conjecture`, a definition declared in [WantedExt/Analysis/ErdosEntireFunctionCountableDensePreimageWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ErdosEntireFunctionCountableDensePreimageWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/countable-dense-sets-as-preimages-under-entire-f/index.html#conjecture).

## Every countable dense set is a preimage of any other under an entire function

For any two
countable dense subsets $A$ and $B$ of $\mathbb{C}$, there is an entire function
$f : \mathbb{C} \to \mathbb{C}$ such that for every $z \in \mathbb{C}$, $f(z) \in B$ if and only
if $z \in A$; that is, $f^{-1}(B) = A$.

Hayman's update to Problem 2.31 reports that Barth and Schneider constructed such functions.

## Sources

- K. F. Barth and W. J. Schneider, Entire functions mapping arbitrary countable dense sets and their complements onto each other, J. London Math. Soc. (2) 4 (1972), 482-488, https://doi.org/10.1112/jlms/s2-4.3.482.

Stated but not proved: `MathlibExt.Analysis.ErdosEntireFunctionCountableDensePreimageWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/ErdosEntireFunctionCountableDensePreimageWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ErdosEntireFunctionCountableDensePreimageWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/countable-dense-sets-as-preimages-under-entire-f/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Countable dense sets as preimages under entire functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/countable-dense-sets-as-preimages-under-entire-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/entire-functions/countable-dense-sets-as-preimages-under-entire-f)
