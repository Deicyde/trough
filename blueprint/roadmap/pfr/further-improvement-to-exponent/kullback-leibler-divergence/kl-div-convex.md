---
declaration: lemma
origin: cited
lean: KLDiv_of_convex
statement: formalized
proof: formalized
---

# Convexity of Kullback–Leibler

If $S$ is a finite set, $\sum_{s \in S} w_s = 1$ for some non-negative $w_s$, and ${\bf P}(X=x) = \sum_{s\in S} w_s {\bf P}(X_s=x)$, ${\bf P}(Y=x) = \sum_{s\in S} w_s {\bf P}(Y_s=x)$ for all $x$, then

$$
D_{KL}(X\Vert Y) \le \sum_{s\in S} w_s D_{KL}(X_s\Vert Y_s).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kullback–Leibler divergence](kl-div.md)
- [log sum inequality](../../applications-of-jensens-inequality/log-sum.md)

## Proof

For each $x$, replace $\log \frac{\mathbf{P}(X_s=x)}{\mathbf{P}(Y_s=x)}$ in the definition with $\log \frac{w_s\mathbf{P}(X_s=x)}{w_s\mathbf{P}(Y_s=x)}$ for each $s$, and apply [log sum inequality](../../applications-of-jensens-inequality/log-sum.md).

## Lean

Formalized as [`KLDiv_of_convex`](https://teorth.github.io/pfr/docs/find/#doc/KLDiv_of_convex).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 38](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L38)
