---
declaration: theorem
origin: cited
lean: AlmostPeriodicity.almost_periodicity
statement: formalized
proof: formalized
---

# $L_p$ almost periodicity

Let $\epsilon\in (0,1]$ and $m\geq 1$. Let $K\geq 2$ and $A,S\subseteq G$ with $\lvert A+S\rvert\leq K\lvert A\rvert$. Let $f:G\to \mathbb{C}$. There exists $T\subseteq G$ such that

$$
\lvert T\rvert \geq K^{-512m\epsilon^{-2}}\lvert S\rvert
$$

such that for any $t\in T$ we have

$$
\| \tau_t(\mu_A\ast f)-\mu_A\ast f\|_{2m}\leq \epsilon \| f\|_{2m}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [random_approx_expect](random-approx-expect.md)
- [lots_of_diagonals](lots-of-diagonals.md)
- [aps_in_translates](aps-in-translates.md)

## Proof

Test.

## Lean

Formalized as [`AlmostPeriodicity.almost_periodicity`](https://yaeldillies.github.io/apap/docs/find/#doc/AlmostPeriodicity.almost_periodicity).

## Sources

- [Kelley-Meka bound blueprint: chapter/ap.tex, line 126](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/ap.tex#L126)
