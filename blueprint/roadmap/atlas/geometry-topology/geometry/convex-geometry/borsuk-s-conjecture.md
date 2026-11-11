---
declaration: section
origin: cited
lean: Metric.HasBorsukCover, Metric.setBorsukNumber, Metric.dimensionBorsukNumber, Metric.firstBorsukFailureDimension, Metric.setBorsukNumber_le_of_cover, Metric.hasBorsukCover_iff_exactUnion, Metric.hasBorsukCover_iff_closedCover, Metric.hasBorsukCover_pos
statement: formalized
proof: formalized
---

# Borsuk's conjecture

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html).

## Borsuk covers

Let $s$ be a set in an extended pseudometric space and let $k$ be a
natural number. The set $s$ has a $k$-piece Borsuk cover if there are $k$ sets whose union
contains $s$, each of extended diameter strictly smaller than that of $s$.

Formalized by `Metric.HasBorsukCover`, a definition declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#has-borsuk-cover).

## Borsuk number of a set

The Borsuk number of a set $s$ in the Euclidean space
$\mathbb{R}^n$ is the least natural number $k$ such that $s$ has a $k$-piece Borsuk cover, that
is, $s$ is covered by $k$ sets each of strictly smaller extended diameter than $s$; it is
$\infty$ if no such $k$ exists.

Formalized by `Metric.setBorsukNumber`, a definition declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#set-borsuk-number).

## Borsuk number of a Euclidean space

For a natural number $n$, the Borsuk number of the
Euclidean space $\mathbb{R}^n$ is the supremum, in $\mathbb{N} \cup \{\infty\}$, of the Borsuk
numbers of the bounded subsets of $\mathbb{R}^n$ with at least two points.

Formalized by `Metric.dimensionBorsukNumber`, a definition declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#dimension-borsuk-number).

## First Borsuk failure dimension

The first Borsuk failure dimension is the least positive
integer $n$ such that the Borsuk number of the Euclidean space $\mathbb{R}^n$ is greater than
$n + 1$, and $\infty$ if there is no such $n$.

Formalized by `Metric.firstBorsukFailureDimension`, a definition declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#first-borsuk-failure-dimension).

## A Borsuk cover bounds the Borsuk number

If a set $s$ in the Euclidean space
$\mathbb{R}^n$ has a $k$-piece Borsuk cover for a natural number $k$, then the Borsuk number of
$s$ is at most $k$.

Formalized by `Metric.setBorsukNumber_le_of_cover`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#set-borsuk-number-le-of-cover).

## Borsuk covers by subsets

For natural numbers $n$ and $k$, a set $s$ in the Euclidean
space $\mathbb{R}^n$ has a $k$-piece Borsuk cover if and only if there are subsets
$c_1, \dots, c_k$ of $s$ with $s = c_1 \cup \dots \cup c_k$, each of extended diameter strictly
smaller than that of $s$.

Formalized by `Metric.hasBorsukCover_iff_exactUnion`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#has-borsuk-cover-iff-exact-union).

## Borsuk covers by closed sets

For natural numbers $n$ and $k$, a set $s$ in the Euclidean
space $\mathbb{R}^n$ has a $k$-piece Borsuk cover if and only if there are $k$ closed subsets of
$\mathbb{R}^n$ whose union contains $s$, each of extended diameter strictly smaller than that
of $s$.

Formalized by `Metric.hasBorsukCover_iff_closedCover`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#has-borsuk-cover-iff-closed-cover).

## Borsuk covers of nonempty sets have at least one piece

Let $n$ and $k$ be natural
numbers. If a nonempty set $s$ in the Euclidean space $\mathbb{R}^n$ has a $k$-piece Borsuk
cover, then $0 < k$.

Formalized by `Metric.hasBorsukCover_pos`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#has-borsuk-cover-pos).

## Enlarging a Borsuk cover

Let $n$, $k$ and $l$ be natural numbers with $k \le l$. If a
nonempty set $s$ in the Euclidean space $\mathbb{R}^n$ has a $k$-piece Borsuk cover, then $s$ has
an $l$-piece Borsuk cover.

Repeating an existing piece enlarges the cover to the larger size.

Formalized by `Metric.hasBorsukCover_mono`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#has-borsuk-cover-mono).

## Bounds on the Borsuk number of a set

For a nonempty set $s$ in the Euclidean space
$\mathbb{R}^n$ and a natural number $k$, the Borsuk number of $s$ is at most $k$ if and only if
$s$ has a $k$-piece Borsuk cover.

Formalized by `Metric.setBorsukNumber_le_iff`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#set-borsuk-number-le-iff).

## Upper bounds on the Borsuk number of a Euclidean space

For natural numbers $n$ and $k$,
the Borsuk number of the Euclidean space $\mathbb{R}^n$ is at most $k$ if and only if every
bounded subset $s$ of $\mathbb{R}^n$ with at least two points has a $k$-piece Borsuk cover,
that is, $s$ is covered by $k$ sets, each of extended diameter strictly smaller than that of
$s$.

Formalized by `Metric.dimensionBorsukNumber_le_iff`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#dimension-borsuk-number-le-iff).

## Borsuk's conjecture in a given dimension

For a natural number $n$, Borsuk's conjecture
in dimension $n$ is the statement that the Borsuk number of the Euclidean space $\mathbb{R}^n$
is at most $n + 1$.

Equivalently, every bounded subset of $\mathbb{R}^n$ with at least two points is covered by
$n + 1$ sets, each of extended diameter strictly smaller than that of the set.

Formalized by `Metric.borsukConjectureInDimension`, a definition declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#borsuk-conjecture-in-dimension).

## When the first Borsuk failure dimension is infinite

The first Borsuk failure dimension
is $\infty$ if and only if, for every positive integer $n$, the Borsuk number of the Euclidean
space $\mathbb{R}^n$ is at most $n + 1$.

Formalized by `Metric.firstBorsukFailureDimension_eq_top_iff`, a theorem declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#first-borsuk-failure-dimension-eq-top-if).

## Two-distance sets

A set $s$ in the Euclidean space $\mathbb{R}^n$ is a two-distance set
if there are reals $0 < a < b$ such that the distance between any two distinct points of $s$ is
$a$ or $b$, and both $a$ and $b$ occur as the distance between some two points of $s$.

Formalized by `Metric.IsTwoDistanceSet`, a definition declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#is-two-distance-set).

## Two-distance Borsuk number in dimension $n$

The two-distance Borsuk number in dimension
$n$ is the supremum, taken in $\mathbb{N} \cup \{\infty\}$, of the Borsuk numbers of all bounded
two-distance sets with at least two points in the Euclidean space $\mathbb{R}^n$.

Formalized by `Metric.twoDistanceBorsukNumber`, a definition declared in [MathlibExt/Geometry/Euclidean/BorsukNumber.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BorsukNumber.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html#two-distance-borsuk-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Borsuk's conjecture](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/borsuk-s-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/convex-geometry/borsuk-s-conjecture)
