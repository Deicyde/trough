---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HermanProblem290Wanted.IsDiophantine, MathlibExt.Analysis.HermanProblem290Wanted.AnalyticCircleDiffeo, MathlibExt.Analysis.HermanProblem290Wanted.HasRotationNumber, MathlibExt.Analysis.HermanProblem290Wanted.IsAnalyticallyConjugateToRotation, MathlibExt.Analysis.HermanProblem290Wanted.conjecture, MathlibExt.Analysis.HermanProblem290Wanted.conjecture_holds
statement: formalized
---

# Linearization of circle diffeomorphisms

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html).

## Diophantine numbers

A real number $\alpha$ is Diophantine when there are real numbers
$\gamma > 0$ and $\tau \ge 0$ such that $|\alpha - p/q| \ge \gamma / q^{2 + \tau}$ for every
integer $p$ and every integer $q \ge 1$.

## Sources

- Hayman (2018), Problem 2.90; https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.HermanProblem290Wanted.IsDiophantine`, a definition declared in [WantedExt/Analysis/HermanProblem290Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HermanProblem290Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html#is-diophantine).

## Real-analytic circle diffeomorphisms

A real-analytic orientation-preserving
diffeomorphism of the circle is given by a lift $F : \mathbb{R} \to \mathbb{R}$ together with an
inverse lift $G : \mathbb{R} \to \mathbb{R}$, both real-analytic on all of $\mathbb{R}$, such that
for every real $x$ we have $F(x + 1) = F(x) + 1$, $G(x + 1) = G(x) + 1$, $G(F(x)) = x$ and
$F(G(x)) = x$, and $F$ is strictly increasing.

## Sources

- Hayman (2018), Problem 2.90; https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.HermanProblem290Wanted.AnalyticCircleDiffeo`, a structure declared in [WantedExt/Analysis/HermanProblem290Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HermanProblem290Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html#analytic-circle-diffeo).

## Rotation number of a lift

Let $F : \mathbb{R} \to \mathbb{R}$ be a function, and for a
natural number $n$ write $F^n$ for the $n$-th iterate of $F$. Then $F$ has rotation number
$\alpha \in \mathbb{R}$ when, for every real $x$, $(F^n(x) - x)/n$ tends to $\alpha$ as $n$ tends
to infinity.

## Sources

- Hayman (2018), Problem 2.90; https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.HermanProblem290Wanted.HasRotationNumber`, a definition declared in [WantedExt/Analysis/HermanProblem290Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HermanProblem290Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html#has-rotation-number).

## Analytic conjugacy to a rotation

A function $F : \mathbb{R} \to \mathbb{R}$ is
analytically conjugate to the rotation by $\alpha \in \mathbb{R}$ when there is a real-analytic
circle diffeomorphism with lift $H$ such that $H(F(x)) = H(x) + \alpha$ for every real $x$.

## Sources

- Hayman (2018), Problem 2.90; https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.HermanProblem290Wanted.IsAnalyticallyConjugateToRotation`, a definition declared in [WantedExt/Analysis/HermanProblem290Wanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HermanProblem290Wanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html#is-analytically-conjugate-to-rotation).

## Herman's analytic linearization problem

The statement that there is an irrational real
number $\alpha$ that is not Diophantine such that, for every real-analytic circle diffeomorphism
whose lift $F$ has rotation number $\alpha$, $F$ is analytically conjugate to the rotation by
$\alpha$.

M. R. Herman asked whether such an $\alpha$ exists; this is Problem 2.90 in Hayman's list.

## Sources

- Hayman (2018), Problem 2.90; https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.HermanProblem290Wanted.conjecture`, a definition declared in [WantedExt/Analysis/HermanProblem290Wanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HermanProblem290Wanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html#conjecture).

## Herman's analytic linearization problem has a positive answer

There is an irrational real
number $\alpha$ that is not Diophantine such that, for every real-analytic circle diffeomorphism
whose lift $F$ has rotation number $\alpha$, $F$ is analytically conjugate to the rotation by
$\alpha$.

Yoccoz characterized the Herman class $\mathcal{H}$ of rotation numbers $\alpha$ for which every
real-analytic circle diffeomorphism with rotation number $\alpha$ is analytically linearizable,
and proved that $\mathcal{H}$ strictly contains the set of Diophantine numbers; any $\alpha$ in
$\mathcal{H}$ that is not Diophantine has the required property.

## Sources

- H. Eliasson, B. Fayad and R. Krikorian, Jean-Christophe Yoccoz and the theory of circle diffeomorphisms (2018), arXiv:1810.07107 (account of J.-C. Yoccoz, Analytic linearization of circle diffeomorphisms, Lecture Notes in Math. 1784, Springer (2002), 125-173), https://arxiv.org/abs/1810.07107.

Stated but not proved: `MathlibExt.Analysis.HermanProblem290Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/HermanProblem290Wanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HermanProblem290Wanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linearization of circle diffeomorphisms](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/low-dimensional-dynamics/linearization-of-circle-diffeomorphisms)
