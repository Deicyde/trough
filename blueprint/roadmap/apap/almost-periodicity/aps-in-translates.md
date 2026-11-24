---
declaration: lemma
origin: cited
lean: AlmostPeriodicity.just_the_triangle_inequality
statement: formalized
proof: formalized
---

# aps_in_translates

Let $A\subseteq G$ and $f:G\to \mathbb{C}$. Let $\epsilon>0$ and $m\geq 1$ and $k\geq 1$. Let

$$
L = \{{\vec{a}}\in A^k : \|\tfrac{1}{k}\sum_{i=1}^k f(x-a_i) - \mu_A\ast f\|_{2m}
\leq \epsilon \| f\|_{2m}\}.
$$

If $t\in G$ is such that ${\vec{a}}\in L$ and ${\vec{a}}+(t,\ldots,t)\in L$ then

$$
\| \tau_t(\mu_A\ast f)-\mu_A\ast f\|_{2m}\leq 2\epsilon \|f\|_{2m}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`AlmostPeriodicity.just_the_triangle_inequality`](https://yaeldillies.github.io/apap/docs/find/#doc/AlmostPeriodicity.just_the_triangle_inequality).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 92](https://github.com/YaelDillies/apap/blob/b401f6e22417e6dbe6f87d6620571ea6c513aed3/blueprint/src/chapter/ap.tex#L92)
