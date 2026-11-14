---
declaration: theorem
origin: cited
lean: ModularForm.dimension_level_one
statement: formalized
proof: formalized
---

# lvl1_dims

Let $k \in \mathbb{Z}$ with $k \ge 0$ and even. Then $\dim M_k(\Gamma_1) = \lfloor k / 12 \rfloor$ if $k \equiv 2 \mod 12$ and $\dim M_k(\Gamma_1) = \lfloor k / 12 \rfloor + 1$ if $k \not\equiv 2 \mod 12$.

## Depends on

- [holomorphic-modular-form](../part-01/def-holomorphic-modular-form.md)
- [disc-E4E6](lemma-disc-e4e6.md)
- [disc-definition](../part-01/def-disc-definition.md)

## Proof

First we note that for $2 < k$ we have $\dim(M_k(\Gamma_1)) = 1 + \dim S_k(\Gamma_1)$. This follows since we know the $E_k$ are in $M_k$ so by scaling appropriately, any non-cuspform $f \in M_k$ we would have $f - a E_k \in S_k$ for some $a$.

Next, note that $S_k(\Gamma_1)$ is isomorphic to $M_{k-12}(\Gamma_1)$, since if $f \in S_k$ then $f/ \Delta$ is now a modular form (using the product expansion of $\Delta$ and its non-vanishing on $\mathfrak{H}$) of weight $k-12$. Note its important that $f$ is a cuspform so that the quotient by $\Delta$ is a modular form.

So we only need to know the dimensions of $M_k(\Gamma_1)$ for $0 \le k \le 12$. For $k = 0$ we have $\dim M_0(\Gamma_1) = 1$ by [Theorem nonpos_wt](thm-nonpos-wt.md). For $k = 4$ we have $\dim M_4(\Gamma_1) = 1$ since if there was a cuspform $f$ of weight $4$ then $f/ \Delta$ would be a modular form of negative weight, i.e. zero, so $f=0$. Similarly for $k=6,8,10$. For $k=12$ we have $\dim S_{12}(\Gamma_1) = 1$ since the discriminant form is a cusp form of weight $12$ and any other cusp form of weight $12$ would be a scalar multiple of $\Delta$ (since their ratio would be a modular form of weight $0$). So we have $\dim M_{12}(\Gamma_1) = 2$.

Finally we need to check that $\dim M_2(\Gamma_1) = 0$. Firstly, there can't be any cuspforms here by the same argument as above. So we need to check that there are no modular forms of weight $2$. If we did have one, call it $f$ then $f^2$ would be a non-cuspform of weight $4$ and so $f^2 = a E_4$, where in fact $a=a_0(f)^2$ (since $(f^2-a_0(f)E_4)$ is now a cuspform of weight $4$ which means its zero). Similarly, $f^3 = a_0(f)^3 E_6$. But now taking powers to make them weight $12$ forms we see that $a_0(f)^6(E_4^3 - E_6^2) = 0 = 1728 a_0(f)^6 \Delta$ but $a_0(f) \ne 0$ (since its assumed to not be a cuspform), this would mean $\Delta =0$ which we know can't happen.

## Lean

Formalized as [`ModularForm.dimension_level_one`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularForm.dimension_level_one).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 269](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L269)
