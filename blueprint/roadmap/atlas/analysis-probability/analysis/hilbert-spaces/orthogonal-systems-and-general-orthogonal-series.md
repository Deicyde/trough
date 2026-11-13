---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook186Wanted.banach186_orthonormal_system_divergent_ae, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook51Wanted.SequenceSystemsAreCountable, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook51Wanted.FunctionSystemsAreCountable, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook51Wanted.orthogonal_systems_not_necessarily_countable, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook86Wanted.scottishBook86Measure, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook86Wanted.ScottishBookProblem86Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook86Wanted.banach86_refuted
statement: formalized
---

# Orthogonal systems and general orthogonal series

7 results, 4 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html).

## Banach's Problem 186: a complete orthonormal system with divergent Fourier series

There is a
sequence $(\varphi_i)_{i \ge 0}$ of square-integrable real functions on $[0, 1]$, with respect to
Lebesgue measure, that is orthonormal, $\int_0^1 \varphi_i \varphi_j \, dx = \delta_{ij}$ for
all $i, j$, and complete, in the sense that every square-integrable $g$ on $[0, 1]$ with
$\int_0^1 g \varphi_i \, dx = 0$ for all $i$ vanishes almost everywhere on $[0, 1]$, such that
the following holds: for every continuous $f \colon \mathbb{R} \to \mathbb{R}$ that is not
identically zero on $[0, 1]$, with Fourier coefficients $c_i = \int_0^1 f \varphi_i \, dx$, the
partial sums $\sum_{i < N} c_i \varphi_i(t)$ are unbounded in $N$ for almost every
$t \in [0, 1]$.

The $\varphi_i$ are not assumed continuous: the source imposes continuity only on $f$, and
continuity of the $\varphi_i$ would make the claim false (taking $f = \varphi_0$ would give
Fourier coefficients $\delta_{0i}$ and bounded partial sums).

## Sources

- S. Banach, Problem 186 of the Scottish Book; answered by A. M. Olevskii, "Fourier series with respect to general orthogonal systems" (1975). See the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook186Wanted.banach186_orthonormal_system_divergent_ae` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook186Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook186Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html#banach186-orthonormal-system-divergent-a).

## Countability of orthogonal systems of sequences

This is the statement that every set $S$
of real sequences $(f_n)_{n \in \mathbb{N}}$ with the following two properties is at most
countable: no member of $S$ is the zero sequence; and for any two distinct $f, g \in S$ the series
$\sum_{n} f_n g_n$ converges absolutely and its sum is $0$.

The zero sequence is excluded because it is orthogonal to everything, so without this it
would be a trivial member of every family.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook51Wanted.SequenceSystemsAreCountable`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook51Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook51Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html#sequence-systems-are-countable).

## Countability of orthogonal systems of functions

Let $\lambda$ be Lebesgue measure on
$[0, 1]$. This is the statement that every set $S$ of functions $[0, 1] \to \mathbb{R}$ with the
following three properties is at most countable: no member of $S$ is $\lambda$-almost everywhere
equal to $0$; any two members of $S$ that are equal $\lambda$-almost everywhere are equal; and
any two members $f, g$ of $S$ that are not equal $\lambda$-almost everywhere are measurable, have
$\lambda$-integrable product $fg$, and satisfy $\int_{[0, 1]} f g \, d\lambda = 0$.

No square-integrability is assumed. Without the second property, uncountably many
almost-everywhere-equal copies of one function would satisfy the orthogonality condition
vacuously. The first property excludes the indicator functions of single points, each of which
is zero almost everywhere.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook51Wanted.FunctionSystemsAreCountable`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook51Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook51Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html#function-systems-are-countable).

## Orthogonal systems need not be countable

Both of the following statements are false.
(a) Every set $S$ of real sequences $(f_n)_{n \in \mathbb{N}}$ in which no member is the zero
sequence, and in which for any two distinct $f, g \in S$ the series $\sum_n f_n g_n$ converges
absolutely with sum $0$, is at most countable. (b) Let $\lambda$ be Lebesgue measure on
$[0, 1]$. Every set $S$ of functions $[0, 1] \to \mathbb{R}$ in which no member is
$\lambda$-almost everywhere equal to $0$, no two distinct members are equal $\lambda$-almost
everywhere, and any two members $f, g$ that are not equal $\lambda$-almost everywhere are
measurable with $fg$ $\lambda$-integrable and $\int_{[0, 1]} f g \, d\lambda = 0$, is at most
countable.

This answers both parts of Mazur's Problem 51 of the Scottish Book in the negative: Plichko and
Razenkov construct a continuum-sized pairwise-orthogonal family of sequences, and from it an
uncountable orthogonal system of functions on an interval. No square-integrability is assumed;
in $\ell^2$ or $L^2$ an orthogonal family is at most countable, since those spaces are
separable Hilbert spaces.

## Sources

- S. Mazur, Problem 51 of the Scottish Book; A. M. Plichko and V. Razenkov, On three problems from the Scottish Book connected with orthogonal systems, Colloq. Math. 70 (1996), 227-234, Section 3; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook51Wanted.orthogonal_systems_not_necessarily_countable` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook51Wanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook51Wanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html#orthogonal-systems-not-necessarily-count).

