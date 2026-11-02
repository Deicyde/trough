---
declaration: lemma
origin: cited
lean: kvm_ineq_II
statement: formalized
proof: formalized
---

# Kaimonovich–Vershik–Madiman inequality, II

If $n \geq 1$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then

$$
d[X; \sum_{i=1}^n Y_i] \leq 2 \sum_{i=1}^n d[X; Y_i].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kaimonovich–Vershik–Madiman inequality](klm-1.md)
- [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md)
- [Distance controls entropy difference](../../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)

## Proof

Applying [Kaimonovich–Vershik–Madiman inequality](klm-1.md) with all the $Y_i$ replaced by $-Y_i$, and using [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md) and [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md), we obtain after some rearranging

$$
d[X; \sum_{i=1}^n Y_i] + \frac{1}{2} (\mathbb{H}[\sum_{i=1}^n Y_i] - \mathbb{H}[X]) \leq \sum_{i=1}^n \left(d[X;Y_i] + \frac{1}{2} (\mathbb{H}[Y_i] - \mathbb{H}[X])\right).
$$

From [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md) we have

$$
\mathbb{H}[\sum_{i=1}^n Y_i] \geq \mathbb{H}[Y_i]
$$

for all $i$; subtracting $\mathbb{H}[X]$ and averaging, we conclude that

$$
\mathbb{H}[\sum_{i=1}^n Y_i] - \mathbb{H}[X] \geq \frac{1}{n} \sum_{i=1}^n \mathbb{H}[Y_i] - \mathbb{H}[X]
$$

and thus

$$
d[X; \sum_{i=1}^n Y_i] \leq \sum_{i=1}^n d[X;Y_i] + \frac{n-1}{2n} (\mathbb{H}[Y_i] - \mathbb{H}[X]).
$$

From [Distance controls entropy difference](../../entropic-ruzsa-calculus/part-01/ruzsa-diff.md) we have

$$
\mathbb{H}[Y_i] - \mathbb{H}[X] \leq 2 d[X;Y_i].
$$

Since $0 \leq \frac{n-1}{2n} \leq \frac{1}{2}$, the claim follows.

## Lean

Formalized as [`kvm_ineq_II`](https://teorth.github.io/pfr/docs/find/#doc/kvm_ineq_II).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 84](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L84)
