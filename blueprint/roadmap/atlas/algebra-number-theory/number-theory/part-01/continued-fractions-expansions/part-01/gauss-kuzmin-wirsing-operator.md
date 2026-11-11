---
declaration: section
origin: cited
lean: MathlibExt.Analysis.WirsingConstant.gkwTerm, MathlibExt.Analysis.WirsingConstant.IsEigenvalue, MathlibExt.Analysis.WirsingConstant.isEigenvalue_one, MathlibExt.Analysis.WirsingConstant.gkwTermHol, MathlibExt.Analysis.WirsingConstant.IsHolomorphicEigenvalue, MathlibExt.Analysis.WirsingConstant.wirsingConstant, MathlibExt.Analysis.WirsingConstantWanted.mayerRoepstorffLowerBound_wanted, MathlibExt.Analysis.WirsingConstantWanted.mayerRoepstorffUpperBound_wanted
statement: formalized
---

# Gauss–Kuzmin–Wirsing operator

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html).

## Terms of the Gauss–Kuzmin–Wirsing series

For a function $f : \mathbb{R} \to \mathbb{R}$,
a real number $x$ and a natural number $k$, the $k$-th term of the Gauss–Kuzmin–Wirsing series
of $f$ at $x$ is $\frac{1}{(x+k+1)^2} f\left(\frac{1}{x+k+1}\right)$, with the convention
$1/0 = 0$.

Summing these terms over $k \ge 0$ gives the Gauss–Kuzmin–Wirsing operator, whose value at $x$ is
$\sum_{k \ge 1} (x+k)^{-2} f(1/(x+k))$ when this series converges absolutely and $0$ otherwise;
for $x \in [0, 1]$ the series converges absolutely whenever $f$ is bounded on $[0, 1]$.

Formalized by `MathlibExt.Analysis.WirsingConstant.gkwTerm`, a definition declared in [MathlibExt/Analysis/WirsingConstant.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/WirsingConstant.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#gkw-term).

## Eigenvalues of the Gauss–Kuzmin–Wirsing operator on continuous functions

A real number
$\lambda$ is an eigenvalue of the Gauss–Kuzmin–Wirsing operator in the continuous model when
there is a function $f : \mathbb{R} \to \mathbb{R}$, continuous on $[0, 1]$, bounded on
$[0, 1]$ and not identically zero on $[0, 1]$, such that for every $x \in [0, 1]$

$$\sum_{k \ge 1} \frac{1}{(x+k)^2} f\left(\frac{1}{x+k}\right) = \lambda f(x).$$

Boundedness follows from continuity on $[0, 1]$ and is recorded explicitly; it makes the series
converge on $[0, 1]$. This continuous model is not the source's spectral space: it admits
eigenvalues that the holomorphic theory excludes (for example $1/3$, from eigenfunction lifts
under inversion), so it is kept only as a pointwise model exhibiting the dominant eigenvalue
$1$. The Wirsing constant is defined over holomorphic eigenfunctions instead.

Formalized by `MathlibExt.Analysis.WirsingConstant.IsEigenvalue`, a definition declared in [MathlibExt/Analysis/WirsingConstant.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/WirsingConstant.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#is-eigenvalue).

## The Gauss–Kuzmin–Wirsing operator has eigenvalue one

There is a function
$f : \mathbb{R} \to \mathbb{R}$ that is continuous on $[0, 1]$, bounded on $[0, 1]$ and not
identically zero on $[0, 1]$, such that
$\sum_{k \ge 1} \frac{1}{(x+k)^2} f\left(\frac{1}{x+k}\right) = f(x)$ for every $x \in [0, 1]$;
that is, $1$ is an eigenvalue of the Gauss–Kuzmin–Wirsing operator in the continuous model.

An eigenfunction is the Gauss density $x \mapsto 1/(1+x)$, for which the series telescopes.

Formalized by `MathlibExt.Analysis.WirsingConstant.isEigenvalue_one`, a theorem declared in [MathlibExt/Analysis/WirsingConstant.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/WirsingConstant.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#is-eigenvalue-one).

## Terms of the complex Gauss–Kuzmin–Wirsing series

For a function
$f : \mathbb{C} \to \mathbb{C}$, a complex number $z$ and a natural number $k$, the $k$-th term
of the Gauss–Kuzmin–Wirsing series of $f$ at $z$ is
$\frac{1}{(z+k+1)^2} f\left(\frac{1}{z+k+1}\right)$, with the convention $1/0 = 0$.

Formalized by `MathlibExt.Analysis.WirsingConstant.gkwTermHol`, a definition declared in [MathlibExt/Analysis/WirsingConstant.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/WirsingConstant.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#gkw-term-hol).

## Holomorphic eigenvalues of the Gauss–Kuzmin–Wirsing operator

Let
$D = \{z \in \mathbb{C} : |z - 1| < 3/2\}$ be the Mayer disk. A complex number $\lambda$ is a
holomorphic eigenvalue of the Gauss–Kuzmin–Wirsing operator when there is a function
$f : \mathbb{C} \to \mathbb{C}$, holomorphic on $D$ and not identically zero on $D$, such that
for every $z \in D$

$$\sum_{k \ge 1} \frac{1}{(z+k)^2} f\left(\frac{1}{z+k}\right) = \lambda f(z).$$

This is the function space of Mayer and Roepstorff, on which the spectrum of the operator below
the dominant eigenvalue $1$ is the source's spectral data.

Formalized by `MathlibExt.Analysis.WirsingConstant.IsHolomorphicEigenvalue`, a definition declared in [MathlibExt/Analysis/WirsingConstant.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/WirsingConstant.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#is-holomorphic-eigenvalue).

## Wirsing constant

The Wirsing constant is the supremum in $\mathbb{R}$ of $|\lambda|$
over all holomorphic eigenvalues $\lambda \ne 1$ of the Gauss–Kuzmin–Wirsing operator on the
Mayer disk $\{z \in \mathbb{C} : |z - 1| < 3/2\}$, with the convention that the supremum is $0$
when there is no such $\lambda$ or when these absolute values are unbounded.

The source's spectral theorem, that this supremum is attained at the negative eigenvalue
$\lambda_2$ and that no other holomorphic eigenvalue lies between it and $1$ in absolute value,
is not asserted here.

Formalized by `MathlibExt.Analysis.WirsingConstant.wirsingConstant`, a definition declared in [MathlibExt/Analysis/WirsingConstant.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/WirsingConstant.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#wirsing-constant).

## Mayer–Roepstorff lower bound for the Wirsing constant

The
Wirsing constant is at least $0.30366299$.

## Sources

- Mayer and Roepstorff (1987), eq. (5.20), catalogue lower bound `0.30366299`, certified via generalized Temple inequalities.

Stated but not proved: `MathlibExt.Analysis.WirsingConstantWanted.mayerRoepstorffLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/Analysis/WirsingConstantWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WirsingConstantWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#mayer-roepstorff-lower-bound-wanted).

## Mayer–Roepstorff upper bound for the Wirsing constant

The
Wirsing constant is at most $0.30366327$.

## Sources

- Mayer and Roepstorff (1987), eq. (5.20), catalogue upper bound `0.30366327`.

Stated but not proved: `MathlibExt.Analysis.WirsingConstantWanted.mayerRoepstorffUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/Analysis/WirsingConstantWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WirsingConstantWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html#mayer-roepstorff-upper-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gauss–Kuzmin–Wirsing operator](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-wirsing-operator)
