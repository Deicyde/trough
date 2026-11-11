---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.smallDoublingImpliesSmallTripling, MathlibExt.Combinatorics.SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.smallDoublingImpliesSmallTripling_refuted
statement: formalized
---

# Small doubling and small tripling

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/small-doubling-and-small-tripling/index.html).

## Tao's small-doubling question (AIM Problem 3.5)

The proposition that small doubling
forces small tripling uniformly in all groups: there is a function $f : \mathbb{R} \to \mathbb{R}$
such that for every group $G$, every finite nonempty subset $A \subseteq G$ and every real number
$K$, if $|A \cdot A| \le K |A|$ then $|A \cdot A \cdot A| \le f(K) |A|$. Here
$A \cdot A = \{ab : a, b \in A\}$ and $A \cdot A \cdot A = \{abc : a, b, c \in A\}$.

Formalized by `MathlibExt.Combinatorics.SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.smallDoublingImpliesSmallTripling`, a definition declared in [WantedExt/Combinatorics/SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/small-doubling-and-small-tripling/index.html#small-doubling-implies-small-tripling).

## Small doubling does not imply small tripling

There is no function
$f : \mathbb{R} \to \mathbb{R}$ such that for every group $G$, every finite nonempty subset
$A \subseteq G$ and every real number $K$ with $|A \cdot A| \le K |A|$ one has
$|A \cdot A \cdot A| \le f(K) |A|$. Here $A \cdot A = \{ab : a, b \in A\}$ and
$A \cdot A \cdot A = \{abc : a, b, c \in A\}$.

B. Green and M.-C. Chang pointed out the counterexample $A = H \cup \{x\}$ with $H$ a finite
non-normal subgroup and $x$ outside the normalizer of $H$: then $|A \cdot A|$ is comparable to
$|A|$, while $|A \cdot A \cdot A|$ can be much larger.

## Sources

- AIM workshop Recent trends in additive combinatorics (2004), problem list collected by E. Croot and V. F. Lev, https://aimath.org/WWN/additivecomb/additivecomb.pdf, Problem 3.5 (T. Tao) and Tao's comment; resolution: Tao's comment on Problem 3.5 in the AIM problem list (counterexample pointed out by B. Green and M.-C. Chang); T. Tao, Product set estimates for non-commutative groups, Combinatorica 28 (2008), 547-594, arXiv:math/0601431, comment to Problem 3.5: 'the problem as stated is false, as it follows by considering A = H ∪ {x} where H is a non-normal subgroup and x is not in the normalizer of H'; Tao's paper, Section 1 ('if A is the union of a subgroup and a point, then A · A will be small, but higher products such as A · A · A can be large') and Section 3 (A = H ∪ {x}, H a finite subgroup, x outside its normalizer: A² has size comparable to A, but A³ can be much larger), https://aimath.org/WWN/additivecomb/additivecomb.pdf.

Stated but not proved: `MathlibExt.Combinatorics.SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.smallDoublingImpliesSmallTripling_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SmallDoublingTriplingAIMCombinatoricsProblem242Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/small-doubling-and-small-tripling/index.html#small-doubling-implies-small-tripling-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Small doubling and small tripling](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/small-doubling-and-small-tripling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/small-doubling-and-small-tripling)
