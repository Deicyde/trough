---
declaration: lemma
origin: cited
lean: KLDiv_nonneg
statement: formalized
proof: formalized
---

# Gibbs inequality

$D_{KL}(X\Vert Y) \geq 0$.

## Depends on

- [Kullback–Leibler divergence](kl-div.md)

## Proof depends on

- [log sum inequality](../../applications-of-jensens-inequality/log-sum.md)

## Proof

Apply [log sum inequality](../../applications-of-jensens-inequality/log-sum.md) on the definition.

## Lean

Formalized as [`KLDiv_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/KLDiv_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 22](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L22)
