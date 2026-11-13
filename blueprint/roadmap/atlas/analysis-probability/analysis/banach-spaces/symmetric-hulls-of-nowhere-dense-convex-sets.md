---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook65Wanted.ScottishBookProblem65Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook65Wanted.mazur65_refuted
statement: formalized
---

# Symmetric hulls of nowhere dense convex sets

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/symmetric-hulls-of-nowhere-dense-convex-sets/index.html).

## Mazur's symmetric hull claim (Scottish Book Problem 65)

The claim that for every real
Banach space $E$ and every convex set $W \subseteq E$ with $0 \in W$, if the closure of $W$ has
empty interior (that is, $W$ is nowhere dense), then the closure of the convex hull of
$W \cup (-W)$ also has empty interior. The convex hull of $W \cup (-W)$ is the smallest convex
set containing $W$ that is symmetric about the origin.

The typescript's parenthetical identifies this set with the difference set $W - W$, which is
larger in general; the smallest-set reading is adopted here. For the Ad 65 counterexample $W$
(non-decreasing functions, a cone) the two constructions coincide, so the counterexample still
applies.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook65Wanted.ScottishBookProblem65Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook65Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook65Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/symmetric-hulls-of-nowhere-dense-convex-sets/index.html#scottish-book-problem65-claim).

## Mazur's Problem 65 has a negative answer

The symmetric hull claim of Scottish Book
Problem 65 is false: there are a real Banach space $E$ and a convex set $W \subseteq E$ with
$0 \in W$ whose closure has empty interior, such that the closure of the convex hull of
$W \cup (-W)$ has nonempty interior.

## Sources

- S. Mazur, Problem 65 of the Scottish Book; typescript Ad 65 records the negative answer, with the counterexample of the set `W` of non-decreasing functions in the space `(C)` of continuous functions: `W` is convex, nowhere dense, and contains `0`, while the symmetric convex set containing `W` contains all functions of bounded variation and is not nowhere dense (indeed, it is dense, since it contains the polynomials). For this `W` (a cone) the `W ∪ -W` hull and the difference-set construction coincide, so the counterexample refutes the corrected claim too.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook65Wanted.mazur65_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook65Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook65Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/symmetric-hulls-of-nowhere-dense-convex-sets/index.html#mazur65-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Symmetric hulls of nowhere dense convex sets](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/symmetric-hulls-of-nowhere-dense-convex-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/symmetric-hulls-of-nowhere-dense-convex-sets)
