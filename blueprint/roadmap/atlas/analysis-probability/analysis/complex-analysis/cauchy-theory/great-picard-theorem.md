---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.GreatPicardWanted.IsEssentialIsolatedSingularityAt, MathlibExt.Analysis.Complex.GreatPicardWanted.greatPicard
statement: formalized
proof: formalized
---

# Great Picard theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/great-picard-theorem/index.html).

## Essential isolated singularity

A function $f : \mathbb{C} \to \mathbb{C}$ has an
essential isolated singularity at $c \in \mathbb{C}$ when $f$ is holomorphic on some punctured
disc $0 < |z - c| < r$ with $r > 0$, $f(z)$ has no finite limit as $z \to c$ with $z \ne c$, and
$|f(z)|$ does not tend to $\infty$ as $z \to c$ with $z \ne c$.

Formalized by `MathlibExt.Analysis.Complex.GreatPicardWanted.IsEssentialIsolatedSingularityAt`, a definition declared in [MathlibExt/Analysis/Complex/GreatPicard.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/GreatPicard.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/great-picard-theorem/index.html#is-essential-isolated-singularity-at).

## Great Picard theorem

Suppose $f : \mathbb{C} \to \mathbb{C}$ has an essential isolated
singularity at $c \in \mathbb{C}$. Then there is at most one $w \in \mathbb{C}$ for which some
$r > 0$ makes the set $\{z : 0 < |z - c| < r,\ f(z) = w\}$ finite; that is, with at most one
exception, $f$ takes every complex value infinitely often on every punctured disc around $c$.

## Sources

- Great Picard theorem, E. Picard 1879; see Ahlfors, Complex Analysis; Lean is essential isolated singularity version with finite-fiber exceptional set subsingleton, at most one value finitely often near c.

Formalized by `MathlibExt.Analysis.Complex.GreatPicardWanted.greatPicard`, a theorem declared in [MathlibExt/Analysis/Complex/GreatPicard.lean, line 1203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/GreatPicard.lean#L1203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/great-picard-theorem/index.html#great-picard).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Great Picard theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/great-picard-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/great-picard-theorem)
