---
declaration: theorem
origin: cited
lean: Cayley.Pack.lower_le_ev, Cayley.Pack.pLower_le, Cayley.Pack.pStats_sound
statement: formalized
proof: formalized
---

# Coefficient bound

Let $p = \sum_m c_m t^m$. For $t \in [-1,1]^5$,

$$
p(t) \ge c_0 - \sum_{m \text{ with an odd exponent}} |c_m| - \sum_{\substack{m \ne 0 \text{ all exponents even}\\ c_m < 0}} |c_m|,
\qquad
|p(t) - c_0| \le \sum_{m \ne 0} |c_m|.
$$

## Depends on

- [pe](../def-pe.md)

## Proof

For $|t_i| \le 1$ every monomial lies in $[-1, 1]$, and a monomial with only even exponents lies in $[0, 1]$.

## Lean

Formalized as [`Cayley.Pack.lower_le_ev`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.lower_le_ev), [`Cayley.Pack.pLower_le`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pLower_le), [`Cayley.Pack.pStats_sound`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.pStats_sound).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 29](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/polybounds.tex#L29)
