---
declaration: section
origin: cited
lean: MathlibExt.Algebra.KoetheNilLeftIdealsWanted.IsNilLeftIdeal, MathlibExt.Algebra.KoetheNilLeftIdealsWanted.conjecture, MathlibExt.Algebra.KoetheNilLeftIdealsWanted.conjecture_refuted
statement: formalized
---

# Köthe's conjecture

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/k-the-s-conjecture/index.html).

## Nil left ideal

A left ideal $I$ of a ring $R$ is nil if each of its elements is
nilpotent: for every $x \in I$ there is a natural number $n$ with $x^n = 0$.

Formalized by `MathlibExt.Algebra.KoetheNilLeftIdealsWanted.IsNilLeftIdeal`, a definition declared in [WantedExt/Algebra/KoetheNilLeftIdealsWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/KoetheNilLeftIdealsWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/k-the-s-conjecture/index.html#is-nil-left-ideal).

## Köthe's conjecture

The statement that for every ring $R$ (associative, with identity)
and all nil left ideals $I$ and $J$ of $R$, the sum $I + J$ is again a nil left ideal.

Formalized by `MathlibExt.Algebra.KoetheNilLeftIdealsWanted.conjecture`, a definition declared in [WantedExt/Algebra/KoetheNilLeftIdealsWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/KoetheNilLeftIdealsWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/k-the-s-conjecture/index.html#conjecture).

## Köthe's conjecture is false

There exist a ring $R$ (associative, with identity) and nil left
ideals $I$ and $J$ of $R$ (left ideals all of whose elements are nilpotent) such that the sum
$I + J$ is not nil.

Adamczewski, Böhmler and Marczinzik (arXiv:2609.07996, 2026; Lean 4 machine-checked by
Adamczewski) build, over any countable field $F$, a nil algebra $N$ such that $M_2(F1 + N)$ has
two nil left ideals with non-nil sum. Greenfeld, King and Vendramin (arXiv:2609.15080) give an
independent refutation.

## Sources

- Tom Adamczewski, Bernhard Böhmler and René Marczinzik, A counterexample to Köthe's conjecture and a question of Rowen, arXiv:2609.07996 (2026), https://arxiv.org/abs/2609.07996; Be'eri Greenfeld, G. King and Leandro Vendramin, The Köthe conjecture via point modules, arXiv:2609.15080 (2026), https://arxiv.org/abs/2609.15080.

Stated but not proved: `MathlibExt.Algebra.KoetheNilLeftIdealsWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Algebra/KoetheNilLeftIdealsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/KoetheNilLeftIdealsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/k-the-s-conjecture/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Köthe's conjecture](https://deicyde.github.io/atlas-lean/roadmap/Algebra/associative-algebras/k-the-s-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/associative-algebras/k-the-s-conjecture)
