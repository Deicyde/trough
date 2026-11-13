---
declaration: section
origin: cited
lean: MathlibExt.Analysis.RubelHInfinityCoherenceWanted.Disc, MathlibExt.Analysis.RubelHInfinityCoherenceWanted.IsHInf, MathlibExt.Analysis.RubelHInfinityCoherenceWanted.HInfinitySubring, MathlibExt.Analysis.RubelHInfinityCoherenceWanted.HInfinity, MathlibExt.Analysis.RubelHInfinityCoherenceWanted.RubelProblem524, MathlibExt.Analysis.RubelHInfinityCoherenceWanted.RubelProblem524_holds
statement: formalized
---

# Finitely generated ideals of H^∞

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html).

## The open unit disc

The open unit disc
$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$, the open ball of radius $1$ about $0$ in
$\mathbb{C}$, taken as a space in its own right whose points are the points of the disc.

Formalized by `MathlibExt.Analysis.RubelHInfinityCoherenceWanted.Disc`, an abbreviation declared in [WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html#disc).

## Membership in $H^\infty$ of the unit disc

A complex-valued function $f$ on the open unit
disc $\mathbb{D}$ belongs to $H^\infty$ when there is a function $F : \mathbb{C} \to \mathbb{C}$
that is complex differentiable on $\mathbb{D}$ and satisfies $f(z) = F(z)$ for every
$z \in \mathbb{D}$, and there is a real number $C \ge 0$ with $|f(z)| \le C$ for every
$z \in \mathbb{D}$.

## Sources

- [AMR-022-5024], Research Problems in Function Theory, Problem 5.24.

Formalized by `MathlibExt.Analysis.RubelHInfinityCoherenceWanted.IsHInf`, a definition declared in [WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html#is-hinf).

## The ring $H^\infty$ as a subring of functions on the disc

$H^\infty$ is the subring of
the ring of all complex-valued functions on the open unit disc $\mathbb{D}$, under pointwise
addition and multiplication, consisting of the functions that belong to $H^\infty$: those that
agree on $\mathbb{D}$ with a function $\mathbb{C} \to \mathbb{C}$ complex differentiable on
$\mathbb{D}$ and are bounded on $\mathbb{D}$.

## Sources

- [AMR-022-5024], Research Problems in Function Theory, Problem 5.24.

Formalized by `MathlibExt.Analysis.RubelHInfinityCoherenceWanted.HInfinitySubring`, a definition declared in [WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html#hinfinity-subring).

## Elements of $H^\infty$

The space whose points are the members of the subring $H^\infty$
of complex-valued functions on the open unit disc $\mathbb{D}$, that is, the bounded functions
on $\mathbb{D}$ that agree on $\mathbb{D}$ with a function complex differentiable there.

## Sources

- [AMR-022-5024], Research Problems in Function Theory, Problem 5.24.

Formalized by `MathlibExt.Analysis.RubelHInfinityCoherenceWanted.HInfinity`, a definition declared in [WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html#hinfinity).

## Rubel's problem on intersections of finitely generated ideals in $H^\infty$

The
statement that for any two finitely generated ideals $I$ and $J$ of the commutative ring
$H^\infty$ of bounded holomorphic functions on the open unit disc, the intersection $I \cap J$ is
finitely generated.

Rubel asked whether this statement is true.

## Sources

- [AMR-022-5024], Research Problems in Function Theory, Problem 5.24 (L. A. Rubel).

Formalized by `MathlibExt.Analysis.RubelHInfinityCoherenceWanted.RubelProblem524`, a definition declared in [WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html#rubel-problem524).

## McVoy–Rubel theorem on finitely generated ideals of $H^\infty$

For any two finitely
generated ideals $I$ and $J$ of the commutative ring $H^\infty$ of bounded holomorphic functions
on the open unit disc, the intersection $I \cap J$ is finitely generated. This answers Rubel's
Problem 5.24 positively.

Resolved by McVoy and Rubel (J. Funct. Anal. 21 (1976) 76-87), who proved that $H^\infty$ of the
unit disc is a coherent ring. Restated in Mortini, arXiv:1606.05568, and Hayman-Lingham
Update 5.24.

## Sources

- R. Mortini, Noncoherent uniform algebras in C^n (2016), arXiv:1606.05568, https://arxiv.org/abs/1606.05568.

Stated but not proved: `MathlibExt.Analysis.RubelHInfinityCoherenceWanted.RubelProblem524_holds` is written with `theorem_wanted` in [WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/RubelHInfinityCoherenceWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html#rubel-problem524-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finitely generated ideals of H^∞](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/analytic-function-spaces/finitely-generated-ideals-of-h)
