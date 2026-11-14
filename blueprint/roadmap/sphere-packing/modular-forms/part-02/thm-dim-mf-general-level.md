---
declaration: theorem
origin: cited
lean: dim_gen_cong_levels
statement: formalized
---

# dim-mf-general-level

Let $\Gamma$ be a congruence subgroup. Then $M_k(\Gamma)$ is finite-dimensional.

## Depends on

- [Mk](../part-01/def-mk.md)
- [lvl1_dims](thm-lvl1-dims.md)

## Proof

We know that $\dim(M_k(\Gamma_1))$ is finite dimensional from the above, now this means that there is some $r_k$ such that any element of $M_k(\Gamma_1)$ vanishing at infinity to degree $> r_k$ must be zero. Now take $f \in M_k(\Gamma)$ and vanishes to degree $n$ at infinity, then consider $F = \prod_\gamma f\mid_k \gamma$ where the product is over a set of representatives of $\Gamma_1 \backslash \Gamma$. Then $F$ is a modular form of weight $k d$ where $d = [\Gamma_1: \Gamma]$ and vanishes at infinity to degree at least $n$. So if $n > r_{kd}$ then $F=0$ meaning the $f=0$.

## Lean

Stated as [`dim_gen_cong_levels`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/dim_gen_cong_levels); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 302](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L302)
