---
declaration: theorem
origin: cited
lean: groupCohomology.inflationRestriction, groupCohomology.inflation_restriction_mono, groupCohomology.inflation_restriction_exact
statement: formalized
---

# inflation restriction sequence

Let $S$ be a normal subgroup of a group $G$ and let $n$ be a positive integer. Assume that for all natural numbers $0 \lt i < n$ we have $H^{i}(S,M) \cong 0$. Then the following sequence is exact:

$$
0 \to H^{n}(G/S, M^S) \to H^{n}(G,M) \to H^{n}(S,M),
$$

where the first map is inflation and the second is restriction.

## Depends on

- [up](../dimension-shifting/def-up.md)
- [coind₁' invariants trivial cohomology](../dimension-shifting/cor-coind1-invariants-trivial-cohomology.md)
- [inflation restriction naturality](../group-cohomology-and-homology/lem-inflation-restriction-naturality.md)

## Proof

This is already in Mathlib for $n=1$. Assume the result is true for some $n\ge 1$; we will prove it for $n+1$ by dimension-shifting.

Let $M$ be a representation such that $H^i(S,M)\cong 0$ for all $0 < i < n+1$. This implies $H^i(S,\mathrm{up}(M)) \cong 0$ for all $0 < i < n$. Hence by the inductive hypothesis the following sequence is exact:

$$
0 \to H^n( G/S, \mathrm{up}(M)^S) \to H^n(G, \mathrm{up}(M)) \to H^n(S,\mathrm{up}(M)).
$$

Recall that we have a short exact sequence of representations of $G$:

$$
0 \to M \to \mathrm{coind}_1'(M) \to \mathrm{up}(M) \to 0.
$$

Since $0 < 1 < n+1$, our condition on $M$ implies $H^1(S,M) \cong 0$, so by taking $S$-invariants we obtain a short exact sequence of $G/S$-modules:

$$
0 \to M^S \to \mathrm{coind}_1'(M)^S \to \mathrm{up}(M)^S \to 0.
$$

By [coind₁' invariants trivial cohomology](../dimension-shifting/cor-coind1-invariants-trivial-cohomology.md), $\mathrm{coind}_1'(M)^S$ has trivial cohomology, so we have an isomorphism

$$
H^n(G/S, \mathrm{up}(M)^S) \to H^{n+1}(G/S, M^S).
$$

We now have a diagram where the horizontal maps are inflation and restriction maps and the vertical maps are dimension-shifting isomorphisms.

$$
\begin{matrix}
0 &\to& H^{n}(G/S, \mathrm{up}(M)^S) &\to &H^{n}(G,\mathrm{up}(M)) & \to & H^n(S,\mathrm{up}(M)) \\
&   &   \downarrow              &    &  \downarrow         &     &  \downarrow  \\
0 &\to& H^{n+1}(G/S, M^S) &\to &H^{n+1}(G,M) & \to & H^{n+1}(S,M).
\end{matrix}
$$

The diagram commutes by [inflation restriction naturality](../group-cohomology-and-homology/lem-inflation-restriction-naturality.md). The first row is exact by the inductive hypothesis. Therefore the second row is also exact.

## Lean

Stated as [`groupCohomology.inflationRestriction`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.inflationRestriction), [`groupCohomology.inflation_restriction_mono`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.inflation_restriction_mono), [`groupCohomology.inflation_restriction_exact`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.inflation_restriction_exact); the blueprint marks no proof of it as formalized.

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1310](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1310)
