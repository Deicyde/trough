---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.ContainsKSunflower, MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.IsKSunflowerFree, MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.conjecture, MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.conjecture_holds, MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.Set.IsSunflower, MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.Set.IsSystem, MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.ImprovedBoundsSunflowerLemma.lowerBound, MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.ImprovedBoundsSunflowerLemma.C
statement: formalized
---

# Sunflower lemma

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html).

## Families containing a sunflower

Let $n$ and $k$ be natural numbers. A family $F$ of
subsets of $\{0, \dots, n-1\}$ contains a $k$-sunflower if some subfamily $T \subseteq F$ with
exactly $k$ members satisfies $A \cap B = C \cap D$ for all $A, B, C, D \in T$ with $A \ne B$ and
$C \ne D$, that is, all pairwise intersections of distinct members of $T$ are equal.

Formalized by `MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.ContainsKSunflower`, a definition declared in [WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#contains-ksunflower).

## Sunflower-free families

Let $n$ and $k$ be natural numbers. A family $F$ of subsets of
$\{0, \dots, n-1\}$ is $k$-sunflower-free if it does not contain a $k$-sunflower.

Formalized by `MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.IsKSunflowerFree`, a definition declared in [WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#is-ksunflower-free).

## Erdős–Szemerédi sunflower conjecture for $k \ge 4$

The proposition asserts that for every
natural number $k \ge 4$ there is a real number $c$ with $0 < c < 2$ such that, for all
sufficiently large $n$, every $k$-sunflower-free family of subsets of $\{0, \dots, n-1\}$ has at
most $c^n$ members.

The bound is required only for large $n$ because for $2^n < k$ the family of all subsets of
$\{0, \dots, n-1\}$ is $k$-sunflower-free. The case $k = 3$, proved by Naslund and Sawin, is
omitted.

Formalized by `MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#conjecture).

## The Erdős–Szemerédi sunflower bound for $k \ge 4$

For every natural number $k \ge 4$ there
is a real number $c$ with $0 < c < 2$ such that, for all sufficiently large $n$, every family of
subsets of $\{0, \dots, n-1\}$ that contains no $k$-sunflower has at most $c^n$ members. Here a
$k$-sunflower in a family is a choice of $k$ distinct members whose pairwise intersections are
all equal.

Resolved true: Proved: Bucić, He and Lee (arXiv:2610.26686, 2026, Theorem 1) show that for every
k >= 3 and n >= 1 a family of subsets of [n] with no k-sunflower has at most 3(2 - 1/(16k^3))^n
members, which gives the formalized bound c^n with c < 2 for each k >= 4 and all large n.
erdosproblems.com/857 (checked 2026-10-22) records this bound as known. The paper states that
the proof of its vector-sunflower bound (Theorem 2) was found by ChatGPT 6 Astra Pro and
verified by the authors. Source: Matija Bucić, Fankang He and Hyunwoo Lee, Proof of the
Erdős-Szemerédi sunflower conjecture, arXiv:2610.26686 (2026), https://arxiv.org/abs/2610.26686;
T. F. Bloom, Erdős Problem #857, erdosproblems.com, https://www.erdosproblems.com/857. Moved
from `OpenConjectures/Combinatorics/ErdosProblem857WeakSunflower`.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem857WeakSunflowerWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosProblem857WeakSunflowerWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#conjecture-holds).

## Sunflower

Let $r \in \mathbb{N}$ and let $S$ be a family of subsets of a type $X$. Then
$S$ is an $r$-sunflower if $S$ has exactly $r$ members (its cardinality is taken to be $0$ when
$S$ is infinite) and any two distinct members $A \ne B$ of $S$ satisfy $A \cap B = \bigcap S$,
the intersection of all members of $S$.

## Sources

- R. Alweiss, S. Lovett, K. Wu, and J. Zhang, *Improved bounds for the sunflower lemma*, Annals of Math 194 (3), 2021, Definition 1.1.

Formalized by `MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.Set.IsSunflower`, a definition declared in [WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#is-sunflower).

## Bounded-size set systems

Let $w \in \mathbb{N}$ and let $\mathcal{F}$ be a family of
subsets of a type $X$. Then $\mathcal{F}$ is a $w$-set system if every member $A \in \mathcal{F}$
has at most $w$ elements, where the size of an infinite set is taken to be $0$.

## Sources

- R. Alweiss, S. Lovett, K. Wu, and J. Zhang, *Improved bounds for the sunflower lemma*, Annals of Math 194 (3), 2021, second sentence of the introduction.

Formalized by `MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.Set.IsSystem`, a definition declared in [WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#is-system).

## Sunflower lower bound

For natural numbers $r$ and $w$ and a real number $C$, the lower
bound is the real number

$$\left(C\, r^3 \log_{1.9} w \, \log_{1.9}(\log_{1.9} w)\right)^w,$$

where $\log_{1.9} x = \ln x / \ln 1.9$, with the convention $\ln 0 = 0$.

Following the authors, logarithms are taken to base $1.9$; see the paragraph directly after
Theorem 1.4 of Alweiss, Lovett, Wu, and Zhang, *Improved bounds for the sunflower lemma*.

Formalized by `MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.ImprovedBoundsSunflowerLemma.lowerBound`, a definition declared in [WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#lower-bound).

## Sunflower constant

An unspecified real number $C$, the absolute constant in the
Alweiss–Lovett–Wu–Zhang sunflower bound (Theorem 1.4); it does not depend on $r$ or $w$.

## Sources

- R. Alweiss, S. Lovett, K. Wu, and J. Zhang, `Improved bounds for the sunflower lemma`, Annals of Math, 194 (3) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_improved_bounds_sunflower_lemma` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.ImprovedBoundsSunflowerLemma.C` is written with `def_wanted` in [WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#c).

## Alweiss–Lovett–Wu–Zhang sunflower bound

Let $C$ be the sunflower constant, a real number
not depending on $r$ or $w$. Let $r \ge 3$ and $w \ge 2$ be natural numbers, let $X$ be a finite
type, and let $\mathcal{F}$ be a $w$-set system of subsets of $X$, that is, every member of
$\mathcal{F}$ has at most $w$ elements. If $\mathcal{F}$ has at least

$$\left(C\, r^3 \log_{1.9} w \, \log_{1.9}(\log_{1.9} w)\right)^w$$

members, then some subfamily $S \subseteq \mathcal{F}$ is an $r$-sunflower: $S$ has exactly $r$
members and any two distinct members of $S$ intersect in $\bigcap S$.

This is Theorem 1.4 (main theorem, sunflowers); logarithms are to base $1.9$, as in the paper.
We require $w \ge 2$, as the paper assumes $\log \log w > 0$.

## Sources

- R. Alweiss, S. Lovett, K. Wu, and J. Zhang, `Improved bounds for the sunflower lemma`, Annals of Math, 194 (3) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_improved_bounds_sunflower_lemma` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.ImprovedBoundsSunflowerLemmaWanted.ImprovedBoundsSunflowerLemma.theorem_1_4` is written with `theorem_wanted` in [WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ImprovedBoundsSunflowerLemmaWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html#theorem-1-4).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sunflower lemma](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/sunflower-lemma)
