---
declaration: section
origin: cited
lean: MetaMathlibExt.AreFiniteArithmeticProgressionsWithCommonDifference, MetaMathlibExt.vosper_eq_iff
statement: formalized
proof: formalized
---

# Vosper's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/vosper-s-theorem/index.html).

## Arithmetic progressions with a common difference

Let $G$ be an additive commutative
monoid and let $A$ and $B$ be finite subsets of $G$. We say that $A$ and $B$ are arithmetic
progressions with a common difference if there are $d, a, b \in G$ such that
$A = \{a + nd : n \in \mathbb{N},\ n < |A|\}$ and $B = \{b + nd : n \in \mathbb{N},\ n < |B|\}$,
where $nd$ is the sum of $n$ copies of $d$. The two progressions may have different initial terms
and different lengths.

## Sources

- Fabián Arias, Jerson Borja, and Samuel Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences 26 (2023), Article 23.8.1, Theorem [Vosper] `theo_Vosper` condition (iii), lines 256–267, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.tex>: "`A` and `B` are arithmetic progressions with the same common difference".

Formalized by `MetaMathlibExt.AreFiniteArithmeticProgressionsWithCommonDifference`, a definition declared in [MathlibExt/Combinatorics/Additive/CommonDifferenceProgressions.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/CommonDifferenceProgressions.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/vosper-s-theorem/index.html#are-finite-arithmetic-progressions-with).

## Vosper's theorem

Let $p$ be a prime and let $A$ and $B$ be nonempty subsets of
$\mathbb{Z}/p\mathbb{Z}$ whose sumset $A + B = \{a + b : a \in A, b \in B\}$ is not all of
$\mathbb{Z}/p\mathbb{Z}$. Then $|A + B| = |A| + |B| - 1$ if and only if one of the following
holds: (i) $\min(|A|, |B|) = 1$; (ii) $|A + B| = p - 1$ and there is an element
$c \in \mathbb{Z}/p\mathbb{Z}$ such that the complement of $A + B$ is $\{c\}$ and $B$ is the
complement of $c - A = \{c - a : a \in A\}$; or (iii) $A$ and $B$ are arithmetic progressions
with the same common difference, that is, there are $d, a_0, b_0 \in \mathbb{Z}/p\mathbb{Z}$
with $A = \{a_0 + n d : 0 \le n < |A|\}$ and $B = \{b_0 + n d : 0 \le n < |B|\}$.

## Sources

- Fabián Arias, Jerson Borja, and Samuel Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences 26 (2023), Article 23.8.1, Theorem [Vosper] `theo_Vosper`, lines 256–267, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.tex>.

Formalized by `MetaMathlibExt.vosper_eq_iff`, a theorem declared in [MathlibExt/Combinatorics/Additive/VosperTheorem.lean, line 833](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/VosperTheorem.lean#L833). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/vosper-s-theorem/index.html#vosper-eq-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vosper's theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/vosper-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/vosper-s-theorem)
