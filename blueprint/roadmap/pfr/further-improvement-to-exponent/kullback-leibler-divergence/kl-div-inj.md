---
declaration: lemma
origin: cited
lean: KLDiv_of_comp_inj
statement: formalized
proof: formalized
---

# Kullback–Leibler and injections

If $f:G \to H$ is an injection, then $D_{KL}(f(X)\Vert f(Y)) = D_{KL}(X\Vert Y)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kullback–Leibler divergence](kl-div.md)

## Proof

Clear from definition.

## Lean

Formalized as [`KLDiv_of_comp_inj`](https://teorth.github.io/pfr/docs/find/#doc/KLDiv_of_comp_inj).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 48](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L48)