## Lebesgue measure on the unit interval (Scottish Book Problem 86)

Lebesgue measure on
$\mathbb{R}$ restricted to the unit interval $[0, 1]$, the ambient measure for Problem 86.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook86Wanted.scottishBook86Measure`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook86Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook86Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html#scottish-book86-measure).

## Scottish Book Problem 86 (Banach)

The claim that for every real $M > 0$ and every
sequence $(\varphi_n)_{n \in \mathbb{N}}$ of functions $\mathbb{R} \to \mathbb{R}$ that are
almost everywhere measurable on $[0, 1]$, orthonormal in $L^2[0, 1]$ (that is,
$\int_0^1 \varphi_n \varphi_m \, dt$ is $1$ if $n = m$ and $0$ otherwise) and satisfy
$|\varphi_n(t)| \le M$ for all $n$ and all $t \in [0, 1]$, there is a sequence
$(\psi_n)_{n \in \mathbb{N}}$ of functions $\mathbb{R} \to \mathbb{R}$, almost everywhere
measurable on $[0, 1]$, orthonormal in the same sense and with $|\psi_n(t)| \le M$ for all $n$
and all $t \in [0, 1]$, such that every $\varphi_n$ equals some $\psi_m$ and $(\psi_n)$ is
complete: every $g \in L^2[0, 1]$ with $\int_0^1 \psi_n g \, dt = 0$ for all $n$ vanishes
almost everywhere on $[0, 1]$.

The case of interest in the original problem is when infinitely many functions are necessary
for the completion.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook86Wanted.ScottishBookProblem86Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook86Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook86Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html#scottish-book-problem86-claim).

## Banach's Scottish Book Problem 86 fails

The Scottish Book Problem 86 claim is false: there
are a real $M > 0$ and a sequence $(\varphi_n)_{n \in \mathbb{N}}$ of functions
$\mathbb{R} \to \mathbb{R}$, almost everywhere measurable on $[0, 1]$, orthonormal in
$L^2[0, 1]$ and with $|\varphi_n(t)| \le M$ for all $n$ and all $t \in [0, 1]$, such that there
is no sequence $(\psi_n)_{n \in \mathbb{N}}$ of functions $\mathbb{R} \to \mathbb{R}$, almost
everywhere measurable on $[0, 1]$, orthonormal in $L^2[0, 1]$ and with $|\psi_n(t)| \le M$ for
all $n$ and all $t \in [0, 1]$, that has every $\varphi_n$ as one of its terms and is complete:
every $g \in L^2[0, 1]$ with $\int_0^1 \psi_n g \, dt = 0$ for all $n$ vanishes almost
everywhere on $[0, 1]$.

## Sources

- S. Banach, Problem 86 of the Scottish Book; negative answer via A. Plichko and A. Razenkov, "On three problems from the Scottish Book connected with orthogonal systems", Colloq. Math. 70 (1996), 227–234, Proposition 3, which constructs a bounded orthogonal sequence in a Banach space densely and non-compactly embedded in a Hilbert space that admits no extension to a fundamental orthogonal sequence using elements of the Banach space. Earlier work on the problem includes S. Kaczmarz (1936) and K. S. Kazarian ("On a problem of S. Banach from the Scottish Book", Proc. Amer. Math. Soc. 110 (1990), 881–887).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook86Wanted.banach86_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook86Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook86Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html#banach86-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orthogonal systems and general orthogonal series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/hilbert-spaces/orthogonal-systems-and-general-orthogonal-series)
