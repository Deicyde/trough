---
declaration: proposition
origin: cited
lean: pn_asymptotic
statement: formalized
proof: formalized
---

# pn-asymptotic

One has

$$
p_n = (1+o(1)) n \log n
$$

as $n \to \infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pi-alt](pi-alt.md)

## Proof

Use Corollary [pi-alt](pi-alt.md) to show that $n=\pi(p_n)\sim p_n/\log p_n$ Taking logs gives $\log n \sim \log p_n - \log\log p_n \sim \log p_n$. Multiplying these gives $p_n\sim n\log n$ from which the result follows.

## Lean

Formalized as [`pn_asymptotic`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/pn_asymptotic).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
