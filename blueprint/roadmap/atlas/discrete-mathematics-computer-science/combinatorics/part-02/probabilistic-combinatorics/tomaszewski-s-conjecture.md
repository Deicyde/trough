---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.TomaszewskiRandomSignedSumAMR127Problem0002Wanted.tomaszewskiConjecture, MathlibExt.Combinatorics.TomaszewskiRandomSignedSumAMR127Problem0002Wanted.tomaszewskiConjecture_holds
statement: formalized
---

# Tomaszewski's conjecture

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/tomaszewski-s-conjecture/index.html).

## Tomaszewski's conjecture

The statement that for every natural number $n$ and every
vector $a = (a_1, \dots, a_n) \in \mathbb{R}^n$ with $a_1^2 + \dots + a_n^2 = 1$, at least half of
the $2^n$ sign vectors $x \in \{-1, 1\}^n$ satisfy $|a_1 x_1 + \dots + a_n x_n| \le 1$.

## Sources

- O'Donnell, Open Problems in Analysis of Boolean Functions, Problem 2. A sign vector is a map `x : Fin n → Bool`, with `true` read as `1` and `false` as `-1`.

Formalized by `MathlibExt.Combinatorics.TomaszewskiRandomSignedSumAMR127Problem0002Wanted.tomaszewskiConjecture`, a definition declared in [WantedExt/Combinatorics/TomaszewskiRandomSignedSumAMR127Problem0002Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/TomaszewskiRandomSignedSumAMR127Problem0002Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/tomaszewski-s-conjecture/index.html#tomaszewski-conjecture).

## Tomaszewski's conjecture holds

For every natural number $n$ and every vector
$a = (a_1, \dots, a_n) \in \mathbb{R}^n$ with $a_1^2 + \dots + a_n^2 = 1$, at least half of the
$2^n$ sign vectors $x \in \{-1, 1\}^n$ satisfy $|a_1 x_1 + \dots + a_n x_n| \le 1$; equivalently,
for a uniformly random sign vector $x$ this inequality holds with probability at least $1/2$.

## Sources

- R. O'Donnell, Open Problems in Analysis of Boolean Functions (2012), arXiv:1204.6447, Problem 2 (Tomaszewski's Conjecture); resolution: N. Keller and O. Klein, Proof of Tomaszewski's conjecture on randomly signed sums, Adv. Math. 407 (2022), 108558, arXiv:2006.16834, main theorem (Section 1): for X = ∑ aᵢxᵢ with ∑ aᵢ² = 1 and independent uniform xᵢ ∈ {-1, 1}, Pr[|X| ≤ 1] ≥ 1/2, https://arxiv.org/abs/2006.16834.

Stated but not proved: `MathlibExt.Combinatorics.TomaszewskiRandomSignedSumAMR127Problem0002Wanted.tomaszewskiConjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/TomaszewskiRandomSignedSumAMR127Problem0002Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/TomaszewskiRandomSignedSumAMR127Problem0002Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/tomaszewski-s-conjecture/index.html#tomaszewski-conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tomaszewski's conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/tomaszewski-s-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/tomaszewski-s-conjecture)
