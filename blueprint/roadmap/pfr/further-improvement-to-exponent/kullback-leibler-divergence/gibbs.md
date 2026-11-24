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

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 22](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/further_improvement.tex#L22)
