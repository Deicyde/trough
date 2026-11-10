---
declaration: lemma
origin: cited
lean: ent_sub_zsmul_sub_ent_le
statement: formalized
proof: formalized
---

# Sums of dilates II

Let $X,Y$ be independent $G$-valued random variables, and let $a$ be an integer. Then

$$
\mathbb{H}[X-aY] - \mathbb{H}[X] \leq 4 |a| d[X;Y].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Flipping a sign](sign-flip.md)
- [Sums of dilates I](sum-dilate-i.md)

## Proof

From [Kaimanovich-Vershik-Madiman inequality](../../entropic-ruzsa-calculus/part-02/kv.md) one has

$$
\mathbb{H}[Y-X+X'] - \mathbb{H}[Y-X] \leq \mathbb{H}[Y+X'] - \mathbb{H}[Y] = \mathbb{H}[Y+X] - \mathbb{H}[Y]
$$

which by [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md) gives

$$
\mathbb{H}[X-Y-X'] -\mathbb{H}[X] \leq d[X;Y] + d[X;-Y]
$$

and hence by [Flipping a sign](sign-flip.md)

$$
\mathbb{H}[X-Y-X'] - \mathbb{H}[X] \leq 4d[X;Y].
$$

From [Sums of dilates I](sum-dilate-i.md) we then have

$$
\mathbb{H}[X-(a\pm 1)Y] \leq \mathbb{H}[X-aY] + 4 d[X;Y]
$$

and the claim now follows by an induction on $|a|$.

## Lean

Formalized as [`ent_sub_zsmul_sub_ent_le`](https://teorth.github.io/pfr/docs/find/#doc/ent_sub_zsmul_sub_ent_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 147](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L147)
