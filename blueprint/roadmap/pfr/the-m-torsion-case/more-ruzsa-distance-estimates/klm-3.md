---
declaration: lemma
origin: cited
lean: kvm_ineq_III
statement: formalized
proof: formalized
---

# Kaimonovich–Vershik–Madiman inequality, III

If $n \geq 1$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then

$$
d\left[X; \sum_{i=1}^n Y_i\right] \leq d\left[X; Y_1\right] + \frac{1}{2}\left(\mathbb{H}\left[ \sum_{i=1}^n Y_i\right] - \mathbb{H}[Y_1]\right).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)

## Proof

From [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md) one has

$$
\mathbb{H}\left[-X + \sum_{i=1}^n Y_i\right] \leq \mathbb{H}[ - X + Y_1 ] + \mathbb{H}\left[ \sum_{i=1}^n Y_i \right] - \mathbb{H}[Y_1].
$$

The claim then follows from [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md) and some elementary algebra.

## Lean

Formalized as [`kvm_ineq_III`](https://teorth.github.io/pfr/docs/find/#doc/kvm_ineq_III).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 102](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L102)
