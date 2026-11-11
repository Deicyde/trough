---
declaration: lemma
origin: cited
lean: rhoMinus_of_subgroup
statement: formalized
proof: formalized
---

# Rho minus of subgroup

If $H$ is a finite subgroup of $G$, then $\rho^-(U_H) = \log |A| - \log \max_t |A \cap (H+t)|$.

## Depends on

- [Rho minus](rhominus-def.md)

## Proof depends on

- [log sum inequality](../../applications-of-jensens-inequality/log-sum.md)

## Proof

For every $G$-valued random variable $T$ that is independent of $Y$,

$$
D_{KL}(U_H \Vert U_A+T) = \sum_{h\in H} \frac{1}{|H|}\log\frac{1/|H|}{\mathbf{P}[U_A+T=h]}\ge -\log(\mathbf{P}[U_A+T\in H]),
$$

by [log sum inequality](../../applications-of-jensens-inequality/log-sum.md). Then observe that

$$
-\log(\mathbf{P}[U_A+T\in H])=-\log(\mathbf{P}[U_A\in H-T])\ge -\log(\max_{t\in G} \mathbf{P}[U_A\in H+t]).
$$

This proves $\ge$.

To get the equality, let $t^*:=\arg\max_t |A \cap (H+t)|$ and observe that

$$
\rho^-(U_H)\le D_{KL}(U_H \Vert  U_A+(U_H-t^*))= \log |A| - \log \max_t|A \cap (H+t)|.
$$

## Lean

Formalized as [`rhoMinus_of_subgroup`](https://teorth.github.io/pfr/docs/find/#doc/rhoMinus_of_subgroup).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 100](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L100)
