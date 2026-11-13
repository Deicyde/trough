---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.HasMonochromaticAP, MathlibExt.Combinatorics.OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.offDiagonalVanDerWaerdenPolynomial, MathlibExt.Combinatorics.OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.offDiagonalVanDerWaerdenPolynomial_refuted, MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.HasMonoAP, MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.ForcesThreeK, MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.vanDerWaerdenThreeSubexponential, MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.vanDerWaerdenThreeSuperpolynomial, MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.vanDerWaerdenThreeSubexponential_holds
statement: formalized
---

# Van der Waerden numbers W(3, k)

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html).

## Monochromatic arithmetic progression

Let $c$ be a colouring of the natural numbers with
the two colours true and false, let $b$ be a colour and let $l, N$ be natural numbers. Then $c$
has a monochromatic progression of colour $b$ and length $l$ in $\{1, \dots, N\}$ when there are
natural numbers $a \ge 1$ and $d \ge 1$ with $a + (l - 1) d \le N$, where $l - 1$ is read as $0$
when $l = 0$, such that $c(a + j d) = b$ for every $j < l$.

Formalized by `MathlibExt.Combinatorics.OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.HasMonochromaticAP`, a definition declared in [WantedExt/Combinatorics/OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#has-monochromatic-ap).

## Polynomial growth of the off-diagonal van der Waerden numbers (claim)

There are natural
numbers $C$ and $A$ such that for every $k \ge 1$, every colouring of the natural numbers in red
and blue has a red $3$-term or a blue $k$-term arithmetic progression $a, a + d, \dots$ with
$a \ge 1$, $d \ge 1$ and all terms in $\{1, \dots, C k^A\}$. Equivalently, the van der Waerden
number $W(3, k)$, the least $n$ such that every red/blue colouring of $\{1, \dots, n\}$ has a red
$3$-term or a blue $k$-term arithmetic progression, satisfies $W(3, k) \le C k^A$ for every
$k \ge 1$.

This is the AIM question (Graph Ramsey theory, Problem 43) stated as a claim.

Formalized by `MathlibExt.Combinatorics.OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.offDiagonalVanDerWaerdenPolynomial`, a definition declared in [WantedExt/Combinatorics/OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#off-diagonal-van-der-waerden-polynomial).

## The off-diagonal van der Waerden numbers are not polynomially bounded

There are no
natural numbers $C$ and $A$ such that for every $k \ge 1$, every colouring of the natural numbers
in red and blue has a red $3$-term or a blue $k$-term arithmetic progression $a, a + d, \dots$
with $a \ge 1$, $d \ge 1$ and all terms in $\{1, \dots, C k^A\}$.

Equivalently, the van der Waerden number $W(3, k)$, the least $n$ such that every red/blue
colouring of $\{1, \dots, n\}$ has a red $3$-term or a blue $k$-term arithmetic progression, is
not bounded by $C k^A$ for any constants $C$ and $A$. Green proved that for some constant $c > 0$
and all sufficiently large $k$, $W(3, k) \ge k^{b(k)}$ with
$b(k) = c (\log k / \log \log k)^{1/3}$, which tends to infinity (the colours of his colouring are
swapped relative to this statement, which is symmetric).

## Sources

- AIM workshop Graph Ramsey theory, problem list, https://www.overleaf.com/read/mnvcscjjysvg, Problem 43 (same text: AimPL, Graph Ramsey Theory, section 25, http://aimpl.org/graphramsey/1/); resolution: B. Green, New lower bounds for van der Waerden numbers, Forum Math. Pi 10 (2022), e18, arXiv:2102.01543, abstract and main theorem: there is a red-blue colouring of [N] with no blue 3-term progression and no red progression of length e^{C (log N)^{3/4} (log log N)^{1/4}}, so w(3, k) ≥ k^{b(k)} with b(k) = c (log k / log log k)^{1/3} → ∞; Z. Hunter (arXiv:2111.01099) improved this to w(3, k) ≥ k^{c log k / log log k}, https://doi.org/10.1017/fmp.2022.12.

Stated but not proved: `MathlibExt.Combinatorics.OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.offDiagonalVanDerWaerdenPolynomial_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/OffDiagonalVanDerWaerdenGrowthAIMCombinatoricsProblem90Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#off-diagonal-van-der-waerden-polynomial-2).

## Monochromatic arithmetic progressions in an initial interval

Let $c$ be a red/blue
colouring of the natural numbers, given as a map to the Booleans ($\mathrm{true}$ is red,
$\mathrm{false}$ is blue), let $b$ be a colour and let $\ell$ and $N$ be natural numbers. Then $c$
has an $\ell$-term arithmetic progression of colour $b$ inside $\{1, \dots, N\}$ if there are
natural numbers $a$ and $d > 0$ such that for every $i < \ell$ we have $1 \le a + id \le N$ and
$c(a + id) = b$.

Formalized by `MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.HasMonoAP`, a definition declared in [WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#has-mono-ap).

## Intervals forcing the van der Waerden number $W(3, k)$

For natural numbers $N$ and $k$,
the interval $\{1, \dots, N\}$ forces $W(3, k)$ if every red/blue colouring of the natural numbers
has, inside $\{1, \dots, N\}$, a red $3$-term arithmetic progression or a blue $k$-term arithmetic
progression (progressions have common difference $d > 0$). Equivalently $W(3, k) \le N$, where the
van der Waerden number $W(3, k)$ is the least $n$ such that every red/blue colouring of
$\{1, \dots, n\}$ has a red $3$-term or a blue $k$-term arithmetic progression.

Formalized by `MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.ForcesThreeK`, a definition declared in [WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#forces-three-k).

## Subexponential upper bound for $W(3, k)$ (statement)

Write $W(3, k)$ for the van der
Waerden number: the least $n$ such that every red/blue colouring of $\{1, \dots, n\}$ has a red
$3$-term or a blue $k$-term arithmetic progression (progressions have common difference
$d > 0$). Say that $N$ forces $W(3, k)$ if every red/blue colouring of $\{1, \dots, N\}$ has a red
$3$-term or a blue $k$-term arithmetic progression. This is the proposition that there is a real
constant $c < 1$ such that for all sufficiently large natural numbers $k$ some natural number
$N < \exp(k^c)$ forces $W(3, k)$. Equivalently, $W(3, k) < \exp(k^c)$ for all large $k$.

Formalized by `MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.vanDerWaerdenThreeSubexponential`, a definition declared in [WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#van-der-waerden-three-subexponential).

## Green's superpolynomial lower bound for $W(3, k)$ (statement)

Write $W(3, k)$ for the van
der Waerden number: the least $n$ such that every red/blue colouring of $\{1, \dots, n\}$ has a
red $3$-term or a blue $k$-term arithmetic progression (progressions have common difference
$d > 0$). Say that $N$ forces $W(3, k)$ if every red/blue colouring of $\{1, \dots, N\}$ has a red
$3$-term or a blue $k$-term arithmetic progression. This is the proposition that there is a real
constant $c > 0$ such that for all sufficiently large natural numbers $k$, no natural number
$N < \exp\bigl(c (\log k)^{4/3} / (\log \log k)^{1/3}\bigr)$ forces $W(3, k)$. Equivalently,
$W(3, k) \ge \exp\bigl(c (\log k)^{4/3} / (\log \log k)^{1/3}\bigr)$ for all large $k$.

Formalized by `MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.vanDerWaerdenThreeSuperpolynomial`, a definition declared in [WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#van-der-waerden-three-superpolynomial).

## Schoen's subexponential upper bound for $W(3, k)$

Write $W(3, k)$ for the van der Waerden
number: the least $n$ such that every red/blue colouring of $\{1, \dots, n\}$ has a red $3$-term
or a blue $k$-term arithmetic progression (progressions have common difference $d > 0$). Say that
$N$ forces $W(3, k)$ if every red/blue colouring of $\{1, \dots, N\}$ has a red $3$-term or a
blue $k$-term arithmetic progression. There is a real constant $c < 1$ such that for all
sufficiently large natural numbers $k$ some natural number $N < \exp(k^c)$ forces $W(3, k)$.
Equivalently, $W(3, k) < \exp(k^c)$ for all large $k$.

Schoen proved $W(3, k) \le \exp(O(k^{1-\delta}))$ for an absolute constant $\delta > 0$, which gives
this statement; erdosproblems.com/721 records Schoen as the first to show it. The best known bound
is now $\exp(O((\log k)^9))$, via Bloom and Sisask.

## Sources

- T. F. Bloom, Erdős Problems, Problem #721, https://www.erdosproblems.com/721 (status SOLVED); resolution: T. Schoen, A subexponential upper bound for van der Waerden numbers W(3, k), Electron. J. Combin. 28 (2021), Paper 2.34; B. Green, New lower bounds for van der Waerden numbers, Forum Math. Pi 10 (2022), e18, Schoen's abstract: N ≤ exp(O(k^{1-c})) for an absolute c > 0 whenever {1, …, N} splits into a 3-AP-free part and a k-AP-free part; abstract of arXiv:2102.01543 (Green): w(3, k) ≥ k^{b(k)} with b(k) = c (log k / log log k)^{1/3}; erdosproblems.com/721: both specific challenges of Erdős have been met, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i2p34.

Stated but not proved: `MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.vanDerWaerdenThreeSubexponential_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#van-der-waerden-three-subexponential-hol).

## Green's superpolynomial lower bound for $W(3, k)$

Write $W(3, k)$ for the van der Waerden
number: the least $n$ such that every red/blue colouring of $\{1, \dots, n\}$ has a red $3$-term
or a blue $k$-term arithmetic progression (progressions have common difference $d > 0$). Say that
$N$ forces $W(3, k)$ if every red/blue colouring of $\{1, \dots, N\}$ has a red $3$-term or a
blue $k$-term arithmetic progression. There is a real constant $c > 0$ such that for all
sufficiently large natural numbers $k$, no natural number
$N < \exp\bigl(c (\log k)^{4/3} / (\log \log k)^{1/3}\bigr)$ forces $W(3, k)$. Equivalently,
$W(3, k) \ge \exp\bigl(c (\log k)^{4/3} / (\log \log k)^{1/3}\bigr)$ for all large $k$.

Green's colouring has no $3$-term progression in one colour and no long progression in the other;
it disproves Graham's guess $W(3, k) \ll k^2$. Hunter improved the bound to
$\exp(c (\log k)^2 / \log \log k)$ (erdosproblems.com/721).

## Sources

- T. F. Bloom, Erdős Problems, Problem #721, https://www.erdosproblems.com/721 (status SOLVED); resolution: T. Schoen, A subexponential upper bound for van der Waerden numbers W(3, k), Electron. J. Combin. 28 (2021), Paper 2.34; B. Green, New lower bounds for van der Waerden numbers, Forum Math. Pi 10 (2022), e18, Schoen's abstract: N ≤ exp(O(k^{1-c})) for an absolute c > 0 whenever {1, …, N} splits into a 3-AP-free part and a k-AP-free part; abstract of arXiv:2102.01543 (Green): w(3, k) ≥ k^{b(k)} with b(k) = c (log k / log log k)^{1/3}; erdosproblems.com/721: both specific challenges of Erdős have been met, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i2p34.

Stated but not proved: `MathlibExt.Combinatorics.VanDerWaerdenThreeKErdosProblem721Wanted.vanDerWaerdenThreeSuperpolynomial_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/VanDerWaerdenThreeKErdosProblem721Wanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html#van-der-waerden-three-superpolynomial-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van der Waerden numbers W(3, k)](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/van-der-waerden-numbers-w-3-k)
