---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.agree, MIPRE.LowDegree.prob_agree_le_totalDegree, MIPRE.LowDegree.prob_agree_le_individualDegree, MIPRE.LowDegree.card_agree_le_of_natDegree
statement: formalized
proof: formalized
---

# Schwartz–Zippel

Let $f \neq g : \mathbb{F}_q^m \to \mathbb{F}_q$ be polynomials of total degree at most $d$. Then $\Pr_{x \sim \mathbb{F}_q^m}[ f(x) = g(x) ] \leq d/q$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Mathlib's `MvPolynomial.schwartz_zippel_totalDegree` is the statement for one nonzero polynomial and a product of arbitrary finite subsets; apply it to $f - g$ with every subset all of $\mathbb{F}_q$.

## Lean

Formalized as [`MIPRE.LowDegree.agree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.agree), [`MIPRE.LowDegree.prob_agree_le_totalDegree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.prob_agree_le_totalDegree), [`MIPRE.LowDegree.prob_agree_le_individualDegree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.prob_agree_le_individualDegree), [`MIPRE.LowDegree.card_agree_le_of_natDegree`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.card_agree_le_of_natDegree).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7231](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7231)
