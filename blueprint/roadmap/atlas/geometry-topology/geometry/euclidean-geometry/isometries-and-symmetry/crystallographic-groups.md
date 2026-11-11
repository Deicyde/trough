---
declaration: section
origin: cited
lean: MathlibExt.Geometry.CrystallographicShared.E, MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.E, MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.IsOrientationPreservingIsom, MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.AffOPEquivalent, MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.crystallographicCountOP, MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.crystallographicCountOPOnly, MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.space_groups, MathlibExt.Geometry.WallpaperGroupsWanted.Geometry.WallpaperGroupsProblem.E
statement: formalized
---

# Crystallographic groups

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html).

## Euclidean space $\mathbb{R}^d$

For a natural number $d$, $E(d)$ is the $d$-dimensional
Euclidean space $\mathbb{R}^d$, with coordinates indexed by $0, 1, \dots, d - 1$ and the standard
inner product.

Formalized by `MathlibExt.Geometry.CrystallographicShared.E`, an abbreviation declared in [WantedExt/Geometry/CrystallographicShared.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/CrystallographicShared.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#e).

## Euclidean space $\mathbb{R}^d$ for the space-group problem

For a natural number $d$, this
is the $d$-dimensional real Euclidean space $\mathbb{R}^d$ with its standard inner product.

Formalized by `MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.E`, an abbreviation declared in [WantedExt/Geometry/SpaceGroupsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpaceGroupsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#e-2).

## Orientation-preserving isometry

An affine isometry of the Euclidean space $\mathbb{R}^d$
is orientation-preserving if its linear part has positive determinant.

Formalized by `MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.IsOrientationPreservingIsom`, a definition declared in [WantedExt/Geometry/SpaceGroupsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpaceGroupsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#is-orientation-preserving-isom).

## Orientation-preserving affine equivalence

Two subgroups $G_1$ and $G_2$ of the group of
affine isometries of the Euclidean space $\mathbb{R}^d$ are orientation-preserving affinely
equivalent if there is an affine bijection $\varphi$ of $\mathbb{R}^d$ whose linear part has
positive determinant such that $\{\varphi g \varphi^{-1} : g \in G_1\} = G_2$ as sets of affine
maps of $\mathbb{R}^d$.

Formalized by `MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.AffOPEquivalent`, a definition declared in [WantedExt/Geometry/SpaceGroupsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpaceGroupsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#aff-opequivalent).

## Number of orientation-preserving affine classes of crystallographic groups

For a natural
number $d$, this is the number, in $\mathbb{N} \cup \{\infty\}$, of classes of $d$-dimensional
crystallographic groups under orientation-preserving affine equivalence. Here a crystallographic
group is a subgroup $G$ of the group of affine isometries of $\mathbb{R}^d$ that is discrete (for
every point $x$ and every $\varepsilon > 0$ only finitely many $g \in G$ satisfy
$\operatorname{dist}(g x, x) \le \varepsilon$) and contains translations by $d$ linearly
independent vectors.

Formalized by `MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.crystallographicCountOP`, a definition declared in [WantedExt/Geometry/SpaceGroupsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpaceGroupsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#crystallographic-count-op).

## Number of orientation-preserving affine classes of orientation-preserving crystallographic groups

**Number of orientation-preserving affine classes of orientation-preserving crystallographic
groups.** For a natural number $d$, this is the number, in $\mathbb{N} \cup \{\infty\}$, of classes
under orientation-preserving affine equivalence of those $d$-dimensional crystallographic groups
all of whose elements are orientation-preserving isometries. Here a crystallographic group is a
subgroup $G$ of the group of affine isometries of $\mathbb{R}^d$ that is discrete (for every
point $x$ and every $\varepsilon > 0$ only finitely many $g \in G$ satisfy
$\operatorname{dist}(g x, x) \le \varepsilon$) and contains translations by $d$ linearly
independent vectors.

Formalized by `MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.crystallographicCountOPOnly`, a definition declared in [WantedExt/Geometry/SpaceGroupsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpaceGroupsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#crystallographic-count-oponly).

## The 230 space groups

In dimension $3$ there are exactly $230$ classes of crystallographic
groups under orientation-preserving affine equivalence, exactly $219$ classes of crystallographic
groups under affine equivalence (conjugation by an arbitrary affine bijection of $\mathbb{R}^3$),
and exactly $65$ classes under orientation-preserving affine equivalence of crystallographic
groups all of whose elements are orientation-preserving isometries.

## Sources

- E. Fedorov, 'Симметрія правильныхъ системъ фигуръ' (Symmetry of regular systems of figures), Trans. Min. Soc. St. Petersburg 28 (1891) 1–146; A. Schoenflies, *Krystallsysteme und Krystallstructur*, Teubner 1891, independently. Listed as §94 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `space_groups_230` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.SpaceGroupsWanted.Geometry.SpaceGroupsProblem.space_groups` is written with `theorem_wanted` in [WantedExt/Geometry/SpaceGroupsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SpaceGroupsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#space-groups).

## Euclidean space for wallpaper groups

For a natural number $d$, the $d$-dimensional real
Euclidean space $\mathbb{R}^d$ with its standard inner product.

Formalized by `MathlibExt.Geometry.WallpaperGroupsWanted.Geometry.WallpaperGroupsProblem.E`, an abbreviation declared in [WantedExt/Geometry/WallpaperGroupsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/WallpaperGroupsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#e-3).

## There are exactly 17 wallpaper groups

Call a group $G$ of isometries of the Euclidean
plane $\mathbb{R}^2$ crystallographic if it is discrete, meaning that for every point $x$ and
every $\varepsilon > 0$ only finitely many $g \in G$ satisfy
$\operatorname{dist}(g x, x) \le \varepsilon$, and it contains translations by two linearly
independent vectors. Call two such groups $G_1$ and $G_2$ affinely equivalent if some invertible
affine map $\varphi$ of $\mathbb{R}^2$ satisfies $\{\varphi g \varphi^{-1} : g \in G_1\} = G_2$.
Up to affine equivalence there are exactly $17$ crystallographic groups of the plane.

## Sources

- G. Pólya, 'Über die Analogie der Kristallsymmetrie in der Ebene', Z. Kristallogr. 60 (1924) 278–282; P. Niggli, 'Die Flächensymmetrien homogener Diskontinuen', Z. Kristallogr. 60 (1924) 283–298. Listed as §94 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `wallpaper_groups_17` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.WallpaperGroupsWanted.Geometry.WallpaperGroupsProblem.there_are_17_wallpaper_groups` is written with `theorem_wanted` in [WantedExt/Geometry/WallpaperGroupsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/WallpaperGroupsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html#there-are-17-wallpaper-groups).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Crystallographic groups](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/crystallographic-groups)
