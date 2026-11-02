---
declaration: lemma
origin: cited
lean: kaimanovich_vershik
statement: formalized
proof: formalized
---

# Kaimanovich-Vershik-Madiman inequality

Suppose that $X, Y, Z$ are independent $G$-valued random variables. Then

$$
\mathbb{H}[X + Y + Z] - \mathbb{H}[X + Y] \leq \mathbb{H}[Y+ Z] - \mathbb{H}[Y].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Submodularity](../../shannon-entropy-inequalities/part-01/submodularity.md)
- [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)

## Proof

From [Submodularity](../../shannon-entropy-inequalities/part-01/submodularity.md) we have

$$
\mathbb{H}[X, X + Y+ Z] + \mathbb{H}[Z, X + Y+ Z] \geq \mathbb{H}[X, Z, X + Y+ Z] + \mathbb{H}[X + Y+ Z].
$$

However, using Lemmas [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md), [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md) repeatedly we have $\mathbb{H}[X, X + Y+ Z] = \mathbb{H}[X, Y+ Z] = \mathbb{H}[X] + \mathbb{H}[Y+ Z]$, $\mathbb{H}[Z, X + Y + Z] = \mathbb{H}[Z, X + Y] = \mathbb{H}[Z] + \mathbb{H}[X + Y]$ and $\mathbb{H}[X, Z, X + Y+ Z] = \mathbb{H}[X, Y, Z] = \mathbb{H}[X] + \mathbb{H}[Y] + \mathbb{H}[Z]$. The claim then follows from a calculation.

## Lean

Formalized as [`kaimanovich_vershik`](https://teorth.github.io/pfr/docs/find/#doc/kaimanovich_vershik).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 242](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L242)
