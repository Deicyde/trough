---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsStable.and
---

# locally_inter

If $P, Q$ are stable classes of processes then $(P\cap Q)_{\mathrm{loc}} = P_{\mathrm{loc}}\cap Q_{\mathrm{loc}}$.

## Depends on

- [Local property](def-locally.md)
- [stable](def-stable.md)

## Proof depends on

- [localizingSequence_min](lem-localizingsequence-min.md)

## Proof

The forward direction is trivial so we only provide proof for the reverse.

Suppose that $X \in P_{\mathrm{loc}}\cap Q_{\mathrm{loc}}$. Then, there exists localizing sequences $(\tau_n)_{n \in \mathbb{N}}$ and $(\sigma_n)_{n \in \mathbb{N}}$ such that $X^{\tau_n} \mathbb{I}_{\tau_n > 0}\in P$ and $X^{\sigma_n} \mathbb{I}_{\sigma_n > 0} \in Q$. Consequently, by the stability of $P$,

$$
X^{\sigma_n \wedge \tau_n} \mathbb{I}_{\sigma_n \wedge \tau_n > 0} = (X^{\tau_n} \mathbb{I}_{\tau_n > 0})^{\sigma_n \wedge \tau_n} \mathbb{I}_{\sigma_n \wedge \tau_n > 0} \in P.
$$

Similarly, by the stability of $Q$, $X^{\sigma_n \wedge \tau_n} \mathbb{I}_{\sigma_n \wedge \tau_n > 0} \in Q$. Thus, as $\sigma_n \wedge \tau_n$ is a localizing sequence by Lemma [localizingSequence_min](lem-localizingsequence-min.md) and $X^{\sigma_n \wedge \tau_n} \mathbb{I}_{\sigma_n \wedge \tau_n > 0} \in P \cap Q$ for all $n$, it follows that $X \in (P \cap Q)_{\mathrm{loc}}$

## Lean

Formalized as [`ProbabilityTheory.IsStable.and`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsStable.and).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 152](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L152)
