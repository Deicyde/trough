---
declaration: lemma
origin: cited
lean: MIPRE.exists_sum_star_mul_self, MIPRE.sum_star_mul_self_pad, MIPRE.Halmos.isPVMIn_proj, MIPRE.DilationAncilla, MIPRE.exists_pvm_dilation_ge, MIPRE.exists_pvm_dilation
statement: formalized
proof: formalized
---

# Projective dilation against a fixed state, in a star-ordered ring

Let $R$ be a star-ordered $*$-algebra and $\{Q^x_a\}_a$ a finite family of POVMs in $R$. There are a finite ancilla $T$, a basis state $t_0 \in T$ and projective measurements $\{P^x_{a}\}_a$ in $M_T(R)$ whose $(t_0, t_0)$ entries are $Q^x_a$, for every $x$.

## Depends on

- [Commutation-preserving dilation](../part-02/lem-co-dilation.md)

## Proof

In a star-ordered ring a nonnegative element is a finite sum of elements $z^* z$, so each POVM is a Kraus family $\{Z^x_{a,i}\}$ with $\sum_{a,i} (Z^x_{a,i})^* Z^x_{a,i} = {I}$; pad the number of terms to a common bound. The Halmos unitary of its Naimark column dilates it to orthogonal projections; coarse-grained over $i$, they compress at the fixed basis vector to $Q^x_a$. Neither finite dimension nor a square root is used; the matrix proof's unitary extension needed both.

## Lean

Formalized as [`MIPRE.exists_sum_star_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_sum_star_mul_self), [`MIPRE.sum_star_mul_self_pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_star_mul_self_pad), [`MIPRE.Halmos.isPVMIn_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.isPVMIn_proj), [`MIPRE.DilationAncilla`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.DilationAncilla), [`MIPRE.exists_pvm_dilation_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_pvm_dilation_ge), [`MIPRE.exists_pvm_dilation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_pvm_dilation).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1971](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1971)
