---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_three, MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_four, MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_five, MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_six, MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.rothNumberNat_five_to_fourteen
statement: formalized
---

# Small values of cap set sizes and Roth numbers

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers/index.html).

## Largest cap set in dimension three

Let $\mathbb{F}_3$ be the field with three elements.
The largest subset of $\mathbb{F}_3^3$ containing no three-term arithmetic progression, that is,
no elements $a, b, c$ of the subset with $a + c = 2b$ and $a \neq b$, has exactly $9$ elements.

Over $\mathbb{F}_3$ these subsets are exactly the caps: sets with no three distinct collinear
points.

## Sources

- exhaustive search; OEIS A090245; listed in leansolving/SqueezeBench `SqueezeBench/Problems/CapSet/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers/index.html#cap-set-dim-three).

## Largest cap set in dimension four

Let $\mathbb{F}_3$ be the field with three elements.
The largest subset of $\mathbb{F}_3^4$ containing no three-term arithmetic progression, that is,
no elements $a, b, c$ of the subset with $a + c = 2b$ and $a \neq b$, has exactly $20$ elements.

Over $\mathbb{F}_3$ these subsets are exactly the caps: sets with no three distinct collinear
points.

## Sources

- G. Pellegrino, *Sul massimo ordine delle calotte in S₄,₃*, Matematiche (Catania) 25 (1970), 149–157; OEIS A090245; listed in SqueezeBench `SqueezeBench/Problems/CapSet/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers/index.html#cap-set-dim-four).

## Largest cap set in dimension five

Let $\mathbb{F}_3$ be the field with three elements.
The largest subset of $\mathbb{F}_3^5$ containing no three-term arithmetic progression, that is,
no elements $a, b, c$ of the subset with $a + c = 2b$ and $a \neq b$, has exactly $45$ elements.

Over $\mathbb{F}_3$ these subsets are exactly the caps: sets with no three distinct collinear
points.

## Sources

- Y. Edel, S. Ferret, I. Landjev, and L. Storme, *The classification of the largest caps in AG(5,3)*, J. Combin. Theory Ser. A 99 (2002), 95–110; OEIS A090245; listed in SqueezeBench `SqueezeBench/Problems/CapSet/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers/index.html#cap-set-dim-five).

## Largest cap set in dimension six

Let $\mathbb{F}_3$ be the field with three elements.
The largest subset of $\mathbb{F}_3^6$ containing no three-term arithmetic progression, that is,
no elements $a, b, c$ of the subset with $a + c = 2b$ and $a \neq b$, has exactly $112$ elements.

Over $\mathbb{F}_3$ these subsets are exactly the caps: sets with no three distinct collinear
points.

## Sources

- A. Potechin, *Maximal caps in AG(6,3)*, Des. Codes Cryptogr. 46 (2008), 243–259; OEIS A090245; listed in SqueezeBench `SqueezeBench/Problems/CapSet/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.capSet_dim_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers/index.html#cap-set-dim-six).

## Roth numbers from five to fourteen

For a natural number $n$, let $r_3(n)$ be the largest
size of a subset of $\{0, 1, \dots, n - 1\}$ containing no three-term arithmetic progression,
that is, no elements $a, b, c$ of the subset with $a + c = 2b$ and $a \neq b$. Then the values
$r_3(5), r_3(6), \dots, r_3(14)$ are $4, 4, 4, 4, 5, 5, 6, 6, 7, 8$, in this order.

## Sources

- OEIS A003002; listed in SqueezeBench `SqueezeBench/Problems/Roth/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.Additive.ThreeAPFreeValuesWanted.rothNumberNat_five_to_fourteen` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/ThreeAPFreeValuesWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers/index.html#roth-number-nat-five-to-fourteen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Small values of cap set sizes and Roth numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/small-values-of-cap-set-sizes-and-roth-numbers)
