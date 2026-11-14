---
declaration: theorem
origin: cited
lean: KummerCriterion.voronoi_congruence_mod_p_strong
statement: formalized
proof: formalized
---

# voronoi-congruence

Let $p \ge 5$ be a prime, $a$ an integer prime to $p$, and $k$ a positive even index with $(p-1)\nmid k$. Then

$$
(a^{k}-1)\,B_k \;\equiv\;
k\,a^{k-1} \sum_{j=0}^{p-1} j^{\,k-1}\left\lfloor \frac{ja}{p}\right\rfloor
\pmod{p}.
$$

## Depends on

- [vonstaudt-p-integral](../numerators-p-adic-congruences-and-von-staudt-cla/lem-vonstaudt-p-integral.md)

## Proof

This is Voronoi's congruence (see e.g. (ireland-rosen, Chapter 15)). Writing $ja = p\lfloor ja/p \rfloor + r_j$ with $r_j$ the residue of $ja$, summing $r_j^k$ over $j$ and expanding by the binomial theorem identifies the two sides modulo $p$, using Faulhaber's formula for power sums and the von Staudt–Clausen integrality ([Lemma vonstaudt-p-integral](../numerators-p-adic-congruences-and-von-staudt-cla/lem-vonstaudt-p-integral.md)) to control the Bernoulli denominators of the lower-order terms.

## Lean

Formalized as [`KummerCriterion.voronoi_congruence_mod_p_strong`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.voronoi_congruence_mod_p_strong).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 196](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L196)
