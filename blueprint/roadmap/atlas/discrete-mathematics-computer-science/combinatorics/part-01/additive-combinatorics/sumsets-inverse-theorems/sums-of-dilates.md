---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.transcendentalDilateLowerBound, MathlibExt.Combinatorics.TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.transcendentalDilateLowerBound_holds
statement: formalized
---

# Sums of dilates

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-of-dilates/index.html).

## Lower bound for sums of transcendental dilates

There is a real constant $c > 0$ such that
for every real number $\alpha$ transcendental over $\mathbb{Q}$ and every finite set $A$ of real
numbers,

$$e^{c\sqrt{\log |A|}}\,|A| \le |A + \alpha \cdot A|,$$

where $A + \alpha \cdot A = \{a + \alpha b : a, b \in A\}$.

Formalized by `MathlibExt.Combinatorics.TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.transcendentalDilateLowerBound`, a definition declared in [WantedExt/Combinatorics/TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-of-dilates/index.html#transcendental-dilate-lower-bound).

## Conlon–Lim theorem on sums of transcendental dilates

There is a real constant $c > 0$
such that for every real number $\alpha$ transcendental over $\mathbb{Q}$ and every finite set $A$
of real numbers,

$$e^{c\sqrt{\log |A|}}\,|A| \le |A + \alpha \cdot A|,$$

where $A + \alpha \cdot A = \{a + \alpha b : a, b \in A\}$.

Resolved true: Conlon and Lim prove that there is an absolute constant `c > 0` such that `|A + λ·A|
≥ e^{c √(log |A|)} |A|` for every finite `A ⊆ ℝ` and every transcendental `λ ∈ ℝ`, best possible up
to the constant `c` by the construction of Konyagin and Łaba.

## Sources

- Problems presented at the workshop on recent trends in additive combinatorics, collected by E. Croot and V. F. Lev, AIM workshop problem list, Problem 4.8 (I. Łaba), https://aimath.org/WWN/additivecomb/additivecomb.pdf; resolution: D. Conlon and J. Lim, Sums of transcendental dilates, Bull. London Math. Soc. 55 (2023) 2400-2406, arXiv:2212.10128, abstract and main theorem, https://arxiv.org/abs/2212.10128.

Stated but not proved: `MathlibExt.Combinatorics.TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.transcendentalDilateLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TranscendentalDilateSumsetAIMCombinatoricsProblem264Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-of-dilates/index.html#transcendental-dilate-lower-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of dilates](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-of-dilates/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-of-dilates)
