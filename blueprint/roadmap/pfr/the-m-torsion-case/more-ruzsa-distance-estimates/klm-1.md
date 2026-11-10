---
declaration: lemma
origin: cited
lean: kvm_ineq_I
statement: formalized
proof: formalized
---

# Kaimonovich–Vershik–Madiman inequality

If $n \geq 0$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then

$$
\mathbb{H}\left[X + \sum_{i=1}^n Y_i\right] - \mathbb{H}[X] \leq \sum_{i=1}^n \left(\mathbb{H}[X+Y_i] - \mathbb{H}[X]\right).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md)

## Proof

This is trivial for $n=0,1$, while the $n=2$ case is [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md). Now suppose inductively that $n > 2$, and the claim was already proven for $n-1$. By a further application of [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md) one has

$$
\mathbb{H}\left[X + \sum_{i=1}^n Y_i\right] -  \mathbb{H}\left[X + \sum_{i=1}^{n-1} Y_i\right] \leq \mathbb{H}[X+Y_n] - \mathbb{H}[X].
$$

By induction hypothesis one has

$$
\mathbb{H}\left[X + \sum_{i=1}^{n-1} Y_i\right] - \mathbb{H}[X] \leq \sum_{i=1}^{n-1} \mathbb{H}[X+Y_i] - \mathbb{H}[X].
$$

Summing the two inequalities, we obtain the claim.

## Lean

Formalized as [`kvm_ineq_I`](https://teorth.github.io/pfr/docs/find/#doc/kvm_ineq_I).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 73](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L73)
