---
declaration: lemma
origin: cited
lean: rho_of_translate
statement: formalized
proof: formalized
---

# Rho invariant

For any $s \in G$, $\rho(X+s) = \rho(X)$.

## Depends on

- [Rho functional](rho-def.md)

## Proof depends on

- [Kullback–Leibler and injections](../kullback-leibler-divergence/kl-div-inj.md)

## Proof

Observe that by [Kullback–Leibler and injections](../kullback-leibler-divergence/kl-div-inj.md),

$$
\inf_T D_{KL}(X\Vert U_A+T)=\inf_T D_{KL}(X+s\Vert U_A+T+s)=\inf_{T'} D_{KL}(X+s\Vert U_A+T').
$$

## Lean

Formalized as [`rho_of_translate`](https://teorth.github.io/pfr/docs/find/#doc/rho_of_translate).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 137](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L137)
