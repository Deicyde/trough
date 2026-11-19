---
declaration: theorem
origin: cited
lean: KummerCriterion
statement: formalized
proof: formalized
---

# kummer-criterion

Let $p$ be an odd prime. Then

$$
p\ \text{is regular}
\quad\Longleftrightarrow\quad
\forall k,\ 1\le k,\ 2k\le p-3,\quad
p\nmid\operatorname{num}(B_{2k}).
$$

## Depends on

- [regular-prime](../../introduction/overview/def-regular-prime.md)
- [dvd-h-iff-bernoulli-units](../the-total-class-number-criterion/thm-dvd-h-iff-bernoulli-units.md)

## Proof

By [Definition regular-prime](../../introduction/overview/def-regular-prime.md), $p$ is regular if and only if $p$ is coprime to the class number of the $p$th cyclotomic field; since $p$ is prime, this is equivalent to $p\nmid h(K)$. By [Theorem dvd-h-iff-bernoulli-units](../the-total-class-number-criterion/thm-dvd-h-iff-bernoulli-units.md), the negation of $p\mid h(K)$ is exactly the assertion that no $k$ in the range $1\le k$, $2k\le p-3$ satisfies $p\mid\operatorname{num}(B_{2k})$, which is the displayed universal nondivisibility.

## Lean

Formalized as [`KummerCriterion`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion).

## Sources

- [Kummer's criterion blueprint: subsections/final.tex, line 93](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/final.tex#L93)
